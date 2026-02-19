# 信息分析

## -info_defines

收集 design/verif 文件夹中的所有宏定义，分析指定层级内的文件夹/文件。
将创建 `info_defines` 来存储审查信息。该文件会被 git 忽略，需要手动删除。
请注意：vip 文件夹将被跳过。

审查信息包括：

- 在 design 中找到
- 在 verif 中找到

## -info_git_submodule

显示所有 git 仓库/子模块信息。

## -info_uvm

根据 `config/info/uvc.info` 中指定的列表，显示 xVCs 的文件/结构摘要。

## -info_all_testlist

test 文件夹中所有 testlist 的信息。
