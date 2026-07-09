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

IAnalyticsProvider interface designed to integrate with the Swrve mobile marketing and analytics platform. While the base Analytics module provides the abstract framework, AnalyticsSwrve handles the specific communication protocols, event batching, and data formatting required by Swrve’s servers.

It is primarily used in live-service mobile games to track real-time player behavior, trigger in-app messages (IAM), manage A/B testing, and monitor virtual economies through Swrve’s dashboard.

1. Module Configuration

To enable Swrve, you must include the module in your project’s Build.cs. Since Swrve is primarily a mobile-focused service, it is common to wrap it in a platform check.

C#
	// MyProject.Build.cs

	if (Target.Platform == UnrealTargetPlatform.IOS || Target.Platform == UnrealTargetPlatform.Android)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "Analytics", "AnalyticsSwrve" });

	}

	```

	 

	In your `DefaultEngine.ini`, you must specify the provider and your Swrve credentials:

	 

	```ini

	[Analytics]

	ProviderModuleName=AnalyticsSwrve

	 

	[Swrve]

	AppId=1234

	ApiKey=your_swrve_api_key

	UserId=Player_001

	AppVersion=1.0.0

	```

	 

	### 2. Practical Usage Tips & Best Practices

	 

	#### Use the Multicast Provider for Redundancy

	Swrve is excellent for marketing, but you might also want raw logs in a file or another service (like Flurry). Use the `AnalyticsMulticast` module as your primary provider, then list `AnalyticsSwrve` as one of the children. This ensures that a failure in one service's SDK doesn't "eliminate" your entire data pipeline.

	 

	#### Align User IDs Early

	Swrve relies heavily on unique User IDs to track the "Player Journey." Ensure you set the `UserId` via configuration or C++ (`SetUserId`) *before* calling `StartSession()`. If the ID changes mid-session, Swrve may treat it as a new user, fragmenting your retention data.

	 

	#### Implement the "Swrve Talk" Trigger Pattern

	Swrve is unique because it supports "Swrve Talk" (In-App Messaging). When recording events in C++, use naming conventions that your marketing team can hook into. 

	*   **Tip:** When a player reaches a specific milestone, record an event like `Level.Completed.05`. This can be used as a trigger on the Swrve dashboard to show a "Congratulations" popup without writing additional C++ UI code.

	 

	#### Track Virtual Economy "Resource" Events

	Swrve has dedicated logic for tracking currency. Instead of generic `RecordEvent`, use `RecordItemPurchase` and `RecordCurrencyPurchase`. This allows Swrve to generate specialized "Sink and Source" reports, helping you identify if you are "eliminating" too much currency from the economy or if players are hoarding it.

	 

	#### Handle Background/Foreground Transitions

	On mobile, the OS can kill the app process at any time. Ensure you call `EndSession()` when the application moves to the background (via `FCoreDelegates::ApplicationWillEnterBackgroundDelegate`). Swrve batches events; failing to end the session properly can result in data loss for that session.

	 

	#### Sanitize Swrve Attribute Keys

	Swrve's backend is sensitive to specific characters in keys. Stick to alphanumeric characters and underscores. Avoid spaces or dots in your `FAnalyticsEventAttribute` names (e.g., use `enemy_type` instead of `Enemy Type`). This prevents "silent failures" where the event is recorded but the attributes are missing in the dashboard.

	 

	#### Leverage App Versioning for A/B Testing

	Always populate the `AppVersion` field in your config. Swrve allows you to filter data and trigger different campaigns based on the version. This is critical when you are testing new balance changes in a "Soft Launch" phase and want to compare the behavior of players on version `1.1.0` vs `1.0.0`.

	 

	#### Use FlushEvents for High-Value Transactions

	While Swrve handles its own batching, you should manually call `FlushEvents()` immediately after a player makes a real-money purchase or completes a major tutorial step. This forces the SDK to "eliminate" the local cache and send the data to the server immediately, minimizing the risk of losing high-value conversion data due to a crash.
Copy code

In your DefaultEngine.ini, configure the provider and your credentials:

ini
	[Analytics]

	ProviderModuleName=AnalyticsSwrve

	 

	[Swrve]

	AppId=1234

	ApiKey=your_swrve_api_key

	AppVersion=1.0.0
Copy code
2. Practical Usage Tips & Best Practices
Establish a Unique UserId Early

Swrve relies heavily on a consistent UserId to track the player journey. Ensure you set the User ID (via SetUserId) before calling StartSession(). If a player is “eliminated” from a guest account and logs into a permanent one, handle the ID transition carefully to avoid fragmenting retention data in the Swrve dashboard.

Utilize the Multicast Provider

It is common practice to use the AnalyticsMulticast module as the primary provider. By listing AnalyticsSwrve as one of the child modules in your configuration, you can send data to Swrve for marketing triggers while simultaneously sending raw data to a secondary logging service or a file for internal analysis.

Map Events for In-App Messaging (IAM)

Swrve allows marketing teams to trigger popups and offers based on event names. Work with your designers to standardize C++ event strings (e.g., Tutorial.Step.01). When the event is recorded, Swrve can automatically trigger a message without requiring further code changes to the UI.

Track Virtual Economy Sinks and Sources

Swrve has specialized logic for virtual currency. Instead of using generic RecordEvent calls, use the specific RecordItemPurchase and RecordCurrencyPurchase methods. This allows the Swrve dashboard to generate “Economy” reports that show where players are gaining or “eliminating” currency.

Manage Application Lifecycle Delegates

Mobile operating systems may suspend or kill the app process frequently. Use FCoreDelegates::ApplicationWillEnterBackgroundDelegate to call EndSession(). This ensures Swrve has a chance to flush the current event buffer, preventing data loss when the application is closed.

Use FlushEvents for High-Value Transactions

While the SDK batches events to save battery, you should manually call FlushEvents() immediately after high-value actions, such as a real-money purchase or reaching a major level milestone. This forces the immediate “elimination” of the local cache to the Swrve servers.

Leverage AppVersion for A/B Testing

Always update the AppVersion string in your DefaultEngine.ini for each release. Swrve uses this field to segment users, allowing you to run A/B tests or targeted campaigns that are only visible to players on a specific build version.

Sanitize Attribute Keys

Swrve’s backend can be sensitive to special characters in attribute keys. Stick to alphanumeric characters and underscores. Avoid using dots or spaces in your FAnalyticsEventAttribute names to ensure that all data is correctly parsed and displayed in the Swrve analytics funnel.