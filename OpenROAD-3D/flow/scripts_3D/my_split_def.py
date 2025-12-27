import os
import math
import re


def _parse_units_scale(def_lines):
    """
    从 'UNITS DISTANCE MICRONS <scale> ;' 解析出 scale（如 1000）。
    解析失败则返回 1000。
    """
    for ln in def_lines:
        s = ln.strip()
        if s.startswith("UNITS DISTANCE MICRONS"):
            m = re.search(r"UNITS\s+DISTANCE\s+MICRONS\s+(\d+)\s*;", s)
            if m:
                return int(m.group(1))
    return 1000


def _find_row_block(def_lines):
    """
    找到 ROW block 的 [start, end) 区间，并按“语句”收集原始 row 语句（每条可能跨多行）。
    兼容：
      ROW ...\n
       ;\n
    """
    n = len(def_lines)
    start = None
    end = None
    row_stmts = []

    i = 0
    while i < n:
        if def_lines[i].lstrip().startswith("ROW "):
            start = i
            break
        i += 1

    if start is None:
        return None, None, []

    i = start
    while i < n:
        s = def_lines[i].lstrip()

        if s.startswith("ROW "):
            buf = [def_lines[i]]
            i += 1
            while i < n:
                buf.append(def_lines[i])
                if ";" in def_lines[i]:
                    i += 1
                    break
                i += 1
            row_stmts.append(buf)
            continue

        if def_lines[i].strip() == "" or def_lines[i].strip() == ";":
            i += 1
            continue

        end = i
        break

    if end is None:
        end = n

    return start, end, row_stmts


def _row_stmt_first_row_line(row_stmt_lines):
    for ln in row_stmt_lines:
        if ln.lstrip().startswith("ROW "):
            return ln
    return ""


def _normalize_row_stmt_to_single_line_with_semicolon(row_stmt_lines):
    """
    bottom.def 要求：ROW 规则要带分号。
    把多行 ROW 语句规范化成单行并补 ' ;\\n'。
    """
    first = _row_stmt_first_row_line(row_stmt_lines).rstrip("\n")
    if not first:
        return ""

    first = first.rstrip()
    if first.endswith(";"):
        first = first[:-1].rstrip()
    return first + " ;\n"


def generate_upper_rows(orig_row_main_lines, units_scale=1000, new_site="asap7sc6t", new_h=0.216):
    """
    upper.def：只替换 ROW block。
    生成 6T rows（new_h 默认按微米给，自动换算到 DEF units）。
    """
    if not orig_row_main_lines:
        return []

    def parse_row_main_line(line):
        # ROW <rowName> <site> <x> <y> <orient> DO <nx> BY <ny> STEP <sx> <sy> ...
        parts = line.strip().split()
        if len(parts) < 6 or parts[0] != "ROW":
            raise ValueError(f"Cannot parse ROW line: {line!r}")

        # 关键：不要用“提取第一个数字”的方式（CORE_ROW_0 会干扰）
        x = float(parts[3])
        y = float(parts[4])

        do_match = re.search(r"\bDO\s+(\d+)\b", line)
        num_sites = int(do_match.group(1)) if do_match else 100

        step_match = re.search(r"\bSTEP\s+([-+]?\d+\.?\d*)\b", line)
        step_x = float(step_match.group(1)) if step_match else 54.0

        return x, y, num_sites, step_x

    x0, y0, num_sites, step_x = parse_row_main_line(orig_row_main_lines[0])
    _, y_last, _, _ = parse_row_main_line(orig_row_main_lines[-1])

    if len(orig_row_main_lines) > 1:
        _, y1, _, _ = parse_row_main_line(orig_row_main_lines[1])
        orig_pitch = abs(y1 - y0)
    else:
        orig_pitch = 270.0  # 0.27um * 1000（兜底）

    total_height = abs(y_last - y0) + orig_pitch

    new_h_units = float(new_h) * units_scale if float(new_h) < 10.0 else float(new_h)
    if new_h_units <= 0:
        raise ValueError(f"new_h must be > 0, got {new_h}")

    new_count = int(math.ceil(total_height / new_h_units))

    new_rows = []
    x0i = int(round(x0))
    base_y = float(y0)
    step_xi = int(round(step_x))

    for i in range(new_count):
        cur_y = int(round(base_y + i * new_h_units))
        orient = "N" if i % 2 == 0 else "FS"
        new_rows.append(
            f"ROW ROW_{i} {new_site} {x0i} {cur_y} {orient} DO {num_sites} BY 1 STEP {step_xi} 0 ;\n"
        )

    return new_rows


