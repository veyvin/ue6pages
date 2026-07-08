---
layout: default
title: AnalyticsLog
---

<!-- ai-generation-failed -->

<h1>AnalyticsLog</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Analytics/AnalyticsLog/AnalyticsLog.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

’s Analytics framework. It provides a local “File Logging” provider that captures and writes analytics events to the local disk in a human-readable JSON format rather than sending them to a remote server (like Flurry or Epic’s backend).

Its primary purpose is debugging and validation. It allows developers to verify that data—such as player progression, “elimination” events, or economy changes—is being correctly recorded and formatted before integrating a paid or external analytics service.

Practical Usage Tips and Best Practices
Configure via DefaultEngine.ini To enable the module, you must register it as your provider in your project configuration. This tells the engine to route all RecordEvent calls to the local file logger.
ini
	[Analytics]

	ProviderModuleName=FileLogging
Copy code
Locating Output Files The module saves data to your project’s folder under Saved/Analytics/. Files are generated with a .analytics extension and contain JSON objects. Use this to verify that event parameters (like EliminationSource or PlayerScore) are populating with the correct values.
Mandatory Module Dependency If you are triggering analytics via C++, ensure the AnalyticsLog module is available in your build environment. Add it to your Build.cs file, specifically for editor or development builds.
C++
	if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PrivateDependencyModuleNames.Add("AnalyticsLog");

	}
Copy code
Combine with Multicast for Parallel Testing You can use the AnalyticsMulticast provider to send data to both the FileLogging provider and a live backend simultaneously. This is ideal for cross-referencing local logs against the data that actually appears on your live dashboard.
ini
	[Analytics]

	ProviderModuleName=AnalyticsMulticast

	ProviderModuleNames=FileLogging,YourRemoteProvider
Copy code
Strictly Prevent Production Deployment The AnalyticsLog module writes to the disk frequently, which can cause performance degradation and storage bloat. Never include it in a released product. Use the [AnalyticsDevelopment] or [AnalyticsTest] ini sections to ensure it is only active during internal testing.
Validate “Elimination” Event Logic Use the logs to debug complex event sequences. For example, if you are tracking “elimination” counts, check the JSON log to ensure the EndSession call is triggered correctly when the game exits; otherwise, the events might not be finalized or written to the file.
Format Verification for Custom Data When sending custom structs or maps as event attributes, the AnalyticsLog module is the fastest way to see how the engine serializes your data. It helps you catch “null” or “invalid” entries that would be harder to find once the data is hidden inside a remote database.
Use for Offline Development If your team is working without a consistent internet connection, the AnalyticsLog module allows you to continue developing and testing the data-gathering pipeline without needing to reach a remote API endpoint.