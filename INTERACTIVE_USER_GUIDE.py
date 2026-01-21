# -*- coding: utf-8 -*-
"""
INTERACTIVE PARTICLE GENERATION SYSTEM - USER GUIDE
交互式粒子生成系统 - 用户指南

This document explains how to use the enhanced, user-friendly SHPSG particle
generation script with interactive features.

本文档介绍如何使用增强的、用户友好的SHPSG粒子生成脚本及其交互功能。
"""

# ============================================================================
# 1. RUNNING THE INTERACTIVE SCRIPT
# 运行交互式脚本
# ============================================================================

"""
BASIC USAGE / 基本用法:
    python run_competition_generation.py

The script will guide you through the process step by step.
脚本将逐步引导您完成整个过程。
"""


# ============================================================================
# 2. WELCOME HEADER & INFORMATION
# ============================================================================

"""
When you start the script, you'll see:

    ================================================================================
                         SHPSG Particle Generation Tool
    ================================================================================

    Timestamp: 2026-01-21 16:37:33
    Target Container: Cylindrical (Diameter: 1000 micrometers)

    Goals:
      - Generate irregular particles sized 30-90 micrometers
      - Control particle morphology through Form, Roundness, and Roughness
      - Create realistic particle batch for packing simulation

This header provides:
    - Current date and time
    - Target container specifications
    - Overall objectives for the particle generation
"""


# ============================================================================
# 3. INTERACTIVE INPUT PHASE
# ============================================================================

"""
STEP 1: Particle Quantity Input

    Particle Batch Configuration:
    ────────────────────────────────────────────────────────────────────────────
    Enter number of particles to generate (default: 50): 

Action:
    - Type a number and press Enter (e.g., 100)
    - Or just press Enter to accept the default (50)
    - If you enter a number > 500, system will ask for confirmation

Examples:
    - Input: 50 -> Generates 50 particles
    - Input: (blank) -> Uses default 50
    - Input: 1000 -> Asks: "Continue? (y/n):"

The system validates input and handles errors gracefully.
"""


# ============================================================================
# 4. RECIPE DISPLAY
# ============================================================================

"""
STEP 2: Current Parameter Recipe

    Current 'Recipe' - Parameter Ranges:
    ────────────────────────────────────────────────────────────────────────────
    Form Parameters:
      - Elongation Index (Ei):  [0.6, 1.0]  (spherical to elongated)
      - Flatness Index (Fi):    [0.6, 1.0]  (oblate to spherical)

    Morphology Parameters:
      - Roundness/Angularity (D2_8):  [0.00, 0.35]  (smooth to angular)
      - Roughness (D9_15):             [0.00, 0.15]  (smooth to rough)

    Size Parameter:
      - Equivalent Diameter (D_eq):    [30, 90] micrometers (uniform random)

Information Provided:
    - Parameter ranges for each morphological feature
    - Physical interpretation of each parameter
    - How each parameter affects particle appearance
    - All values are randomly selected within these ranges for each particle

Understanding the Recipe:
    - Ei=1.0, Fi=1.0: Perfectly spherical
    - Ei<0.8: Prolate (elongated)
    - Fi<0.8: Oblate (flattened)
    - D2_8=0: Perfectly smooth corners
    - D2_8=0.35: Highly angular edges
    - D9_15=0: Smooth surface
    - D9_15=0.15: Rough, bumpy surface
"""


# ============================================================================
# 5. REAL-TIME PROGRESS REPORTING
# ============================================================================

"""
STEP 3: Particle Generation with Progress

    Preparation Phase:
    ────────────────────────────────────────────────────────────────────────────
    Generating base mesh geometry...
    >> Mesh geometry ready (Surface elements: 320)

    Generation Phase:
    ────────────────────────────────────────────────────────────────────────────
    [============================--------------------] 58.0%

Features of Progress Reporting:

1. PROGRESS BAR:
   - Shows visual representation of completion
   - Updates in real-time as particles are generated
   - Percentage display at the right

2. DETAILED INFORMATION (every 10 particles):
   
   Step 10/50: particle_0009.stl
     Size: 65.4 um | Type: Oblate | Roundness: 0.18 | Surface: Moderately Rough

   Information includes:
   - Step counter (X/Total)
   - Filename being generated
   - Size in micrometers
   - Particle type classification
   - Roundness/Angularity value (D2_8)
   - Surface roughness description

3. PARTICLE TYPE CLASSIFICATION:
   - Spherical: Ei >= 0.9 AND Fi >= 0.9
   - Prolate: Ei < 0.8 AND Fi >= 0.85 (elongated)
   - Oblate: Ei >= 0.85 AND Fi < 0.8 (flattened)
   - Mixed: All other combinations

4. SURFACE DESCRIPTION:
   - Smooth: D9_15 < 0.05
   - Moderately Rough: 0.05 <= D9_15 < 0.10
   - Very Rough: D9_15 >= 0.10
"""


