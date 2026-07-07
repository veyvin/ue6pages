---
layout: default
title: AnimationEditMode
---

<!-- ai-generation-failed -->

<h1>AnimationEditMode</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AnimationEditMode/AnimationEditMode.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorInteractiveToolsFramework, Engine, InteractiveToolsFramework, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

zed Animation Mode (Shift + 7) UI in Unreal Engine 5. It provides the framework for viewport-based animation authoring, specifically designed to work with Control Rig and Sequencer.

While standard modes are used for level editing, this module enables an animation-centric workflow by exposing tools like the Anim Outliner, Anim Details, and specialized viewport gizmos for manipulating bones and controls directly. It is the backend that allows animators to create, keyframe, and refine character motion entirely within the Unreal Editor.

1. Leverage the Anim Outliner for Hierarchy

The AnimationEditMode module introduces the Anim Outliner, which filters out all non-essential actors.

Tip: Use this to focus purely on your Control Rig hierarchy. It inherits the colors defined in your Control Rig asset, making it much faster to distinguish between Left (Red) and Right (Blue) limb controls compared to the standard World Outliner.
2. Isolate Selection with “Select” Mode

When Animation Mode is active, the module provides a “Select” toggle. Enabling this prevents you from accidentally selecting the floor, lights, or other level actors while you are animating. This effectively eliminates the frustration of losing your character selection while trying to click a small finger control in a crowded scene.

3. Use Constraints for Props

AnimationEditMode includes a dedicated Constraints panel. This allows you to dynamically attach objects (like a sword or a cup) to a character’s hand controls without manually managing complex attachment logic in Blueprints. These constraints are baked into the Sequencer track, ensuring the prop follows the animation perfectly.

4. Optimize Performance with FastPath

When working in the Animation Blueprint editor (which shares logic with this module), look for the Lightning Icon on nodes.

Best Practice: Ensure your logic uses FastPath by only connecting variables directly to node inputs without logic “breaks.” This allows the engine to skip the Blueprint Virtual Machine, significantly improving performance when you have many animated characters in the viewport.
5. Utilize the Pose Library

The module supports a Pose Library that allows you to save and mirror poses for your Control Rigs.

Tip: Create a “Hand Pose” library for common gestures (fist, point, relaxed). You can then “Paste” or “Paste Mirrored” these poses across different frames in Sequencer to speed up the blocking phase of your animation.
6. Space Switching for IK/FK

AnimationEditMode surfaces Space Switching controls. This allows you to change the parent of a control (e.g., switching a hand from “Local Space” to “World Space” or “Chest Space”) mid-animation. This is vital for tasks like keeping a hand stationary on a wall while the rest of the body moves.

7. Debug with the Rewind Debugger

If your animation logic isn’t behaving as expected, use the Rewind Debugger (linked with this module’s data). It records the state of all animation variables and poses over time, allowing you to scrub backward to see exactly which node or variable caused a visual glitch or an unexpected pose.

8. Customizing the Anim Details

The Anim Details panel is a streamlined version of the standard Details panel.

Best Practice: In your Control Rig asset, mark only the most important variables as “Animatable.” The AnimationEditMode module will then hide all other technical properties, keeping your workspace clean and focused only on the attributes that need keyframing.