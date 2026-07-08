---
layout: default
title: Persona
---

<!-- ai-generation-failed -->

<h1>Persona</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/Persona/Persona.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AdvancedPreviewScene, AnimGraph, AnimGraphRuntime, AnimationBlueprintLibrary, AnimationEditMode, AnimationModifiers, AppFramework, ApplicationCore, BlueprintGraph, ClothingSystemEditorInterface, ClothingSystemRuntimeCommon, ClothingSystemRuntimeInterface, CommonMenuExtensions, ContentBrowser, ContentBrowserData, Core, CoreUObject, CurveEditor, DesktopWidgets, EditorFramework, EditorInteractiveToolsFramework, EditorStyle, EditorViewport, EditorWidgets, Engine, GraphEditor, InputCore, InteractiveToolsFramework, InterchangeEngine, Json, JsonUtilities, Kismet, KismetWidgets, NaniteUtilities, PinnedCommandList, PropertyEditor, RHI, RenderCore, Sequencer, SequencerWidgets, SkeletalMeshDescription, SkeletalMeshUtilitiesCommon, Slate, SlateCore, StatusBar, TimeManagement, ToolMenus, ToolWidgets, TypedElementRuntime, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ystem in Unreal Engine. It provides the unified user interface, viewport, and shared logic used across all animation-related editors, including the Skeleton, Skeletal Mesh, Animation Sequence, and Animation Blueprint editors.

What it is and What it’s used for

Located in Developer/Persona and Editor/Persona, this module acts as a “shell” that hosts character-centric tools. Rather than rebuilding a viewport for every animation asset type, the engine uses Persona to create a consistent environment for previewing and editing assets.

Primary uses include:

Unified Viewport: Providing the 3D preview space where you can manipulate bones, view cloth simulations, and test hitboxes.
Asset Tooling: Handling the details panels, skeleton trees, and mesh editing tools for character assets.
Preview Scenes: Managing the FPersonaPreviewScene, which allows developers to customize the lighting, floor, and sky specifically for animation workflows.
Shared Commands: Implementing common actions like “Record Animation,” “Retarget,” and “Mesh LOD Management.”
Practical Usage Tips and Best Practices
1. Utilize the Pose Watch Manager

In the Animation Blueprint editor (powered by Persona), right-click any node and select Toggle Pose Watch. This allows the elimination of guesswork when debugging complex blending by drawing the bone transforms of that specific node in the viewport, even if it isn’t the final output pose.

2. Optimize with Visibility-Based Anim Tick

Within the Persona-driven Skeletal Mesh settings, you can set the Visibility Based Anim Tick Option. Setting this to “Only Tick Pose When Rendered” is a critical optimization for the elimination of CPU overhead for characters that are off-screen or hidden by occlusion.

3. Layer State Machines for Readability

Persona allows you to nest state machines. Instead of one massive, unreadable graph, create a “Locomotion” state machine and nest an “Idle/Turn” state machine inside it. This organizational best practice leads to the elimination of visual clutter and makes logic easier to debug.

4. Leverage Pose Caching to Save Performance

If you use the same animation logic in multiple places within an AnimBP, use a New Saved Cached Pose node. This ensures the elimination of redundant calculations by evaluating the pose once and storing it for reuse throughout the graph, which is significantly more efficient than duplicating nodes.

5. Customizing the Preview Scene

Use the Preview Scene Settings tab to swap out the environment or the preview mesh. Properly configuring a “Dark Room” or “High Contrast” preview scene results in the elimination of visual noise when you are trying to fine-tune subtle additive animations or socket placements.

6. Use Linked Animation Layers for Modular Logic

Instead of building a single AnimBP for every weapon type, use Linked Anim Layers. This allows for the elimination of “Monolithic Blueprints” by letting you swap out specific parts of the animation logic (like the “Upper Body” pose) dynamically at runtime.

7. Debug with “stat animation” and “stat sequencer”

When performance drops in a Persona-heavy scene, use the console command stat animation. This displays the time taken for each part of the character update, leading to the elimination of bottlenecks caused by expensive nodes like Rigid Body or Control Rig.

8. Strategic Elimination of Unused Bone Tracks

In the Skeleton editor, identify bones that do not require animation (like tiny decorative bits) and remove their tracks or use the Bone Compression Settings. Proper track management results in the elimination of wasted memory in your Animation Sequences, keeping your character memory footprint lean.