# ============================================================================
# 6. ERROR HANDLING
# ============================================================================

"""
ERROR HANDLING FEATURES:

The script includes try-except blocks to handle failures gracefully.

Example Warning:
    WARNING: Failed to generate particle_5
    Error: [Errno 13] Permission denied

When an error occurs:
    1. The specific particle index is identified
    2. The error message is displayed
    3. Generation continues with remaining particles
    4. Final report shows success/failure statistics

Possible Errors:
    - Disk space issues: "No space left on device"
    - Permission problems: "Permission denied"
    - Invalid directory: "No such file or directory"
    - Memory issues: "Memory error"

Recovery:
    - Failed particles are tracked separately
    - Success rate is calculated and displayed
    - Metadata file still contains only successful particles
"""


# ============================================================================
# 7. WORK SUMMARY REPORT
# ============================================================================

"""
FINAL OUTPUT: Comprehensive Summary Report

    ================================================================================
                              Work Summary Report
    ================================================================================

    Generation Results:
    ────────────────────────────────────────────────────────────────────────────
      Total particles created:  50
      Success rate:             100.0%

    Batch Statistics:
    ────────────────────────────────────────────────────────────────────────────
      Average particle size:    62.34 micrometers
      Size range:               30.12 - 89.87 micrometers
      Average elongation (Ei):  0.814
      Average flatness (Fi):    0.795
      Average angularity:       0.168
      Average roughness:        0.072

    File Storage:
    ────────────────────────────────────────────────────────────────────────────
      Location: ./data/competition_particles
      STL files (3D models):    ./data/competition_particles/*.stl (50 files)
      PNG visualizations:       ./data/competition_particles/*.png (50 files)
      Metadata file:            ./data/competition_particles/metadata.txt

    Next Steps:
    ────────────────────────────────────────────────────────────────────────────
      1. You can now use these STL files for the random packing simulation (Problem 1.2)
      2. Import STL files into DEM simulation software
      3. Analyze packing efficiency and particle interactions
      4. Use metadata.txt for batch documentation

Summary Information Includes:

1. GENERATION RESULTS:
   - Total particles successfully created
   - Number of failed particles (if any)
   - Success rate percentage

2. BATCH STATISTICS:
   - Mean particle size and range
   - Average values for all morphological parameters
   - Distribution information for quality assessment

3. FILE STORAGE:
   - Directory where files are saved
   - Number of STL files (3D models)
   - Number of PNG files (visualizations)
   - Metadata file location for documentation

4. NEXT STEPS:
   - Guidance for using particles in simulations
   - Recommended workflow for competition
   - Integration suggestions with external software
"""


# ============================================================================
# 8. OUTPUT FILE STRUCTURE
# ============================================================================

"""
FILES GENERATED:

./data/competition_particles/
├── particle_0000.stl        (3D model - 30-90 micrometers)
├── particle_0000.png        (Visualization - automatically scaled)
├── particle_0001.stl
├── particle_0001.png
├── ...
├── particle_0049.stl
├── particle_0049.png
└── metadata.txt             (Statistics and attributes)

Total: 50 STL + 50 PNG + 1 metadata = 101 files


METADATA FILE FORMAT:

Particle Generation Metadata
================================================================================

Total particles: 50
D_eq range (um): 30.45 - 89.87
Ei range: 0.601 - 0.998
Fi range: 0.602 - 0.997
D2_8 range: 0.001 - 0.349
D9_15 range: 0.003 - 0.149

================================================================================

Individual Particle Data:
================================================================================
Index  D_eq(um)   Ei       Fi       D2_8     D9_15   
────────────────────────────────────────────────────────────────────────────
0      45.23      0.812    0.654    0.156    0.043   
1      67.89      0.945    0.723    0.012    0.098   
...
49     52.34      0.678    0.891    0.287    0.014   


STL FILE FORMAT:
    - Binary STL format (industry standard)
    - Contains full 3D geometry of particle
    - Compatible with:
        * CAD software (Blender, FreeCAD, SolidWorks)
        * DEM simulation software
        * 3D visualization tools
        * 3D printing software

PNG FILE FORMAT:
    - 3D visualization of particle
    - Automatically scaled based on particle size
    - Shows wireframe and shaded surfaces
    - Useful for quick visual inspection
"""


# ============================================================================
# 9. EXAMPLE WORKFLOW
# ============================================================================

