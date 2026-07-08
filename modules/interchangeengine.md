---
layout: default
title: InterchangeEngine
---

<!-- ai-generation-failed -->

<h1>InterchangeEngine</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Interchange/Engine/InterchangeEngine.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetRegistry, Core, CoreUObject, DeveloperSettings, Engine, InterchangeCore, Json, JsonUtilities, MeshDescription, SkeletalMeshDescription, SkeletalMeshUtilitiesCommon, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ource/Runtime/Interchange/Engine, this module is file-format agnostic and operates asynchronously. It replaces the legacy, rigid import pathways (like the old FBX importer) with a modular pipeline where data is first converted into an intermediary “Node Graph” before being built into Unreal assets by factories.

Primary uses include:

Asynchronous Importing: Running import tasks in the background to ensure the elimination of editor freezes during large asset ingestions.
Pipeline Management: Coordinating “Pipeline Stacks” that allow developers to inject custom logic (via Blueprints or Python) during the import process.
Format Translation: Managing “Translators” for formats like FBX, GLTF, OBJ, and MaterialX, ensuring they all follow a unified data structure.
Runtime Support: Enabling the engine to import 3D models or textures at runtime in shipped builds, not just within the Editor.
Practical Usage Tips and Best Practices
1. Customize via Pipeline Stacks

Instead of modifying engine code, create a Blueprint Interchange Pipeline. This allows you to hook into the ScriptedPostImportPipeline to automate tasks like renaming assets, assigning default materials, or setting up collision automatically. This leads to the elimination of repetitive manual setup for every imported mesh.

2. Leverage Asynchronous Imports for Large Scenes

Interchange is designed to be non-blocking. When importing large scenes via the Interchange Manager, you can continue working in the Editor while the “Node Graph” is being built in the background. Monitor the progress in the Asynchronous Import Task window to manage your workflow efficiency.

3. Use the “Basic Layout” for Simplicity

The Interchange import dialog can be complex. Use the Basic Layout toggle in the configuration window to show only the most essential settings (like Scale and Rotation). This is a best practice for artist-facing workflows to ensure the elimination of confusion caused by low-level technical toggles.

4. Enable Experimental FBX Support for Testing

While FBX support is becoming standard, you may need to enable it via console commands in older 5.x versions (Interchange.FeatureFlags.Import.FBX 1). Testing your FBX files through Interchange is a best practice to prepare for the eventual elimination of the legacy FBX importer.

5. Verify Node Graphs with the Visualizer

If an asset imports incorrectly, use the Interchange Pipeline Configuration window to inspect the intermediary nodes. This allows you to see if the error happened during “Translation” (reading the file) or “Factory” (creating the Unreal asset), which is critical for debugging complex scene hierarchies.

6. Optimize Runtime Imports

When using Interchange at runtime, keep your pipeline stacks lean. Disable unnecessary features like “Generate Lightmap UVs” or “Build Adjacency Buffer” if they aren’t needed for your specific use case. This ensures the elimination of excessive CPU overhead and memory spikes on player machines.

7. Set Project-Wide Defaults

In Project Settings > Interchange, you can define default pipeline stacks for different file types. Setting these up at the start of a project ensures that every team member uses the same import settings, leading to the elimination of “drift” where different artists have slightly different asset configurations.

8. Strategic Elimination of Stale Translators

If your project only uses GLTF, you can disable other Interchange translators in the Plugins menu. This reduces the engine’s memory footprint and speeds up the initial “format check” when dragging files into the Content Browser, keeping your import pipeline as fast as possible.