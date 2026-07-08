---
layout: default
title: AnimationSettings
---

<!-- ai-generation-failed -->

<h1>AnimationSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AnimationSettings/AnimationSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ges the global configuration for Unreal Engine’s animation system. It provides a centralized class, UAnimationSettings, which allows teams to define project-wide standards for how animations are processed, compressed, and optimized.

What it is and What it’s used for

This module is primarily used to control the default behaviors of the animation pipeline. Instead of modifying every individual animation sequence, developers use this module to set global rules that the engine follows during import, compression, and runtime.

Primary uses include:

Default Compression: Setting the default Bone and Curve compression assets for the entire project.
Performance Toggles: Enabling or disabling global optimizations like “Zero-Ticking.”
Pipeline Consistency: Defining standard naming conventions for custom bone attributes and mirroring.
Project-Wide Recompression: Forcing a recomputation of all animation data when engine versions or compression algorithms change.
Practical Usage Tips and Best Practices
1. Set a Global Bone Compression Asset

Avoid leaving animations on the engine default settings. Create a custom Bone Compression Settings asset (using ACL or the engine’s per-track compressor) and assign it in Project Settings > Animation. This ensures every new animation imported into your project automatically uses your optimized settings, saving memory from day one.

2. Manage Mirror Data Tables

If your project uses animation mirroring, you can define the Mirror Data Table globally within these settings. This eliminates the need to manually assign a mirror table to every “Mirror” node in your Animation Blueprints, ensuring that left-to-right logic remains consistent across all characters.

3. Toggle “Zero-Ticking” for Optimization

The bTickAnimationOnSkeletalMeshInit setting (Zero-Ticking) controls whether a mesh evaluates its animation immediately upon being spawned. Disabling this can improve performance when spawning many actors at once, though you should verify that it doesn’t cause a “pop” in the character’s pose on their first visible frame.

4. Access Settings via C++

You can access these global settings in C++ to drive custom tools or logic. Use the GetDefault<UAnimationSettings>() function to read project-wide values, such as the list of custom bone attributes, ensuring your custom plugins stay synchronized with the rest of the project.

5. Define Custom Attribute Names

If your pipeline relies on custom data baked into bones (like weapon kick values or foot-step metadata), add these names to the User Defined Attributes list in the Animation Settings. This ensures the engine recognizes and imports these attributes consistently across different FBX files.

6. Use the Version Property for Recompression

The CompressionVersion integer is a powerful tool for large-scale optimization. If you update your compression settings and want to apply them to thousands of existing assets, incrementing this version number will trigger a full recompression of all animations in the project during the next cook or when the “Recompress” commandlet is run.

7. Standardize Curve Compression

Just like bone data, curves (used for morph targets or material parameters) can take up significant memory. Use the Animation Settings to point to a default Curve Compression Settings asset. This helps eliminate redundant keyframes in curves that don’t change frequently, reducing the final build size of your project.

8. Configure Attribute Blend Types

You can define how custom attributes are blended during transitions (e.g., Override, Accumulate, or Blendable). Setting these globally prevents unexpected behavior when two animations with the same custom attribute cross-fade, ensuring that your gameplay-driven data remains predictable.