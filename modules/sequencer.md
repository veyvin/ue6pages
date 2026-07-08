---
layout: default
title: Sequencer
---

<!-- ai-generation-failed -->

<h1>Sequencer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/Sequencer/Sequencer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ActorPickerMode, AppFramework, ApplicationCore, AssetRegistry, BlueprintGraph, CinematicCamera, Constraints, ContentBrowser, Core, CoreUObject, CurveEditor, DeveloperSettings, DeveloperToolSettings, EditorFramework, EditorInteractiveToolsFramework, EditorStyle, EditorWidgets, Engine, GraphEditor, InputCore, LevelSequence, MovieScene, MovieSceneCapture, MovieSceneTools, MovieSceneTracks, PropertyEditor, RenderCore, SceneOutliner, SequencerCore, SequencerWidgets, SerializedRecorderInterface, Slate, SlateCore, SubobjectDataInterface, TimeManagement, ToolMenus, ToolWidgets, TypedElementFramework, TypedElementRuntime, UniversalObjectLocator, UnrealEd, ViewportInteraction, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

al Engine. It provides a non-linear, multi-track editing environment used for creating real-time cinematics, gameplay cutscenes, and complex animations. While the LevelSequence asset stores the data (keys and tracks), the Sequencer module provides the editor interface and the runtime logic to evaluate those tracks over time.

It is used to animate actors, trigger audio, swap cameras, and execute events. By acting as a production hub, it allows you to eliminate the need for baked video files, instead rendering everything in real-time with full access to the engine’s lighting, physics, and post-processing systems.

Practical Usage Tips and Best Practices
Understand Spawnables vs. Possessables
A Spawnable exists only while the sequence is playing; a Possessable is an actor already in the level that Sequencer takes control of. Use Spawnables for cinematic-only FX or temporary actors to eliminate level clutter, as they are automatically cleaned up when the sequence ends.
Utilize Subsequences for Team Collaboration
For large cinematics, break your work into “Shots” using the Shot Track. Each shot is its own Level Sequence. This modular approach helps you eliminate file-locking conflicts, as different artists can work on the “Lighting” subsequence while others handle “Animation” in the same master scene.
Minimize Ticking for Performance
If a sequence doesn’t need to evaluate every frame (e.g., a simple UI fade), set the Tick Manager settings appropriately. You can also disable the “Tick” on actors that are being fully driven by Sequencer to eliminate redundant CPU calculations.
Use Event Tracks for Gameplay Logic
Instead of hard-coding timing in Blueprints, use Event Tracks (Trigger or Repeater) to fire functions in your Level Blueprint or Actor classes. This allows you to visually sync gameplay changes (like the “elimination” of a barrier or a character spawning) directly with the cinematic timeline.
Master the Curve Editor for Smooth Motion
Don’t rely solely on the timeline view. Open the Curve Editor to fine-tune the interpolation between keyframes. Using Cubic or Hermite interpolation helps you eliminate robotic, linear movement, providing a more natural and professional cinematic look.
Leverage Hierarchical Bias in Subscenes
If you have multiple subscenes affecting the same actor (e.g., two different lighting setups), use the Hierarchical Bias property. Higher values take precedence. This priority system helps you eliminate conflicting property values without needing to delete tracks.
Render via Movie Render Queue (MRQ)
For final output, always use the Movie Render Queue rather than the legacy “Render Movie” button. MRQ offers spatial and temporal sampling, which helps you eliminate aliasing and flickering in high-quality renders for trailers or film.
Clean Up Bindings on Sequence Elimination
When a sequence finishes, ensure its “Restore State” option is correctly set. If you want actors to return to their original positions after the “elimination” of the cinematic, enable this in the Sequence settings to eliminate “ghosting” where actors remain stuck in their final cinematic pose.