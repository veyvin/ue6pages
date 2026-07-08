---
layout: default
title: Eigen
---

<!-- ai-generation-failed -->

<h1>Eigen</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Eigen/Eigen.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

+ template library for linear algebra.

Description

Eigen is a specialized library used for complex mathematical operations involving matrices, vectors, numerical solvers, and related algorithms. While Unreal Engine has its own math library (FVector, FMatrix, FQuat), Eigen is included to handle advanced computations that require high performance and precision beyond standard gameplay math. It is heavily utilized by engine subsystems like Control Rig, Chaos Physics, Animation Retargeting, and Procedural Mesh generation, where solving large systems of linear equations or performing Singular Value Decomposition (SVD) is required.

Practical Usage Tips and Best Practices
1. Include the Module in Build.cs

To use Eigen in your custom C++ code, you must first add it as a dependency in your module’s Build.cs file. Because it is a third-party library, it is added to the PublicDependencyModuleNames:

C#
PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "Eigen" });
Copy code

This ensures the Unreal Build Tool (UBT) correctly adds the Eigen include paths to your project.

2. Wrap Includes with Third-Party Macros

Eigen is an external library that does not follow Unreal’s coding standards (e.g., it uses standard C++ headers and different warning levels). To prevent compiler warnings from breaking your build, always wrap your Eigen includes with these macros:

C++
	THIRD_PARTY_INCLUDES_START

	#include <Eigen/Dense>

	#include <Eigen/SVD>

	THIRD_PARTY_INCLUDES_END
Copy code
3. Use Eigen::Map for Data Conversion

Avoid copying large amounts of data between Unreal types (TArray) and Eigen types. Use Eigen::Map to wrap existing memory. This allows Eigen to perform operations directly on the memory allocated by an Unreal TArray<float>, resulting in the elimination of redundant allocation and copying overhead.

4. Manage Alignment and SIMD

Eigen is highly optimized for SIMD (Single Instruction, Multiple Data) instructions. However, this requires data to be 16-byte aligned. When using Eigen types as members of Unreal UCLASS or USTRUCT objects, use EIGEN_MAKE_ALIGNED_OPERATOR_NEW to ensure the memory is correctly aligned, or use the Eigen::DontAlign flag for small fixed-size matrices.

5. Prioritize Eigen for Complex Solvers

If your logic requires finding eigenvalues, performing least-squares fitting, or solving sparse matrices, use Eigen instead of trying to implement these in standard Unreal math. Eigen’s solvers are mathematically robust and significantly faster than naive implementations, leading to the elimination of precision errors in simulation code.

6. Avoid Namespace Pollution

Eigen uses the Eigen namespace. Do not use using namespace Eigen; in header files, as this can cause naming collisions with Unreal’s own math types (like Vector). Instead, use explicit scoping (e.g., Eigen::Vector3f) or create specific using declarations within your .cpp function scopes.

7. Profile with Unreal Insights

When performing heavy matrix math, use Unreal Insights to monitor the CPU cost. If Eigen operations are taking too long, check if you are accidentally using “dynamic” matrices (MatrixXd) where “fixed-size” matrices (Matrix3d) would suffice. Fixed-size operations allow the compiler to perform more aggressive optimizations.

8. Handle Memory Elimination in Loops

When performing iterative calculations (like an IK solver), pre-allocate your Eigen matrices outside the loop. Repeatedly creating and destroying large Eigen matrices inside a high-frequency loop (like Tick) will cause heap fragmentation. The elimination of temporary matrix allocations is key to maintaining a stable 60Hz or 120Hz framerate.