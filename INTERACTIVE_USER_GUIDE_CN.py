# -*- coding: utf-8 -*-
"""
交互式粒子生成系统 - 用户指南
INTERACTIVE PARTICLE GENERATION SYSTEM - USER GUIDE (中文版)

本文档介绍如何使用增强的、用户友好的SHPSG粒子生成脚本及其交互功能。
This document explains how to use the enhanced, user-friendly SHPSG particle
generation script with interactive features.
"""

# ============================================================================
# 1. 运行交互式脚本 / RUNNING THE INTERACTIVE SCRIPT
# ============================================================================

"""
基本用法 / BASIC USAGE:
    python run_competition_generation.py

脚本将逐步引导您完成整个过程。
The script will guide you through the process step by step.
"""


# ============================================================================
# 2. 欢迎标题和信息 / WELCOME HEADER & INFORMATION
# ============================================================================

"""
启动脚本时，您将看到：
When you start the script, you'll see:

    ================================================================================
                       SHPSG粒子生成工具 / SHPSG Particle Generation Tool
    ================================================================================

    时间戳 / Timestamp: 2026-01-21 16:37:33
    目标容器 / Target Container: 圆筒形（直径：1000微米）/ Cylindrical (Diameter: 1000 micrometers)

    目标 / Goals:
      - 生成30-90微米的不规则粒子
      - Generate irregular particles sized 30-90 micrometers
      - 通过形状、圆度和粗糙度控制粒子形态
      - Control particle morphology through Form, Roundness, and Roughness
      - 为堆积模拟创建逼真的粒子批次
      - Create realistic particle batch for packing simulation

该标题提供以下信息：
This header provides:
    - 当前日期和时间 / Current date and time
    - 目标容器规格 / Target container specifications
    - 粒子生成的总体目标 / Overall objectives for the particle generation
"""


# ============================================================================
# 3. 交互式输入阶段 / INTERACTIVE INPUT PHASE
# ============================================================================

"""
步骤1：粒子数量输入
STEP 1: Particle Quantity Input

    粒子批次配置 / Particle Batch Configuration:
    ────────────────────────────────────────────────────────────────────────────
    输入要生成的粒子数量（默认值：50）：
    Enter number of particles to generate (default: 50): 

操作 / Action:
    - 输入数字并按Enter键（例如，100）
    - Type a number and press Enter (e.g., 100)
    - 或直接按Enter键接受默认值（50）
    - Or just press Enter to accept the default (50)
    - 如果输入的数字> 500，系统将要求确认
    - If you enter a number > 500, system will ask for confirmation

示例 / Examples:
    - 输入：50 → 生成50个粒子
    - Input: 50 -> Generates 50 particles
    - 输入：（空白）→ 使用默认的50
    - Input: (blank) -> Uses default 50
    - 输入：1000 → 询问："继续？(y/n):"
    - Input: 1000 -> Asks: "Continue? (y/n):"

系统将验证输入并妥善处理错误。
The system validates input and handles errors gracefully.
"""


# ============================================================================
# 4. 参数配方显示 / RECIPE DISPLAY
# ============================================================================

"""
步骤2：当前参数配方
STEP 2: Current Parameter Recipe

    当前"配方" - 参数范围：
    Current 'Recipe' - Parameter Ranges:
    ────────────────────────────────────────────────────────────────────────────
    形状参数 / Form Parameters:
      - 拉伸比（Ei）/ Elongation Index (Ei):  [0.6, 1.0]  (球形到拉长 / spherical to elongated)
      - 扁度（Fi）/ Flatness Index (Fi):    [0.6, 1.0]  (扁平到球形 / oblate to spherical)

    形态参数 / Morphology Parameters:
      - 圆度/棱角度（D2_8）/ Roundness/Angularity (D2_8):  [0.00, 0.35]  (光滑到棱角 / smooth to angular)
      - 粗糙度（D9_15）/ Roughness (D9_15):             [0.00, 0.15]  (光滑到粗糙 / smooth to rough)

    尺寸参数 / Size Parameter:
      - 等效直径（D_eq）/ Equivalent Diameter (D_eq):    [30, 90] 微米 (均匀随机 / micrometers uniform random)

提供的信息 / Information Provided:
    - 每个形态特征的参数范围
    - Parameter ranges for each morphological feature
    - 每个参数的物理解释
    - Physical interpretation of each parameter
    - 每个参数如何影响粒子外观
    - How each parameter affects particle appearance
    - 所有值都在这些范围内为每个粒子随机选择
    - All values are randomly selected within these ranges for each particle

理解配方 / Understanding the Recipe:
    - Ei=1.0, Fi=1.0: 完美球形 / Perfectly spherical
    - Ei<0.8: 长球体（拉长）/ Prolate (elongated)
    - Fi<0.8: 扁球体（扁平）/ Oblate (flattened)
    - D2_8=0: 完美光滑的角 / Perfectly smooth corners
    - D2_8=0.35: 高度棱角的边缘 / Highly angular edges
    - D9_15=0: 光滑表面 / Smooth surface
    - D9_15=0.15: 粗糙的、不平的表面 / Rough, bumpy surface
"""


