# -*- coding: utf-8 -*-
"""
Enhanced Particle Generation Module for SHPSG
Supports:
- Size control (30-90 micrometers)
- Batch generation with unique attributes
- Advanced morphological parameters (Angularity, Roughness)
"""

import numpy as np
from SHPSG import SHPSG
from funcs import icosahedron, subdivsurf, cleanmesh, car2sph, sh2stl, plotstl


def generate_coeffs(Ei, Fi, D2_8, D9_15):
    """
    Generate spherical harmonics coefficients with morphological control.
    
    Parameters:
    - Ei: Elongation index (b/a), range [0.5, 1.0]
    - Fi: Flatness index (c/b), range [0.5, 1.0]
    - D2_8: Angularity descriptor, range [0.0, 0.4]
    - D9_15: Roughness descriptor, range [0.0, 0.2]
    
    Returns:
    - coeff: SH coefficients matrix (256x3 complex)
    """
    # Call the original SHPSG function which handles all the math
    coeff = SHPSG(Ei, Fi, D2_8, D9_15)
    return coeff


def generate_random_particle_params():
    """
    Generate random morphological parameters for a unique particle.
    
    Returns:
    - params: dict with keys Ei, Fi, D2_8, D9_15, D_eq
    """
    params = {
        'Ei': np.random.uniform(0.6, 1.0),      # Elongation: more spherical to elongated
        'Fi': np.random.uniform(0.6, 1.0),      # Flatness: more oblate to spherical
        'D2_8': np.random.uniform(0.0, 0.35),   # Angularity: low to high
        'D9_15': np.random.uniform(0.0, 0.15),  # Roughness: smooth to rough
        'D_eq': np.random.uniform(30, 90)       # Equivalent diameter: 30-90 micrometers
    }
    return params


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
        
        # Generate random parameters for this particle
        params = generate_random_particle_params()
        
        # Generate SH coefficients
        coeff = generate_coeffs(
            params['Ei'],
            params['Fi'],
            params['D2_8'],
            params['D9_15']
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
            'png_path': png_filename
        }
        particle_list.append(particle_metadata)
    
    if verbose:
        print("Successfully generated {} particles!".format(num_particles))
    
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
        f.write("=" * 80 + "\n\n")
        f.write("Total particles: {}\n".format(len(particle_list)))
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
        f.write("\n" + "=" * 80 + "\n\n")
        f.write("Individual Particle Data:\n")
        f.write("=" * 80 + "\n")
        f.write("{:<6} {:<10} {:<8} {:<8} {:<8} {:<8}\n".format(
            'Index', 'D_eq(um)', 'Ei', 'Fi', 'D2_8', 'D9_15'))
        f.write("-" * 80 + "\n")
        
        for p in particle_list:
            f.write("{:<6d} {:<10.2f} {:<8.3f} {:<8.3f} {:<8.3f} {:<8.3f}\n".format(
                p['index'], p['D_eq'], p['Ei'], p['Fi'], p['D2_8'], p['D9_15']))

if __name__ == '__main__':
    """
    Example usage: Generate 50 particles and save metadata
    """
    # Generate batch of 50 particles
    particles = batch_generate_particles(num_particles=50, verbose=True)
    
    # Save metadata to file
    save_particle_metadata(particles)
    
    print("\nParticle batch generation complete!")
    print("Files saved to: ./data/particles/")
