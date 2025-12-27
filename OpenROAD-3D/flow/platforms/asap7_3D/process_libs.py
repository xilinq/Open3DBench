import re
import sys

def extract_unique_strings(file_path):

    pattern = re.compile(r'cell \((.*?)\)')
    unique_strings = set()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                matches = pattern.findall(line)
                unique_strings.update(matches)
                
    except FileNotFoundError:
        print("Error: The file does not exist.")
        return []
    except IOError:
        print("Error: Failed to read the file.")
        return []
    
    return list(unique_strings)

def find_and_replace(file_path, search_text, replace_text):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        content = content.replace(search_text, replace_text)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print("File updated successfully.")
        
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Failed to read or write to the file.")

def replace_field_in_cell_names(input_lib, output_lib, old_field, new_field):
    """
    将.lib中所有 cell(name) 的名称里包含 old_field 的部分替换为 new_field。
    仅修改单元名本身，不做统一后缀追加。
    """
    try:
        with open(input_lib, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: The file does not exist.")
        return
    except IOError:
        print("Error: Failed to read the file.")
        return

    # 捕获 cell(name) 中的 name
    cell_pattern = re.compile(r'(?i)cell\s*\(\s*([^)]+?)\s*\)')  # (?i) 忽略大小写匹配 'cell'
    mapping = {}
    for m in cell_pattern.finditer(content):
        old_name = m.group(1)
        if old_field in old_name:
            new_name = old_name.replace(old_field, new_field)
            mapping[old_name] = new_name

    if not mapping:
        print("警告: 未找到包含指定旧字段的单元名称，文件将保持不变。")
        try:
            with open(output_lib, 'w', encoding='utf-8') as f:
                f.write(content)
        except IOError:
            print("Error: Failed to write to the file.")
        return

    # 应用映射：
    # 1) 定位并替换 cell (old) -> cell (new)
    # 2) 额外安全替换：当旧名以字符串被引用时 "old" -> "new"
    updated = content
    for old_name, new_name in mapping.items():
        # 替换 cell(...) 名称（仅替换 cell 行里的 name，避免误伤）
        updated = re.sub(
            rf'(?i)(\bcell\s*\(\s*){re.escape(old_name)}(\s*\))',
            rf'\1{new_name}\2',
            updated
        )
        # 替换被引号引用的完整单元名
        updated = re.sub(
            rf'"{re.escape(old_name)}"',
            f'"{new_name}"',
            updated
        )

    try:
        with open(output_lib, 'w', encoding='utf-8') as f:
            f.write(updated)
    except IOError:
        print("Error: Failed to write to the file.")
        return

    print("处理完成!")
    print(f"输入文件: {input_lib}")
    print(f"输出文件: {output_lib}")
    print(f"替换字段: {old_field} -> {new_field}")
    print(f"处理了 {len(mapping)} 个单元名")


def add_suffix_to_cell_names(input_lib, output_lib, suffix):
    """
    为 .lib 中所有 cell(name) 的名称添加统一后缀 suffix。
    """
    try:
        with open(input_lib, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: The file does not exist.")
        return
    except IOError:
        print("Error: Failed to read the file.")
        return

    cell_pattern = re.compile(r'(?i)cell\s*\(\s*([^)]+?)\s*\)')
    mapping = {}
    for m in cell_pattern.finditer(content):
        old_name = m.group(1)
        new_name = old_name + suffix
        mapping[old_name] = new_name

    updated = content
    for old_name, new_name in mapping.items():
        updated = re.sub(
            rf'(?i)(\bcell\s*\(\s*){re.escape(old_name)}(\s*\))',
            rf'\1{new_name}\2',
            updated
        )
        updated = re.sub(
            rf'"{re.escape(old_name)}"',
            f'"{new_name}"',
            updated
        )

    try:
        with open(output_lib, 'w', encoding='utf-8') as f:
            f.write(updated)
    except IOError:
        print("Error: Failed to write to the file.")
        return

    print("处理完成!")
    print(f"输入文件: {input_lib}")
    print(f"输出文件: {output_lib}")
    print(f"添加后缀: {suffix}")
    print(f"处理了 {len(mapping)} 个单元名")


def main():
    if len(sys.argv) < 4:
        print("用法:")
        print("  python process_libs.py <input_lib> <output_lib> <suffix>")
        print("  python process_libs.py <input_lib> <output_lib> --replace <old_field> <new_field>")
        print("示例:")
        print("  python process_libs.py input.lib output.lib _T0")
        print("  python process_libs.py input.lib output.lib --replace _BOT _TOP")
        sys.exit(1)

    input_lib = sys.argv[1]
    output_lib = sys.argv[2]
    op = sys.argv[3]

    if op == "--replace":
        if len(sys.argv) != 6:
            print("错误: --replace 模式需提供 old_field 与 new_field。")
            print("示例: python process_libs.py input.lib output.lib --replace _BOT _TOP")
            sys.exit(1)
        old_field = sys.argv[4]
        new_field = sys.argv[5]
        replace_field_in_cell_names(input_lib, output_lib, old_field, new_field)
    else:
        suffix = op
        if len(sys.argv) > 4:
            # 兼容旧用法，忽略多余参数
            pass
        add_suffix_to_cell_names(input_lib, output_lib, suffix)


if __name__ == "__main__":
    main()