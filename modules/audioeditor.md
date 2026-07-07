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

ides the tools, UI, and specialized logic for managing and creating audio assets. It serves as the bridge between raw audio data and the professional toolsets within the Unreal Editor.

Description and Purpose

This module is responsible for the specialized editors associated with sound assets, including the Sound Cue Editor, the Sound Class/Mix Editors, and the Audio Bus Editor. It defines the factory logic for importing WAV files, manages the graph-based UI for sound nodes, and handles the previewing of audio within the editor environment. Its primary purpose is to provide audio designers with a visual, interactive interface to author complex sound behaviors without needing to write code.

Practical Usage Tips and Best Practices
Override Audio Factories for Custom Imports
If your studio requires specific metadata or settings (like automatic Sound Class assignment) when importing WAV files, you can extend the UAudioFactory class found in this module. This allows you to automate the standardization of your audio library upon drag-and-drop.
Leverage Non-Destructive Wave Editing
The module supports a non-destructive Wave Editor. Use it to trim, fade, or loop audio files directly in the engine. Because this is non-destructive, the original source data remains intact, allowing you to eliminate the need for external tools like Audacity for simple edits.
Bulk Edit via Property Matrix
The AudioEditor module integrates heavily with the Property Matrix. Select multiple Sound Waves or Sound Cues, right-click, and choose “Asset Actions > Bulk Edit via Property Matrix” to quickly standardize Sample Rates, Compression Settings, or Attenuation assets across hundreds of files.
Utilize Real-Time Audio (RTA) for Level Mixing
Enable “Real Time Audio” in the Level Viewport to hear changes as you tweak Sound Cues or Attenuation settings. The AudioEditor module ensures that as you move sliders or nodes, the audio engine updates the active preview immediately, providing an instant feedback loop.
Standardize Elimination SFX with Sound Cues
For player elimination sounds, use the Sound Cue editor to create a “Random” node connected to multiple variations of a “thud” or “shatter” sound. By setting the “Weight” pins in the editor, you can ensure the most satisfying sounds play more frequently, keeping the elimination feedback loop feeling fresh.
Monitor Visualizers for Performance
Use the visualizers provided by this module (such as the Sound Class hierarchy view) to identify assets that may be too expensive. Ensure that complex Sound Cues aren’t running excessive “Mixer” or “Modulator” nodes that could be simplified into a single pre-baked wave asset.
Isolate Editor-Only Logic
Since this is an editor module, ensure any custom C++ audio tools you build are placed in an “Editor” type module in your .uplugin or .uproject file. This prevents the heavy editor UI and factory code from being compiled into your shipping game executable.
Debug with the Audio Dashboard
The AudioEditor module supports the “Audio Dashboard” (found under the Window menu). Use this to see a live view of active sounds, their volumes, and which Sound Classes are currently active. This is the most effective way to debug why a specific sound, such as an elimination alert, isn’t being heard during gameplay testing.