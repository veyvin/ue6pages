---
layout: default
title: RawPDB
---

<!-- ai-generation-failed -->

<h1>RawPDB</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/RawPDB/RawPDB.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Engine that provides a high-performance, standalone parser for Windows Program Database (.pdb) files.

Description and Purpose

Unlike standard Windows debugging tools that rely on the Microsoft DIA (Debug Interface Access) SDK, the RawPDB module is a self-contained implementation designed to read and interpret symbol data directly from the PDB bitstream. Its primary purpose is to allow engine-side tools—such as Live Coding, Zen Loader, and the Crash Report Client—to resolve function names, source file paths, and line numbers without requiring the heavy DIA COM components to be installed or initialized. By using this module, Unreal Engine can eliminate the dependency on external debugger APIs, enabling rapid “hot” patching of code and accurate symbolication even on machines without a full Visual Studio installation.

Practical Usage Tips and Best Practices
Integrate for Custom Tooling
If you are building an internal editor tool that needs to analyze the project’s own binary (e.g., a custom profiler or automated testing suite), add "RawPDB" to your PrivateDependencyModuleNames in your .Build.cs file. This is the best way to eliminate the need for manual symbol lookups or external command-line utilities.
Prioritize for Live Coding Performance
The Live Coding system uses this module to map modified functions in memory back to their original source locations. If your Live Coding sessions are slow to initialize, ensure your .pdb files are stored on a high-speed SSD. The RawPDB module is optimized for fast scanning, and localized storage helps it eliminate I/O bottlenecks during the symbol-mapping phase.
Use for Runtime Symbolication in Tools
In development tools, you can use the RawPDB API to resolve a memory address (Program Counter) to a human-readable function name. This is a best practice for logging systems that need to provide context-aware traces, helping you eliminate the guesswork when a specific thread or task hangs in a non-shipping build.
Avoid in Shipping Builds
The RawPDB module is strictly a developer/editor utility. Ensure that any code referencing this module is wrapped in #if WITH_EDITOR or #if !UE_BUILD_SHIPPING blocks. This ensures you eliminate unnecessary binary bloat and potential security risks by not shipping symbol-parsing logic to your end-users.
Verify PDB Integrity via the Module
If your symbols aren’t loading, you can use the module’s validation logic to check if the .pdb file matches the current executable’s GUID. Using this programmatic check is a reliable way to eliminate “mismatched symbol” errors that often occur after a partial build or interrupted compilation.
Handle Large PDB Memory Footprint
Parsing a massive .pdb file (which can be several gigabytes for a large project) consumes significant RAM. When using the module’s FRawPdbFile class (or similar), ensure you close the file handle or release the object as soon as your analysis is complete to eliminate memory pressure on the editor process.
Leverage for Asset/Code Mapping
This module is often used to map optimized data chunks back to their source files. If you are extending the engine’s loading pipeline, use this module to cross-reference compiled data with its original C++ definitions to eliminate data-mismatch bugs in complex asset loaders.
Debugging via Symbol Stores
If the CrashReportClient fails to symbolicate a crash, it is often because it cannot find the RawPDB-compatible symbols. A best practice is to use a Symbol Store (SymStore.exe) alongside this module. This helps the engine’s internal tools eliminate the “UnknownFunction” lines in callstacks by providing a central, indexed location for the module to scan.