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

real Engine source code. It is designed to serve as a starting point for developers who need to create a new C++ module from scratch. It contains the bare-essential file structure (.Build.cs, .h, and .cpp) and the required macros to register a module with the engine’s ModuleManager, ensuring it is correctly loaded, initialized, and unloaded by the engine.

Practical Usage Tips & Best Practices
1. Use as a Foundation for Encapsulation

The primary purpose of a new module is to separate logic. Use the BlankModule structure to move systems (like a custom AI system or a specialized math library) out of your primary game module. This leads to the elimination of “monolithic” codebases where every class depends on every other class, making your project much easier to maintain.

2. Follow the Standard Directory Structure

When implementing your module based on the blank template, strictly adhere to the Public and Private folder convention:

Public: Contains header files (.h) that other modules need to see.
Private: Contains the .cpp implementation files and headers that should remain internal. This structure is required for the “Include What You Use” (IWYU) optimization system to work effectively.
3. Use the Correct Module Implementation Macro

For a simple module that doesn’t need special startup or shutdown logic, use the FDefaultModuleImpl class within the implementation macro: IMPLEMENT_MODULE(FDefaultModuleImpl, YourModuleName); If you need to initialize a third-party library or register a custom style when the module loads, you must create a custom class that inherits from IModuleInterface instead.

4. Manage Module Dependencies Wisely

In your new module’s .Build.cs file, only add the modules you absolutely need.

Best Practice: Add essential modules like Core and CoreUObject to PublicDependencyModuleNames. Add modules like Engine or InputCore to PrivateDependencyModuleNames if they are only used in your internal .cpp files. This helps in the elimination of circular dependencies.
5. Define a Module-Specific API Macro

To expose classes or functions from your new module to the rest of the project, you must use the YOURMODULENAME_API macro. Without this, you will encounter “unresolved external symbol” linker errors. The BlankModule setup reminds you to define this macro, which handles the complex dllexport/dllimport logic for different platforms.

6. Set the Appropriate Loading Phase

In your .uproject or .uplugin file, you must specify when your module should load.

Tip: Most gameplay modules use the Default phase. If your module provides low-level systems that other modules rely on, consider using PreDefault. This ensures your systems are initialized before the rest of the game logic begins.
7. Utilize for Editor-Only Logic

If you are creating custom tools or details panel customizations, use a BlankModule-style setup with the Type set to Editor in your plugin descriptor. This ensures that the code is only compiled for the Unreal Editor and is completely stripped out of your final shipping build, leading to the elimination of unnecessary code bloat in the executable.

8. Verify Module Loading via Console

After creating and compiling your new module, you can verify it is running correctly using the console command module list. This will show you every loaded module in the engine, its current memory usage, and its loading status, which is essential for debugging initialization failures.