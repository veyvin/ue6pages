---
layout: default
title: CrashReportCore
---

<!-- ai-generation-failed -->

<h1>CrashReportCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/CrashReportCore/CrashReportCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, AnalyticsET, Core, CrashDebugHelper, HTTP, Json, XmlParser</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

responsible for the shared backend logic used to generate, format, and process crash data. It acts as the “data engine” that sits between a crashing application and the standalone CrashReportClient (CRC) executable. Its primary role is to aggregate system information (OS version, GPU drivers), callstacks, and game logs into a standardized XML/JSON format known as the Crash Context.

While you rarely call its functions during normal gameplay, it is the module you must interface with if you want to customize how crash data is packaged and sent to your error-tracking backend (such as Sentry, Backtrace, or a custom server).

Practical Usage Tips and Best Practices
1. Include for Custom Crash Metadata

If you are building a custom crash reporting tool or a wrapper that needs to parse Unreal’s .crashcontext files, you must add this module to your Build.cs. This provides access to the shared types and serialization logic used by the engine:

C#
	PublicDependencyModuleNames.Add("CrashReportCore");

	```

	 

	#### 2. Use "FGenericCrashContext" for Custom Keys

	The most common practical use for this module's logic is adding custom key-value pairs to your crash reports. Use the `FPlatformCrashContext::SetGameData` or `FGenericCrashContext::AddCrashProperty` methods (accessible via the `Core` and `CrashReportCore` integration) to include high-level gameplay state, such as `CurrentMapName` or `ActiveQuestID`. This data is invaluable for the **elimination** of non-reproducible bugs.

	 

	#### 3. Configure the Crash Report UI

	In your project’s `DefaultEngine.ini`, you can use settings processed by this module to control how the Crash Report Client behaves. For example, to ensure the "Send Report" dialog appears even in unattended environments for debugging:

	```ini

	[CrashReportClient]

	bAllowAutomatedReports=true

	bHideLogFilesOption=false

	```

	 

	#### 4. Distinguish "Ensure" vs. "Crash" Data

	This module handles both **Crashes** (fatal) and **Ensures** (non-fatal asserts). Be aware that `ensure()` calls also use the `CrashReportCore` logic to generate a "mini" report in the background. If your logs are becoming bloated, use the module's configuration to limit the frequency of these non-fatal reports, ensuring the **elimination** of noise in your error tracking service.

	 

	#### 5. Verify the "CrashContext.runtime-xml"

	During development, if you want to see exactly what data this module is capturing, navigate to your project's `Saved/Crashes/[CrashID]/` folder. The `CrashContext.runtime-xml` file is the direct output of this module. Reviewing this file manually is the best way to verify that your custom "GameData" keys are being serialized correctly before they are sent to a server.

	 

	#### 6. Optimize Log Inclusion

	The `CrashReportCore` logic automatically attaches the last few hundred lines of the `Project.log` to a report. If your game generates massive logs, this can lead to slow upload times or the **elimination** of the report entirely on slow connections. Use `FGenericCrashContext` settings to truncate logs to only the most recent relevant entries.

	 

	#### 7. Secure Sensitive Information

	Since this module captures system paths and environment variables, ensure you are not accidentally including PII (Personally Identifiable Information). If your game handles user emails or real names, use a custom override to sanitize the data processed by `CrashReportCore` before it is packaged into the final `.zip` file for upload.

	 

	#### 8. Link with Symbolic Information

	While `CrashReportCore` handles the data, it does not "symbolicate" (convert hex addresses to function names). To make the data from this module useful, you must maintain a matching **Symbol Store** (PDBs on Windows, dSYMs on iOS). Without matching symbols, the data processed by this module will only show hex offsets, resulting in the **elimination** of its usefulness for debugging.
Copy code
2. Use FGenericCrashContext for Custom Keys

The most common practical use for this module’s logic is adding custom key-value pairs to your crash reports. Use FPlatformCrashContext::SetGameData or FGenericCrashContext::AddCrashProperty to include high-level gameplay state, such as CurrentMapName or ActiveQuestID. This data is invaluable for the elimination of non-reproducible bugs.

3. Configure the Crash Report UI

In your project’s DefaultEngine.ini, you can use settings processed by this module to control how the Crash Report Client behaves. For example, to ensure the “Send Report” dialog appears even in unattended environments for debugging:

ini
	[CrashReportClient]

	bAllowAutomatedReports=true

	bHideLogFilesOption=false
Copy code
4. Distinguish Ensure vs. Crash Data

This module handles both Crashes (fatal) and Ensures (non-fatal asserts). Be aware that ensure() calls also use the CrashReportCore logic to generate a “mini” report in the background. If your logs are becoming bloated, use the module’s configuration to limit the frequency of these non-fatal reports, ensuring the elimination of noise in your error tracking service.

5. Verify the “CrashContext.runtime-xml”

During development, if you want to see exactly what data this module is capturing, navigate to your project’s Saved/Crashes/[CrashID]/ folder. The CrashContext.runtime-xml file is the direct output of this module. Reviewing this file manually is the best way to verify that your custom “GameData” keys are being serialized correctly.

6. Optimize Log Inclusion

The CrashReportCore logic automatically attaches the last few hundred lines of the Project.log to a report. If your game generates massive logs, this can lead to slow upload times or the elimination of the report entirely on slow connections. Use the module settings to truncate logs to only the most recent relevant entries.

7. Secure Sensitive Information

Since this module captures system paths and environment variables, ensure you are not accidentally including PII (Personally Identifiable Information). If your game handles user emails or real names, use a custom override to sanitize the data processed by CrashReportCore before it is packaged into the final .zip file.

8. Link with Symbolic Information

While CrashReportCore handles the data, it does not “symbolicate” (convert hex addresses to function names). To make the data from this module useful, you must maintain a matching Symbol Store (PDBs on Windows, dSYMs on iOS). Without matching symbols, the data processed by this module will only show hex offsets, resulting in the elimination of its usefulness for debugging.