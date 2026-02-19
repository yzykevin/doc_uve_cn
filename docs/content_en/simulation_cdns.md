# Xcelium

> 指定 `-tool=cdns` 以使用这些选项。

## -c_run1

选择 Cadence 工具的运行方式：`step1`。执行从编译到仿真的完整流程。

## -c_run3

选择 Cadence 工具的运行方式：`step3`。执行从编译到仿真的完整流程。

## -c_com

仅使用 XRUN 1-step 方法进行编译。

## -c_dut

使用 XRUN 3-step 方法编译 DUT。

## -c_tb

使用 XRUN 3-step 方法编译 testbench。

**保护：** `-c_tb` 需要有效的 DUT 编译数据库。如果同一命令中未请求 DUT 编译，请指定 `-base_dut=<name>`。

## -c_sim

使用 XRUN 3-step 方法执行仿真。

**保护：** `-c_sim` 需要有效的 TB 编译数据库。如果同一命令中未请求 TB 编译，请指定 `-base_tb=<name>`。

## 波形兼容性（XRUN）

`-wave=shm` 是 Cadence 原生格式。

`-wave=fsdb` 和 `-wave=vpd` 可能在正确的 PLI 设置下才能工作，但不是默认推荐。
