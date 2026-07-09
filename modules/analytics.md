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

ding telemetry and player behavior data. Rather than binding your game logic directly to a specific service (like Flurry, Google Analytics, or a custom backend), you write code against the IAnalyticsProvider interface. This allows you to swap or multicast to different analytics backends purely through configuration without changing your C++ code.

It is primarily used for Player Retention tracking, Economy monitoring (virtual currency spending), Level progression analysis, and Crash/Error reporting.

1. Module Configuration

To use the analytics system in C++, you must add the module to your Build.cs file. If you are using the common Epic-provided web-backend implementation, you may also need AnalyticsET.

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "Analytics" });

	 

	// If using the standard Epic event telemetry provider:

	PrivateDependencyModuleNames.Add("AnalyticsET");

	```

	 

	---

	 

	### 2. Practical Usage Tips & Best Practices

	 

	#### Interface-Driven Implementation

	Always access the system through `FAnalytics::Get().GetDefaultConfiguredProvider()`. Never instantiate a specific provider class (like `FAnalyticsFlurry`) directly in your game logic. This ensures that if you change providers in your `.ini` file, your code remains functional and "elimination" of a specific service doesn't break the build.

	 

	#### Manage Sessions via GameInstance

	Start your analytics session in `StartGameInstance()` and end it in `Shutdown()`. This provides a clean "Session Duration" metric. For mobile games, you should also hook into `ApplicationWillEnterBackgroundDelegate` and `ApplicationHasEnteredForegroundDelegate` to pause/resume sessions when the user minimizes the app.

	 

	#### Use Structured Attributes

	Avoid sending dozens of individual events for a single action. Instead, use `FAnalyticsEventAttribute` to send one event with multiple parameters. 

	*   **Tip:** When recording a "LevelEnd" event, include attributes for `TimeTaken`, `FinalHealth`, `EnemiesKilled`, and `Outcome`. This makes data visualization and filtering significantly more powerful than individual "EnemyKilled" pings.

	 

	#### Leverage Environment-Specific Configs

	Use the `DefaultEngine.ini` hierarchy to separate your development data from production data. You can define `[AnalyticsDevelopment]` and `[AnalyticsRelease]` sections to point to different API keys. This prevents your local testing and QA sessions from polluting your actual player retention and monetization metrics.

	 

	#### Batch and Flush Strategically

	Analytics events are usually cached locally and sent in batches to save bandwidth and battery. However, critical events (like a successful In-App Purchase or a crash) should be followed by `FlushEvents()`. This forces the provider to send the data immediately, ensuring high-priority information isn't lost if the app closes unexpectedly.

	 

	#### Sanitize and Standardize Keys

	Establish a strict naming convention for your events (e.g., `Category.Action.Detail`). Because different providers have different restrictions on special characters and string lengths, sticking to a `PascalCase` or `snake_case` format across your entire C++ codebase prevents "broken" strings that some backends might reject.

	 

	#### Performance: Avoid Ticking Logs

	Never record analytics events inside a `Tick()` function or high-frequency loops. Analytics calls involve string construction and memory allocation. Even if the provider is asynchronous, the overhead of creating `TArray<FAnalyticsEventAttribute>` thousands of times will cause frame drops. Instead, aggregate data and send a single summary event at logical breakpoints (e.g., every 5 minutes or at the end of a combat encounter).

	 

	#### Use the Blueprint Bridge for UX

	While core systems should be C++, use the **Blueprint Analytics Plugin** to allow designers to track UX-specific interactions (like "Clicked Tutorial Button"). This keeps your C++ code clean of UI-specific "clutter" while still funneling all data through the same unified `IAnalyticsProvider` you configured in native code.
Copy code
2. Practical Usage Tips & Best Practices
Interface-Driven Implementation

Always access the system through FAnalytics::Get().GetDefaultConfiguredProvider(). Never instantiate a specific provider class directly in your game logic. This ensures that if you change providers in your .ini file, your code remains functional and the “elimination” of a specific service doesn’t break the build.

Manage Sessions via GameInstance

Start your analytics session in StartGameInstance() and end it in Shutdown(). This provides a clean “Session Duration” metric. For mobile games, you should also hook into application lifecycle delegates to pause or resume sessions when the user minimizes the app.

Use Structured Attributes

Avoid sending dozens of individual events for a single action. Instead, use FAnalyticsEventAttribute to send one event with multiple parameters.

Tip: When recording an event for player “elimination,” include attributes for DamagerType, Location, and ActiveWeapon. This is significantly more powerful for data visualization than a simple event count.
Leverage Environment-Specific Configs

Use the DefaultEngine.ini hierarchy to separate your development data from production data. You can define [AnalyticsDevelopment] and [AnalyticsRelease] sections to point to different API keys. This prevents your local testing and QA sessions from polluting your actual player metrics.

Batch and Flush Strategically

Analytics events are usually cached locally and sent in batches to save bandwidth and battery. However, critical events (like a successful store purchase) should be followed by FlushEvents(). This forces the provider to send the data immediately, ensuring high-priority information isn’t lost if the app closes unexpectedly.

Sanitize and Standardize Keys

Establish a strict naming convention for your events (e.g., Category.Action.Detail). Because different providers have different restrictions on special characters and string lengths, sticking to a consistent format across your entire C++ codebase prevents “broken” strings that some backends might reject.

Performance: Avoid Ticking Logs

Never record analytics events inside a Tick() function or high-frequency loops. Analytics calls involve string construction and memory allocation. Even if the provider is asynchronous, the overhead of creating attribute arrays thousands of times will cause performance degradation. Aggregate data and send a summary event at logical breakpoints.

Use the Blueprint Bridge for UX

While core systems should be C++, use the Blueprint Analytics Plugin to allow designers to track UX-specific interactions (like clicking a specific UI button). This keeps your C++ code clean of UI-specific clutter while still funneling all data through the same unified provider.