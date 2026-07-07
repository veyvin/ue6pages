---
layout: default
title: ChaosUserDataPTTests
---

<!-- ai-generation-failed -->

<h1>ChaosUserDataPTTests</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/ChaosUserDataPTTests/ChaosUserDataPTTests.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>TestModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Chaos, ChaosUserDataPT, Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ynchronously.

This module specifically tests the “marshalling” (transferring) of custom data from Game Thread objects (like Actors or Components) to their corresponding Physics Thread representations. It ensures that data remains consistent, thread-safe, and is not accidentally “eliminated” or corrupted during the transition between threads.

Practical Usage Tips & Best Practices
1. Reference for Async Physics C++

If you are implementing IPhysicsComponent or custom FPhysicsData that must be accessed during the OnPhysicsStep callback, use this module’s source code as a reference. It demonstrates the correct patterns for passing data to the Physics Thread without causing race conditions or memory access violations.

2. Test Thread-Safe Data Persistence

Use these tests to understand the lifecycle of User Data. A common pitfall is deleting a Game Thread object while the Physics Thread is still processing its collision; this module validates that the engine’s internal proxy system keeps the necessary data alive until the physics simulation for that frame is finished.

3. Focus on Data Marshalling

When writing custom physics extensions, ensure your data is “trivially copyable” where possible. This module tests the efficiency of copying data from GT to PT. If your data involves complex pointers, the tests here show how to use TSharedPtr or internal handles to avoid pointers becoming invalid after an actor is eliminated on the Game Thread.

4. Debugging via Catch2 Tags

Like other LLTs, you can run specific tests by using tags in the command line. If you are specifically working on collision-related user data, look for tags related to [Collision] or [Proxy] within the ChaosUserDataPTTests executable.

5. Verify Bit-for-Bit Consistency

In multiplayer games using Network Physics Prediction, the data on the Physics Thread must be perfectly consistent across clients. This module includes checks to ensure that the user data doesn’t drift or change unpredictably during the marshalling process.

6. Leverage for Build Pipeline Validation

Integrate this module into your Continuous Integration (CI) flow using RunUAT. This ensures that any changes to your project’s low-level C++ physics wrappers don’t break the async data pipeline:

bash
RunUAT.bat BuildGraph -Script="Engine/Build/LowLevelTests.xml" -Target="Chaos User Data PT Tests Win64"
Copy code
7. Monitor Memory Overhead

The tests in this module help identify “memory bloat” caused by keeping too much user data in the physics proxy. Best practice is to keep Physics Thread user data as small as possible—only store what is strictly necessary for the solver (like mass overrides or material properties).

8. Trace Data During Elimination

Use the tests to observe what happens when a physics body is removed from the simulation. The module validates that the “Elimination” of a physics proxy correctly triggers the cleanup of associated user data, preventing memory leaks in scenes with high object turnover (like destruction-heavy environments).