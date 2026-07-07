---
layout: default
title: AITestSuite
---


<h1>AITestSuite</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AITestSuite/AITestSuite.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AIModule, Core, CoreUObject, Engine, GameplayTasks</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

gned for low-level automated testing of AI systems. It provides a framework to validate AI logic, such as Behavior Trees and the Environment Query System (EQS), in a controlled and repeatable manner.

Description and Purpose

While the FunctionalTesting module is intended for high-level, level-based actor interactions, AITestSuite focuses on granular unit and integration testing. It allows developers to mock world states and programmatically verify that AI decision-making remains consistent. It is a critical tool for developers building complex, data-driven AI who need to ensure that framework updates or code changes do not break existing NPC behaviors.

Practical Usage Tips and Best Practices
Configure Build Dependencies
Since this is a developer module, it should not be included in your final game build. Add it to your [Project].Build.cs using a conditional check to ensure it only loads in non-shipping configurations:
C#
	if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PrivateDependencyModuleNames.Add("AITestSuite");

	}

	```

	 

	#### 2. Inherit from FAITestBase

	To create a custom C++ AI test, inherit your test class from `FAITestBase`. This base class provides the boilerplate needed to interface with the Unreal Automation Controller and manage the lifecycle of an AI-specific test.

	 

	#### 3. Isolate EQS Queries

	One of the best uses of this module is testing **EQS (Environment Query System)**. You can use the module's utilities to manually run a query against a set of mock items (like points or actors) and assert that the "Best Item" returned matches your expected result, bypassing the need to wait for a "pawn" to physically execute it in-game.

	 

	#### 4. Mock the World and WorldContext

	AI components often require a `UWorld` to function (e.g., for line traces or navigation lookups). When using `AITestSuite`, use the internal helpers to create a "Small World" or a mock `WorldContext`. This ensures your tests are fast and don't conflict with other tests running in the same session.

	 

	#### 5. Verify Behavior Tree Transitions

	Use the suite to "pump" the Behavior Tree component. Instead of waiting for real-time seconds, you can programmatically trigger events (like changing a Blackboard key) and immediately verify if the `BTComponent` has successfully transitioned to the expected task or sub-tree.

	 

	#### 6. Use Latent Commands for Pathfinding

	Testing navigation often requires waiting for a path to be generated. Combine `AITestSuite` logic with `ADD_LATENT_AUTOMATION_COMMAND` to wait for the `NavigationSystem` to finish a request before asserting that the path is valid.

	 

	#### 7. Clean Up Mock Actors

	Tests in this module often spawn `AAIController` or `APawn` instances. Always override the teardown/cleanup logic to destroy these actors. Failing to do so will result in "World Leak" warnings in the Automation Front End, which can invalidate subsequent tests.

	 

	#### 8. Regression Testing for Bug Fixes

	Whenever you fix a bug in a complex Behavior Tree Task or a custom AI Controller, write an `AITestSuite` test that reproduces the failure state. This ensures that future changes to the AI's "brain" won't re-introduce the same bug, which is common in complex state-driven AI.
Copy code
Inherit from FAITestBase
For custom C++ AI tests, inherit your class from FAITestBase. This provides the necessary environment setup, including a specialized test runner and access to common AI mocking utilities.
Isolate EQS Testing
Use the suite to test Environment Query System (EQS) assets in isolation. You can manually feed the query a set of mock items and assert that the “Best Item” chosen matches your expected result, which is much faster than spawning a Pawn and waiting for a spatial query to run in a live level.
Mock the World Context
AI components often require a UWorld to function. Use the module’s helpers to create a lightweight “Mock World.” This prevents your tests from interfering with the persistent level and keeps test execution times extremely low.
Validate Behavior Tree Transitions
Instead of watching an NPC in the editor, use the suite to “pump” the Behavior Tree component. You can programmatically change Blackboard keys and immediately verify if the BTComponent has transitioned to the correct task or sub-tree.
Use Latent Commands for Navigation
Testing pathfinding often requires waiting for the NavigationSystem to finish a request. Combine AITestSuite logic with ADD_LATENT_AUTOMATION_COMMAND to pause the test until a path is successfully generated or fails as expected.
Implement Regression Tests for Eliminations
When building combat AI, create a test case that simulates a player elimination. Use the suite to verify that the AI’s “Perception” or “Targeting” logic correctly clears the target and transitions back to an “Idle” or “Patrol” state immediately upon the elimination event.
Cleanup Mock Actors
AI tests frequently spawn AAIController or APawn instances. Always override the cleanup functions provided by FAITestBase to destroy these actors. This prevents “World Leak” errors in the Automation Front End that can cause subsequent tests to fail.