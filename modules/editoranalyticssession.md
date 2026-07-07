---
layout: default
title: EditorAnalyticsSession
---

<!-- ai-generation-failed -->

<h1>EditorAnalyticsSession</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/EditorAnalyticsSession/EditorAnalyticsSession.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

track and manage the lifecycle of an Unreal Editor instance for telemetry and stability monitoring.

Description and Purpose

This module handles the creation, persistence, and reporting of “sessions” for the Unreal Editor. It records critical data points such as the session start time, duration, and most importantly, the exit status (e.g., whether the editor was closed normally or terminated by a crash). Unlike standard gameplay analytics, this module is focused on Developer Efficiency and Editor Stability. It provides the infrastructure to help studio leads and pipeline engineers identify patterns in editor crashes or performance regressions across a large team of developers.

Practical Usage Tips and Best Practices
Detect Abnormal Shutdowns (Crashes)
This module is the primary way to determine if a developer’s previous session ended in a crash. By checking the WasLastSessionAbnormal state, you can trigger specific logic upon the next launch—such as a prompt to clear the cache—to eliminate persistent stability issues caused by corrupted local data.
Monitor Feature Adoption Rates
You can use this module to track how often specific editor tools are being utilized within your studio. This data allows you to eliminate support for unused internal plugins or prioritize bug fixes for the tools that your designers use most frequently.
Integrate with Studio Telemetry
In UE 5.6, pair this module with the Studio Telemetry plugin. By routing session events to a central dashboard (like Horde), you can eliminate the “silent” bugs that developers might not report, as the system automatically flags workstations experiencing frequent abnormal shutdowns.
Analyze Hardware-Specific Failures
The session data includes hardware and driver information. If a specific GPU driver version is causing an elimination of editor stability across your team, this module provides the data needed to identify the common denominator and issue a team-wide driver update.
Minimize Performance Overhead
The module is designed to be lightweight. It writes session metadata to small files on the local disk to ensure that the tracking itself does not eliminate editor performance. Avoid adding heavy, custom logic to the session-start delegates to keep the editor boot time fast.
Utilize Session IDs for Log Correlation
Every editor run is assigned a unique SessionID. Include this ID in your custom UE_LOG messages. This helps you eliminate confusion when searching through massive logs, as you can filter for all events associated with a single, specific editor session.
Respect Developer Privacy
If you are building custom analytics on top of this module, ensure you are only collecting data relevant to editor stability. By anonymizing PII (Personally Identifiable Information), you eliminate potential legal and ethical concerns regarding the tracking of employee activity.
Configure via Engine.ini
You can control the behavior of the analytics provider in the [Analytics] section of your DefaultEngine.ini. Properly configuring the APIKey and APIServer ensures that your session data is routed to your studio’s internal servers, helping you eliminate data silos.