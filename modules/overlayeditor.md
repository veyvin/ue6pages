---
layout: default
title: OverlayEditor
---

<!-- ai-generation-failed -->

<h1>OverlayEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/OverlayEditor/OverlayEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, Engine, Overlay, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

author Overlays, which are assets used primarily for timed text, subtitles, and localized closed captions within the Media Framework. While traditional subtitles are often embedded in audio waves, the Overlay system allows for external, standalone text data that can be synchronized with video playback or cinematic sequences.

This module provides the interface for the Overlay Editor tool, allowing developers to import, edit, and preview timed text tracks. By separating text data from the media source, it facilitates the elimination of “hard-coded” text, enabling a more flexible and scalable approach to multi-language support and accessibility in games and virtual productions.

Practical Usage Tips and Best Practices
1. Use for Standalone SRT Imports

The OverlayEditor module is the primary handler for .srt (SubRip) file imports. When you drag an SRT into the Content Browser, it creates a Basic Overlay asset. Using this module for imports leads to the elimination of manual timestamp entry, as it automatically parses the start and end times into the asset’s internal data structure.

2. Localize via FText Properties

Every entry in an Overlay asset uses the FText type. This means your overlays are fully compatible with the Localization Dashboard. Leveraging this feature leads to the elimination of separate asset files for different languages; the engine will automatically swap the text based on the user’s active culture at runtime.

3. Synchronize with the Media Player

To display overlays during video playback, use the Media Overlays component in conjunction with a Media Player. The OverlayEditor ensures that the data is stored in a format the Media Player can query. This synchronization assists in the elimination of “desync” issues where subtitles might drift away from the video’s audio track.

4. Preview in the Overlay Editor Window

Double-clicking an Overlay asset opens the editor provided by this module. Use this window to audit the timing of specific lines. Testing your text lengths here leads to the elimination of “text overflow” bugs, ensuring that long sentences fit within your UI’s designated subtitle safe-zone before you ever run the game.

5. Integrate with Sequencer

Overlays can be added to a Subtitle Track within Sequencer. The OverlayEditor module provides the logic to display these entries during cinematic playback. This practice facilitates the elimination of complex Blueprint logic for displaying narrative text, as the Sequencer handles the timing and visibility automatically.

6. Convert Basic Overlays to Subtitle Assets

If your project uses the newer “Subtitle” plugin features (introduced in UE 5.x), you can right-click a Basic Overlay asset to convert it. This transition leads to the elimination of legacy data formats and grants access to more robust text styling and layout options provided by the modern subtitle system.

7. Maintain Consistent Timing Buffers

When editing overlays, ensure there is a small gap (at least 0.1 seconds) between the end of one entry and the start of the next. This practice, supported by the OverlayEditor’s timeline view, assists in the elimination of “flickering” artifacts on certain hardware where two text entries might otherwise try to render on the same frame.

8. Audit for “Mature” Content

The OverlayEditor allows you to flag specific entries or entire assets as containing “Mature” language. Using these flags leads to the elimination of compliance risks, as you can easily write a simple Blueprint toggle to filter or skip these overlays based on the player’s parental control settings.