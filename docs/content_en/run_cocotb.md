# Cocotb 仿真

`run_cocotb` 是基于 [cocotb](https://www.cocotb.org/) 框架运行 Python 测试平台的入口。

支持多种仿真器以及 Verilog 和 VHDL 设计。

## 支持的仿真器

- Synopsys VCS
- Cadence Xcelium
- Mentor Questa / ModelSim
- Aldec Riviera-PRO / Active-HDL
- Icarus Verilog
- Verilator
- GHDL / NVC

## 功能

**测试控制**
- 指定 Python 测试模块、单个测试函数和顶层模块
- 控制随机种子和重复次数，用于随机化测试策略

**源文件支持**
- 支持 Verilog 和 VHDL 源文件列表或单个文件路径
- 支持 Verilog 的 include 目录
- 支持 AMS 仿真的 VAMS（模拟）源文件

**DUT 配置**
- 直接传递模块参数（NAME=VALUE 格式）
- 配置 HDL 时间单位和时间精度

**仿真运行时**
- 预编译和后运行阶段每个仿真器的参数传递
- 仿真器 plusargs 支持
- 可配置的构建目录和结果输出文件

**波形转储**
- 启用波形捕获，支持 GHW、FST 和 VCD 格式

**覆盖率与性能分析**
- Python 代码覆盖率收集
- 调用图性能分析
- cocotb 内部覆盖率分析

**模拟/混合信号（AMS）**
- Xcelium 和 VCS 的 AMS 仿真支持
- 混合信号设计的 discipline 配置

**GPI 接口（VHDL）**
- VHDL 设计可选的 GPI 接口：VPI、VHPI 或 FLI
- 支持额外的 GPI 库和自定义 PyGPI 入口点

**X/Z 值解析**
- X/Z 逻辑值转换为整数时的可配置行为：错误、置零、置一或随机

**调试支持**
- 在仿真开始前暂停，以便附加外部调试器
- 测试异常时进入 Python 调试器（pdb）
- HTTP 内存调试端点

## 示例

```terminal
python3 run_cocotb -testmodule=test_uart -top=uart_top -sim=vcs
```
