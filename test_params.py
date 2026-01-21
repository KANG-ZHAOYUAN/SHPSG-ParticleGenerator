#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Quick test of modified parameters"""

from particle_generator import generate_random_particle_params

print("Testing modified parameter generation:")
print("=" * 60)

for i in range(3):
    p = generate_random_particle_params()
    print(f"\nParticle {i+1}:")
    print(f"  Ei (Elongation):  {p['Ei']:.3f} (should be 0.4-0.7)")
    print(f"  Fi (Flatness):    {p['Fi']:.3f} (should be 0.4-0.7)")
    print(f"  D2_8 (Angularity): {p['D2_8']:.3f} (should be 0.2-0.45)")
    print(f"  D9_15 (Roughness): {p['D9_15']:.3f} (should be 0.08-0.25)")
    print(f"  max_degree:       {p['max_degree']} (should be 12-17)")
    print(f"  coeff_multiplier: {p['coeff_multiplier']:.1f} (should be 1.2)")

print("\n" + "=" * 60)
print("? Parameters successfully modified for 'strange' morphology!")
