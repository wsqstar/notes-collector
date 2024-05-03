# How to use? 如何使用？


# Usage Guide

This script is designed to merge Markdown files into one, lowering header levels by one.

## Installation

1. Clone or download this GitHub repository to your local machine.
   
2. Ensure Python 3 is installed on your computer.

## Usage

Run the following command in your terminal:

```bash
python merge_markdown.py input_folder output_file.md
```

Where:
- `input_folder` is the path to the folder containing Markdown files. Default is the current directory of the Python file.
- `output_file.md` is the name of the merged Markdown file to be generated.

If no input folder is specified, the script will default to using the current directory of the Python file.

## Example

```bash
python merge_markdown.py my_folder merged_file.md
```

This will merge all Markdown files in the `my_folder` directory into `merged_file.md`.

## Notes

- The script will merge all Markdown files in the input folder into the specified output file.
- If the output file has the same name as a file in the input folder, that file will not be merged into the output file.
- During the merge process, `#` within code blocks will not be converted to `##`.

## Help

For assistance or any questions, please contact us.

---
   
# 使用说明

这个脚本用于合并 Markdown 文件到一个文件中，并将标题级别降低一个级别。

## 安装

1. 克隆或下载这个 GitHub 仓库到本地电脑。

2. 确保你的电脑上安装了 Python 3。

## 使用方法

在终端中执行以下命令：

```bash
python merge_markdown.py input_folder output_file.md
```

其中：
- `input_folder` 是包含 Markdown 文件的文件夹的路径。默认为当前 Python 文件所在的文件夹。
- `output_file.md` 是生成的合并后的 Markdown 文件的名称。

如果不指定输入文件夹，脚本会默认使用当前 Python 文件所在的文件夹。

## 示例

```bash
python merge_markdown.py my_folder merged_file.md
```

这会将 `my_folder` 文件夹中的所有 Markdown 文件合并到 `merged_file.md` 中。

## 注意事项

- 脚本会将输入文件夹中的所有 Markdown 文件合并到指定的输出文件中。
- 如果输出文件与输入文件夹中的某个文件同名，该文件不会被合并到输出文件中。
- 在合并过程中，代码块内的 `#` 不会被转换为 `##`。

## 帮助

如果需要帮助或有任何问题，请联系我们。

