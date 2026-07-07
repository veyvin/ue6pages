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

xt and metadata that is “overlaid” on media or gameplay. It primarily consists of two parts: the Overlay Asset (data) and the SOverlay/UOverlay widgets (UI).

This system is most commonly used for subtitles, closed captions, and localized text that must be synchronized with a specific timeline, such as a video file or a Sequencer track. It serves as a more structured alternative to raw strings, supporting multiple languages and precise timing.

Practical Usage Tips and Best Practices
1. Convert SRT to Subtitle Assets

The Overlay module handles the ingestion of external subtitle formats.

Action: When you import an .srt file, it enters the engine as a Basic Overlay asset. Right-click this asset and select Convert Basic Overlays to Subtitles. This allows the data to work with the high-level subtitle system, eliminating the need for manual text entry.
2. Use Overlays to Replace Canvas Panels

In UMG (UI), the Overlay widget is a high-performance container that allows children to be stacked on top of one another.

Best Practice: Use an Overlay widget instead of a Canvas Panel for simple stacking (like an icon with a notification badge). Overlays have significantly less CPU overhead than Canvas Panels, helping you eliminate unnecessary layout calculations and draw calls.
3. Manage Layer IDs for Performance

Every child added to a UOverlay widget increments its Layer ID so they can render on top of each other.

Tip: Avoid nesting dozens of Overlay widgets within each other. Each layer requires a separate draw call setup. Keeping your Overlay hierarchy shallow helps you eliminate GPU performance bottlenecks in complex HUDs.
4. Synchronize via Sequencer Subtitle Tracks

The Overlay module is deeply integrated with the engine’s cinematic tools.

Action: Drag your Subtitle/Overlay asset directly onto a Subtitle Track in Sequencer. The duration is controlled by the section length in the timeline, which helps you eliminate synchronization drift between character dialogue and the displayed text.
5. Leverage Localizable FText

Overlay assets utilize the FText type for their content strings.

Best Practice: Always use the localization dashboard to gather text from your Overlay assets. Because they use FText, the engine will automatically swap the text to the player’s culture at runtime, eliminating the need for custom “Language Switcher” logic.
6. Use for Non-Text Metadata

The Overlay system isn’t strictly for dialogue; it can store any timed string data.

Tip: Use Overlay assets to trigger “metadata events” during a cinematic (e.g., a string that tells the UI to “Show Button Now”). Parsing these strings at specific timestamps helps you eliminate complex Blueprint timing logic for UI-synced cinematics.
7. Implement “Searchable” Subtitles

Because Overlay assets are standard Unreal assets, they are indexed by the engine.

Action: Use the Global Asset Registry to find specific Overlay assets containing certain keywords. This is useful for developers to eliminate the time spent hunting for a specific line of dialogue across hundreds of different cinematic files.
8. Migrate Embedded Subtitles

If you are moving from an older version of Unreal where subtitles were hidden inside Sound Waves:

Action: Use the Migrate Embedded Subtitles to Asset tool. This extracts the text into standalone Overlay assets, which are easier to manage and localize, eliminating the risk of losing subtitle data when sound assets are modified.