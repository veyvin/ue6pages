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

thin the Unreal Engine source tree (Engine/Source/Developer/BlankModule).

Description and Purpose

The BlankModule serves as the definitive reference template for creating new C++ modules in Unreal Engine. It contains the bare minimum file structure and code required for a module to be recognized and compiled by the Unreal Build Tool (UBT). Its primary purpose is to provide a “clean slate” for developers to copy and rename when they need to extend engine functionality, create custom editor tools, or organize project-specific code into decoupled units.

Practical Usage Tips and Best Practices
Use as a Blueprint for New Modules
When your project grows too large for a single module, copy the structure of BlankModule (the .Build.cs, .h, and .cpp files) to create a new folder in your Source directory. This is the fastest way to ensure your new module follows Epic’s expected directory structure and macro usage.
Identify Minimal Header Requirements
Study the BlankModule.h to see the minimal implementation of IModuleInterface. For most custom modules, you only need to override StartupModule() and ShutdownModule() to manage the lifecycle of your systems or register custom settings.
Keep Dependencies Lean
The BlankModule.Build.cs starts with minimal dependencies (usually just Core). Follow this example by only adding modules to your PublicDependencyModuleNames that are absolutely necessary. This helps eliminate circular dependencies and keeps your compile times fast.
Correct Naming Conventions
When duplicating the blank module, remember to replace all instances of BLANKMODULE_API with your new MODULENAME_API. Failing to update this macro will lead to linker errors when you try to access your classes from other modules.
Implementing Lifecycle Logic
Use the StartupModule function to initialize singletons or register delegates. For example, if you are building a system that tracks player elimination stats globally, you would initialize your data tracker here to ensure it is ready before any gameplay actors are spawned.
Choose the Right Module Type
While the BlankModule is located in the Developer folder, your derivative module should be categorized correctly in your .uproject or .uplugin file. Use Runtime for gameplay code, Editor for tools, and Developer only for code that should be excluded from shipping builds.
Toggle Functionality Safely
Use the ShutdownModule to perform clean-up. If your module allocated memory or spawned background threads to process elimination VFX or data logs, you must eliminate those resources here to prevent memory leaks or crashes when the engine closes or the module is reloaded (Hot Reload).
Reference for IWYU (Include What You Use)
The BlankModule follows modern Unreal Engine standards. Use it as a guide for how to set up your private PCH (Precompiled Header) and how to include only the specific headers needed for your source files, rather than including “Engine.h” which slows down the build process.