# ============================================================================
# 5. 实时进度报告 / REAL-TIME PROGRESS REPORTING
# ============================================================================

"""
步骤3：带进度的粒子生成
STEP 3: Particle Generation with Progress

    准备阶段 / Preparation Phase:
    ────────────────────────────────────────────────────────────────────────────
    正在生成基础网格几何...
    Generating base mesh geometry...
    >> 网格几何就绪（表面单元：320）
    >> Mesh geometry ready (Surface elements: 320)

    生成阶段 / Generation Phase:
    ────────────────────────────────────────────────────────────────────────────
    [============================--------------------] 58.0%

进度报告功能 / Features of Progress Reporting:

1. 进度条 / PROGRESS BAR:
   - 显示完成情况的可视化表示
   - Shows visual representation of completion
   - 在生成粒子时实时更新
   - Updates in real-time as particles are generated
   - 右侧显示百分比
   - Percentage display at the right

2. 详细信息（每10个粒子）/ DETAILED INFORMATION (every 10 particles):
   
   步骤 10/50: particle_0009.stl / Step 10/50: particle_0009.stl
     大小：65.4 um | 类型：扁球体 | 圆度：0.18 | 表面：中等粗糙
     Size: 65.4 um | Type: Oblate | Roundness: 0.18 | Surface: Moderately Rough

   信息包括 / Information includes:
   - 步骤计数器（X/总计）/ Step counter (X/Total)
   - 正在生成的文件名 / Filename being generated
   - 大小（微米）/ Size in micrometers
   - 粒子类型分类 / Particle type classification
   - 圆度/棱角值（D2_8）/ Roundness/Angularity value (D2_8)
   - 表面粗糙度描述 / Surface roughness description

3. 粒子类型分类 / PARTICLE TYPE CLASSIFICATION:
   - 球形 / Spherical: Ei >= 0.9 AND Fi >= 0.9
   - 长球体（拉长）/ Prolate: Ei < 0.8 AND Fi >= 0.85 (elongated)
   - 扁球体（扁平）/ Oblate: Ei >= 0.85 AND Fi < 0.8 (flattened)
   - 混合型 / Mixed: 所有其他组合 / All other combinations

4. 表面描述 / SURFACE DESCRIPTION:
   - 光滑 / Smooth: D9_15 < 0.05
   - 中等粗糙 / Moderately Rough: 0.05 <= D9_15 < 0.10
   - 非常粗糙 / Very Rough: D9_15 >= 0.10
"""


# ============================================================================
# 6. 错误处理 / ERROR HANDLING
# ============================================================================

"""
错误处理功能 / ERROR HANDLING FEATURES:

脚本包含try-except块以妥善处理故障。
The script includes try-except blocks to handle failures gracefully.

示例警告 / Example Warning:
    警告：未能生成粒子_5 / WARNING: Failed to generate particle_5
    错误：[Errno 13] 权限被拒绝 / Error: [Errno 13] Permission denied

发生错误时 / When an error occurs:
    1. 标识特定的粒子索引 / The specific particle index is identified
    2. 显示错误信息 / The error message is displayed
    3. 继续生成剩余粒子 / Generation continues with remaining particles
    4. 最终报告显示成功/失败统计 / Final report shows success/failure statistics

可能的错误 / Possible Errors:
    - 磁盘空间问题：设备上没有可用空间
    - Disk space issues: "No space left on device"
    - 权限问题：权限被拒绝
    - Permission problems: "Permission denied"
    - 无效目录：没有此类文件或目录
    - Invalid directory: "No such file or directory"
    - 内存问题：内存错误
    - Memory issues: "Memory error"

恢复 / Recovery:
    - 失败的粒子被分开跟踪 / Failed particles are tracked separately
    - 成功率被计算并显示 / Success rate is calculated and displayed
    - 元数据文件仍仅包含成功的粒子 / Metadata file still contains only successful particles
"""


# ============================================================================
# 7. 工作总结报告 / WORK SUMMARY REPORT
# ============================================================================

