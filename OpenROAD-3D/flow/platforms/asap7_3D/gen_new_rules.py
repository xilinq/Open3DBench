#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import re
from pathlib import Path


RE_BLOCK_NORMAL = re.compile(r"^\s*Metal\s+\d+\s+[A-Z]+\s+\d+\s*$")
RE_BLOCK_OVERUNDER = re.compile(r"^\s*Metal\s+\d+\s+OVER\s+\d+\s+UNDER\s+\d+\s*$")

RE_END_DIST = re.compile(r"^\s*END\s+DIST\s*$")
RE_DIST_START = re.compile(r"^\s*DIST\s+count\s+(\d+)\s+width\s+([0-9eE\+\-\.]+)\s*$")

RE_ANY_METAL = re.compile(r"^\s*Metal\s+(\d+)\b")
RE_LAYERCOUNT = re.compile(r"^\s*LayerCount\s+\d+\s*$")


def normalize_header(line: str) -> str:
    return " ".join(line.strip().split())


def is_numeric_line(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    toks = s.split()
    for t in toks:
        if not re.fullmatch(r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?", t):
            return False
    return True


def zero_numeric_line(line: str) -> str:
    toks = line.strip().split()
    if len(toks) == 0:
        return line if line.endswith("\n") else line + "\n"
    # 只将最后 3 列置 0，其余列保留
    keep = toks[:-3] if len(toks) > 3 else []
    zeros = ["0"] * min(3, len(toks))
    return " ".join(keep + zeros) + "\n"


def is_dist_block_empty(block_lines: list[str]) -> bool:
    """
    判定 asap7 的同名块是否“空”：
    - DIST count == 0 视为空
    - 或者块内没有任何纯数字数据行，也视为空
    """
    dist_count = None
    has_numeric = False

    for ln in block_lines:
        m = RE_DIST_START.match(ln)
        if m:
            dist_count = int(m.group(1))
        if is_numeric_line(ln):
            has_numeric = True

    if dist_count == 0:
        return True
    if not has_numeric:
        return True
    return False


def parse_blocks_from_asap7(path: Path) -> dict[str, list[str]]:
    blocks: dict[str, list[str]] = {}

    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        if RE_BLOCK_NORMAL.match(line) or RE_BLOCK_OVERUNDER.match(line):
            hdr = normalize_header(line)
            buf = [line]
            i += 1
            while i < n:
                buf.append(lines[i])
                if RE_END_DIST.match(lines[i]):
                    i += 1
                    break
                i += 1
            blocks[hdr] = buf
            continue
        i += 1

    return blocks


def emit_template_block_zeroed(block_lines: list[str]) -> list[str]:
    out: list[str] = []
    for ln in block_lines:
        if is_numeric_line(ln):
            out.append(zero_numeric_line(ln))
        else:
            out.append(ln if ln.endswith("\n") else ln + "\n")
    return out


def generate_new_rules(asap7_path: Path, template_path: Path, out_path: Path, max_metal: int = 20) -> None:
    asap7_blocks = parse_blocks_from_asap7(asap7_path)

    t_lines = template_path.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)

    out: list[str] = []
    i = 0
    n = len(t_lines)

    skip_metal = False

    while i < n:
        line = t_lines[i]

        if RE_LAYERCOUNT.match(line):
            out.append(f"LayerCount {max_metal}\n")
            i += 1
            continue

        mm = RE_ANY_METAL.match(line)
        if mm:
            metal_id = int(mm.group(1))
            skip_metal = metal_id > max_metal

        if skip_metal:
            i += 1
            continue

        # 规则块：按块头替换 or 模板置0
        if RE_BLOCK_NORMAL.match(line) or RE_BLOCK_OVERUNDER.match(line):
            hdr = normalize_header(line)

            # 取出模板块（到 END DIST）
            block_buf = [t_lines[i]]
            i += 1
            while i < n:
                block_buf.append(t_lines[i])
                if RE_END_DIST.match(t_lines[i]):
                    i += 1
                    break
                i += 1

            asap7_block = asap7_blocks.get(hdr)
            if asap7_block and (not is_dist_block_empty(asap7_block)):
                # 同名且非空：原封不动替换为 asap7
                out.extend(asap7_block)
            else:
                # 无同名 或 同名但空：保留模板结构，并将模板数值行置 0
                out.extend(emit_template_block_zeroed(block_buf))

            continue

        # 非块行：复制模板
        out.append(line)
        i += 1

    out_path.write_text("".join(out), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Generate new.rules using nangate45_3D.rules structure, filled by asap7_3D.rules blocks (exact header match; empty asap7 blocks do not override template)."
    )
    ap.add_argument("--asap7", default="asap7_3D.rules")
    ap.add_argument("--template", default="nangate45_3D.rules")
    ap.add_argument("--output", default="new.rules")
    ap.add_argument("--max-metal", type=int, default=20)
    args = ap.parse_args()

    generate_new_rules(Path(args.asap7), Path(args.template), Path(args.output), max_metal=args.max_metal)
    print(f"Wrote: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())