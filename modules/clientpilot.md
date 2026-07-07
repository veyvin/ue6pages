---
layout: default
title: ClientPilot
---

<!-- ai-generation-failed -->

<h1>ClientPilot</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/ClientPilot/ClientPilot.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

g framework designed to drive a game client without human input.

Description and Purpose

ClientPilot acts as a “virtual player” system that can be programmed to perform specific actions, navigate worlds, and interact with game systems automatically. Unlike standard AI bots which are part of the game logic, ClientPilot is a developer-facing tool used primarily for automated smoke testing, performance profiling, and soak testing. It allows developers to simulate hundreds of hours of gameplay to find crashes, memory leaks, or performance regressions that would be impossible to detect through manual testing. It is frequently used in conjunction with the Gauntlet Automation Framework to run unattended test sessions on various platforms.

Practical Usage Tips and Best Practices
Integrate with Gauntlet for CI/CD
The most effective way to use ClientPilot is within a Gauntlet script. You can configure Gauntlet to launch a build, initialize a ClientPilot controller, and monitor the session for crashes. This setup allows you to eliminate the need for manual daily smoke tests.
Use the ClientPilot Blackboard
Utilize the IClientPilotBlackboard interface to share data between the automation controller and the game. You can push state information (like “Current Level” or “Match Phase”) to the blackboard, allowing the Pilot to make context-aware decisions about where to move or what to interact with.
Implement Custom Pilot Components
For project-specific logic, create a custom UClientPilotComponent. This allows you to define unique “Pilot Actions”—such as using a specific ability or navigating to a custom objective—ensuring the automated agent tests the actual “fun” parts of your gameplay loop.
Automate Performance Bottleneck Discovery
Use ClientPilot to run a fixed “golden path” through a level while recording performance data (CSV or Insights). By running the same path on every build, you can easily identify and eliminate performance dips caused by recent code or asset changes.
Simulate High-Stress Elimination Scenarios
In multiplayer games, program ClientPilot to gather many agents in a small area to trigger constant combat and elimination events. This “stress test” is vital for identifying network saturations or VFX-related frame drops that occur when many players are eliminated simultaneously.
Enable via Command Line
You can trigger ClientPilot without modifying code by using the command-line argument -ClientPilot. This is useful for QA teams or build machines to quickly spin up an automated instance of the game using the default pilot settings.
Leverage Navigation Mesh Data
ClientPilot works best when the world has a valid NavMesh. Ensure your pilot logic uses the NavigationSystem to find paths; this prevents the automated agent from getting stuck on geometry, which helps eliminate “false positive” failures in your automation reports.
Record and Verify “Pilot Errors”
Configure your pilot to log an error if it fails to reach a goal within a certain timeframe. These “liveness” checks are essential for finding “soft-locks” in the game where a player might get stuck in a menu or a piece of collision, allowing you to eliminate these issues before release.