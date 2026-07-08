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

nd managing the lifecycle of an Unreal Editor instance for telemetry and stability reporting.

Description

This module acts as the “black box” recorder for the Unreal Editor. It manages an Analytics Session, which starts when the editor launches and concludes when it is closed. Its primary purpose is to capture metadata about the editor’s state, such as project info, hardware specs, and plugin configurations. Crucially, it provides the logic for “Session Recovery” by detecting if the previous session ended unexpectedly. It serves as the foundation for Studio Telemetry and the Horde Analytics ecosystem, allowing studio leads to track editor stability and performance across a large team of developers.

Practical Usage Tips and Best Practices
1. Monitor Editor Stability Trends

The module tracks “Abnormal Shutdowns.” By piping this data into an analytics backend (like Horde), studio technical directors can identify if a specific engine version or a newly integrated plugin is causing a spike in crashes across the team. This allows for the proactive elimination of unstable tools before they impact project deadlines.

2. Utilize the Session ID for Log Correlation

Every time the editor starts, this module generates a unique SessionID. When debugging complex issues reported by team members, always correlate the SessionID found in the analytics data with the local Saved/Logs folder. This ensures you are looking at the exact log file corresponding to the reported telemetry event.

3. Configure via Studio Telemetry Plugin

In Unreal Engine 5.6⁄5.7, the EditorAnalyticsSession module is best managed through the Studio Telemetry plugin. Ensure this plugin is enabled in your .uproject file to allow the session data to be sent to your internal servers. You can configure the target endpoint in your DefaultEngine.ini under [StudioTelemetry.Provider.HordeAnalytics].

4. Respect Developer Privacy

By default, this module sends data to Epic Games (if opted-in). However, for internal studio use, you should configure it to send data only to your own infrastructure. A best practice is to ensure that no personally identifiable information (PII) is included in custom telemetry events to maintain a professional and compliant development environment.

5. Track Long-Running “Hung” Sessions

The module can help identify “Ghost” processes—instances of the editor that are stuck in memory but no longer visible. By analyzing session duration data, you can detect patterns where the editor fails to exit properly, helping you identify and target the elimination of deadlocked threads in your custom C++ code.

6. Leverage for Hardware Audits

Since the module records hardware configurations (CPU, GPU, RAM), you can use it to perform an automated audit of your team’s workstations. If certain developers are experiencing poor performance, the analytics session data can reveal if they are running on outdated drivers or insufficient hardware compared to the rest of the team.

7. Detect Feature Bottlenecks

You can send custom events through the session to see which editor features are used most frequently. If data shows that a specific custom tool is rarely touched, it might be a candidate for elimination or a complete redesign to improve developer efficiency.

8. Verify Connection to Zen Store

In modern versions of UE, the EditorAnalyticsSession often tracks connectivity to the Zen Store and DDC. If the session data shows frequent “DDC Cache Misses” or “Zen Connection Retries,” it is a signal that your local network infrastructure is bottlenecking the editor, necessitating an investigation into your server configurations.