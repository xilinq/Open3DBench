import os
import math
import re


def _parse_units_scale(def_lines):
    for ln in def_lines:
        s = ln.strip()
        if s.startswith("UNITS DISTANCE MICRONS"):
            m = re.search(r"UNITS\s+DISTANCE\s+MICRONS\s+(\d+)\s*;", s)
            if m:
                return int(m.group(1))
    return 1000


def _find_row_block(def_lines):
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


def _parse_core_box(def_lines, *, units_scale):
    """
    DEF 中 FE_CORE_BOX_* 是 REAL（通常是微米），需要转换为 DEF database units：
      units_value = microns_value * units_scale
    返回 (llx,lly,urx,ury) in DEF units 或 None。
    """
    llx = lly = urx = ury = None

    # 只捕获：1) 完整 key  2) 数值；避免 group 索引被 (LL|UR)/(X|Y) 干扰
    pat = re.compile(
        r"^DESIGN\s+"
        r"(FE_CORE_BOX_(?:LL|UR)_(?:X|Y))"
        r"\s+REAL\s+"
        r"([-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?)"
        r"\s*;\s*$"
    )

    for ln in def_lines:
        m = pat.match(ln.strip())
        if not m:
            continue
        key = m.group(1)
        val_um = float(m.group(2))
        val_units = val_um * float(units_scale)

        if key == "FE_CORE_BOX_LL_X":
            llx = val_units
        elif key == "FE_CORE_BOX_LL_Y":
            lly = val_units
        elif key == "FE_CORE_BOX_UR_X":
            urx = val_units
        elif key == "FE_CORE_BOX_UR_Y":
            ury = val_units

    if None in (llx, lly, urx, ury):
        return None
    return llx, lly, urx, ury


def generate_upper_rows(
    orig_row_main_lines,
    *,
    units_scale,
    new_site="asap7sc6t",
    new_h_um=0.216,
    core_box_units=None,  # (llx,lly,urx,ury) in DEF units
):
    if not orig_row_main_lines:
        return []

    def parse_row_main_line(line):
        # ROW <rowName> <site> <x> <y> <orient> DO <nx> BY <ny> STEP <sx> <sy> ...
        parts = line.strip().split()
        if len(parts) < 6 or parts[0] != "ROW":
            raise ValueError(f"Cannot parse ROW line: {line!r}")

        x = float(parts[3])
        y = float(parts[4])

        do_match = re.search(r"\bDO\s+(\d+)\b", line)
        num_sites = int(do_match.group(1)) if do_match else 100

        step_match = re.search(r"\bSTEP\s+([-+]?\d+\.?\d*)\b", line)
        step_x = float(step_match.group(1)) if step_match else 54.0

        return x, y, num_sites, step_x

    x0, y0, num_sites, step_x = parse_row_main_line(orig_row_main_lines[0])

    # 兜底 pitch（只用于 core_box 缺失时）
    if len(orig_row_main_lines) > 1:
        _, y1, _, _ = parse_row_main_line(orig_row_main_lines[1])
        orig_pitch = abs(y1 - y0)
    else:
        orig_pitch = 270.0  # 0.27um * 1000（兜底）

    new_h_units = float(new_h_um) * float(units_scale)
    if new_h_units <= 0:
        raise ValueError(f"new_h_um must be > 0, got {new_h_um}")

    if core_box_units is not None:
        _, core_lly, _, core_ury = core_box_units
        base_y = float(core_lly)
        total_height = float(core_ury) - float(core_lly)
    else:
        _, y_last, _, _ = parse_row_main_line(orig_row_main_lines[-1])
        base_y = float(y0)
        total_height = abs(y_last - y0) + orig_pitch

    # 关键：向下取整保证“总行高不超过原高度”，且至少 1 行
    new_count = max(1, int(math.floor(total_height / new_h_units)))

    new_rows = []
    x0i = int(round(x0))
    step_xi = int(round(step_x))

    for i in range(new_count):
        cur_y = int(round(base_y + i * new_h_units))
        orient = "N" if i % 2 == 0 else "FS"
        new_rows.append(
            f"ROW ROW_{i} {new_site} {x0i} {cur_y} {orient} DO {num_sites} BY 1 STEP {step_xi} 0 ;\n"
        )

    return new_rows


