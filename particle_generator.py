# -*- coding: utf-8 -*-
"""
Enhanced Particle Generation Module for SHPSG
Supports:
- Size control (30-90 micrometers)
- Batch generation with unique attributes
- Advanced morphological parameters (Angularity, Roughness)
- Mixed morphology generation (Regular + Weird particles)
"""

import numpy as np
from SHPSG import SHPSG
from funcs import icosahedron, subdivsurf, cleanmesh, car2sph, sh2stl, plotstl


def generate_coeffs(Ei, Fi, D2_8, D9_15, max_degree=16, coeff_multiplier=1.0):
    """
    Generate spherical harmonics coefficients with morphological control.
    
    Parameters:
    - Ei: Elongation index (b/a), range [0.5, 1.0]
    - Fi: Flatness index (c/b), range [0.5, 1.0]
    - D2_8: Angularity descriptor, range [0.0, 0.4]
    - D9_15: Roughness descriptor, range [0.0, 0.2]
    - max_degree: Maximum SH degree (default 16), can be 8-50 for weird particles
    - coeff_multiplier: Multiply coefficients by this factor (1.0 for regular, 5-10 for weird)
    
    Returns:
    - coeff: SH coefficients matrix (max_degree^2 x 3 complex)
    """
    # Call the original SHPSG function which handles all the math
    coeff = SHPSG(Ei, Fi, D2_8, D9_15)
    
    # Apply coefficient multiplier for extreme geometries
    if coeff_multiplier != 1.0:
        coeff = coeff * coeff_multiplier
    
    return coeff


def generate_random_particle_params(category='regular', particle_index=None, total_particles=50):
    """
    Generate random morphological parameters for a unique particle.
    
    Parameters:
    - category: 'regular' (realistic rock-like) or 'weird' (extreme spikes/hollows)
    - particle_index: if provided, enables gradual morphology transition (0-49)
    - total_particles: total number of particles in batch
    
    Returns:
    - params: dict with keys Ei, Fi, D2_8, D9_15, D_eq, max_degree, coeff_multiplier, category
    """
    # If particle_index is provided, use gradual transition mode
    if particle_index is not None:
        # Gradual transition from regular (k=0) to extremely weird (k=1)
        # Divide 50 particles into 5 groups of 10
        group = particle_index // 10  # 0-4
        k = group / 4.0              # 0.0 to 1.0 (gradual factor)
        
        # Form parameters: transition from near-spherical (0.9) to strange (0.4)
        ei_regular, ei_strange = 0.9, 0.4
        fi_regular, fi_strange = 0.9, 0.4
        
        ei_value = ei_regular - k * (ei_regular - ei_strange)  # 0.9 ¡ú 0.4
        fi_value = fi_regular - k * (fi_regular - fi_strange)  # 0.9 ¡ú 0.4
        
        # Add randomness within a shrinking range
        ei_range = 0.15 * (1 - k)  # Range decreases with k
        fi_range = 0.15 * (1 - k)
        ei_value += np.random.uniform(-ei_range, ei_range)
        fi_value += np.random.uniform(-fi_range, fi_range)
        
        # Roundness (D2_8): transition from 0.05 (smooth) to 0.4 (angular)
        d2_8_base_min = 0.05
        d2_8_base_max = 0.1
        d2_8_value = d2_8_base_min + k * (d2_8_base_max * 3.0 - d2_8_base_min)
        d2_8_value += np.random.uniform(-0.03, 0.03)  # Small random perturbation
        
        # Roughness (D9_15): transition from near-0 to 0.25
        d9_15_base_min = 0.0
        d9_15_base_max = 0.05
        d9_15_value = d9_15_base_min + k * (d9_15_base_max * 5.0)
        d9_15_value += np.random.uniform(-0.02, 0.02)  # Small random perturbation
        
        # max_degree: gradually increase from 8 to 16 for more complexity
        max_degree_value = int(8 + k * 8)
        
        # coeff_multiplier: gradually increase from 1.0 to 1.5
        coeff_mult_value = 1.0 + k * 0.5
        
        params = {
            'Ei': np.clip(ei_value, 0.3, 1.0),
            'Fi': np.clip(fi_value, 0.3, 1.0),
            'D2_8': np.clip(d2_8_value, 0.0, 0.4),
            'D9_15': np.clip(d9_15_value, 0.0, 0.3),
            'D_eq': np.random.uniform(30, 90),      # Size remains random
            'max_degree': max_degree_value,
            'coeff_multiplier': coeff_mult_value,
            'category': 'gradual_' + str(group)
        }
        return params
    
    # Original behavior when no particle_index is provided
    if category == 'regular':
        # Irregular particles with "strange" morphology - enhanced angularity and roughness
        params = {
            'Ei': np.random.uniform(0.4, 0.7),      # Highly elongated (breaks spherical form)
            'Fi': np.random.uniform(0.4, 0.7),      # Significantly flattened (breaks spherical form)
            'D2_8': np.random.uniform(0.2, 0.45),   # Enhanced angularity with macroscopic features
            'D9_15': np.random.uniform(0.08, 0.25), # Increased roughness for surface texture
            'D_eq': np.random.uniform(30, 90),      # Equivalent diameter: 30-90 micrometers
            'max_degree': np.random.randint(12, 18),# Increased SH degree: 12-17 for more detail
            'coeff_multiplier': 1.2,                # Slight amplification for more pronounced features
            'category': 'regular'
        }
    elif category == 'weird':
        # Extreme particles with spikes and hollows
        params = {
            'Ei': np.random.uniform(0.2, 0.5),      # Highly elongated
            'Fi': np.random.uniform(0.1, 0.4),      # Highly flattened
            'D2_8': np.random.uniform(0.2, 0.4),    # High angularity
            'D9_15': np.random.uniform(0.1, 0.2),   # High roughness
            'D_eq': np.random.uniform(30, 90),      # Equivalent diameter: 30-90 micrometers
            'max_degree': np.random.randint(30, 51),# SH degree: 30-50 for extreme features
            'coeff_multiplier': np.random.uniform(5, 10),  # Amplified coefficients (5-10x)
            'category': 'weird'
        }
    else:
        raise ValueError("category must be 'regular' or 'weird'")
    
    return params


