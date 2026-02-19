# 文件管理指南

## 在 design 文件夹中创建

请勿修改以下文件：

- design/fl/dut.f
- design/fl/dut_auto_fl/xxx_filelist.f

这些文件是自动生成的。

请使用有意义的文件夹来组织设计文件。

## 在 doc 文件夹中创建

请勿修改以下文件：

- doc/test_status.xlsx

这些文件是自动生成的。

## 在 test 文件夹中创建

基础测试可被不同模块的测试扩展，可以放在 test 文件夹中。

### 创建测试

- 同一模块的各种测试应放在以模块命名的文件夹中
- 测试名称应以模块名开头
- 类型应紧跟在测试名称中模块名之后
- 测试名称应以 _test.sv 结尾

例如：
xxx/xxx_aaa_sv_test.sv
xxx/xxx_aaa_sv_test.sv
xxx/xxx_bbb_ccc_sv_test.sv

### 创建 testlist

> 注意：无论 testlist 文件中有多少测试，都不要忘记添加 SUITE 行

testlist 的命名格式应为：testlist_xxx

例如，testlist_xxx

应包含注释：

- Description:（作为标题）
- 每个部分用 ',' 分隔
- 每个部分格式：Some Topic-详细信息
- Random-xxx、Owner-xxx 应放在注释的末尾

可以使用选项 `-gen_testlist` 生成示例 testlist_xxx

### 在 verif 文件夹中创建

请勿修改以下文件：

- verif/tb/test_include/xxx_test_include.sv
- tb.f

这些文件是自动生成的。

### 创建 pkg/uvc

单个模块的所有组件应放在 verif/pkg 文件夹中以模块名命名的文件夹内。

### 创建序列

序列和 sequence_library 应放在相关模块文件夹中的新创建的 seqs 文件夹内。

### 创建通用内容

testbench 的通用内容应放在 tb 文件夹中：

- tb/top
- tb/top_sub
- tb/tb_include
- tb/test_include
- tb/wrappers

请保持顺序，不要造成编译错误而中断他人的工作。

### 在 vip 文件夹中创建

请勿复制文件到此文件夹。如果 VIP 来自 Synopsys，此处的所有文件都使用 Synopsys VIP 工具生成。

## 在 tools 文件夹中创建

IP 指定的工具应放在以模块名命名的文件夹中。

### result_check

这用于错误/警告检查，并涉及使用 pytest 框架进行结果复核和审查。

这也会影响网站和 CI 中的结果报告。

可以根据不同的项目阶段修改检查规则为严格或宽松：

- 早期阶段 - 宽松
- 后期阶段 - 严格

使用此策略来消除被忽略的错误或检查器的泄漏，以确保 tape-out 前验证的成功。

有 4 个文件来管理检查方法：

- result_error_check
- result_error_ignore
- result_warning_check
- result_warning_ignore

"//" 将被视为注释并被流程忽略。

规则如下：

- 首先忽略 ignore 列表中的项目
- 如果 check 中的文本匹配，但 ignore 中有更具体的文本，则更具体的文本将被忽略
- warning 检查会导致用例失败
- 每个日志将被视为一个单独的测试，应用到整个规则

请注意：

- 想要修改此内容的用户应非常谨慎，最好是添加而不是减少。特别是在通用块中。
- 用户可以以详细的描述开始 ignore/check 并为其添加/修改自己的项目。
- 请注意，所有修改都将影响整个项目和所有人。来自其他工程师的测试可能会获得虚假通过。
- 规则文件应多次审查，以覆盖不应被遗漏的内容。
