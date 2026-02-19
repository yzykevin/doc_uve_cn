# 准备工作

## -h/--help

显示所有选项的帮助信息及描述。

## -env_setup

根据您的 shell 类型设置所需的环境变量。

支持的 shell 类型：

- bash/zsh
- tcsh/csh

## -env_unset

清除所有与 `uve_tools` 相关的环境变量。

## -json

json/json_extra 文件位于：`config/json/project/`

使用 JSON 文件指定项目的配置。该文件管理 EDA 工具的所有选项以及仿真或仿真的流程。默认文件为 `uve.json`。

要使用特定的 JSON 文件进行仿真，请将其作为参数传递：

示例：`-json=xxx.json`

## -json_extra

使用额外的 JSON 文件指定项目的配置。该文件包含编译、 elaboration 和执行的配置节。默认文件为 `uve_extra.json`。

要使用特定的额外 JSON 文件进行仿真，请将其作为参数传递：

示例：`-json_extra=xxx_extra.json`
