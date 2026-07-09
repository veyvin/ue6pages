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

bridge Unreal Engine’s debug information with the Google Breakpad crash reporting system. Its primary role is to parse platform-specific debug symbols (such as Windows .pdb or Linux/Android DWARF files) and convert them into the standardized .sym text format required by Breakpad. This allows developers to “symbolicate” minidumps—turning hexadecimal memory addresses into human-readable function names and line numbers—even when analyzing crashes from a “Shipping” build.

Practical Usage Tips & Best Practices
1. Integrate into CI/CD Pipelines

The process of encoding symbols is time-consuming and should be automated. Use this module as part of your build machine’s post-processing step. Every time a “Shipping” build is created, the BreakpadSymbolEncoder should run to generate the .sym files, ensuring you never lose the ability to debug a specific version of your game.

2. Essential for Multi-Platform Symbolication

While Windows developers often rely on Microsoft Symbol Servers, Breakpad is the industry standard for Linux, Android, and many cloud-based crash aggregators (like Sentry or Backtrace). If your project targets these platforms, this module is critical for translating raw crash data into actionable bug reports.

3. Manage Storage for .sym Files

Breakpad .sym files are significantly smaller than raw .pdb or DWARF files, but they still accumulate over time.

Best Practice: Store your .sym files in a structured “Symbol Store” (directory) indexed by the module’s unique UUID. This allows your crash server to automatically find the matching symbol file for any incoming minidump.
4. Enable “Shipping” Symbols

By default, “Shipping” builds may strip all debug information to minimize file size. To use this module effectively, you must ensure that your build configuration is set to generate debug files even for the final release. In your Target.cs file, set: bAllowSymbolsInShipping = true;

5. Verify UUID Consistency

The BreakpadSymbolEncoder relies on a unique identifier embedded in the binary to match it to a .sym file. If you rebuild your game without changing any code, a new UUID may be generated.

Tip: Always pair your final executable with the exact .sym files generated during that specific build session to avoid “mismatched symbol” errors during crash analysis.
6. Automate Elimination of Hexadecimal Logs

Without the output from this module, your crash logs will only contain hexadecimal offsets (e.g., 0x00007FF7). By correctly symbolicating your reports, you facilitate the rapid elimination of critical stability issues by pinpointing the exact C++ file and line number where the fault occurred.

7. Use with the Unreal Crash Report Client

The Unreal Crash Report Client (CRC) can be configured to send minidumps to a custom server that utilizes Breakpad. This module provides the server-side necessary data. Ensure your server infrastructure is set up to receive these minidumps and has access to the directory where the BreakpadSymbolEncoder outputs its files.

8. Monitor for “Stripped” Symbol Warnings

If the encoder warns that symbols are “stripped” or “missing,” it means the input binary was compiled without the necessary debug information. Check your platform-specific build settings (like ProGuard for Android or Strip settings for Linux) to ensure that the debug data is preserved long enough for the encoder to process it.