---
layout: default
title: GameProjectGeneration
---

<!-- ai-generation-failed -->

<h1>GameProjectGeneration</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/GameProjectGeneration/GameProjectGeneration.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AddContentDialog, Analytics, AppFramework, ApplicationCore, AssetTools, AudioMixer, AudioMixerCore, BuildSettings, ClassViewer, ContentBrowserData, Core, CoreUObject, DesktopPlatform, EditorFramework, EditorSubsystem, EditorViewport, EditorWidgets, Engine, EngineSettings, HardwareTargeting, InputCore, LauncherPlatform, Projects, RenderCore, Slate, SlateCore, SourceControl, TargetPlatform, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

of template files, generates .uproject files, configures initial DefaultGame.ini settings, and interfaces with the Unreal Build Tool (UBT) to generate project files (like .sln or .xcodeproj). Its primary goal is to “eliminate” the manual labor involved in setting up the directory structures and boilerplate code required for a functional Unreal Engine project.

Practical Usage Tips and Best Practices
Create Custom Project Templates
You can create your own templates by placing a project in the Templates folder of the engine. This module reads the TemplateDefs.ini file in those folders. This is a best practice for “eliminating” repetitive setup tasks when starting multiple projects that share the same base plugins or architecture.
Override Class Generation via Templates
The module uses .template files (found in Engine/Content/Editor/Templates) to generate new C++ classes. By modifying or adding to these, you can “eliminate” the need to manually add company-standard headers, includes, or logging macros every time a developer adds a new Actor or Character class.
Add Module Dependencies for Editor Tools
If you are building an editor plugin that needs to automate project creation or add classes programmatically (e.g., a “Project Initializer” tool), you must add "GameProjectGeneration" to your Build.cs. This “eliminates” compilation errors when accessing the FGameProjectGenerationModule interface.
Use FProjectDescriptor for Metadata
This module provides the FProjectDescriptor class, which allows you to programmatically read or modify a .uproject file. Use this to “eliminate” manual JSON editing when you need to toggle plugins or change the engine version of a project via an external script or tool.
Automate Class Creation via GameProjectGenerationUtils
Instead of manually creating .h and .cpp files, use the GameProjectGenerationUtils::AddCodeToProject function. This ensures the files are placed in the correct Source subfolders and that the project files are refreshed, “eliminating” the risk of “File Not Found” errors during the next compilation.
Validate Project Names Early
If building a custom launcher, use this module’s validation logic to check project names before creation. This “eliminates” failures caused by illegal characters, reserved Windows filenames, or names that exceed the maximum path length allowed by the OS.
Refresh Project Files Programmatically
After adding files via code, use this module to trigger a project file generation. This “eliminates” the friction of forcing the user to right-click the .uproject file in Windows Explorer to “Generate Visual Studio project files” manually.
Handle Multi-Module Projects
When adding a class to a project with multiple modules, this module provides the UI for the user to select the target module. In your own tools, ensure you specify the ModuleName to “eliminate” ambiguity, ensuring the code is injected into the correct Source folder.