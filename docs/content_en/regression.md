# 回归测试

要运行 testlist 中所有测试的回归测试，回归文件夹将使用回归和运行日期/时间的组合在 `work` 文件夹中创建。

测试与种子组合的文件夹将创建在 `regression_` 文件夹中。

testlist 中每个测试命令的以下选项将被忽略：

- `-wave`
- `-seed`

这些选项可以在回归命令中传递。

请注意，如果单个测试命令中有 `-repeat` 选项，`-seed` 将被忽略，并为 `-repeat` 次使用随机种子。

示例：

VCS 3-step 命令

```terminal
python3 run -s_regress3=test/xxx/testlist_xxx -reg_num=8 -wave=fsdb -seed=100
```

VCS 2-step 命令

```terminal
python3 run -s_regress2=test/xxx/testlist_xxx -reg_num=8 -wave=fsdb -seed=100
```

**注意：** 如果所有回归都打开波形，结果文件夹将很大，可能会消耗过多磁盘空间。

## 终端显示

所有信息将以*颜色*显示。

信息包括：

- 主程序进程 PID
- 并行运行的进程数
- 运行用例的总数
- 当前服务器的 CPU 总数
- `run` 文件夹中的回归位置
- 运行测试详情：
  - 名称
  - PID
  - 开始日期 /时间
-完成的测试详情：
  - 名称
  - 完成日期/时间
  - 持续时间
- 成功完成的测试（可能卡住的测试不会显示）
- 测试大致结果：`PASSED`/`FAILED`
- 测试结果报告文件位置

## -reg_num

指定并行回归的数量。默认为 5。

**注意：** 不要设置数量过高以避免服务器过载。

并行运行在单个服务器上使用多个进程。数量越高，回归时间越短，但系统资源消耗越高。请提供合理的数字，确保不影响其他工程师的工作。

这可以与 `-lsf`/`-slurm` 结合使用。

## -suite

使用 testlist 中提供的 suite 运行回归。

## -rm_pass

在回归中，此选项删除已通过的测试文件夹以节省磁盘空间，但会保留已通过测试的日志以替换删除的文件夹。

## -rerun

回归后，如果指定此选项，失败的测试将被收集并在 `reg_result_fail` 中维护。所有失败的测试将在回归文件夹中的同一文件夹内重新运行，并打开波形（目前为 `fsdb`）。

这使调试更容易、更快。

## rerun_for 选项

无论是否传递 `-rerun`，此选项都将在指定回归文件夹中重新运行打开波形的失败测试。

示例：

```terminal
-s_rerun2_for=regression_2028_03_21_15_37_11
```

请在相关工具描述中查看详细选项。

## -report（待完成）

此选项仅在回归期间有效，支持 VCS-2step 和 VCS-3step 流程。

它使用结果检查工具详细分析所有日志，并在回归文件夹中生成 HTML 报告（`report.html`）。该报告可以在 Firefox 等网页浏览器中打开和查看。

报告简单但信息丰富，显示以下详细信息：

- 用例数量摘要，包括通过和失败数量
- 结果状态
- 日志链接（在 Linux 服务器上访问时可点击）
- 用例名称
- 种子
- 仿真时间
- 完成时间
- 完整日志路径
- 遇到的第一个错误

启用 `-slurm/-lsf` 时，结果检查工具将提交给作业调度器进行处理。

如果禁用此选项，回归过程中仍会生成基本报告，包括：

- 基于测试 PASS/FAIL 状态的基本分析
- 在回归文件夹中创建的 `reg_result` 和 `reg_result_fail` 文件

如果在回归期间禁用了该选项但之后需要，用户可以导航到回归文件夹并执行报告脚本以生成 `report.html`，而无需重新运行回归。

### -step2

在运行 VCS-2step 的回归文件夹中进行报告收集。默认为 VCS-3step

### -clean

一般来说，用户不需要担心 Python pytest 使用或生成的 py 文件。

如果用户想手动清理所有 `test_xxx.py` 文件，请使用此选项。

请参考 Guideline_for_creating_and_managing_files.pdf 了解：

- 错误检查/忽略
- 警告检查/忽略

这对于 QA 验证非常重要。

## 真实随机回归助手

辅助脚本位于：

`uve_tools/md_tools/real_regress_runner.py`

在准备的容器环境中的典型用法：

```terminal
python3 uve_tools/md_tools/real_regress_runner.py --project-root /home/devuser/uve/uve --count 30 --mode real --tools all --setup-script auto --shell-mode auto
```

推荐的行为：

- 默认是共享运行文件夹，以便可以有意重用编译和 testbench 的工件。
- 仅在需要严格的每个用例隔离时才添加 `--isolated-run-folder`。
- 如果想避免在随机抽样中选择部分流程命令，请使用 `--skip-partial-flow`。

输出：

- `summary.json`
- `summary.md`
- 每个用例的日志和命令记录
