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

plate library, a high-performance linear algebra library specializing in matrices, vectors, numerical solvers, and related mathematical algorithms.

Description and Purpose

While Unreal Engine features its own math library (FVector, FMatrix), those types are primarily optimized for 3D/4D transformations and real-time gameplay logic. The Eigen module is used when the engine requires more complex mathematical operations—such as solving large sparse linear systems, performing Singular Value Decomposition (SVD), or handling high-dimensional matrix math. It is a critical dependency for advanced UE5 features like Motion Matching, Control Rig, and Chaos Physics, where numerical stability and optimization for complex solvers are required.

Practical Usage Tips and Best Practices
Protect Against Macro Collisions
Eigen and Unreal Engine (specifically on Windows) often have naming conflicts with macros like check, MIN, or MAX. To eliminate compilation errors, always wrap your Eigen includes with the engine’s third-party protection headers:
C#
	    PublicDependencyModuleNames.Add("Eigen");

	    ```

	    This ensures the Unreal Build Tool (UBT) adds the correct header paths from `Engine/Source/ThirdParty/Eigen`.

	 

	*   **Protect Against Macro Collisions**  

	    Eigen and Unreal Engine occasionally have macro naming conflicts (e.g., `check`, `PF_MAX`, or Windows-specific macros). Always wrap Eigen includes in the engine's third-party protection macros to **eliminate** compilation errors:

	    ```cpp

	    THIRD_PARTY_INCLUDES_START

	    #include <Eigen/Core>

	    #include <Eigen/Dense>

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	*   **Use Eigen::Map for Zero-Copy Conversion**  

	    Avoid manually looping through arrays to convert `TArray<float>` or `FVector` to Eigen types. Use `Eigen::Map` to wrap existing Unreal memory. This allows Eigen to operate directly on Unreal's data, which helps **eliminate** unnecessary memory allocations and copy overhead:

	    ```cpp

	    FVector UEPos(100.f, 200.f, 300.f);

	    Eigen::Map<Eigen::Vector3f> EigenPos(&UEPos.X);

	    ```

	 

	*   **Leverage for High-Dimensional Math**  

	    Unreal’s `FMatrix` is strictly 4x4. If you are implementing a custom procedural animation system or a machine learning inference pass that requires a 10x10 or dynamic matrix, use `Eigen::MatrixXf`. This allows you to **eliminate** the complexity of writing custom solvers for high-dimensional data.

	 

	*   **Be Mindful of Memory Alignment**  

	    Eigen often uses SIMD instructions that require 16-byte or 32-byte alignment. When nesting Eigen types inside Unreal `USTRUCT` or `UCLASS` types, use the `EIGEN_MAKE_ALIGNED_OPERATOR_NEW` macro. Failing to do this can lead to hard-to-debug crashes (Access Violations) during object instantiation.

	 

	*   **Prefer Row-Major for Unreal Compatibility**  

	    By default, Eigen uses Column-Major storage, while many developers expect Row-Major or need to interface with specific data structures. You can define your matrices as `Eigen::Matrix<float, 4, 4, Eigen::RowMajor>` to better align with Unreal’s internal `FMatrix` memory layout and **eliminate** transposition logic.

	 

	*   **Use for Solving Optimization Problems**  

	    If you need to implement a Least-Squares fit for a character's foot placement or a complex Inverse Kinematics (IK) solver, use Eigen’s built-in solvers (like `JacobiSVD` or `ColPivHouseholderQR`). These are highly optimized and will **eliminate** the need for you to implement complex numerical recipes from scratch.

	 

	*   **Strictly Editor or Tooling Use**  

	    Unless your gameplay specifically requires complex runtime math (like a real-time physics solver), keep Eigen usage within Editor modules or specialized plugins. This keeps your runtime game executable smaller and helps **eliminate** the risk of unintended performance spikes on low-end mobile or console hardware.
