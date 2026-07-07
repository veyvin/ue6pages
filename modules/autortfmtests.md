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

cally designed to validate the AutoRTFM (Automatic Real-Time Fast Mutex) system in Unreal Engine. AutoRTFM is Unreal’s implementation of Transactional Memory, which allows the engine to execute code blocks speculatively and “roll back” changes if a conflict occurs (e.g., during Verse execution or parallel gameplay logic).

The module contains unit tests and stress tests that ensure the transactional compiler and runtime can correctly track memory mutations, handle nested transactions, and maintain data integrity across threads.

Practical Usage Tips and Best Practices
1. Use as a Reference for Transactional C++

If you are working with the AutoRTFM API in C++, this module is your best resource for syntax examples.

Tip: Look at the tests for UE_AUTORTFM_OPEN and AutoRTFM::Commit. These demonstrate how to wrap logic in a transaction so that if a failure occurs, the state is restored, eliminating the risk of partial data corruption.
2. Verify Thread Safety without Manual Mutexes

AutoRTFM is designed to manage concurrency without traditional locks.

Best Practice: Study the contention tests in this module to understand how the system handles multiple threads accessing the same data. By using transactional memory instead of rigid mutexes, you can eliminate deadlocks in complex parallel systems.
3. Test Abort and Rollback Logic

A core feature of AutoRTFM is the ability to undo memory changes.

Tip: Implement your own tests using the patterns found in AutoRTFMTests to verify that your custom structs and containers support rollback. This ensures that if a gameplay transaction fails, all variables are reset to their original state, eliminating “ghost” values.
4. Understand Non-Transactional “Escapes”

Not all code can be rolled back (e.g., I/O operations or hardware calls).

Best Practice: Reference the “Open” tests in the module. These show how to use UE_AUTORTFM_OPEN to execute code that must persist even if the surrounding transaction is aborted. This is critical for logging or sending network packets that shouldn’t be eliminated during a retry.
5. Run Tests During Engine Customization

If you are modifying the Unreal Build Tool (UBT) or the Clang compiler integration for your project:

Action: Regularly run the AutoRTFMTests via the Session Frontend. If these tests fail, it indicates that your compiler changes have broken the transactional memory instrumentation, which will eliminate the stability of any Verse-based systems.
6. Use for Performance Benchmarking

The module includes “Contention” tests that measure how the system scales under heavy load.

Tip: Run these tests on your target hardware (especially consoles) to see the overhead of transactional memory. Understanding these limits helps you eliminate performance bottlenecks before deploying large-scale parallel logic.
7. Profile Transactional Aborts

Frequent rollbacks are expensive and can degrade performance.

Best Practice: Use the patterns in the stress tests to identify “hot spots” where transactions frequently conflict. By rearranging data to be more thread-local, you eliminate unnecessary aborts and retries, streamlining execution.
8. Monitor Memory Instrumentation

AutoRTFM requires specific memory alignment and tracking.

Tip: Watch for “Write-after-Read” or “Write-after-Write” conflict logs produced by these tests. These logs help you identify logic that is too “intertwined” for transactional execution, allowing you to refactor and eliminate complex dependencies.