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

provides the bridge between raw cinematic data (MovieScene) and the Sequencer user interface.

Description and Purpose

While the MovieScene module handles the runtime data of a sequence, MovieSceneTools contains the logic for creating, editing, and visualizing those tracks within the Unreal Editor. It provides the base classes for “Track Editors,” which define how different types of data (like animations, transforms, or audio) appear and behave in the Sequencer timeline. Its primary purpose is to provide the UI plumbing and automation logic required to build custom cinematic tools. By using this module, developers can eliminate the manual effort of writing complex timeline UI, allowing them to focus on how their custom data should be keyed and interpolated.

Practical Usage Tips and Best Practices
Inherit from FMovieSceneTrackEditor
When creating a custom track type for Sequencer, inherit from FMovieSceneTrackEditor. This class provides the essential hooks for handling drag-and-drop actions and right-click menus, helping you eliminate the need to write custom Slate code for standard timeline interactions.
Utilize K2Node_PlayMovieScene for Blueprint Integration
The module includes logic for handling “K2Nodes” related to cinematics. If you are building a tool that triggers sequences via Blueprints, use the utilities here to ensure your nodes correctly reference sequence assets. This helps you eliminate “null reference” errors when a sequence asset is renamed or moved.
Leverage FMovieSceneSectionPainter for Custom Visuals
If your custom track needs to display unique data—like a waveform for audio or a thumbnail for animation—use the FMovieSceneSectionPainter class. Overriding the paint logic allows you to draw custom graphics directly on the Sequencer blocks, which is a best practice to eliminate user confusion when managing complex timelines.
Automate Keyframe Creation via C++
Use the helper functions in this module to programmatically add keys to tracks. When building a “Record” tool or a “Live Link” bridge, using these standardized helpers is the best way to eliminate inconsistencies in how tangents and interpolation are handled across different tracks.
Implement IKeyframeHandler for Selection Logic
To ensure your custom track supports standard Sequencer shortcuts (like ’S’ to key), implement the IKeyframeHandler interface. This ensures your tool behaves like a native engine feature, helping you eliminate friction for cinematic artists who rely on established hotkeys.
Use MovieSceneToolHelpers for Property Binding
When creating a track that animates a specific property of an Actor (like a light’s intensity), use MovieSceneToolHelpers::MapProperty. This utility handles the complex reflection logic required to find and bind properties, which helps you eliminate “Property Not Found” warnings in the Sequencer UI.
Extend the “Add Track” Menu
The module provides the ISequencer::OnGetAddMenuContent delegate. By registering your custom track editor here, you can place your custom logic directly into the main Sequencer (+) menu. This is the best way to eliminate extra steps for users who need to find and add your specific tool to their scene.
Validate Sequences with FMovieSceneValidation
Before rendering a cinematic, use the validation utilities in this module to check for overlapping sections or missing bindings. Running an automated validation pass helps you eliminate “ghost” frames or missing actors before they ruin a high-resolution render in the Movie Render Queue.