---
layout: default
title: OodleDataCompression
---

<!-- ai-generation-failed -->

<h1>OodleDataCompression</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/OodleDataCompression/OodleDataCompression.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

on suite, which is the industry-standard solution for high-performance data compression within Unreal Engine.

Description and Purpose

This module provides the core algorithms (such as Kraken, Mermaid, Selkie, and Leviathan) used to compress game packages (.pak and .utoc files). Its primary purpose is to eliminate the trade-off between small file sizes and fast loading times. Unlike standard Zlib compression, Oodle is designed specifically for game data, providing significantly faster decompression speeds which reduces CPU overhead during streaming and loading. This ensures that assets can be pulled from the disk and decompressed into memory with minimal impact on frame rate or load duration.

Practical Usage Tips and Best Practices
Select the Correct Compressor for Your Target
Use Kraken as your default for a balance of high compression and fast decompression. If your target hardware has very weak CPUs (like older mobile devices), switch to Mermaid or Selkie to eliminate CPU bottlenecks during asset streaming at the cost of slightly larger install sizes.
Configure Effort Levels per Build Type
Oodle allows you to set different “Effort” levels for different build configurations. Use a low level (e.g., Fast) for daily development builds to eliminate long wait times during packaging, but use a high level (e.g., Optimal or Level 7) for your final distribution build to achieve the smallest possible download size.
Set the Compression Block Size to 256KB
In your Project Packaging settings, ensure the “Pak File Compression Commandline Options” include -compressionblocksize=256KB. This is the “sweet spot” for Oodle that helps eliminate seek-time latency on modern SSDs while maintaining high compression ratios.
Use Oodle Texture RDO (Rate Distortion Optimization)
Oodle Data works best when combined with Oodle Texture. By enabling RDO on your textures, you create data that is “Oodle-friendly.” This can eliminate massive amounts of redundant data in your packaged build, often reducing texture disk footprint by 20-50% without perceivable quality loss.
Enable via BaseGame.ini
Ensure Oodle is active by checking your BaseGame.ini. You should see PakFileCompressionFormats=Oodle. Using this module as the primary compressor is a best practice to eliminate the performance inconsistencies found with legacy compression formats.
Leverage for IOStore and Zen Loader
In UE5, the Zen Loader (IOStore) is highly optimized for Oodle. Using these together allows the engine to eliminate “I/O hitching” by decompressing data in parallel across multiple CPU cores, which is essential for open-world games that stream Nanite and Lumen data constantly.
Monitor Compression Ratios in the Log
When packaging, check the output log for lines like Oodle v2.9.0 initializing with method=Kraken. Review the final “Compression Ratio” stats in the log to eliminate bloated assets; if the ratio is poor for a specific file type, consider whether those files should be compressed at all.
Verify Dictionary Sizes for Custom Data
For developers using custom bulk data, Oodle can use “dictionaries” to find patterns across files. While this is advanced, properly setting up a shared dictionary for similar assets (like many similar text files or structured data) is the best way to eliminate redundant strings and minimize your final patch sizes.