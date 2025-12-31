#!/usr/bin/env python3
"""
Extract leakage power information for cells from Liberty files.
"""

import os
import re
import csv
import glob


def read_target_cells(allcell_file):
    """Read target cell names from allcell file, ignoring pin mappings."""
    cells = set()
    with open(allcell_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            # Skip pin mapping lines (contain "->")
            if '->' in line:
                continue
            # Format: cell_name [pin_mapping] - we only need cell_name
            cell_name = line.split()[0]
            cells.add(cell_name)
    return cells


def extract_leakage_blocks(cell_content):
    """Extract all leakage_power blocks from cell content, handling nested braces."""
    blocks = []
    pattern = re.compile(r'leakage_power\s*\(\s*\)\s*\{')
    
    for match in pattern.finditer(cell_content):
        start_pos = match.end()
        brace_count = 1
        pos = start_pos
        
        while brace_count > 0 and pos < len(cell_content):
            if cell_content[pos] == '{':
                brace_count += 1
            elif cell_content[pos] == '}':
                brace_count -= 1
            pos += 1
        
        block_content = cell_content[start_pos:pos-1]
        blocks.append(block_content)
    
    return blocks


def parse_lib_for_leakage(lib_dir):
    """Parse all .lib files in directory and extract leakage power for each cell.
    
    Liberty file structure:
    cell (cell_name) {
        ...
        leakage_power () {
            value : 943.483;        <- This is the average/default leakage (no 'when')
            related_pg_pin : VDD;
        }
        ...
    }
    
    We want the leakage_power block that:
    1. Has NO 'when' condition (it's the default/average leakage)
    2. Has related_pg_pin : VDD (not VSS which is always 0)
    """
    leakage_info = {}
    lib_files = glob.glob(os.path.join(lib_dir, '*.lib'))
    
    for lib_file in lib_files:
        print(f"  Parsing {lib_file}...")
        with open(lib_file, 'r') as f:
            content = f.read()
        
        # Find all cell blocks
        cell_starts = list(re.finditer(r'\bcell\s*\(\s*(\w+)\s*\)\s*\{', content))
        
        for i, match in enumerate(cell_starts):
            cell_name = match.group(1)
            start_pos = match.end()
            
            # Find the end of this cell block by counting braces
            brace_count = 1
            pos = start_pos
            while brace_count > 0 and pos < len(content):
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                pos += 1
            
            cell_content = content[start_pos:pos-1]
            
            # Extract all leakage_power blocks
            leakage_blocks = extract_leakage_blocks(cell_content)
            
            avg_leakage = None
            for block in leakage_blocks:
                # Check if this block has 'when' condition
                has_when = re.search(r'\bwhen\s*:', block) is not None
                
                if has_when:
                    continue  # Skip blocks with 'when' condition
                
                # Extract value
                value_match = re.search(r'value\s*:\s*([\d.eE+-]+)\s*;', block)
                if not value_match:
                    continue
                    
                value = float(value_match.group(1))
                
                # Check related_pg_pin - we want VDD (non-zero) not VSS (zero)
                pg_pin_match = re.search(r'related_pg_pin\s*:\s*(\w+)\s*;', block)
                if pg_pin_match:
                    pg_pin = pg_pin_match.group(1)
                    if pg_pin == 'VDD':
                        avg_leakage = value
                        break
                else:
                    # If no related_pg_pin specified, take this value if it's non-zero
                    if value > 0:
                        avg_leakage = value
                        break
            
            if avg_leakage is not None:
                if cell_name not in leakage_info:
                    leakage_info[cell_name] = avg_leakage
    
    return leakage_info


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # File paths
    allcell_file = os.path.join(script_dir, 'asap7_hetero_common.allcell')
    lib_bottom_dir = os.path.join(script_dir, 'lib_bottom')
    lib_upper_dir = os.path.join(script_dir, 'lib_upper')
    output_file = os.path.join(script_dir, 'leakage_info.csv')
    
    # Step 1: Read target cells
    print(f"Reading target cells from {allcell_file}...")
    target_cells = read_target_cells(allcell_file)
    print(f"Found {len(target_cells)} target cells")
    
    # Step 2: Parse lib files
    print(f"Parsing lib files from {lib_bottom_dir}...")
    leakage_bottom_raw = parse_lib_for_leakage(lib_bottom_dir)
    print(f"Found leakage info for {len(leakage_bottom_raw)} cells in lib_bottom")
    
    print(f"Parsing lib files from {lib_upper_dir}...")
    leakage_upper_raw = parse_lib_for_leakage(lib_upper_dir)
    print(f"Found leakage info for {len(leakage_upper_raw)} cells in lib_upper")
    
    # Debug: show some samples
    if leakage_bottom_raw:
        sample = list(leakage_bottom_raw.items())[:5]
        print(f"Sample leakage_bottom_raw: {sample}")
    if leakage_upper_raw:
        sample = list(leakage_upper_raw.items())[:5]
        print(f"Sample leakage_upper_raw: {sample}")
    
    # Step 3: Output CSV
    # Map cell names: lib uses cell_name + "_bottom" or "_upper" suffix
    print(f"Writing results to {output_file}...")
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['cell', 'leakage_bottom', 'leakage_upper'])
        
        for cell in sorted(target_cells):
            # Look up with suffix
            cell_bottom = cell + "_bottom"
            cell_upper = cell + "_upper"
            
            lb = leakage_bottom_raw.get(cell_bottom, '')
            lu = leakage_upper_raw.get(cell_upper, '')
            writer.writerow([cell, lb, lu])
    
    print(f"Done! Results written to {output_file}")


if __name__ == '__main__':
    main()