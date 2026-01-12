#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
只保留 Metal 1..N，并且只保留 1..N 之间的耦合关系：
- 删除 Metal > N 的全部规则块
- 对于 Metal <= N：删除任何引用到 >N 的耦合块（UNDER/OVER/DIAGUNDER/OVERUNDER 等）
- 允许引用 0（通常不是金属层号）
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

METAL_LINE_RE = re.compile(r"^\s*Metal\s+(\d+)\b")
LAYERCOUNT_RE = re.compile(r"^\s*LayerCount\s+(\d+)\s*$")
END_DENSITYMODEL_RE = re.compile(r"^\s*END\s+DensityModel\b")

# 抓取耦合目标层号（出现在 Metal 行里的 UNDER/OVER/DIAGUNDER 后面）
COUPLING_TARGET_RE = re.compile(r"\b(?:UNDER|OVER|DIAGUNDER)\s+(\d+)\b")


def metal_block_keep(metal_line: str, max_metal: int) -> bool:
    """
    判断一个以 'Metal ...' 开头的块是否保留。
    规则：
    - base metal 在 1..max_metal
    - 所有 UNDER/OVER/DIAGUNDER 引用的目标层 t 满足：t==0 或 1..max_metal
    """
    m = METAL_LINE_RE.match(metal_line)
    if not m:
        return True

    base = int(m.group(1))
    if not (1 <= base <= max_metal):
        return False

    targets = [int(x) for x in COUPLING_TARGET_RE.findall(metal_line)]
    for t in targets:
        if t != 0 and not (1 <= t <= max_metal):
            return False

    return True


def filter_rules(lines: list[str], max_metal: int = 7) -> list[str]:
    out: list[str] = []

    current_keep = True
    current_in_metal_block = False

    for line in lines:
        # 全局结束：强制保留并重置状态
        if END_DENSITYMODEL_RE.match(line):
            out.append(line)
            current_keep = True
            current_in_metal_block = False
            continue

        # LayerCount：改为 max_metal
        m_lc = LAYERCOUNT_RE.match(line)
        if m_lc:
            out.append(f"LayerCount {max_metal}\n")
            continue

        # 遇到新的 Metal 块起始行：重新判定 keep
        if METAL_LINE_RE.match(line):
            current_in_metal_block = True
            current_keep = metal_block_keep(line, max_metal)
            if current_keep:
                out.append(line)
            continue

        # 非 Metal 行
        if not current_in_metal_block:
            # 文件头/全局配置：保留
            out.append(line)
        else:
            # Metal 块内部：按 current_keep 决定
            if current_keep:
                out.append(line)

    # 保证结尾换行
    if out and not out[-1].endswith("\n"):
        out[-1] += "\n"
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Keep only Metal 1..N and couplings within 1..N from asap7.rules.")
    parser.add_argument("--input", default="asap7.rules")
    parser.add_argument("--output", default="asap7_3D.rules")
    parser.add_argument("--max-metal", type=int, default=7)
    args = parser.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)

    if not in_path.exists():
        raise FileNotFoundError(f"Input file not found: {in_path.resolve()}")

    lines = in_path.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
    filtered = filter_rules(lines, max_metal=args.max_metal)

    out_path.write_text("".join(filtered), encoding="utf-8")
    print(f"Wrote {out_path} (kept Metal 1..{args.max_metal} and only couplings within 1..{args.max_metal})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())