def _find_components_block(def_lines):
    n = len(def_lines)
    start = end = None

    for i in range(n):
        if def_lines[i].lstrip().startswith("COMPONENTS"):
            start = i
            break
    if start is None:
        return None, None, None, None, []

    for j in range(start + 1, n):
        if def_lines[j].lstrip().startswith("END COMPONENTS"):
            end = j + 1
            break
    if end is None:
        return start, None, def_lines[start], None, def_lines[start + 1 :]

    header = def_lines[start]
    end_line = def_lines[end - 1]
    body = def_lines[start + 1 : end - 1]
    return start, end, header, end_line, body


def _split_component_statements(component_body_lines):
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
            stmts.append([ln])

    if buf:
        stmts.append(buf)

    return stmts


def _classify_component_stmt(stmt_lines):
    first = ""
    for ln in stmt_lines:
        if ln.lstrip().startswith("-"):
            first = ln.strip()
            break
    if not first:
        return "all"

    parts = first.split()
    if len(parts) < 3:
        return "all"

    master = parts[2].lower()
    if "bottom" in master:
        return "bottom"
    if "upper" in master:
        return "upper"
    return "all"


def _find_nets_block(def_lines):
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
    core_box_units = _parse_core_box(lines, units_scale=units_scale)

    # ---- ROW ----
    row_start, row_end, row_stmts = _find_row_block(lines)
    if row_start is None:
        print("ERROR: No ROW block found in DEF.")
        return

    row_main_lines = []
    for stmt in row_stmts:
        main = _row_stmt_first_row_line(stmt)
        if main:
            row_main_lines.append(main)

    upper_rows = generate_upper_rows(
        row_main_lines,
        units_scale=units_scale,
        new_site="asap7sc6t",
        new_h_um=0.216,
        core_box_units=core_box_units,
    )

    # ---- COMPONENTS split ----
    comps_start, comps_end, _, comps_end_line, comps_body = _find_components_block(lines)
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
                if any(ln.lstrip().startswith("-") for ln in stmt):
                    bottom_cnt += 1

            if cls in ("upper", "all"):
                upper_body.extend(stmt)
                if any(ln.lstrip().startswith("-") for ln in stmt):
                    upper_cnt += 1

        comps_repl_bottom = [f"COMPONENTS {bottom_cnt} ;\n"] + bottom_body + [comps_end_line]
        comps_repl_upper = [f"COMPONENTS {upper_cnt} ;\n"] + upper_body + [comps_end_line]

    # ---- write bottom.def (ROW block 原样保留) ----
    bottom_lines = _rewrite_def(
        lines,
        row_repl=None,
        comps_repl=comps_repl_bottom,
        drop_nets=True,
    )
    with open(os.path.join(results_dir, "bottom.def"), "w", encoding="utf-8") as f:
        f.writelines(bottom_lines)

    # ---- write upper.def (替换 ROW block) ----
    upper_lines = _rewrite_def(
        lines,
        row_repl=upper_rows,
        comps_repl=comps_repl_upper,
        drop_nets=True,
    )
    with open(os.path.join(results_dir, "upper.def"), "w", encoding="utf-8") as f:
        f.writelines(upper_lines)

    print("[*] Done.")
    print(f"[*] units_scale: {units_scale}")
    if core_box_units is not None:
        llx, lly, urx, ury = core_box_units
        print(f"[*] core_box_units: ({llx:.1f},{lly:.1f})-({urx:.1f},{ury:.1f})")
    print(f"[*] bottom.def rows: {len(row_stmts)} (kept original ROW block)")
    print(f"[*] upper.def rows: {len(upper_rows)} (6T, total height ~= original, floor)")


if __name__ == "__main__":
    split_3dic_def()