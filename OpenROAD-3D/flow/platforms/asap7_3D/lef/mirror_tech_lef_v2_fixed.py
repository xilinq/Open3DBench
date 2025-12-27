#!/usr/bin/env python3
"""
将 2D tech LEF 改造为 F2F 3DIC 架构（修复版）：
- 底部芯片: M1-M7 (保持原名)
- 顶部芯片: M8-M14 (镜像 M7-M1)
- 3D 互连: M7 ↔ M8 键合
- 删除原始 M8, M9, Pad 等不需要的层

Input:  asap7_tech_1x_201209.lef
Output: asap7_tech_f2f_3d.lef
"""

from __future__ import annotations
import re
from pathlib import Path
from typing import List, Dict, Set

THIS_DIR = Path(__file__).parent
INPUT_LEF = THIS_DIR / "asap7_tech_1x_201209.lef"
OUTPUT_LEF = THIS_DIR / "asap7_tech_f2f_3d.lef"

# 底部芯片保留的层
BOTTOM_KEEP_LAYERS = {
    "nwell", "pwell", "Gate", "Active",  # 工艺基础层
    "V0", "M1", "V1", "M2", "V2", "M3", "V3",
    "M4", "V4", "M5", "V5", "M6", "V6", "M7"
}

# 需要删除的层（原始 2D 中的顶层）
LAYERS_TO_DELETE = {"V7", "M8", "V8", "M9", "V9", "Pad"}

# 顶部芯片层映射 (原始 → 新名称)
TOP_LAYER_MAP = {
    "M7": "M8",  "V6": "V8",
    "M6": "M9",  "V5": "V9",
    "M5": "M10", "V4": "V10",
    "M4": "M11", "V3": "V11",
    "M3": "M12", "V2": "V12",
    "M2": "M13", "V1": "V13",
    "M1": "M14", "V0": "V14",
}

# 底部 VIA 保留列表
BOTTOM_KEEP_VIAS = {
    "VIA12", "VIA23", "VIA34", "VIA45", "VIA56", "VIA67"
}

# 需要删除的 VIA
VIAS_TO_DELETE = {"VIA78", "VIA89", "VIA9Pad"}

# 顶部 VIA 映射 (避免名称冲突)
TOP_VIA_MAP = {
    "VIA67": "VIA_M8_M9",      # M8↔M9 (原M6↔M7)
    "VIA56": "VIA_M9_M10",     # M9↔M10 (原M5↔M6)
    "VIA45": "VIA_M10_M11",    # M10↔M11 (原M4↔M5)
    "VIA34": "VIA_M11_M12",    # M11↔M12 (原M3↔M4)
    "VIA23": "VIA_M12_M13",    # M12↔M13 (原M2↔M3)
    "VIA12": "VIA_M13_M14",    # M13↔M14 (原M1↔M2)
}

# 底部 VIARULE 保留列表
BOTTOM_KEEP_VIARULES = {
    "M2_M1", "M3_M2widePWR0p936", "M4_M3widePWR0p864",
    "M5_M4widePWR0p864", "M6_M5", "M6_M5widePWR1p152",
    "M7_M6", "M7_M6widePWR1p152"
}

# 需要删除的 VIARULE
VIARULES_TO_DELETE = {
    "Pad_M9", "M9_M8", "M8_M7"
}

