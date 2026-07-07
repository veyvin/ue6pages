---
layout: default
title: AnalyticsHorde
---

<!-- ai-generation-failed -->

<h1>AnalyticsHorde</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Analytics/AnalyticsHorde/AnalyticsHorde.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, AnalyticsET, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

grate Unreal Engine’s internal analytics system with Horde, Epic Games’ distributed CI/CD and build automation platform. While standard analytics modules (like AnalyticsET) often target player behavior, AnalyticsHorde is specifically built for developer telemetry.

It is used to track and aggregate technical data from the Unreal Editor, Unreal Build Tool (UBT), and Unreal Automation Tool (UAT). This data allows teams to identify bottlenecks in developer workflows—such as slow map load times, shader compilation delays, or asset cooking hitches—by sending events directly to a Horde server for visualization and analysis.

1. Configuration via DefaultEngine.ini

To activate the module, you must configure the provider in your project’s configuration files. This tells the Studio Telemetry system to route its data through the Horde provider.

ini
	[StudioTelemetry.Provider.HordeAnalytics]

	Name=HordeAnalytics

	ProviderModule=AnalyticsET

	UsageType=EditorAndClient

	APIKeyET=HordeAnalytics.Dev

	APIServerET="http://your-horde-server-address:13340/"

	APIEndpointET="api/v1/telemetry/engine"
Copy code
2. Identify Workflow Bottlenecks

Use this module to track “Editor-to-PIE” (Play In Editor) times across your entire team. If a specific department is experiencing massive delays when starting a play session, the aggregated data in Horde will highlight the issue, allowing you to optimize those specific levels or blueprints and eliminate unproductive waiting time.

3. Monitor DDC and Shader Compilation

AnalyticsHorde is excellent for monitoring Derived Data Cache (DDC) hit rates. By analyzing the telemetry, you can see if developers are frequently missing the shared DDC and being forced to compile shaders locally. High miss rates indicate a need for DDC server maintenance or network optimization to prevent the elimination of team productivity.

4. Custom Event Annotation

Developers can add their own telemetry events to track project-specific metrics. You can use the IAnalyticsProvider interface to record how long custom build scripts or internal tools take to execute, helping you maintain a high-performance development pipeline.

5. Utilize Structured Logging

Horde excels at handling structured logs (JSON-based metadata). When sending data through AnalyticsHorde, ensure your events include relevant metadata (like branch name, machine spec, or engine version). This allows for much more powerful filtering in the Horde dashboard compared to simple string logs.

6. Set Up Telemetry Stores in globals.json

On the Horde server side, ensure you have configured a telemetryStore in your globals.json file. This is necessary to aggregate the incoming raw events from the AnalyticsHorde module into viewable metrics and charts. Without this configuration, the data is collected but never processed for display.

7. Performance Impact Minimization

Telemetry is generally sent asynchronously to avoid stalling the Editor. However, it is a best practice to avoid firing high-frequency events inside Tick functions. Frequent network requests can cause micro-stutters; instead, batch your data or fire events only at the start and completion of major tasks (e.g., “Begin Compile” and “End Compile”).

8. Use for UBA and UAT Tracking

Beyond the Editor, ensure your CI/CD build machines are utilizing this module via the Unreal Build Accelerator (UBA). Tracking the performance of your automated build farm through AnalyticsHorde helps identify which specific build steps are failing or slowing down, allowing you to eliminate inefficiencies in your release cycle.