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

gainst Unreal Engine’s core libraries.

It is used by developers as a starting point for creating lightweight, command-line utilities or background tools that need to leverage Unreal’s foundational systems (like the Task System, Logging, or File I/O) without the overhead of the full Engine, Renderer, or Slate UI.

Practical Usage Tips and Best Practices
1. Use for High-Performance Data Converters

BlankProgram is ideal for building standalone command-line tools that perform batch operations, such as converting custom proprietary file formats into Unreal-friendly formats. Because it doesn’t initialize the renderer or the world, it starts nearly instantly and uses minimal memory.

2. Strict Module Dependencies

Keep the Build.cs file lean. Usually, you only need to include "Core" and "Projects". Including "Engine" or "UnrealEd" will dramatically increase your executable size and compile time, defeating the purpose of a “Blank” program. If you need to manipulate assets, prefer "CoreUObject" over the full engine module.

3. Minimal Main Entry Point

A BlankProgram requires a manual main or WinMain entry point. Always use the GEngineLoop initialization macros or call FPlatformRuntimeStats::Setup() and FTaskGraphInterface::Startup() manually if you need multi-threading. This ensures the environment is set up correctly before your logic begins.

4. Automated Cleanup (Eliminate Leaks)

Since there is no AActor lifecycle or automatic Garbage Collection (unless you manually initialize the UObject system), you are responsible for memory management. Ensure you call FEngineLoop::AppPreExit() and FEngineLoop::AppExit() at the end of your main function to “eliminate” any hanging threads or file handles.

5. Leverage the Unreal Task System

Even without the full engine, you can use UE::Tasks::Launch or the TaskGraph within a BlankProgram. This allows you to write highly parallelized CLI tools that can utilize every core of a build server to process data, far outperforming standard single-threaded C++ scripts.

6. Target.cs Configuration

Ensure your Target.cs file is set to TargetType.Program. You must also set bBuildRequiresCookedData = false and bCompileAgainstEngine = false to ensure the build system doesn’t try to link in heavy gameplay frameworks that aren’t needed for a utility tool.

7. Command Line Argument Parsing

Use the FCommandLine::Get() and FParse utilities. These are part of the Core module and allow your program to handle flags (e.g., -input="path/to/file") using the same syntax and logic as the Unreal Editor, making it consistent with other Unreal commandlets.

8. Remote Execution and CI/CD

BlankProgram targets are perfect for Continuous Integration (CI) pipelines. Since they are small and independent, they can be distributed to build agents to perform pre-build validation or post-build packaging tasks without requiring a full engine installation on every node.

Minimal Program Template

To create a new tool based on this module, your primary .cpp file would look like this:

C++
	#include "RequiredProgramMainCPPInclude.h"

	#include "Framework/Application/SlateApplication.h"

	 

	IMPLEMENT_APPLICATION(MyCustomTool, "MyCustomTool");

	 

	int32 MyCustomToolMain(const TCHAR* CommandLine)

	{

	    // Start the engine core systems

	    FTaskGraphInterface::Startup(FPlatformMisc::NumberOfCores());

	    

	    UE_LOG(LogTemp, Display, TEXT("Utility tool started successfully!"));

	 

	    // Your custom logic here...

	    

	    // Shut down to eliminate hanging threads

	    FEngineLoop::AppPreExit();

	    FTaskGraphInterface::Shutdown();

	    

	    return 0;

	}
Copy code
Performance & Best Practices
Compile Times: Because these programs link against a limited set of modules, they compile significantly faster than the Editor. Use them for rapid prototyping of low-level algorithms.
Logging: Always initialize the GLog system if you want to use UE_LOG. Without it, your output will not appear in the console.
Static Linking: Be mindful of license requirements if you plan to distribute a standalone program created this way, as it may statically link parts of the Unreal Engine Core.