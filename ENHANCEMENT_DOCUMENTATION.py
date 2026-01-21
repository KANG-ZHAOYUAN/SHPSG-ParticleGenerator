# -*- coding: utf-8 -*-
"""
SHPSG ENHANCEMENT DOCUMENTATION
Enhanced Spherical Harmonics Particle Shape Generator for Mathematical Modeling

This document outlines all modifications made to support competition requirements.
"""

# ============================================================================
# 1. SPHERICAL HARMONICS EXPANSION DEPTH
# ============================================================================

"""
MODIFICATION: funcs.py - sph2cart() function
CHANGE: Extended SH expansion from degree 9 to degree 16

Original:
    for n in range(9):  # Limited to degree 9
        
Enhanced:
    for n in range(16):  # Extended to degree 16

RATIONALE:
- Degrees 0-8: Form (sphere geometry) + Angularity
- Degrees 9-15: Roughness features (high-frequency surface details)
- Extended range enables realistic surface roughness simulation

IMPACT:
- Coefficient matrix size: 81x3 -> 256x3 (16^2 coefficients)
- Higher computational cost but better shape fidelity
- Roughness descriptor D9_15 now fully functional for all degrees 9-15
"""


# ============================================================================
# 2. PARTICLE SIZE CONTROL
# ============================================================================

"""
MODIFICATION: funcs.py - sh2stl() function
ENHANCEMENT: Added D_eq parameter for equivalent diameter scaling

New Signature:
    def sh2stl(coeff, sph_cor, vertices, faces, stlpath, D_eq=1.0)

Parameters:
    - D_eq: equivalent diameter (in micrometers), default 1.0 for backward compatibility

Implementation:
    scale_factor = D_eq / 2.0  # radius scaling
    vertices_copy[:,i] *= scale_factor  # Apply to all coordinates

FEATURES:
- Supports particles in 30-90 micrometers range
- Maintains normalized SH representation
- Simple linear scaling without distortion

USAGE:
    sh2stl(coeff, sph_cor, vertices, faces, 'particle.stl', D_eq=60.0)
"""


# ============================================================================
# 3. VISUALIZATION WITH DYNAMIC SCALING
# ============================================================================

"""
MODIFICATION: funcs.py - plotstl() function
ENHANCEMENT: Adaptive axis limits based on particle size

New Signature:
    def plotstl(stlpath, figpath, D_eq=1.0)

Dynamic Axis Limits:
    margin = D_eq * 0.6  # 60% margin for better visualization
    ax.set_xlim([-margin, margin])
    ax.set_ylim([-margin, margin])
    ax.set_zlim([-margin, margin])

BENEFITS:
- Automatically scales visualization for 30-90 um particles
- Consistent visual representation across all sizes
- No manual axis adjustment needed
- Maintains aspect ratio

EXAMPLE RANGES:
    D_eq=30 um -> limits: [-18, 18]
    D_eq=60 um -> limits: [-36, 36]
    D_eq=90 um -> limits: [-54, 54]
"""


# ============================================================================
# 4. MORPHOLOGICAL PARAMETER FUNCTIONS
# ============================================================================

