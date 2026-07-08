---
layout: default
title: Overlay
---

<!-- ai-generation-failed -->

<h1>Overlay</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Overlay/Overlay.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, Slate, SlateCore, UMG</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

handle the synchronization and display of timed text and localized captions. It provides the data structures and interfaces necessary to overlay subtitles, closed captions, and audio descriptions onto a game or cinematic sequence.

At its core, the module manages FOverlayItem objects—timed segments of text—and exposes an API through the IOverlayStream and IOverlayStreamer interfaces. It is used to create accessible experiences, allowing you to eliminate communication barriers for players who are deaf, hard of hearing, or playing in localized languages.

Practical Usage Tips and Best Practices
Synchronize via the Subtitles Subsystem
Instead of manually triggering UI widgets, use the USubtitlesSubsystem (accessible via C++ or Blueprints). This module integrates directly with the subsystem to queue timed text, helping you eliminate desynchronization between the audio and the visual captions.
Implement ‘Externally Timed’ for Narrative Control
Set the ESubtitleTiming to ExternallyTimed when captions need to be triggered by specific gameplay events rather than a fixed audio duration. This allows the logic to manually start and stop captions, helping you eliminate the risk of text remaining on screen during an unexpected dialogue skip.
Use Overlay Assets for Cinematic Sequencer
You can create Overlay Assets in the Content Browser to store blocks of timed text. These can be placed directly onto a Sequencer track, providing a visual timeline of your dialogue. This practice helps you eliminate the complexity of managing hundreds of independent string variables.
Optimize Draw Calls with Overlays
In UMG, use the Overlay Panel widget to stack UI elements. Unlike Canvas Panels, which can be computationally expensive due to complex anchors, the Overlay Panel is highly efficient for simple stacking. This helps you eliminate unnecessary CPU overhead in your HUD layout.
Leverage Localized Text (FText)
Always use the FText type for your overlay content rather than FString. The Overlay module is designed to work with Unreal’s localization pipeline, ensuring that the engine can automatically swap captions for different regions, helping you eliminate the need for manual translation logic in your code.
Manage Priorities for Overlapping Text
If multiple characters speak at once, use the Priority property within the overlay data. The system uses this to determine which text should take precedence or how they should be stacked, helping you eliminate “text clutter” where multiple captions overlap and become unreadable.
Configure Subtitle Styles in Project Settings
Use the Subtitles and Closed Captions section in Project Settings to define a global font, size, and background opacity. This provides a consistent look across the entire game, helping you eliminate visual inconsistencies that occur when different designers create their own caption widgets.
Flush Queues on Actor Elimination
When a character is defeated or removed from the scene (the “elimination” of the speaker), ensure you call StopSubtitlesInAsset or StopAllSubtitles. This clears any pending text from the queue, helping you eliminate “phantom captions” where a character continues to “speak” via text after they are no longer in the world.