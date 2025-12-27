import re
import os

def mirror_layer_numbers(file_path, output_path):
    """
    镜像 LEF 文件中 MACRO 内 PIN 和 OBS 的层编号
    规则：
    - M1 <-> M14, M2 <-> M13, ..., M7 <-> M8
    - V1 <-> V14, V2 <-> V13, ..., V7 <-> V8
    
    参数:
        file_path: 输入 LEF 文件路径
        output_path: 输出 LEF 文件路径
    """
    
    def metal_replacement(match):
        """金属层镜像映射函数：M1<->M14, M2<->M13, ..."""
        layer_num = int(match.group(1))
        new_num = 15 - layer_num  # M1->M14, M2->M13, ..., M14->M1
        return f'M{new_num}'
    
    def via_replacement(match):
        """通孔层镜像映射函数：V1<->V14, V2<->V13, ..."""
        layer_num = int(match.group(1))
        new_num = 15 - layer_num  # V1->V14, V2->V13, ..., V14->V1
        return f'V{new_num}'
    
    # 编译正则表达式
    # 匹配 LAYER 后面的金属层名称（M 后跟数字）
    metal_pattern = re.compile(r'\bM(\d+)\b')
    # 匹配 LAYER 后面的通孔层名称（V 后跟数字）
    via_pattern = re.compile(r'\bV(\d+)\b')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 先替换金属层
        updated_content = metal_pattern.sub(metal_replacement, content)
        # 再替换通孔层
        updated_content = via_pattern.sub(via_replacement, updated_content)
        
        # 写入新文件
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        
        print(f"✓ 成功处理文件")
        print(f"  输入文件: {file_path}")
        print(f"  输出文件: {output_path}")
        print(f"  镜像规则: M1<->M14, M2<->M13, ..., M7<->M8")
        print(f"           V1<->V14, V2<->V13, ..., V7<->V8")
        
    except FileNotFoundError:
        print(f"错误: 找不到文件 {file_path}")
    except IOError as e:
        print(f"错误: 文件读写失败 - {e}")

if __name__ == "__main__":
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 输入文件路径
    input_file = os.path.join(script_dir, 'asap7sc7p5t_28_L.lef')
    
    # 输出文件路径（在当前目录下，添加 _mirrored 后缀）
    output_file = os.path.join(script_dir, 'asap7sc7p5t_28_L_mirrored.lef')
    
    # 执行镜像处理
    mirror_layer_numbers(input_file, output_file)

