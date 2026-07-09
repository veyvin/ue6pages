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

s, which can lead to a cluttered and unreadable graph.

Tip: Use the -stats "StatName1, StatName2" argument to isolate specific metrics. For example, if you are investigating GPU bottlenecks, filter for GPUTime and SlateTickTime to keep the chart focused on relevant data.
3. Normalize Graphs with Fixed Dimensions

By default, the tool may scale graphs based on the data range.

Best Practice: Use the -width and -height flags to ensure all your generated SVGs have the same dimensions. This allows you to flip through different graphs or overlay them in a report, facilitating the elimination of “visual noise” when comparing two different builds.
4. Define Budgets with “-thresholds”

You can add horizontal lines to your graphs to represent performance targets (e.g., a 16.6ms line for 60 FPS).

Tip: Use the -thresholds argument to define these budget lines. Any data point crossing these lines will be immediately obvious, allowing for the rapid elimination of code paths that exceed the frame budget.
5. Summarize Large Captures with Average/Median

For very long play sessions, the raw SVG can become overly dense.

Best Practice: Use arguments like -average or -smooth to apply a moving average filter to the data. This helps reveal the underlying performance trend by smoothing out minor frame-to-frame jitters, making the graph more useful for high-level reporting.
6. Correlate Gameplay Events via Annotations

The CSV Profiler allows you to insert “Events” or “Metadata” during a recording (e.g., “Player Spawned” or “Enemy Elimination”).

Tip: csvtosvg can display these events as vertical markers on the timeline. This is invaluable for correlating a sudden frame drop with a specific gameplay event, such as a character elimination triggering a complex particle effect.
7. Leverage “-title” and “-legends” for Reports

When sharing performance data with a team, context is everything.

Best Practice: Use the -title "Build #1234 - Combat Stress Test" and ensure legends are enabled. A well-labeled graph leads to the elimination of confusion when multiple developers are reviewing performance data from different branches.
8. Batch Process with Wildcards

If you have a folder full of performance captures from a multi-device test, you don’t need to run the tool individually for each file.

Tip: Use standard command-line wildcards (e.g., csvtosvg.exe *.csv) to batch-convert an entire directory of data into a gallery of SVG images, streamlining the analysis of large-scale performance surveys.