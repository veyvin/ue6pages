---
layout: default
title: CrashReportClientEditor
---

<!-- ai-generation-failed -->

<h1>CrashReportClientEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/CrashReportClient/CrashReportClientEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>CrashReportClient</code></span></li><li><span class="label">依赖</span><span class="value">Concert, EditorAnalyticsSession, Messaging</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Unreal Editor and the standalone Crash Report Client application. Its primary responsibility is to monitor the editor’s process and, in the event of a failure, gather the necessary context—such as log files, minidumps, and system metadata—to package a crash report.

Unlike the runtime crash reporter used in shipped games, this module is tailored for the developer workflow. it ensures that the unique identifiers (GUIDs) and callstack information are correctly mapped to the project’s source and symbols, allowing developers to eliminate guesswork when diagnosing instability in a local or team environment.

Practical Usage Tips and Best Practices
Manage Local Report Storage
By default, reports are stored in your project’s Saved/Crashes folder. On large teams, these folders can grow significantly. Periodically eliminate old report folders to reclaim disk space, especially before performing a clean build or migrating a project.
Utilize the -CrashForUAT Flag
When running automation scripts via the Unreal Automation Tool (UAT), use the -CrashForUAT command-line flag. This ensures the CrashReportClientEditor logic handles the exit correctly, allowing your build farm to eliminate “silent” failures where a script hangs instead of reporting a crash.
Verify Symbol Access for Callstacks
To eliminate “Unknown Function” entries in your reports, ensure that the editor has access to the .pdb (symbol) files for your project. This module relies on these symbols to translate memory addresses into human-readable code locations during the report generation phase.
Configure Privacy via Project Settings
In the Editor Preferences under General > Privacy, you can control how much data is sent to Epic Games. For sensitive internal projects, you may want to eliminate automatic submission to ensure that intellectual property contained in logs or pathnames is not transmitted externally.
Debug Unattended Mode
If the editor is running in -unattended mode (common for build machines), the module will eliminate the pop-up UI and attempt to send the report automatically. Ensure your build machine’s firewall allows the Crash Report Client to communicate with your designated crash-reporting server.
Review Logs for “Ensure” Failures
This module also captures “Ensures” (non-fatal assertions). While they do not shut down the editor, they are often precursors to critical failures. Regularly check the Saved/Crashes logs for these entries to eliminate bugs before they escalate into full editor crashes.
Customizing the Crash Context
If you are building custom engine tools, you can use the API associated with this module to add custom strings or metadata to the crash context. This helps eliminate ambiguity by including specific tool-state information in the report that is generated when a crash occurs.
Check LogConfig for Client Paths
If the crash reporter fails to launch, verify that the CrashReportClient path is correctly defined in your engine’s BaseEngine.ini. If the path is incorrect, the editor will be unable to hand off the crash data, which can eliminate your ability to capture the cause of the failure.