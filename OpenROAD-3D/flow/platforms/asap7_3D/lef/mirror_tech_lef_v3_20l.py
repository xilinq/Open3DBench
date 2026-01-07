#!/usr/bin/env python3
"""
F2F 3DIC tech LEF 生成器 (v3, 20l)

ls -a asap7 tech LEF 组织成“看起来像 2D 双倍金属数”的 tech LEF。

ls - 25-53 行的修改一致）：
- 底部 die：按原顺序保留 nwell/pwell/Gate/Active + V0~V9 + M1~M9 + Pad
ls -a *_u（例如 M7 -> M7_u, Pad -> Pad_u）
- inter-die：使用自定义 UBUMP 连接 Pad <-> Pad_u
ls --color=auto -a (VIA12..VIA9Pad、M2_M1..Pad_M9)，顶部生成 *_/VIA名/规则名替换）

: asap7_tech_1x_201209.lef (同目录)
: asap7_tech_f2f_3d_20l.lef (同目录)
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Tuple


THIS_DIR = Path(__file__).parent
INPUT_LEF = THIS_DIR / "asap7_tech_1x_201209.lef"
OUTPUT_LEF = THIS_DIR / "asap7_tech_f2f_3d_20l.lef"


BOTTOM_KEEP_LAYERS = [
    "nwell",
    "pwell",
    "Gate",
    "Active",
    "V0",
    "M1",
    "V1",
    "M2",
    "V2",
    "M3",
    "V3",
    "M4",
    "V4",
    "M5",
    "V5",
    "M6",
    "V6",
    "M7",
    "V7",
    "M8",
    "V8",
    "M9",
    "V9",
    "Pad",
]

TOP_LAYER_MAP = {
    "Pad": "Pad_u",
    "M9": "M9_u",
    "V9": "V9_u",
    "M8": "M8_u",
    "V8": "V8_u",
    "M7": "M7_u",
    "V7": "V7_u",
    "M6": "M6_u",
    "V6": "V6_u",
    "M5": "M5_u",
    "V5": "V5_u",
    "M4": "M4_u",
    "V4": "V4_u",
    "M3": "M3_u",
    "V3": "V3_u",
    "M2": "M2_u",
    "V2": "V2_u",
    "M1": "M1_u",
    "V1": "V1_u",
    "V0": "V0_u",
}

TOP_ORDER = [
    "Pad_u",
    "V9_u",
    "M9_u",
    "V8_u",
    "M8_u",
    "V7_u",
    "M7_u",
    "V6_u",
    "M6_u",
    "V5_u",
    "M5_u",
    "V4_u",
    "M4_u",
    "V3_u",
    "M3_u",
    "V2_u",
    "M2_u",
    "V1_u",
    "M1_u",
    "V0_u",
]

BOTTOM_VIA_KEEP = [
    "VIA12",
    "VIA23",
    "VIA34",
    "VIA45",
    "VIA56",
    "VIA67",
    "VIA78",
    "VIA89",
    "VIA9Pad",
]

BOTTOM_VIARULE_KEEP = [
    "M2_M1",
    "M3_M2widePWR0p936",
    "M4_M3widePWR0p864",
    "M5_M4widePWR0p864",
    "M6_M5",
    "M6_M5widePWR1p152",
    "M7_M6",
    "M7_M6widePWR1p152",
    "M8_M7",
    "M9_M8",
    "Pad_M9",
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


def rename_layer_refs(text: str, mapping: Dict[str, str]) -> str:
    """Rename layer references inside blocks.

    Covers common forms:
    - LAYER M7
    - LAYER M7 ;
    - END M7
    """

    for old, new in mapping.items():
        text = re.sub(rf"\bLAYER\s+{re.escape(old)}\b", f"LAYER {new}", text)
        text = re.sub(rf"\bEND\s+{re.escape(old)}\b", f"END {new}", text)
    return text


def rename_via_refs(text: str, mapping: Dict[str, str]) -> str:
    """Rename VIA references inside VIARULE blocks (e.g. 'VIA VIA67 ;')."""

    for old, new in mapping.items():
        text = re.sub(rf"\bVIA\s+{re.escape(old)}\b", f"VIA {new}", text)
    return text


def mirror_layer_block(block: List[str], old_name: str) -> List[str]:
    if old_name not in TOP_LAYER_MAP:
        return []
    text = "".join(block)
    new_name = TOP_LAYER_MAP[old_name]
    text = rename_layer_refs(text, {old_name: new_name})
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

    top_via_name_map: Dict[str, str] = {v: f"{v}_u" for v in BOTTOM_VIA_KEEP}
    top_viarule_name_map: Dict[str, str] = {r: f"{r}_u" for r in BOTTOM_VIARULE_KEEP}

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

            i = i2
            continue

        if re.match(r"^\s*VIA\s+\S+", ln):
            seen_body = True
            block, i2, vname = collect_block(src, i, "VIA")

            if vname in set(BOTTOM_VIA_KEEP):
                bottom_via_blocks[vname] = block

                text_mir = "".join(block)
                text_mir = rename_layer_refs(text_mir, TOP_LAYER_MAP)
                new_vname = top_via_name_map[vname]
                text_mir = re.sub(
                    r"^\s*VIA\s+\S+",
                    f"VIA {new_vname}",
                    text_mir,
                    count=1,
                    flags=re.M,
                )
                text_mir = re.sub(
                    rf"\bEND\s+{re.escape(vname)}\b",
                    f"END {new_vname}",
                    text_mir,
                )
                top_via_blocks[new_vname] = text_mir.splitlines(keepends=True)

            i = i2
            continue

        if re.match(r"^\s*VIARULE\s+\S+", ln):
            seen_body = True
            block, i2, rname = collect_block(src, i, "VIARULE")

            if rname in set(BOTTOM_VIARULE_KEEP):
                bottom_viarule_blocks[rname] = block

                text_mir = "".join(block)
                text_mir = rename_layer_refs(text_mir, TOP_LAYER_MAP)
                text_mir = rename_via_refs(text_mir, top_via_name_map)
                new_rname = top_viarule_name_map[rname]
                text_mir = re.sub(
                    rf"^\s*VIARULE\s+{re.escape(rname)}",
                    f"VIARULE {new_rname}",
                    text_mir,
                    flags=re.M,
                )
                text_mir = re.sub(
                    rf"\bEND\s+{re.escape(rname)}\b",
                    f"END {new_rname}",
                    text_mir,
                )
                top_viarule_blocks[new_rname] = text_mir.splitlines(keepends=True)

            i = i2
            continue

        if not seen_body:
            header.append(ln)
        i += 1

    out: List[str] = []
    out.extend(header)

    out.append("\n# ========================================\n")
    out.append("# Bottom Die Layers (M1-M9 + Pad)\n")
    out.append("# ========================================\n\n")
    out.extend(bottom_layer_lines)

    out.append("\n# ========================================\n")
    out.append("# Top Die Layers (*_u, mirrored)\n")
    out.append("# ========================================\n\n")
    for lname in TOP_ORDER:
        blk = top_layer_blocks.get(lname)
        if blk:
            out.extend(blk)

    out.append("\n# ========================================\n")
    out.append("# 3D Inter-die Connection (UBUMP between Pad and Pad_u)\n")
    out.append("# ========================================\n\n")
    out.extend(
        [
            "LAYER UBUMP\n",
            "  TYPE CUT ;\n",
            "  SPACING 0.2 ;\n",
            "  WIDTH 0.1 ;\n",
            "END UBUMP\n",
            "\n",
            "VIA ubumping Default\n",
            "  LAYER Pad ;\n",
            "    RECT -0.05 -0.05 0.05 0.05 ;\n",
            "  LAYER Pad_u ;\n",
            "    RECT -0.05 -0.05 0.05 0.05 ;\n",
            "  LAYER UBUMP ;\n",
            "    RECT -0.05 -0.05 0.05 0.05 ;\n",
            "END ubumping\n",
            "\n",
            "VIARULE Pad_Pad_u_UBUMP GENERATE DEFAULT\n",
            "  LAYER Pad ;\n",
            "    ENCLOSURE 0.011 0.0 ;\n",
            "  LAYER Pad_u ;\n",
            "    ENCLOSURE 0.011 0.0 ;\n",
            "  LAYER UBUMP ;\n",
            "    RECT -0.05 -0.05 0.05 0.05 ;\n",
            "    SPACING 0.2 BY 0.2 ;\n",
            "END Pad_Pad_u_UBUMP\n",
            "\n",
        ]
    )

    out.append("# ========================================\n")
    out.append("# Bottom Die VIAs\n")
    out.append("# ========================================\n\n")
    for vname in BOTTOM_VIA_KEEP:
        blk = bottom_via_blocks.get(vname)
        if blk:
            out.extend(blk)

    out.append("\n# ========================================\n")
    out.append("# Top Die VIAs (mirrored)\n")
    out.append("# ========================================\n\n")
    for vname in [f"{v}_u" for v in BOTTOM_VIA_KEEP]:
        blk = top_via_blocks.get(vname)
        if blk:
            out.extend(blk)

    out.append("# ========================================\n")
    out.append("# Bottom Die VIARULEs\n")
    out.append("# ========================================\n\n")
    for rname in BOTTOM_VIARULE_KEEP:
        blk = bottom_viarule_blocks.get(rname)
        if blk:
            out.extend(blk)

    out.append("\n# ========================================\n")
    out.append("# Top Die VIARULEs (mirrored)\n")
    out.append("# ========================================\n\n")
    for rname in [f"{r}_u" for r in BOTTOM_VIARULE_KEEP]:
        blk = top_viarule_blocks.get(rname)
        if blk:
            out.extend(blk)

    out.append("\nEND LIBRARY\n")

    OUTPUT_LEF.write_text("".join(out), encoding="utf-8")
    print(f"Generated: {OUTPUT_LEF}")


if __name__ == "__main__":
    main()