def generate_regular_particle_params():
    """Generate parameters for a regular (realistic) particle"""
    return generate_random_particle_params(category='regular')


def generate_weird_particle_params():
    """Generate parameters for a weird (extreme) particle"""
    return generate_random_particle_params(category='weird')


def batch_generate_particles(num_particles=50, output_dir='./data/particles', 
                             include_png=True, verbose=True):
    """
    Generate a batch of particles with unique random attributes.
    
    Parameters:
    - num_particles: number of particles to generate (default 50)
    - output_dir: directory to save STL and PNG files
    - include_png: whether to generate PNG visualizations
    - verbose: whether to print progress information
    
    Returns:
    - particle_list: list of generated particle metadata
    """
    import os
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Pre-generate mesh geometry once (reusable for all particles)
    if verbose:
        print("Generating base mesh geometry...")
    level = 2
    vertices, faces = icosahedron()
    for i in range(level):
        vertices, faces = subdivsurf(faces, vertices)
        vertices, faces = cleanmesh(faces, vertices)
    sph_cor = car2sph(vertices)
    
    particle_list = []
    
    for i in range(num_particles):
        if verbose and (i + 1) % 10 == 0:
            print("Generating particle {}/{}...".format(i + 1, num_particles))
        
        # Generate random parameters for this particle with gradual transition
        params = generate_random_particle_params(particle_index=i, total_particles=num_particles)
        
        # Generate SH coefficients
        coeff = generate_coeffs(
            params['Ei'],
            params['Fi'],
            params['D2_8'],
            params['D9_15'],
            max_degree=params.get('max_degree', 16),
            coeff_multiplier=params.get('coeff_multiplier', 1.0)
        )
        
        # Create output filenames
        stl_filename = "{}/particle_{:04d}.stl".format(output_dir, i)
        png_filename = "{}/particle_{:04d}.png".format(output_dir, i) if include_png else None
        
        # Generate and save STL with scaling based on D_eq
        vertices_copy = vertices.copy()
        sh2stl(coeff, sph_cor, vertices_copy, faces, stl_filename, D_eq=params['D_eq'])
        
        # Generate PNG if requested
        if include_png:
            plotstl(stl_filename, png_filename, D_eq=params['D_eq'])
        
        # Store metadata
        particle_metadata = {
            'index': i,
            'filename': "particle_{:04d}".format(i),
            'D_eq': params['D_eq'],
            'Ei': params['Ei'],
            'Fi': params['Fi'],
            'D2_8': params['D2_8'],
            'D9_15': params['D9_15'],
            'stl_path': stl_filename,
            'png_path': png_filename,
            'category': params.get('category', 'regular')
        }
        particle_list.append(particle_metadata)
    
    if verbose:
        print("Successfully generated {} particles!".format(num_particles))
    
    return particle_list