Copy code
Use Eigen::Map for Zero-Copy Data Handling
Instead of manually copying data between TArray and Eigen matrices, use Eigen::Map. This allows Eigen to perform operations directly on the existing memory of an Unreal array, which helps eliminate unnecessary memory allocations and CPU overhead:
C#
	    PublicDependencyModuleNames.Add("Eigen");

	    ```

	    This ensures the Unreal Build Tool (UBT) adds the correct header paths from `Engine/Source/ThirdParty/Eigen`.

	 

	*   **Protect Against Macro Collisions**  

	    Eigen and Unreal Engine occasionally have macro naming conflicts (e.g., `check`, `PF_MAX`, or Windows-specific macros). Always wrap Eigen includes in the engine's third-party protection macros to **eliminate** compilation errors:

	    ```cpp

	    THIRD_PARTY_INCLUDES_START

	    #include <Eigen/Core>

	    #include <Eigen/Dense>

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	*   **Use Eigen::Map for Zero-Copy Conversion**  

	    Avoid manually looping through arrays to convert `TArray<float>` or `FVector` to Eigen types. Use `Eigen::Map` to wrap existing Unreal memory. This allows Eigen to operate directly on Unreal's data, which helps **eliminate** unnecessary memory allocations and copy overhead:

	    ```cpp

	    FVector UEPos(100.f, 200.f, 300.f);

	    Eigen::Map<Eigen::Vector3f> EigenPos(&UEPos.X);

	    ```

	 

	*   **Leverage for High-Dimensional Math**  

	    Unreal’s `FMatrix` is strictly 4x4. If you are implementing a custom procedural animation system or a machine learning inference pass that requires a 10x10 or dynamic matrix, use `Eigen::MatrixXf`. This allows you to **eliminate** the complexity of writing custom solvers for high-dimensional data.

	 

	*   **Be Mindful of Memory Alignment**  

	    Eigen often uses SIMD instructions that require 16-byte or 32-byte alignment. When nesting Eigen types inside Unreal `USTRUCT` or `UCLASS` types, use the `EIGEN_MAKE_ALIGNED_OPERATOR_NEW` macro. Failing to do this can lead to hard-to-debug crashes (Access Violations) during object instantiation.

	 

	*   **Prefer Row-Major for Unreal Compatibility**  

	    By default, Eigen uses Column-Major storage, while many developers expect Row-Major or need to interface with specific data structures. You can define your matrices as `Eigen::Matrix<float, 4, 4, Eigen::RowMajor>` to better align with Unreal’s internal `FMatrix` memory layout and **eliminate** transposition logic.

	 

	*   **Use for Solving Optimization Problems**  

	    If you need to implement a Least-Squares fit for a character's foot placement or a complex Inverse Kinematics (IK) solver, use Eigen’s built-in solvers (like `JacobiSVD` or `ColPivHouseholderQR`). These are highly optimized and will **eliminate** the need for you to implement complex numerical recipes from scratch.

	 

	*   **Strictly Editor or Tooling Use**  

	    Unless your gameplay specifically requires complex runtime math (like a real-time physics solver), keep Eigen usage within Editor modules or specialized plugins. This keeps your runtime game executable smaller and helps **eliminate** the risk of unintended performance spikes on low-end mobile or console hardware.
Copy code
Leverage for High-Dimensional Math
Unreal’s FMatrix is strictly 4x4. If your project requires an 8x8 matrix for a custom inverse kinematics solver or a 12x12 matrix for a complex physics constraint, use Eigen’s Matrix<float, N, N>. This allows you to eliminate the technical debt of writing custom high-dimensional math solvers.
Explicitly Choose Row-Major vs. Column-Major
Unreal Engine typically uses a row-major convention for its matrices, while Eigen defaults to column-major. When defining Eigen matrices that will interface with Unreal data, specify Eigen::RowMajor in the template arguments to eliminate the need for frequent transposition.
Alignment and SIMD Optimization
Eigen uses SIMD instructions for performance. When nesting Eigen types inside Unreal USTRUCT or UCLASS types, ensure you use the EIGEN_MAKE_ALIGNED_OPERATOR_NEW macro. This ensures the object is allocated on the correct byte boundary, helping you eliminate alignment-related crashes on certain platforms.
Utilize Advanced Solvers for Gameplay Features
For features like procedural foot placement or complex character elimination physics, use Eigen’s built-in solvers like JacobiSVD or ColPivHouseholderQR. These are highly optimized and stable, which helps you eliminate jitter and “exploding” physics results in your simulations.
Strictly Segregate to Developer/Editor Modules
Unless your runtime gameplay strictly requires complex linear algebra (like a real-time machine learning plugin), keep Eigen usage within Editor or Developer modules. This helps you eliminate the binary size footprint and potential performance overhead in your final shipping build.
Reference the ThirdParty Directory
If you need to check the specific version of Eigen included with your engine version (e.g., UE 5.6), look in Engine/Source/ThirdParty/Eigen. Familiarizing yourself with the included headers will eliminate confusion about which specific Eigen features (like unsupported modules) are available for your project.