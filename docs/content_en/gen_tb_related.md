# 自动化

## -gen_test_status

请根据文件夹配置要搜索的测试，信息位于：`config/info/tests.info`

自动生成 xlsx 文件以显示当前仓库中存在的测试。测试列在 xlsx 的不同选项卡中，使用测试文件夹管理。

信息将显示：

- 测试组（用于要验证的不同模块）
- 测试 SUITE（功能特性）
- 测试名称
- 测试描述
- 随机配置
- 验证级别
- 平台
- 状态
- 宏定义
- 测试插针参数
- 值插针参数
- 所有者
- 测试用例数量
- 测试组总数
- 测试总数

## -gen_tb

使用项目名称 `xxx` 在各种文件夹中生成所有所需文件。生成的文件包括：

- `xxx_hvl_top.sv`
- `xxx_hdl_top.sv`
- `tb_xxx_include.sv`
- `testlist_xxx`

- **默认**：空字符串
- **用法**：确保 JSON 文件的命名适当。

## -gen_tb_top

在 `verif/tb/top` 文件夹中生成 `xxx_hvl_top.sv` 和 `xxx_hdl_top.sv` 文件。

- **默认**：空字符串

## -gen_tb_include

在 `verif/tb/tb_include` 文件夹中生成 `tb_xxx_include.sv` 文件。

- **默认**：空字符串

## -gen_testlist

在 `verif/test/xxx/testlist_xxx` 文件夹中生成 `testlist_xxx` 文件。包括用于创建兼容仿真命令的模板。

- **默认**：空字符串

## -gen_base_test

在 `verif/test/xxx` 文件夹中生成 `xxx_base_sv_test.sv` 文件。

- **默认**：空字符串
