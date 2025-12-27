import os
import re
import argparse
import shutil

def find_lib_files(directory):
    """Find all .lib files in the given directory."""
    lib_files = []
    if os.path.exists(directory):
        for f in os.listdir(directory):
            if f.endswith('.lib'):
                lib_files.append(os.path.join(directory, f))
    return lib_files

def extract_cell_names(lib_file):
    """Extract cell names from a .lib file."""
    cell_names = []
    cell_pattern = re.compile(r'^\s*cell\s*\(\s*"?([^")\s]+)"?\s*\)')
    with open(lib_file, 'r') as f:
        for line in f:
            match = cell_pattern.match(line)
            if match:
                cell_names.append(match.group(1))
    return cell_names

def check_suffix(cell_names, suffix, lib_file):
    """Check if cell names have the given suffix and print them."""
    found = []
    for name in cell_names:
        if name.endswith(suffix):
            found.append(name)
    return found

def normalize_cell_name(cell_name, target_suffix):
    """
    Normalize cell name to have exactly one target suffix (_bottom or _upper).
    Remove any existing _bottom/_upper suffixes first, then add the target suffix.
    
    Args:
        cell_name: Original cell name
        target_suffix: Either '_bottom' or '_upper'
    
    Returns:
        Normalized cell name with exactly one target suffix
    """
    # Remove all trailing _bottom and _upper suffixes
    base_name = cell_name
    while base_name.endswith('_bottom') or base_name.endswith('_upper'):
        if base_name.endswith('_bottom'):
            base_name = base_name[:-7]  # len('_bottom') = 7
        elif base_name.endswith('_upper'):
            base_name = base_name[:-6]  # len('_upper') = 6
    
    # Add the target suffix
    return base_name + target_suffix

def fix_lib_file(lib_file, target_suffix, dry_run=False):
    """
    Fix cell names in a .lib file to have exactly one target suffix.
    
    Args:
        lib_file: Path to the .lib file
        target_suffix: Either '_bottom' or '_upper'
        dry_run: If True, only report changes without modifying the file
    
    Returns:
        List of (old_name, new_name) tuples for changed cells
    """
    changes = []
    
    with open(lib_file, 'r') as f:
        content = f.read()
    
    original_content = content
    
    # Extract all cell names first
    cell_names = extract_cell_names(lib_file)
    
    for cell_name in cell_names:
        new_name = normalize_cell_name(cell_name, target_suffix)
        
        if new_name != cell_name:
            changes.append((cell_name, new_name))
            
            if not dry_run:
                # Replace cell name in cell definition: cell(name) or cell("name")
                # Pattern 1: cell(name)
                content = re.sub(
                    r'\bcell\s*\(\s*' + re.escape(cell_name) + r'\s*\)',
                    f'cell({new_name})',
                    content
                )
                # Pattern 2: cell("name")
                content = re.sub(
                    r'\bcell\s*\(\s*"' + re.escape(cell_name) + r'"\s*\)',
                    f'cell("{new_name}")',
                    content
                )
                
                # Replace cell references in other places (e.g., cell_footprint, related_pin, etc.)
                # Be careful to only replace whole word matches
                content = re.sub(
                    r'\b' + re.escape(cell_name) + r'\b',
                    new_name,
                    content
                )
    
    # Write changes if not dry run and content changed
    if not dry_run and content != original_content:
        # Backup original file
        backup_file = lib_file + '.bak'
        shutil.copy2(lib_file, backup_file)
        
        with open(lib_file, 'w') as f:
            f.write(content)
    
    return changes

def check_mode():
    """Original check-only mode."""
    # Check lib_bottom directory for cells with '_bottom' suffix
    print("Checking ./lib_bottom for cells with '_bottom' suffix:")
    bottom_files = find_lib_files('./lib_bottom')
    for lib_file in bottom_files:
        cell_names = extract_cell_names(lib_file)
        cells_with_suffix = check_suffix(cell_names, '_bottom', lib_file)
        if cells_with_suffix:
            print(f"\n  File: {lib_file}")
            for cell in cells_with_suffix:
                print(f"    {cell}")
    
    # Check lib_upper directory for cells with '_upper' suffix
    print("\nChecking ./lib_upper for cells with '_upper' suffix:")
    upper_files = find_lib_files('./lib_upper')
    for lib_file in upper_files:
        cell_names = extract_cell_names(lib_file)
        cells_with_suffix = check_suffix(cell_names, '_upper', lib_file)
        if cells_with_suffix:
            print(f"\n  File: {lib_file}")
            for cell in cells_with_suffix:
                print(f"    {cell}")

def fix_mode(dry_run=False):
    """Fix cell names to have exactly one suffix."""
    mode_str = "DRY RUN - " if dry_run else ""
    
    # Fix lib_bottom directory
    print(f"\n{mode_str}Fixing ./lib_bottom cells to have exactly one '_bottom' suffix:")
    bottom_files = find_lib_files('./lib_bottom')
    total_bottom_changes = 0
    for lib_file in bottom_files:
        changes = fix_lib_file(lib_file, '_bottom', dry_run=dry_run)
        if changes:
            print(f"\n  File: {lib_file}")
            for old_name, new_name in changes:
                print(f"    {old_name} -> {new_name}")
            total_bottom_changes += len(changes)
    
    if total_bottom_changes == 0:
        print("  No changes needed.")
    else:
        print(f"\n  Total changes in lib_bottom: {total_bottom_changes}")
    
    # Fix lib_upper directory
    print(f"\n{mode_str}Fixing ./lib_upper cells to have exactly one '_upper' suffix:")
    upper_files = find_lib_files('./lib_upper')
    total_upper_changes = 0
    for lib_file in upper_files:
        changes = fix_lib_file(lib_file, '_upper', dry_run=dry_run)
        if changes:
            print(f"\n  File: {lib_file}")
            for old_name, new_name in changes:
                print(f"    {old_name} -> {new_name}")
            total_upper_changes += len(changes)
    
    if total_upper_changes == 0:
        print("  No changes needed.")
    else:
        print(f"\n  Total changes in lib_upper: {total_upper_changes}")
    
    if not dry_run and (total_bottom_changes > 0 or total_upper_changes > 0):
        print("\n[Note] Backup files (.bak) have been created for modified files.")

def main():
    parser = argparse.ArgumentParser(
        description='Check and fix cell names in .lib files to ensure exactly one _bottom/_upper suffix.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python fix_lib_cell_name.py              # Check mode (default, original behavior)
  python fix_lib_cell_name.py --fix        # Fix cell names (creates .bak backups)
  python fix_lib_cell_name.py --dry-run    # Show what would be changed without modifying files
        '''
    )
    parser.add_argument(
        '--fix', 
        action='store_true',
        help='Fix cell names to have exactly one _bottom/_upper suffix'
    )
    parser.add_argument(
        '--dry-run', 
        action='store_true',
        help='Show changes without modifying files (implies --fix mode)'
    )
    
    args = parser.parse_args()
    
    if args.dry_run:
        fix_mode(dry_run=True)
    elif args.fix:
        fix_mode(dry_run=False)
    else:
        check_mode()

if __name__ == '__main__':
    main()
