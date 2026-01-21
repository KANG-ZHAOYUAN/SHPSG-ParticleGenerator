# -*- coding: utf-8 -*-
"""
Mixed Morphology Batch Generation Script

This script demonstrates how to generate a batch with:
- Category A (Regular): 40 particles with realistic rock-like shapes
  * SH degree: 8-12
  * Standard coefficients (multiplier = 1.0)
  * Typical aspect ratios (Ei: 0.8-1.0, Fi: 0.7-0.95)

- Category B (Weird): 10 particles with extreme spikes and hollows
  * SH degree: 30-50 (high frequency features)
  * Amplified coefficients (multiplier: 5-10x)
  * Extreme aspect ratios (Ei: 0.2-0.5, Fi: 0.1-0.4)

Output Structure:
  ./Output_Batch/
    ©À©¤©¤ particle_reg_01.stl
    ©À©¤©¤ particle_reg_01.png
    ©À©¤©¤ particle_reg_02.stl
    ©À©¤©¤ ...
    ©À©¤©¤ particle_reg_40.stl
    ©À©¤©¤ particle_weird_01.stl
    ©À©¤©¤ particle_weird_01.png
    ©À©¤©¤ particle_weird_02.stl
    ©À©¤©¤ ...
    ©À©¤©¤ particle_weird_10.stl
    ©¸©¤©¤ metadata.txt
"""

from particle_generator import batch_generate_mixed_particles, save_particle_metadata
import os

def main():
    """Main execution function"""
    
    print("\n" + "=" * 100)
    print(" " * 30 + "MIXED MORPHOLOGY PARTICLE BATCH GENERATOR")
    print("=" * 100)
    
    print("\nConfiguration:")
    print("-" * 100)
    print("  Category A (Regular):  40 particles")
    print("    ©¸©¤ Realistic rock-like shapes with typical aspect ratios")
    print("    ©¸©¤ SH Degree: 8-12 (standard frequency range)")
    print("    ©¸©¤ Coefficient multiplier: 1.0x (standard)")
    print("\n  Category B (Weird):     10 particles")
    print("    ©¸©¤ Extreme shapes with spikes and hollows")
    print("    ©¸©¤ SH Degree: 30-50 (high frequency range)")
    print("    ©¸©¤ Coefficient multiplier: 5-10x (amplified)")
    print("\n  Total: 50 unique particles (80% regular, 20% weird)")
    print("-" * 100)
    
    # Generate mixed batch
    print("\nGenerating particles...\n")
    particles = batch_generate_mixed_particles(
        output_dir='./Output_Batch',
        regular_count=40,
        weird_count=10,
        include_png=True,
        verbose=True
    )
    
    # Save metadata
    print("\nSaving metadata...")
    metadata_file = './Output_Batch/metadata.txt'
    save_particle_metadata(particles, metadata_file)
    
    # Print summary
    print("\n" + "=" * 100)
    print("GENERATION COMPLETE")
    print("=" * 100)
    print("Output Directory: ./Output_Batch/")
    print("Total files generated: {}".format(len(particles) * 2 + 1))  # STL + PNG + metadata
    print("  - Regular particles: 40 (particle_reg_01.stl ~ particle_reg_40.stl)")
    print("  - Weird particles: 10 (particle_weird_01.stl ~ particle_weird_10.stl)")
    print("  - Metadata file: metadata.txt")
    print("=" * 100 + "\n")
    
    return particles


if __name__ == '__main__':
    particles = main()
