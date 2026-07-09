---
layout: default
title: HordeTest
---

<!-- ai-generation-failed -->

<h1>HordeTest</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Horde/Samples/HordeTest/HordeTest.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Unreal Engine’s Gauntlet Automation Framework with the Horde CI/CD ecosystem. It provides the logic necessary to intercept test results—such as logs, screenshots, and performance metrics—and format them into a structured schema that the Horde Automation Hub can ingest. This module is essential for teams looking to surface high-level “health” data from automated game sessions into a searchable, web-based dashboard.

Practical Usage Tips & Best Practices
1. Enable Reporting via BuildGraph

The most common way to invoke the HordeTest logic is through a BuildGraph node. Simply running a test is not enough; you must explicitly signal the engine to write results in a Horde-compatible format.

Best Practice: Add the -WriteTestResultsForHorde argument to your RunUnreal command in BuildGraph. This ensures the module generates the JSON metadata required for the Automation Hub to visualize the results, facilitating the elimination of manual log parsing.
2. Leverage Searchable Metadata for Filtering

The HordeTest module automatically extracts metadata from your tests, such as the RHI (DirectX vs. Vulkan), GPU model, and build configuration.

Tip: Use the Automation Filters in the Horde UI to create custom dashboards. Because HordeTest populates these fields, you can quickly isolate bugs that only occur on specific mobile chipsets, ensuring the elimination of platform-specific regressions.
3. Capture Screenshots for Visual Regressions

A key feature of this module is its ability to surface screenshots directly in the Horde web interface.

Best Practice: When a Gauntlet test fails (e.g., a “Character Elimination” animation doesn’t play), ensure your test script captures a screenshot. The HordeTest module will detect these artifacts and link them to the specific failure event in the dashboard.
4. Utilize “Test Tiles” for Aggregate Health

In the Horde Automation Hub, results are presented as color-coded “tiles” representing the state of specific test suites.

Tip: Organize your tests into meaningful suites (e.g., SmokeTests, Performance). The HordeTest module uses these suite names to aggregate results, which assists in the elimination of confusion when determining which subsystem is currently broken in the main branch.
5. Integrate with the Horde Device Manager

The HordeTest module works alongside the Mobile/Console Device Manager to ensure tests run on the correct hardware.

Best Practice: Define your HordeDevicePool in your project settings. This ensures the test is dispatched to a machine with the correct physical device attached, leading to the elimination of “false passes” that occur when testing mobile logic on a PC.
6. Track Performance via Historical Telemetry

HordeTest surfaces more than just pass/fail states; it can track performance metrics over time.

Tip: Monitor the “Test History” graphs in the Automation Hub. If you see a sudden spike in frame times during an “Enemy Elimination” event, you can use the historical data to correlate the performance drop with a specific Perforce changelist.
7. Automate Failure Notifications

The module allows the CI system to know exactly who broke a test based on the commit history.

Best Practice: Ensure your Perforce user identity is linked to your Horde profile. When the HordeTest module reports a failure, Horde can ping the developer who submitted the breaking change, resulting in the elimination of long delays in finding the responsible party.
8. Use Custom Test Events for Deep Diagnostics

For complex gameplay systems, simple success/failure messages are often insufficient.

Tip: Within your C++ Gauntlet controller, emit custom test events. The HordeTest module will capture these events—complete with callstacks—allowing for the elimination of “mystery bugs” by providing the full context of the failure during long-running soak tests.