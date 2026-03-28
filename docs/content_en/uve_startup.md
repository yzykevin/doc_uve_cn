# 项目初始化

`uve_startup` 是项目脚手架工具，可自动生成包含所有必要目录、配置文件和入口点的新 UVE 项目结构。

## 创建内容

- 标准项目目录布局（`bin`、`config`、`design`、`verif`、`doc`、`work`）
- 默认配置文件
- `run` 和 `run_cocotb` 入口点符号链接
- `.gitignore` 及相关项目文件

## 主要选项

### project_name

要创建的项目名称（必填）。

### -o / --output-dir

指定输出目录。默认：当前目录。

### --submodule-add

项目创建后，添加 `.gitmodules` 中定义的子模块。

### -r / --remote

为新创建的项目设置 git 远程 origin URL。

## 示例

```terminal
python3 uve_startup project_name -o /path/to/projects
```
