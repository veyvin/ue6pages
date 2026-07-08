---
layout: default
title: AnalyticsET
---

<!-- ai-generation-failed -->

<h1>AnalyticsET</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Analytics/AnalyticsET/AnalyticsET.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core, HTTP, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

of Unreal Engine’s generic Analytics interface. While the base Analytics module provides the abstract framework, AnalyticsET is the concrete “worker” that handles the actual HTTP transmission, JSON formatting, and buffering of data to a REST-based telemetry server.

What it is and What it’s used for

It is specifically designed to communicate with custom data pipelines or the Epic Horde server. Unlike third-party analytics plugins, this module allows studios to maintain full ownership of their data by pointing it to their own infrastructure.

Primary uses include:

Studio Telemetry: Tracking editor-side metrics like cook times, shader compilation speed, and asset load times to improve developer efficiency.
Dev-Ops Monitoring: Using the Horde dashboard to visualize performance regressions across different builds.
Custom Game Analytics: Sending gameplay events (like player progression or when a character is eliminated) to a private studio database.
Practical Usage Tips and Best Practices
1. Configuration via DefaultEngine.ini

Most of the setup is handled through configuration files rather than code. You must define the provider and endpoint in your project’s DefaultEngine.ini to let the module know where to send data:

ini
	[Analytics]

	ProviderModuleName=AnalyticsET

	 

	[AnalyticsET]

	APIServerET="http://your-analytics-server.com/"

	APIKeyET="YourUniqueProjectKey"

	APIEndpointET="api/v1/events"

	```

	 

	#### 2. Module Dependency Setup

	To use this in C++, you must include both the interface and the implementation modules in your `*.Build.cs`. Because analytics is often used for debugging/telemetry, it's common to keep it as a private dependency:

	```cpp

	// YourProject.Build.cs

	PrivateDependencyModuleNames.AddRange(new string[] { "Analytics", "AnalyticsET" });

	```

	 

	#### 3. Accessing the Provider in C++

	Always access the module through the `IAnalyticsModule` interface. This ensures that if you change providers later, your gameplay code doesn't break.

	```cpp

	#include "Interfaces/IAnalyticsProvider.h"

	#include "Analytics.h"

	 

	// Get the default provider (configured in .ini)

	TSharedPtr<IAnalyticsProvider> Provider = FAnalytics::Get().GetDefaultConfiguredProvider();

	if (Provider.IsValid())

	{

	    Provider->RecordEvent(TEXT("PlayerDeath"), { FAnalyticsEventAttribute(TEXT("Reason"), TEXT("Lava")) });

	}

	```

	 

	#### 4. Batching and Buffering

	`AnalyticsET` handles event buffering automatically to prevent saturating the network. However, you should avoid firing events in a `Tick()` function. For high-frequency data (like player position), aggregate the data into a single "Summary" event every 30-60 seconds rather than sending 60 events per second.

	 

	#### 5. Use Attributes for Context

	Don't create separate event names for every minor variation (e.g., `Level1_Start`, `Level2_Start`). Instead, use a generic event name like `LevelStatus` and use `FAnalyticsEventAttribute` to provide the context:

	```cpp

	TArray<FAnalyticsEventAttribute> Attributes;

	Attributes.Add(FAnalyticsEventAttribute(TEXT("LevelName"), TEXT("Map_Canyon")));

	Attributes.Add(FAnalyticsEventAttribute(TEXT("Status"), TEXT("Started")));

	Provider->RecordEvent(TEXT("LevelStatus"), Attributes);

	```

	 

	#### 6. Privacy and GDPR Compliance

	Since `AnalyticsET` sends data to your own server, you are responsible for data privacy. Always check a "User Consent" boolean (stored in your `USaveGame`) before calling `StartSession()`. If the user opts out, do not initialize the provider.

	 

	#### 7. Handling Session Lifecycle

	Call `StartSession()` when the game or editor starts and `EndSession()` on exit. `AnalyticsET` uses these calls to generate unique Session IDs, which are critical for your backend to stitch together a sequence of events from a single user.

	 

	#### 8. Verify with "stat analytics"

	Use the console command `stat analytics` while the game is running. This provides a real-time overlay showing how many events are currently buffered and how many have been successfully uploaded. If the "Buffer" count keeps rising without decreasing, your `APIServerET` URL is likely incorrect or your server is unreachable.
Copy code
2. Module Dependency Setup

To use this module in C++, you must include both the interface and the implementation in your *.Build.cs. Since telemetry is often a developer tool, it is frequently kept as a private dependency:

C++
	// YourProject.Build.cs

	PrivateDependencyModuleNames.AddRange(new string[] { "Analytics", "AnalyticsET" });
Copy code
3. Access via the IAnalyticsProvider Interface

Avoid hard-coding references to AnalyticsET classes. Instead, use the IAnalyticsModule to get a generic provider. This ensures that if you switch from a private server to a different backend later, your gameplay logic remains unchanged:

C++
	#include "Interfaces/IAnalyticsProvider.h"

	#include "Analytics.h"

	 

	TSharedPtr<IAnalyticsProvider> Provider = FAnalytics::Get().GetDefaultConfiguredProvider();

	if (Provider.IsValid())

	{

	    Provider->RecordEvent(TEXT("EditorToolUsed"), { FAnalyticsEventAttribute(TEXT("ToolName"), TEXT("PCG_Graph_Alpha")) });

	}
Copy code
4. Leverage Built-in Studio Telemetry

In UE 5.5 and later, the Studio Telemetry plugin uses AnalyticsET by default. Before writing custom events, check if the engine is already tracking what you need (e.g., Zen DDC efficiency or UBT compilation times) to eliminate redundant data collection.

5. Efficient Event Attributes

Don’t create a unique event name for every minor variation. Use generic event names and distinguish them using attributes. This makes filtering and aggregation much easier in your backend dashboard:

C++
	TArray<FAnalyticsEventAttribute> Attrs;

	Attrs.Add(FAnalyticsEventAttribute(TEXT("MapName"), TEXT("Canyon_P")));

	Attrs.Add(FAnalyticsEventAttribute(TEXT("Outcome"), TEXT("Eliminated")));

	Provider->RecordEvent(TEXT("MatchResult"), Attrs);
Copy code
6. Use “stat analytics” for Debugging

If you suspect data isn’t reaching your server, use the console command stat analytics. This displays a real-time overlay showing the number of events currently in the buffer and how many have failed to upload. If the buffer never clears, check your APIServerET URL.

7. Handle Session Lifecycles

The module generates a unique Session ID when StartSession() is called. Ensure your game calls EndSession() when shutting down or returning to the main menu. This allows your backend to accurately group events belonging to a single play session.

8. Privacy and Anonymization

When sending data to a private server, ensure you are not sending PII (Personally Identifiable Information). By default, the engine attempts to anonymize IDs, but you should verify that your attribute values (like machine names or user handles) comply with your studio’s data privacy policies.