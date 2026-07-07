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

rovider for Unreal Engine. It serves as the primary implementation of the IAnalyticsProvider interface, designed to send telemetry data to a backend server (such as Epic’s Horde, a custom web service, or a third-party endpoint) using standard JSON payloads over HTTP.

This module is the “glue” that takes game events (clicks, level loads, or player actions) and packages them into structured web requests for remote collection and analysis.

Practical Usage Tips & Best Practices
1. Configure via Engine.ini

Instead of hard-coding endpoints, configure the provider in your DefaultEngine.ini. This allows you to point to different servers for development, testing, and production builds without changing C++ code.

ini
	[Analytics]

	ProviderModuleName=AnalyticsET

	APIServerET="https://your-analytics-server.com/api"

	APIKeyET="YourUniqueProjectKey"

	SendInterval=60
Copy code
2. Batch Events to Reduce Overhead

Avoid sending an HTTP request for every single event, as this can severely impact network performance. Use the SendInterval setting to buffer events locally. The module will collect multiple events and “flush” them in a single batch, which is much more efficient for both the client and the server.

3. Use Attributes for Context

When recording events, use FAnalyticsEventAttribute to provide context rather than creating dozens of unique event names.

Poor: RecordEvent(TEXT("PlayerEliminatedByGrenade"))
Better: RecordEvent(TEXT("Elimination"), Attributes) where attributes include Method: Grenade and Location: ZoneA.
4. Design for Async Processing

AnalyticsET operates asynchronously. When you call RecordEvent, the module stores the data and continues execution. However, if the game crashes or is force-closed, un-flushed events may be lost. If you have a critical event (like a successful store purchase), you can manually call FlushEvents() to force an immediate upload.

5. Implement a “Heartbeat” Event

To accurately measure player retention and session length, implement a “Heartbeat” event that fires every few minutes. This allows you to track users who might crash or lose connection, ensuring you don’t lose all data regarding their time spent in the session before the elimination of the process.

6. Utilize the Blueprint Analytics Library

For UI and high-level gameplay logic, use the Analytics Blueprint Library plugin. It provides a wrapper for AnalyticsET, allowing designers to instrument the game without C++. Ensure the AnalyticsBlueprintLibrary module is added to your project dependencies to access these nodes.

7. Verify Payload Formats

Since AnalyticsET sends data via HTTP POST, ensure your backend is prepared to receive the specific JSON schema used by Unreal. You can debug the exact payload being sent by using the console command Log LogAnalytics Verbose to see the JSON strings in the Output Log before they are transmitted.

8. Respect Privacy and GDPR

Always wrap your analytics initialization in a check for user consent. Do not call StartSession() until the player has accepted your privacy policy. If a player opts out, you can call EndSession() and stop recording to ensure you are compliant with regional data protection laws.