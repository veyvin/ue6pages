---
layout: default
title: MovieSceneTools
---

<!-- ai-generation-failed -->

<h1>MovieSceneTools</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/MovieSceneTools/MovieSceneTools.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ActorPickerMode, AnimGraphRuntime, AnimationBlueprintLibrary, AnimationCore, AppFramework, BlueprintGraph, CinematicCamera, ClassViewer, Constraints, ContentBrowser, Core, CoreUObject, CurveEditor, DataLayerEditor, DesktopPlatform, EditorFramework, EditorStyle, EditorSubsystem, EditorWidgets, Engine, GraphEditor, InputCore, Json, JsonUtilities, Kismet, KismetCompiler, LevelSequence, LiveLinkInterface, MaterialEditor, MessageLog, MovieScene, MovieSceneCapture, MovieSceneTracks, Private, PropertyEditor, RHI, RenderCore, SceneOutliner, SequenceRecorder, Sequencer, SequencerCore, Slate, SlateCore, TimeManagement, ToolMenus, ToolWidgets, UnrealEd, XmlParser</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nd and automate the functionality of Sequencer and the MovieScene ecosystem. While MovieScene provides the runtime data structures and Sequencer handles the UI, MovieSceneTools contains the “logic” for track manipulation, keyframe processing, and editor-side object binding.

It is primarily used by technical artists and pipeline engineers to create custom track types, automate cinematic assembly through C++ or Python, and develop specialized tools for the Sequencer interface.

Practical Usage Tips & Best Practices
1. Utilize FMovieSceneToolHelpers for Automation

This class is the “Swiss Army Knife” of the module, containing static functions for common Sequencer tasks that are otherwise difficult to script.

Best Practice: Use FMovieSceneToolHelpers to perform batch operations like importing FBX data onto tracks or fixing up broken actor bindings. Leveraging these helpers ensures the elimination of manual, error-prone data entry when managing hundreds of cinematic shots.
2. Implement Custom Track Editors

If you are creating a unique gameplay system that needs to be animated (e.g., a custom weather system or specialized camera rig), you need a way for Sequencer to “talk” to it.

Tip: Inherit from FMovieSceneTrackEditor. This allows you to define how your custom track appears in the “Add Track” menu and how it handles drag-and-drop events. Proper implementation results in the elimination of workflow friction for cinematics artists using your tools.
3. Leverage the Keyframe Reduction Utilities

When importing motion capture data or baking physics into Sequencer, you often end up with a keyframe on every single frame, which is a nightmare to edit.

Best Practice: Use the FKeyReduction utilities within the module to simplify curves while maintaining their shape. This leads to the elimination of redundant data, significantly improving Sequencer’s UI performance and making the curves manageable for animators.
4. Automate “Possessable” to “Spawnable” Conversions

In Sequencer, a “Possessable” actor exists in the level, while a “Spawnable” is created by Sequencer itself.

Tip: Use the module’s conversion utilities to automate the process of turning level actors into spawnables. This facilitates the elimination of “dirty” levels, as cinematic-only actors will no longer be permanently saved into your map files.
5. Use FMovieSceneSectionCustomization for UI

By default, Sequencer sections are simple colored blocks. You can make them much more informative by adding thumbnails or text overlays.

Best Practice: Create a customization class for your sections to display relevant metadata (like the name of an animation clip or an audio waveform). Adding visual context results in the elimination of confusion when artists are navigating complex, multi-layered timelines.
6. Optimize Keyframe Selection via Scripting

The module provides hooks to the ISequencer interface to query and manipulate the current user selection.

Tip: Write Editor Utility Widgets that use these tools to perform “Align,” “Snap,” or “Scale” operations on selected keys. This leads to the elimination of tedious pixel-perfect manual dragging when adjusting the timing of cinematic events.
7. Handle Multi-Channel Data with Property Track Utilities

If you are animating a custom C++ struct, you need to tell Sequencer how to break it down into individual float channels (like X, Y, Z).

Best Practice: Use the automated property track generators provided in this module. Correctly mapping your C++ properties to MovieScene channels ensures the elimination of “Unknown Property” errors and allows for standard curve editing on your custom data types.
8. Verify Bindings with the MovieScene Editor Data

Sometimes an actor in a sequence loses its link to the level actor (turning red in the UI).

Tip: Use the binding utilities to programmatically “re-bind” actors based on name or tags. This is especially useful in multi-user environments, resulting in the elimination of broken cinematic sequences when assets are renamed or moved by different departments.