# Quick Start Guide - Interactive Particle Generator

## Getting Started in 30 Seconds

### Run the Interactive Script
```bash
python run_competition_generation.py
```

### What Happens Next

1. **Welcome Header** - Shows timestamp and container information
2. **Input Prompt** - Enter desired particle count (default: 50)
3. **Parameter Recipe** - View the parameter ranges being used
4. **Real-Time Progress** - Watch as particles are generated with gradual morphology transition
5. **Summary Report** - Complete statistics and file locations

### Gradual Morphology Transition

By default, the script generates 50 particles with an automatic **stepped progression**:
- **Particles 1-10**: Regular shapes (near-spherical, smooth surfaces)
- **Particles 11-20**: Slightly irregular (transitioning angularity)
- **Particles 21-30**: Moderately strange (increased roughness)
- **Particles 31-40**: Highly irregular (pronounced features)
- **Particles 41-50**: Extremely strange (maximum complexity and roughness)

This creates a natural progression from simple to complex shapes.

## Example Session

```
================================================================================
                       SHPSG Particle Generation Tool
================================================================================

Timestamp: 2026-01-21 16:37:33
Target Container: Cylindrical (Diameter: 1000 micrometers)

Goals:
  - Generate irregular particles sized 30-90 micrometers
  - Control particle morphology through Form, Roundness, and Roughness
  - Create realistic particle batch for packing simulation

©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Particle Batch Configuration:
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Enter number of particles to generate (default: 50): 50
>> Using default: 50 particles

[Progress updates shown here...]

================================================================================
                           Work Summary Report
================================================================================

Generation Results:
  Total particles created:  50
  Success rate:             100.0%

Batch Statistics:
  Average particle size:    59.58 micrometers
  Size range:               31.70 - 89.78 micrometers
  Average elongation (Ei):  0.656 (gradual from ~0.9 to ~0.4)
  Average flatness (Fi):    0.637 (gradual from ~0.9 to ~0.4)
  Average angularity:       0.171 (gradual from ~0.05 to ~0.3)
  Average roughness:        0.122 (gradual from ~0.01 to ~0.25)

File Storage:
  Location: ./data/competition_particles
  STL files (3D models):    ./data/competition_particles/*.stl (50 files)
  PNG visualizations:       ./data/competition_particles/*.png (50 files)
  Metadata file:            ./data/competition_particles/metadata.txt

Next Steps:
  1. You can now use these STL files for the random packing simulation (Problem 1.2)
  2. Import STL files into DEM simulation software
  3. Analyze packing efficiency and particle interactions
  4. Use metadata.txt for batch documentation

================================================================================
Generation process completed successfully!
================================================================================
```

## Files Generated

For each particle, you get:
- **particle_XXXX.stl** - 3D model ready for simulation or 3D viewing
- **particle_XXXX.png** - Visual preview of the particle

Plus:
- **metadata.txt** - Complete statistics of all particles

## Key Features

? **User-Friendly** - Interactive prompts guide you through the process
? **Real-Time Progress** - Watch particles being generated
? **Detailed Info** - Particle characteristics displayed as they're created
? **Error Handling** - Graceful handling of any generation issues
? **Complete Report** - Comprehensive summary with next steps

## Common Questions

**Q: How long does it take to generate 50 particles?**
A: About 2-3 minutes (includes 3D visualization generation)

**Q: Can I change the number of particles?**
A: Yes! Just enter a different number when prompted (or accept default of 50)

**Q: What if I want larger/smaller particles?**
A: Current range is 30-90 micrometers. Contact developers to modify ranges.

**Q: Can I disable PNG generation for speed?**
A: Advanced users can modify `run_competition_generation.py` to set `include_png=False`

**Q: Where are the files saved?**
A: All files go to `./data/competition_particles/`

**Q: Can I generate multiple batches?**
A: Yes! Each run will create a new set with the same folder structure

## For Help

- See **INTERACTIVE_USER_GUIDE.py** for detailed documentation
- See **ENHANCEMENT_DOCUMENTATION.py** for technical details
- See **README_ENHANCEMENTS.md** for complete feature overview
