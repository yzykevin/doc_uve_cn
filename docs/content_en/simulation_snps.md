# VCS

> 指定 `-tool=snps` 以使用这些选项。

## -s_run2

选择 Synopsys 工具的运行方式：`step2`。执行从编译到仿真的完整流程。

## -s_run3

选择 Synopsys 工具的运行方式：`step3`。执行从编译到仿真的完整流程。

> **注意：** 如果使用 `step3`，DUT/testbench 编译文件夹不会自动刷新。如果 DUT/testbench 已更新，必须清理编译文件夹，然后再次执行 `step3` 运行以使用更新的文件。
> 对于开发阶段的用例，建议使用 `step2` 运行（`-s_run=step2`）。

## -s_com

仅使用 VCS `step2` 方法进行编译。

## -s_dut

使用 VCS `step3` 方法编译 DUT。

## -s_tb

使用 VCS `step3` 方法编译 testbench。

**保护：** `-s_tb` 需要有效的 DUT 编译数据库。如果同一命令中未请求 DUT 编译，请指定 `-base_dut=<name>`。

## -s_sim

使用 VCS `step3` 方法执行仿真。

**保护：** `-s_sim` 需要有效的 TB 编译数据库。如果同一命令中未请求 TB 编译，请指定 `-base_tb=<name>`。

## -s_part_comp

指定 Synopsys 工具分区编译方法：`auto`、`manual` 或 `no`。默认为 `no`。

对于手动分区，可以减少编译时间。但是，必须结合 `json_extra` 来传递 `cfg.v`。示例见 `xxx_extra.json`。

## 波形兼容性（VCS）

`-wave=fsdb` 和 `-wave=vpd` 支持 VCS。

`-wave=shm` 是 Cadence 专用的，在 VCS 中被阻止。