"""
最终输出：综合总结报告
FINAL OUTPUT: Comprehensive Summary Report

    ================================================================================
                          工作总结报告 / Work Summary Report
    ================================================================================

    生成结果 / Generation Results:
    ────────────────────────────────────────────────────────────────────────────
      创建的总粒子数 / Total particles created:  50
      成功率 / Success rate:             100.0%

    批次统计 / Batch Statistics:
    ────────────────────────────────────────────────────────────────────────────
      平均粒子大小 / Average particle size:    62.34 微米 / micrometers
      大小范围 / Size range:               30.12 - 89.87 微米 / micrometers
      平均拉伸比（Ei）/ Average elongation (Ei):  0.814
      平均扁度（Fi）/ Average flatness (Fi):    0.795
      平均棱角度 / Average angularity:       0.168
      平均粗糙度 / Average roughness:        0.072

    文件存储 / File Storage:
    ────────────────────────────────────────────────────────────────────────────
      位置 / Location: ./data/competition_particles
      STL文件（3D模型）/ STL files (3D models):    ./data/competition_particles/*.stl (50个文件 / files)
      PNG可视化 / PNG visualizations:       ./data/competition_particles/*.png (50个文件 / files)
      元数据文件 / Metadata file:            ./data/competition_particles/metadata.txt

    下一步 / Next Steps:
    ────────────────────────────────────────────────────────────────────────────
      1. 您现在可以使用这些STL文件进行随机堆积模拟（问题1.2）
      1. You can now use these STL files for the random packing simulation (Problem 1.2)
      2. 将STL文件导入DEM模拟软件
      2. Import STL files into DEM simulation software
      3. 分析堆积效率和粒子相互作用
      3. Analyze packing efficiency and particle interactions
      4. 使用metadata.txt进行批次文档记录
      4. Use metadata.txt for batch documentation

总结信息包括 / Summary Information Includes:

1. 生成结果 / GENERATION RESULTS:
   - 成功创建的总粒子数 / Total particles successfully created
   - 失败粒子数（如果有） / Number of failed particles (if any)
   - 成功率百分比 / Success rate percentage

2. 批次统计 / BATCH STATISTICS:
   - 平均粒子大小和范围 / Mean particle size and range
   - 所有形态参数的平均值 / Average values for all morphological parameters
   - 质量评估的分布信息 / Distribution information for quality assessment

3. 文件存储 / FILE STORAGE:
   - 保存文件的目录 / Directory where files are saved
   - STL文件数（3D模型） / Number of STL files (3D models)
   - PNG文件数（可视化） / Number of PNG files (visualizations)
   - 文档的元数据文件位置 / Metadata file location for documentation

4. 下一步 / NEXT STEPS:
   - 在模拟中使用粒子的指导 / Guidance for using particles in simulations
   - 竞赛推荐工作流程 / Recommended workflow for competition
   - 与外部软件集成的建议 / Integration suggestions with external software
"""


# ============================================================================
# 8. 输出文件结构 / OUTPUT FILE STRUCTURE
# ============================================================================

"""
生成的文件 / FILES GENERATED:

./data/competition_particles/
├── particle_0000.stl        (3D模型 - 30-90微米 / 3D model - 30-90 micrometers)
├── particle_0000.png        (可视化 - 自动缩放 / Visualization - automatically scaled)
├── particle_0001.stl
├── particle_0001.png
├── ...
├── particle_0049.stl
├── particle_0049.png
└── metadata.txt             (统计和属性 / Statistics and attributes)

总计：50个STL + 50个PNG + 1个元数据 = 101个文件
Total: 50 STL + 50 PNG + 1 metadata = 101 files


元数据文件格式 / METADATA FILE FORMAT:

粒子生成元数据 / Particle Generation Metadata
================================================================================

总粒子数 / Total particles: 50
D_eq范围（微米）/ D_eq range (um): 30.45 - 89.87
Ei范围 / Ei range: 0.601 - 0.998
Fi范围 / Fi range: 0.602 - 0.997
D2_8范围 / D2_8 range: 0.001 - 0.349
D9_15范围 / D9_15 range: 0.003 - 0.149

================================================================================

个体粒子数据 / Individual Particle Data:
================================================================================
索引   D_eq(微米) Ei       Fi       D2_8     D9_15
Index  D_eq(um)   Ei       Fi       D2_8     D9_15   
────────────────────────────────────────────────────────────────────────────
0      45.23      0.812    0.654    0.156    0.043   
1      67.89      0.945    0.723    0.012    0.098   
...
49     52.34      0.678    0.891    0.287    0.014   


STL文件格式 / STL FILE FORMAT:
    - 二进制STL格式（工业标准）/ Binary STL format (industry standard)
    - 包含粒子的完整3D几何结构 / Contains full 3D geometry of particle
    - 兼容于 / Compatible with:
        * CAD软件（Blender、FreeCAD、SolidWorks）
        * CAD software (Blender, FreeCAD, SolidWorks)
        * DEM模拟软件 / DEM simulation software
        * 3D可视化工具 / 3D visualization tools
        * 3D打印软件 / 3D printing software

PNG文件格式 / PNG FILE FORMAT:
    - 粒子的3D可视化 / 3D visualization of particle
    - 根据粒子大小自动缩放 / Automatically scaled based on particle size
    - 显示线框和阴影表面 / Shows wireframe and shaded surfaces
    - 对于快速视觉检查很有用 / Useful for quick visual inspection
"""


