# 项目文件索引

[返回作品集](README.md)

| 项目 | 文件 | 内容 |
|---|---|---|
| 本科毕设 | [论文](undergraduate-thesis.pdf)、[系统图](undergraduate-primary-system.pdf)、[主接线图资料](undergraduate-design-source.zip) | 供配电一次系统设计说明书及工程图纸 |
| 施耐德实习 | [KiCad 工程包](internship-kicad-engineering.zip) | 原理图、PCB、Gerber、BOM、坐标、装配图与检查记录 |
| ELEC5204 | [模型与脚本](5204_selected_source.zip) | 基础网络、三相短路、A相接地 Simulink 模型与解析计算 |
| ELEC5211 | [仿真工程](5211_selected_source.zip) | 潮流、动态响应、故障清除时间、SMIB 脚本与数值结果 |
| ELEC5208 | [控制与优化代码](5208_selected_source.zip) | 规则式 HEMS、优化式 HEMS、SOCP 动态运行区间 |
| ELEC5208 | [年度汇总](5208_annual_summary.csv) | 光伏及两种储能容量的电压、反送电量与不平衡指标 |
| ELEC5206 | [正常入射](5206_mppt_normal.csv)、[倾斜入射](5206_mppt_tilted.csv) | 光伏电压、电流、功率与采样时间 |
| ELEC5206 | [风机测量](5206_wind_measurements.csv) | 三种风速下的转速、转矩和功率 |

## 分析工具

[数据核算脚本](verify_results.py) 计算年度反送电量变化、光伏平均功率与功率乘积差，并定位风机最大功率点。

运行方式：

```shell
python verify_results.py
```
