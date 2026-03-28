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

## 主要选项

### -testmodule

指定要运行的 Python 测试模块。

### -top

指定 DUT 顶层模块名称。

### -sim

选择使用的仿真器。

### -seed

指定随机种子。默认：随机。

### -repeat

指定测试用例的重复次数。

### -wave

启用波形转储。

### -cov

启用覆盖率收集。

### -parameters

以 `NAME=VALUE` 格式向 DUT 传递参数。

## 示例

```terminal
python3 run_cocotb -testmodule=test_uart -top=uart_top -sim=vcs
```
