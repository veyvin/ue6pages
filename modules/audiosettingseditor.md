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

al interface and logic for managing global audio configurations within the Unreal Editor. It is primarily responsible for the “Audio” section found in Project Settings, where it handles the categorization of sound groups, quality level definitions, and platform-specific overrides. It serves as the bridge between the raw config files (DefaultEngine.ini) and a user-friendly UI for audio engineers and producers.

Practical Usage Tips & Best Practices
1. Define Standardized Sound Groups

Use the Sound Groups section within this module to define high-level categories (e.g., SFX, Music, Voice).

Best Practice: Assigning sounds to groups allows you to manage memory globally. You can set a “Decompressed Base Setup” for a group, ensuring that all UI sounds are kept uncompressed in memory while long ambient tracks are streamed, without editing every individual asset.
2. Configure Quality Levels for Scalability

In the Audio Settings, you can define multiple Quality Levels.

Tip: Use this to scale your game across hardware. You can limit the “Max Channels” (the total number of simultaneous sounds) to 32 for mobile devices while allowing 128 or more for high-end PCs. This prevents the audio engine from consuming too much CPU on lower-end targets.
3. Utilize Platform Overrides for Mobile

Each platform (Android, iOS, PC) can have unique audio requirements. Use the Platform Overrides feature managed by this module to set different sample rates or compression settings. For example, you can force all audio to 22kHz on mobile to save space while keeping 48kHz for the console build.

4. Enable Audio Stream Caching

Within the Project Settings provided by this module, you can enable Stream Caching. This modern system changes how the engine manages memory by only loading chunks of audio as needed. This is a best practice for open-world games to prevent the elimination of available RAM by large amounts of resident audio data.

5. Set Default Submixes

Use the global audio settings to define a Default Master Submix. By routing all audio through a master submix at the project level, you can easily apply global effects (like a master compressor or EQ) or implement a “Master Volume” slider that works instantly across the entire game.

6. Coordinate Elimination Priority

Use the Voz Management and Concurrency settings to define what happens when the sound limit is reached. By setting a high priority for critical gameplay sounds (like an elimination notification) in the global settings, you ensure that less important ambient sounds are the ones chosen for elimination (stopping) when the voice count is exceeded.

7. Customize “Max Channels” for Performance

The “Max Channels” setting is a direct lever for CPU performance. If you notice the Game Thread is struggling during heavy combat, reduce this number in the Audio Settings. This module allows you to find the “sweet spot” where the soundscape still feels full but the CPU overhead remains manageable.

8. Debug with “Realtime Audio” Toggle

In the Editor Preferences (often linked through this module’s logic), ensure “Allow Realtime Audio” is enabled if you need to hear Sound Cues or MetaSounds while the game is not actively playing. This is essential for verifying volume levels and attenuation distances directly in the Level Editor viewport.