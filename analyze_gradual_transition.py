#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Analyze the gradual transition in generated particles"""

import re

metadata_file = "./data/competition_particles/metadata.txt"

# Parse the metadata file
particles = []
with open(metadata_file, 'r') as f:
    lines = f.readlines()
    in_data_section = False
    for line in lines:
        if "Individual Particle Data" in line:
            in_data_section = True
            continue
        if in_data_section and line.strip().startswith("UNK"):
            parts = line.split()
            if len(parts) >= 7:
                particles.append({
                    'filename': parts[1],
                    'D_eq': float(parts[2]),
                    'Ei': float(parts[3]),
                    'Fi': float(parts[4]),
                    'D2_8': float(parts[5]),
                    'D9_15': float(parts[6])
                })

print("Gradual Morphology Transition Analysis")
print("=" * 80)

# Analyze key groups
groups = {
    "Group 0 (0-9)": particles[0:10],
    "Group 1 (10-19)": particles[10:20],
    "Group 2 (20-29)": particles[20:30],
    "Group 3 (30-39)": particles[30:40],
    "Group 4 (40-49)": particles[40:50]
}

print("\nParameter Averages by Group:")
print("-" * 80)
print(f"{'Group':<15} {'Ei (avg)':<12} {'Fi (avg)':<12} {'D2_8 (avg)':<12} {'D9_15 (avg)':<12}")
print("-" * 80)

for group_name, group_particles in groups.items():
    if group_particles:
        ei_avg = sum(p['Ei'] for p in group_particles) / len(group_particles)
        fi_avg = sum(p['Fi'] for p in group_particles) / len(group_particles)
        d2_8_avg = sum(p['D2_8'] for p in group_particles) / len(group_particles)
        d9_15_avg = sum(p['D9_15'] for p in group_particles) / len(group_particles)
        print(f"{group_name:<15} {ei_avg:<12.4f} {fi_avg:<12.4f} {d2_8_avg:<12.4f} {d9_15_avg:<12.4f}")

print("\n" + "=" * 80)
print("Visual Representation (normalized 0-1):")
print("-" * 80)

# Create visual bars
for group_name, group_particles in groups.items():
    if group_particles:
        ei_avg = sum(p['Ei'] for p in group_particles) / len(group_particles)
        fi_avg = sum(p['Fi'] for p in group_particles) / len(group_particles)
        d2_8_avg = sum(p['D2_8'] for p in group_particles) / len(group_particles)
        d9_15_avg = sum(p['D9_15'] for p in group_particles) / len(group_particles)
        
        # Normalize to 0-1 range
        ei_norm = max(0, min(1, ei_avg / 1.0))
        fi_norm = max(0, min(1, fi_avg / 1.0))
        d2_8_norm = max(0, min(1, d2_8_avg / 0.35))
        d9_15_norm = max(0, min(1, d9_15_avg / 0.27))
        
        bar_width = 30
        ei_bar = "=" * int(ei_norm * bar_width)
        fi_bar = "=" * int(fi_norm * bar_width)
        d2_8_bar = "=" * int(d2_8_norm * bar_width)
        d9_15_bar = "=" * int(d9_15_norm * bar_width)
        
        print(f"\n{group_name}:")
        print(f"  Ei      [{ei_bar:<30}] {ei_avg:.3f} (should decrease)")
        print(f"  Fi      [{fi_bar:<30}] {fi_avg:.3f} (should decrease)")
        print(f"  D2_8    [{d2_8_bar:<30}] {d2_8_avg:.3f} (should increase)")
        print(f"  D9_15   [{d9_15_bar:<30}] {d9_15_avg:.3f} (should increase)")

print("\n" + "=" * 80)
print("Expected Progression:")
print("  Group 0: Near-spherical (Ei~0.9, Fi~0.9) with smooth surface")
print("  Group 1: Transition (Ei~0.75, Fi~0.75) with angular features")
print("  Group 2: Mixed (Ei~0.65, Fi~0.65) with rough surface")
print("  Group 3: More irregular (Ei~0.55, Fi~0.55) with more roughness")
print("  Group 4: Extremely strange (Ei~0.4, Fi~0.4) with maximum roughness")
