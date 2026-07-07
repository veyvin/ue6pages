---
layout: default
title: CrashReportClient
---

<!-- ai-generation-failed -->

<h1>CrashReportClient</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/CrashReportClient/CrashReportClient.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, AnalyticsET, ApplicationCore, Core, CoreUObject, CrashReportCore, DesktopPlatform, HTTP, InputCore, Json, LauncherPlatform, MessageLog, PakFile, Projects, Slate, SlateCore, StandaloneRenderer, XmlParser</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

esigned to handle the aftermath of an engine crash. Because a crashed process is inherently unstable, Unreal Engine spawns the CRC as a separate, lightweight process that outlives the main game. Its primary purpose is to gather the crash context (logs, callstacks, and system info) and transmit it to a server for analysis.

In a shipping game, this is the window that appears asking the player to “Send and Close.” For developers, it is a critical pipeline tool for identifying and prioritizing the bugs that most frequently eliminate the application.

1. Configure the Crash Report Receiver

By default, the CRC is configured to send reports to Epic Games. For your own project, you must redirect this to your own backend (such as Sentry, Backtrace, or BugSplat).

Best Practice: Define your endpoint in DefaultEngine.ini under the [CrashReportClient] section using the DataRouterUrl key. This ensures that every crash in the wild is sent directly to your team’s dashboard.
2. Add Custom Context Attributes

You can inject game-specific metadata (like the current Map Name, Player Level, or Match ID) into the crash report before the application is eliminated.

Tip: Use the FPlatformMisc::SetStoredValue or the FCrashContext API in C++ to add key-value pairs. Seeing that 90% of crashes occur on a specific “Level_02” is much more helpful than just seeing a raw memory address.
3. Utilize Unattended Mode for Build Machines

If a crash occurs on a dedicated server or a continuous integration (CI) build machine, there is no user to click the “Send” button.

Best Practice: Launch your builds with the -unattended flag. When this flag is detected, the CrashReportClient will automatically package and send the report without waiting for user input, ensuring you don’t lose valuable data from automated tests.
4. Handle Privacy and GDPR

Crash reports can sometimes contain sensitive information, such as the user’s local file paths or machine name.

Tip: Review the data being sent and provide a checkbox in your game’s legal/options menu to toggle crash reporting. You can use the FGenericCrashContext to scrub or eliminate personal identifiable information (PII) from the logs before they are transmitted.
5. Force a Crash for Testing

You should verify that your CRC pipeline works before you ship.

Best Practice: Use the console command debug crash in a non-shipping build. This will purposefully eliminate the engine and trigger the CrashReportClient. This is the best way to confirm that your server is receiving the data and that your symbols are correctly resolving the callstack.
6. Include Symbols for Callstack Resolution

A crash report is useless if the callstack only shows memory addresses (e.g., 0x00007FF...).

Tip: When packaging your game, ensure you generate and store Debug Symbols (.pdb or .dsym files). Most crash reporting backends allow you to upload these symbols so they can “symbolicate” the report, turning hex addresses into human-readable function names and line numbers.
7. Monitor “Ensure” and “Assert” Reports

The CRC doesn’t just handle fatal crashes. It can also be configured to send reports for ensure() failures.

Best Practice: An ensure is a non-fatal error that allows the game to continue but signifies something is wrong. Tracking these allows you to eliminate “silent” bugs that might be degrading the player experience or causing performance hitches without actually closing the game.
8. Customize the CRC UI for Your Brand

The default “Unreal” look of the crash reporter can be jarring for players.

Tip: You can modify the source code of the CrashReportClient (found in Engine/Source/Programs/CrashReportClient) to change its UI to match your game’s branding. This makes the experience feel more professional and can increase the “Send Report” conversion rate by making the tool look trustworthy.