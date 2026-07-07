---
layout: default
title: CSVtoSVG
---


<h1>CSVtoSVG</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/CSVtoSVG/CSVtoSVG.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ContentBrowserData, Core, CoreUObject, EditorConfig, EditorFramework, Engine, InputCore, Settings, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rformance data captured by the CSV Profiler into high-quality, scalable vector graphics (SVG) charts.

Description and Purpose

This module provides the logic for parsing .csv files generated during engine profiling sessions and converting them into visual graphs. While the CSV Profiler records raw data such as frame times, memory usage, and draw calls, CsvToSvg is the tool that makes this data human-readable. It is primarily used for performance analysis and reporting, allowing developers to generate visual trend lines that highlight spikes, regressions, and bottlenecks. It is a critical component of automated performance pipelines, as it can be scripted to generate status reports after automated build tests.

Practical Usage Tips and Best Practices
Integrate with Automated Build Pipelines
Script the CsvToSvg.exe (found in Engine/Binaries/DotNET/CsvTools/) to run automatically after a Gauntlet test or a soak test. By auto-generating graphs for every build, you can immediately visualize performance trends and eliminate the need for manual data processing.
Use Configuration Files for Consistency
The tool supports .xml configuration files to define graph styles, colors, and thresholds. Create a standard “Project Performance Template” to ensure all team members are looking at the same visual representation of data, which helps eliminate confusion during cross-departmental reviews.
Leverage Command-Line Arguments
Use specific arguments to customize your output. For example, use -width and -height to set the resolution of the SVG, or -nolegend if you are generating small “sparkline” graphs. These controls allow you to fit performance data into different types of documentation or dashboards.
Visualize Player Elimination Spikes
If your game experiences hitches during intense combat, use the CSV Profiler to record a session and then use CsvToSvg to graph the GameThread and RenderThread times. Look for the exact timestamp of an elimination event on the graph; if you see a massive spike, you can narrow down whether the cause is VFX, physics, or logic.
Smooth Data with Moving Averages
Use the -avg or -smooth flags to apply a moving average to volatile data. High-frequency noise in frame times can hide the bigger picture; smoothing the data helps you eliminate distractions and focus on the underlying performance trends over a longer play session.
Generate Budget Overlays
You can specify budget lines (e.g., a 33.3ms line for 30 FPS targets) in your command-line call or config file. Visualizing your data against these hard targets makes it obvious when a feature is over-budget, allowing your team to quickly identify and eliminate performance offenders.
Batch Process Multiple CSVs
If you are running A/B tests (comparing two different optimization strategies), you can batch process multiple CSV files into a single SVG or a side-by-side comparison. This is the fastest way to verify if an optimization actually succeeded in eliminating a specific bottleneck.
Export for Web-Based Dashboards
Because the output is SVG, the files are extremely lightweight and resolution-independent. They are perfect for embedding into internal wiki pages or web-based build health dashboards, ensuring the entire studio has visibility into the current performance state of the project.