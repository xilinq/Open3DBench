import os
import re
import numpy as np
from collections import defaultdict

# 调试开关和抽样设置
DEBUG = True
SAMPLE_CELLS = ['AND2x2', 'NAND2x1', 'NOR2x1']  # 抽样打印这些单元的详细信息
SAMPLE_COUNT = 3  # 每个阶段最多抽样打印的数量


def debug_print(msg, force=False):
    """调试打印函数"""
    if DEBUG or force:
        print(f"[DEBUG] {msg}")


def read_cells_from_allcell():
    """
    读取asap7_hetero_common.allcell文件中的所有单元
    忽略引脚映射和TIEHIx1、TIELOx1、FILLER、FILLERxp5、TAPCELL、TAPCELL_WITH_FILLER、DECAP系列单元
    """
    print("\n" + "="*60)
    print("阶段1: 读取单元列表")
    print("="*60)
    
    cells = []
    filtered_cells = ['TIEHIx1', 'TIELOx1', 'FILLER', 'FILLERxp5', 'TAPCELL', 'TAPCELL_WITH_FILLER', 'DECAP', 'CKINVDC']
    
    allcell_path = './asap7_hetero_common.allcell'
    debug_print(f"尝试读取文件: {os.path.abspath(allcell_path)}")
    
    try:
        with open(allcell_path, 'r') as f:
            lines = f.readlines()
            debug_print(f"文件总行数: {len(lines)}")
            
            for line_num, line in enumerate(lines, 1):
                original_line = line
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '->' in line or ':' in line:
                    continue
                cell_name = line.split()[0]
                if any(filtered in cell_name for filtered in filtered_cells):
                    debug_print(f"过滤掉单元: {cell_name}")
                    continue
                cells.append(cell_name)
                
    except FileNotFoundError:
        print("错误: 找不到文件 ./asap7_hetero_common.allcell")
        return []
    
    print(f"\n找到 {len(cells)} 个单元")
    print(f"前5个单元: {cells[:5]}")
    print(f"后5个单元: {cells[-5:]}")
    
    return cells


def find_matching_brace(content, start_pos):
    """
    从start_pos开始查找匹配的右大括号位置
    """
    count = 1
    pos = start_pos
    while pos < len(content) and count > 0:
        if content[pos] == '{':
            count += 1
        elif content[pos] == '}':
            count -= 1
        pos += 1
    return pos


