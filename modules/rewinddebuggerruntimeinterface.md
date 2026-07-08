---
layout: default
title: RewindDebuggerRuntimeInterface
---

<!-- ai-generation-failed -->

<h1>RewindDebuggerRuntimeInterface</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/RewindDebuggerRuntimeInterface/RewindDebuggerRuntimeInterface.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

bridge between gameplay code and the Rewind Debugger framework. It defines the runtime interfaces and data structures required to record, track, and scrub through gameplay data during a live session or a recorded trace.

While the Rewind Debugger UI resides in the editor, this module lives at the runtime level, allowing Actors and Components to expose their internal state to the timeline. By implementing this interface, you can eliminate the difficulty of debugging frame-specific logic by enabling “time-travel” debugging for custom gameplay systems, animation states, and physics interactions.

Practical Usage Tips and Best Practices
Expose Custom Tracks via Extension
Use the IRewindDebuggerExtension interface to register custom tracks for your project-specific systems. This allows you to visualize variables (like “Mana” or “AI State”) on the same timeline as animations, helping you eliminate synchronization issues between gameplay logic and visual feedback.
Leverage Data Channels for Performance
The module allows you to group data into different Channels. In your project settings, you can disable specific channels during recording to eliminate CPU overhead and reduce the size of trace files when you only need to debug a specific system like Physics or Animation.
Implement Per-Provider Locking
When writing custom trace providers for the Rewind Debugger, always use FProviderEditScopeLock. This ensures that your data recording is thread-safe and prevents deadlocks during the “elimination” of old frame data when the buffer wraps around, maintaining editor stability.
Filter Object Selection for Clarity
Use the URewindDebuggerSettings to configure the SelectorAllowedTypes array. By limiting the debugger to specific classes (like ACharacter or APawn), you can eliminate clutter in the Object Outliner, making it much faster to find and select the specific actor you need to debug.
Auto-Record during PIE
Enable the “Auto-Record” and “Auto-Eject” settings in the Rewind Debugger toolbar. This ensures that every time you press Play, the engine starts capturing data immediately. This practice helps you eliminate the frustration of missing a bug because you forgot to hit the record button.
Scrub to Analyze Frame-Specific Spikes
When you notice a performance hitch or a “glitchy” animation, pause the simulation and use the Rewind Debugger timeline to scrub back to the exact frame. This allows you to eliminate the guesswork by seeing exactly which notifies or state transitions triggered during that specific millisecond.
Debug Motion Matching Costs
If using the Pose Search plugin, this module enables the Motion Matching Selection Table. You can use the “Heat Map” view (Green for favorable, Red for unfavorable) to eliminate bad animation transitions by seeing exactly why the system chose one pose over another.
Clean Up Traces on Session Elimination
Upon the “elimination” of a debugging session (stopping PIE), the module handles the finalization of the trace data. Ensure your custom providers properly implement their OnSessionEnd logic to eliminate memory leaks or corrupted .utrace files that cannot be opened later for post-mortem analysis.