# ============================================================================
# 9. 工作流示例 / EXAMPLE WORKFLOW
# ============================================================================

"""
完整工作流示例 / COMPLETE WORKFLOW EXAMPLE:

步骤1：启动脚本
Step 1: Launch the script
    $ python run_competition_generation.py

步骤2：查看欢迎标题
Step 2: See the welcome header
    [显示时间戳、容器信息、目标]
    [Displays timestamp, container info, goals]

步骤3：输入粒子数量
Step 3: Enter particle count
    输入要生成的粒子数量（默认值：50）：100
    Enter number of particles to generate (default: 50): 100
    >> 已确认：生成100个粒子
    >> Confirmed: Generating 100 particles

步骤4：查看配方
Step 4: Review the recipe
    [显示所有参数范围]
    [Shows all parameter ranges]

步骤5：观察实时进度
Step 5: Watch real-time progress
    [每10个粒子的进度条和详细信息]
    [Progress bar and detailed info for every 10 particles]
    [生成STL和PNG文件]
    [Generates STL and PNG files]

步骤6：查看总结
Step 6: Review the summary
    [显示统计和成功率]
    [Shows statistics and success rate]
    [确认文件位置]
    [Confirms file locations]
    [提供下一步]
    [Provides next steps]

步骤7：使用生成的粒子
Step 7: Use the generated particles
    - 将STL文件导入DEM软件
    - Import STL files into DEM software
    - 使用metadata.txt作为初始条件
    - Use metadata.txt for initial conditions
    - 在模拟中分析结果
    - Analyze results in simulation
"""


# ============================================================================
# 10. 提示和故障排除 / TIPS AND TROUBLESHOOTING
# ============================================================================

"""
最佳使用提示 / TIPS FOR OPTIMAL USE:

1. 批次大小选择 / BATCH SIZE SELECTION:
   - 从10-20开始进行快速测试
   - Start with 10-20 for quick testing
   - 使用50-100进行逼真堆积模拟
   - Use 50-100 for realistic packing simulations
   - 避免>500，除非有时间和磁盘空间
   - Avoid >500 unless you have time and disk space

2. 生成时间 / GENERATION TIME:
   - 每个粒子：~2-3秒（含PNG）
   - Each particle: ~2-3 seconds (with PNG)
   - 50个粒子：~2-3分钟
   - 50 particles: ~2-3 minutes
   - 100个粒子：~4-6分钟
   - 100 particles: ~4-6 minutes
   - 可通过代码修改禁用PNG以加快生成
   - Can disable PNG with code modification for faster generation

3. 磁盘空间 / DISK SPACE:
   - 每个粒子：~300-400 KB（STL + PNG）
   - Each particle: ~300-400 KB (STL + PNG)
   - 50个粒子：~20 MB
   - 50 particles: ~20 MB
   - 100个粒子：~40 MB
   - 100 particles: ~40 MB
   - 确保./data/文件夹中有足够的磁盘空间
   - Ensure adequate disk space in ./data/ folder

4. 验证结果 / VERIFYING RESULTS:
   - 检查文件计数：应为2*N + 1（N个粒子，N个PNG，1个元数据）
   - Check file count: should be 2*N + 1 (N particles, N PNGs, 1 metadata)
   - 打开PNG文件以直观检查粒子
   - Open PNG files to visually inspect particles
   - 查看metadata.txt的统计摘要
   - Review metadata.txt for statistical summary
   - 将示例STL导入CAD软件以验证几何
   - Import sample STL into CAD software to verify geometry


故障排除 / TROUBLESHOOTING:

问题1：保存文件时出现"没有此类文件或目录"
Issue: "No such file or directory" when saving files
解决方案：确保./data/文件夹存在，或手动创建它
Solution: Ensure ./data/ folder exists, or create it manually
    mkdir -p ./data/competition_particles

问题2：脚本运行非常缓慢
Issue: Script runs very slowly
解决方案 / Solution:
    - 检查磁盘空间可用性 / Check disk space availability
    - 必要时减少批次大小 / Reduce batch size if necessary
    - 在高级使用中禁用PNG生成 / Disable PNG generation in advanced usage

问题3：生成的粒子看起来不正确
Issue: Generated particles look incorrect
解决方案 / Solution:
    - 验证STL文件在3D查看器中正确打开 / Verify STL file is opened correctly in 3D viewer
    - 检查D_eq缩放是否正确应用 / Check if D_eq scaling is applied correctly
    - 确保matplotlib后端配置正确 / Ensure matplotlib backend is configured properly

问题4：元数据文件为空或不完整
Issue: Metadata file is empty or incomplete
解决方案 / Solution:
    - 检查文件夹权限 / Check folder permissions
    - 确保磁盘具有写入权限 / Ensure disk has write access
    - 验证metadata.txt路径是否正确 / Verify metadata.txt path is correct
"""