def parse_lib_file(lib_path, sample_cells=None):
    """
    解析.lib文件，提取单元延迟信息
    返回格式: {cell_name: {timing_type: [(index_1, index_2, values), ...]}}
    """
    cell_delays = {}
    
    try:
        with open(lib_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"错误: 找不到文件 {lib_path}")
        return {}
    
    debug_print(f"文件大小: {len(content)} 字节")
    
    # 匹配cell块: cell (cell_name) { 格式（无引号）
    cell_pattern = re.compile(r'\bcell\s*\(\s*(\w+)\s*\)\s*\{')
    
    cell_matches = list(cell_pattern.finditer(content))
    debug_print(f"找到 {len(cell_matches)} 个cell定义")
    
    sampled_count = 0
    
    for i, match in enumerate(cell_matches):
        cell_name = match.group(1)
        # 去除 _upper 或 _bottom 后缀以统一单元名称
        base_cell_name = re.sub(r'_(upper|bottom)$', '', cell_name)
        
        # 判断是否需要详细打印
        should_sample = sample_cells and base_cell_name in sample_cells and sampled_count < SAMPLE_COUNT
        
        if should_sample:
            print(f"\n  --- 抽样单元: {cell_name} (base: {base_cell_name}) ---")
            sampled_count += 1
        
        start = match.end()
        # 找到匹配的右大括号
        end = find_matching_brace(content, start)
        cell_content = content[start:end]
        
        if should_sample:
            print(f"  cell内容长度: {len(cell_content)} 字符")
        
        cell_delays[base_cell_name] = {}
        
        # 匹配 cell_rise 或 cell_fall 块
        timing_block_pattern = re.compile(
            r'(cell_rise|cell_fall)\s*\(\s*\w+\s*\)\s*\{',
            re.MULTILINE
        )
        
        timing_matches = list(timing_block_pattern.finditer(cell_content))
        
        if should_sample:
            print(f"  找到 {len(timing_matches)} 个timing块 (cell_rise/cell_fall)")
        
        for timing_match in timing_matches:
            timing_type = timing_match.group(1)
            block_start = timing_match.end()
            block_end = find_matching_brace(cell_content, block_start)
            timing_block = cell_content[block_start:block_end]
            
            # 提取 index_1: index_1 ("5, 10, 20, 40, 80, 160, 320");
            index_1_match = re.search(r'index_1\s*\(\s*"([^"]+)"\s*\)', timing_block)
            # 提取 index_2: index_2 ("1.44, 2.88, 5.76, 11.52, 23.04, 46.08, 92.16");
            index_2_match = re.search(r'index_2\s*\(\s*"([^"]+)"\s*\)', timing_block)
            
            if should_sample:
                print(f"    {timing_type}: index_1找到={index_1_match is not None}, index_2找到={index_2_match is not None}")
            
            if not index_1_match or not index_2_match:
                if should_sample:
                    print(f"    跳过: 缺少index")
                    # 打印timing_block的前200字符帮助调试
                    print(f"    timing_block前200字符: {timing_block[:200]}...")
                continue
            
            index_1 = [float(x.strip()) for x in index_1_match.group(1).split(',')]
            index_2 = [float(x.strip()) for x in index_2_match.group(1).split(',')]
            
            if should_sample:
                print(f"    index_1 ({len(index_1)}个): {index_1[:3]}...{index_1[-1:]}")
                print(f"    index_2 ({len(index_2)}个): {index_2[:3]}...{index_2[-1:]}")
            
            # 提取 values 块
            values_match = re.search(
                r'values\s*\(\s*((?:[^;])+)\s*\)\s*;',
                timing_block,
                re.DOTALL
            )
            
            if not values_match:
                if should_sample:
                    print(f"    跳过: 未找到values块")
                continue
            
            values_str = values_match.group(1)
            values = []
            
            # 提取每行的值（在双引号内）
            row_pattern = re.compile(r'"([^"]+)"')
            for row_match in row_pattern.finditer(values_str):
                row_str = row_match.group(1)
                row_values = [float(x.strip()) for x in row_str.split(',') if x.strip()]
                if row_values:
                    values.append(row_values)
            
            if should_sample:
                print(f"    values: {len(values)}行 x {len(values[0]) if values else 0}列")
                if values:
                    print(f"    第一行前3个值: {values[0][:3]}")
            
            if values:
                if timing_type not in cell_delays[base_cell_name]:
                    cell_delays[base_cell_name][timing_type] = []
                cell_delays[base_cell_name][timing_type].append((index_1, index_2, values))
    
    return cell_delays


