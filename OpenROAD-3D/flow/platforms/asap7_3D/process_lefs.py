import re
import sys

def add_suffix_to_macros(input_lef, output_lef, suffix):
    """
    为LEF文件中的所有MACRO添加后缀
    
    Args:
        input_lef: 输入LEF文件路径
        output_lef: 输出LEF文件路径
        suffix: 要添加的后缀字符串
    """
    with open(input_lef, 'r') as f:
        content = f.read()
    
    macro_mapping = {}
    macro_pattern = r'MACRO\s+(\S+)'
    for match in re.finditer(macro_pattern, content):
        original_name = match.group(1)
        new_name = original_name + suffix
        macro_mapping[original_name] = new_name
    
    content = _apply_macro_mapping(content, macro_mapping)
    
    with open(output_lef, 'w') as f:
        f.write(content)
    
    print("处理完成!")
    print(f"输入文件: {input_lef}")
    print(f"输出文件: {output_lef}")
    print(f"添加后缀: {suffix}")
    print(f"处理了 {len(macro_mapping)} 个MACRO单元")


def replace_field_in_macros(input_lef, output_lef, old_field, new_field):
    """
    替换MACRO名称中的自定义字段
    
    Args:
        input_lef: 输入LEF文件路径
        output_lef: 输出LEF文件路径
        old_field: 需要被替换的字段
        new_field: 替换后的字段
    """
    with open(input_lef, 'r') as f:
        content = f.read()
    
    macro_mapping = {}
    macro_pattern = r'MACRO\s+(\S+)'
    for match in re.finditer(macro_pattern, content):
        original_name = match.group(1)
        if old_field in original_name:
            new_name = original_name.replace(old_field, new_field)
            macro_mapping[original_name] = new_name
    
    if not macro_mapping:
        print("警告: 未找到包含指定旧字段的MACRO名称，文件将保持不变。")
        with open(output_lef, 'w') as f:
            f.write(content)
        return
    
    content = _apply_macro_mapping(content, macro_mapping)
    
    with open(output_lef, 'w') as f:
        f.write(content)
    
    print("处理完成!")
    print(f"输入文件: {input_lef}")
    print(f"输出文件: {output_lef}")
    print(f"替换字段: {old_field} -> {new_field}")
    print(f"处理了 {len(macro_mapping)} 个MACRO单元")


def _apply_macro_mapping(content, macro_mapping):
    """
    将MACRO名称映射关系应用到LEF内容中
    """
    for original_name, new_name in macro_mapping.items():
        content = re.sub(
            r'\bMACRO\s+' + re.escape(original_name) + r'\b',
            f'MACRO {new_name}',
            content
        )
        content = re.sub(
            r'\bFOREIGN\s+' + re.escape(original_name) + r'\b',
            f'FOREIGN {new_name}',
            content
        )
        content = re.sub(
            r'\bEND\s+' + re.escape(original_name) + r'\b',
            f'END {new_name}',
            content
        )
    return content


def main():
    if len(sys.argv) < 4:
        print("用法:")
        print("  python process_lefs.py <input_lef> <output_lef> <suffix>")
        print("  python process_lefs.py <input_lef> <output_lef> --replace <old_field> <new_field>")
        print("示例:")
        print("  python process_lefs.py input.lef output.lef _T0")
        print("  python process_lefs.py input.lef output.lef --replace _BOT _TOP")
        sys.exit(1)
    
    input_lef = sys.argv[1]
    output_lef = sys.argv[2]
    operation = sys.argv[3]
    
    if operation == "--replace":
        if len(sys.argv) != 6:
            print("错误: --replace 模式需提供 old_field 与 new_field。")
            print("示例: python process_lefs.py input.lef output.lef --replace _BOT _TOP")
            sys.exit(1)
        old_field = sys.argv[4]
        new_field = sys.argv[5]
        replace_field_in_macros(input_lef, output_lef, old_field, new_field)
    else:
        # 兼容旧用法，直接将第三个参数视为后缀
        suffix = operation
        if len(sys.argv) > 4:
            print("警告: 多余参数已忽略，当前模式使用后缀添加。")
        add_suffix_to_macros(input_lef, output_lef, suffix)


if __name__ == "__main__":
    main()