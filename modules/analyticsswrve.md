---
layout: default
title: AnalyticsSwrve
---

<!-- ai-generation-failed -->

<h1>AnalyticsSwrve</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Analytics/AnalyticsSwrve/AnalyticsSwrve.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core, HTTP, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

l Engine that implements the IAnalyticsProvider interface specifically for the Swrve platform. Swrve is a real-time mobile marketing and customer experience platform used heavily in live-service mobile games.

This module acts as the “glue” that translates Unreal’s generic analytics calls into Swrve-specific REST API requests, allowing developers to handle player segmentation, A/B testing, and in-app messaging.

Practical Usage Tips and Best Practices
1. Configure for Editor and Target Platforms

Because Swrve is primarily a mobile/live-service tool, wrap your module dependency in your [Project].Build.cs to ensure it only compiles for relevant platforms, preventing unnecessary overhead in dedicated server builds.

C#
	// MyProject.Build.cs

	if (Target.Type == TargetType.Editor || Target.Platform == UnrealTargetPlatform.IOS || Target.Platform == UnrealTargetPlatform.Android)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "Analytics", "AnalyticsSwrve" });

	}

	```

	 

	#### 2. Register the Provider in INI

	Instead of hardcoding provider names in C++, set the `ProviderModuleName` in your `DefaultEngine.ini`. This allows the engine's `FAnalytics` singleton to automatically instantiate the Swrve provider.

	 

	```ini

	[Analytics]

	ProviderModuleName=AnalyticsSwrve

	AppId=1234

	ApiKey=your_production_api_key

	UserId=optional_custom_id_logic

	```

	 

	#### 3. Define Environment-Specific Keys

	Swrve requires separate App IDs and API Keys for "Sandbox" vs "Production" environments. Use Unreal’s config hierarchy to ensure development data doesn't pollute your live metrics.

	 

	```ini

	; Use this for internal testing

	[AnalyticsDevelopment]

	AppId=5678

	ApiKey=your_sandbox_api_key

	 

	; Use this for shipping builds

	[Analytics]

	AppId=1234

	ApiKey=your_production_api_key

	```

	 

	#### 4. Code Against the Interface

	Avoid casting directly to `FAnalyticsSwrve`. Always interact with the analytics system through the `IAnalyticsProvider` interface. This makes it trivial to swap Swrve for another provider (like Firebase or Flurry) later without changing your gameplay code.

	 

	```cpp

	#include "Runtime/Analytics/Analytics/Public/Interfaces/IAnalyticsProvider.h"

	#include "Runtime/Analytics/Analytics/Public/Analytics.h"

	 

	TSharedPtr<IAnalyticsProvider> Provider = FAnalytics::Get().GetDefaultConfiguredProvider();

	if (Provider.IsValid())

	{

	    Provider->RecordEvent(TEXT("LevelStarted"), { FAnalyticsEventAttribute(TEXT("LevelName"), TEXT("Ocean_01")) });

	}

	```

	 

	#### 5. Map "Elimination" to Custom Events

	In Swrve, tracking how and where a player was eliminated is critical for balancing. Use detailed attributes to capture the `EliminatorID`, `WeaponUsed`, and `MapCoordinates`. This allows you to create "Heatmaps" or "Churn Funnels" within the Swrve dashboard.

	 

	#### 6. Leverage User Attributes

	Swrve excels at user segmentation. Use `SetUserAttribute` to store persistent data such as "PlayerClass," "TotalSpend," or "CurrentLeague." This enables you to send targeted push notifications or in-game messages only to specific groups (e.g., "All players in League 5 who haven't played in 3 days").

	 

	#### 7. Track Virtual Economy

	Use the specialized `RecordItemPurchase` and `RecordCurrencyPurchase` methods. Swrve has dedicated reporting for "Sinks and Sources," allowing you to see if you are giving away too much virtual currency or if your shop prices are too high for the average player.

	 

	#### 8. Manual Flush for Critical Events

	Swrve often buffers events to save battery and bandwidth. For critical events—such as completing a tutorial or a major "elimination" milestone—call `FlushEvents()` to ensure the data is sent immediately before the app is potentially closed.

	 

	```cpp

	Provider->RecordEvent(TEXT("TutorialComplete"));

	Provider->FlushEvents(); // Force immediate upload
Copy code
2. Segregate Sandbox and Production Data

Swrve requires different App IDs and API Keys for testing. Use the [AnalyticsDevelopment] and [Analytics] sections in your DefaultEngine.ini to ensure that data from your internal “elimination” tests doesn’t skew your live production metrics.

3. Use SetUserAttribute for Segmentation

Swrve’s power lies in its ability to target specific player groups. Use SetUserAttribute to track persistent traits like PlayerClass, TotalCurrencyEarned, or CurrentLeague. This allows you to send targeted in-app rewards to players in a specific league who haven’t played in 24 hours.

4. Instrument Elimination Metrics

To optimize player retention, record an event every time a player reaches an elimination state. Include attributes like EliminatorID, LocationX/Y/Z, and TimeInSession. Analyzing where players are frequently eliminated helps identify frustrating level design or balance issues.

5. Track Economy via Specialized Calls

Avoid using generic RecordEvent for purchases. Use Swrve’s specific RecordCurrencyPurchase and RecordItemPurchase functions. This enables Swrve’s specialized “Economy” dashboards, which automatically calculate virtual currency sinks and sources for you.

6. Leverage Blueprint Analytics Library

Instead of writing custom C++ wrappers for every trigger, enable the Analytics Blueprint Library plugin. This allows designers to place Swrve event nodes directly in gameplay Blueprints, significantly speeding up the instrumentation process.

7. Handle Session Start/End Manually

For mobile games, accurately tracking “App to Foreground” and “App to Background” is vital. Ensure your GameMode or GameInstance explicitly calls StartSession and EndSession to give Swrve accurate data on player session lengths and daily active users (DAU).

8. Verify Provider Validity

Before firing events, always ensure the Swrve provider is properly initialized. If the API key is missing or the network is unavailable during the first boot, the provider might be null.

C++
	TSharedPtr<IAnalyticsProvider> SwrveProvider = FAnalytics::Get().GetDefaultConfiguredProvider();

	if (SwrveProvider.IsValid())

	{

	    SwrveProvider->RecordEvent(TEXT("TutorialComplete"));

	}
Copy code