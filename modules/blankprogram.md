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

al Engine used to create lightweight console applications. These programs run independently of the Unreal Editor and the full Game Engine framework, utilizing only the essential low-level libraries.

What it is and What it’s used for

Located in Engine/Source/Programs/BlankProgram, it serves as a “boilerplate” for developers building custom utility tools. Unlike a standard Game or Editor module, a Program target does not load the renderer, physics, or high-level gameplay systems by default.

Primary uses include:

Asset Processors: Building standalone command-line tools to batch-process textures, meshes, or metadata.
Build/CI Utilities: Creating custom tools for build farms to validate project integrity or generate reports.
Network Daemons: Running small, dedicated communication or signaling servers that don’t require the overhead of a game instance.
Diagnostic Tools: Creating low-level hardware or file-system checkers using Unreal’s cross-platform Core abstractions.
Practical Usage Tips and Best Practices
1. Minimize Module Dependencies

In your BlankProgram.Build.cs, only include the Core module unless absolutely necessary. Including Engine or UnrealEd will significantly increase your binary size and compile time, as it forces the inclusion of heavy runtime frameworks that a console utility rarely needs.

2. Implement a Minimal Entry Point

Standard Unreal programs don’t use the WinMain or main you might expect. Instead, they typically use the GEngineLoop for initialization. A minimal BlankProgram entry point looks like this:

C++
	#include "RequiredProgramMainCPPInclude.h"

	 

	IMPLEMENT_APPLICATION(BlankProgram, "BlankProgram");

	 

	INT32_MAIN_INT32_ARGC_TCHAR_ARGV()

	{

	    GEngineLoop.PreInit(ArgC, ArgV);

	    // Your logic here

	    FEngineLoop::AppPreExit();

	    FEngineLoop::AppExit();

	    return 0;

	}

	```

	 

	#### 3. Use FCommandLine for Argument Parsing

	Instead of manually parsing `argc` and `argv`, use Unreal's `FCommandLine` and `FParse`. This allows your tool to use standard Unreal syntax (e.g., `-SILENT`, `-MYPARAM=Value`) and makes your utility feel consistent with other engine tools like `UnrealEditor-Cmd.exe`.

	 

	#### 4. Configure the .Target.cs Properly

	Ensure your `BlankProgram.Target.cs` sets its `Type` to `TargetType.Program`. You should also set `bBuildDeveloperTools = false` and `bUseMallocProfiler = false` to keep the binary footprint as small as possible.

	 

	#### 5. Leverage FPlatformProcess for OS Tasks

	If your program needs to launch other processes, manage files, or interact with the OS environment, use `FPlatformProcess` and `FPlatformFileManager`. These provide a consistent, cross-platform C++ API that works across Windows, Linux, and macOS without needing platform-specific `#ifdefs`.

	 

	#### 6. Redirect Logging for Console Output

	By default, Unreal logs to a `.log` file. To see output directly in your terminal, ensure you use `GLog->SetPrintCanBeDeferred(false);` and use the `UE_LOG` macro. In your target settings, you may also need to enable `bCompileAgainstCoreUObject = false` if you don't need the reflection system.

	 

	#### 7. Handle the Unreal Message Bus

	If your standalone program needs to "talk" to the Unreal Editor (e.g., to notify an artist that a process finished), include the `Messaging` and `UdpMessaging` modules. This allows your Program to send and receive messages using the engine’s internal communication bus.

	 

	#### 8. Avoid Slate Unless Building a GUI

	While you *can* use Slate in a Program target (like the Project Launcher does), avoid it for console utilities. Adding `Slate` and `SlateCore` dependencies pulls in the entire rendering and windowing architecture, which contradicts the "Blank" nature of the module and slows down iteration.
Copy code
3. Use FCommandLine for Argument Parsing

Instead of manually parsing argc and argv, use Unreal’s FCommandLine and FParse. This allows your tool to use standard Unreal syntax (e.g., -SILENT, -MYPARAM=Value) and makes your utility feel consistent with other engine tools like UnrealEditor-Cmd.exe.

4. Configure the .Target.cs Properly

Ensure your BlankProgram.Target.cs sets its Type to TargetType.Program. You should also set bBuildDeveloperTools = false and bUseMallocProfiler = false in the constructor to keep the binary footprint as small as possible and eliminate unnecessary overhead.

5. Leverage FPlatformProcess for OS Tasks

If your program needs to launch other processes, manage files, or interact with the OS environment, use FPlatformProcess and FPlatformFileManager. These provide a consistent, cross-platform C++ API that works across Windows, Linux, and macOS without needing platform-specific code.

6. Redirect Logging for Console Output

By default, Unreal logs to a .log file. To see output directly in your terminal, ensure you use GLog->SetPrintCanBeDeferred(false); and use the UE_LOG macro. In your target settings, you may also need to enable bCompileAgainstCoreUObject = false if you don’t need the reflection system.

7. Handle the Unreal Message Bus

If your standalone program needs to “talk” to the Unreal Editor (e.g., to notify an artist that a process finished), include the Messaging and UdpMessaging modules. This allows your Program to send and receive messages using the engine’s internal communication bus.

8. Avoid Slate Unless Building a GUI

While you can use Slate in a Program target (like the Project Launcher does), avoid it for console utilities. Adding Slate and SlateCore dependencies pulls in the entire rendering and windowing architecture, which contradicts the “Blank” nature of the module and slows down iteration.