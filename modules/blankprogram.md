---
layout: default
title: BlankProgram
---

<!-- ai-generation-failed -->

<h1>BlankProgram</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/BlankProgram/BlankProgram.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Projects</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

standalone C++ console applications within the Unreal Engine ecosystem. Unlike standard Game, Client, or Editor targets, a “Program” is a lean, independent executable that lives in the Engine/Source/Programs directory. It is primarily used to build specialized command-line tools (like UnrealHeaderTool, ShaderCompileWorker, or custom build-pipeline utilities) that leverage Unreal’s Core libraries without the massive overhead of the full Engine, Slate UI, or Rendering systems.

Minimal C++ Implementation

To create a BlankProgram, you need a .Target.cs, a .Build.cs, and a .cpp file.

BlankProgram.Target.cs

C#
	using UnrealBuildTool;

	 

	public class BlankProgramTarget : TargetRules

	{

	    public BlankProgramTarget(TargetInfo Target) : base(Target)

	    {

	        Type = TargetType.Program;

	        LinkType = TargetLinkType.Monolithic;

	        LaunchModuleName = "BlankProgram";

	 

	        // Programs usually don't need the engine or editor features

	        bCompileLeanAndMeanUE = true;

	        bUseLoggingInShipping = true;

	        bBuildDeveloperTools = false;

	        bUseMallocProfiler = false;

	    }

	}

	```

	 

	**BlankProgram.Build.cs**

	```csharp

	using UnrealBuildTool;

	 

	public class BlankProgram : ModuleRules

	{

	    public BlankProgram(ReadOnlyTargetRules Target) : base(Target)

	    {

	        // Core is the only essential dependency for most programs

	        PublicDependencyModuleNames.Add("Core");

	        

	        // Disable precompiled headers for faster small-tool builds

	        PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

	    }

	}

	```

	 

	**BlankProgram.cpp**

	```cpp

	#include "RequiredProgramMainCPPInclude.h"

	 

	// Define the entry point for a standalone engine program

	IMPLEMENT_FOREIGN_ENGINE_PROG(BlankProgram);

	 

	int32 Main(const TCHAR* CommandLine)

	{

	    // Initialize the Core systems (Logging, Pathing, etc.)

	    GEngineLoop.PreInit(CommandLine);

	    

	    UE_LOG(LogTemp, Display, TEXT("Hello from a Standalone UE Program!"));

	    

	    // Cleanup and exit

	    FEngineLoop::AppExit();

	    return 0;

	}

	```

	 

	---

	 

	### Practical Usage Tips & Best Practices

	 

	#### 1. Leverage "Lean and Mean" Mode

	Always set `bCompileLeanAndMeanUE = true` in your `.Target.cs`. This prevents the Unreal Build Tool from linking the heavy `Engine` and `Slate` modules by default, resulting in a significantly smaller binary and faster link times.

	 

	#### 2. Use `IMPLEMENT_FOREIGN_ENGINE_PROG`

	Unlike game modules that use `IMPLEMENT_PRIMARY_GAME_MODULE`, standalone programs must use the `IMPLEMENT_FOREIGN_ENGINE_PROG` macro. This sets up the global `GEngineLoop` and basic application lifecycle required for a program to run without a `UProject` context.

	 

	#### 3. Minimize Module Dependencies

	Only include the `Core` module in your `Build.cs` unless you specifically need advanced features. If you need JSON parsing, add `Json`; if you need file utilities, add `Projects`. Avoiding the `Engine` module is the key to keeping the program lightweight.

	 

	#### 4. PreInit vs. Full Init

	Most tools only require `GEngineLoop.PreInit`. This initializes the essential low-level systems (like `FPlatformProcess`, `FCommandLine`, and `GLog`). Avoid a full `Init()` call unless you are building a tool that actually needs to spawn `UObjects` or run the engine’s ticking loop.

	 

	#### 5. Independent Compilation

	Programs are compiled using the UnrealBuildTool directly. You can build your program from the command line using:

	`UnrealBuildTool.exe BlankProgram Win64 Development`

	This is much faster than compiling the entire project solution, making it ideal for build-server utilities.

	 

	#### 6. Cross-Platform Portability

	By staying within the `Core` module, your program is automatically cross-platform. The `FPlatform` and `FPaths` APIs allow you to write a tool once and run it on Windows, Linux, or Mac without changing a single line of C++.

	 

	#### 7. Handle Command Line Arguments

	Use `FCommandLine::Get()` to parse input. Programs are almost always driven by flags (e.g., `-input="path"`). Using `FParse::Value` is a best practice to keep your argument handling consistent with other Unreal tools.

	 

	#### 8. Manual Garbage Collection

	If your program *does* link the `CoreUObject` module to use reflection, remember that there is no automatic `Tick` calling `CollectGarbage`. You must manually call `IncrementalPurgeGarbage` or manage your object lifetimes strictly using `TStrongObjectPtr` if the tool runs for a long duration.
Copy code

BlankProgram.Build.cs

C#
	using UnrealBuildTool;

	 

	public class BlankProgram : ModuleRules

	{

	    public BlankProgram(ReadOnlyTargetRules Target) : base(Target)

	    {

	        // Core is the only essential dependency for most programs

	        PublicDependencyModuleNames.Add("Core");

	        

	        // Disable precompiled headers for faster small-tool builds

	        PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

	    }

	}
Copy code

BlankProgram.cpp

C++
	#include "RequiredProgramMainCPPInclude.h"

	 

	// Define the entry point for a standalone engine program

	IMPLEMENT_FOREIGN_ENGINE_PROG(BlankProgram);

	 

	int32 Main(const TCHAR* CommandLine)

	{

	    // Initialize the Core systems (Logging, Pathing, etc.)

	    GEngineLoop.PreInit(CommandLine);

	    

	    UE_LOG(LogTemp, Display, TEXT("Hello from a Standalone UE Program!"));

	    

	    // Cleanup and exit

	    FEngineLoop::AppExit();

	    return 0;

	}
Copy code
Practical Usage Tips & Best Practices
1. Leverage “Lean and Mean” Mode

Always set bCompileLeanAndMeanUE = true in your .Target.cs. This prevents the Unreal Build Tool from linking the heavy Engine and Slate modules by default, resulting in a significantly smaller binary and faster link times.

2. Use IMPLEMENT_FOREIGN_ENGINE_PROG

Unlike game modules that use IMPLEMENT_PRIMARY_GAME_MODULE, standalone programs must use the IMPLEMENT_FOREIGN_ENGINE_PROG macro. This sets up the global GEngineLoop and basic application lifecycle required for a program to run without a UProject context.

3. Minimize Module Dependencies

Only include the Core module in your Build.cs unless you specifically need advanced features. If you need JSON parsing, add Json; if you need file utilities, add Projects. Avoiding the Engine module is the key to keeping the program lightweight.

4. PreInit vs. Full Init

Most tools only require GEngineLoop.PreInit. This initializes the essential low-level systems (like FPlatformProcess, FCommandLine, and GLog). Avoid a full Init() call unless you are building a tool that actually needs to spawn UObjects or run the engine’s ticking loop.

5. Independent Compilation

Programs are compiled using the UnrealBuildTool directly. You can build your program from the command line using: UnrealBuildTool.exe BlankProgram Win64 Development This is much faster than compiling the entire project solution, making it ideal for build-server utilities.

6. Cross-Platform Portability

By staying within the Core module, your program is automatically cross-platform. The FPlatform and FPaths APIs allow you to write a tool once and run it on Windows, Linux, or Mac without changing a single line of C++.

7. Handle Command Line Arguments

Use FCommandLine::Get() to parse input. Programs are almost always driven by flags (e.g., -input="path"). Using FParse::Value is a best practice to keep your argument handling consistent with other Unreal tools.

8. Manual Garbage Collection

If your program does link the CoreUObject module to use reflection, remember that there is no automatic Tick calling CollectGarbage. You must manually call IncrementalPurgeGarbage or manage your object lifetimes strictly using TStrongObjectPtr if the tool runs for a long duration.