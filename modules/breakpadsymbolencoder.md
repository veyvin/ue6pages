---
layout: default
title: BreakpadSymbolEncoder
---

<!-- ai-generation-failed -->

<h1>BreakpadSymbolEncoder</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/BreakpadSymbolEncoder/BreakpadSymbolEncoder.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

l Engine used for processing and converting engine debug symbols into a format compatible with the Google Breakpad crash reporting system.

Description and Purpose

This module provides the utility logic to parse standard platform debug symbols (such as Windows .pdb files or Linux/Mac DWARF data) and “encode” them into text-based .sym files. Its primary purpose is to support the CrashReportClient and third-party crash integration services (like Sentry or Backtrace) on platforms where Google Breakpad is the preferred crash-handling framework (primarily Linux, Android, and occasionally macOS). By converting heavy binary symbols into lightweight text files, it enables the server-side “symbolication” of crash reports, turning raw memory addresses into human-readable function names and line numbers.

Practical Usage Tips and Best Practices
Integrate into CI/CD Pipelines
Automate the execution of this encoder as a post-build step in your Continuous Integration pipeline. Since you cannot debug a crash without the matching .sym file, ensuring these are generated and archived for every “Shipping” build is vital to eliminate “untraceable” crashes from your live environment.
Manage Storage for .sym Files
Unlike binary PDBs, .sym files are significantly smaller but still numerous. Establish a dedicated symbol server or a structured directory on your NAS. This module generates a specific header in the .sym file containing a unique Build ID; ensure your storage hierarchy uses this ID to prevent symbol mismatches.
Essential for Linux Dedicated Servers
If you are deploying dedicated servers on Linux, use the BreakpadSymbolEncoder to generate symbols for your server binaries. This allows you to symbolicate “server-side” crashes, which is critical for maintaining uptime and identifying bugs that only occur under high network load.
Use with Third-Party Services
Most modern crash-tracking services require symbols to be uploaded in the Breakpad format. If you are using a service like Sentry, this module is the engine-side tool responsible for prepping your metadata. Without it, you would have to manually run external command-line tools to convert your engine’s debug data.
Debug Elimination of Crashes
When a player reports a crash during a high-intensity event—such as a massive player elimination in a battle royale—the stack trace is your only map. Proper encoding ensures that the elimination logic (e.g., TakeDamage, OnEliminated) is clearly visible in the crash dump, allowing you to eliminate the bug at the source.
Validate Build IDs
Ensure that the symbols you encode exactly match the binary sent to players. If the BreakpadSymbolEncoder runs against a slightly different build of the engine than the one used for the executable, the Build IDs won’t match, and the resulting crash reports will remain “unsymbolicated” and useless for debugging.
Selective Symbol Encoding
To save time during the build process, you can configure the encoder to ignore certain third-party libraries or modules that you aren’t actively debugging. This helps eliminate unnecessary processing time and reduces the final size of your symbol archive.
Run via Commandlet
In many cases, this module is accessed via a UBT (Unreal Build Tool) argument or a specific commandlet like GenerateSYMS. Familiarize yourself with these command-line arguments to trigger symbol encoding without needing to open the Unreal Editor UI.