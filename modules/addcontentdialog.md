---
layout: default
title: AddContentDialog
---

<!-- ai-generation-failed -->

<h1>AddContentDialog</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AddContentDialog/AddContentDialog.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, DesktopPlatform, DirectoryWatcher, EditorFramework, Engine, ImageWrapper, InputCore, Json, PakFile, Slate, SlateCore, ToolWidgets, WidgetCarousel</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nsible for the “Add Feature or Content Pack” interface. It allows developers to inject standardized templates (like the First Person or Third Person templates) or asset bundles (like Starter Content) into an existing project.

Technically, it manages the discovery of .upack files, parses their metadata, and handles the logic for migrating assets, C++ source files, and configuration settings into the current project’s directory structure.

1. Programmatic Invocation

You can trigger the Add Content Dialog from your own Editor Utility Widgets or C++ plugins. This is useful for creating custom project setup wizards for your team.

C++
	#include "IAddContentDialogModule.h"

	#include "Framework/Application/SlateApplication.h"

	#include "Modules/ModuleManager.h"

	 

	void FMyEditorTool::OpenAddContentWindow()

	{

	    // Load the module by name

	    IAddContentDialogModule& AddContentModule = FModuleManager::LoadModuleChecked<IAddContentDialogModule>("AddContentDialog");

	    

	    // Get the main frame window to use as a parent

	    TSharedPtr<SWindow> ParentWindow = FSlateApplication::Get().GetActiveTopLevelWindow();

	    

	    if (ParentWindow.IsValid())

	    {

	        AddContentModule.ShowDialog(ParentWindow.ToSharedRef());

	    }

	}

	```

	 

	### 2. Custom Feature Pack Discovery

	The module automatically scans the `Engine/FeaturePacks/` directory for `.upack` files. A `.upack` is essentially a renamed `.zip` file containing a compressed project structure. If you want to distribute custom company-wide templates, place your `.upack` files in this directory; the `AddContentDialog` module will detect and display them in the UI based on their internal manifest.

	 

	### 3. Understanding the Manifest.json

	Every feature pack relies on a `manifest.json` file inside the `.upack`. This file tells the `AddContentDialog` module how to display the pack. 

	- **Best Practice:** Always include a unique `Name`, `Description`, and `Thumbnail` path in your manifest so that users can identify your custom content easily within the dialog's grid view.

	 

	### 4. Handling Dependencies

	The module supports dependencies between packs. For example, if your "Advanced Physics Content" pack requires the "Starter Content" pack to function, you can define this in the manifest. The `AddContentDialog` will then prompt the user or automatically include the required dependencies during the injection process.

	 

	### 5. Extension via Content Source Providers

	The module architecture is extensible via the `IContentSourceProvider` interface. You can access the provider manager through `IAddContentDialogModule::Get().GetContentSourceProviderManager()`. This allows you to register custom logic for where content comes from—for example, pulling feature packs from a remote server or a network drive instead of the local `FeaturePacks` folder.

	 

	### 6. Managing C++ vs. Content-Only Packs

	The module distinguishes between Blueprint-based and C++-based feature packs. When a C++ pack is added, the module doesn't just copy assets; it can also trigger a project file regeneration (e.g., updating the `.uproject` and `.sln`) to ensure that new source files are compiled. 

	- **Tip:** When creating custom C++ packs, ensure your source folder structure exactly matches the expected layout, or the module may fail to link the new classes to the project.

	 

	### 7. Performance and Asset Merging

	When the dialog injects content, it uses the `UPackFactory` under the hood. 

	- **Best Practice:** Be aware that adding a pack that shares the same folder names as your project (e.g., `/Game/StarterContent/`) will trigger a merge. To avoid overwriting existing work, ensure your custom feature packs use unique, namespaced root folders (e.g., `/Game/StudioName/FeatureName/`).

	 

	### 8. Module Dependencies in Build.cs

	If you are writing C++ code that interacts with this module, you must include it in your editor module's `Build.cs` file. Note that since this is an editor-only module, it should only be added to `Editor` type modules.

	 

	```csharp

	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "AddContentDialog" });

	}

	
Copy code
2. Custom Feature Pack Location

The module automatically scans the Engine/FeaturePacks/ directory for .upack files. To distribute studio-wide templates, place your custom .upack files here. The module will automatically detect them and display them in the UI based on their internal manifest.json.

3. Use Unique Namespaces to Prevent Overwrites

When the module injects content, it merges folders. If your feature pack and your project both use /Game/Materials/, the pack might overwrite existing assets.

Best Practice: Always root your feature pack assets in a unique subfolder (e.g., /Game/FeaturePacks/MyCustomPack/) to ensure no project assets are accidentally eliminated or replaced during the merge.
4. Optimize via .upack Compression

A .upack file is essentially a compressed archive. For large asset libraries, ensure your feature packs are optimized and compressed before deployment. The AddContentDialog module uses the UPackFactory to extract these; smaller file sizes lead to faster “Add to Project” operations and less disk bloat.

5. Managing C++ Template Dependencies

The module handles the transition between Blueprint and C++ projects. If you add a C++ feature pack to a Blueprint-only project, the module will prompt to add the necessary source code folders.

Tip: Ensure your C++ pack includes a valid Config folder within the pack to ensure Input Mappings and Project Settings are updated alongside the code.
6. Dependency Declaration in Manifests

The manifest.json within a feature pack allows you to list dependencies. If your custom tool requires the “Starter Content” pack, list it in the manifest. The AddContentDialog module will check if the dependency exists and prompt the user to add it if it’s missing, ensuring the injected logic doesn’t break.

7. Clean Up Redirectors After Addition

After using the Add Content Dialog to bring in a large pack, it is a best practice to right-click your Content folder and select Fix Up Redirectors. While the module is efficient, moving or renaming files shortly after a pack injection can sometimes leave broken references if redirectors aren’t cleaned up.

8. Build.cs Configuration

Because this is an Editor-only module, you must gate it correctly in your Build.cs file. Including it in a Runtime module will cause packaging errors.

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "AddContentDialog" });

	}
Copy code