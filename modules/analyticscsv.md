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

hat records telemetry data locally to comma-separated value (.csv) files. It is primarily used for debugging and local data analysis during development.

Description and Purpose

While most analytics providers (like Flurry or Epic’s internal tools) send data to remote servers, AnalyticsCSV redirects that same data to the project’s Saved/Analytics folder. It is an essential tool for developers who need to verify that their event-tracking logic is firing correctly without waiting for cloud dashboards to update. It provides a human-readable log of every event, attribute, and value sent through the IAnalyticsProvider interface.

Practical Usage Tips and Best Practices
Project Module Configuration
To use this provider in C++, you must include the module in your Build.cs file. It is recommended to wrap this in a developer-only check to keep the shipping executable lean:
C#
	if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PublicDependencyModuleNames.Add("AnalyticsCSV");

	}
Copy code
Configure via DefaultEngine.ini
To enable the CSV provider as your primary analytics engine, set it in your configuration files. This tells the engine to use the AnalyticsCSV module to handle all RecordEvent calls:
ini
	[Analytics]

	ProviderModuleName=AnalyticsCSV
Copy code
Use for Offline Logic Validation
Before integrating a paid third-party analytics service, use AnalyticsCSV to ensure your event parameters are being passed correctly. It is much easier to catch a typo in a local .csv file than it is to debug a missing data column on a web dashboard.
Track Elimination Events for Balance
Use the provider to log every player elimination. By recording the weapon type, location coordinates, and time-of-day in the CSV, you can import this data into Excel or Google Sheets to generate “heat maps” or weapon balance charts without needing a backend server.
Combine with Multicast Provider
You can use the AnalyticsMulticast module to send data to both a cloud provider and the CSV provider simultaneously. This allows you to monitor live data while maintaining a local backup for immediate debugging:
ini
	[Analytics]

	ProviderModuleName=AnalyticsMulticast

	ProviderModuleNames=FileLogging,AnalyticsCSV
Copy code
Monitor Performance impact
Writing to disk frequently can cause hitches. During profiling, ensure you are not recording an excessive number of events per frame. AnalyticsCSV is best suited for discrete events (like a match start or an elimination) rather than continuous per-tick data.
Check the Saved Directory
The generated files are stored in [ProjectName]/Saved/Analytics/. Each session typically generates a new file with a unique timestamp. Remember to clear this folder periodically, as these files can accumulate and take up significant disk space over long development cycles.
Exclude from Shipping Builds
The AnalyticsCSV module is intended for internal testing. Always ensure that you use the Analytics system’s built-in functionality to disable this provider in your Shipping configuration to prevent users from seeing internal telemetry logs and to eliminate unnecessary file I/O overhead.