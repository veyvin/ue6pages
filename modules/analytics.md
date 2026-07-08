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

smitting telemetry data from your game to an external backend. It provides a provider-agnostic interface (IAnalyticsProvider), which acts as a wrapper for various services like Firebase, Flurry, or custom internal solutions.

It is primarily used to track player behavior (e.g., level completion times, economy balance), monitor hardware performance across your user base, and gather “elimination” metrics to tune combat difficulty.

Practical Usage Tips and Best Practices
1. Add Module Dependencies

The Analytics module is not included in the default project template. You must manually add it to your [Project].Build.cs file to access the FAnalytics singleton and provider interfaces.

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "Analytics" });

	```

	 

	#### 2. Use the Singleton Safely

	Always access the analytics provider through the `FAnalytics` singleton. Because providers are often initialized asynchronously or might fail to load (e.g., no internet), you must verify the provider is valid before recording events.

	 

	```cpp

	#include "Analytics.h"

	#include "Interfaces/IAnalyticsProvider.h"

	 

	void UMyGameInstance::RecordGameStart()

	{

	    TSharedPtr<IAnalyticsProvider> Provider = FAnalytics::Get().GetDefaultConfiguredProvider();

	    if (Provider.IsValid())

	    {

	        Provider->StartSession();

	    }

	}

	```

	 

	#### 3. Batch Attributes for Efficiency

	Avoid sending multiple individual events for a single action. Instead, use `FAnalyticsEventAttribute` to send a single event with a collection of contextual metadata. This reduces network overhead and keeps your data structured.

	 

	```cpp

	TArray<FAnalyticsEventAttribute> Attributes;

	Attributes.Add(FAnalyticsEventAttribute(TEXT("WeaponName"), TEXT("PlasmaRifle")));

	Attributes.Add(FAnalyticsEventAttribute(TEXT("DamageType"), TEXT("Energy")));

	Attributes.Add(FAnalyticsEventAttribute(TEXT("EnemyLevel"), 15));

	 

	Provider->RecordEvent(TEXT("WeaponEquipped"), Attributes);

	```

	 

	#### 4. Distinguish Development vs. Production Data

	Use the `DefaultEngine.ini` file to specify different API keys for your `Development`, `Test`, and `Shipping` builds. This prevents internal playtest data from polluting your live production metrics.

	 

	```ini

	[Analytics]

	ProviderModuleName=MyCustomAnalyticsProvider

	ApiKey=ProductionKey_XYZ

	 

	[AnalyticsDevelopment]

	ApiKey=DevKey_123

	```

	 

	#### 5. Respect Data Privacy (GDPR/COPPA)

	Implement an "Opt-In/Opt-Out" toggle in your game's settings menu. Before calling `StartSession()`, check a saved user preference variable. If the user opts out, do not initialize the provider or call `RecordEvent`.

	 

	#### 6. Use "Flush" for Critical Data

	Analytics providers often buffer events locally to save battery/bandwidth. If an event is critical (e.g., a real-money purchase or a crash report), call `FlushEvents()` immediately after recording to force the provider to send the data to the server.

	 

	#### 7. Profile Telemetry Overhead

	While the Analytics module is lightweight, recording hundreds of events per second can impact frame time due to string formatting and memory allocation for attributes. Limit high-frequency logging (like "PlayerPosition") to specific sampling rates (e.g., once every 5 seconds).

	 

	#### 8. Leverage the Blueprint Library

	For designers, enable the **Analytics Blueprint Library** plugin. This provides a wrapper around the C++ module, allowing events to be fired from Character or Level Blueprints without writing custom C++ glue code for every new metric.
Copy code
2. Validate the Provider

Analytics providers are often initialized asynchronously or may fail if the user is offline. Always verify the provider is valid before attempting to record an event to prevent null pointer crashes.

C++
	TSharedPtr<IAnalyticsProvider> Provider = FAnalytics::Get().GetDefaultConfiguredProvider();

	if (Provider.IsValid())

	{

	    Provider->RecordEvent(TEXT("GameStarted"));

	}
Copy code
3. Use Attributes for Context

Avoid creating hundreds of unique event names. Instead, use a single event name and provide context through FAnalyticsEventAttribute. This makes data filtering much easier in your analytics dashboard.

C++
	TArray<FAnalyticsEventAttribute> Attributes;

	Attributes.Add(FAnalyticsEventAttribute(TEXT("MapName"), TEXT("Forest")));

	Attributes.Add(FAnalyticsEventAttribute(TEXT("Difficulty"), 3));

	Provider->RecordEvent(TEXT("Match_Start"), Attributes);
Copy code
4. Environment-Specific Keys

Use DefaultEngine.ini to define different API keys for your development and production environments. This ensures that developer testing and internal QA “elimination” data does not pollute your live production metrics.

ini
	[Analytics]

	ApiKey=Production_Key_123

	 

	[AnalyticsDevelopment]

	ApiKey=Dev_Key_ABC
Copy code
5. Batch and Flush Critical Data

Most providers buffer events locally to save bandwidth. For critical events that must be sent immediately (like a player completing a real-money transaction), call FlushEvents() to force an immediate upload to the server.

6. Respect Privacy and Opt-Outs

Before calling StartSession(), always check a user-controlled setting for data privacy (GDPR/COPPA). If a player opts out, you should avoid initializing the provider entirely or ensure no personal data is captured.

7. Track Elimination Events

To balance gameplay, record the cause and location of a player’s elimination. Tracking whether players are being eliminated by a specific boss or environmental hazard allows you to identify “difficulty spikes” that may cause player churn.

8. Use Blueprint Wrapper for Designers

If you have a non-technical team, enable the Analytics Blueprint Library plugin. This allows designers to fire analytics events directly from Blueprint logic without requiring a C++ programmer to expose every specific event trigger.