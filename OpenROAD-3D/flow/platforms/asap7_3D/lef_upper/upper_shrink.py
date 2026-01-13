#!/usr/bin/env python3
import sys
from pathlib import Path

def shrink_macros(input_lef: Path, output_lef: Path):
    inside_macro = False
    macro_name = None

    with input_lef.open("r") as fin, output_lef.open("w") as fout:
        for line in fin:
            stripped = line.lstrip()
            # 进入一个 MACRO 块
            if stripped.startswith("MACRO"):
                inside_macro = True
                # 记录宏名（可选，不需要实际使用）
                parts = stripped.split()
                if len(parts) >= 2:
                    macro_name = parts[1]
                fout.write(line)
                continue

            # 离开 MACRO 块
            if inside_macro and stripped.startswith("END"):
                inside_macro = False
                macro_name = None
                fout.write(line)
                continue

            # 如果在 MACRO 块中且遇到 SIZE 行，则替换
            if inside_macro and stripped.startswith("SIZE"):
                # 保留原有缩进（如有）
                indent = line[:len(line) - len(stripped)]
                fout.write(f"{indent}SIZE 0.054 BY 0.270 ;\n")
            else:
                fout.write(line)

if __name__ == "__main__":
    # 默认输入输出路径，可根据需要修改或通过命令行参数传入
    input_path = Path("asap7_upper_shrink.lef")
    output_path = Path("asap7_upper_shrink_shrinked.lef")

    # 如果通过命令行传入文件名
    if len(sys.argv) >= 2:
        input_path = Path(sys.argv[1])
    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])

    if not input_path.exists():
        sys.stderr.write(f"Input file {input_path} does not exist.\n")
        sys.exit(1)

    shrink_macros(input_path, output_path)
    print(f"Done. New LEF written to {output_path}")