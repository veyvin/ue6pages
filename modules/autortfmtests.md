---
layout: default
title: AutoRTFMTests
---

<!-- ai-generation-failed -->

<h1>AutoRTFMTests</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/AutoRTFMTests/AutoRTFMTests.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, AutoRTFM, Catch2Extras, Core, CoreUObject, DesktopPlatform, Internal, Private, Projects</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

validate the functionality and correctness of the AutoRTFM (Automatic Relaxed Transactional Fine-grained Memory) system. AutoRTFM is Unreal Engine’s experimental implementation of software transactional memory, which allows the engine to execute C++ code within “transactions” that can be automatically rolled back if a conflict or violation occurs.

This module contains a suite of unit and integration tests that ensure that memory operations, object state changes, and engine-specific logic behave predictably when wrapped in an AutoRTFM transaction.

Practical Usage Tips and Best Practices
Understand Transactional Contexts
Use these tests as a reference for how to properly scope a transaction. AutoRTFM transactions are designed to “eliminate” the need for complex manual mutexes in certain multi-threaded scenarios, but they must be carefully tested to ensure they don’t include non-transactional side effects like raw file I/O.
Test for Rollback Integrity
A key best practice when writing tests for this module is verifying that a failed transaction restores memory to its exact prior state. Ensure your tests “eliminate” any leaked state by checking that variables modified inside a transaction revert to their original values upon an abort.
Monitor for Abort Triggers
The tests in this module often focus on identifying “unsupported operations” (such as certain system calls) that cause a transaction to abort. Use these tests to learn which parts of the Unreal API are “transaction-safe” and which are not.
Configure for Low-Level Testing
In your Build.cs, you may need to explicitly include this module when running specific test targets or building for platforms where AutoRTFM is being evaluated.
C#
	// In YourProject.Build.cs

	if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PublicDependencyModuleNames.Add("AutoRTFMTests");

	}
Copy code
Validate Thread Safety Without Locks
Use the patterns found in AutoRTFMTests to verify that shared data can be modified by multiple threads without traditional locks. This helps “eliminate” common deadlocking issues, provided the logic remains within the supported transactional bounds.
Use the Automation Frontend
Like most engine tests, these are accessible via the Session Frontend (Window > Tools > Session Frontend). Filter by “AutoRTFM” to run the suite and verify that the transactional memory system is functioning correctly on your current hardware/OS configuration.
Isolate Side Effects
When writing custom logic intended for AutoRTFM, follow the module’s example of “eliminating” external dependencies inside the transaction. If a function within a transaction calls a non-reflected C++ library, the test suite is designed to detect and report these violations.
Profile Performance Overheads
Transactional memory carries a performance cost for tracking changes. Use the timing data from these tests to “eliminate” inefficient transactional logic that might be better suited for standard synchronous execution or traditional task-based parallelism.