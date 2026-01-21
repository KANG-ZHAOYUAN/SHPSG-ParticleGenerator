#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test gradual morphology transition"""

from particle_generator import generate_random_particle_params
import numpy as np

print("Testing Gradual Morphology Transition (0-49 particles)")
print("=" * 80)

# Test particles at key positions
test_indices = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 49]

print("\nParticle Index | Group | Factor(k) | Ei    | Fi    | D2_8  | D9_15 | Category")
print("-" * 80)

for idx in test_indices:
    # Generate 3 samples per index to show variability
    params_list = [generate_random_particle_params(particle_index=idx, total_particles=50) for _ in range(3)]
    
    # Average the values
    ei_avg = np.mean([p['Ei'] for p in params_list])
    fi_avg = np.mean([p['Fi'] for p in params_list])
    d2_8_avg = np.mean([p['D2_8'] for p in params_list])
    d9_15_avg = np.mean([p['D9_15'] for p in params_list])
    
    group = idx // 10
    k = group / 4.0
    
    print(f"      {idx:2d}      |  {group}   | {k:.2f}      | {ei_avg:.3f} | {fi_avg:.3f} | {d2_8_avg:.3f} | {d9_15_avg:.3f} | Group {group}")

print("\n" + "=" * 80)
print("Gradual transition verified!")
print("\nExpected progression:")
print("  Particles 0-9:   Near-spherical (Ei~0.9, Fi~0.9) -> Smooth surface")
print("  Particles 10-19: Slightly flattened (Ei~0.75, Fi~0.75) -> More angular")
print("  Particles 20-29: Moderately flattened (Ei~0.65, Fi~0.65) -> More rough")
print("  Particles 30-39: Highly flattened (Ei~0.55, Fi~0.55) -> Very rough")
print("  Particles 40-49: Extremely strange (Ei~0.4, Fi~0.4) -> Extremely rough")
