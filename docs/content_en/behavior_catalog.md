# 6.1 行为模型目录

| Model | 简介 |
|---|---|
| `generic_boot_flash_model` | 面向启动 flash 的镜像访问和复位行为。 |
| `generic_clock_manager_model` | 时钟源、门控、分频和切换行为。 |
| `generic_gpio_pad_model` | GPIO pad 驱动、高阻态和竞争行为。 |
| `generic_i2c_target_model` | I2C target、应答、数据载荷和协议边界行为。 |
| `generic_lpddr_subsystem_model` | 用于存储系统集成研究的 LPDDR 子系统行为。 |
| `generic_pcie_endpoint_model` | PCIe endpoint 完成、**中断和控制访问场景。 |
| `generic_pinmux_pad_model` | 引脚复用、输出使能、上下拉、输入和竞争行为。 |
| `generic_pll_model` | PLL 锁定、重锁定、禁用和门控输出行为。 |
| `generic_power_domain_model` | 电源域睡眠、唤醒、保持和非保持行为。 |
| `generic_sensor_model` | 传感器阈值、告警和故障注入行为。 |
| `generic_spi_target_model` | SPI target 的时钟相位、位序、响应和完成行为。 |
| `generic_uart_peer_model` | UART peer 的奇偶校验、break 和线路恢复行为。 |
| `generic_ucie_phy_model` | UCIe PHY 方向的延迟、流控、应答和错误行为。 |

每个模型都配有独立自检，用于覆盖正常行为及边界行为。
