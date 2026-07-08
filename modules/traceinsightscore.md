---
layout: default
title: TraceInsightsCore
---


<h1>TraceInsightsCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/TraceInsightsCore/TraceInsightsCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, DesktopPlatform, InputCore, Slate, SlateCore, ToolWidgets, TraceServices</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

d visualization logic for Unreal Insights. While modules like TraceAnalysis handle raw data parsing and TraceServices manage the data storage, TraceInsightsCore contains the Slate-based base classes and extension interfaces (such as ITimingViewExtender and FTimingEventsTrack) used to render performance data into the interactive timeline.

It is the essential module for developers looking to add custom tracks, tabs, or tooltips to the Unreal Insights standalone application or its embedded editor views.

Practical Usage Tips and Best Practices
Extend the Timing View via ‘ITimingViewExtender’
To add a custom track to the main Timing Insights window, implement the ITimingViewExtender interface. This allows you to hook into the UI’s creation process and inject your own tracks. This approach helps you eliminate the need to modify core engine files when adding project-specific profiling tracks.
Derive from ‘FTimingEventsTrack’ for Custom Visuals
When creating a new track, derive from FTimingEventsTrack. This base class handles the heavy lifting of horizontal scrolling, zooming, and time-mapping. By overriding BuildDrawState, you can define exactly how your events appear on the timeline, which helps you eliminate boilerplate rendering code.
Use ‘FProviderLock’ for Thread-Safe UI Updates
The Insights UI runs on a separate thread from the data analysis. When your track queries a data provider (from TraceServices), always use FProviderLock to wrap your access. This helps you eliminate race conditions and “flickering” UI states that occur when the UI reads a data structure while it is being updated by an analyzer.
Leverage ‘FInsightsManager’ for Global UI State
Use the FInsightsManager singleton to access global UI settings, such as the current time range or active session information. This centralized access helps you eliminate inconsistent time-scaling issues across different custom windows in your tool.
Implement ‘InitTooltip’ for Rich Data Inspection
Override the InitTooltip function in your custom track class to provide contextual information when a user hovers over an event. Providing detailed text or small Slate widgets here helps you eliminate the need for users to manually cross-reference logs or external documentation.
Register as a Modular Feature
To ensure your custom Insights extension is discovered at runtime, register it using the IModularFeatures API. This decoupled architecture allows your plugin to be loaded dynamically by the Unreal Insights program, helping you eliminate hard dependencies between your game code and the profiling tools.
Synchronize with ‘FInsightsCommands’
Use the existing FInsightsCommands system to map your track’s visibility or filter settings to keyboard shortcuts. Reusing the engine’s command patterns helps you eliminate UI friction and ensures your custom tools feel like a native part of the Unreal Insights experience.
Clean Up UI Resources on Session Elimination
Ensure your extender implements proper cleanup logic when a session is closed. Releasing Slate brushes and clearing cached handles during the elimination of the analysis session helps you eliminate memory leaks and prevents “ghost tracks” from appearing when the user opens a new .utrace file.