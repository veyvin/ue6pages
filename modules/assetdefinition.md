---
layout: default
title: AssetDefinition
---

<!-- ai-generation-failed -->

<h1>AssetDefinition</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AssetDefinition/AssetDefinition.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

real Engine 5 that defines how custom asset types appear and behave within the Editor. It is the successor to the legacy IAssetTypeActions system.

By inheriting from UAssetDefinition, developers can control an asset’s display name, color, categorization, thumbnail behavior, and context menu actions. Unlike the old system, which required manual registration in a module’s startup code, the AssetDefinition system is discovery-based; the engine automatically finds these classes via the reflection system.

Practical Usage Tips and Best Practices
1. Inherit from UAssetDefinitionDefault

For most custom assets, you should inherit from UAssetDefinitionDefault instead of the base UAssetDefinition. This provides a standard implementation for the most common editor tasks, such as opening the asset, which saves you from writing repetitive boilerplate code.

2. Utilize Deep Categorization

The modern system supports complex sub-menus in the “Create Asset” menu. Use FAssetCategoryPath to organize your tools logically (e.g., Game > Magic > Spells). This prevents your top-level menus from becoming cluttered and helps designers locate specific data types quickly.

3. Implement Context Menu Actions

Use the GetContextMenuActions override to add custom right-click options to your asset. This system is more robust than the legacy one, allowing you to pass a UAssetDefinitionContextMenuContext to bind complex logic, such as “Export to JSON” or “Validate Data,” directly to the asset in the Content Browser.

4. Define Visual Identity

Customize the visual representation of your asset using GetAssetColor() and GetThumbnailBrushName(). Giving unique colors to different data types (e.g., green for “Abilities,” orange for “Stats”) allows for rapid visual scanning of folders and reduces the risk of accidental asset “elimination” (deletion) caused by misidentification.

5. Keep Definitions in Editor Modules

UAssetDefinition classes should always reside in an Editor Module. Since they depend on Editor-only logic and headers (like UnrealEd), placing them in a Runtime module will cause compilation failure during the packaging process. Reference your Runtime class using GetAssetClass().

6. Leverage Automatic Discovery

Since these are UObjects, you do not need to manually call RegisterAssetTypeActions. As long as your module is loaded, the UAssetDefinitionRegistry will find your class automatically. This eliminates the “forgot to register” bugs common in earlier versions of Unreal.

7. Filter with Asset Registry Tags

The AssetDefinition system works closely with the Asset Registry. When defining how assets are filtered or searched, ensure that critical data properties in your runtime class are marked as AssetRegistrySearchable. This allows the Editor to display metadata in tooltips or column views without fully loading the asset.

C++ Implementation Example

To create a definition for a custom runtime class UMyWeaponData:

MyAssetDefinition.h

C++
	virtual FAssetCategoryPath GetAssetCategories() const override 

	{ 

	    return FAssetCategoryPath(NSLOCTEXT("MyGame", "WeaponCat", "MyGame"), NSLOCTEXT("MyGame", "SubCat", "Melee")); 

	}

	```

	 

	#### 3. Define Context Menu Actions via `GetContextMenuActions`

	The new system uses a more robust approach for context menu extensions. Instead of returning a list of names, you override `GetContextMenuActions` to provide `UAssetDefinitionContextMenuContext`. This allows you to bind complex logic, including sub-menus and dynamic visibility based on the selected asset's state.

	 

	#### 4. Automatic Discovery via CDO

	You no longer need to manually register your asset actions in `StartupModule()`. The engine’s `UAssetDefinitionRegistry` automatically discovers and registers any `UAssetDefinition` classes found in loaded modules during the Editor’s startup phase. This simplifies module maintenance and reduces code bloat in your module classes.

	 

	#### 5. Separating Editor and Runtime Modules

	Ensure your `UAssetDefinition` classes live in an **Editor-only module**. Since these classes inherit from Editor-specific libraries, placing them in a runtime module will cause packaging errors. Reference your runtime class using `GetAssetClass()` to bridge the two.

	 

	#### 6. Customizing Visual Identity

	Use `GetAssetColor()` and `GetThumbnailBrushName()` to make your assets instantly recognizable. Providing a unique color and icon for custom data assets (like a "SkillData" or "ItemTable") helps designers navigate the Content Browser significantly faster by providing clear visual cues.

	 

	#### 7. Performance-Minded Filtering

	`UAssetDefinition` works closely with the **Asset Registry**. When implementing custom filtering or search behavior, ensure your asset properties are marked as `AssetRegistrySearchable`. This allows the `AssetDefinition` logic to query metadata without needing to fully load the asset into memory.

	 

	---

	 

	### C++ Implementation Example

	 

	To define a custom asset type, create a class in your Editor module:

	 

	**MyAssetDefinition.h**

	```cpp

	#include "AssetDefinitionDefault.h"

	#include "MyAssetDefinition.generated.h"

	 

	UCLASS()

	class MYEDITOR_API UAssetDefinition_MyCustomAsset : public UAssetDefinitionDefault

	{

	    GENERATED_BODY()

	 

	public:

	    // Link this definition to your runtime class

	    virtual TSoftClassPtr<UObject> GetAssetClass() const override { return UMyCustomRuntimeClass::StaticClass(); }

	    

	    virtual FText GetAssetDisplayName() const override { return INVTEXT("My Custom Asset"); }

	    virtual FLinearColor GetAssetColor() const override { return FLinearColor(0.2f, 0.8f, 0.4f); }

	    

	    // Define where it appears in the "Right Click > Create" menu

	    virtual FAssetCategoryPath GetAssetCategories() const override 

	    { 

	        return FAssetCategoryPath(INVTEXT("My Tools")); 

	    }

	};

	```

	 

	**Project.Build.cs (Editor Module)**

	```csharp

	PublicDependencyModuleNames.AddRange(new string[] { 

	    "Core", 

	    "CoreUObject", 

	    "Engine", 

	    "AssetDefinition", // Required for UAssetDefinition

	    "UnrealEd" 

	});

	```

	 

	### Best Practices & Performance

	*   **Avoid Logic in Definitions:** Treat `UAssetDefinition` as metadata. Do not perform heavy computations or file I/O inside its methods.

	*   **Migration:** If you are upgrading from UE4, prioritize moving your `IAssetTypeActions` to `UAssetDefinition`. The engine still supports the old way for compatibility, but newer Editor features (like certain Content Browser filters) may only work with the new system.

	*   **Icon Selection:** Use existing Editor brushes for icons (e.g., `ClassIcon.StaticMesh`) to maintain visual consistency with the rest of the engine unless a custom brand-new icon is strictly necessary.
Copy code

MyEditorModule.Build.cs

C#
	PublicDependencyModuleNames.AddRange(new string[] { 

	    "Core", 

	    "CoreUObject", 

	    "AssetDefinition", // Required module

	    "UnrealEd" 

	});
Copy code
Performance & Best Practices
Avoid Complex Logic: The methods in UAssetDefinition are called frequently by the UI. Do not perform heavy file operations or complex calculations inside functions like GetAssetDisplayName.
Icon Selection: Use existing Editor brushes where possible to keep a consistent aesthetic with the engine.
Migration: If you are upgrading a project from UE4, prioritizing the migration of IAssetTypeActions to UAssetDefinition will ensure compatibility with the latest Content Browser features and future engine updates.