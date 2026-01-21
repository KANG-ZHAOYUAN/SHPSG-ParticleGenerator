# SHPSG - Spherical Harmonics Particle Shape Generator

> **For:** 2026 Harbin Institute of Technology (Shenzhen) Hongli Cup Mathematical Modeling Competition
> 
> **Base Project:** [budizhao/SHPSG](https://github.com/budizhao/SHPSG)

---

## What This Tool Does

Generate highly realistic **irregular particles** for packing simulations.

### Three Core Capabilities

| Capability | Parameter | Range | Effect |
|------------|-----------|-------|--------|
| **1. Form Control** | Ei, Fi | 0.4-0.9 | Control particle elongation and flatness (create non-spherical shapes) |
| **2. Roundness** | D2_8 | 0.0-0.35 | Generate angular features and macroscopic protrusions |
| **3. Roughness** | D9_15 | 0.0-0.25 | Add surface texture and microscopic irregularities |

### Additional Features

- **Particle Size:** 30-90 micrometers
- **Batch Generation:** 50 particles with automatic gradual transition (smooth ¡ú extreme)
- **Output:** 3D models (.stl), visualizations (.png), metadata (txt)
- **Gradual Progression:** 5 groups showing shape evolution from spherical to extremely strange

---

## Quick Start: 3 Steps

### Step 1: Environment Setup
```bash
# Ensure you have Python 3 with required packages
pip install numpy scipy matplotlib
```

### Step 2: Run Generator
```bash
cd D:/HIT/Mathematical_Modeling/2026_Hong_Li/SHPSG
python run_competition_generation.py
```

### Step 3: Input Parameters
```
Enter number of particles to generate (default: 50):
>> Press Enter to use default, or type a number
```

**That's it!** Generated files appear in `./data/competition_particles/`

---

## Output Files

For 50 particles:
- `particle_0000.stl` to `particle_0049.stl` ¡ª 3D models for simulation
- `particle_0000.png` to `particle_0049.png` ¡ª Visual previews
- `metadata.txt` ¡ª All particle parameters and statistics

---

## Parameter Customization

To customize morphology, edit the parameter ranges in `particle_generator.py`:

```python
# In generate_random_particle_params() function
'Ei': np.random.uniform(0.4, 0.9),      # Change elongation range
'Fi': np.random.uniform(0.4, 0.9),      # Change flatness range
'D2_8': np.random.uniform(0.2, 0.45),   # Change angularity range
'D9_15': np.random.uniform(0.08, 0.25), # Change roughness range
```

---

## Advanced Usage

### Generate Only STL (No PNG)
```bash
# Edit run_competition_generation.py, line ~280
# Change: include_png=True to include_png=False
python run_competition_generation.py
```

### Reproducible Results
```python
# Add at top of run_competition_generation.py
import numpy as np
np.random.seed(42)
```

### Single Particle
```python
from SHPSG import SHPSG
from funcs import sh2stl, plotstl, icosahedron, subdivsurf, cleanmesh, car2sph

# Setup geometry
vertices, faces = icosahedron()
for i in range(2):
    vertices, faces = subdivsurf(faces, vertices)
    vertices, faces = cleanmesh(faces, vertices)
sph_cor = car2sph(vertices)

# Create and save particle
coeff = SHPSG(Ei=0.5, Fi=0.5, D2_8=0.3, D9_15=0.2)
vertices_copy = vertices.copy()
sh2stl(coeff, sph_cor, vertices_copy, faces, 'my_particle.stl', D_eq=60.0)
plotstl('my_particle.stl', 'my_particle.png', D_eq=60.0)
```

---

## Documentation

- **[QUICKSTART.md](QUICKSTART.md)** ¡ª 30-second quick start with example output
- **[GRADUAL_TRANSITION_GUIDE.md](GRADUAL_TRANSITION_GUIDE.md)** ¡ª Detailed gradual morphology transition explanation
- **[README_ENHANCEMENTS.md](README_ENHANCEMENTS.md)** ¡ª Complete enhancement technical details
- **[INTERACTIVE_USER_GUIDE.py](INTERACTIVE_USER_GUIDE.py)** ¡ª Full interactive guide

---

## File Structure

```
SHPSG/
©À©¤©¤ run_competition_generation.py  (Main script - use this!)
©À©¤©¤ particle_generator.py          (Batch generation functions)
©À©¤©¤ SHPSG.py                       (Core algorithm)
©À©¤©¤ funcs.py                       (Utilities)
©À©¤©¤ main.ipynb                     (Jupyter notebook example)
©¸©¤©¤ data/
    ©¸©¤©¤ competition_particles/     (Output folder)
        ©À©¤©¤ particle_*.stl
        ©À©¤©¤ particle_*.png
        ©¸©¤©¤ metadata.txt
```

---

## Common Questions

**Q: How long does it take to generate 50 particles?**  
A: ~2-3 minutes (includes STL generation and PNG visualization)

**Q: Can I change the number of particles?**  
A: Yes! Enter a different number when prompted (or modify the script)

**Q: What if I want only STL files without PNG?**  
A: Edit `run_competition_generation.py` and set `include_png=False`

**Q: How do I use these particles in simulation software?**  
A: Import the .stl files directly into DEM software (Yade, LIGGGHTS, etc.)

**Q: Can I fix a random seed for reproducibility?**  
A: Yes! Add `np.random.seed(42)` before generation

---

## Support

For technical implementation details, see [README_ENHANCEMENTS.md](README_ENHANCEMENTS.md).

For complete API documentation, see [INTERACTIVE_USER_GUIDE.py](INTERACTIVE_USER_GUIDE.py).