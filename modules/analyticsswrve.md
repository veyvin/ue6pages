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

Engine Analytics API that integrates the Swrve platform into your project. Swrve is a comprehensive suite used primarily in mobile and live-service games for real-time telemetry, A/B testing, and targeted player engagement.

This module acts as the “bridge” that translates Unreal’s generic analytics calls into Swrve-specific data packets, enabling developers to track user behavior and manage live operations without writing platform-specific network code.

Practical Usage Tips and Best Practices
1. Add Platform-Specific Dependencies

Since Swrve is primarily used for mobile platforms (iOS and Android), wrap your module dependencies in your Build.cs to avoid including unnecessary bloat in desktop-only builds.

C#
	// In YourProject.Build.cs

	if (Target.Platform == UnrealTargetPlatform.IOS || Target.Platform == UnrealTargetPlatform.Android)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "Analytics", "AnalyticsSwrve" });

	}

	```

	 

	#### 2. Configure via DefaultEngine.ini

	The module automatically looks for specific keys in your project settings. Avoid hard-coding your API keys; instead, use the `[Analytics]` category.

	```ini

	[Analytics]

	ProviderModuleName=AnalyticsSwrve

	; Replace with your actual Swrve App ID and API Key

	AppID=1234

	ApiKey=abc123yourkeyhere

	; Optional: Flush interval in seconds

	SendInterval=60

	 

	[AnalyticsDevelopment]

	AppID=5678

	ApiKey=dev_key_here

	```

	 

	#### 3. Use the Generic Interface

	Always interact with the analytics system via the `FAnalytics` singleton rather than referencing `FAnalyticsSwrve` directly. This keeps your code portable if you ever switch providers.

	```cpp

	#include "Analytics.h"

	#include "Interfaces/IAnalyticsProvider.h"

	 

	// Record a purchase event

	TArray<FAnalyticsEventAttribute> Attributes;

	Attributes.Add(FAnalyticsEventAttribute(TEXT("ItemID"), TEXT("Gold_Pack_01")));

	Attributes.Add(FAnalyticsEventAttribute(TEXT("Price"), 4.99f));

	 

	FAnalytics::Get().GetDefaultConfiguredProvider()->RecordEvent(TEXT("StorePurchase"), Attributes);

	```

	 

	#### 4. Leverage User Identification

	Swrve relies heavily on unique user IDs for its "Live-ops" features. Use `SetUserID` as soon as the player logs in (e.g., via PlayFab, Steam, or Game Center) to ensure that A/B testing and push notifications are correctly targeted to that specific user.

	 

	#### 5. Track Critical "Elimination" and Churn Points

	In mobile games, understanding where players quit is vital. Record an event whenever a player is **eliminated** in a way that ends their session (e.g., "GameOver") and include attributes like `LevelID`, `CurrentScore`, and `RevivesUsed`. This data allows you to use Swrve’s dashboard to find difficulty spikes that cause players to leave.

	 

	#### 6. Coordinate with A/B Testing

	The Swrve provider supports "User Properties." Use `SetUserProperty` to flag players into different buckets. While Swrve can do this automatically on its backend, manually tagging users (e.g., `UserType: Whale` or `SkillLevel: Pro`) allows you to run different experiment variations through the Swrve dashboard without changing game code.

	 

	#### 7. Handle Backgrounding on Mobile

	Since Swrve is primarily used on mobile, ensure your session logic handles app backgrounding. Use the `FCoreDelegates::ApplicationWillDeactivateDelegate` to call `EndSession()`. Swrve's SDK usually handles some of this, but explicit calls ensure data integrity during unexpected app closures.

	 

	#### 8. Use Batching for Performance

	Swrve (and most mobile analytics) has limits on how many events you can send per second. Group multiple related data points into a single `RecordEventWithAttributes` call instead of firing five separate `RecordEvent` calls. This reduces CPU overhead and ensures your network buffer doesn't overflow during intense gameplay.
Copy code
2. Centralize Keys in DefaultEngine.ini

The module is designed to read your App ID and API Key directly from your project configuration. This allows you to easily swap between development and production environments without changing C++ code.

ini
	[Analytics]

	ProviderModuleName=AnalyticsSwrve

	AppID=1234

	ApiKey=your_production_key

	 

	[AnalyticsDevelopment]

	AppID=5678

	ApiKey=your_sandbox_key
Copy code
3. Set User IDs for Cross-Platform Tracking

Swrve’s strength lies in tracking individual user journeys. As soon as a player logs into your backend (e.g., Epic Online Services or PlayFab), call SetUserID on the provider. This ensures that data remains consistent if a player switches devices.

4. Monitor Elimination Data for Churn Analysis

To improve player retention, record a detailed event every time a player is eliminated. Use attributes to track the cause of elimination, the current level, and the player’s currency balance. Swrve can then use this data to trigger “come back” push notifications or gift the player items to help them progress.

5. Leverage User Properties for Segmentation

Use SetUserProperty to tag players based on their behavior (e.g., “FrequentBuyer,” “ProExplorer,” or “TutorialComplete”). These properties allow you to create specific “segments” in the Swrve dashboard for targeted A/B tests or specialized in-game messaging.

6. Use Timed Events for Performance

If you are tracking how long a specific task takes (like loading a level or completing a boss fight), use the RecordEvent interface to mark the start and end. Swrve can calculate the duration, helping you identify technical bottlenecks or design flaws that frustrate players.

7. Handle App Backgrounding

Mobile sessions can be interrupted by phone calls or the user switching apps. Ensure your game logic calls EndSession when the application deactivates and StartSession when it returns to the foreground to maintain accurate session length metrics.

8. Batch Attributes to Optimize Bandwidth

To minimize the impact on mobile data plans and CPU performance, avoid sending multiple individual events in a single frame. Combine related data into a single RecordEventWithAttributes call to reduce the number of HTTP requests sent to the Swrve collectors.