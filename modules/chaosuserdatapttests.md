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

suite in Unreal Engine. Its purpose is to validate the integrity and synchronization of User Data on the Physics Thread (PT).

In the Chaos Physics architecture, data is often “marshaled” (copied) from the Game Thread (GT) to the Physics Thread to allow for asynchronous simulation. This module ensures that custom metadata attached to physics objects (like particles or geometry collections) is correctly persisted and remains accessible to the solver without being corrupted or “eliminated” during the thread hand-off.

Practical Usage Tips and Best Practices
1. Understand the “PT” in the Name

The “PT” stands for Physics Thread. These tests are specifically designed for the Async Physics workflow. If your project uses the standard “Tick” based physics on the Game Thread, these tests may not be relevant. Use them primarily if you are implementing custom sub-stepping or async physics logic where data must cross thread boundaries.

2. Reference for FPhysicsProxy Data

Use this module’s source code as a blueprint for how to pass custom data through an FPhysicsProxy. It demonstrates how to “push” data from a Component into the Chaos Solver and retrieve it during the physics callback without causing race conditions.

3. Validate Data Persistence

When adding custom gameplay tags or status effects to a physics body (e.g., marking a destructible piece as “Invulnerable”), use these tests to ensure the data persists. A common bug is for data to be “eliminated” when a geometry collection fractures; these tests help you verify that the new “child” particles inherit the User Data correctly.

4. Debugging Thread Desyncs

If your physics callbacks are receiving null pointers or garbage data for User Data, run the tests in this module. If the engine’s built-in tests pass but yours fail, it indicates that your custom data isn’t being correctly registered with the FChaosMarshalingManager.

5. Proper Memory Management

These tests emphasize the “elimination” of data at the correct time. Because User Data on the Physics Thread exists outside the standard Garbage Collection (GC) loop of the Game Thread, you must ensure your data is manually cleaned up when the Physics Proxy is destroyed. Follow the patterns in these tests to avoid memory leaks.

6. Use with “Unreal Insights”

When running the ChaosUserDataPTTests, keep Unreal Insights open with the Physics Trace enabled. This allows you to see the exact frame where data is marshaled from the Game Thread to the Physics Thread, helping you visualize the synchronization process the module is testing.

7. Test for Scalability and “Elimination”

In scenes with thousands of active physics bodies, the overhead of User Data can become significant. These tests can be used to benchmark the performance cost of attaching large structs to every physics particle, helping you decide when to use a lightweight index instead of a full object reference.

How to Access the Tests

You can run these tests via the Session Frontend:

Open Tools > Session Frontend.
Navigate to the Automation tab.
Search for the filter: System.Physics.Chaos.UserData.
Core Technical Concepts
Marshaling: The process of moving data from the GT to the PT safely.
Physics Proxy: The middleman object that represents a Game Thread Actor in the Physics World.
Dirty State: The module tests the logic that marks User Data as “dirty” to trigger a sync between threads only when necessary, optimizing performance.