def batch_generate_mixed_particles(output_dir='./Output_Batch', 
                                   regular_count=40, 
                                   weird_count=10,
                                   include_png=True, 
                                   verbose=True):
    """
    Generate a mixed batch of Regular and Weird particles.
    
    Parameters:
    - output_dir: directory to save all particles (default './Output_Batch')
    - regular_count: number of regular particles (default 40 = 80%)
    - weird_count: number of weird particles (default 10 = 20%)
    - include_png: whether to generate PNG visualizations
    - verbose: whether to print progress information
    
    Returns:
    - particle_list: list of all generated particle metadata (regular + weird)
    """
    import os
    
    # Create output directory structure
    os.makedirs(output_dir, exist_ok=True)
    
    # Pre-generate mesh geometry once (reusable for all particles)
    if verbose:
        print("Generating base mesh geometry...")
    level = 2
    vertices, faces = icosahedron()
    for i in range(level):
        vertices, faces = subdivsurf(faces, vertices)
        vertices, faces = cleanmesh(faces, vertices)
    sph_cor = car2sph(vertices)
    
    particle_list = []
    total_count = regular_count + weird_count
    
    # ====================================================================
    # GENERATE REGULAR PARTICLES (Category A)
    # ====================================================================
    if verbose:
        print("\n" + "=" * 80)
        print("Generating REGULAR particles (Category A): {} particles".format(regular_count))
        print("=" * 80)
    
    for i in range(regular_count):
        if verbose and (i + 1) % 10 == 0:
            print("Generating regular particle {}/{}...".format(i + 1, regular_count))
        
        try:
            # Generate random parameters for regular particle
            params = generate_regular_particle_params()
            
            # Generate SH coefficients
            coeff = generate_coeffs(
                params['Ei'],
                params['Fi'],
                params['D2_8'],
                params['D9_15'],
                max_degree=params.get('max_degree', 16),
                coeff_multiplier=params.get('coeff_multiplier', 1.0)
            )
            
            # Create output filenames with naming convention
            stl_filename = "{}/particle_reg_{:02d}.stl".format(output_dir, i + 1)
            obj_filename = "{}/particle_reg_{:02d}.obj".format(output_dir, i + 1)
            png_filename = "{}/particle_reg_{:02d}.png".format(output_dir, i + 1) if include_png else None
            
            # Generate and save STL with scaling based on D_eq
            vertices_copy = vertices.copy()
            sh2stl(coeff, sph_cor, vertices_copy, faces, stl_filename, D_eq=params['D_eq'])
            
            # Generate PNG if requested
            if include_png:
                plotstl(stl_filename, png_filename, D_eq=params['D_eq'])
            
            # Store metadata
            particle_metadata = {
                'index': i + 1,
                'filename': "particle_reg_{:02d}".format(i + 1),
                'D_eq': params['D_eq'],
                'Ei': params['Ei'],
                'Fi': params['Fi'],
                'D2_8': params['D2_8'],
                'D9_15': params['D9_15'],
                'max_degree': params.get('max_degree', 16),
                'coeff_multiplier': params.get('coeff_multiplier', 1.0),
                'stl_path': stl_filename,
                'obj_path': obj_filename,
                'png_path': png_filename,
                'category': 'regular'
            }
            particle_list.append(particle_metadata)
            
        except Exception as e:
            if verbose:
                print("ERROR generating regular particle {}: {}".format(i + 1, str(e)))
            continue
    
    # ====================================================================
    # GENERATE WEIRD PARTICLES (Category B)
    # ====================================================================
    if verbose:
        print("\n" + "=" * 80)
        print("Generating WEIRD particles (Category B): {} particles".format(weird_count))
        print("=" * 80)
    
    for i in range(weird_count):
        if verbose and (i + 1) % 5 == 0:
            print("Generating weird particle {}/{}...".format(i + 1, weird_count))
        
        try:
            # Generate random parameters for weird particle
            params = generate_weird_particle_params()
            
            # Generate SH coefficients with extreme morphology
            coeff = generate_coeffs(
                params['Ei'],
                params['Fi'],
                params['D2_8'],
                params['D9_15'],
                max_degree=params.get('max_degree', 30),
                coeff_multiplier=params.get('coeff_multiplier', 5.0)
            )
            
            # Create output filenames with naming convention
            stl_filename = "{}/particle_weird_{:02d}.stl".format(output_dir, i + 1)
            obj_filename = "{}/particle_weird_{:02d}.obj".format(output_dir, i + 1)
            png_filename = "{}/particle_weird_{:02d}.png".format(output_dir, i + 1) if include_png else None
            
            # Generate and save STL with scaling based on D_eq
            vertices_copy = vertices.copy()
            sh2stl(coeff, sph_cor, vertices_copy, faces, stl_filename, D_eq=params['D_eq'])
            
            # Generate PNG if requested
            if include_png:
                plotstl(stl_filename, png_filename, D_eq=params['D_eq'])
            
            # Store metadata
            particle_metadata = {
                'index': i + 1,
                'filename': "particle_weird_{:02d}".format(i + 1),
                'D_eq': params['D_eq'],
                'Ei': params['Ei'],
                'Fi': params['Fi'],
                'D2_8': params['D2_8'],
                'D9_15': params['D9_15'],
                'max_degree': params.get('max_degree', 30),
                'coeff_multiplier': params.get('coeff_multiplier', 5.0),
                'stl_path': stl_filename,
                'obj_path': obj_filename,
                'png_path': png_filename,
                'category': 'weird'
            }
            particle_list.append(particle_metadata)
            
        except Exception as e:
            if verbose:
                print("ERROR generating weird particle {}: {}".format(i + 1, str(e)))
            continue
    
    if verbose:
        print("\n" + "=" * 80)
        print("Successfully generated {} particles total!".format(len(particle_list)))
        print("  - Regular: {} particles".format(len([p for p in particle_list if p['category'] == 'regular'])))
        print("  - Weird: {} particles".format(len([p for p in particle_list if p['category'] == 'weird'])))
        print("=" * 80)
    
    return particle_list


