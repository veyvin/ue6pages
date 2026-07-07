---
layout: default
title: AudioSettingsEditor
---

<!-- ai-generation-failed -->

<h1>AudioSettingsEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AudioSettingsEditor/AudioSettingsEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, InputCore, PropertyEditor, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e that provides the interface and logic for managing project-wide audio configurations. It acts as the bridge between the high-level Project Settings UI and the underlying configuration files.

Description and Purpose

This module is responsible for the “Audio” section found within Project Settings. It handles the customization and validation of the UAudioSettings class, which dictates how the audio engine initializes and behaves across the entire project. Its primary purpose is to allow developers to define global defaults—such as the Master Submix, default Sound Classes, and VOIP settings—and to manage platform-specific overrides. It ensures that any changes made in the editor are correctly serialized into the DefaultEngine.ini and various PlatformEngine.ini files.

Practical Usage Tips and Best Practices
Define Global Routing Defaults
Use the settings provided by this module to set your Default Master Submix and Base Sound Class. By defining these early, you ensure that every new sound asset imported into the project is automatically routed correctly, preventing “unmanaged” sounds from bypassing your global volume controls or effects chains.
Manage Platform-Specific Quality Levels
The AudioSettingsEditor allows you to define “Quality Levels.” Use these to scale the complexity of your audio for different hardware. For example, you can set a “Mobile” quality level that reduces the Max Channels (voice count) to 32, helping to eliminate CPU bottlenecks on lower-end devices while keeping a 128-voice limit for PC.
Configure VOIP Sample Rates
Within the Audio Settings, you can set the sample rate for Voice Over IP (typically 16kHz or 24kHz). Higher rates provide clearer voice but use more bandwidth. Use this module to find the “sweet spot” for your game’s networking constraints to ensure clear communication during team-based gameplay.
Leverage Default Sound Concurrency
Set a project-wide Default Sound Concurrency asset. This acts as a safety net to prevent the engine from trying to play too many sounds simultaneously (e.g., if 50 explosions happen at once), which can cause audible clipping or hardware-level stuttering.
Standardize Asset Naming for Dialogue
This module contains settings for Dialogue Filename Format. Configure this to match your studio’s pipeline (using tags like {DialogueGuid} or {ContextId}). Standardizing this here ensures that the dialogue system generates consistent, trackable filenames for your localization team.
Verify Audio Mixer Backends
In the platform-specific sections managed by this module, you can check which Audio Mixer is being used. For modern UE 5.x projects, ensure that “Audio Mixer” is enabled for all target platforms to utilize features like MetaSounds and real-time submix effects.
Global Elimination Feedback Volume
If your game has a specific UI sound for an elimination, you can use the Audio Settings to route all UI sounds to a dedicated “UI Submix.” This allows you to adjust the volume of all elimination alerts and menu sounds globally without having to open individual Sound Cue assets.
Use the “Cook Overrides” for Optimization
Under the “Cooking” section of the Audio Settings, you can enable Stream Caching. This changes how audio is loaded into memory during the cook process. For large open-world games, this setting is vital to eliminate long load times and reduce the overall memory footprint of your audio library.