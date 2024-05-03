import os
import argparse
import re

def merge_markdown_files(input_folder, output_file):
    # 打开输出文件以写入模式
    with open(output_file, 'a', encoding='utf-8') as output:
        # 遍历输入文件夹内的所有文件
        for file in os.listdir(input_folder):
            # 仅处理Markdown文件
            if file.endswith('.md'):
                # 检查文件是否与输出文件相同
                if file == os.path.basename(output_file):
                    continue
                # 构造文件路径
                file_path = os.path.join(input_folder, file)
                # 打开并读取Markdown文件内容
                with open(file_path, 'r', encoding='utf-8') as input_file:
                    markdown_content = input_file.read()
                    # 使用正则表达式找到代码块内容并替换为占位符
                    code_blocks = re.findall(r'```.*?```', markdown_content, re.DOTALL)
                    code_placeholder = '%%CODE_BLOCK%%'
                    markdown_content = re.sub(r'```.*?```', code_placeholder, markdown_content, flags=re.DOTALL)
                    # 将标题级别向下移动一个级别
                    markdown_content = markdown_content.replace('# ', '## ')
                    # 将占位符替换回代码块内容
                    for code_block in code_blocks:
                        markdown_content = markdown_content.replace(code_placeholder, code_block, 1)
                    # 写入输出文件
                    output.write(markdown_content)
                    output.write('\n\n')  # 添加分隔符

def main():
    default_input_folder = os.path.dirname(__file__)
    parser = argparse.ArgumentParser(description='Merge Markdown files in a folder')
    parser.add_argument('input_folder', nargs='?', default=default_input_folder, type=str, help='Input folder containing Markdown files (default: current directory)')
    parser.add_argument('output_file', type=str, help='Output file name for merged Markdown')
    args = parser.parse_args()

    merge_markdown_files(args.input_folder, args.output_file)

if __name__ == "__main__":
    main()
