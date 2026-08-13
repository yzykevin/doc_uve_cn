# 7.1 架构模型目录

`uve_arch` 是基于 SystemC/Accellera 的架构建模和探索平台。其模型用于系统设计研究、集成验证、性能分析、瓶颈识别、软件可见行为研究，以及向 Linux 启动和 RTL 交付演进的流程。

| 模型系列 | 简介 |
|---|---|
| CPU 与处理器模型 | 处理器和 CPU wrapper 架构研究。 |
| 互连与 NoC 模型 | crossbar、仲裁器、NoC 和拓扑研究。 |
| 存储系统模型 | DDR/HBM 和存储器控制器性能研究。 |
| Chiplet 与 die-to-die 模型 | chiplet 连接和系统集成研究。 |
| 高速互连模型 | PCIe、Ethernet 和 CXL 架构研究。 |
| 外设系统模型 | UART、SPI、I2C、GPIO、timer、watchdog、RTC 和中断集成。 |
| 时钟、电源与安全模型 | 时钟/电源时序、root-of-trust、secure-boot 和访问控制研究。 |
| AI/NPU 架构模型 | AI 加速器和 NPU 系统探索。 |

该平台用于研究架构选择、集成行为、性能瓶颈和系统级权衡，为详细 RTL 实现提供依据。
