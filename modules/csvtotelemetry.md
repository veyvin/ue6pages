---
layout: default
title: CSVToTelemetry
---

<!-- ai-generation-failed -->

<h1>CSVToTelemetry</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/CSVTools/CSVToTelemetry/CSVToTelemetry.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnalyticsET, ApplicationCore, AssetRegistry, BuildSettings, CSVUtils, Core, CoreUObject, HTTP, Horde, Projects, RSA, StudioTelemetry, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

hich code change (CL) caused an increase in memory or a drop in FPS.
Dashboard Integration: Powering web-based dashboards (like those in Horde) to visualize project health for producers and leads.
Cross-Platform Comparison: Aggregating performance data from different hardware (PS5, Xbox, PC) into a single unified view.
Practical Usage Tips and Best Practices
1. Run as a Commandlet in CI/CD

The most common way to use this module is via the CSVToTelemetryCommandlet. Integrate this into your Build Farm’s post-test step to ensure that every automated playtest results in an immediate data upload:

bash
UnrealEditor-Cmd.exe MyProject -run=CSVToTelemetry -CSVFile="D:/Saved/Profiling/Test.csv" -TelemetryBackend="Horde"
Copy code
2. Inject Metadata with -csvMetadata

To make your telemetry data searchable, you must include context. Use the -csvMetadata command-line argument when running your game to bake info into the CSV. The telemetry module will then use these as “tags” (e.g., BuildType=Nightly, Map=Orion, Branch=Main). This is vital for the elimination of noise when filtering charts later.

3. Define Standard Stats in the Configuration

The module can be configured to only extract “KPIs” (Key Performance Indicators) rather than every single stat. Use the DefaultEngine.ini or specialized telemetry config files to specify which rows (like FrameTime, GCMarkTime, or TotalPhysicalMemory) should be promoted to the telemetry dashboard.

4. Use “Standardized” Capture Names

For consistent longitudinal data, ensure your CSV capture names are standardized. If one developer names a capture CombatTest and another names it Fight_01, the telemetry module will treat them as different data sets. Enforce a naming convention via your automation scripts.

5. Monitor for Performance Regressions

Pair the telemetry output with an alerting system. Many teams use the data pushed by this module to trigger “Regression Alerts.” If the AverageFPS drops by more than 5% compared to the 7-day rolling average, the system can automatically flag the relevant engineers.

6. Leverage the “Horde” Integration

If you are using Epic’s Horde for CI/CD, this module is pre-configured to work with it. By setting your APIServerET and APIKeyET in the [StudioTelemetry.Provider.HordeAnalytics] section of your config, the transition from local CSV to cloud-based chart becomes almost entirely automated.

7. Filter Outliers Before Upload

The module allows for basic filtering. If a test run ends prematurely (e.g., a crash or an accidental “eliminate” event for the player), avoid uploading that CSV. Validating the CSV integrity before calling the telemetry commandlet prevents skewed averages in your long-term data.

8. Combine with “CSVToSVG” for Local Reports

While CSVtoTelemetry is for long-term tracking, you can use its sister module, CSVToSVG, to generate instant visual reports for the same data. This allows developers to see an immediate graph of their local run before the data is archived into the global telemetry database.