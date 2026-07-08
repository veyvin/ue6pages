---
layout: default
title: Horde
---

<!-- ai-generation-failed -->

<h1>Horde</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Horde/Horde.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, HTTP, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ames’ Horde, a high-performance build automation, remote execution, and continuous integration (CI) platform. Unlike generic CI tools like Jenkins, this module is purpose-built to handle the unique demands of Unreal Engine projects, such as massive Perforce repositories, distributed C++ compilation, and automated hardware testing.

It acts as the connective tissue between the local Unreal Editor/Build tools and the Horde Server, facilitating the elimination of manual build management by automating the entire lifecycle from commit to deployment.

Practical Usage Tips and Best Practices
1. Implement BuildGraph for Pipeline Logic

Horde is designed to use BuildGraph scripts as its primary instruction set. Using BuildGraph instead of raw batch files facilitates the elimination of rigid, non-parallel pipelines, allowing Horde to distribute different parts of your build (like Cook, Compile, and Test) across multiple agents simultaneously.

2. Utilize the Unreal Build Accelerator (UBA)

Integrate the Horde module with UBA to distribute C++ compilation and shader compilation tasks across your agent pool. This practice leads to the elimination of “compilation bottlenecks,” where a single developer or build machine is stuck for hours; instead, the workload is spread across the network for near-instant results.

3. Leverage “Remove on Sleep” for Agent Health

When configuring Horde Agents, set up automatic workspace cleanup. This ensures that old build artifacts and stale intermediate files are cleared between jobs, aiding in the elimination of disk-space errors that commonly cause build failures in large-scale production environments.

4. Configure Device Manager for Hardware Testing

Use the Horde module to interface with the Device Manager. This allows you to automatically deploy builds to mobile devices or consoles for automated Gauntlet tests. This automation is key for the elimination of manual “smoke testing,” ensuring that every build is verified on actual target hardware.

5. Monitor Studio Analytics

Enable the Studio Analytics features within the module to track telemetry from your team’s editors. Analyzing data such as “Average Shader Compile Time” or “Editor Load Time” across the studio leads to the elimination of workflow friction by identifying which hardware or project versions are slowing down your developers.

6. Use UGS Metadata Integration

The Horde module can report build status directly to UnrealGameSync (UGS). By displaying “Bad Build” or “Build In Progress” indicators to every developer in the studio, it assists in the elimination of wasted time spent by artists syncing to broken revisions.

7. Define Dynamic Agent Pools

Group your build machines into pools based on their capabilities (e.g., “High-RAM-Cookers” or “GPU-Shader-Nodes”). This ensures that heavy tasks are routed to appropriate hardware, facilitating the elimination of crashes caused by running memory-intensive cooks on underpowered agents.

8. Implement Elimination-Event Notifications

Configure Horde to send notifications (via Slack, Discord, or Email) upon the elimination of a build (a failure event). Fast feedback loops regarding build failures are the most effective way to ensure the elimination of bugs before they propagate to other branches in your Perforce stream.