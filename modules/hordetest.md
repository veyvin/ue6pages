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

onnect Unreal Engine’s internal testing frameworks with Horde, Epic’s high-performance CI/CD and build automation system.

Description and Purpose

This module serves as the primary bridge between the Gauntlet Automation Framework and the Horde server. Its purpose is to ingest individual test results, logs, and performance metrics from an automated run and format them into searchable metadata for the Horde Automation Hub. By using this module, developers can surface test health across different platforms, branches, and rendering APIs in a unified dashboard. It is essential for teams using Horde to track historical test data, investigate elimination events or crashes via callstacks, and manage large-scale automated playtests.

Practical Usage Tips and Best Practices
Enable Result Reporting via Command Line
To ensure your tests are visible in the Horde dashboard, you must append the -WriteTestResultsForHorde argument to your Gauntlet or UAT (Unreal Automation Tool) command line. This tells the module to generate the specific JSON metadata required to eliminate manual status reporting.
Define Target Device Pools in BuildGraph
Use the HordeDevicePool and HordeDeviceService properties within your BuildGraph.xml scripts. This allows the HordeTest module to intelligently route tests to specific hardware (like an Android farm), helping you eliminate resource contention during busy build windows.
Utilize Test Events for Visual Debugging
Script your tests to trigger “Test Events” through the Horde interface. These can include screenshots taken at the moment of a failure or an elimination event. Viewing these directly in the Horde UI helps you eliminate the need to manually download and scrub through massive log files.
Monitor Test Health with Build Badges
The HordeTest module feeds data into the “Build Health” system. Configure your stream to show status badges for specific test suites (e.g., “BVT” or “SmokeTests”). This visibility allows developers to quickly see if a recent commit caused an elimination of build stability.
Cross-Stream Comparison for Regressions
Use the Automation Hub’s historical view to compare current test results against previous changelists. This is the most efficient way to eliminate regressions, as you can pinpoint the exact commit where a performance metric or test case began to fail.
Leverage Metadata Filters
Since the HordeTest module generates data-driven metadata, use the UI filters to isolate failures by “RHI” (e.g., DX12 vs Vulkan) or “Configuration” (e.g., Debug vs Shipping). This granular filtering helps you eliminate noise when investigating platform-specific bugs.
Automate Triage with Fingerprints
Horde uses “Fingerprints” to group similar test failures together. If multiple tests fail due to the same underlying crash or elimination of a service, the system will group them into a single “Issue,” helping you eliminate redundant bug reports for the same root cause.
Include Performance Telemetry
Beyond simple pass/fail states, use the module to report telemetry like frame times or memory usage. Tracking these over time in Horde allows your team to eliminate “performance creep” by identifying subtle regressions that don’t necessarily cause a test to fail.