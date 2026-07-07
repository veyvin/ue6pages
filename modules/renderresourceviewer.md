---
layout: default
title: RenderResourceViewer
---

<!-- ai-generation-failed -->

<h1>RenderResourceViewer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/RenderResourceViewer/RenderResourceViewer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DeveloperSettings, InputCore, RHI, Slate, SlateCore, TreeMap, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

es a detailed, searchable snapshot of all GPU memory allocations.

Description and Purpose

This module implements the Render Resource Viewer window (found under Tools > Control Panel > Render Resource Viewer). Its primary purpose is to provide transparency into how Video RAM (VRAM) is being utilized by specific assets and engine subsystems. Unlike the generic “stat memory” commands, this tool lists every individual buffer (Vertex, Index, Uniform), Texture, and Ray Tracing Acceleration Structure currently residing on the GPU. By using this module, developers can eliminate the mystery behind VRAM bloat by identifying exactly which “Owner” (the UObject or Asset) is responsible for a specific memory allocation.

Practical Usage Tips and Best Practices
Manual Refresh for Snapshot Accuracy
The viewer does not update in real-time to save performance. You must click the Refresh button to capture a new state of the GPU. This is a best practice to eliminate confusion when trying to see if a recent asset elimination or change has successfully freed up VRAM.
Filter by Resource Type
Use the checkboxes (e.g., RT, DS, UAV, Streaming) to narrow down the list. If you are specifically hunting for high-resolution textures, uncheck everything except “Streaming” and “Resident” to eliminate noise from geometric buffers and render targets.
Search by Asset Path
The search box scans both the resource name and the “Owner” path. Typing a specific folder name (e.g., /Game/Characters/) is the fastest way to eliminate irrelevant data and see the total VRAM footprint for a specific character or environment set.
Identify Nanite Overhead
Look for entries labeled “Nanite Streaming Manager” or “Cluster Page Data.” These represent the memory pool used by Nanite. If this number is unexpectedly high, you can use this information to adjust your r.Nanite.Streaming.PoolSize console variable and eliminate over-allocation.
Analyze Transient Resources
Transient resources share memory during a single frame. While the “Size” might look large, the “Transient” flag indicates that the memory is recycled. Understanding this helps you eliminate false alarms where it seems like your render targets are exceeding your hardware’s total VRAM.
Detect Redundant Index Buffers
If you see multiple entries for the same mesh with “Depth Only” or “Reversed” flags, these are often generated for non-Nanite platforms. If your project is fully Nanite, you can disable these in the Project Settings to eliminate unnecessary geometric data on the GPU.
Optimize Virtual Texture Pools
The viewer lists “Virtual Texture Page Pools.” If you see high usage here combined with blurry textures in the viewport, it means your pool is too small. Use the viewer to verify the current physical size, then increase the pool in your settings to eliminate texture popping and low-resolution mips.
Check Ray Tracing Acceleration Structures (RTAS)
For projects using Ray Tracing or Lumen, search for “RTAS.” These structures can consume significant VRAM. If the RTAS size for a specific mesh is too large, it is a sign you should eliminate unnecessary geometric complexity or use a simpler “Proxy Mesh” for ray tracing.