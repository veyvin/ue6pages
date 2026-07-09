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

provides the infrastructure for audio asset management and the visual interfaces for audio tools. It handles the logic for the Sound Cue Editor, the Sound Class/Mix editors, and the asset actions (import/export) for audio files. It serves as the bridge between raw audio data and the visual nodes designers use to craft soundscapes.

Practical Usage Tips & Best Practices
1. Avoid Runtime Dependencies

Since AudioEditor contains editor-specific UI and logic, it is not available in packaged builds. Always ensure this module is placed in the PrivateDependencyModuleNames of an Editor module, never a runtime game module. If you need to reference it in a shared module, wrap the code in #if WITH_EDITOR blocks.

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AudioEditor");

	}
Copy code
2. Utilize the Property Matrix for Batch Editing

When managing hundreds of USoundWave or USoundCue assets, don’t open them individually. Select your assets in the Content Browser, right-click, and choose Asset Actions > Edit Selection in Property Matrix. The AudioEditor module facilitates this view, allowing you to bulk-adjust settings like Loudness, Compression Quality, or Virtualization Mode simultaneously.

3. Optimize AnimGraph Interaction

The AudioEditor logic heavily supports Animation Notifies. For best performance, use the Play Sound notify to trigger audio rather than calling “Play Sound” logic every frame in an AnimBP tick. This allows the engine to utilize the “Fast Path” for animation, reducing the CPU overhead of audio-heavy sequences.

4. Leverage Sound Cue Editor UI Features

In the Sound Cue Editor (managed by this module), use the Palette panel to drag-and-drop nodes like Random, Modulator, and Enveloper. To keep graphs readable, follow the standard workflow: place Wave Players on the far left, processing nodes in the center, and the Output node on the right.

5. Debugging with the Output Log

The AudioEditor module routes internal warnings to the Output Log. If a sound fails to play or an asset is corrupted during import, filter the log by LogAudio or LogAudioEditor. This is the fastest way to identify if a .wav file was imported with an unsupported bit depth or sample rate.

6. Coordinate Elimination Logic with Sound Mixes

Use the Sound Mix editor to manage how audio reacts to gameplay events. For example, when a player undergoes elimination, you can use a Sound Mix to “duck” (lower) the volume of environmental music and boost the “Death” sound effect. This module allows you to visually set the attack and release times for these volume shifts without writing C++.

7. Use the “Play Node” Feature for Iteration

Within the Sound Cue Viewport, you can select any individual node and click Play Node in the toolbar. This allows you to hear the sound at that specific point in the graph (e.g., after a pitch modulator but before a reverb send). This is essential for isolating issues in complex sound design graphs.

8. Visualizing Virtualization and Concurrency

Within the editor’s audio settings, use the visualization tools to check Sound Concurrency. The AudioEditor module allows you to define how many instances of a sound can play at once. Properly configuring this prevents the “elimination” of important audio cues by less important, high-frequency sounds (like bullet impacts).