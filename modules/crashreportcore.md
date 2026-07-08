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

or processing, formatting, and symbolicating crash data within the Unreal Engine ecosystem. While the CrashReportClient provides the user-facing window seen after a crash, CrashReportCore handles the “heavy lifting” of the crash pipeline, including parsing minidumps, generating the CrashContext.runtime-xml file, and managing the transmission of reports to a server.

It is designed to be platform-agnostic, providing the underlying structures that ensure crash data is consistently captured across Windows, Linux, and Mac.

Practical Usage Tips and Best Practices
1. Add Custom Context via SetGameData

The most practical use of this system for gameplay developers is adding “Breadcrumbs.” Use FPlatformCrashContext::SetGameData(Key, Value) to inject custom strings into the crash report. For example, store the current Map Name or active Quest ID. This allows for the elimination of mystery regarding the game state when a crash occurred.

2. Configure the DataRouterUrl

In your project’s DefaultEngine.ini, you can specify where crash reports are sent by setting the DataRouterUrl. If you are using a third-party service like Sentry or Backtrace, or your own custom crash server, ensuring this URL is correct is vital for the elimination of lost telemetry data from your players.

3. Include Symbols for Proper Callstacks

A crash report is useless without symbols (PDBs). Ensure your build pipeline archives the symbols for every shipping build. CrashReportCore can only provide human-readable function names if the server receiving the report has access to these symbols, leading to the elimination of cryptic hex addresses in your logs.

4. Monitor the CrashContext.runtime-xml

Before a report is sent, the engine generates an XML file containing environment details (CPU, GPU, RAM, OS version). If you are debugging hardware-specific crashes, parsing this file helps in the elimination of hardware compatibility issues by identifying patterns in the reported machine specs.

5. Utilize “Ensure” for Non-Fatal Reporting

Use the ensure() macro to report non-fatal logic errors to the crash system without closing the game. This triggers the CrashReportCore logic to capture a callstack in the background while the game continues to run, assisting in the elimination of “silent” bugs that don’t cause an immediate crash.

6. Enable GPU Crash Debugging

To get the most out of this module for rendering issues, add r.GPUCrashDebugging=1 to your ConsoleVariables.ini. This instructs the core to capture the GPU state and “breadcrumbs” from the RHI, which is essential for the elimination of “Device Removed” or “TDR” crashes.

7. Handle Unattended Mode for Servers

For dedicated servers, ensure the crash reporter is set to Unattended Mode via the command line (-Unattended). This prevents the process from hanging while waiting for a user to click “Send,” ensuring the elimination of server downtime by allowing the process to close and restart immediately.

8. Verify Module Dependencies in Build.cs

If you are writing a custom editor tool or a specialized reporter, you must include CrashReportCore in your PrivateDependencyModuleNames. This gives you access to FCrashAnalyzer and other utility classes used to read .dmp files, facilitating the elimination of manual hex-editing when analyzing local crash files.