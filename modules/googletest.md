---
layout: default
title: GoogleTest
---

<!-- ai-generation-failed -->

<h1>GoogleTest</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/GoogleTest/GoogleTest.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

n the engine’s third-party source) is the Unreal Engine integration of the Google C++ Testing and Mocking Framework (GTest/GMock). While Unreal Engine 5 uses Catch2 as its primary framework for Low-Level Tests (LLT), GoogleTest is provided as a robust alternative for developers who require advanced mocking capabilities or are migrating existing C++ unit tests.

It is designed for isolated C++ unit tests that operate independently of the engine’s UObject system, renderer, or world. This allows for the high-speed validation of math libraries, data parsers, and core logic.

Practical Usage Tips and Best Practices
Opt-Out of Catch2 in Build.cs
By default, Unreal’s TestModuleRules includes Catch2. To use GoogleTest instead, you must pass false to the base constructor and set the GoogleTest flag in the metadata. This “eliminates” compilation conflicts between the two frameworks:
C#
	    public class MyGTestModule : TestModuleRules

	    {

	        public MyGTestModule(ReadOnlyTargetRules Target) : base(Target, false) // false = no Catch2

	        {

	            UpdateBuildGraphPropertiesFile(new Metadata("MyGTest", "My GTest Module", GoogleTest: true));

	        }

	    }

	    ```

	 

	*   **Wrap Includes to Prevent Macro Conflicts**  

	    GoogleTest and Unreal Engine both define common macros (like `CHECK` or `TEXT`). To "eliminate" compiler errors, always wrap GoogleTest/GMock includes in the engine's third-party protection macros:

	    ```cpp

	    THIRD_PARTY_INCLUDES_START

	    #include "gtest/gtest.h"

	    #include "gmock/gmock.h"

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	*   **Leverage GMock for Interface Isolation**  

	    The primary reason to use this module over Catch2 is **GMock**. Use it to "eliminate" dependencies on heavy Unreal modules by mocking C++ interfaces. This allows you to test a gameplay calculator without needing to instantiate a `UWorld` or `APlayerController`.

	 

	*   **Use for Non-UObject Logic Only**  

	    GoogleTest is not reflection-aware. If your test relies on `UPROPERTY` serialization, Blueprints, or `UFUNCTION` calls, use the engine's native **Automation Framework** instead. Use GoogleTest strictly for "pure" C++ logic, math libraries, or data parsers.

	 

	*   **Prefer `EXPECT_*` for Non-Fatal Assertions**  

	    Use `EXPECT_EQ` rather than `ASSERT_EQ` whenever possible. `EXPECT_*` allows the test to continue and report further failures in the same run, which "eliminates" the need to rerun tests multiple times just to see the full state of a failure.

	 

	*   **Organize Tests in `Source/Programs/LowLevelTests`**  

	    Follow the engine's convention by placing your GoogleTest files in the `LowLevelTests` directory. This "eliminates" discovery issues, as the Unreal Build Tool and UnrealVS extension are optimized to find and run executables located in this specific path.

	 

	*   **Initialize the Mocking Engine**  

	    If you are using GMock, you must initialize it in your test’s main entry point or global setup. Unreal’s LLT runner handles most of this, but ensure your test fixtures call `::testing::InitGoogleMock` if you are running a standalone test executable to "eliminate" runtime crashes when mocks are invoked.

	 

	*   **Manage Mock Lifetimes with `NiceMock`**  

	    If your mock object has many methods and your test only cares about one, wrap your mock in `testing::NiceMock<T>`. This "eliminates" verbose "uninteresting function call" warnings in your test logs, making it easier to spot actual failures.
