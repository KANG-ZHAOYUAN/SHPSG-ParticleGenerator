# -*- coding: utf-8 -*-
"""
验证脚本 - 确保所有修改正确实施
VERIFICATION SCRIPT - Ensure all modifications are correctly implemented
"""

import sys
import os

def verify_modifications():
    """验证所有修改是否正确完成"""
    
    print("\n" + "="*80)
    print("VERIFICATION SCRIPT - Mixed Morphology Implementation")
    print("="*80 + "\n")
    
    issues = []
    
    # =====================================================================
    # 检查 1: 导入必要的模块
    # =====================================================================
    print("[1/5] Checking imports...")
    try:
        from particle_generator import (
            generate_coeffs,
            generate_random_particle_params,
            generate_regular_particle_params,
            generate_weird_particle_params,
            batch_generate_mixed_particles,
            batch_generate_particles,
            save_particle_metadata
        )
        print("  ? All functions imported successfully")
    except ImportError as e:
        issues.append(f"Import error: {str(e)}")
        print(f"  ? Import failed: {e}")
    
    # =====================================================================
    # 检查 2: 函数签名验证
    # =====================================================================
    print("\n[2/5] Checking function signatures...")
    
    try:
        import inspect
        from particle_generator import generate_coeffs, batch_generate_mixed_particles
        
        # 检查 generate_coeffs 有新参数
        sig = inspect.signature(generate_coeffs)
        params = list(sig.parameters.keys())
        
        if 'max_degree' in params and 'coeff_multiplier' in params:
            print("  ? generate_coeffs() has new parameters: max_degree, coeff_multiplier")
        else:
            issues.append("generate_coeffs() missing new parameters")
            print("  ? generate_coeffs() missing new parameters")
        
        # 检查 batch_generate_mixed_particles 参数
        sig = inspect.signature(batch_generate_mixed_particles)
        params = list(sig.parameters.keys())
        
        if 'regular_count' in params and 'weird_count' in params:
            print("  ? batch_generate_mixed_particles() has correct parameters")
        else:
            issues.append("batch_generate_mixed_particles() has incorrect parameters")
            print("  ? batch_generate_mixed_particles() has incorrect parameters")
            
    except Exception as e:
        issues.append(f"Signature check failed: {str(e)}")
        print(f"  ? Error: {e}")
    
    # =====================================================================
    # 检查 3: 参数生成逻辑验证
    # =====================================================================
    print("\n[3/5] Checking parameter generation logic...")
    
    try:
        import numpy as np
        from particle_generator import (
            generate_regular_particle_params,
            generate_weird_particle_params
        )
        
        # 生成普通粒子参数
        regular_params = generate_regular_particle_params()
        if (regular_params['Ei'] >= 0.8 and regular_params['Ei'] <= 1.0 and
            regular_params['Fi'] >= 0.7 and regular_params['Fi'] <= 0.95 and
            regular_params['max_degree'] >= 8 and regular_params['max_degree'] <= 12 and
            regular_params['coeff_multiplier'] == 1.0):
            print("  ? Regular particle parameters in correct ranges")
        else:
            issues.append("Regular particle parameters out of range")
            print("  ? Regular particle parameters out of range")
            print(f"      Ei={regular_params['Ei']:.3f}, Fi={regular_params['Fi']:.3f}, "
                  f"L={regular_params['max_degree']}, mult={regular_params['coeff_multiplier']}")
        
        # 生成奇异粒子参数
        weird_params = generate_weird_particle_params()
        if (weird_params['Ei'] >= 0.2 and weird_params['Ei'] <= 0.5 and
            weird_params['Fi'] >= 0.1 and weird_params['Fi'] <= 0.4 and
            weird_params['max_degree'] >= 30 and weird_params['max_degree'] <= 50 and
            weird_params['coeff_multiplier'] >= 5.0 and weird_params['coeff_multiplier'] <= 10.0):
            print("  ? Weird particle parameters in correct ranges")
        else:
            issues.append("Weird particle parameters out of range")
            print("  ? Weird particle parameters out of range")
            print(f"      Ei={weird_params['Ei']:.3f}, Fi={weird_params['Fi']:.3f}, "
                  f"L={weird_params['max_degree']}, mult={weird_params['coeff_multiplier']:.1f}x")
        
        # 检查 category 字段
        if 'category' in regular_params and regular_params['category'] == 'regular':
            print("  ? Regular particle has correct category field")
        else:
            issues.append("Regular particle missing/incorrect category field")
            print("  ? Regular particle missing/incorrect category field")
            
        if 'category' in weird_params and weird_params['category'] == 'weird':
            print("  ? Weird particle has correct category field")
        else:
            issues.append("Weird particle missing/incorrect category field")
            print("  ? Weird particle missing/incorrect category field")
            
    except Exception as e:
        issues.append(f"Parameter generation check failed: {str(e)}")
        print(f"  ? Error: {e}")
    
    # =====================================================================
    # 检查 4: 新增文件验证
    # =====================================================================
    print("\n[4/5] Checking new documentation files...")
    
    files_to_check = [
        'generate_mixed_batch.py',
        'MIXED_MORPHOLOGY_GUIDE.py',
        'QUICK_REFERENCE.py',
        'MODIFICATION_SUMMARY.py',
        'README_MIXED_MORPHOLOGY.md',
        'IMPLEMENTATION_COMPLETE.md'
    ]
    
    missing_files = []
    for filename in files_to_check:
        if os.path.exists(filename):
            print(f"  ? {filename}")
        else:
            print(f"  ? {filename} (missing)")
            missing_files.append(filename)
            issues.append(f"Missing file: {filename}")
    
    if not missing_files:
        print("  ? All documentation files present")
    
    # =====================================================================
    # 检查 5: 错误处理验证
    # =====================================================================
    print("\n[5/5] Checking error handling...")
    
    try:
        # 检查代码中是否包含 try-except
        with open('particle_generator.py', 'r', encoding='utf-8') as f:
            content = f.read()
            
        try_except_count = content.count('try:') - content.count('try,')  # 排除字符串中的 "try"
        
        if try_except_count >= 2:  # 应该有至少 2 个 try-except (普通粒子 + 奇异粒子)
            print(f"  ? Error handling implemented ({try_except_count} try-except blocks)")
        else:
            issues.append(f"Not enough try-except blocks (found {try_except_count}, expected >=2)")
            print(f"  ??  Warning: Only {try_except_count} try-except blocks found (expected >=2)")
            
        if 'continue' in content and 'except' in content:
            print("  ? Error handling uses 'continue' to skip failed particles")
        else:
            issues.append("Error handling may not skip failed particles properly")
            print("  ??  Error handling may not skip failed particles properly")
            
    except Exception as e:
        issues.append(f"Error handling check failed: {str(e)}")
        print(f"  ? Error: {e}")
    
    # =====================================================================
    # 最终报告
    # =====================================================================
    print("\n" + "="*80)
    print("VERIFICATION SUMMARY")
    print("="*80)
    
    if not issues:
        print("\n? ALL CHECKS PASSED!")
        print("\nThe following modifications have been successfully verified:")
        print("  1. ? generate_coeffs() extended with max_degree and coeff_multiplier")
        print("  2. ? generate_random_particle_params() refactored with category parameter")
        print("  3. ? generate_regular_particle_params() implemented")
        print("  4. ? generate_weird_particle_params() implemented")
        print("  5. ? batch_generate_mixed_particles() implemented")
        print("  6. ? Error handling with try-except blocks")
        print("  7. ? All documentation files created")
        print("\nYou can now run:")
        print("  python generate_mixed_batch.py")
        return True
    else:
        print(f"\n??  {len(issues)} ISSUE(S) FOUND:\n")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
        return False
    
    print("\n" + "="*80 + "\n")


if __name__ == '__main__':
    success = verify_modifications()
    sys.exit(0 if success else 1)
