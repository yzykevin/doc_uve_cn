# JasperGold 形式化验证

> 在项目根目录下通过 `jg_run`（或 `python3 jg_run`）执行。

UVE 提供独立的 JasperGold 形式化验证入口，与仿真流程分离。

## 环境设置

### -env_setup

打印 JasperGold 环境变量设置命令。Source 输出内容以配置 shell 环境。

### -env_unset

打印取消 JasperGold 环境变量的命令。

## 项目配置

### -json

指定项目 JSON 配置文件。默认：`jg.json`。

### -name

指定验证任务名称（例如 `my_module_fpv`）。

### -top

指定 DUT 顶层模块名称。

### -lib

指定设计库名称。默认：`work`。

### -gen_jg_proj

以给定名称生成模板 JSON 配置文件。

## 设计文件

### -fl

指定设计 filelist（`.f` 文件）。

### -sva_fl

指定 SVA / property filelist。

### -inc

指定 include 目录（空格分隔，可重复使用）。

## 形式化应用

多个应用可在单次运行中组合使用。

| 选项 | 说明 |
|------|------|
| `-fpv` | 形式化属性验证（默认） |
| `-conn` | 连接性检查 |
| `-csr` | CSR 检查 |
| `-xprop` | X 传播检查 |
| `-lpv` | 低功耗验证 |
| `-cdc` | 跨时钟域验证 |
| `-sec` | 时序等价检查 |
| `-superlint` | Superlint（形式化 lint + 溢出检查） |
| `-cov_app` | 覆盖率应用（形式化覆盖率测量） |
| `-spv` | 安全路径验证 |

## 环境约束

### -clock

指定主时钟信号。

### -reset

指定复位信号。使用 `~` 前缀表示低有效（例如 `-reset=~rst_n`）。

### -assume

指定假设表达式。可重复使用以添加多个假设。

## 验证选项

### -gui

以交互式 GUI 模式打开 JasperGold。

### -dry_run

打印生成的命令但不执行。

### -regen_tcl

强制重新生成 TCL 脚本，即使 `verif/` 下已存在。

### -check

每个形式化应用完成后自动运行结果检查器。

### -check_only

跳过 JasperGold 运行，仅检查上次运行的结果。需要指定 `-name` 和相关应用标志。

### -max_jobs

最大并行验证任务数。默认：`50`。

### -bbox_mul

将宽度超过 N 位的乘法器黑盒化。默认：`0`（禁用）。

### -cov

在形式化运行期间启用覆盖率收集。

## 运行目录

### -run_dir

指定运行目录的创建位置。默认：若存在 `work/` 则为 `work/formal`，否则为 `jasper_run`。

## 形式化回归

### -fl_formal

运行形式化 testlist 文件中列出的所有形式化测试。

示例：`-fl_formal=verif/formal/adder/formal_adder`

### -suite

将回归限制为 testlist 中指定 SUITE 的测试。

### -gen_formal_testlist

为给定模块名称生成形式化 testlist 模板。
