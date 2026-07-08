---
layout: default
title: AudioEditor
---

<!-- ai-generation-failed -->

<h1>AudioEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AudioEditor/AudioEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, AssetDefinition, AudioExtensions, AudioLinkEngine, AudioMixer, ClassViewer, ContentBrowser, Core, CoreUObject, DetailCustomizations, DeveloperSettings, EditorFramework, EditorSubsystem, Engine, GameProjectGeneration, GraphEditor, InputCore, Kismet, Landscape, LevelEditor, PropertyEditor, RenderCore, SignalProcessing, Slate, SlateCore, ToolMenus, ToolWidgets, UMG, UMGEditor, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

t provides the specialized tooling, UI, and graph logic for audio-related assets. It acts as the backend for the visual editors used to create complex sound behaviors, including Sound Cues and Sound Submixes.

Description

This module extends the Unreal Editor’s capabilities to handle audio assets beyond simple playback. It manages the Sound Cue Editor, where designers use a node-based graph to define randomization, looping, and mixing logic. It also handles the Sound Submix Editor, which allows for the visual routing of audio signals and the application of real-time effects like reverb and EQ. Essentially, this module provides the “canvas” and “tools” that technical sound designers use to mold audio within the engine.

Practical Usage Tips and Best Practices
1. Strictly Separate Editor Dependencies

Since AudioEditor is an editor module, it must never be included in runtime or shipping builds. In your *.Build.cs file, always wrap the dependency in a check for the Editor target to prevent packaging errors:

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AudioEditor");

	}
Copy code
2. Extend Sound Cue Functionality

If your project requires a custom audio node (e.g., a specialized procedural wind generator), you will need to interface with this module. You typically create a runtime USoundNode class and then use the AudioEditor module’s classes to define how that node appears and behaves within the Sound Cue graph.

3. Utilize Submix Visualizers

The AudioEditor provides real-time spectrum and envelope visualizers within the Submix Editor. Use these tools to monitor signal levels and frequency distribution. This is the most effective way to identify and eliminate “clipping” or frequency masking before you ever move to a dedicated mixing pass.

4. Custom Asset Actions

Use the module’s FAssetTypeActions_SoundBase or related classes to create custom right-click menu items for audio assets in the Content Browser. For example, you can create a “Batch Create Sound Cues” action to automatically generate cues from a selection of raw Wave assets, drastically reducing manual iteration time.

5. Debugging with the Audio Console

The AudioEditor module integrates with the engine’s debug visualization. Use console commands like au.Debug.SoundCues 1 or au.Debug.Submixes 1 while in the editor. This module handles the drawing of the active paths in the Sound Cue graph, allowing you to see exactly which branch is playing in real-time.

6. Manage Sound Class Hierarchies

While Sound Classes are runtime objects, the visual hierarchy and “Class Mix” editor are managed by this module. Use these tools to organize your sounds into logical groups (e.g., UI, Ambience, Combat). This allows you to globally adjust volumes or apply effects to entire categories of sound at once.

7. Validate Logic on Elimination

When designing “death” or “destruction” sounds, use the Sound Cue Editor to create variations for a player’s elimination. This module allows you to set up “Random” nodes and “Modulator” nodes to ensure that the sound of an elimination remains varied and doesn’t become repetitive during a long gameplay session.

8. Leverage Detail Customizations

The module provides specialized “Detail Customizations” for audio properties. If you are building a custom actor that handles complex audio (like a vehicle or a weapon), you can use this module to create a cleaner UI in the Details panel, hiding irrelevant properties and exposing only the essential audio parameters for your designers.