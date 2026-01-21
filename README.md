# Spherical Harmonics Particle Shape Generator - SHPSG

> **声明 / Declaration**: 本项目参考了仓库 [budizhao/SHPSG](https://github.com/budizhao/SHPSG) 的核心逻辑，在此基础上进行了用户友好的改进和优化。该仓库仅用于 **2026年哈尔滨工业大学（深圳）弘理杯数学竞赛**。
>
> This project references the core logic from [budizhao/SHPSG](https://github.com/budizhao/SHPSG) and has been enhanced with user-friendly improvements and optimizations. This repository is intended for use in the **2026 Harbin Institute of Technology (Shenzhen) Hongli Cup Mathematical Modeling Competition** only.


> 可阅读INTERACTIVE_USER_GUIDE，获得用户指南。

---

## ? 功能介绍 / Feature Overview

### 核心功能 (Core Features)

#### ? 球谐函数粒子生成
- 使用球谐函数展开式生成高度逼真的不规则粒子
- 支持扩展到16阶球谐展开 (SH degree 16)，产生256个系数
- 生成高保真的粒子3D几何形状

#### ? 粒子尺寸控制
- 支持粒子等效直径范围：**30-90微米**
- 精确的尺度缩放，适合圆形容器（1000微米直径）堆积模拟
- 参数化等效直径 (D_eq) 控制

#### ? 形态学参数控制

| 参数 | 中文名称 | 范围 | 描述 |
|------|---------|------|------|
| **Ei (Form)** | 伸长率 | [0.6, 1.0] | b/a 比值，控制粒子的伸长程度 |
| **Fi (Roundness)** | 扁平率 | [0.6, 1.0] | c/b 比值，控制粒子的扁平程度 |
| **D2_8 (Angularity)** | 棱角度 | [0.0, 0.35] | 控制SH 2-8阶系数，描述粒子棱角 |
| **D9_15 (Roughness)** | 粗糙度 | [0.0, 0.15] | 控制SH 9-15阶系数，描述粒子表面粗糙度 |

#### ? 批量生成系统
- **标准粒子生成**：生成形状逼真的岩石状粒子 (50-100个/批)
- **混合形态生成**：支持多种形态类别
  - Regular（常规）：现实的岩石形状
  - Elongated（细长）：高伸长率粒子
  - Flattened（扁平）：高扁平率粒子
  - Angular（棱角）：高棱角度粒子
  - Rough（粗糙）：高表面粗糙度粒子

#### ? 输出格式
- **3D模型 (.stl)** - 可导入CAD和仿真软件
- **可视化 (.png)** - 快速预览粒子形状
- **元数据文件** - 记录所有粒子参数和统计信息

#### ? 用户交互界面
- **交互式脚本** (`run_competition_generation.py`) - 实时参数输入和进度反馈
- **详细的工作总结报告** - 生成统计数据和文件位置
- **中英文支持** - 完整的中英文文档和指南

### 主要改进 (Key Improvements)

? 扩展球谐函数阶数 (9 → 16)，增强粒子复杂度  
? 添加粒子形态学参数化控制系统  
? 实现高效的批量生成流程  
? 提供友好的用户交互界面  
? 完整的元数据和统计报告  
? STL和PNG双格式输出支持  

---

## ? 快速开始 (Quick Start)

```bash
# 运行交互式粒子生成器
python run_competition_generation.py
```

详见 [QUICKSTART.md](QUICKSTART.md) 获得30秒快速指南。

---

## ? 文档 (Documentation)

- [INTERACTIVE_USER_GUIDE.py](INTERACTIVE_USER_GUIDE.py) - 完整用户指南
- [README_ENHANCEMENTS.md](README_ENHANCEMENTS.md) - 功能增强详解
- [README_MIXED_MORPHOLOGY.md](README_MIXED_MORPHOLOGY.md) - 混合形态生成指南
- [QUICKSTART.md](QUICKSTART.md) - 30秒快速开始