# ============================================================================
# 11. 高级自定义 / ADVANCED CUSTOMIZATION
# ============================================================================

"""
修改参数范围 / MODIFYING PARAMETER RANGES:

要将粒子大小范围从[30, 90]更改为[40, 80]：
To change the particle size range from [30, 90] to [40, 80]:

1. 编辑particle_generator.py / Edit particle_generator.py
2. 找到generate_random_particle_params()函数 / Find generate_random_particle_params() function
3. 更改：'D_eq': np.random.uniform(30, 90)
   改为：'D_eq': np.random.uniform(40, 80)
   Change: 'D_eq': np.random.uniform(30, 90)
   To:      'D_eq': np.random.uniform(40, 80)


要更改棱角度范围 / To change angularity range:

   更改：'D2_8': np.random.uniform(0.0, 0.35)
   改为：'D2_8': np.random.uniform(0.1, 0.25)
   Change: 'D2_8': np.random.uniform(0.0, 0.35)
   To:      'D2_8': np.random.uniform(0.1, 0.25)


禁用PNG生成（更快） / To disable PNG generation (faster):

1. 编辑run_competition_generation.py / Edit run_competition_generation.py
2. 更改：include_png=True
   改为：include_png=False
   Change: include_png=True
   To:      include_png=False


可重现的结果 / REPRODUCIBLE RESULTS:

要生成相同的批次两次 / To generate the same batch twice:

1. 添加到main()的开始处：/ Add at the start of main():
   import numpy as np
   np.random.seed(42)

2. 这使随机生成具有确定性 / This makes random generation deterministic
3. 使用相同种子的所有运行都会生成相同的粒子 / All runs with same seed produce identical particles
"""


# ============================================================================
# 12. 与竞赛问题的集成 / INTEGRATION WITH COMPETITION PROBLEM
# ============================================================================

"""
如何用于竞赛问题1.2（堆积模拟） / HOW TO USE FOR COMPETITION PROBLEM 1.2 (Packing Simulation):

1. 生成粒子 / GENERATE PARTICLES:
   python run_competition_generation.py
   [为模拟选择合适的批次大小]
   [Select appropriate batch size for your simulation]

2. 验证文件 / VERIFY FILES:
   - 检查./data/competition_particles/中的STL文件
   - Check ./data/competition_particles/ for STL files
   - 查看metadata.txt以了解粒子特性
   - Review metadata.txt for particle properties
   - 打开示例PNG以验证几何
   - Open a sample PNG to verify geometry

3. 导入DEM软件 / IMPORT INTO DEM SOFTWARE:
   - 大多数DEM软件接受STL格式
   - Most DEM software accepts STL format
   - 加载metadata.txt以获取初始粒子属性
   - Load metadata.txt for initial particle attributes
   - 将模拟容器设置为1000微米直径圆筒
   - Set simulation container to 1000 um diameter cylinder

4. 运行模拟 / RUN SIMULATION:
   - 执行随机堆积模拟
   - Execute random packing simulation
   - 监控堆积效率
   - Monitor packing efficiency
   - 分析粒子相互作用
   - Analyze particle interactions

5. 收集结果 / COLLECT RESULTS:
   - 导出最终堆积配置
   - Export final packing configuration
   - 记录统计数据
   - Document statistics
   - 与理论预测进行比较
   - Compare with theoretical predictions

生成的粒子提供适合精确颗粒材料模拟的逼真不规则几何。
The generated particles provide realistic irregular geometry suitable for
accurate granular material simulations.
"""
