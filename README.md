# 郭浩田 · 供配电与电气运维项目作品集

**Haotian Guo | Electrical Engineering Portfolio**

河南理工大学电气工程及其自动化本科，悉尼大学电气工程硕士在读。本作品集展示供配电设计、短路与稳定性分析、配电网运行评估、实验数据处理，以及实习中的工程资料整理经历。

关注方向：**电气运维、数据中心基础设施供配电、设备运行与故障分析**。MATLAB、Simulink、OpenDSS、Julia 和 Python 用于支持工程计算、批量分析与结果核查。

## 代表项目

| 项目 | 解决的问题 | 可查看的成果 |
|---|---|---|
| [本科毕设：井下供配电一次系统设计](01-power-distribution-design.md) | 负荷如何分配，变压器、电缆和开关设备如何选择与校验 | 设计流程、负荷与短路分析方法、设备校核思路 |
| [ELEC5204：三相系统建模与故障分析](02-short-circuit-analysis.md) | 三相短路和单相接地时，电流、电压如何变化 | 7 节点模型、标幺值与序网络计算结果 |
| [ELEC5208：配电网运行与储能分析](04-distribution-network-and-storage.md) | 光伏和电池如何影响全年电压、反向潮流及运行约束 | 105,120 步年度仿真、场景对比、原始结果图与汇总数据 |

## 全部项目

| 类别 | 项目 | 方法 / 工具 | 项目性质 |
|---|---|---|---|
| 本科毕业设计 | [井下供配电一次系统设计](01-power-distribution-design.md) | 负荷计算、无功补偿、设备选型、短路校验、CAD | 毕业设计 |
| 硕士课程 | [三相电力系统与短路故障分析](02-short-circuit-analysis.md) | MATLAB / Simulink、Zbus、对称分量法 | 小组实验 |
| 硕士课程 | [多机系统动态稳定性与临界清除时间](03-dynamic-stability.md) | MATPOWER、ode45、二分搜索 | 小组项目 |
| 硕士课程 | [配电网、家庭储能与动态运行区间](04-distribution-network-and-storage.md) | OpenDSS、Julia、JuMP、HiGHS、Clarabel | 小组项目 |
| 硕士实验 | [光伏 MPPT 与风机运行特性测试](05-energy-laboratory.md) | DACI / LVDAC-EMS、数据清洗、功率与误差核查 | 小组实验 |
| 实习学习 | [传感器节点 PCB 设计与工程资料整理](06-internship-engineering.md) | KiCad、ERC / DRC、版本与验证资料 | 实习学习项目 |
| 硕士研究 | [P2P 能源交易研究](07-capstone-research.md) | 市场出清、用户偏好与配电网约束 | 研究进行中 |

## 工程分析方式

从设备参数和负荷数据出发，建立正常与故障工况模型，结合计算结果、仿真波形和实验数据分析供电系统的运行状态。重点关注设备容量、故障电流、电压质量和运行稳定性。

## 项目资料

- 本科毕设：[论文 PDF](undergraduate-thesis.pdf)、[一次系统图](undergraduate-primary-system.pdf)、[CAD 工程](undergraduate-design-source.zip)。
- 实习项目：[KiCad 原理图、PCB 与生产资料](internship-kicad-engineering.zip)。

- [项目文件索引](EVIDENCE.md)：模型、计算脚本、成果图与实验数据。
- [结果复核脚本](verify_results.py)：仅使用 Python 标准库，核对公开的实验数据与年度汇总指标。
- 工程代码节选：[5204 模型与计算脚本](5204_selected_source.zip)、[5211 脚本与已保存数值结果](5211_selected_source.zip)、[5208 控制与优化代码](5208_selected_source.zip)。
- [年度仿真汇总](5208_annual_summary.csv)、[光伏正常入射数据](5206_mppt_normal.csv)、[光伏倾斜数据](5206_mppt_tilted.csv)、[风机测量数据](5206_wind_measurements.csv)。

```shell
python verify_results.py
```

更新日期：2026 年 10 月 15 日。
