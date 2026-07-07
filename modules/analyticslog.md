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

er) is a specialized debugging tool within Unreal Engine’s analytics framework. Instead of sending telemetry data to a remote cloud service (like Flurry or a custom backend), it captures all analytics events and writes them locally to the disk as JSON-formatted text files.

This is primarily used during development to verify that your instrumentation is correct, ensuring that events are firing with the expected attributes before you deploy to production servers.

Practical Usage Tips and Best Practices
1. Add the Module to your Build

To use the File Logging provider, include the module in your Build.cs. Since this is a debugging tool, you may want to conditionally include it to keep shipping builds lean.

C#
	// In YourProject.Build.cs

	if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PublicDependencyModuleNames.Add("AnalyticsLog");

	}

	```

	 

	#### 2. Configure via DefaultEngine.ini

	You can activate the module without writing extra C++ code by setting it as your default provider in your project's configuration files. This tells the `Analytics` system to route all calls to the file logger.

	 

	```ini

	; In DefaultEngine.ini

	[Analytics]

	ProviderModuleName=FileLogging

	```

	 

	#### 3. Locate the Output Files

	The module automatically generates files during a session. Knowing where to find them is critical for rapid iteration.

	*   **Path:** `[ProjectDirectory]/Saved/Analytics/`

	*   **Extension:** `.analytics`

	*   **Format:** Each file contains a JSON array of events recorded during a single engine session.

	 

	#### 4. Use for "Dry Run" Validation

	Before integrating a complex backend like PlayFab or GameAnalytics, use `FileLogging` to perform a "dry run." By inspecting the local `.analytics` files, you can ensure that your `FAnalyticsEventAttribute` arrays are correctly structured and that mandatory keys are present.

	 

	#### 5. Monitor File Growth

	The `AnalyticsLog` provider writes every event to disk, and these files do not self-delete.

	*   **Best Practice:** Do not leave this provider active in a long-running "Auto-Test" or "Burn-in" environment, as it can eventually consume significant disk space on dev kits or build machines.

	 

	#### 6. Combine with the Multicast Provider

	You can log to a file **and** a cloud backend simultaneously by using the `AnalyticsMulticast` module. This allows you to see what is being sent to your dashboard in real-time by checking your local logs.

	 

	```ini

	; Example of logging to both a file and a cloud service

	[Analytics]

	ProviderModuleName=AnalyticsMulticast

	ProviderModuleNames=FileLogging,YourCloudProvider

	```

	 

	#### 7. C++ Session Management

	Even when logging to a local file, you must explicitly start and end the session in C++ (or Blueprints) for the file to be generated correctly.

	 

	```cpp

	#include "Analytics.h"

	#include "Interfaces/IAnalyticsProvider.h"

	 

	void AMyGameMode::StartAnalytics()

	{

	    // Gets the default provider (FileLogging if configured in .ini)

	    TSharedPtr<IAnalyticsProvider> Provider = FAnalytics::Get().GetDefaultConfiguredProvider();

	    if (Provider.IsValid())

	    {

	        Provider->StartSession();

	        UE_LOG(LogTemp, Log, TEXT("Analytics File Logging started."));

	    }

	}

	```

	 

	#### 8. Verify JSON Syntax

	If your analytics events contain complex strings (like JSON-within-JSON), the `AnalyticsLog` module will automatically escape them. If you see malformed logs, check for illegal characters in your C++ `FString` attributes that might be confusing the internal JSON writer.
Copy code
2. Configure via DefaultEngine.ini

You can activate the module by setting it as your default provider in your project’s configuration files. This tells the Analytics system to route all calls to the file logger.

ini
	; In DefaultEngine.ini

	[Analytics]

	ProviderModuleName=FileLogging
Copy code
3. Locate the Output Files

The module automatically generates files during a session. Knowing where to find them is critical for rapid verification.

Path: [ProjectDirectory]/Saved/Analytics/
Extension: .analytics
Format: Each file contains a JSON array of events recorded during a single engine session.
4. Use for “Dry Run” Validation

Before integrating a complex backend like PlayFab or a custom web service, use FileLogging to perform a “dry run.” By inspecting the local files, you can ensure that your attribute arrays are correctly structured and that mandatory keys are present.

5. Monitor File Growth

The AnalyticsLog provider writes every event to disk, and these files do not self-delete.

Best Practice: Do not leave this provider active in a long-running “Auto-Test” or “Burn-in” environment, as it can eventually consume significant disk space on dev kits or build machines.
6. Combine with the Multicast Provider

You can log to a file and a cloud backend simultaneously by using the AnalyticsMulticast module. This allows you to see exactly what is being sent to your dashboard in real-time by checking your local logs.

ini
	; Example of logging to both a file and a cloud service

	[Analytics]

	ProviderModuleName=AnalyticsMulticast

	ProviderModuleNames=FileLogging,YourCloudProvider
Copy code
7. C++ Session Management

Even when logging to a local file, you must explicitly start and end the session in C++ (or Blueprints) for the file to be generated correctly.

C++
	#include "Analytics.h"

	#include "Interfaces/IAnalyticsProvider.h"

	 

	// Example initialization

	TSharedPtr<IAnalyticsProvider> Provider = FAnalytics::Get().GetDefaultConfiguredProvider();

	if (Provider.IsValid())

	{

	    Provider->StartSession();

	}
Copy code
8. Verify Event Elimination Logic

When testing logic where a player or entity is removed from the game world, use the AnalyticsLog to confirm that the “elimination” event is firing with the correct coordinates and instigator data. This is much faster than waiting for web dashboard updates to refresh.