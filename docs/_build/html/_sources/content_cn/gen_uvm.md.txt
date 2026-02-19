# UVM 包生成

## -gen_uvm_tp_json

生成用于创建 UVM 包的 JSON 模板。必须使用 `-gen_uvm_tp_name` 选项指定包类型。

- **选项**：`agt_pkg`、`env_pkg`、`ral_pkg`、`seq_lib_pkg`
- **默认**：`none`
- **用法**：必须与 `-gen_uvm_tp_name` 结合使用。

## -gen_uvm_tp_yaml

生成用于创建 UVM 包的 YAML 模板。必须使用 `-gen_uvm_tp_name` 选项指定包类型。

- **选项**：`agt_pkg`、`env_pkg`、`ral_pkg`、`seq_lib_pkg`
- **默认**：`none`
- **用法**：必须与 `-gen_uvm_tp_name` 结合使用。

## -gen_uvm_tp_toml

生成用于创建 UVM 包的 TOML 模板。必须使用 `-gen_uvm_tp_name` 选项指定包类型。

- **选项**：`agt_pkg`、`env_pkg`、`ral_pkg`、`seq_lib_pkg`
- **默认**：`none`
- **用法**：必须与 `-gen_uvm_tp_name` 结合使用。

## -gen_uvm_tp_name

指定要生成的 UVM 包的名称。

- **默认**：空字符串
- **用法**：必须与 `-gen_uvm_tp_json`、`-gen_uvm_tp_yaml` 或 `-gen_uvm_tp_toml` 结合使用。

## -gen_uvm_pkg

指定模板格式（`json`、`yaml` 或 `toml`）来生成 UVM 包。

- **默认**：空字符串

## -conv

将模板文件从一种格式转换为另一种格式。支持 JSON、YAML 和 TOML 格式。

- **选项**：
  - `j2y`：JSON 转 YAML
  - `j2t`：JSON 转 TOML
  - `y2j`：YAML 转 JSON
  - `y2t`：YAML 转 TOML
  - `t2j`：TOML 转 JSON
  - `t2y`：TOML 转 YAML
- **默认**：`none`
- **用法**：必须与 `-conv_file` 结合使用。

## -conv_file

指定要转换的模板文件。文件类型可以是 JSON、YAML 或 TOML。

- **默认**：空字符串
- **用法**：必须与 `-conv` 结合使用。
