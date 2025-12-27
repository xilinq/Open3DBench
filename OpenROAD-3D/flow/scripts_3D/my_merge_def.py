import os
import re
import tempfile
from typing import Dict, List, Tuple, Optional


PLACED_RE = re.compile(
    r"\b(PLACED|FIXED)\s*\(\s*([-+]?\d+)\s+([-+]?\d+)\s*\)",
    flags=re.IGNORECASE,
)


def _iter_component_statements(lines: List[str]) -> List[List[str]]:
    """
    仅切分 COMPONENTS 段内的“组件语句”：
      - 以 '-' 开头视为一条组件语句开始
      - 遇到包含 ';' 的行视为该语句结束（兼容 ' ;' 单独一行）
    返回：list[stmt_lines]
    """
    stmts: List[List[str]] = []
    inside = False
    buf: Optional[List[str]] = None

    for ln in lines:
        s = ln.strip()

        if s.startswith("COMPONENTS"):
            inside = True
            buf = None
            continue
        if s == "END COMPONENTS":
            inside = False
            buf = None
            continue

        if not inside:
            continue

        if ln.lstrip().startswith("-"):
            # 新语句开始
            if buf:
                stmts.append(buf)
            buf = [ln]
            if ";" in ln:
                stmts.append(buf)
                buf = None
            continue

        # 语句续行
        if buf is not None:
            buf.append(ln)
            if ";" in ln:
                stmts.append(buf)
                buf = None
        else:
            # COMPONENTS 段里可能有空行/注释等：忽略即可
            pass

    if buf:
        stmts.append(buf)

    return stmts


def _get_inst_name(stmt_lines: List[str]) -> Optional[str]:
    """
    从组件语句第一行解析实例名：
      - <inst> <master> ...
    """
    first = ""
    for ln in stmt_lines:
        if ln.lstrip().startswith("-"):
            first = ln.strip()
            break
    if not first:
        return None
    parts = first.split()
    if len(parts) < 2:
        return None
    return parts[1]


def _extract_xy_from_stmt(stmt_lines: List[str]) -> Optional[Tuple[str, str]]:
    """
    从组件语句中提取 PLACED/FIXED 坐标。
    可能只出现在第一行，也可能跨行；这里把整条语句 join 后匹配。
    """
    blob = " ".join(ln.strip() for ln in stmt_lines)
    m = PLACED_RE.search(blob)
    if not m:
        return None
    x, y = m.group(2), m.group(3)
    return x, y


def read_def_and_store_coord(def_path: str, name2coord: Dict[str, Tuple[str, str]]) -> int:
    """
    读取 DEF，在 COMPONENTS 段内按语句解析，提取每个 inst 的 (x,y) 存入 name2coord。
    返回成功读取到坐标的实例数量。
    """
    with open(def_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    stmts = _iter_component_statements(lines)
    count = 0
    for stmt in stmts:
        inst = _get_inst_name(stmt)
        if not inst:
            continue
        xy = _extract_xy_from_stmt(stmt)
        if not xy:
            continue
        name2coord[inst] = xy
        count += 1
    return count


def _replace_xy_in_stmt_lines(stmt_lines: List[str], new_x: str, new_y: str) -> List[str]:
    """
    在一条组件语句内，将第一个出现的 PLACED/FIXED (x y) 替换为新坐标。
    尽量只改包含坐标的那一行，保持其它格式（包括下一行单独 ' ;'）不动。
    """
    out = stmt_lines[:]
    for i, ln in enumerate(out):
        m = PLACED_RE.search(ln)
        if not m:
            continue
        keyword = m.group(1)  # 保留原来的 PLACED/FIXED 大小写风格
        replaced = PLACED_RE.sub(f"{keyword} ( {new_x} {new_y} )", ln, count=1)
        out[i] = replaced
        break
    return out


def modify_def_inplace(target_def: str, name2coord: Dict[str, Tuple[str, str]]) -> int:
    """
    就地修改 target_def：在 COMPONENTS 段内按语句解析，若 inst 在 name2coord 中，则替换其坐标。
    返回成功修改的实例数量。
    """
    with open(target_def, "r", encoding="utf-8") as f:
        lines = f.readlines()

    modified = 0
    out_lines: List[str] = []

    inside_components = False
    stmt_buf: Optional[List[str]] = None

    def flush_stmt(buf: List[str]) -> None:
        nonlocal modified, out_lines
        inst = _get_inst_name(buf)
        if inst and inst in name2coord:
            new_x, new_y = name2coord[inst]
            new_buf = _replace_xy_in_stmt_lines(buf, new_x, new_y)
            if new_buf != buf:
                modified += 1
            out_lines.extend(new_buf)
        else:
            out_lines.extend(buf)

    for ln in lines:
        s = ln.strip()

        if s.startswith("COMPONENTS"):
            inside_components = True
            out_lines.append(ln)
            stmt_buf = None
            continue
        if s == "END COMPONENTS":
            if stmt_buf:
                flush_stmt(stmt_buf)
                stmt_buf = None
            inside_components = False
            out_lines.append(ln)
            continue

        if not inside_components:
            out_lines.append(ln)
            continue

        # inside COMPONENTS
        if ln.lstrip().startswith("-"):
            if stmt_buf:
                flush_stmt(stmt_buf)
            stmt_buf = [ln]
            if ";" in ln:
                flush_stmt(stmt_buf)
                stmt_buf = None
            continue

        if stmt_buf is not None:
            stmt_buf.append(ln)
            if ";" in ln:
                flush_stmt(stmt_buf)
                stmt_buf = None
            continue

        # COMPONENTS 段内的非语句行（空行/注释等）
        out_lines.append(ln)

    # 安全写回：先写临时文件再替换
    dir_name = os.path.dirname(target_def) or "."
    with tempfile.NamedTemporaryFile("w", delete=False, dir=dir_name, encoding="utf-8") as tf:
        tf.writelines(out_lines)
        tmp_path = tf.name
    os.replace(tmp_path, target_def)

    return modified


if __name__ == "__main__":
    results_dir = os.environ.get("RESULTS_DIR")
    if not results_dir:
        raise SystemExit("ERROR: RESULTS_DIR environment variable is not set.")

    upper_def = os.path.join(results_dir, "upper_legalized.def")
    bottom_def = os.path.join(results_dir, "bottom_legalized.def")
    target_def = os.path.join(results_dir, "4_1_cts.def")

    name2coord_map: Dict[str, Tuple[str, str]] = {}

    c1 = read_def_and_store_coord(upper_def, name2coord_map)
    c2 = read_def_and_store_coord(bottom_def, name2coord_map)
    print(f"[*] read coords: upper={c1}, bottom={c2}, total_unique={len(name2coord_map)}")

    m = modify_def_inplace(target_def, name2coord_map)
    print(f"[*] modified instances in target DEF: {m}")
    print(f"[*] updated file: {target_def}")