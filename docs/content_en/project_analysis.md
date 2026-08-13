# UVE_INFO：项目信息和分析

UVE_INFO 提供面向项目的信息发现、分析和报告服务。

## 信息发现

- `-info_all`：汇总项目项目信息视图；
- `-info_defines`：发现和汇总编译期 define；
- `-info_git_submodule`：检查仓库和 submodule 信息；
- `-info_uvm`：检查 UVM 包结构和可复用组件；
- `-info_all_testlist`：收集项目中的 testlist；以及
- 测试状态和项目元数据分析。

## 分析与报告

UVE_INFO 支持 package、class、sequence、interface、define、parameter、register、filelist、test、配置和一致性分析。结果可以通过本地报告视图、VS Code 扩展和项目自动化检查使用。

## 结果和自检集成

信息分析与工具自检、基于 pytest 的检查、回归结果收集、报告生成和一致性审查集成，使项目状态可以在同一验证环境中检查。
