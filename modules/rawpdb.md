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

tract information from Program Database (.pdb) files on Windows. PDB files contain debugging information about compiled executables and DLLs, such as function names, variable types, and source line mappings.

This module is primarily utilized by engine-level tools and crash-reporting systems (like the Crash Report Client) to “symbolicate” stack traces. It allows the engine to translate raw memory addresses into human-readable function names and file locations without requiring the full Microsoft DIA (Debug Interface Access) SDK to be installed on the user’s machine.

Practical Usage Tips & Best Practices
1. Use for Custom Crash Reporting

If you are building a custom in-house crash reporter or a diagnostic tool that needs to analyze minidumps, RawPDB is the go-to module.

Best Practice: Link against the RawPDB module in your tool’s .Build.cs. This allows your application to read PDB files directly, facilitating the elimination of “Unknown Function” entries in your error logs.
2. Verify PDB Existence for Symbolication

The module cannot function if the .pdb files were stripped during the build process or moved to a different directory.

Tip: When packaging your project, ensure “Include Debug Files” is checked in the Project Settings. Including these files ensures the elimination of useless, unreadable crash dumps when testing your game in a “Shipping” or “Test” configuration.
3. Optimize Tool Performance with Metadata Only

PDB files can be several gigabytes in size for large projects like Unreal.

Best Practice: Use the module to extract only the necessary metadata (like the PDB Guid and Age) to match a specific executable version. This targeted extraction leads to the elimination of massive memory overhead compared to loading the entire debug database into memory.
4. Handle Platform-Specific Logic

The RawPDB module is specifically designed for the Microsoft PDB format and is only relevant for Windows builds.

Tip: Always wrap your RawPDB-related code in #if PLATFORM_WINDOWS macros. This results in the elimination of compilation errors when building your project for Linux, macOS, or consoles that use different debug formats (like DWARF).
5. Leverage for Automated Performance Audits

You can use this module to write scripts that scan your compiled binaries to see which functions are taking up the most space or where excessive inlining is occurring.

Best Practice: Use the RawPDB parser to iterate through symbols and log function sizes. This proactive auditing facilitates the elimination of “code bloat” by identifying unexpectedly large functions in your project’s final binary.
6. Coordinate with Source Indexing

RawPDB can extract the source file paths associated with specific symbols.

Tip: Combine this with a Source Control provider (like Perforce) to automatically open the correct version of a file when an error is detected. This workflow leads to the elimination of manual searching through different branches to find where a bug originated.
7. Monitor PDB Version Mismatches

A PDB must perfectly match the executable it was generated with; even a tiny code change creates an “Age” mismatch.

Best Practice: Use the RawPDB API to check the signature of the PDB against the header of the running .exe. Verifying this match ensures the elimination of “Offset Errors” where the debugger points to the wrong line of code because the files are out of sync.
8. Implement “Symbol Store” Logic

For large teams, you can use this module to create a local symbol server script that organizes PDBs by their internal GUIDs.

Tip: Have your build machine use RawPDB to index symbols into a shared network folder. This centralized management results in the elimination of “Missing Symbols” prompts for your QA team, as their debuggers can automatically fetch the correct PDB for any build.