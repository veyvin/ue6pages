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

ry for linear algebra, matrices, vectors, numerical solvers, and related algorithms. While Unreal provides its own math types (like FVector and FMatrix), Eigen is used for high-dimensional data, complex decompositions (LU, QR, SVD), and sophisticated optimization problems that go beyond standard game-engine geometry. In UE5, it is a critical dependency for systems like Control Rig, FullBody IK, and Physics/Chaos solvers.

Practical Usage Tips & Best Practices
1. Use THIRD_PARTY_INCLUDES for Header Safety

Eigen is a standalone library and doesn’t follow Unreal’s strict macro and warning standards. Including it directly can trigger “Shadow Variable” or “Undefined Macro” errors.

Best Practice: Always wrap your Eigen includes with the third-party guard macros to isolate the compiler environment.
C++
	THIRD_PARTY_INCLUDES_START

	#include <Eigen/Dense>

	#include <Eigen/Core>

	THIRD_PARTY_INCLUDES_END

	```

	This ensures the **elimination** of hundreds of noise warnings that would otherwise prevent your code from compiling under the `TreatWarningsAsErrors` policy.

	 

	#### 2. Handle 16-Byte Alignment Requirements

	Fixed-size Eigen types (like `Eigen::Vector4f` or `Eigen::Matrix4f`) require 16-byte alignment for SIMD optimization. If these are members of a class, you must ensure the class is correctly aligned.

	*   **Tip:** Use the `EIGEN_MAKE_ALIGNED_OPERATOR_NEW` macro in the public section of any class or struct that contains fixed-size Eigen members. This facilitates the **elimination** of random "Access Violation" crashes that occur when the heap allocator provides an unaligned memory address.

	 

	#### 3. Prefer "Dynamic" Matrices for UObjects

	Unreal’s garbage collector and `TArray` do not natively guarantee Eigen’s 16-byte alignment requirements for fixed-size members.

	*   **Best Practice:** When storing Eigen data in `UCLASS` or `USTRUCT` properties, use dynamic-size types like `Eigen::MatrixXf` instead of fixed ones. Dynamic matrices allocate their data on the heap (where Eigen can control alignment), leading to the **elimination** of complex memory-alignment bugs in reflected types.

	 

	#### 4. Map Unreal Types to Eigen (Zero-Copy)

	You can operate on `FVector` or `TArray` data using Eigen logic without copying the memory by using `Eigen::Map`.

	*   **Tip:** Use `Eigen::Map<Eigen::Vector3f>` to wrap an `FVector`'s data pointer.

	```cpp

	FVector MyUEVec(1, 2, 3);

	Eigen::Map<Eigen::Vector3f> EigenVec(&MyUEVec.X);

	// Operations on EigenVec now affect MyUEVec directly

	```

	This allows for the **elimination** of expensive memory allocations when passing data between Unreal's physics state and Eigen's solvers.

	 

	#### 5. Restrict to Private Module Dependencies

	Eigen is a header-only library, but in Unreal, it is organized as a module. You should keep its footprint small.

	*   **Best Practice:** Add `"Eigen"` to your `PrivateDependencyModuleNames` in your `*.Build.cs` file rather than Public. This prevents every other module that depends on yours from also having the Eigen include paths in their search space, resulting in the **elimination** of "Header Pollution" and keeping compile times lower.

	 

	#### 6. Beware of Namespace Conflicts

	Eigen uses the `Eigen` namespace, but it also defines several common terms. 

	*   **Tip:** Never use `using namespace Eigen;` in a header file. Always use the explicit `Eigen::` prefix. This is critical for the **elimination** of name collisions with Unreal's math library or other third-party integrations that might use similar terminology (like `Matrix` or `Vector`).

	 

	#### 7. Define EIGEN_MPL2_ONLY for Licensing Safety

	Depending on your project's legal requirements, you may need to ensure you aren't accidentally using code covered by more restrictive licenses (like LGPL/GPL) found in some Eigen sub-modules.

	*   **Best Practice:** Add `PublicDefinitions.Add("EIGEN_MPL2_ONLY");` to your `Build.cs`. This forces Eigen to only enable code under the MPL2 license, facilitating the **elimination** of legal risks when shipping your commercial application.

	 

	#### 8. Use for Large-Scale Linear Solvers

	Don't use Eigen for simple 3D math; Unreal’s `FVector` and `FMath` are already highly optimized and SIMD-accelerated for game-specific tasks.

	*   **Tip:** Reserve Eigen for tasks involving massive matrices (e.g., a 100x100 matrix for a cloth simulation or a least-squares fit for animation data). Using Eigen only where its advanced solvers are needed ensures the **elimination** of unnecessary complexity in your standard gameplay code.
Copy code

This ensures the elimination of hundreds of noise warnings that would otherwise prevent your code from compiling under the TreatWarningsAsErrors policy.

2. Handle 16-Byte Alignment Requirements

Fixed-size Eigen types (like Eigen::Vector4f or Eigen::Matrix4f) require 16-byte alignment for SIMD optimization. If these are members of a class, you must ensure the class is correctly aligned.

Tip: Use the EIGEN_MAKE_ALIGNED_OPERATOR_NEW macro in the public section of any class or struct that contains fixed-size Eigen members. This facilitates the elimination of random “Access Violation” crashes that occur when the heap allocator provides an unaligned memory address.
3. Prefer “Dynamic” Matrices for UObjects

Unreal’s garbage collector and TArray do not natively guarantee Eigen’s 16-byte alignment requirements for fixed-size members.

Best Practice: When storing Eigen data in UCLASS or USTRUCT properties, use dynamic-size types like Eigen::MatrixXf instead of fixed ones. Dynamic matrices allocate their data on the heap (where Eigen can control alignment), leading to the elimination of complex memory-alignment bugs in reflected types.
4. Map Unreal Types to Eigen (Zero-Copy)

You can operate on FVector or TArray data using Eigen logic without copying the memory by using Eigen::Map.

Tip: Use Eigen::Map<Eigen::Vector3f> to wrap an FVector’s data pointer.
C++
	FVector MyUEVec(1, 2, 3);

	Eigen::Map<Eigen::Vector3f> EigenVec(&MyUEVec.X);

	// Operations on EigenVec now affect MyUEVec directly
Copy code

This allows for the elimination of expensive memory allocations when passing data between Unreal’s physics state and Eigen’s solvers.

5. Restrict to Private Module Dependencies

Eigen is a header-only library, but in Unreal, it is organized as a module. You should keep its footprint small.

Best Practice: Add "Eigen" to your PrivateDependencyModuleNames in your *.Build.cs file rather than Public. This prevents every other module that depends on yours from also having the Eigen include paths in their search space, resulting in the elimination of “Header Pollution” and keeping compile times lower.
6. Beware of Namespace Conflicts

Eigen uses the Eigen namespace, but it also defines several common terms.

Tip: Never use using namespace Eigen; in a header file. Always use the explicit Eigen:: prefix. This is critical for the elimination of name collisions with Unreal’s math library or other third-party integrations that might use similar terminology (like Matrix or Vector).
7. Define EIGEN_MPL2_ONLY for Licensing Safety

Depending on your project’s legal requirements, you may need to ensure you aren’t accidentally using code covered by more restrictive licenses (like LGPL/GPL) found in some Eigen sub-modules.

Best Practice: Add PublicDefinitions.Add("EIGEN_MPL2_ONLY"); to your Build.cs. This forces Eigen to only enable code under the MPL2 license, facilitating the elimination of legal risks when shipping your commercial application.
8. Use for Large-Scale Linear Solvers

Don’t use Eigen for simple 3D math; Unreal’s FVector and FMath are already highly optimized and SIMD-accelerated for game-specific tasks.

Tip: Reserve Eigen for tasks involving massive matrices (e.g., a 100x100 matrix for a cloth simulation or a least-squares fit for animation data). Using Eigen only where its advanced solvers are needed ensures the elimination of unnecessary complexity in your standard gameplay code.