"""
NEW FILE: particle_generator.py

FUNCTION 1: generate_coeffs(Ei, Fi, D2_8, D9_15)
    Purpose: Generate SH coefficients with morphological control
    Input: Form parameters (Ei, Fi) and descriptor parameters (D2_8, D9_15)
    Output: 256x3 complex coefficient matrix
    Note: Wraps original SHPSG() function for consistency

FUNCTION 2: generate_random_particle_params()
    Purpose: Create randomized parameters for each particle
    Returns: Dictionary with random values:
        - Ei (Elongation): uniform [0.6, 1.0]   (spherical to elongated)
        - Fi (Flatness): uniform [0.6, 1.0]     (oblate to spherical)
        - D2_8 (Angularity): uniform [0.0, 0.35] (rounded to angular)
        - D9_15 (Roughness): uniform [0.0, 0.15] (smooth to rough)
        - D_eq (Size): uniform [30, 90]         (30-90 micrometers)

FUNCTION 3: batch_generate_particles(num_particles, output_dir, include_png, verbose)
    Purpose: Batch generation of particles with unique attributes
    Parameters:
        - num_particles: default 50 (adjustable for competition needs)
        - output_dir: default './data/particles'
        - include_png: whether to generate visualizations
        - verbose: progress reporting
    Returns: List of particle metadata dictionaries
    
    Process:
        1. Pre-compute mesh geometry once (efficient reuse)
        2. For each particle:
           - Generate random morphological parameters
           - Generate SH coefficients
           - Create STL file with scaling
           - Generate PNG visualization
           - Store metadata
        3. Return complete particle list with all attributes

FUNCTION 4: save_particle_metadata(particle_list, output_file)
    Purpose: Export particle attributes to text file
    Output Format: Formatted table with statistics
        - Total count
        - Distribution ranges (D_eq, Ei, Fi, D2_8, D9_15)
        - Individual particle data rows
    
    Sample Output:
        Particle Generation Metadata
        ================================================================================
        Total particles: 50
        D_eq range (um): 30.45 - 89.87
        Ei range: 0.601 - 0.998
        Fi range: 0.602 - 0.997
        D2_8 range: 0.001 - 0.349
        D9_15 range: 0.003 - 0.149
        ...
"""


# ============================================================================
# 5. BATCH PARTICLE GENERATION WORKFLOW
# ============================================================================

"""
EXECUTION SCRIPT: run_competition_generation.py

Main Features:
    - Generates 50 particles (configurable)
    - Each particle has unique random attributes
    - Outputs both STL (3D model) and PNG (visualization)
    - Saves comprehensive metadata

Usage:
    python run_competition_generation.py

Output Structure:
    ./data/competition_particles/
        

Size and Diversity:
    - All particles between 30-90 micrometers
    - Random form (Ei, Fi) ensures shape variety
    - Random angularity (D2_8) for corner features
    - Random roughness (D9_15) for surface features
    - Each particle is computationally unique
"""


# ============================================================================
# 6. MORPHOLOGICAL PARAMETERS EXPLAINED
# ============================================================================

"""
THREE-SCALE PARTICLE SHAPE CHARACTERIZATION

SCALE 1: FORM (Elongation Ei, Flatness Fi)
    - Ei = b/a (aspect ratio of b-axis to a-axis)
        - Ei = 1.0: spherical
        - Ei < 1.0: elongated/prolate
    - Fi = c/b (aspect ratio of c-axis to b-axis)
        - Fi = 1.0: spherical
        - Fi < 1.0: flattened/oblate
    
    Control: SHPSG() function parameters Ei, Fi

SCALE 2: ROUNDNESS/ANGULARITY (D2_8 descriptor)
    - Controlled by SH degrees 2-8
    - D2_8 = 0.0: perfectly smooth spheroid
    - D2_8 = 0.35: highly angular particle with sharp corners
    - Simulates intermediate-scale features
    - Random coefficients in degree range 2-8 create angular variations
    
    Control: Descriptor parameter D2_8

SCALE 3: ROUGHNESS (D9_15 descriptor)
    - Controlled by SH degrees 9-15
    - D9_15 = 0.0: smooth surface
    - D9_15 = 0.15: rough/bumpy surface
    - Simulates high-frequency surface details
    - Random coefficients in degree range 9-15 create bumps/ridges
    
    Control: Descriptor parameter D9_15

IMPLEMENTATION IN SHPSG():
    The original SHPSG() function handles the mathematical details:
    1. Uses Ei, Fi to scale the l=1 coefficients (form)
    2. Normalizes D2_8 across degrees 2-8 based on power law (alpha=1.387)
    3. Normalizes D9_15 across degrees 9-15 based on power law (beta=1.426)
    4. Generates random complex coefficients for each SH degree
    5. Applies normalization to achieve target descriptors
    6. Returns 256x3 complex coefficient matrix (16x16 per dimension)
"""


# ============================================================================
# 7. MATHEMATICAL MODELING APPLICATION
# ============================================================================

