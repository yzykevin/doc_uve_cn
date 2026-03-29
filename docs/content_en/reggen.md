# 寄存器生成器

寄存器生成器（reggen）集成于 `uve_tools`，可从寄存器描述文件自动生成硬件和验证团队所需的全部寄存器相关产物。

## 支持的输入格式

- YAML / JSON / TOML
- XLSX（Excel）
- SystemRDL
- IP-XACT

## 支持的输出类型

- **UVM RAL 模型** — SystemVerilog UVM 寄存器抽象层，用于测试平台集成
- **SystemVerilog RTL** — 可综合的寄存器模块 RTL，支持多种总线接口配置
- **C Header** — 便携式 C 头文件，用于嵌入式软件/固件访问寄存器
- **Markdown 文档** — 自动生成的寄存器参考文档

## 支持的总线协议

支持 APB、AXI4-Lite、Avalon 和 Wishbone 总线协议。可配置总线宽度和地址宽度。

## 格式转换

寄存器描述文件可在 YAML、JSON、TOML 和 XLSX 格式之间相互转换，无需重新生成输出。配置文件同样支持 YAML、JSON 和 TOML 之间的格式转换。

## 模板

提供 YAML、JSON 和 TOML 格式的入门模板，便于快速启动新的寄存器描述文件。

## 位字段访问类型

支持完整的位字段访问类型集合，涵盖标准读写语义、硬件驱动类型、触发类型、置位/清除/翻转变体以及计数器类型：

`rw` `ro` `wo` `rwtrg` `rotrg` `rof` `rohw` `wrc` `wrs` `rowo` `rowotrg` `wc` `woc` `ws` `wos` `w0c` `w1c` `w0s` `w1s` `w0t` `w1t` `rc` `rs` `w0crs` `w1crs` `wcrs` `w0src` `w1src` `wsrc` `rwc` `rws` `rwe` `rwl` `rwhw` `w0trg` `w1trg` `row0trg` `row1trg` `wotrg` `wo1` `w1` `counter` `custom` `reserved`

## 可扩展性

该生成器支持插件系统，可加载自定义输出生成器。