def _find_components_block(def_lines):
    """返回 (start, end, header_line, end_line, body_lines[start+1:end-1])，区间为 [start,end)"""
    n = len(def_lines)
    start = end = None

    i = 0
    while i < n:
        if def_lines[i].lstrip().startswith("COMPONENTS"):
            start = i
            break
        i += 1
    if start is None:
        return None, None, None, None, []

    i = start + 1
    while i < n:
        if def_lines[i].lstrip().startswith("END COMPONENTS"):
            end = i + 1
            break
        i += 1
    if end is None:
        return start, None, def_lines[start], None, def_lines[start + 1 :]

    header = def_lines[start]
    end_line = def_lines[end - 1]
    body = def_lines[start + 1 : end - 1]
    return start, end, header, end_line, body


def _split_component_statements(component_body_lines):
    """
    将 COMPONENTS body 按语句（从 '-' 开始，到含 ';' 结束）切分。
    返回 list[list[str]]，每个元素是一条组件语句的原始多行。
    """
    stmts = []
    buf = None

    for ln in component_body_lines:
        s = ln.lstrip()
        if s.startswith("-"):
            if buf:
                stmts.append(buf)
            buf = [ln]
            if ";" in ln:
                stmts.append(buf)
                buf = None
            continue

        if buf is not None:
            buf.append(ln)
            if ";" in ln:
                stmts.append(buf)
                buf = None
        else:
            # body 里可能有空行/注释等：保留为“独立语句”，两边都写回
            stmts.append([ln])

    if buf:
        stmts.append(buf)

    return stmts


def _classify_component_stmt(stmt_lines):
    """
    返回 ('bottom'|'upper'|'all')。
    规则参考 split_cts_def.py：根据 master/class 名是否包含 bottom/upper。
    """
    first = ""
    for ln in stmt_lines:
        if ln.lstrip().startswith("-"):
            first = ln.strip()
            break
    if not first:
        return "all"

    parts = first.split()
    # 典型：- <instName> <masterName> + ...
    if len(parts) < 3:
        return "all"

    master = parts[2].lower()
    if "bottom" in master:
        return "bottom"
    if "upper" in master:
        return "upper"
    return "all"


def _find_nets_block(def_lines):
    """返回 NETS 的 [start,end)；找不到返回 (None,None)"""
    n = len(def_lines)
    start = end = None

    for i in range(n):
        if def_lines[i].lstrip().startswith("NETS"):
            start = i
            break
    if start is None:
        return None, None

    for j in range(start + 1, n):
        if def_lines[j].lstrip().startswith("END NETS"):
            end = j + 1
            break

    return start, end


def _rewrite_def(lines, *, row_repl=None, comps_repl=None, drop_nets=True):
    """
    按 block 级别重写：
      - 可替换 ROW block
      - 可替换 COMPONENTS block
      - 可删除 NETS block（参考 split_cts_def.py 的做法）
    """
    row_start, row_end, _ = _find_row_block(lines)
    comps_start, comps_end, _, _, _ = _find_components_block(lines)
    nets_start, nets_end = _find_nets_block(lines)

    out = []
    i = 0
    n = len(lines)
    while i < n:
        if row_repl is not None and row_start is not None and i == row_start:
            out.extend(row_repl)
            i = row_end
            continue

        if comps_repl is not None and comps_start is not None and comps_end is not None and i == comps_start:
            out.extend(comps_repl)
            i = comps_end
            continue

        if drop_nets and nets_start is not None and nets_end is not None and i == nets_start:
            i = nets_end
            continue

        out.append(lines[i])
        i += 1

    return out


