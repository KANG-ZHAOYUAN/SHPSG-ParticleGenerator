# -*- coding: utf-8 -*-
"""
QUICK REFERENCE - 代码修改速查表
SHPSG Mixed Morphology Batch Generation Quick Reference
"""

# ============================================================================
# 方式 1: 最简单的使用方式 (3 行代码)
# ============================================================================

"""
from particle_generator import batch_generate_mixed_particles, save_particle_metadata

particles = batch_generate_mixed_particles()
save_particle_metadata(particles, './Output_Batch/metadata.txt')
"""

# ============================================================================
# 方式 2: 修改参数的使用方式
# ============================================================================

"""
from particle_generator import batch_generate_mixed_particles, save_particle_metadata

# 生成 50 个普通 + 50 个奇异粒子
particles = batch_generate_mixed_particles(
    output_dir='./Custom_Batch',
    regular_count=50,    # 改成 50 代替默认的 40
    weird_count=50,      # 改成 50 代替默认的 10
    include_png=True,
    verbose=True
)

save_particle_metadata(particles, './Custom_Batch/metadata.txt')
"""

# ============================================================================
# 方式 3: 命令行运行
# ============================================================================

"""
# 直接运行生成脚本
python generate_mixed_batch.py

# 或直接运行 particle_generator.py
python particle_generator.py
"""

# ============================================================================
# 关键参数对比
# ============================================================================

"""
                    普通粒子 (Regular)        奇异粒子 (Weird)
───────────────────────────────────────────────────────────────
Ei 拉长指数          0.8 - 1.0              0.2 - 0.5
Fi 扁平指数          0.7 - 0.95             0.1 - 0.4
D2_8 棱角度         0.0 - 0.3              0.2 - 0.4
D9_15 粗糙度        0.0 - 0.1              0.1 - 0.2
SH 度数 (L)         8 - 12                 30 - 50
系数放大 (mult)     1.0x                   5.0 - 10.0x
数量                40 (80%)               10 (20%)
形状                岩石般、现实            尖刺/深凹、极端
───────────────────────────────────────────────────────────────
"""

# ============================================================================
# 核心代码片段
# ============================================================================

"""
========================================================================
1. 生成普通粒子参数
========================================================================

from particle_generator import generate_regular_particle_params

params = generate_regular_particle_params()
print("生成的参数:")
print("  Ei (拉长):", params['Ei'])          # 0.8-1.0
print("  Fi (扁平):", params['Fi'])          # 0.7-0.95
print("  D2_8 (棱角):", params['D2_8'])      # 0.0-0.3
print("  D9_15 (粗糙):", params['D9_15'])    # 0.0-0.1
print("  Max Degree:", params['max_degree'])  # 8-12
print("  Multiplier:", params['coeff_multiplier']) # 1.0


========================================================================
2. 生成奇异粒子参数
========================================================================

from particle_generator import generate_weird_particle_params

params = generate_weird_particle_params()
print("生成的参数:")
print("  Ei (拉长):", params['Ei'])          # 0.2-0.5 (极端拉长)
print("  Fi (扁平):", params['Fi'])          # 0.1-0.4 (极端扁平)
print("  D2_8 (棱角):", params['D2_8'])      # 0.2-0.4 (高棱角)
print("  D9_15 (粗糙):", params['D9_15'])    # 0.1-0.2 (高粗糙)
print("  Max Degree:", params['max_degree'])  # 30-50 (高频特征)
print("  Multiplier:", params['coeff_multiplier']) # 5-10x (系数放大)


========================================================================
3. 生成 SH 系数（通用函数）
========================================================================

from particle_generator import generate_coeffs

# 普通粒子系数
coeff_regular = generate_coeffs(
    Ei=0.9,                    # 长宽比
    Fi=0.8,                    # 扁平比
    D2_8=0.2,                  # 棱角度
    D9_15=0.05,                # 粗糙度
    max_degree=12,             # SH 度数 (通常用默认 16)
    coeff_multiplier=1.0       # 普通粒子用 1.0
)

# 奇异粒子系数
coeff_weird = generate_coeffs(
    Ei=0.3,                    # 高度拉长
    Fi=0.2,                    # 高度扁平
    D2_8=0.35,                 # 高棱角
    D9_15=0.15,                # 高粗糙
    max_degree=40,             # 高频 SH 度数
    coeff_multiplier=7.5       # 系数放大 7.5 倍
)


========================================================================
4. 批量生成全流程示例
========================================================================

from particle_generator import batch_generate_mixed_particles, save_particle_metadata

# Step 1: 生成 50 个粒子 (40 普通 + 10 奇异)
print("生成粒子中...")
particles = batch_generate_mixed_particles(
    output_dir='./Output_Batch',
    regular_count=40,
    weird_count=10,
    include_png=True,
    verbose=True
)

# Step 2: 保存元数据
print("保存元数据...")
save_particle_metadata(particles, './Output_Batch/metadata.txt')

# Step 3: 检查结果
print("\\n生成统计:")
regular = [p for p in particles if p['category'] == 'regular']
weird = [p for p in particles if p['category'] == 'weird']
print(f"  普通粒子: {len(regular)}")
print(f"  奇异粒子: {len(weird)}")
print(f"  总数: {len(particles)}")
"""

