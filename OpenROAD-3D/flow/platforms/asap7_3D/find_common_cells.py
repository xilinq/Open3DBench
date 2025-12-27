#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
找出 upper 和 bottom 共有的单元，并列出逻辑对应相同但名称不同的pin映射
"""

import os

# 文件路径
upper_file = 'lef_upper/asap7_upper.allcell'
bottom_file = 'lef_bottom/asap7_bottom.allcell'
output_file = 'asap7_hetero_common.allcell'

def parse_cell_file(filename, suffix):
    """解析单元文件，返回 {基础单元名: [pin列表]} 的字典"""
    cells = {}
    current_cell = None
    current_pins = []
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if not line:
                continue
            
            # 如果是单元名（不以空格开头）
            if not line.startswith(' ') and not line.startswith('\t'):
                # 保存上一个单元
                if current_cell is not None:
                    base_name = current_cell[:-len(suffix)]
                    cells[base_name] = current_pins.copy()
                
                # 开始新单元
                if line.endswith(suffix):
                    current_cell = line
                    current_pins = []
                else:
                    current_cell = None
                    current_pins = []
            # 如果是pin名称（以空格或制表符开头）
            elif current_cell is not None:
                pin_name = line.strip()
                if pin_name:
                    current_pins.append(pin_name)
        
        # 保存最后一个单元
        if current_cell is not None:
            base_name = current_cell[:-len(suffix)]
            cells[base_name] = current_pins.copy()
    
    return cells

# 解析两个文件
print('正在解析文件...')
upper_cells_dict = parse_cell_file(upper_file, '_upper')
bottom_cells_dict = parse_cell_file(bottom_file, '_bottom')

# 找出共同的单元
common_cells = sorted(set(upper_cells_dict.keys()) & set(bottom_cells_dict.keys()))

# 写入输出文件，包含pin映射信息
with open(output_file, 'w', encoding='utf-8') as f:
    for cell in common_cells:
        bottom_pins = bottom_cells_dict[cell]
        upper_pins = upper_cells_dict[cell]
        
        # 写入单元名
        f.write(cell + '\n')
        
        # 比较pin集合（不考虑顺序）
        bottom_pin_set = set(bottom_pins)
        upper_pin_set = set(upper_pins)
        
        # 如果pin集合相同，说明所有pin名称都相同，不需要映射
        if bottom_pin_set == upper_pin_set:
            # 所有pin名称都相同，不需要映射
            pass
        else:
            # pin集合不同，尝试找出逻辑对应相同但名称不同的pin映射
            # 首先检查pin数量是否相同
            if len(bottom_pins) == len(upper_pins):
                different_mappings = []
                used_upper = set()
                
                # 找出只在bottom或只在upper中的pin（名称不同）
                only_bottom = bottom_pin_set - upper_pin_set
                only_upper = upper_pin_set - bottom_pin_set
                
                # 尝试为每个bottom中的pin在upper中找到对应的pin
                for bottom_pin in sorted(only_bottom):
                    best_match = None
                    best_score = 0
                    
                    # 尝试匹配相似的pin名称
                    for upper_pin in only_upper:
                        if upper_pin in used_upper:
                            continue
                        
                        # 检查是否相似（一个去掉数字后缀后等于另一个）
                        # 例如：B1 对应 B，C1 对应 C
                        if bottom_pin.endswith('1') and bottom_pin[:-1] == upper_pin:
                            best_match = upper_pin
                            best_score = 1
                            break
                        elif upper_pin.endswith('1') and upper_pin[:-1] == bottom_pin:
                            best_match = upper_pin
                            best_score = 1
                            break
                        # 也可以尝试其他相似性规则
                        elif bottom_pin == upper_pin:
                            best_match = upper_pin
                            best_score = 2
                            break
                    
                    if best_match and best_score > 0:
                        different_mappings.append(f'{bottom_pin}->{best_match}')
                        used_upper.add(best_match)
                
                # 如果有名称不同的映射，写入
                if different_mappings:
                    for mapping in sorted(different_mappings):
                        f.write(f'  {mapping}\n')

print(f'Upper 单元总数: {len(upper_cells_dict)}')
print(f'Bottom 单元总数: {len(bottom_cells_dict)}')
print(f'共同单元数量: {len(common_cells)}')
print(f'结果已保存到 {output_file}')


