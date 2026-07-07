---
layout: default
title: Analytics
---

<!-- ai-generation-failed -->

<h1>Analytics</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Analytics/Analytics/Analytics.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nd transmitting telemetry, player behavior, and game performance data. It provides a provider-agnostic abstraction layer, allowing you to write a single set of instrumentation logic that can be routed to various backends (such as a local file, a custom database, or third-party services) via simple configuration changes.

This module is primarily used for tracking player retention, economy balancing, level difficulty heatmaps, and monitoring technical health across different build configurations.

Practical Usage Tips and Best Practices
1. Configure Module Dependencies

To utilize analytics in C++, you must add the module to your project’s Build.cs file. For most implementations, you will also want the AnalyticsET (Event Tracking) module for standard attribute handling.

C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "Analytics", "AnalyticsET" });

	```

	 

	#### 2. Segregate Development and Production Data

	Never mix your internal testing data with real player data. Use the `[AnalyticsDevelopment]` and `[AnalyticsTest]` sections in your `.ini` files to point to different API keys or even different providers during development.

	 

	```ini

	[Analytics]

	ProviderModuleName=MyProductionProvider

	ApiKey=PROD_KEY_123

	 

	[AnalyticsDevelopment]

	ProviderModuleName=FileLogging

	; Logs to a local file instead of the cloud during dev

	```

	 

	#### 3. Use the Multicast Provider for Redundancy

	If you need to send data to multiple destinations (e.g., a custom database for game balance and a third-party service for marketing), use the `AnalyticsMulticast` module. It acts as a multiplexer that forwards a single `RecordEvent` call to multiple registered providers simultaneously.

	 

	#### 4. Batch Events with Attributes

	Avoid sending hundreds of individual events. Instead, use `RecordEventWithAttributes`. For example, instead of firing "PlayerJumped", "PlayerAttacked", and "PlayerDashed", fire a "CombatAction" event with an attribute string `ActionType`. This reduces network overhead and makes data visualization cleaner.

	 

	```cpp

	TArray<FAnalyticsEventAttribute> Attributes;

	Attributes.Add(FAnalyticsEventAttribute(TEXT("WeaponType"), TEXT("Sword")));

	Attributes.Add(FAnalyticsEventAttribute(TEXT("DamageDealt"), 45.0f));

	 

	FAnalytics::Get().GetDefaultConfiguredProvider()->RecordEvent(TEXT("PlayerAttack"), Attributes);

	```

	 

	#### 5. Leverage the Blueprint Analytics Plugin

	While the core logic is often C++, enable the **Blueprint Analytics Plugin** to allow game designers to instrument the game without programmer intervention. This provides "Record Event" nodes that automatically interface with your C++ configured provider.

	 

	#### 6. Mind the Privacy and PII (Personal Identifiable Information)

	Be extremely careful not to record PII (emails, real names, IP addresses) unless your analytics provider is GDPR/CCPA compliant and you have explicit player consent. Use the `UserId` field for an anonymous GUID rather than anything that can be traced back to a specific individual.

	 

	#### 7. Manually Flush on Critical State Changes

	Most providers buffer events to save battery and bandwidth. If your game is about to perform a high-risk operation (like a map transition or closing the application), call `FlushEvents()`. This ensures the cached data is sent to the server before the session terminates.

	 

	#### 8. Implement Session Heartbeats

	Don't just rely on `StartSession` and `EndSession`. If a game crashes, the `EndSession` call might never trigger, leading to "infinite" session length data. Fire a "Heartbeat" event every 5 minutes to accurately track active play time even in the event of a crash.
Copy code
2. Segregate Environments via INI Files

Never mix development testing data with live player data. Use the DefaultEngine.ini file to specify different providers or API keys for different build types using the [AnalyticsDevelopment], [AnalyticsTest], and [Analytics] (Production) headers.

3. Use the Multicast Provider

If you need to send data to multiple destinations simultaneously (e.g., a high-level dashboard and a raw data warehouse), use the AnalyticsMulticast provider. It acts as a multiplexer that forwards your single RecordEvent call to all registered sub-modules.

4. Batch Data with Attributes

Avoid firing hundreds of high-frequency “simple” events. Instead, use RecordEventWithAttributes to group related data. For example, instead of a “Jump” event, send a “CharacterAction” event with an attribute string for the action type and a float for the character’s current coordinates.

5. Track Elimination Events for Balance

Recording the elimination of players or NPCs is critical for difficulty balancing. Use analytics to track the location of an elimination, the weapon used, and the time elapsed since the start of the session. This helps identify “choke points” or overpowered equipment that disrupts gameplay.

6. Manually Flush on Critical Transitions

Most analytics providers buffer events to save bandwidth. To prevent data loss during a crash or an unexpected shutdown, call FlushEvents() during critical state changes, such as when a player completes a level or immediately before the application closes.

7. Implement Heartbeat Events

Relying solely on EndSession can result in lost data if the game process is terminated abruptly. Fire a “Heartbeat” event every few minutes; this allows you to reconstruct accurate session lengths even if a proper “End Session” event was never recorded due to a crash.

8. Leverage the Blueprint Analytics Plugin

Enable the Blueprint Analytics Plugin to empower designers to instrument the game. This provides a “Record Event” node that interfaces directly with the C++ backend you have configured, allowing for rapid iteration on what data needs to be collected without constant code changes.