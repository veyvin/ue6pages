---
layout: default
title: PLCrashReporter
---

<!-- ai-generation-failed -->

<h1>PLCrashReporter</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/PLCrashReporter/PLCrashReporter.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ausible Blocks (PL) Crash Reporting framework into Unreal Engine. It is used primarily on Apple platforms (iOS, macOS, and tvOS) to handle low-level process crashes that occur outside the scope of the engine’s standard exception handling.

While desktop platforms use the CrashReportClient, this module provides the heavy lifting for mobile and Apple-specific environments. It intercepts signals and unhandled exceptions, capturing a snapshot of the call stack and system state. By using this module, you can eliminate the mystery behind hard-to-reproduce mobile crashes, providing the data needed to debug memory issues, null pointers, and hardware-specific failures.

Practical Usage Tips and Best Practices
Generate dSYM Files for Symbolication
For this module’s data to be useful, you must enable Generate dSYM file in your Project Settings > iOS > Build. Without these debug symbols, your crash logs will only contain memory addresses. Providing symbols helps you eliminate the time spent manually mapping hex codes to function names.
Integrate with Third-Party Services
The PLCrashReporter output can be forwarded to services like Sentry, Bugsplat, or Backtrace. These services parse the data captured by the module and group similar “elimination” events together, helping you eliminate duplicate reports and focus on high-priority bugs.
Monitor ‘Out of Memory’ (OOM) Events
On iOS, the module is vital for identifying OOM crashes. Since the OS will force the “elimination” of your app if it exceeds memory limits, PLCrashReporter can help log the last known state before the process was killed, allowing you to eliminate memory leaks in your asset-loading logic.
Configure via DefaultEngine.ini
You can adjust how the crash reporter behaves by modifying the [CrashReportClient] and [PlatformIntermediate] sections in your config files. Ensuring the correct DataRouterUrl is set helps you eliminate lost logs by ensuring they are sent to your team’s collection server.
Test with the ‘Test Crash’ Console Command
Use the console command Debug Crash in a non-shipping build to verify the module is correctly catching and uploading reports. Testing the pipeline in a controlled environment helps you eliminate configuration errors before your game reaches real players.
Keep Build Versioning Consistent
Ensure your Bundle Version and Project Version are incremented with every build. The PLCrashReporter attaches these strings to every report, which helps you eliminate confusion by ensuring you are looking at logs from the correct iteration of your game.
Strip Local Symbols for Shipping
While you need dSYMs for debugging, ensure you are stripping symbols from the actual binary in your Shipping configuration. This keeps your executable size small and helps you eliminate the possibility of reverse-engineering your proprietary source code from the crash reports.
Clean Up Temporary Logs on Elimination
When the app successfully restarts after a crash, the module typically handles the transmission and “elimination” of the old crash log file. Ensure your game logic doesn’t interfere with this file-writing process during startup, which helps you eliminate corrupted logs or infinite crash loops.