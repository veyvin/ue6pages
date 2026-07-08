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

ilot operates at the gameplay level—it can spawn into a map, move between waypoints, and interact with the world. It is a key component of the Gauntlet Automation Framework, allowing developers to run hundreds of automated “playtest” sessions across different platforms to detect crashes, performance regressions, or navigation errors before they reach a human QA team.

Practical Usage Tips and Best Practices
1. Use for Automated Performance Baselines

Integrate ClientPilot into your CI/CD pipeline to run “flythroughs” of your levels. By having a bot follow a consistent path, you can generate repeatable performance data. If a recent check-in causes a frame-rate drop at a specific location, the ClientPilot logs will help you identify the exact coordinates and assets involved.

2. Implement Custom Pilot Commands

The module is extensible. You can create your own IClientPilotCommand to perform game-specific actions, such as “Use Ability” or “Open Inventory.” This allows you to go beyond simple movement and simulate complex player loops, ensuring that gameplay systems remain functional after large code refactors.

3. Leverage the Waypoint System

To prevent bots from getting stuck, use a waypoint or “POI” (Point of Interest) system. You can configure ClientPilot to move between specific Actor tags in your level. This is a best practice for stress-testing specific high-density areas of a map where performance is most likely to degrade.

4. Configure via Command Line

ClientPilot is highly data-driven. You can trigger it via the command line when launching your game: -ClientPilot -Map=/Game/Maps/TestMap -PilotScript=MyFlightPath This makes it easy to integrate with external automation tools like Jenkins or TeamCity, as no manual interaction with the UI is required to start the test.

5. Combine with “Nativize” for Profiling

When running ClientPilot for performance testing, ensure you are running in a Test or Shipping build configuration. This ensures that the results are not skewed by editor overhead or debug symbols, allowing you to see the true impact of gameplay logic on the CPU and GPU.

6. Use for “Soak Testing”

Run ClientPilot in a loop for several hours (a “soak test”) to identify long-term issues like memory leaks or rare race conditions. Because the bot can move and interact indefinitely, it is much more likely to trigger an edge-case crash than a static test or a short manual playtest.

7. Monitor Bots During Elimination Events

In multiplayer projects, use ClientPilot to simulate high-occupancy matches. You can program bots to engage in combat, allowing you to test the stability of your networking and VFX systems during a mass elimination event. If 50 bots are eliminated simultaneously by a single explosion, ClientPilot will help you measure the server hitch and ensure the elimination logic doesn’t crash the instance.

8. Blacklist Problematic Areas

If your level has areas that are under construction or known to be broken, use the ClientPilot blacklist feature to prevent bots from entering those zones. This eliminates “false positive” crash reports from known-bad areas, allowing your team to focus on legitimate bugs discovered in “ready-to-test” sections of the game.