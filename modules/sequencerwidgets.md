---
layout: default
title: SequencerWidgets
---

<!-- ai-generation-failed -->

<h1>SequencerWidgets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/SequencerWidgets/SequencerWidgets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, InputCore, MovieScene, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ividual Slate components used to build the Sequencer editor interface. It contains highly optimized widgets for time-based manipulation, such as the time slider, transport controls, zoom-and-pan breadcrumbs, and keyframe selection boxes.

This module is primarily used by tools developers who want to extend the Sequencer or build custom editor tools that require a timeline-like interface. By using these pre-made components, you can eliminate the complexity of writing custom rendering logic for frames, seconds, and time-scrubbing interactions, ensuring your custom tools look and feel like native Unreal Engine editors.

Practical Usage Tips and Best Practices
Integrate the ‘STimeSlider’ for Custom Timelines
If you are building a custom animation or audio tool, use the STimeSlider widget from this module. It handles the display of frame numbers, subframes, and time ranges. Utilizing this widget helps you eliminate the difficult task of calculating pixel-to-time ratios manually.
Synchronize with ‘FSequencer’ Interface
Most widgets in this module expect an ISequencer or FSequencer reference to stay in sync with the current playhead. When building custom UI extensions, ensure you bind your widgets to the active sequencer instance to eliminate “drift” between your custom UI and the main timeline.
Use ‘SSequencerBreadcrumb’ for Deep Hierarchies
For tools that involve nested sequences (like Shots and Takes), use the breadcrumb widget found in this module. It provides a standard “trail” for users to navigate back to the master sequence, which helps you eliminate user confusion in complex cinematic projects.
Leverage Selection and Range Widgets
The module provides specialized Slate components for the “Playback Range” and “Selection Range” (the green and red markers). Using these ensures that your custom tool adheres to the same UI standards as the engine, helping you eliminate UX friction for artists who are already familiar with the Sequencer.
Optimize Slate Performance with ‘STrackArea’
When displaying thousands of keyframes or sections, use the STrackArea component. It is designed to handle high-density data by only rendering what is visible in the current view. This optimization helps you eliminate editor lag when working with long or data-heavy cinematic sequences.
Customize Transport Controls
If your tool requires specific playback behavior (like “Loop Selection” or “Play Backward”), you can customize the transport control widgets. Reusing the engine’s standard icons and button logic helps you eliminate the need to design new assets for basic playback functions.
Implement Tooltips for Time Snapshots
Use the built-in time-formatting utilities within the module to display tooltips as users scrub the timeline. Providing real-time frame or time-code feedback helps you eliminate precision errors when users are trying to place events at specific gameplay moments.
Cleanup Delegates on Widget Elimination
When your custom widget is destroyed (the “elimination” of the tool window), ensure you unregister any delegates tied to the Sequencer’s time-change events. Failing to do so can cause the editor to attempt to update a null widget, which you must eliminate to prevent crashes.