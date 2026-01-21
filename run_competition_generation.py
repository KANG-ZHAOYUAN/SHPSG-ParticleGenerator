# -*- coding: utf-8 -*-
"""
Complete Example: Generate a batch of irregular particles for packing simulation
This script demonstrates all the enhanced SHPSG features.
"""

import numpy as np
from particle_generator import (
    batch_generate_particles,
    save_particle_metadata,
    generate_random_particle_params
)
import os
import sys
from datetime import datetime


def print_header():
    """Print the welcome header with timestamp and container info"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("\n" + "=" * 80)
    print(" " * 15 + "SHPSG Particle Generation Tool")
    print("=" * 80)
    print("\nTimestamp: {}".format(timestamp))
    print("Target Container: Cylindrical (Diameter: 1000 micrometers)")
    print("\nGoals:")
    print("  - Generate irregular particles sized 30-90 micrometers")
    print("  - Control particle morphology through Form, Roundness, and Roughness")
    print("  - Create realistic particle batch for packing simulation")
    print("\n" + "-" * 80)


def get_user_input():
    """Get number of particles from user with validation"""
    default_num = 50
    
    print("\nParticle Batch Configuration:")
    print("-" * 80)
    
    try:
        user_input = input("Enter number of particles to generate (default: {}): ".format(default_num))
        
        if user_input.strip() == "":
            num_particles = default_num
            print(">> Using default: {} particles".format(default_num))
        else:
            num_particles = int(user_input)
            if num_particles < 1:
                print(">> Invalid input. Using default: {} particles".format(default_num))
                num_particles = default_num
            elif num_particles > 500:
                print(">> Warning: Large batch ({} particles) may take significant time".format(num_particles))
                confirm = input("   Continue? (y/n): ").strip().lower()
                if confirm != 'y':
                    print(">> Generation cancelled. Using default: {} particles".format(default_num))
                    num_particles = default_num
    except ValueError:
        print(">> Invalid input. Using default: {} particles".format(default_num))
        num_particles = default_num
    
    return num_particles


def show_parameter_recipe():
    """Display the current parameter ranges (recipe)"""
    print("\nCurrent 'Recipe' - Parameter Ranges:")
    print("-" * 80)
    print("  Form Parameters:")
    print("    - Elongation Index (Ei):  [0.6, 1.0]  (spherical to elongated)")
    print("    - Flatness Index (Fi):    [0.6, 1.0]  (oblate to spherical)")
    print("\n  Morphology Parameters:")
    print("    - Roundness/Angularity (D2_8):  [0.00, 0.35]  (smooth to angular)")
    print("    - Roughness (D9_15):             [0.00, 0.15]  (smooth to rough)")
    print("\n  Size Parameter:")
    print("    - Equivalent Diameter (D_eq):    [30, 90] micrometers (uniform random)")
    print("\n" + "-" * 80)


def get_particle_type(ei, fi):
    """Determine particle shape type based on Ei and Fi"""
    if ei >= 0.9 and fi >= 0.9:
        return "Spherical"
    elif ei < 0.8 and fi >= 0.85:
        return "Prolate"
    elif ei >= 0.85 and fi < 0.8:
        return "Oblate"
    else:
        return "Mixed"


def get_surface_description(d9_15):
    """Describe surface roughness"""
    if d9_15 < 0.05:
        return "Smooth"
    elif d9_15 < 0.10:
        return "Moderately Rough"
    else:
        return "Very Rough"


def progress_bar(current, total, width=50):
    """Generate a simple progress bar"""
    percent = float(current) / total
    filled = int(width * percent)
    bar = '=' * filled + '-' * (width - filled)
    return "[{}] {:.1f}%".format(bar, percent * 100)


def enhanced_batch_generate_particles(num_particles, output_dir='./data/competition_particles', 
                                      include_png=True):
    """
    Enhanced batch generation with interactive progress reporting.
    Returns list of particles with error tracking.
    """
    import os
    from SHPSG import SHPSG
    from funcs import sh2stl, plotstl, icosahedron, subdivsurf, cleanmesh, car2sph
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    print("\nPreparation Phase:")
    print("-" * 80)
    print("Generating base mesh geometry...")
    
    # Pre-generate mesh geometry
    level = 2
    vertices, faces = icosahedron()
    for i in range(level):
        vertices, faces = subdivsurf(faces, vertices)
        vertices, faces = cleanmesh(faces, vertices)
    sph_cor = car2sph(vertices)
    print(">> Mesh geometry ready (Surface elements: {})".format(len(faces)))
    
    # Generation phase
    print("\nGeneration Phase:")
    print("-" * 80)
    
    particle_list = []
    failed_particles = []
    
    for i in range(num_particles):
        try:
            # Show progress
            sys.stdout.write("\r" + progress_bar(i + 1, num_particles) + " ")
            sys.stdout.flush()
            
            # Generate random parameters with gradual transition
            params = generate_random_particle_params(particle_index=i, total_particles=num_particles)
            
            # Generate coefficients
            coeff = SHPSG(params['Ei'], params['Fi'], params['D2_8'], params['D9_15'])
            
            # Create filenames
            stl_filename = "{}/particle_{:04d}.stl".format(output_dir, i)
            png_filename = "{}/particle_{:04d}.png".format(output_dir, i) if include_png else None
            
            # Generate STL
            vertices_copy = vertices.copy()
            sh2stl(coeff, sph_cor, vertices_copy, faces, stl_filename, D_eq=params['D_eq'])
            
            # Generate PNG
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
            
            # Print detailed info every 10 particles or at end
            if (i + 1) % 10 == 0 or i == num_particles - 1:
                particle_type = get_particle_type(params['Ei'], params['Fi'])
                surface = get_surface_description(params['D9_15'])
                sys.stdout.write("\n")
                sys.stdout.flush()
                print("  Step {}/{}: particle_{:04d}.stl".format(
                    i + 1, num_particles, i))
                print("    Size: {:.1f} um | Type: {} | Roundness: {:.2f} | Surface: {}".format(
                    params['D_eq'], particle_type, params['D2_8'], surface))
                sys.stdout.write(progress_bar(i + 1, num_particles) + " ")
                sys.stdout.flush()
        
        except Exception as e:
            failed_particles.append((i, str(e)))
            print("\n  WARNING: Failed to generate particle_{}".format(i))
            print("    Error: {}".format(str(e)))
    
    print("\n")
    return particle_list, failed_particles


def print_summary(particles, failed_particles, output_dir):
    """Print comprehensive summary report"""
    print("\n" + "=" * 80)
    print(" " * 25 + "Work Summary Report")
    print("=" * 80)
    
    successful_count = len(particles)
    total_count = successful_count + len(failed_particles)
    
    print("\nGeneration Results:")
    print("-" * 80)
    print("  Total particles created:  {}".format(successful_count))
    if failed_particles:
        print("  Failed to generate:       {}".format(len(failed_particles)))
        print("  Success rate:             {:.1f}%".format(100.0 * successful_count / total_count))
    else:
        print("  Success rate:             100.0%")
    
    if successful_count > 0:
        d_eq_values = [p['D_eq'] for p in particles]
        ei_values = [p['Ei'] for p in particles]
        fi_values = [p['Fi'] for p in particles]
        d2_8_values = [p['D2_8'] for p in particles]
        d9_15_values = [p['D9_15'] for p in particles]
        
        print("\nBatch Statistics:")
        print("-" * 80)
        print("  Average particle size:    {:.2f} micrometers".format(np.mean(d_eq_values)))
        print("  Size range:               {:.2f} - {:.2f} micrometers".format(
            np.min(d_eq_values), np.max(d_eq_values)))
        print("  Average elongation (Ei):  {:.3f}".format(np.mean(ei_values)))
        print("  Average flatness (Fi):    {:.3f}".format(np.mean(fi_values)))
        print("  Average angularity:       {:.3f}".format(np.mean(d2_8_values)))
        print("  Average roughness:        {:.3f}".format(np.mean(d9_15_values)))
        
        print("\nFile Storage:")
        print("-" * 80)
        print("  Location: {}".format(output_dir))
        print("  STL files (3D models):    {}/*.stl ({} files)".format(output_dir, successful_count))
        print("  PNG visualizations:       {}/*.png ({} files)".format(output_dir, successful_count))
        print("  Metadata file:            {}/metadata.txt".format(output_dir))
    
    print("\nNext Steps:")
    print("-" * 80)
    print("  1. You can now use these STL files for the random packing simulation (Problem 1.2)")
    print("  2. Import STL files into DEM simulation software")
    print("  3. Analyze packing efficiency and particle interactions")
    print("  4. Use metadata.txt for batch documentation")
    
    if failed_particles:
        print("\nFailed Particles:")
        print("-" * 80)
        for idx, error in failed_particles:
            print("  particle_{:04d}: {}".format(idx, error))
    
    print("\n" + "=" * 80)
    print("Generation process completed successfully!")
    print("=" * 80 + "\n")


def main():
    """Main execution function with enhanced interactivity"""
    
    # Display welcome header
    print_header()
    
    # Get user input
    num_particles = get_user_input()
    
    # Show parameter recipe
    show_parameter_recipe()
    
    # Set output directory
    output_dir = './data/competition_particles'
    
    # Generate particles with enhanced progress reporting
    print("\nStarting particle generation...")
    print("This may take a while depending on batch size and PNG generation.\n")
    
    particles, failed_particles = enhanced_batch_generate_particles(
        num_particles=num_particles,
        output_dir=output_dir,
        include_png=True
    )
    
    # Save metadata
    try:
        save_particle_metadata(particles, output_file=os.path.join(output_dir, 'metadata.txt'))
    except Exception as e:
        print("WARNING: Failed to save metadata: {}".format(str(e)))
    
    # Print comprehensive summary
    print_summary(particles, failed_particles, output_dir)
    
    return particles


if __name__ == '__main__':
    particles = main()