def calc_delay_parameters(cells):
    """
    计算单元在upper和bottom库之间的Δdelay，并拟合成Δdelay = a * Load + b的形式
    返回: {cell_name: (a, b)}
    """
    print("\n" + "="*60)
    print("阶段2: 解析lib文件")
    print("="*60)
    
    lib_bottom_dir = './lib_bottom/'
    lib_upper_dir = './lib_upper/'
    
    debug_print(f"bottom库目录: {os.path.abspath(lib_bottom_dir)}")
    debug_print(f"upper库目录: {os.path.abspath(lib_upper_dir)}")
    
    bottom_delays = {}
    upper_delays = {}
    
    # 解析bottom库
    print(f"\n--- 解析bottom库 ---")
    if os.path.exists(lib_bottom_dir):
        lib_files = [f for f in os.listdir(lib_bottom_dir) if f.endswith('.lib')]
        debug_print(f"找到 {len(lib_files)} 个.lib文件: {lib_files}")
        
        for lib_file in lib_files:
            lib_path = os.path.join(lib_bottom_dir, lib_file)
            print(f"正在解析: {lib_path}")
            delays = parse_lib_file(lib_path, SAMPLE_CELLS)
            debug_print(f"  解析到 {len(delays)} 个单元")
            bottom_delays.update(delays)
    else:
        print(f"警告: 目录 {lib_bottom_dir} 不存在")
    
    # 解析upper库
    print(f"\n--- 解析upper库 ---")
    if os.path.exists(lib_upper_dir):
        lib_files = [f for f in os.listdir(lib_upper_dir) if f.endswith('.lib')]
        debug_print(f"找到 {len(lib_files)} 个.lib文件: {lib_files}")
        
        for lib_file in lib_files:
            lib_path = os.path.join(lib_upper_dir, lib_file)
            print(f"正在解析: {lib_path}")
            delays = parse_lib_file(lib_path, SAMPLE_CELLS)
            debug_print(f"  解析到 {len(delays)} 个单元")
            upper_delays.update(delays)
    else:
        print(f"警告: 目录 {lib_upper_dir} 不存在")
    
    print(f"\n--- 解析结果汇总 ---")
    print(f"从bottom库解析到 {len(bottom_delays)} 个单元")
    print(f"从upper库解析到 {len(upper_delays)} 个单元")
    
    # 打印解析到的单元名称样本
    if bottom_delays:
        sample_keys = list(bottom_delays.keys())[:5]
        debug_print(f"bottom库单元样本: {sample_keys}")
    if upper_delays:
        sample_keys = list(upper_delays.keys())[:5]
        debug_print(f"upper库单元样本: {sample_keys}")
    
    print("\n" + "="*60)
    print("阶段3: 计算延迟参数")
    print("="*60)
    
    delay_parameters = {}
    missing_cells = []
    insufficient_data_cells = []
    
    for idx, cell in enumerate(cells):
        # 判断是否需要详细打印
        should_sample = cell in SAMPLE_CELLS
        
        if cell not in bottom_delays:
            missing_cells.append((cell, 'bottom'))
            if should_sample:
                print(f"\n  [抽样] 单元 {cell} 在bottom库中未找到")
            continue
        if cell not in upper_delays:
            missing_cells.append((cell, 'upper'))
            if should_sample:
                print(f"\n  [抽样] 单元 {cell} 在upper库中未找到")
            continue
        
        if should_sample:
            print(f"\n  --- 抽样计算: {cell} ---")
            print(f"  bottom库timing类型: {list(bottom_delays[cell].keys())}")
            print(f"  upper库timing类型: {list(upper_delays[cell].keys())}")
        
        loads = []
        delta_delays = []
        
        for timing_type in ['cell_rise', 'cell_fall']:
            if timing_type not in bottom_delays[cell] or timing_type not in upper_delays[cell]:
                if should_sample:
                    print(f"    {timing_type}: 跳过 (bottom有={timing_type in bottom_delays[cell]}, upper有={timing_type in upper_delays[cell]})")
                continue
            
            bottom_timings = bottom_delays[cell][timing_type]
            upper_timings = upper_delays[cell][timing_type]
            
            if should_sample:
                print(f"    {timing_type}: bottom有{len(bottom_timings)}组, upper有{len(upper_timings)}组")
            
            # 取较小的数量进行匹配
            num_timings = min(len(bottom_timings), len(upper_timings))
            
            for t_idx in range(num_timings):
                b_index_1, b_index_2, b_values = bottom_timings[t_idx]
                u_index_1, u_index_2, u_values = upper_timings[t_idx]
                
                if should_sample and t_idx == 0:
                    print(f"      组{t_idx}: b_index_2={b_index_2[:3]}..., u_index_2={u_index_2[:3]}...")
                    print(f"      组{t_idx}: b_values形状={len(b_values)}x{len(b_values[0]) if b_values else 0}")
                    print(f"      组{t_idx}: u_values形状={len(u_values)}x{len(u_values[0]) if u_values else 0}")
                
                # index_2 是 output load (电容负载)
                num_rows = min(len(b_values), len(u_values))
                num_cols = min(len(b_index_2), len(u_index_2))
                
                for j in range(num_rows):  # 遍历 input slew
                    for i in range(num_cols):  # 遍历 output load
                        if i < len(b_values[j]) and i < len(u_values[j]):
                            load = b_index_2[i]
                            delta = u_values[j][i] - b_values[j][i]
                            loads.append(load)
                            delta_delays.append(delta)
        
        if should_sample:
            print(f"  收集到 {len(loads)} 个数据点")
            if loads:
                print(f"  load范围: [{min(loads):.2f}, {max(loads):.2f}]")
                print(f"  delta_delay范围: [{min(delta_delays):.2f}, {max(delta_delays):.2f}]")
        
        if len(loads) >= 2:
            # 线性拟合: Δdelay = a * Load + b
            loads_array = np.array(loads)
            delta_delays_array = np.array(delta_delays)
            
            # 使用最小二乘法拟合
            A = np.vstack([loads_array, np.ones(len(loads_array))]).T
            result = np.linalg.lstsq(A, delta_delays_array, rcond=None)
            a, b = result[0]
            
            delay_parameters[cell] = (a, b)
            
            if should_sample:
                print(f"  拟合结果: a={a:.6e}, b={b:.6e}")
                # 计算拟合优度
                predicted = a * loads_array + b
                ss_res = np.sum((delta_delays_array - predicted) ** 2)
                ss_tot = np.sum((delta_delays_array - np.mean(delta_delays_array)) ** 2)
                r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
                print(f"  R² = {r_squared:.4f}")
        else:
            insufficient_data_cells.append((cell, len(loads)))
            if should_sample:
                print(f"  警告: 数据点不足 ({len(loads)} 个)，无法拟合")
    
    # 打印汇总信息
    print(f"\n--- 计算结果汇总 ---")
    print(f"成功计算: {len(delay_parameters)} 个单元")
    print(f"缺失单元: {len(missing_cells)} 个")
    print(f"数据不足: {len(insufficient_data_cells)} 个")
    
    if missing_cells and len(missing_cells) <= 10:
        print(f"缺失单元详情: {missing_cells}")
    elif missing_cells:
        print(f"缺失单元样本: {missing_cells[:5]}...")
    
    if insufficient_data_cells and len(insufficient_data_cells) <= 10:
        print(f"数据不足单元: {insufficient_data_cells}")
    elif insufficient_data_cells:
        print(f"数据不足样本: {insufficient_data_cells[:5]}...")
    
    return delay_parameters


