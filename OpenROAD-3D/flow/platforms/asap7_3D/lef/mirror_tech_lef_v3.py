#!/usr/bin/env python3
"""
F2F 3DIC tech LEF 生成器 (v3)

要求:
- 底部: 按原顺序保留 M1~M7 及相应 V0~V6
- 顶部: 生成 M8~M14 且顺序为 M8→M14 (M8 镜像 M7, M9 镜像 M6, ...)
- M7↔M8 之间使用自定义 UBUMP 过孔
- M8↔M9 的 VIA 为 M6↔M7 的镜像 (几何相同, 层名替换)
- 将结果组织成“看起来像 2D 双倍金属数”的 tech LEF

输入: asap7_tech_1x_201209.lef (同目录)
输出: asap7_tech_f2f_3d.lef (同目录)
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Tuple


THIS_DIR = Path(__file__).parent
INPUT_LEF = THIS_DIR / "asap7_tech_1x_201209.lef"
OUTPUT_LEF = THIS_DIR / "asap7_tech_f2f_3d.lef"


BOTTOM_KEEP_LAYERS = [
    "nwell", "pwell", "Gate", "Active",
    "V0", "M1", "V1", "M2", "V2", "M3", "V3",
    "M4", "V4", "M5", "V5", "M6", "V6", "M7",
]

TOP_LAYER_MAP = {
    "M7": "M8",
    "M6": "M9",   "V6": "V9",
    "M5": "M10",  "V5": "V10",
    "M4": "M11",  "V4": "V11",
    "M3": "M12",  "V3": "V12",
    "M2": "M13",  "V2": "V13",
    "M1": "M14",  "V1": "V14", "V0": "V14",  # V1/V0 -> V14 覆盖到同名以适配引用
}

TOP_ORDER = [
    "M8", "V9", "M9", "V10", "M10",
    "V11", "M11", "V12", "M12", "V13", "M13",
    "V14", "M14",
]


def read_lines(p: Path) -> List[str]:
    return p.read_text(encoding="utf-8").splitlines(keepends=True)


def find_end_library(lines: List[str]) -> int:
    for i, ln in enumerate(lines):
        if ln.strip() == "END LIBRARY":
            return i
    raise RuntimeError("END LIBRARY not found")


def collect_block(lines: List[str], i: int, kind: str) -> Tuple[List[str], int, str]:
    block = [lines[i]]
    header = lines[i].strip()
    if kind == "LAYER":
        m = re.match(r"^\s*LAYER\s+(\S+)", header)
    elif kind == "VIA":
        m = re.match(r"^\s*VIA\s+(\S+)", header)
    elif kind == "VIARULE":
        m = re.match(r"^\s*VIARULE\s+(\S+)", header)
    else:
        raise ValueError("invalid kind")
    if not m:
        raise ValueError(f"invalid {kind} header: {header}")
    name = m.group(1)
    i += 1
    while i < len(lines):
        block.append(lines[i])
        if lines[i].strip() == f"END {name}":
            return block, i + 1, name
        i += 1
    raise RuntimeError(f"END {name} not found for {kind}")


def rename_refs(text: str, mapping: Dict[str, str]) -> str:
    for old, new in mapping.items():
        text = re.sub(rf"\bLAYER\s+{re.escape(old)}\b", f"LAYER {new}", text)
        text = re.sub(rf"\bEND\s+{re.escape(old)}\b", f"END {new}", text)
    return text


def mirror_layer_block(block: List[str], old_name: str) -> List[str]:
    if old_name not in TOP_LAYER_MAP:
        return []
    text = "".join(block)
    new_name = TOP_LAYER_MAP[old_name]
    text = rename_refs(text, {old_name: new_name})
    return text.splitlines(keepends=True)


def main() -> None:
    src = read_lines(INPUT_LEF)
    end_idx = find_end_library(src)

    header: List[str] = []
    bottom_layer_lines: List[str] = []
    top_layer_blocks: Dict[str, List[str]] = {}
    bottom_via_blocks: Dict[str, List[str]] = {}
    top_via_blocks: Dict[str, List[str]] = {}
    bottom_viarule_blocks: Dict[str, List[str]] = {}
    top_viarule_blocks: Dict[str, List[str]] = {}

    i = 0
    seen_body = False
    while i < end_idx:
        ln = src[i]
        if re.match(r"^\s*LAYER\s+\S+\s*$", ln):
            seen_body = True
            block, i2, lname = collect_block(src, i, "LAYER")
            if lname in BOTTOM_KEEP_LAYERS:
                bottom_layer_lines.extend(block)
            if lname in TOP_LAYER_MAP:
                top_block = mirror_layer_block(block, lname)
                if top_block:
                    new_name = TOP_LAYER_MAP[lname]
                    top_layer_blocks[new_name] = top_block
            # 忽略其余原始顶层 (M8/M9/V8/V9/Pad 等)
            i = i2
            continue
        if re.match(r"^\s*VIA\s+\S+", ln):
            seen_body = True
            block, i2, vname = collect_block(src, i, "VIA")
            # 保留底部 VIA: VIA12..VIA67
            if vname in {"VIA12", "VIA23", "VIA34", "VIA45", "VIA56", "VIA67"}:
                bottom_via_blocks[vname] = block
                # 生成镜像顶部 VIA: 用层映射替换层名
                text = "".join(block)
                # 将底部层名替换为顶部层名
                text_mir = text
                text_mir = rename_refs(text_mir, {
                    "M1": "M14", "M2": "M13", "M3": "M12", "M4": "M11",
                    "M5": "M10", "M6": "M9",  "M7": "M8",
                    "V0": "V14", "V1": "V14", "V2": "V13", "V3": "V12",
                    "V4": "V11", "V5": "V10", "V6": "V9",  # 跳过 V8，V6→V9
                })
                # 重命名 VIA 名称为 VIA_Mx_My 形式
                top_via_name_map = {
                    "VIA12": "VIA_M13_M14",
                    "VIA23": "VIA_M12_M13",
                    "VIA34": "VIA_M11_M12",
                    "VIA45": "VIA_M10_M11",
                    "VIA56": "VIA_M9_M10",
                    "VIA67": "VIA_M8_M9",
                }
                text_mir = re.sub(r"^\s*VIA\s+\S+", f"VIA {top_via_name_map[vname]}", text_mir, count=1, flags=re.M)
                text_mir = re.sub(rf"\bEND\s+{re.escape(vname)}\b", f"END {top_via_name_map[vname]}", text_mir)
                top_via_blocks[top_via_name_map[vname]] = text_mir.splitlines(keepends=True)
            i = i2
            continue
        if re.match(r"^\s*VIARULE\s+\S+", ln):
            seen_body = True
            block, i2, rname = collect_block(src, i, "VIARULE")
            # 保留底部与 M1~M7 相关的规则, 忽略与 M8/Pad 相关的
            if rname in {
                "M2_M1", "M3_M2widePWR0p936", "M4_M3widePWR0p864",
                "M5_M4widePWR0p864", "M6_M5", "M6_M5widePWR1p152",
                "M7_M6", "M7_M6widePWR1p152",
            }:
                bottom_viarule_blocks[rname] = block
                # 镜像顶部规则 (层名替换 + 规则名替换)
                rule_map = {
                    "M7_M6": "M8_M9",
                    "M6_M5": "M9_M10",
                    "M5_M4": "M10_M11",
                    "M4_M3": "M11_M12",
                    "M3_M2widePWR0p936": "M12_M13widePWR0p936",
                    "M2_M1": "M13_M14",
                    "M7_M6widePWR1p152": "M8_M9widePWR1p152",
                    "M6_M5widePWR1p152": "M9_M10widePWR1p152",
                    "M5_M4widePWR0p864": "M10_M11widePWR0p864",
                    "M4_M3widePWR0p864": "M11_M12widePWR0p864",
                }
                if rname in rule_map:
                    text = "".join(block)
                    text = rename_refs(text, {
                        "M1": "M14", "M2": "M13", "M3": "M12", "M4": "M11",
                        "M5": "M10", "M6": "M9",  "M7": "M8",
                        "V0": "V14", "V1": "V14", "V2": "V13", "V3": "V12",
                        "V4": "V11", "V5": "V10", "V6": "V9",
                    })
                    text = re.sub(rf"^\s*VIARULE\s+{re.escape(rname)}", f"VIARULE {rule_map[rname]}", text, flags=re.M)
                    text = re.sub(rf"\bEND\s+{re.escape(rname)}\b", f"END {rule_map[rname]}", text)
                    top_viarule_blocks[rule_map[rname]] = text.splitlines(keepends=True)
            i = i2
            continue
        if not seen_body:
            header.append(ln)
        i += 1

    out: List[str] = []
    out.extend(header)

    # 底部层 (按原顺序)
    out.append("\n# ========================================\n")
    out.append("# Bottom Die Layers (M1-M7)\n")
    out.append("# ========================================\n\n")
    out.extend(bottom_layer_lines)

    # 顶部层 (按 M8→M14 顺序)
    out.append("\n# ========================================\n")
    out.append("# Top Die Layers (M8-M14, mirrored)\n")
    out.append("# ========================================\n\n")
    for lname in TOP_ORDER:
        blk = top_layer_blocks.get(lname)
        if blk:
            out.extend(blk)

    # UBUMP 定义 (M7↔M8)
    out.append("\n# ========================================\n")
    out.append("# 3D Inter-die Connection (UBUMP between M7 and M8)\n")
    out.append("# ========================================\n\n")
    out.extend([
        "LAYER UBUMP\n",
        "  TYPE CUT ;\n",
        "  SPACING 0.2 ;\n",
        "  WIDTH 0.1 ;\n",
        "END UBUMP\n",
        "\n",
        "VIA ubumping Default\n",
        "  LAYER M7 ;\n",
        "    RECT -0.05 -0.05 0.05 0.05 ;\n",
        "  LAYER M8 ;\n",
        "    RECT -0.05 -0.05 0.05 0.05 ;\n",
        "  LAYER UBUMP ;\n",
        "    RECT -0.05 -0.05 0.05 0.05 ;\n",
        "END ubumping\n",
        "\n",
        "VIARULE M7_M8_UBUMP GENERATE DEFAULT\n",
        "  LAYER M7 ;\n",
        "    ENCLOSURE 0.011 0.0 ;\n",
        "  LAYER M8 ;\n",
        "    ENCLOSURE 0.011 0.0 ;\n",
        "  LAYER UBUMP ;\n",
        "    RECT -0.05 -0.05 0.05 0.05 ;\n",
        "    SPACING 0.2 BY 0.2 ;\n",
        "END M7_M8_UBUMP\n",
        "\n",
    ])

    # 底部 VIA (包含到 M7)
    out.append("# ========================================\n")
    out.append("# Bottom Die VIAs\n")
    out.append("# ========================================\n\n")
    for vname in ["VIA12", "VIA23", "VIA34", "VIA45", "VIA56", "VIA67"]:
        blk = bottom_via_blocks.get(vname)
        if blk:
            out.extend(blk)

    # 顶部 VIA (按 M8→M14 顺序相邻对)
    out.append("\n# ========================================\n")
    out.append("# Top Die VIAs (mirrored)\n")
    out.append("# ========================================\n\n")
    for vname in [
        "VIA_M8_M9", "VIA_M9_M10", "VIA_M10_M11",
        "VIA_M11_M12", "VIA_M12_M13", "VIA_M13_M14",
    ]:
        blk = top_via_blocks.get(vname)
        if blk:
            out.extend(blk)

    # 底部 VIARULE
    out.append("# ========================================\n")
    out.append("# Bottom Die VIARULEs\n")
    out.append("# ========================================\n\n")
    for rname in [
        "M2_M1", "M3_M2widePWR0p936", "M4_M3widePWR0p864",
        "M5_M4widePWR0p864", "M6_M5", "M6_M5widePWR1p152",
        "M7_M6", "M7_M6widePWR1p152",
    ]:
        blk = bottom_viarule_blocks.get(rname)
        if blk:
            out.extend(blk)

    # 顶部 VIARULE
    out.append("\n# ========================================\n")
    out.append("# Top Die VIARULEs (mirrored)\n")
    out.append("# ========================================\n\n")
    for rname in [
        "M8_M9", "M8_M9widePWR1p152", "M9_M10", "M9_M10widePWR1p152",
        "M10_M11widePWR0p864", "M10_M11", "M11_M12widePWR0p864",
        "M11_M12", "M12_M13widePWR0p936", "M12_M13", "M13_M14",
    ]:
        blk = top_viarule_blocks.get(rname)
        if blk:
            out.extend(blk)

    out.append("\nEND LIBRARY\n")

    OUTPUT_LEF.write_text("".join(out), encoding="utf-8")
    print(f"Generated: {OUTPUT_LEF}")


if __name__ == "__main__":
    main()


