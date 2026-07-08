---
layout: default
title: BlankModule
---

<!-- ai-generation-failed -->

<h1>BlankModule</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/BlankModule/BlankModule.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

oper module located within the engine source at Engine/Source/Developer/BlankModule. It serves as the foundational template and a “skeleton” for developers to reference or duplicate when creating new C++ modules from scratch.

Description

In Unreal Engine’s modular architecture, every major feature is encapsulated in a module. The BlankModule provides the simplest possible implementation of the IModuleInterface. It contains no functional gameplay or engine code; instead, it provides the necessary directory structure (Public/Private), a .Build.cs file, and the basic C++ macros (IMPLEMENT_MODULE) required for the Unreal Build Tool (UBT) to recognize and compile a new unit of code. It is essentially the “Hello World” of Unreal Engine modularity.

Practical Usage Tips and Best Practices
1. Use as a Template for New Systems

When you need to create a new standalone system (like a custom dialogue manager or a specialized physics wrapper), don’t start from an empty file. Copy the structure of BlankModule. This ensures you have the correct Public and Private folder separation and the IMPLEMENT_MODULE macro, which are required for the module to be loaded by the engine.

2. Master the IModuleInterface

The core of any module is the IModuleInterface. Use the StartupModule() and ShutdownModule() functions to handle initialization and cleanup. For example, if your module needs to register a custom asset type or a singleton, StartupModule() is the place to do it.

C++
	virtual void StartupModule() override { /* Initialization logic */ }

	virtual void ShutdownModule() override { /* Cleanup logic */ }

	```

	 

	#### 3. Define the Module Type Correctly

	In your `.uproject` or `.uplugin` file, you must specify the module's type. By default, **BlankModule** is a "Developer" module. 

	*   **Runtime:** Code that runs in the final game.

	*   **Editor:** Code that only runs in the Unreal Editor.

	*   **Developer:** Code used for tools and debugging; it is compiled in "Development" builds but **eliminated** in "Shipping" builds.

	 

	#### 4. Strictly Control Exports with [MODULENAME]_API

	To access a class or function from another module, you must mark it with the `[YOURMODULE]_API` macro. This handles the DLL export/import logic. Keeping as many classes as possible inside the `Private` folder (without the API macro) helps minimize "binary bloat" and improves compile times.

	 

	#### 5. Minimize Private Dependencies

	In your `[ModuleName].Build.cs`, keep your `PrivateDependencyModuleNames` as lean as possible. Including large modules like `Engine` or `UnrealEd` when you only need `Core` will significantly slow down your build times. Start with `Core` and `CoreUObject`, and only add others as needed.

	 

	#### 6. Leverage Loading Phases

	Use the `LoadingPhase` setting in your `.uproject` file to control when your module starts. If your module provides low-level utilities used by other systems, set it to `PreDefault`. If it's a high-level UI system, `Default` or `PostDefault` is usually sufficient. This helps eliminate initialization order issues.

	 

	#### 7. Use for "Third-Party" Wrappers

	If you are integrating a third-party library (like a custom JSON parser), the **BlankModule** structure is ideal for creating a "Wrapper Module." This keeps the external code isolated from your main gameplay logic, allowing you to update or replace the library without touching your game's primary code.

	 

	#### 8. Improve Iteration via Modular Builds

	By splitting your project into multiple small modules (rather than one giant "Primary Game Module"), the Unreal Build Tool only needs to recompile the specific module you changed. This can reduce a 2-minute recompile down to a few seconds, greatly improving your daily development workflow.
Copy code
3. Define the Module Type Correctly

In your .uproject or .uplugin file, you must specify the module’s type. By default, BlankModule is a “Developer” module.

Runtime: Code that runs in the final game.
Editor: Code that only runs in the Unreal Editor.
Developer: Code used for tools and debugging; it is compiled in “Development” builds but eliminated in “Shipping” builds.
4. Strictly Control Exports with [MODULENAME]_API

To access a class or function from another module, you must mark it with the [YOURMODULE]_API macro. This handles the DLL export/import logic. Keeping as many classes as possible inside the Private folder (without the API macro) helps minimize “binary bloat” and improves compile times.

5. Minimize Private Dependencies

In your [ModuleName].Build.cs, keep your PrivateDependencyModuleNames as lean as possible. Including large modules like Engine or UnrealEd when you only need Core will significantly slow down your build times. Start with Core and CoreUObject, and only add others as needed.

6. Leverage Loading Phases

Use the LoadingPhase setting in your .uproject file to control when your module starts. If your module provides low-level utilities used by other systems, set it to PreDefault. If it’s a high-level UI system, Default or PostDefault is usually sufficient. This helps eliminate initialization order issues.

7. Use for “Third-Party” Wrappers

If you are integrating a third-party library (like a custom JSON parser), the BlankModule structure is ideal for creating a “Wrapper Module.” This keeps the external code isolated from your main gameplay logic, allowing you to update or replace the library without touching your game’s primary code.

8. Improve Iteration via Modular Builds

By splitting your project into multiple small modules (rather than one giant “Primary Game Module”), the Unreal Build Tool only needs to recompile the specific module you changed. This can reduce a 2-minute recompile down to a few seconds, greatly improving your daily development workflow.