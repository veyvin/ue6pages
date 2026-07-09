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

cs provider for Unreal Engine that transmits telemetry data over HTTP. Unlike platform-specific providers (like Flurry or AdMob), AnalyticsET is designed to send JSON-formatted event payloads to a custom web service or Epic’s Horde telemetry system.

It acts as the “glue” between the high-level Analytics API and your own data collection server, handling the buffering, formatting, and transmission of events in the background.

Practical Usage Tips and Best Practices
1. Configure Target-Specific Endpoints

Use different APIServerET and APIKeyET values for Development and Shipping builds in your DefaultEngine.ini. This ensures that internal testing data—such as testing an “elimination” mechanic with cheats enabled—does not skew your production player metrics.

2. Leverage Event Buffering

To minimize network overhead, AnalyticsET does not send every event instantly. Use the SendInterval (default ~60s) or MaxEventCountBeforeFlush settings in your configuration. For critical data (e.g., a player’s final session stats), you can manually call FlushEvents() to force an immediate upload.

3. Use Attributes for Contextual Data

Instead of creating a unique event name for every possible scenario (e.g., DeathByLava, DeathByFall), use a generic event name like PlayerElimination and provide specific context via FAnalyticsEventAttribute. This allows for much more powerful data filtering on your backend.

4. Manage Session Lifecycles

Always call StartSession() as early as possible (e.g., in your GameInstance::Init) and EndSession() upon exit. AnalyticsET uses these calls to generate session UUIDs, which are essential for calculating “Session Length” and “User Retention” metrics.

5. Sanitize PII (Personally Identifiable Information)

Since data is sent via HTTP/HTTPS JSON payloads, ensure you are not accidentally including player emails, real names, or IP addresses in your attributes. This is critical for maintaining compliance with global privacy regulations (GDPR/CCPA).

6. Debug with File Logging

Before pointing to a live server, use the AnalyticsFileOut provider to write events to a local .analytics file in your Saved/ folder. This allows you to verify that your JSON structure and attribute values are correct before they hit your database.

7. Prevent Network Flooding

Avoid recording high-frequency events, such as player movement on every tick. Aggressive recording will bloat your payloads and potentially lead to the “elimination” of your server’s bandwidth. Aggregate high-frequency data locally and send a summary event every few minutes instead.

C++ Implementation Recipe

To use AnalyticsET, add the dependencies to your Build.cs and configure your DefaultEngine.ini.

Project.Build.cs

C#
	// AnalyticsET is an Editor/Client module

	PublicDependencyModuleNames.AddRange(new string[] { "Analytics", "AnalyticsET" });

	```

	 

	**DefaultEngine.ini**

	```ini

	[Analytics]

	ProviderModuleName=AnalyticsET

	APIServerET="https://your-api-server.com/api/v1/events"

	APIKeyET="YourProductionKey"

	SendInterval=60

	```

	 

	**C++ Logic**

	```cpp

	#include "Analytics.h"

	#include "Interfaces/IAnalyticsProviderET.h"

	 

	void UMyGameInstance::RecordPlayerKill(FString WeaponName, int32 StreakCount)

	{

	    // Get the configured provider

	    TSharedPtr<IAnalyticsProvider> Provider = FAnalytics::Get().GetDefaultConfiguredProvider();

	 

	    if (Provider.IsValid())

	    {

	        // Define attributes for the event

	        TArray<FAnalyticsEventAttribute> Attributes;

	        Attributes.Add(FAnalyticsEventAttribute(TEXT("Weapon"), WeaponName));

	        Attributes.Add(FAnalyticsEventAttribute(TEXT("Streak"), StreakCount));

	 

	        // Send the event (it will be buffered and sent according to SendInterval)

	        Provider->RecordEvent(TEXT("PlayerKill"), Attributes);

	    }

	}

	```

	 

	### Performance & Debugging

	*   **Log Analytics:** Use the console command `Log LogAnalytics Verbose` to see exactly when events are being queued and flushed in the Output Log.

	*   **Payload Size:** Keep attribute keys short (e.g., `wpn` instead of `CurrentEquippedWeaponName`) if you are operating at a massive scale to reduce bandwidth costs.
Copy code

DefaultEngine.ini

ini
	[Analytics]

	ProviderModuleName=AnalyticsET

	APIServerET="https://your-api-server.com/api/v1/telemetry"

	APIKeyET="YourProjectKey"

	SendInterval=60
Copy code

C++ Logic

C++
	#include "Analytics.h"

	#include "Interfaces/IAnalyticsProvider.h"

	 

	void UMyGameManager::RecordElimination(FString OpponentName, FString WeaponUsed)

	{

	    // Get the default configured provider

	    TSharedPtr<IAnalyticsProvider> Provider = FAnalytics::Get().GetDefaultConfiguredProvider();

	 

	    if (Provider.IsValid())

	    {

	        // Define attributes for the event

	        TArray<FAnalyticsEventAttribute> Attributes;

	        Attributes.Add(FAnalyticsEventAttribute(TEXT("Target"), OpponentName));

	        Attributes.Add(FAnalyticsEventAttribute(TEXT("Weapon"), WeaponUsed));

	 

	        // Record the event

	        Provider->RecordEvent(TEXT("PlayerElimination"), Attributes);

	    }

	}
Copy code
Performance & Best Practices
Log Analytics: Use the console command Log LogAnalytics Verbose to monitor when events are being queued and successfully transmitted in the Output Log.
Payload Size: Keep attribute keys short (e.g., wpn instead of CurrentEquippedWeaponName) to reduce bandwidth costs for mobile players.
Asynchronous Processing: AnalyticsET handles HTTP requests on its own background thread, ensuring that recording events does not hitch the main gameplay thread.