def split_3dic_def():
    results_dir = os.environ.get("RESULTS_DIR")
    if not results_dir:
        print("ERROR: RESULTS_DIR not set.")
        return

    input_def = os.path.join(results_dir, "4_1_cts.def")
    print(f"[*] Processing {input_def}...")

    with open(input_def, "r", encoding="utf-8") as f:
        lines = f.readlines()

    units_scale = _parse_units_scale(lines)

    # ---- ROW blocks ----
    row_start, row_end, row_stmts = _find_row_block(lines)
    if row_start is None:
        print("ERROR: No ROW block found in DEF.")
        return

    row_main_lines = []
    normalized_orig_rows = []
    for stmt in row_stmts:
        main = _row_stmt_first_row_line(stmt)
        if main:
            row_main_lines.append(main)
        norm = _normalize_row_stmt_to_single_line_with_semicolon(stmt)
        if norm:
            normalized_orig_rows.append(norm)

    upper_rows = generate_upper_rows(
        row_main_lines,
        units_scale=units_scale,
        new_site="asap7sc6t",
        new_h=0.216,
    )

    # ---- COMPONENTS split (参考 split_cts_def.py) ----
    comps_start, comps_end, comps_header, comps_end_line, comps_body = _find_components_block(lines)
    comps_repl_bottom = None
    comps_repl_upper = None

    if comps_start is not None and comps_end is not None:
        stmts = _split_component_statements(comps_body)

        bottom_body = []
        upper_body = []
        bottom_cnt = 0
        upper_cnt = 0

        for stmt in stmts:
            cls = _classify_component_stmt(stmt)
            if cls in ("bottom", "all"):
                bottom_body.extend(stmt)
                if cls == "bottom":
                    bottom_cnt += 1
                elif any(ln.lstrip().startswith("-") for ln in stmt):
                    # 'all' 组件也计入 COMPONENTS 数量（更符合 DEF 语义）
                    bottom_cnt += 1

            if cls in ("upper", "all"):
                upper_body.extend(stmt)
                if cls == "upper":
                    upper_cnt += 1
                elif any(ln.lstrip().startswith("-") for ln in stmt):
                    upper_cnt += 1

        # 重建 COMPONENTS block（更新计数）
        comps_repl_bottom = [f"COMPONENTS {bottom_cnt} ;\n"] + bottom_body + [comps_end_line]
        comps_repl_upper = [f"COMPONENTS {upper_cnt} ;\n"] + upper_body + [comps_end_line]

    # ---- write bottom.def ----
    bottom_lines = _rewrite_def(
        lines,
        row_repl=normalized_orig_rows,   # bottom：ROW 规范化并补分号
        comps_repl=comps_repl_bottom,    # bottom：组件拆分
        drop_nets=True,                  # 参考 split_cts_def.py：去掉 NETS
    )
    with open(os.path.join(results_dir, "bottom.def"), "w", encoding="utf-8") as f:
        f.writelines(bottom_lines)

    # ---- write upper.def ----
    upper_lines = _rewrite_def(
        lines,
        row_repl=upper_rows,             # upper：只替换 ROW block
        comps_repl=comps_repl_upper,     # upper：组件拆分
        drop_nets=True,                  # 参考 split_cts_def.py：去掉 NETS
    )
    with open(os.path.join(results_dir, "upper.def"), "w", encoding="utf-8") as f:
        f.writelines(upper_lines)

    print("[*] Done.")
    print(f"[*] ROW block replaced: [{row_start}, {row_end})")
    print(f"[*] bottom.def rows: {len(normalized_orig_rows)} (normalized with semicolons)")
    print(f"[*] upper.def rows: {len(upper_rows)} (6T re-distributed)")
    if comps_start is not None and comps_end is not None:
        print(f"[*] COMPONENTS block rewritten: [{comps_start}, {comps_end})")
    nets_start, nets_end = _find_nets_block(lines)
    if nets_start is not None and nets_end is not None:
        print(f"[*] NETS block dropped: [{nets_start}, {nets_end})")


if __name__ == "__main__":
    split_3dic_def()