Copy code
Wrap Includes to Prevent Macro Collisions
Both Unreal and GoogleTest define common macros like CHECK or TEXT. Always wrap GoogleTest includes in the engine’s third-party protection macros to “eliminate” compiler errors:
C#
	    public class MyGTestModule : TestModuleRules

	    {

	        public MyGTestModule(ReadOnlyTargetRules Target) : base(Target, false) // false = no Catch2

	        {

	            UpdateBuildGraphPropertiesFile(new Metadata("MyGTest", "My GTest Module", GoogleTest: true));

	        }

	    }

	    ```

	 

	*   **Wrap Includes to Prevent Macro Conflicts**  

	    GoogleTest and Unreal Engine both define common macros (like `CHECK` or `TEXT`). To "eliminate" compiler errors, always wrap GoogleTest/GMock includes in the engine's third-party protection macros:

	    ```cpp

	    THIRD_PARTY_INCLUDES_START

	    #include "gtest/gtest.h"

	    #include "gmock/gmock.h"

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	*   **Leverage GMock for Interface Isolation**  

	    The primary reason to use this module over Catch2 is **GMock**. Use it to "eliminate" dependencies on heavy Unreal modules by mocking C++ interfaces. This allows you to test a gameplay calculator without needing to instantiate a `UWorld` or `APlayerController`.

	 

	*   **Use for Non-UObject Logic Only**  

	    GoogleTest is not reflection-aware. If your test relies on `UPROPERTY` serialization, Blueprints, or `UFUNCTION` calls, use the engine's native **Automation Framework** instead. Use GoogleTest strictly for "pure" C++ logic, math libraries, or data parsers.

	 

	*   **Prefer `EXPECT_*` for Non-Fatal Assertions**  

	    Use `EXPECT_EQ` rather than `ASSERT_EQ` whenever possible. `EXPECT_*` allows the test to continue and report further failures in the same run, which "eliminates" the need to rerun tests multiple times just to see the full state of a failure.

	 

	*   **Organize Tests in `Source/Programs/LowLevelTests`**  

	    Follow the engine's convention by placing your GoogleTest files in the `LowLevelTests` directory. This "eliminates" discovery issues, as the Unreal Build Tool and UnrealVS extension are optimized to find and run executables located in this specific path.

	 

	*   **Initialize the Mocking Engine**  

	    If you are using GMock, you must initialize it in your test’s main entry point or global setup. Unreal’s LLT runner handles most of this, but ensure your test fixtures call `::testing::InitGoogleMock` if you are running a standalone test executable to "eliminate" runtime crashes when mocks are invoked.

	 

	*   **Manage Mock Lifetimes with `NiceMock`**  

	    If your mock object has many methods and your test only cares about one, wrap your mock in `testing::NiceMock<T>`. This "eliminates" verbose "uninteresting function call" warnings in your test logs, making it easier to spot actual failures.
Copy code
Use GMock for Interface Isolation
The primary advantage of this module is GMock. Use it to “eliminate” dependencies on heavy engine modules by mocking C++ interfaces. This allows you to test a damage calculator without needing a live AActor or UWorld.
Strictly for Non-Reflected Logic
GoogleTest is not reflection-aware. If your test requires UPROPERTY values, Blueprints, or UFUNCTION calls, you should use the engine’s native Automation Framework or CQTest instead. Use GoogleTest to “eliminate” dependencies for “pure” C++ classes.
Prefer EXPECT_* Over ASSERT_*
Use EXPECT_EQ rather than ASSERT_EQ for non-fatal checks. EXPECT_* allows the test to continue after a failure, which “eliminates” the need for multiple test runs to identify every failing condition in a single suite.
Place Tests in Source/Programs/LowLevelTests
Follow the engine’s directory convention. Placing your GoogleTest files here “eliminates” discovery issues, as the Unreal Build Tool (UBT) and the UnrealVS extension are optimized to find and run test executables in this path.
Use NiceMock to Reduce Log Noise
If your mock has many methods but you only care about one, wrap your mock in testing::NiceMock<T>. This “eliminates” verbose “uninteresting function call” warnings in your output, making it easier to spot actual failures.
Reset Mocks in Teardown
Always “eliminate” the risk of state leakage between test cases by resetting your mock objects or using fresh instances in each TEST_F fixture. This ensures each test is a deterministic, atomic operation.