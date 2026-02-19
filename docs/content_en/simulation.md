# 仿真

## -tool

选择要使用的工具：Synopsys VCS (`snps`) 或 Cadence XRUN (`cdns`)。默认为 `snps`。

## -list

在 `design` 文件夹中自动生成 `filelist.f`，用于 testbench。

`filelist.f` 将包含克隆仓库中所有 `.v` 文件的绝对路径。请确保 `rtl` 文件夹是干净的，不包含未使用的文件。

使用方法如下：

1. 创建 `xxx` 文件夹并将所有设计文件放入其中
2. 将 `xxx` 名称添加到 `design/fl/dut_auto_fl/dut_auto_filelist`
3. 运行命令：`python3 run -list`
4. `xxx_filelist.f` 将在 `design/fl/dut_auto_fl/` 中生成

可以在 `design/fl/dut_auto_fl/dut_auto_filelist` 中找到和管理该列表。

dut_auto_filelist 中的所有文件夹名称都将被生成。

## -auto_dut

在 `design/fl/` 文件夹中自动为每个 RTL 模块生成 `dut.f`，用于 testbench。

使用方法如下：

1. 基于 `-list` 生成的结果，从列表 `design/fl/dut_auto_fl/dut_auto_filelist` 中提供 `xxx`
2. 运行命令：`python3 run -auto_dut=xxx`
3. `dut.f` 将在 `design/fl/` 中生成

## -auto_tb

在 `verif/fl/` 文件夹中自动生成 `tb.f`，用于 testbench。

使用方法如下：

1. 在 `verif/fl/tb_auto_fl/` 中准备 `xxx` filelist
2. 运行命令：`python3 run -auto_tb=xxx`
3. `tb.f` 将在 `verif/fl/` 中生成

此外，自动在 `verif/tb/test_include/` 文件夹中生成 `xxx_test_include.sv`，其中包含 `verif/test/xxx/` 中找到的所有测试，用于 testbench。

`tb.f` 将包含所有现有的 `verif/pkg/xxx` 文件夹、`vip_snps` 文件夹和 `verif/test/xxx` 文件夹路径。

## -manual_dut

指定要仿真的手动编写的 DUT filelist。

filelists 应在相对根目录 `design/fl/dut_manual_fl/` 中准备和管理。

例如，使用 `-manual_dut=xxx_flist.f`：

文件 `design/fl/dut_manual_fl/xxx_flist.f` 将被用作 `dut.f`。

## -manual_tb

指定要仿真的手动编写的 TB filelist。

filelists 应在相对根目录 `verif/fl/tb_manual_fl/` 中准备和管理。

例如，使用 `-manual_tb=xxx_flist.f`：

文件 `verif/fl/tb_manual_fl/xxx_flist.f` 将被用作 `tb.f`。

## -run_folder

指定运行文件夹。默认为 `work`。

## -name

指定测试名称。

例如，使用 `-name=xxx_test`。这将使用 xxx_test.sv，如 +UVM_TESTNAME=xxx_test

### -base_dut

仅 3-step！跳过 dut 编译，使用 base_dut 指定的 dut 编译数据库。

示例：`-base_dut=xxx`
这将创建并编译 `PROJECT_NAME_xxx`。默认情况下，`PROJECT_NAME` 用作编译文件夹。

### -base_tb

仅 3-step！跳过 tb 编译，使用 base_tb 指定的 tb 编译数据库

示例：`-base_tb=xxx_xxx_test`

## -dry_run

运行完整流程但不执行实际仿真。

首次检查命令合法性和生成的命令行时，建议使用 `-dry_run`。

## -dump_scope

指定波形转储范围。默认为 `verif/test/common/dump_scope.txt`。

## -prerun

在仿真之前运行命令/脚本。使用格式：`-prerun=""`。

## -postrun

在仿真之后运行命令/脚本。使用格式：`-postrun=""`。

## -define

向仿真传递宏定义。使用格式：`-define=""`。

示例：
`-define="aaa"`
`-define="aaa bbb ccc"`

## -tpa

向仿真传递测试插针参数。使用格式：`-tpa=""`。

示例：
`-tpa="+aaa"`
`-tpa="+aaa, +bbb"`

## -vpa

向仿真传递值插针参数。使用格式：`-vpa=""`。

示例：
`-vpa="+aaa=xxx"`
`-vpa="+aaa=xxx, +bbb=yyy"`

## -seed

指定仿真的种子。默认为随机。

## -repeat

指定测试用例重复次数。默认为 1。

## -wave

指定波形转储格式。选项：`fsdb`、`vpd`、`shm`。

兼容性建议：

- `snps`：使用 `fsdb` 或 `vpd`；`shm` 无效。
- `cdns`：使用 `shm`；`fsdb`/`vpd` 需要额外的 PLI 环境。

## -cov

启用覆盖率收集。选项：`all` 或特定类型（例如 `line,tgl,fsm,branch,cond,assert`）。

## 运行时保护

在非 `dry_run` 执行期间，UVE 在启动工具命令之前执行预检查：

- Step3 部分流程在跳过编译阶段时需要匹配的基编译数据库（`-base_dut` / `-base_tb`）。
- 工具-波形不匹配会被提前报告，以避免浪费运行时间。
- 检查 PATH 中是否存在所需的可执行文件（例如：`vcs`/`vlogan`/`xrun`）。

如果命令在准备的容器环境之外执行，这些检查可能会如预期般失败。
