---
layout: default
title: CookedEditor
---

<!-- ai-generation-failed -->

<h1>CookedEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/CookedEditor/CookedEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetRegistry, Core, CoreOnline, CoreUObject, Engine, NetCore, Projects, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

gap between the Unreal Editor and cooked content. Its primary purpose is to allow the Unreal Editor to load and utilize cooked data (assets already processed for a target platform like Windows, Console, or Mobile) rather than relying solely on raw source assets.

This is a critical component of “Modular Game Builds” and high-efficiency workflows (similar to UEFN). It allows developers to work in a hybrid environment where the core game or large plugins are loaded as optimized, read-only cooked binaries, significantly reducing memory usage and load times during editor sessions.

1. Enable Cooked Data Support in Project Settings

To allow the editor to recognize cooked content, you must explicitly enable it in your configuration.

Best Practice: Add the following to your DefaultEngine.ini:
ini
	[/Script/UnrealEd.CookerSettings]

	cook.AllowCookedDataInEditorBuilds=True

	s.AllowUnversionedContentInEditor=1
Copy code
This enables the underlying CookedEditor logic to mount and read .uasset and .uexp files that have already been through the cook process.
2. Use for Large-Scale World Iteration

In massive projects, loading the entire world from source can exceed RAM limits or take hours.

Tip: Use the CookedEditor module to load “Background” or “Static” layers of your world from cooked data. This allows level designers to iterate on a specific “Active” layer with source assets while the rest of the environment remains high-performance and lightweight.
3. Understand Read-Only Limitations

Assets loaded via the CookedEditor logic are generally read-only.

Constraint: You cannot open a cooked Material in the Material Editor or a cooked Mesh in the Static Mesh Editor. The module is designed for referencing and viewing content to facilitate faster iteration, not for modifying the underlying cooked binary.
4. Maintain Rigid Folder Structures

The CookedEditor module relies on internal path mapping to resolve references between cooked and source assets.

Best Practice: Never rename or move cooked assets manually once they are in the Saved/Cooked directory. If the folder structure does not match the original source path, the module will fail to resolve dependencies, resulting in “Missing Proxy” or “Failed to Load” errors.
5. Leverage for “Game Feature” Plugins

The module is a key enabler for Game Feature Plugins.

Tip: You can cook a specific feature plugin on a build farm and distribute it to the rest of the team. Using the CookedEditor module, developers can enable that plugin in their editor to test interactions without needing to compile the source code or process the raw assets of that specific feature.
6. Improve Editor Stability on High-End Projects

Because cooked assets are already optimized (e.g., textures are downscaled/compressed, meshes are stripped of editor-only data), they are much less likely to cause out-of-memory (OOM) crashes in the editor.

Best Practice: If your project is hitting 64GB+ of RAM usage in the editor, identify “Finalized” asset folders and load them as cooked content to eliminate memory bloat.
7. Monitor Versioning with “Unversioned” Content

Cooked content is often “unversioned” (stripped of the engine version to save space).

Tip: Ensure s.AllowUnversionedContentInEditor=1 is set. Without this, the CookedEditor module may reject cooked assets if the engine’s internal versioning has ticked up by even a minor revision, even if the binary format is still compatible.
8. Use for Rapid Play-In-Editor (PIE) Testing

The CookedEditor module speeds up PIE sessions by reducing the amount of on-the-fly processing the engine must do.

Best Practice: When testing complex levels, use the Cooked Editor workflow to verify that assets look and behave correctly in their “final” state (including platform-specific compression) without the overhead of a full package-and-deploy cycle.