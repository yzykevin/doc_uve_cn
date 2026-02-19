# 调试

## -debug

启用调试模式以打印额外的调试信息。

## -check_testlist

在仿真或回归之前检查 testlist，以便及早发现错误。

示例：`-check_testlist=./verif/test/ip/testlist_ip`

## -clean

使用交互式操作清理根目录。

## -git_update

更新仓库和子模块。

## -check_git_clean

检查仓库中的所有文件夹，分析指定层级内的文件夹/文件。
将创建 `check_git_clean_check` 文件夹来存储审查信息。该文件夹会被 git 忽略，需要手动删除。

审查信息包括：

- 新增的文件夹
- 不应包含在 xxx 中的内容
