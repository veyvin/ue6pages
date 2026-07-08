---
layout: default
title: ProfileVisualizer
---


<h1>ProfileVisualizer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/ProfileVisualizer/ProfileVisualizer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DesktopPlatform, Engine, InputCore, Slate, SlateCore, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

logic for visualizing performance data captured through Unreal Engine’s CSV (Comma-Separated Values) profiling system. It is the primary backend for the CSV Profile Visualizer, which transforms raw text-based performance logs into interactive, multi-track graphs.

This module is essential for “post-mortem” performance analysis. It allows you to load .csv or .uep files generated during a game session—often from console or mobile builds—to identify spikes in frame time, memory usage, or draw calls. By visualizing these trends, you can eliminate the difficulty of reading thousands of lines of raw data and quickly pinpoint where the hardware was struggling.

Practical Usage Tips and Best Practices
Access via the Session Frontend
The easiest way to use this module is through the Session Frontend (Tools > Debug > Session Frontend). Navigate to the Profiler or Data Graph tabs to load your .csv files. This integrated workflow helps you eliminate the need for external graphing software like Excel.
Capture Data with ‘CSVProfile’ Commands
To generate data for this module, use the console command CSVProfile Start and CSVProfile Stop while playing. You can also add CSVProfile -frames=1000 to capture a specific duration. Consistent capturing helps you eliminate “one-off” anomalies by providing a larger data sample.
Compare Performance Across Hardware
The visualizer allows you to overlay multiple CSV files from different devices (e.g., an iPhone vs. an Android). Comparing these graphs helps you eliminate platform-specific bottlenecks by highlighting where one device diverges from the performance baseline.
Filter for Specific ‘Offenders’
Use the search and filter bar in the visualizer to isolate specific counters, such as Groom, Lumen, or Slate. Filtering out irrelevant data tracks helps you eliminate visual clutter, allowing you to focus on the systems that are actually causing frame-time spikes.
Correlate Spikes with Gameplay Events
When capturing data, use CSVStat to mark specific events (like “Combat_Start” or “Level_Load”). The ProfileVisualizer will display these markers on the timeline, helping you eliminate the guesswork involved in matching a performance dip with an in-game action.
Analyze ‘Averages’ vs. ‘Max’ Values
The module provides statistics for both average and maximum frame times. Pay close attention to the Max spikes; while your average might be 60 FPS, a single 100ms spike will cause a visible hitch. Addressing these spikes helps you eliminate “micro-stutter” in your gameplay.
Export Graphs for Production Reports
You can export the generated graphs as images or share the .csv files with your team. Providing visual proof of performance improvements helps you eliminate communication gaps between engineering and art departments when requesting asset optimizations.
Flush Profiles on Session Elimination
When a profiling session is complete (the “elimination” of the test run), ensure the .csv file has finished writing to disk (the Saved/Profiling/CSV folder) before moving it. This ensures the ProfileVisualizer doesn’t encounter truncated files, which helps you eliminate “Invalid File Format” errors during analysis.