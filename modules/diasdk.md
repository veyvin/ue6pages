---
layout: default
title: DiaSdk
---

<!-- ai-generation-failed -->

<h1>DiaSdk</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/DiaSdk/DiaSdk.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ss (DIA) SDK. Its primary purpose is to provide Unreal Engine with the ability to programmatically access and parse information stored in Program Database (.pdb) files.

While the engine typically relies on the OS to handle basic stack traces, this module is used by low-level developer tools—such as the CrashReportClient, Unreal Insights, and the Editor itself—to perform deep symbolication (converting memory addresses into human-readable function names and source file lines).

Practical Usage Tips and Best Practices
1. Use for Automated Symbolication

The DIASDK is the engine’s primary tool for turning “raw” hex addresses from a crash into a readable callstack. If you are building a custom automated testing tool that needs to verify which function triggered a crash, you will need this module to resolve those symbols. This ensures the elimination of manual PDB lookups during large-scale automated testing.

2. Verify Build.cs Module Type

Because this module wraps a Microsoft SDK, it is platform-specific (Windows). When referencing it in a tool’s Build.cs, always ensure it is wrapped in a platform check. This avoids the elimination of your build’s ability to compile for non-Windows platforms like Linux or Mac:

C#
	if (Target.Platform == UnrealTargetPlatform.Win64)

	{

	    AddEngineThirdPartyPrivateStaticDependencies(Target, "DX11", "DIASDK");

	}
Copy code
3. Match PDBs with Executables

The DIA SDK is extremely strict: the .pdb file must perfectly match the .exe or .dll it was generated with. Even a minor recompile will make them incompatible. Always archive your symbols together with your builds to avoid the elimination of your ability to debug older versions of your game.

4. Leverage for Unreal Insights (TraceAnalysis)

Unreal Insights uses DIA logic to correlate CPU timings with specific C++ functions. If your Insights traces are showing “Unknown” for function names, it is often because the DIASDK cannot find the matching PDBs for the engine or project modules. Keeping your PDBs in the same folder as your binaries is the best way to ensure the elimination of “Unknown” entries in your profiles.

5. Understand the msdia140.dll Requirement

The DIASDK module requires the msdia140.dll (or similar version) to be registered or present on the system. If you are distributing a standalone tool that uses this module, ensure you include the necessary redistributables. Failure to do so will result in the elimination of the tool’s symbol-parsing capabilities on other workstations.

6. Use for Source Indexing Integration

This module plays a role in Unreal’s ability to support Source Indexing. By parsing the PDB, the engine can determine which version of a source file in Perforce or Git corresponds to a specific crash. This facilitates the elimination of the “Searching for Source File” dialog in Visual Studio, as the correct file version can be fetched automatically.

7. Monitor CrashReportClient Logs

If the CrashReportClient fails to show a callstack, check its local log files. It will often report if the DIASDK failed to initialize or if it couldn’t find a symbol provider. Investigating these logs is essential for the elimination of “blind” crashes where no stack trace is provided to the team.

8. Avoid in Shipping Builds

The DIASDK and symbol parsing logic should never be included in a final Shipping build for players. Parsing symbols is a heavy operation and a security risk, as it exposes your internal code structure. Ensure this module is only used in Development, Debug, or Test configurations to assist in the elimination of unauthorized reverse-engineering of your binaries.