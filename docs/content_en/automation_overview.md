# UVE_AUTOMATION：完整自动化能力

UVE_AUTOMATION 覆盖将项目描述转换为可重复验证资产，以及维护这些资产所需的自动化任务。

## 自动生成的验证产物

- register model 和寄存器相关组件；
- SystemVerilog RTL 及软件访问用寄存器产物；
- UVM agent、environment、register 和 sequence 模板；
- DUT 和 HVL 顶层脚手架；
- 测试平台 include 文件和 filelist；
- test 和 testlist 模板；
- base test 和可复用测试基础设施；
- 功能覆盖率模板；
- Jasper 方向项目模板和检查产物；
- 报告和统计分析产物；以及
- 配置模板和格式转换输出。

## 自动项目组合

UVE_AUTOMATION 支持自动生成设计 filelist、DUT filelist、测试平台 filelist、test include、可配置 wrapper，以及组合可复用验证子环境。项目可以针对不同 IP、子系统和 SoC 验证场景增加或替换子环境。

## 自检和结果自动化

自动化能力与项目自检、testlist 检查、预编译一致性检查、基于 pytest 的测试收集、仿真和回归结果分析、报告生成及工作空间清理连接起来。
