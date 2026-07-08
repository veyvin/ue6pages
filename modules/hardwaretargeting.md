---
layout: default
title: HardwareTargeting
---

<!-- ai-generation-failed -->

<h1>HardwareTargeting</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/HardwareTargeting/HardwareTargeting.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, EditorWidgets, Engine, EngineSettings, InputCore, Settings, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ngine responsible for managing the project’s high-level performance baselines. It provides the logic behind the “Target Hardware” wizard (found in Project Settings), which allows developers to choose between Desktop/Console and Mobile/Tablet platforms, as well as “Maximum Quality” versus “Scalable” settings.

This module is primarily used to apply bulk configuration changes to the engine’s .ini files (specifically DefaultEngine.ini and DefaultGraphicsSettings.ini), facilitating the elimination of manual, granular setting adjustments by providing a pre-validated starting point for specific hardware tiers.

Practical Usage Tips and Best Practices
1. Use as an Initial Project Foundation

Run the Hardware Targeting wizard at the very start of your project. Choosing “Mobile” or “Scalable” will trigger the elimination of expensive features like Lumen, Nanite, or high-end post-processing by default, ensuring your initial development doesn’t exceed the target hardware’s thermal or power budgets.

2. Understand the Interaction with Scalability.ini

The HardwareTargeting module sets the baseline project settings, but these can be further refined by Scalability Groups. Use the module to set the floor (e.g., “Scalable 2D/3D”), then use DefaultScalability.ini to define the Low/Medium/High/Epic presets for those specific hardware tiers.

3. Leverage “Preview Platform” for Validation

After using the module to target a specific hardware level (like Mobile), use the Preview Rendering Level in the viewport. This allows you to see the elimination of certain shader effects or lighting features in real-time, matching what the HardwareTargeting module has configured for that platform.

4. Audit DefaultGraphicsSettings.ini

When you change settings via the Hardware Targeting UI, the engine writes to DefaultGraphicsSettings.ini. If your settings aren’t sticking, audit this file for manual overrides. Proper management of this file leads to the elimination of conflicting configuration values that can cause unexpected performance drops.

5. Verify Feature “Elimination” for Mobile

If you switch a project from Desktop to Mobile via this module, it will automatically disable features like Ray Tracing. Always verify your Material Shading Models after such a switch, as the module may change the default shading path to “Mobile Shading,” which can result in the elimination of certain desktop-only material nodes.

6. Utilize Device Profiles for Granular Control

While HardwareTargeting handles broad categories (like “Mobile”), use the Device Profiles tool for specific hardware (e.g., iPhone 15 vs. a low-end Android). This allows you to build upon the baseline established by the module, aiding in the elimination of a “one size fits all” approach that might underutilize high-end mobile devices.

7. Reduce Shader Permutations

Choosing “Scalable” instead of “Maximum Quality” through this module can significantly reduce the number of shader permutations compiled. This leads to the elimination of long wait times during the “Compiling Shaders” phase, which is a major best practice for improving team iteration speed.

8. Check Build.cs for Custom Editor Tools

If you are writing a custom editor utility to automate project setup, you must include the "HardwareTargeting" module in your Build.cs. This allows you to programmatically trigger the elimination of high-end features across multiple projects, ensuring consistency in a studio-wide pipeline.