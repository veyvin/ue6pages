---
layout: default
title: StateStreamTests
---

<!-- ai-generation-failed -->

<h1>StateStreamTests</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/LowLevelTests/StateStreamTests/StateStreamTests.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>TestModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, StateStream</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nreal Engine designed to validate the reliability, networking, and synchronization of the StateTree and MassEntity streaming systems.

Description and Purpose

This module contains a collection of functional and unit tests (utilizing the CQTest and AutomationTest frameworks) that focus on “State Streaming”—the process of passing state-based logic and data between different entities or across a network. Its primary purpose is to ensure that as StateTree assets are loaded, unloaded, or replicated, their internal states remain consistent and do not leak memory or lose data. By running these tests, developers can eliminate regressions in complex AI or crowd systems where an entity might “forget” its current task or get stuck in a transition during a level stream or network hitch.

Practical Usage Tips and Best Practices
Run via the Session Frontend
You can access these tests by opening the Session Frontend (Tools > Sessions Frontend) and navigating to the Automation tab. Searching for “StateStream” will allow you to run the suite, helping you eliminate uncertainty when upgrading engine versions or making deep changes to AI logic.
Use as a Reference for Custom StateTree Tests
If you are building a complex, data-driven StateTree, look at the C++ source for StateStreamTests. It demonstrates how to programmatically trigger state transitions and verify outcomes, which is a best practice to eliminate manual QA testing for every AI variation.
Validate Network Replication Consistency
A key part of this module tests how state data “streams” from a server to a client. Use these tests to verify that your RepNotify logic or RPC calls within a StateTree are firing in the correct order, helping you eliminate “desync” bugs in multiplayer AI.
Monitor Memory Leaks during Streaming
These tests often include “Stress Tests” that rapidly load and unload state-heavy entities. Running these while monitoring the LLM (Low Level Memory) tracker helps you eliminate memory fragmentation caused by improper cleanup of dynamic state data.
Test State Persistence across Level Transitions
Use the streaming-specific tests to ensure that when an actor moves between World Partition cells, its StateTree data is serialized and restored correctly. This is critical to eliminate NPCs resetting their behavior or “teleporting” back to a default state when the player moves away.
Integrate into CI/CD Pipelines
Include the StateStreamTests module in your automated build system (e.g., Gauntlet or Horde). Automatically running these tests after every engine pull helps you eliminate broken builds caused by low-level changes to the StateTree or Mass modules.
Verify Parameter Binding Reliability
The module tests the “Data Binding” system within StateTrees. Ensure your custom bindings (linking tasks to variables) are robust by comparing your implementation against the test cases provided in this module, which helps eliminate “Invalid Binding” errors at runtime.
Debug with the StateTree Debugger
While the tests provide automated “Pass/Fail” results, use the StateTree Debugger alongside them to visualize failures. Seeing exactly which state failed during a test iteration allows you to eliminate the root cause of logic loops or transition failures much faster.