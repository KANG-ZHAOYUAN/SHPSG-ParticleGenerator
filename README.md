# Spherical Harmonics Particle Shape Generator - SHPSG
> **声明**: 本项目参考了仓库 budizhao/SHPSG 的核心逻辑，在此基础上进行了用户友好的改进和优化。该仓库仅用于 2026年哈尔滨工业大学（深圳）弘理杯数学竞赛。
> **Declaration**: This project references the core logic from [budizhao/SHPSG](https://github.com/budizhao/SHPSG) and has been enhanced with user-friendly improvements and optimizations. This repository is intended for use in the **2026 Harbin Institute of Technology (Shenzhen) Hongli Cup Mathematical Modeling Competition** only.
>
> Please refer to [INTERACTIVE_USER_GUIDE.py](INTERACTIVE_USER_GUIDE.py) for the complete user guide.

---

##  Feature Overview

### Core Features

####  Spherical Harmonics Particle Generation
- Generate highly realistic irregular particles using spherical harmonics expansion
- Support extended to 16-degree spherical harmonics (SH degree 16), producing 256 coefficients
- Generate high-fidelity 3D particle geometry

####  Particle Size Control
- Support particle equivalent diameter range: **30-90 micrometers**
- Precise scale scaling suitable for cylindrical container (1000 micrometers diameter) packing simulation
- Parameterized equivalent diameter (D_eq) control

####  Morphological Parameter Control

| Parameter | Range | Description |
|-----------|-------|-------------|
| **Ei (Form)** | [0.6, 1.0] | b/a ratio, controls particle elongation |
| **Fi (Roundness)** | [0.6, 1.0] | c/b ratio, controls particle flatness |
| **D2_8 (Angularity)** | [0.0, 0.35] | Controls SH 2-8 degree coefficients, describes particle angularity |
| **D9_15 (Roughness)** | [0.0, 0.15] | Controls SH 9-15 degree coefficients, describes particle surface roughness |

####  Batch Generation System
- **Standard Particle Generation**: Generate realistic rock-like particles (50-100 per batch)
- **Mixed Morphology Generation**: Support multiple morphology categories
  - Regular: Realistic rock shapes
  - Elongated: High elongation ratio particles
  - Flattened: High flatness ratio particles
  - Angular: High angularity particles
  - Rough: High surface roughness particles

####  Output Formats
- **3D Models (.stl)** - Importable to CAD and simulation software
- **Visualizations (.png)** - Quick preview of particle shapes
- **Metadata Files** - Record all particle parameters and statistics

####  User Interface
- **Interactive Script** (`run_competition_generation.py`) - Real-time parameter input and progress feedback
- **Detailed Work Summary Report** - Generate statistics and file locations
- **Complete Documentation** - Comprehensive guides and examples

### Key Improvements

 Extended spherical harmonics degree (9 → 16), enhanced particle complexity  
 Added particle morphological parameterized control system  
 Implemented efficient batch generation workflow  
 Provided user-friendly interactive interface  
 Complete metadata and statistics reporting  
 STL and PNG dual format output support  

---

##  Quick Start

```bash
# Run interactive particle generator
python run_competition_generation.py
```

See [QUICKSTART.md](QUICKSTART.md) for a 30-second quick start guide.

---

##  Documentation

- [INTERACTIVE_USER_GUIDE.py](INTERACTIVE_USER_GUIDE.py) - Complete user guide
- [README_ENHANCEMENTS.md](README_ENHANCEMENTS.md) - Feature enhancements details
- [README_MIXED_MORPHOLOGY.md](README_MIXED_MORPHOLOGY.md) - Mixed morphology generation guide
- [QUICKSTART.md](QUICKSTART.md) - 30-second quick start