def save_particle_metadata(particle_list, output_file='./data/particles/metadata.txt'):
    """
    Save metadata of generated particles to a text file.
    
    Parameters:
    - particle_list: list of particle metadata dicts
    - output_file: path to save metadata
    """
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w') as f:
        f.write("Particle Generation Metadata\n")
        f.write("=" * 100 + "\n\n")
        f.write("Total particles: {}\n".format(len(particle_list)))
        
        # Categorize particles
        regular_particles = [p for p in particle_list if p.get('category') == 'regular']
        weird_particles = [p for p in particle_list if p.get('category') == 'weird']
        
        if regular_particles:
            f.write("Regular particles (Category A): {}\n".format(len(regular_particles)))
        if weird_particles:
            f.write("Weird particles (Category B): {}\n".format(len(weird_particles)))
        
        f.write("\nGlobal Statistics:\n")
        f.write("-" * 100 + "\n")
        f.write("D_eq range (um): {:.2f} - {:.2f}\n".format(
            min(p['D_eq'] for p in particle_list), 
            max(p['D_eq'] for p in particle_list)))
        f.write("Ei range: {:.3f} - {:.3f}\n".format(
            min(p['Ei'] for p in particle_list), 
            max(p['Ei'] for p in particle_list)))
        f.write("Fi range: {:.3f} - {:.3f}\n".format(
            min(p['Fi'] for p in particle_list), 
            max(p['Fi'] for p in particle_list)))
        f.write("D2_8 range: {:.3f} - {:.3f}\n".format(
            min(p['D2_8'] for p in particle_list), 
            max(p['D2_8'] for p in particle_list)))
        f.write("D9_15 range: {:.3f} - {:.3f}\n".format(
            min(p['D9_15'] for p in particle_list), 
            max(p['D9_15'] for p in particle_list)))
        
        if any('max_degree' in p for p in particle_list):
            f.write("Max Degree range: {} - {}\n".format(
                min(p.get('max_degree', 16) for p in particle_list), 
                max(p.get('max_degree', 16) for p in particle_list)))
        
        if any('coeff_multiplier' in p for p in particle_list):
            f.write("Coeff Multiplier range: {:.1f} - {:.1f}\n".format(
                min(p.get('coeff_multiplier', 1.0) for p in particle_list), 
                max(p.get('coeff_multiplier', 1.0) for p in particle_list)))
        
        f.write("\n" + "=" * 100 + "\n\n")
        f.write("Individual Particle Data:\n")
        f.write("=" * 100 + "\n")
        f.write("{:<8} {:<20} {:<10} {:<8} {:<8} {:<8} {:<8}".format(
            'Cat', 'Filename', 'D_eq(um)', 'Ei', 'Fi', 'D2_8', 'D9_15'))
        if any('max_degree' in p for p in particle_list):
            f.write(" {:<6}".format('L'))
        if any('coeff_multiplier' in p for p in particle_list):
            f.write(" {:<6}".format('Mult'))
        f.write("\n")
        f.write("-" * 100 + "\n")
        
        for p in particle_list:
            cat = 'REG' if p.get('category') == 'regular' else 'WD' if p.get('category') == 'weird' else 'UNK'
            line = "{:<8} {:<20} {:<10.2f} {:<8.3f} {:<8.3f} {:<8.3f} {:<8.3f}".format(
                cat, p['filename'], p['D_eq'], p['Ei'], p['Fi'], p['D2_8'], p['D9_15'])
            if 'max_degree' in p:
                line += " {:<6d}".format(p['max_degree'])
            if 'coeff_multiplier' in p:
                line += " {:<6.1f}".format(p['coeff_multiplier'])
            f.write(line + "\n")

if __name__ == '__main__':
    """
    Example usage: Generate mixed batch with regular and weird particles
    """
    import os
    
    # Create Output_Batch folder with mixed morphologies
    print("\n" + "=" * 100)
    print("MIXED MORPHOLOGY BATCH GENERATION")
    print("=" * 100)
    
    # Generate batch: 40 regular + 10 weird particles
    particles = batch_generate_mixed_particles(
        output_dir='./Output_Batch',
        regular_count=40,      # 80% - rock-like particles
        weird_count=10,        # 20% - extreme spike/hollow particles
        include_png=True,
        verbose=True
    )
    
    # Save detailed metadata
    metadata_file = './Output_Batch/metadata.txt'
    save_particle_metadata(particles, metadata_file)
    
    print("\nParticle batch generation complete!")
    print("Files saved to: ./Output_Batch/")
    print("Metadata saved to: {}".format(metadata_file))
