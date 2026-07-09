---
layout: default
title: AnalyticsCSV
---

<!-- ai-generation-failed -->

<h1>AnalyticsCSV</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Analytics/AnalyticsCSV/AnalyticsCSV.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ngine. Unlike cloud-based providers (such as Flurry or Apsalar), it records analytics events and attributes directly to a Comma-Separated Values (CSV) file on the local machine. It is primarily used during development and QA to verify that analytics events are firing correctly, with the proper data payloads, without requiring a live backend or internet connection.

Practical Usage Tips & Best Practices
1. Enable via DefaultEngine.ini

To use this module as your primary analytics provider for testing, you must configure it in your project’s configuration files. This directs the FAnalytics system to route all calls to the CSV writer.

ini
	[Analytics]

	ProviderModuleName=AnalyticsCSV
Copy code
2. Locate Output Files in Saved/Analytics

By default, the module writes its output to the Saved/Analytics folder within your project directory. Each session generates a unique file ending in .analytics or .csv.

Best Practice: Check these files after a playtest to ensure that custom events (like the elimination of an enemy) recorded the expected coordinates and player stats.
3. Restrict to Non-Shipping Builds

Writing to local disk on every event can cause performance overhead and unnecessary disk wear on player hardware. Ensure the module is only active during development by using the [AnalyticsDevelopment] category in your .ini files. Avoid including this module in your final distribution to prevent data bloat on the end-user’s device.

4. Add Module Dependency in Build.cs

If you need to interface with the CSV provider directly via C++ (e.g., to manually flush the buffer or change the file path), you must add the module to your dependencies.

C#
	// MyProject.Build.cs

	if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PrivateDependencyModuleNames.Add("AnalyticsCSV");

	}
Copy code
5. Verify Event Payloads for “Elimination” Logic

When tracking gameplay events, use the CSV output to debug complex logic. For example, if you log an event when a player undergoes elimination, verify that the FAnalyticsEventAttribute array contains the correct “AttackerID” and “WeaponUsed” keys in the resulting CSV row.

6. Use with Multicast for Parallel Testing

If you are already using a live cloud provider but want local logs for immediate debugging, combine AnalyticsCSV with the AnalyticsMulticast module. This allows the engine to send data to the cloud while simultaneously recording it to a local CSV file for your review.

7. Monitor Performance with Heavy Logging

Because this module performs file I/O, firing hundreds of events per frame (such as every bullet impact) can lead to “hitchiness” or frame rate drops.

Tip: Only log high-level gameplay milestones (level start, level end, player elimination, or shop purchases) when using the CSV provider to maintain a smooth testing environment.
8. Use CSV Tools for Data Analysis

Since the output is standard CSV format, you can import the resulting files into Excel, Google Sheets, or specialized data visualization tools. This is highly effective for balancing game difficulty by visualizing where most player eliminations occur across multiple local test sessions.