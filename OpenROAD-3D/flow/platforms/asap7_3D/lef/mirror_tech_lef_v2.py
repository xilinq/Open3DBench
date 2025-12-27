#!/usr/bin/env python3
"""
将 2D tech LEF 改造为 F2F 3DIC 架构：
- 底部芯片: M1-M7 (保持原名)
- 顶部芯片: M8-M14 (镜像 M7-M1)
- 3D 互连: M7 ↔ M8 键合

Input:  asap7_tech_1x_201209.lef
Output: asap7_tech_f2f_3d.lef
"""

from __future__ import annotations
import re
from pathlib import Path
from typing import List, Dict

THIS_DIR = Path(__file__).parent
INPUT_LEF = THIS_DIR / "asap7_tech_1x_201209.lef"
OUTPUT_LEF = THIS_DIR / "asap7_tech_f2f_3d.lef"

# 层映射配置
BOTTOM_LAYERS = ["M1", "M2", "M3", "M4", "M5", "M6", "M7"]
TOP_LAYER_MAP = {
    "M7": "M8",  "V6": "V8",
    "M6": "M9",  "V5": "V9",
    "M5": "M10", "V4": "V10",
    "M4": "M11", "V3": "V11",
    "M3": "M12", "V2": "V12",
    "M2": "M13", "V1": "V13",
    "M1": "M14", "V0": "V14",
}

# VIA 重命名映射
VIA_RENAME_MAP = {
    "VIA67": "VIA78",
    "VIA56": "VIA89",
    "VIA45": "VIA910",
    "VIA34": "VIA1011",
    "VIA23": "VIA1112",
    "VIA12": "VIA1213",
}

# VIARULE 重命名映射
VIARULE_RENAME_MAP = {
    "M7_M6": "M8_M9",
    "M6_M5": "M9_M10",
    "M5_M4": "M10_M11",
    "M4_M3": "M11_M12",
    "M3_M2": "M12_M13",
    "M2_M1": "M13_M14",
    # 电源宽通孔
    "M7_M6widePWR1p152": "M8_M9widePWR1p152",
    "M6_M5widePWR1p152": "M9_M10widePWR1p152",
    "M5_M4widePWR0p864": "M10_M11widePWR0p864",
    "M4_M3widePWR0p864": "M11_M12widePWR0p864",
    "M3_M2widePWR0p936": "M12_M13widePWR0p936",
}


def read_lef_lines(path: Path) -> List[str]:
    return path.read_text(encoding="utf-8").splitlines(keepends=True)


def find_end_library_index(lines: List[str]) -> int:
    for idx, line in enumerate(lines):
        if line.strip() == "END LIBRARY":
            return idx
    raise RuntimeError("END LIBRARY not found")


def should_keep_layer(layer_name: str) -> bool:
    """判断底部芯片是否保留该层"""
    # 保留 M1-M7 及其对应的 VIA
    if layer_name in BOTTOM_LAYERS:
        return True
    if layer_name in ["V0", "V1", "V2", "V3", "V4", "V5", "V6"]:
        return True
    # 保留工艺基础层
    if layer_name in ["nwell", "pwell", "Gate", "Active"]:
        return True
    return False


def collect_layer_block(lines: List[str], start_idx: int) -> tuple[List[str], int]:
    """收集完整的 LAYER 块"""
    block = [lines[start_idx]]
    header = lines[start_idx].strip()
    m = re.match(r"^\s*LAYER\s+(\S+)", header)
    if not m:
        raise ValueError(f"Invalid LAYER header: {header}")
    layer_name = m.group(1)
    
    i = start_idx + 1
    while i < len(lines):
        block.append(lines[i])
        if lines[i].strip() == f"END {layer_name}":
            return block, i + 1
        i += 1
    raise RuntimeError(f"No END found for LAYER {layer_name}")


def rename_layer_references(text: str, mapping: Dict[str, str]) -> str:
    """替换文本中的层名引用"""
    for old_name, new_name in mapping.items():
        # 匹配 LAYER 语句
        text = re.sub(rf'\bLAYER\s+{old_name}\b', f'LAYER {new_name}', text)
        # 匹配 END 语句
        text = re.sub(rf'\bEND\s+{old_name}\b', f'END {new_name}', text)
    return text


def mirror_layer_block(block: List[str]) -> List[str]:
    """镜像层块并重命名"""
    text = "".join(block)
    
    # 提取原层名
    header = block[0].strip()
    m = re.match(r"^\s*LAYER\s+(\S+)", header)
    if not m:
        return block
    old_name = m.group(1)
    
    # 查找映射
    if old_name not in TOP_LAYER_MAP:
        return block
    
    new_name = TOP_LAYER_MAP[old_name]
    
    # 重命名层名
    text = rename_layer_references(text, {old_name: new_name})
    
    return text.splitlines(keepends=True)


def collect_via_block(lines: List[str], start_idx: int) -> tuple[List[str], int]:
    """收集完整的 VIA 块"""
    block = [lines[start_idx]]
    header = lines[start_idx].strip()
    m = re.match(r"^\s*VIA\s+(\S+)", header)
    if not m:
        raise ValueError(f"Invalid VIA header: {header}")
    via_name = m.group(1)
    
    i = start_idx + 1
    while i < len(lines):
        block.append(lines[i])
        if lines[i].strip() == f"END {via_name}":
            return block, i + 1
        i += 1
    raise RuntimeError(f"No END found for VIA {via_name}")


