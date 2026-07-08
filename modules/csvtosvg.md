---
layout: default
title: CSVtoSVG
---

<!-- ai-generation-failed -->

<h1>CSVtoSVG</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/CSVtoSVG/CSVtoSVG.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ContentBrowserData, Core, CoreUObject, EditorConfig, EditorFramework, Engine, InputCore, Settings, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ngine binaries directory designed to convert raw performance data into high-quality, readable vector graphics.

Description

This tool is a key component of the CSV Profiler workflow. When you record performance stats in Unreal Engine (using csvprofile start), the engine outputs a .csv file containing thousands of data points for CPU, GPU, and memory metrics. The csvtosvg utility processes these files and generates .svg charts. These charts allow developers to visually identify spikes, trends, and bottlenecks over the duration of a playtest. Because it outputs SVG files, the resulting graphs are resolution-independent and ideal for inclusion in automated performance reports.

Practical Usage Tips and Best Practices
1. Locate the Executable

The tool is not a plugin you enable in the editor; it is a standalone C# utility. You can find it in your engine installation folder under: Engine\Binaries\DotNET\CsvTools\csvtosvg.exe. You must run this from a command prompt or as part of an automated batch script to process your profiling results.

2. Use Command-Line Arguments for Scaling

By default, the tool creates a standard-sized graph. You can customize the dimensions to fit your reporting needs using the -width and -height flags. For example, using -width 1920 -height 1080 ensures the graph is large enough to view fine-grained frame-time spikes that might be missed on smaller charts.

3. Define Budgets with Threshold Lines

A best practice for performance monitoring is to visualize your “budget.” You can use the -threshold argument to draw a horizontal line across the graph. For a 60 FPS target, setting a threshold at 16.66ms allows you to see exactly which frames failed to meet the target at a single glance.

4. Apply Smoothing to Identify Trends

Raw performance data is often “noisy” due to micro-stuttering. Use the -smoothing flag to apply a moving average to the data lines. This helps eliminate high-frequency noise and makes long-term performance trends (such as a gradual increase in memory usage) much easier to identify.

5. Generate Multi-Chart Overlays

You don’t have to limit a graph to just one stat. You can specify multiple columns from your CSV to be drawn on a single SVG. Overlaying GPU Time and Game Thread Time on the same chart is a professional technique to quickly determine if a specific performance dip was caused by the renderer or by gameplay logic.

6. Utilize Configuration (.ini) Files

For complex reporting, manual command-line entry is inefficient. The tool supports .ini files that define graph colors, titles, and which specific stats to include. You can create a PerformanceSummary.ini and point the tool to it using the -config flag to ensure consistent graph styling across your entire team.

7. Visualize Logic on Actor Elimination

In combat-heavy games, performance hits often occur when many actors are removed at once. Use the CSV Profiler to capture a mass elimination event, then use csvtosvg to graph the DestroyActor or GC (Garbage Collection) stats. This allows you to see if the elimination of dozens of enemies causes a CPU spike that exceeds your frame budget.

8. Automate with PerfReportTool

While you can use csvtosvg directly, it is best used as part of the engine’s PerfReportTool. This tool uses csvtosvg internally to generate comprehensive HTML reports. By setting up an automated pipeline that runs these tools after a nightly build, you can eliminate the manual labor of data analysis and provide your team with a daily visual health check of the project.