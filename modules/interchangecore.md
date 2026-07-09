---
layout: default
title: InterchangeCore
---

<!-- ai-generation-failed -->

<h1>InterchangeCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Interchange/Core/InterchangeCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core, CoreUObject, Json, JsonUtilities, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

he final Unreal Assets).

Practical Usage Tips & Best Practices
1. Prefer Asynchronous Imports to Prevent Editor Deadlocks

Unlike legacy importers that block the main thread, Interchange is designed to run tasks in the background.

Best Practice: When writing custom C++ import tools, always utilize the UInterchangeManager::ImportAsset async workflow. This ensures the elimination of editor “freezes” during large asset ingestions, allowing developers to continue working while textures or meshes are processed.
2. Utilize the Pipeline Stack for Modular Logic

Interchange uses a “Pipeline Stack” which allows you to chain multiple logic passes together.

Tip: Instead of creating one giant import script, break your logic into small, reusable Interchange Pipelines (e.g., one for naming conventions, one for collision setup). This modularity facilitates the elimination of redundant code across different project departments.
3. Access Intermediate Data via Node Containers

The framework converts source files into an intermediate Interchange Base Node Container before creating assets.

Best Practice: Perform all data validation and attribute modifications on the UInterchangeBaseNodeContainer during the ExecutePipeline stage. Modifying data here, before the factory pass, results in the elimination of expensive post-import fix-up steps.
4. Enable the Interchange Framework for FBX (Experimental)

While Interchange is the default for formats like glTF, FBX still defaults to the legacy path in some versions.

Tip: Use the console command Interchange.FeatureFlags.Import.FBX true to test the new framework. Moving to Interchange for FBX assists in the elimination of legacy bugs and provides more granular control over how skeletal meshes and animations are processed.
5. Leverage Python for Pipeline Customization

InterchangeCore is fully exposed to Unreal’s Python API, making it highly accessible for pipeline technical artists.

Best Practice: Use Python to create custom UInterchangePythonPipeline scripts that enforce project-specific rules (like auto-assigning Materials based on FBX metadata). This leads to the elimination of manual error-prone settings adjustments by artists during the import dialog.
6. Use Factories for Consistent Asset Creation

The Interchange Factory nodes are responsible for the final conversion into UStaticMesh, UTexture, etc.

Tip: If you are supporting a custom proprietary file format, inherit from UInterchangeTranslator but reuse the existing engine Factories. Reusing built-in factories ensures the elimination of compatibility issues with standard engine features like Nanite or Virtual Texturing.
7. Set Up Per-Project Pipeline Presets

You can define specific pipeline stacks in the Project Settings under Plugins > Interchange.

Best Practice: Create different presets for “Characters,” “Environment,” and “Vehicles.” Selecting the correct stack during import ensures the elimination of incorrect LOD settings or missing collision hulls, as the settings are pre-validated for that asset type.
8. Monitor Results with the Interchange Result Handler

The framework includes a robust error and warning reporting system that tracks issues throughout the translation and factory phases.

Tip: Always inspect the UInterchangeResultsContainer after an import operation. Proactively checking this container facilitates the elimination of “silent failures,” where an asset appears in the Content Browser but contains corrupted or missing geometry data.