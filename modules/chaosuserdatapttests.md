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

rs, wind forces, or custom solver parameters—Chaos uses a “Callback” system.

ChaosUserDataPTTests is used to:

Validate Data Flow: Ensure that data sent via FSimCallbackInput arrives intact at the Physics Thread.
Verify Lifecycle Management: Test the creation and destruction of user data objects across threads to prevent memory leaks or race conditions.
Test Async Callbacks: Validate the TSimCallbackObject, which is the primary mechanism for implementing custom physics logic (like custom gravity) without blocking the main game loop.
Stress Thread Safety: Use low-level unit tests to ensure that multiple threads writing to or reading from user data don’t cause crashes during solver steps.
Practical Usage Tips and Best Practices
1. Use as a Blueprint for Custom Gravity

If you are building a custom gravity system (e.g., for a spherical world), this module is your best reference. It demonstrates how to wrap your gravity data in a struct and pass it to the solver using Chaos::TSimCallbackObject. Look at the test cases to see how they verify that the physics solver correctly receives and applies these vectors.

2. Differentiate Input vs. Output Data

Follow the module’s pattern of separating data:

FSimCallbackInput: Data sent from GT to PT (e.g., “Apply 500 units of force to this specific ID”).
FSimCallbackOutput: Data sent back from PT to GT (e.g., “This collision event happened with this much energy”). Testing these separately in your own code prevents “data pollution” where the game thread accidentally overwrites active physics calculations.
3. Leverage “Low-Level Test” (LLT) Speed

Because this module is an Explicit Low-Level Test, it runs using the Catch2 framework. You can run these tests in seconds from the command line or Visual Studio Test Explorer without opening the Unreal Editor. This is the fastest way to debug your custom physics thread logic before integrating it into a full AActor.

4. Monitor the “Timestamp” Logic

The tests in this module often check for Data Freshness. When passing data to the Physics Thread, ensure you include a frame index or timestamp. The tests verify that the solver doesn’t process stale data from three frames ago, which is a common cause of “jittery” physics in networked games.

5. Proper Cleanup of User Data

When an actor is destroyed, its associated physics thread data must be cleaned up on the physics thread, not the game thread. Study the teardown sequences in ChaosUserDataPTTests to see how the module handles the elimination of simulation callback objects to avoid orphaned memory.

6. Use Marshalling instead of Raw Pointers

A key best practice validated by this module is Marshalling. Never pass a raw pointer to a UObject from the Game Thread directly into a Chaos PT callback. Instead, follow the module’s example: extract the raw POD (Plain Old Data) or FVector values into a struct and pass that struct.

7. Test with “Fixed Tick” Enabled

When writing your own tests based on this module, ensure you test with Fixed Timestep enabled. Many Chaos user data issues only appear when the delta time is constant, as variable timesteps can mask interpolation errors that the ChaosUserDataPTTests module is designed to catch.

8. Verify Particle-to-Data Mapping

The module provides examples of mapping FGeometryParticleHandle to your custom user data. If you have thousands of objects, you don’t want to pass a massive array every frame. Use the module’s “dirty flagging” patterns to only send data for particles that have actually changed since the last physics tick.