"""
COMPETITION CONTEXT: Irregular Particle Packing in Cylindrical Container

Container Specifications:
    - Cylindrical geometry
    - Height: 1000 micrometers
    - Diameter: Typical for particle dynamics simulations

Particle Batch Generation:
    - 50 unique particles per batch
    - Size range: 30-90 micrometers
    - Irregular shapes (form, roundness, roughness all vary)
    
These particles can be used for:
    1. Discrete Element Method (DEM) simulations
    2. Packing density analysis
    3. Flow behavior studies
    4. Stress distribution modeling
    5. Realistic granular material behavior

Each particle exhibits:
    - Natural size distribution
    - Shape irregularity at multiple scales
    - Individual uniqueness (no identical twins)
    - Physically realistic geometry (via SH decomposition)
"""


# ============================================================================
# 8. BACKWARD COMPATIBILITY
# ============================================================================

"""
All modifications maintain backward compatibility with original code:

Original function calls still work:
    sh2stl(coeff, sph_cor, vertices, faces, stlpath)
        -> Uses default D_eq=1.0 (original behavior)
    
    plotstl(stlpath, figpath)
        -> Uses default D_eq=1.0 (original behavior)
    
    sph2cart(coeff, phi, theta)
        -> Automatically handles 256 coefficients (extended to degree 16)

All extensions are optional parameters with sensible defaults.
"""


# ============================================================================
# 9. USAGE EXAMPLES
# ============================================================================

"""
EXAMPLE 1: Generate single particle with custom size
    from SHPSG import SHPSG
    from funcs import sh2stl, plotstl, icosahedron, subdivsurf, cleanmesh, car2sph
    
    # Setup geometry
    level = 2
    vertices, faces = icosahedron()
    for i in range(level):
        vertices, faces = subdivsurf(faces, vertices)
        vertices, faces = cleanmesh(faces, vertices)
    sph_cor = car2sph(vertices)
    
    # Generate 60 micrometer particle
    coeff = SHPSG(Ei=0.8, Fi=0.9, D2_8=0.2, D9_15=0.1)
    vertices_copy = vertices.copy()
    sh2stl(coeff, sph_cor, vertices_copy, faces, 'my_particle.stl', D_eq=60.0)
    plotstl('my_particle.stl', 'my_particle.png', D_eq=60.0)


EXAMPLE 2: Generate batch of 100 particles
    from particle_generator import batch_generate_particles, save_particle_metadata
    
    particles = batch_generate_particles(num_particles=100, verbose=True)
    save_particle_metadata(particles, 'particle_stats.txt')


EXAMPLE 3: Custom size distribution (e.g., 50-70 micrometers)
    # Modify generate_random_particle_params() in particle_generator.py
    # Change: 'D_eq': np.random.uniform(50, 70)
    # Or create wrapper function with custom range


EXAMPLE 4: Export particle data for CFD/DEM simulations
    for particle in particles:
        print("ID: {} | Size: {:.1f} um | Angularity: {:.2f}".format(
            particle['index'], particle['D_eq'], particle['D2_8']))
"""


# ============================================================================
# 10. TECHNICAL NOTES
# ============================================================================

"""
1. COEFFICIENT GENERATION:
   - 81 coefficients per dimension (original: degree 9, 0-9)
   - 256 coefficients per dimension (enhanced: degree 16, 0-15)
   - Complex values handle phase information for full 3D description

2. RANDOM SEEDING:
   - np.random used without fixed seed for natural variation
   - For reproducibility, set: np.random.seed(42)

3. NUMERICAL STABILITY:
   - SH normalization prevents overflow at high degrees
   - Power law parameters (alpha, beta) calibrated for realistic shapes

4. PERFORMANCE:
   - Mesh geometry pre-computed once, reused for all 50 particles
   - PNG generation (~3 seconds each) can be disabled with include_png=False
   - STL generation is very fast (< 0.1 seconds)

5. MEMORY USAGE:
   - Each particle: ~256x3 complex coefficients (6 KB)
   - Batch of 50: ~300 KB coefficients
   - Visualization memory is temporary (cleared after PNG saved)
"""


if __name__ == '__main__':
    print("SHPSG Enhancement Documentation")
    print("For usage examples, see run_competition_generation.py")
