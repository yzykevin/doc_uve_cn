# UVE_VIP：通用可复用 VIP 库

UVE_VIP 是 UVE 的可复用验证 IP 层，由两个互补部分组成：

```{toctree}
:maxdepth: 1
:caption: UVE_VIP 模块

uve_pkg
uve_protocol_pkg
```

- **UVE_PKG**：通用验证基础设施、工具、寄存器支持、报告、性能、存储器、DMA、复位、时钟、中断和错误注入服务。
- **UVE_PROTOCOL_PKG**：面向 I2C、SPI、UART 等接口的可复用协议验证包。

两部分共同为项目专用 agent、environment、测试和协议验证组件提供可复用基础。
