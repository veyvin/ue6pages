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

ngine animation system. It provides a centralized way to manage project-wide defaults for asset importing, animation compression, and naming conventions. By adjusting settings within this module, you ensure that every animation asset in your project—from skeletal meshes to animation sequences—adheres to a consistent technical standard.

This module is primarily interacted with via Project Settings > Engine > Animation, where the values are stored in the project’s DefaultEngine.ini file.

Practical Usage Tips & Best Practices
1. Define Global Bone Compression Defaults

Instead of manually setting compression on every imported clip, use the Default Bone Compression Settings property. By choosing a high-quality, performant codec like ACL (Anim Compression Library) as the global default, you ensure that all new assets are optimized for memory and CPU immediately upon import.

2. Standardize Custom FBX Attributes

If your pipeline uses custom data from DCC tools (like Maya or Houdini) to drive gameplay, use the Bone Custom Attribute Names array. By defining names like Footstep_L or Weapon_State here, the engine will automatically search for and import these as animation curves, eliminating the need to manually add them to every sequence.

3. Optimize with Bone Names for Custom Attributes

If you only need custom data from specific bones (e.g., the root or hand_r), add those bone names to the Bone Names with Custom Attributes list. This tells the importer to ignore extra data on other bones, which reduces the final memory footprint of the animation asset and keeps the AnimGraph execution flow clean.

4. Enable Zero-Ticking for Performance

In the Performance section, you can toggle Zero-Ticking. When enabled, the engine will perform an initial animation tick immediately upon a Skeletal Mesh’s initialization. This prevents “pop” artifacts where a character might appear in a T-pose for one frame before the first update, ensuring a smooth visual experience when actors are spawned.

5. Manage Attribute Blend Modes

Use the Custom Attribute Blend Types setting to define how metadata blends during transitions. For example, if you have a “Status” string attribute, you may want to set it to Override so the highest-weighted animation wins, rather than trying to interpolate non-numeric data which could lead to logic errors.

6. Automate Timecode Mapping

For virtual production or high-end cinematics, use the User Defined Timecode Property Names section. By mapping your DCC’s timecode attribute names (like TCFrame or TCHour) here, Unreal will automatically sync the animation’s internal clock with the source file, which is essential for multi-take alignment in Sequencer.

7. Global Curve Import Settings

To maintain a clean project, configure the Alternative Interpolation Threshold and Precision settings. Lowering the precision can help the engine “decimate” or eliminate unnecessary keys in curves that have nearly identical values, significantly reducing the memory cost of thousands of animation files across the project.

8. Utilize Animation Groups for Synchronization

Use the settings to pre-define Sync Groups. By standardizing names like “WalkRun” or “Combat” at a project level, you ensure that different animators and designers use the same markers, allowing the engine to successfully sync foot-plants and loops across different animation clips in a Blend Space.