def mirror_via_block(block: List[str]) -> List[str]:
    """镜像 VIA 块并重命名"""
    text = "".join(block)
    
    # 提取原 VIA 名
    header = block[0].strip()
    m = re.match(r"^\s*VIA\s+(\S+)", header)
    if not m:
        return block
    old_name = m.group(1)
    
    # 查找映射
    if old_name not in VIA_RENAME_MAP:
        return block
    
    new_name = VIA_RENAME_MAP[old_name]
    
    # 重命名 VIA 和内部 LAYER 引用
    text = re.sub(rf'\bVIA\s+{old_name}\b', f'VIA {new_name}', text)
    text = re.sub(rf'\bEND\s+{old_name}\b', f'END {new_name}', text)
    text = rename_layer_references(text, TOP_LAYER_MAP)
    
    return text.splitlines(keepends=True)


def collect_viarule_block(lines: List[str], start_idx: int) -> tuple[List[str], int]:
    """收集完整的 VIARULE 块"""
    block = [lines[start_idx]]
    header = lines[start_idx].strip()
    m = re.match(r"^\s*VIARULE\s+(\S+)", header)
    if not m:
        raise ValueError(f"Invalid VIARULE header: {header}")
    rule_name = m.group(1)
    
    i = start_idx + 1
    while i < len(lines):
        block.append(lines[i])
        if lines[i].strip() == f"END {rule_name}":
            return block, i + 1
        i += 1
    raise RuntimeError(f"No END found for VIARULE {rule_name}")


def mirror_viarule_block(block: List[str]) -> List[str]:
    """镜像 VIARULE 块并重命名"""
    text = "".join(block)
    
    # 提取原 VIARULE 名
    header = block[0].strip()
    m = re.match(r"^\s*VIARULE\s+(\S+)", header)
    if not m:
        return block
    old_name = m.group(1)
    
    # 查找映射
    if old_name not in VIARULE_RENAME_MAP:
        return block
    
    new_name = VIARULE_RENAME_MAP[old_name]
    
    # 重命名 VIARULE 和内部 LAYER 引用
    text = re.sub(rf'\bVIARULE\s+{old_name}\b', f'VIARULE {new_name}', text)
    text = re.sub(rf'\bEND\s+{old_name}\b', f'END {new_name}', text)
    text = rename_layer_references(text, TOP_LAYER_MAP)
    
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


def main():
    lines = read_lef_lines(INPUT_LEF)
    end_idx = find_end_library_index(lines)
    
    output_lines = []
    i = 0
    
    # 阶段标记
    in_layer_section = False
    in_via_section = False
    in_viarule_section = False
    
    bottom_layers = []
    top_layers = []
    bottom_vias = []
    top_vias = []
    bottom_viarules = []
    top_viarules = []
    
    while i < end_idx:
        line = lines[i]
        
        # 检测 LAYER 区域
        if re.match(r"^\s*LAYER\s+\S+\s*$", line):
            block, next_i = collect_layer_block(lines, i)
            layer_name = re.match(r"^\s*LAYER\s+(\S+)", block[0]).group(1)
            
            if should_keep_layer(layer_name):
                bottom_layers.extend(block)
            
            # 如果是需要镜像的层
            if layer_name in TOP_LAYER_MAP:
                mirrored = mirror_layer_block(block)
                top_layers.extend(mirrored)
            
            i = next_i
            continue
        
        # 检测 VIA 区域
        if re.match(r"^\s*VIA\s+\S+", line):
            in_via_section = True
            block, next_i = collect_via_block(lines, i)
            via_name = re.match(r"^\s*VIA\s+(\S+)", block[0]).group(1)
            
            bottom_vias.extend(block)
            
            if via_name in VIA_RENAME_MAP:
                mirrored = mirror_via_block(block)
                top_vias.extend(mirrored)
            
            i = next_i
            continue
        
        # 检测 VIARULE 区域
        if re.match(r"^\s*VIARULE\s+\S+", line):
            in_viarule_section = True
            block, next_i = collect_viarule_block(lines, i)
            rule_name = re.match(r"^\s*VIARULE\s+(\S+)", block[0]).group(1)
            
            bottom_viarules.extend(block)
            
            if rule_name in VIARULE_RENAME_MAP:
                mirrored = mirror_viarule_block(block)
                top_viarules.extend(mirrored)
            
            i = next_i
            continue
        
        # 其他行直接保留
        if i < end_idx:
            output_lines.append(line)
        
        i += 1
    
    # 组装最终输出
    final_output = []
    final_output.extend(output_lines)
    
    # 添加底部芯片层
    final_output.append("\n# ========================================\n")
    final_output.append("# Bottom Die Layers (M1-M7)\n")
    final_output.append("# ========================================\n\n")
    final_output.extend(bottom_layers)
    
    # 添加顶部芯片层
    final_output.append("\n# ========================================\n")
    final_output.append("# Top Die Layers (M8-M14, mirrored)\n")
    final_output.append("# ========================================\n\n")
    final_output.extend(top_layers)
    
    # 添加 3D 键合层
    final_output.extend(generate_3d_bond_layer())
    
    # 添加底部 VIA
    final_output.append("# ========================================\n")
    final_output.append("# Bottom Die VIAs\n")
    final_output.append("# ========================================\n\n")
    final_output.extend(bottom_vias)
    
    # 添加顶部 VIA
    final_output.append("\n# ========================================\n")
    final_output.append("# Top Die VIAs (mirrored)\n")
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
    
    # 结束
    final_output.append("\nEND LIBRARY\n")
    
    OUTPUT_LEF.write_text("".join(final_output), encoding="utf-8")
    print(f"✅ Generated: {OUTPUT_LEF}")
    print(f"   Bottom layers: {len([l for l in bottom_layers if 'LAYER M' in l])} metal layers")
    print(f"   Top layers: {len([l for l in top_layers if 'LAYER M' in l])} metal layers")


if __name__ == "__main__":
    main()

