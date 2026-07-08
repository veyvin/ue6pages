---
layout: default
title: MainFrame
---

<!-- ai-generation-failed -->

<h1>MainFrame</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/MainFrame/MainFrame.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, ApplicationCore, Core, CoreUObject, DesktopPlatform, DeveloperToolSettings, DeviceProfileEditor, Documentation, EditorFramework, EditorStyle, Engine, EngineSettings, HTTP, InputCore, InterchangeCore, InterchangeEngine, LauncherServices, MessageLog, Projects, RHI, RenderCore, Slate, SlateCore, SourceControl, SourceControlWindows, TargetPlatform, ToolMenus, ToolWidgets, TranslationEditor, UATHelper, UndoHistoryEditor, UnrealEd, WebBrowser, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

t manages the primary application window and the overall lifecycle of the Unreal Editor’s user interface. It acts as the “root” of the editor’s Slate-based UI, providing a central point for handling the main window’s creation, parenting, and shutdown.

Essentially, whenever you need to ensure your custom editor window is a “child” of the main Unreal window or you need to perform logic only after the editor’s UI is fully initialized, you use the MainFrame module.

Practical Usage Tips and Best Practices
Bind to OnMainFrameCreationFinished Never try to open complex custom windows or perform UI-heavy initialization in your module’s StartupModule() function. Instead, get the MainFrame module and bind a delegate to OnMainFrameCreationFinished. This ensures the editor’s root window exists and is ready to parent your content, which leads to the elimination of “null window” crashes during editor startup.
Correct Window Parenting When creating a standalone Slate window (via SNew(SWindow)), always use IMainFrameModule::Get().GetParentWindow() as the parent. This practice leads to the elimination of “floating” windows that get hidden behind the editor or fail to minimize/restore alongside the main Unreal Engine application.
Accessing the Global Tab Manager The MainFrame module is the gatekeeper for the editor’s root FTabManager. If you are building a custom workspace or an advanced layout that doesn’t use the standard AssetEditorToolkit, accessing the Tab Manager through the MainFrame facilitates the elimination of inconsistent UI behavior and allows your tabs to be docked properly in the main editor area.
Handle Shutdown with OnMainFrameRequestShutdown If your plugin needs to save data or prompt the user before the editor closes, bind to OnMainFrameRequestShutdown. This delegate allows you to intercept the closing process. Using this properly assists in the elimination of data loss by ensuring your cleanup logic runs before the engine begins tearing down core subsystems.
Verify Module Dependencies in Editor.Build.cs Because the MainFrame is an editor-specific module, it must only be included in Editor.Build.cs (not the runtime one). Adding "MainFrame" to your PrivateDependencyModuleNames is a prerequisite for the elimination of linker errors when trying to reference IMainFrameModule in your C++ code.
Use the MainFrame for Focus Management The module provides methods to set and get the focus of the main window. If you are developing a tool that requires specific input capture, using the MainFrame’s focus controls leads to the elimination of input conflicts where the editor viewport “steals” focus from your custom tool.
Safe Pointer Checking Always use FModuleManager::LoadModulePtr<IMainFrameModule>("MainFrame") and check for null before usage. Since this module only exists in the Editor, failing to guard these calls leads to the elimination of your game’s ability to run in “Standalone” or “Shipping” builds, as those configurations will not contain the MainFrame symbols.