# ============================================================================
# 文件结构
# ============================================================================

"""
修改/新增的文件:

1. particle_generator.py (已修改)
   - 更新了 generate_coeffs()
   - 重构了 generate_random_particle_params()
   - 新增 generate_regular_particle_params()
   - 新增 generate_weird_particle_params()
   - 新增 batch_generate_mixed_particles()
   - 增强了 save_particle_metadata()

2. generate_mixed_batch.py (新文件)
   - 专用的混合批次生成脚本
   - 即插即用，推荐运行此文件

3. MIXED_MORPHOLOGY_GUIDE.py (新文件)
   - 详细的技术文档
   - 参数范围对比
   - 工作流程图
   - 代码示例

输出结构:
./Output_Batch/
├── particle_reg_01.stl      # 普通粒子 1
├── particle_reg_01.png      # 可视化
├── particle_reg_02.stl      # 普通粒子 2
├── ...
├── particle_reg_40.stl      # 普通粒子 40
├── particle_weird_01.stl    # 奇异粒子 1
├── particle_weird_01.png    # 可视化
├── ...
├── particle_weird_10.stl    # 奇异粒子 10
└── metadata.txt             # 统计数据
"""

# ============================================================================
# 常见问题 FAQ
# ============================================================================

"""
Q1: 如何运行生成脚本？
A1: 三种方式任选其一
   python generate_mixed_batch.py
   python particle_generator.py
   python -c "from particle_generator import batch_generate_mixed_particles; batch_generate_mixed_particles()"

Q2: 如何修改普通和奇异粒子的数量比例？
A2: 修改 batch_generate_mixed_particles() 的参数
   particles = batch_generate_mixed_particles(
       regular_count=30,    # 改为你想要的数字
       weird_count=20,      # 改为你想要的数字
   )

Q3: 如何不生成 PNG，加快速度？
A3: 设置 include_png=False
   particles = batch_generate_mixed_particles(
       include_png=False,   # 禁用 PNG 生成
   )

Q4: 生成过程中出错怎么办？
A4: 脚本已内置 try-except 块，会自动跳过失败的粒子并继续
   如果某个粒子失败，console 会打印错误信息，但不会中断整个批处理

Q5: 如何自定义参数范围？
A5: 编辑 generate_regular_particle_params() 或 generate_weird_particle_params()
   或在调用前手动修改参数字典

Q6: STL 文件能转换为 OBJ 格式吗？
A6: 是的，代码预留了 obj_filename 字段
   可使用第三方工具（如 Meshmixer、Blender）或添加转换代码

Q7: 如何导出为 OBJ 格式？
A7: 修改 sh2stl() 函数或使用 trimesh 库的 export 功能
   import trimesh
   mesh = trimesh.load('particle.stl')
   mesh.export('particle.obj')
"""

if __name__ == '__main__':
    print(__doc__)