def output_delay_parameters(delay_parameters, output_file='cell_delay_info.csv'):
    """
    输出参数到cell_delay_info.csv文件
    格式: cell_name,a,b
    """
    print("\n" + "="*60)
    print("阶段4: 输出结果")
    print("="*60)
    
    try:
        with open(output_file, 'w') as f:
            f.write('cell_name,a,b\n')
            for cell_name, (a, b) in sorted(delay_parameters.items()):
                f.write(f'{cell_name},{a:.6e},{b:.6e}\n')
        
        print(f"延迟参数已输出到 {os.path.abspath(output_file)}")
        print(f"共写入 {len(delay_parameters)} 条记录")
        
        # 打印样本
        sample_items = list(delay_parameters.items())[:3]
        print(f"\n输出样本:")
        for cell_name, (a, b) in sample_items:
            print(f"  {cell_name}: a={a:.6e}, b={b:.6e}")
            
    except IOError as e:
        print(f"错误: 无法写入文件 {output_file}: {e}")


if __name__ == '__main__':
    print("="*60)
    print("Cell Delay Parameter Extraction Tool")
    print(f"工作目录: {os.getcwd()}")
    print(f"调试模式: {DEBUG}")
    print(f"抽样单元: {SAMPLE_CELLS}")
    print("="*60)
    
    # 读取所有单元
    cells = read_cells_from_allcell()
    
    if cells:
        # 计算延迟参数
        delay_parameters = calc_delay_parameters(cells)
        
        # 输出延迟参数
        if delay_parameters:
            output_delay_parameters(delay_parameters)
            print(f"\n{'='*60}")
            print(f"完成! 成功处理 {len(delay_parameters)} 个单元")
            print(f"{'='*60}")
        else:
            print("\n警告: 没有计算出任何延迟参数")
    else:
        print("\n错误: 没有读取到任何单元")