# 顶部 VIARULE 映射
TOP_VIARULE_MAP = {
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


def read_lef_lines(path: Path) -> List[str]:
    return path.read_text(encoding="utf-8").splitlines(keepends=True)


def find_end_library_index(lines: List[str]) -> int:
    for idx, line in enumerate(lines):
        if line.strip() == "END LIBRARY":
            return idx
    raise RuntimeError("END LIBRARY not found")


def collect_block(lines: List[str], start_idx: int, keyword: str) -> tuple[List[str], int, str]:
    """收集完整的块（LAYER/VIA/VIARULE），返回 (block, next_idx, name)"""
    block = [lines[start_idx]]
    header = lines[start_idx].strip()
    
    # 提取名称
    if keyword == "LAYER":
        m = re.match(r"^\s*LAYER\s+(\S+)", header)
    elif keyword == "VIA":
        m = re.match(r"^\s*VIA\s+(\S+)", header)
    elif keyword == "VIARULE":
        m = re.match(r"^\s*VIARULE\s+(\S+)", header)
    else:
        raise ValueError(f"Unknown keyword: {keyword}")
    
    if not m:
        raise ValueError(f"Invalid {keyword} header: {header}")
    
    name = m.group(1)
    
    i = start_idx + 1
    while i < len(lines):
        block.append(lines[i])
        if lines[i].strip() == f"END {name}":
            return block, i + 1, name
        i += 1
    
    raise RuntimeError(f"No END found for {keyword} {name}")


def rename_in_text(text: str, mapping: Dict[str, str]) -> str:
    """在文本中替换层/VIA/VIARULE名称"""
    for old_name, new_name in mapping.items():
        # LAYER 语句
        text = re.sub(rf'\bLAYER\s+{re.escape(old_name)}\b', f'LAYER {new_name}', text)
        # END 语句
        text = re.sub(rf'\bEND\s+{re.escape(old_name)}\b', f'END {new_name}', text)
        # VIA 语句
        text = re.sub(rf'\bVIA\s+{re.escape(old_name)}\b', f'VIA {new_name}', text)
        # VIARULE 语句
        text = re.sub(rf'\bVIARULE\s+{re.escape(old_name)}\b', f'VIARULE {new_name}', text)
    return text


def mirror_block(block: List[str], old_name: str, name_map: Dict[str, str], layer_map: Dict[str, str]) -> List[str]:
    """镜像块并重命名"""
    if old_name not in name_map:
        return []
    
    text = "".join(block)
    new_name = name_map[old_name]
    
    # 重命名主名称
    full_map = {old_name: new_name}
    full_map.update(layer_map)
    
    text = rename_in_text(text, full_map)
    
    return text.splitlines(keepends=True)


def generate_3d_bond_layer() -> List[str]:
    """生成 3D 键合层定义"""
    return [
        "\n",
        "# ========================================\n",
        "# 3D Inter-die Connection Layer (M7 ↔ M8)\n",
        "# ========================================\n",
        "\n",
        "LAYER V7_M8_BOND\n",
        "  TYPE CUT ;\n",
        "  SPACING 0.1 ;\n",
        "  WIDTH 0.064 ;\n",
        "  PROPERTY LEF58_TYPE \"TYPE 3D_HYBRID_BOND ;\" ;\n",
        "END V7_M8_BOND\n",
        "\n",
    ]


def generate_3d_bond_via() -> List[str]:
    """生成 3D 键合 VIA"""
    return [
        "# 3D Bonding VIA (M7 to M8)\n",
        "VIA VIA_M7_M8_BOND Default\n",
        "  LAYER M7 ;\n",
        "    RECT -0.032 -0.032 0.032 0.032 ;\n",
        "  LAYER M8 ;\n",
        "    RECT -0.032 -0.032 0.032 0.032 ;\n",
        "  LAYER V7_M8_BOND ;\n",
        "    RECT -0.032 -0.032 0.032 0.032 ;\n",
        "END VIA_M7_M8_BOND\n",
        "\n",
    ]


def generate_3d_bond_viarule() -> List[str]:
    """生成 3D 键合 VIARULE"""
    return [
        "# 3D Bonding VIARULE (M7 to M8)\n",
        "VIARULE M7_M8_BOND GENERATE DEFAULT\n",
        "  LAYER M7 ;\n",
        "    ENCLOSURE 0.011 0.0 ;\n",
        "  LAYER M8 ;\n",
        "    ENCLOSURE 0.011 0.0 ;\n",
        "  LAYER V7_M8_BOND ;\n",
        "    RECT -0.032 -0.032 0.032 0.032 ;\n",
        "    SPACING 0.2 BY 0.2 ;\n",
        "END M7_M8_BOND\n",
        "\n",
    ]


def main():
    lines = read_lef_lines(INPUT_LEF)
    end_idx = find_end_library_index(lines)
    
    # 收集各部分
    header_lines = []
    bottom_layers = []
    top_layers = []
    bottom_vias = []
    top_vias = []
    bottom_viarules = []
    top_viarules = []
    
    i = 0
    in_sections = False
    
    while i < end_idx:
        line = lines[i]
        
        # LAYER 块
        if re.match(r"^\s*LAYER\s+\S+\s*$", line):
            in_sections = True
            block, next_i, name = collect_block(lines, i, "LAYER")
            
            # 删除不需要的层
            if name in LAYERS_TO_DELETE:
                i = next_i
                continue
            
            # 保留底部层
            if name in BOTTOM_KEEP_LAYERS:
                bottom_layers.extend(block)
            
            # 镜像到顶部
            if name in TOP_LAYER_MAP:
                mirrored = mirror_block(block, name, TOP_LAYER_MAP, TOP_LAYER_MAP)
                if mirrored:
                    top_layers.extend(mirrored)
            
            i = next_i
            continue
        
        # VIA 块
        if re.match(r"^\s*VIA\s+\S+", line):
            in_sections = True
            block, next_i, name = collect_block(lines, i, "VIA")
            
            # 删除不需要的 VIA
            if name in VIAS_TO_DELETE:
                i = next_i
                continue
            
            # 保留底部 VIA
            if name in BOTTOM_KEEP_VIAS:
                bottom_vias.extend(block)
                # 镜像到顶部
                mirrored = mirror_block(block, name, TOP_VIA_MAP, TOP_LAYER_MAP)
                if mirrored:
                    top_vias.extend(mirrored)
            
            i = next_i
            continue
        
        # VIARULE 块
        if re.match(r"^\s*VIARULE\s+\S+", line):
            in_sections = True
            block, next_i, name = collect_block(lines, i, "VIARULE")
            
            # 删除不需要的 VIARULE
            if name in VIARULES_TO_DELETE:
                i = next_i
                continue
            
            # 保留底部 VIARULE
            if name in BOTTOM_KEEP_VIARULES:
                bottom_viarules.extend(block)
                # 镜像到顶部
                mirrored = mirror_block(block, name, TOP_VIARULE_MAP, TOP_LAYER_MAP)
                if mirrored:
                    top_viarules.extend(mirrored)
            
            i = next_i
            continue
        
        # 头部内容（在第一个 LAYER 之前）
        if not in_sections:
            header_lines.append(line)
        
        i += 1
    
    # 组装最终输出
    final_output = []
    final_output.extend(header_lines)
    
    # 添加底部芯片层
    final_output.append("\n# ========================================\n")
    final_output.append("# Bottom Die Layers (M1-M7)\n")
    final_output.append("# ========================================\n\n")
    final_output.extend(bottom_layers)
    
    # 添加顶部芯片层
    final_output.append("\n# ========================================\n")
    final_output.append("# Top Die Layers (M8-M14, mirrored from M7-M1)\n")
    final_output.append("# ========================================\n\n")
    final_output.extend(top_layers)
    
    # 添加 3D 键合层
    final_output.extend(generate_3d_bond_layer())
    
    # 添加底部 VIA
    final_output.append("# ========================================\n")
    final_output.append("# Bottom Die VIAs (VIA12 to VIA67)\n")
    final_output.append("# ========================================\n\n")
    final_output.extend(bottom_vias)
    
    # 添加顶部 VIA
    final_output.append("\n# ========================================\n")
    final_output.append("# Top Die VIAs (M8-M14 interconnects)\n")
    final_output.append("# ========================================\n\n")
    final_output.extend(top_vias)
    
    # 添加 3D 键合 VIA
    final_output.extend(generate_3d_bond_via())
    
    # 添加底部 VIARULE
    final_output.append("# ========================================\n")
    final_output.append("# Bottom Die VIARULEs\n")
    final_output.append("# ========================================\n\n")
    final_output.extend(bottom_viarules)
    
    # 添加顶部 VIARULE
    final_output.append("\n# ========================================\n")
    final_output.append("# Top Die VIARULEs (mirrored)\n")
    final_output.append("# ========================================\n\n")
    final_output.extend(top_viarules)
    
    # 添加 3D 键合 VIARULE
    final_output.extend(generate_3d_bond_viarule())
    
    # 结束
    final_output.append("\nEND LIBRARY\n")
    
    OUTPUT_LEF.write_text("".join(final_output), encoding="utf-8")
    
    # 统计信息
    bottom_metal = len([l for l in bottom_layers if re.match(r'^\s*LAYER\s+M\d+\s*$', l)])
    top_metal = len([l for l in top_layers if re.match(r'^\s*LAYER\s+M\d+\s*$', l)])
    bottom_via_count = len([l for l in bottom_vias if l.strip().startswith("VIA ")])
    top_via_count = len([l for l in top_vias if l.strip().startswith("VIA ")])
    
    print(f"✅ Generated: {OUTPUT_LEF}")
    print(f"   📊 Statistics:")
    print(f"      Bottom metal layers: {bottom_metal}")
    print(f"      Top metal layers: {top_metal}")
    print(f"      Bottom VIAs: {bottom_via_count}")
    print(f"      Top VIAs: {top_via_count}")
    print(f"      3D bond layers: 1 (V7_M8_BOND)")
    print(f"      Total lines: {len(final_output)}")


if __name__ == "__main__":
    main()