"""
COMPLETE WORKFLOW EXAMPLE:

Step 1: Launch the script
    $ python run_competition_generation.py

Step 2: See the welcome header
    [Displays timestamp, container info, goals]

Step 3: Enter particle count
    Enter number of particles to generate (default: 50): 100
    >> Confirmed: Generating 100 particles

Step 4: Review the recipe
    [Shows all parameter ranges]

Step 5: Watch real-time progress
    [Progress bar and detailed info for every 10 particles]
    [Generates STL and PNG files]

Step 6: Review the summary
    [Shows statistics and success rate]
    [Confirms file locations]
    [Provides next steps]

Step 7: Use the generated particles
    - Import STL files into DEM software
    - Use metadata.txt for initial conditions
    - Analyze results in simulation
"""


# ============================================================================
# 10. TIPS AND TROUBLESHOOTING
# ============================================================================

"""
TIPS FOR OPTIMAL USE:

1. BATCH SIZE SELECTION:
   - Start with 10-20 for quick testing
   - Use 50-100 for realistic packing simulations
   - Avoid >500 unless you have time and disk space

2. GENERATION TIME:
   - Each particle: ~2-3 seconds (with PNG)
   - 50 particles: ~2-3 minutes
   - 100 particles: ~4-6 minutes
   - Can disable PNG with code modification for faster generation

3. DISK SPACE:
   - Each particle: ~300-400 KB (STL + PNG)
   - 50 particles: ~20 MB
   - 100 particles: ~40 MB
   - Ensure adequate disk space in ./data/ folder

4. VERIFYING RESULTS:
   - Check file count: should be 2*N + 1 (N particles, N PNGs, 1 metadata)
   - Open PNG files to visually inspect particles
   - Review metadata.txt for statistical summary
   - Import sample STL into CAD software to verify geometry


TROUBLESHOOTING:

Issue: "No such file or directory" when saving files
Solution: Ensure ./data/ folder exists, or create it manually
    mkdir -p ./data/competition_particles

Issue: Script runs very slowly
Solution: 
    - Check disk space availability
    - Reduce batch size if necessary
    - Disable PNG generation in advanced usage

Issue: Generated particles look incorrect
Solution:
    - Verify STL file is opened correctly in 3D viewer
    - Check if D_eq scaling is applied correctly
    - Ensure matplotlib backend is configured properly

Issue: Metadata file is empty or incomplete
Solution:
    - Check folder permissions
    - Ensure disk has write access
    - Verify metadata.txt path is correct
"""


# ============================================================================
# 11. ADVANCED CUSTOMIZATION
# ============================================================================

"""
MODIFYING PARAMETER RANGES:

To change the particle size range from [30, 90] to [40, 80]:

1. Edit particle_generator.py
2. Find generate_random_particle_params() function
3. Change: 'D_eq': np.random.uniform(30, 90)
   To:      'D_eq': np.random.uniform(40, 80)


To change angularity range:

   Change: 'D2_8': np.random.uniform(0.0, 0.35)
   To:      'D2_8': np.random.uniform(0.1, 0.25)


To disable PNG generation (faster):

1. Edit run_competition_generation.py
2. Change: include_png=True
   To:      include_png=False


REPRODUCIBLE RESULTS:

To generate the same batch twice:

1. Add at the start of main():
   import numpy as np
   np.random.seed(42)

2. This makes random generation deterministic
3. All runs with same seed produce identical particles
"""


# ============================================================================
# 12. INTEGRATION WITH COMPETITION PROBLEM
# ============================================================================

"""
HOW TO USE FOR COMPETITION PROBLEM 1.2 (Packing Simulation):

1. GENERATE PARTICLES:
   python run_competition_generation.py
   [Select appropriate batch size for your simulation]

2. VERIFY FILES:
   - Check ./data/competition_particles/ for STL files
   - Review metadata.txt for particle properties
   - Open a sample PNG to verify geometry

3. IMPORT INTO DEM SOFTWARE:
   - Most DEM software accepts STL format
   - Load metadata.txt for initial particle attributes
   - Set simulation container to 1000 um diameter cylinder

4. RUN SIMULATION:
   - Execute random packing simulation
   - Monitor packing efficiency
   - Analyze particle interactions

5. COLLECT RESULTS:
   - Export final packing configuration
   - Document statistics
   - Compare with theoretical predictions

The generated particles provide realistic irregular geometry suitable for
accurate granular material simulations.
"""


if __name__ == '__main__':
    print("Interactive SHPSG Particle Generation System - User Guide")
    print("For interactive use, run: python run_competition_generation.py")
