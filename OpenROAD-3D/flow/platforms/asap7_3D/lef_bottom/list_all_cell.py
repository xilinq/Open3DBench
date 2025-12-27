#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
读取 LEF 文件，提取所有单元名称及其所有 pin 名称并保存到输出文件
"""

import re
import os

# 输入和输出文件路径
lef_file = 'asap7_bottom.lef'
output_file = 'asap7_bottom.allcell'

# 存储所有单元信息：{cell_name: [pin1, pin2, ...]}
cells = {}

# 当前正在处理的单元名称
current_cell = None
# 当前单元的所有 pin 名称
current_pins = []

# 读取 LEF 文件
with open(lef_file, 'r', encoding='utf-8') as f:
    for line in f:
        line_stripped = line.strip()
        
        # 查找以 MACRO 开头的行，开始新的单元
        if line_stripped.startswith('MACRO'):
            # 如果之前有单元，先保存
            if current_cell is not None:
                cells[current_cell] = current_pins.copy()
            
            # 提取单元名称（MACRO 后面的部分）
            match = re.match(r'MACRO\s+(\S+)', line_stripped)
            if match:
                current_cell = match.group(1)
                current_pins = []
        
        # 查找以 PIN 开头的行，提取 pin 名称
        elif line_stripped.startswith('PIN') and current_cell is not None:
            match = re.match(r'PIN\s+(\S+)', line_stripped)
            if match:
                pin_name = match.group(1)
                current_pins.append(pin_name)
        
        # 查找以 END 开头的行，检查是否是当前单元的结束
        elif line_stripped.startswith('END') and current_cell is not None:
            match = re.match(r'END\s+(\S+)', line_stripped)
            if match and match.group(1) == current_cell:
                # 保存当前单元
                cells[current_cell] = current_pins.copy()
                current_cell = None
                current_pins = []

# 保存最后一个单元（如果文件没有以 END 结束）
if current_cell is not None:
    cells[current_cell] = current_pins.copy()

# 对单元名称进行排序
sorted_cells = sorted(cells.keys())

# 写入输出文件
with open(output_file, 'w', encoding='utf-8') as f:
    for cell in sorted_cells:
        pins = cells[cell]
        # 写入单元名称
        f.write(f'{cell}\n')
        # 写入该单元的所有 pin 名称
        for pin in pins:
            f.write(f'  {pin}\n')

total_cells = len(cells)
total_pins = sum(len(pins) for pins in cells.values())
print(f'成功提取 {total_cells} 个单元，共 {total_pins} 个 pin，已保存到 {output_file}')

