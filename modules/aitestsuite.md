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

d for automated unit and functional testing of AI systems. It provides a collection of “mock” classes, test fixtures, and specialized environments that allow you to validate AI logic—such as Behavior Trees, Blackboard data, and EQS—without needing to manually play the game or set up complex levels.

Description

AITestSuite is used to ensure the stability of NPC “brains” and navigation logic. By providing lightweight versions of AI controllers and pawns, it allows developers to write C++ tests that verify if an AI agent makes the correct decision when specific data is fed into its Blackboard. It is essential for projects with complex NPC behaviors to prevent logic regressions during development.

Practical Usage Tips and Best Practices
1. Enable for Non-Shipping Builds

Since this is a testing utility, you should avoid including it in your final game executable. Wrap the dependency in your *.Build.cs file to ensure it is only compiled for editor or debug builds:

C#
	if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PublicDependencyModuleNames.Add("AITestSuite");

	}

	```

	 

	#### 2. Use `FAITestFixture` for Setup/Teardown

	The core of the module is the `FAITestFixture` struct. Use this within your `IMPLEMENT_SIMPLE_AUTOMATION_TEST` macros to handle the boilerplate of spawning a test world, an AI controller, and a mock pawn. This ensures every test starts with a "clean slate" AI agent.

	 

	#### 3. Leverage "Mock" AI Classes

	AITestSuite provides pre-made mock classes like `UMockAIController` and `UMockTask`. Instead of using your project's heavy, production-ready AI controllers—which may have complex dependencies—use these mocks to isolate the specific logic you are testing (e.g., verifying a Blackboard value change).

	 

	#### 4. Test Blackboard Logic in Isolation

	You can use the suite to verify that your Behavior Tree keys are being read and written correctly. By using the `MockAI` setup, you can manually trigger BT tasks and then assert that the `UBlackboardComponent` contains the expected data without actually running the full Behavior Tree.

	 

	#### 5. Validate EQS Queries with Mock Data

	Environment Query System (EQS) tests can be brittle. Use AITestSuite to create controlled scenarios where you know exactly how many items should be returned by a generator. This prevents "test drift" caused by changing level geometry.

	 

	#### 6. Utilize Latent AI Commands

	AI tests often require time (e.g., waiting for a move command to finish). Use the `ADD_LATENT_AUTOMATION_COMMAND` alongside the suite's movement helpers to write tests that wait for the AI to reach a destination before asserting success.

	 

	#### 7. Profile AI Performance in Tests

	You can use AITestSuite to run "Stress Tests" for your AI. For example, spawning 100 mock agents and measuring the tick time of a specific Behavior Tree decorator. This helps catch performance regressions early in the development cycle.

	 

	#### 8. Integrate with the Unreal Automation Tool (UAT)

	Once your tests are written using AITestSuite, run them via the **Session Frontend** in the editor or through the command line using UAT. This allows you to include AI validation in your Continuous Integration (CI) pipeline, ensuring that a change to a global AI setting doesn't break individual NPC behaviors.
Copy code
2. Utilize FAITestFixture for Setup

The FAITestFixture struct is the backbone of the module. Use it within your IMPLEMENT_SIMPLE_AUTOMATION_TEST macros to automate the boilerplate of spawning a test world, an AI controller, and a pawn. This ensures every test starts in a clean, isolated environment.

3. Leverage Mock AI Classes

Instead of using your heavy, production-ready AI classes (which may have many dependencies), use UMockAIController and UMockPawn. These are stripped-down versions provided by the suite that allow you to focus purely on testing a specific Behavior Tree task or decorator.

4. Validate Blackboard Key Logic

Use the suite to programmatically check if Blackboard values are being updated correctly. For example, you can force a “TargetActor” key to be null and verify that the AI’s “Search” state is triggered immediately, helping you eliminate edge-case bugs in decision-making.

5. Stress Test EQS Queries

Environment Query System (EQS) tests can be performance-heavy. Use the AITestSuite to run “headless” EQS queries in a loop to measure execution time and ensure that your distance or line-of-sight filters return the expected number of items in a controlled space.

6. Use Latent Commands for Movement

AI actions (like moving to a location) take time. Combine AITestSuite with ADD_LATENT_AUTOMATION_COMMAND to wait for the MoveTo command to complete or fail before running your assertions. This allows you to test pathfinding reliability without manual intervention.

7. Test AI Elimination Logic

Use the suite to simulate the elimination of an AI agent. You can programmatically apply damage to a mock pawn and verify that the AI Controller correctly clears its Blackboard keys and ceases all Behavior Tree execution upon the elimination event.

8. Integrate with Continuous Integration (CI)

Run your AITestSuite tests via the Unreal Automation Tool (UAT) command line. This allows your build server to automatically verify that any changes to the C++ AI framework haven’t broken existing NPC behaviors before the code is merged into the main branch.