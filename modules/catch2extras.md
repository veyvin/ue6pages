---
layout: default
title: Catch2Extras
---

<!-- ai-generation-failed -->

<h1>Catch2Extras</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Catch2/Catch2Extras.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

C++ unit testing framework. While Catch2 is a standard open-source library, it is not inherently aware of Unreal’s architecture. This module provides the necessary “extras”—such as custom macros, lifecycle hooks, and runners—that allow developers to write Low-Level Tests (LLT) that can interact with UObjects, the engine’s reflection system, and the modular build system (UBT).

Practical Usage Tips & Best Practices
1. Use GROUP Macros for Organization

Standard Catch2 uses tags, but the Catch2Extras module introduces GROUP_TEST_CASE.

Best Practice: Use groups to categorize tests by system (e.g., “Physics”, “AI”). This allows you to run specific subsets of tests via the command line, facilitating the elimination of long wait times when you only need to verify a specific module.
2. Leverage Lifecycle Events

The module provides Unreal-aware hooks like GROUP_BEFORE_ALL and GROUP_AFTER_EACH. Use these to initialize global engine systems or mock data once per group rather than per test, which significantly improves the performance of your test suite.

3. Handle UObject Cleanup

When writing tests that spawn UObjects, memory can leak between tests if not handled correctly.

Tip: Use the lifecycle hooks provided in this module to trigger the Garbage Collector or manually call MarkAsGarbage() on your test actors. This ensures the elimination of stale data that could cause “Leftover Object” warnings in subsequent tests.
4. Run Tests via the Command Line

You can execute tests built with this module directly through the compiled test executable (found in Binaries/Win64/). Use the --log and --debug flags. This is the best practice for CI/CD pipelines where you need a lightweight, headless way to verify code health without launching the full Unreal Editor.

5. Inherit from TestModuleRules

To use this module in your project, your test module’s .Build.cs must inherit from TestModuleRules rather than the standard ModuleRules. This automatically configures the include paths and library dependencies required for Catch2 and its extras to function within the UE build environment.

6. Utilize “Wait for Debugger”

If a test is failing in a complex way, use the --waitfordebugger command-line argument. The Catch2Extras runner will pause execution at startup, allowing you to attach Visual Studio or Rider to the process before the test logic begins, ensuring you don’t miss the critical failure point.

7. Combine with “Fake” Subsystems

For Low-Level Tests, you often want to avoid initializing the entire engine. Use the extras to create “Fake” or “Mock” versions of engine subsystems. This allows you to test isolated logic (like a damage calculator) without needing to load a full world, leading to the elimination of heavy engine overhead during unit testing.

8. Monitor Output via UnrealVS

If you are using Visual Studio, install the UnrealVS extension. It integrates with the Catch2Extras module to display your tests in the Visual Studio Test Explorer. This provides a familiar, UI-driven way to run, debug, and see the results of your C++ tests without leaving your IDE.