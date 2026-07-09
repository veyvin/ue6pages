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

ngine. It provides a set of high-performance, lossless data compression algorithms designed to replace older standards like Zlib. In modern Unreal Engine projects, Oodle is the default solution for compressing .pak files, IoStore containers, and generic data buffers.

Its primary purpose is to significantly reduce the disk footprint of packaged games and accelerate loading times by minimizing the amount of data read from disk and processed by the CPU.

Practical Usage Tips & Best Practices
1. Select the Correct Compression Method

Oodle provides four main methods: Kraken, Mermaid, Selkie, and Leviathan.

Best Practice: Use Kraken as your default. It offers the best balance between high compression ratios and extremely fast decompression speeds. Using Kraken leads to the elimination of long loading screens without taxing the CPU heavily during asset streaming.
2. Configure Compression Levels by Build Type

Oodle allows you to set different “effort” levels (1–9) for your compression. Higher levels take much longer to pack but result in smaller files.

Tip: Set a lower effort level (e.g., 3 - Fast) for daily development builds to ensure the elimination of long wait times during the cook process. Use a higher level (e.g., 7 or 9) for your final distribution builds to achieve the smallest possible download size for players.
3. Match Oodle Texture with Oodle Data

Oodle Texture uses Rate Distortion Optimization (RDO) to make textures more “compressible” for the Oodle Data algorithm.

Best Practice: When using Oodle Data for packaging, ensure Oodle Texture is also enabled in your DefaultEngine.ini. This synergy facilitates the elimination of redundant data patterns in textures, allowing Oodle Data to compress them far more effectively than standard BCn encoding alone.
4. Optimize Block Size for Target Hardware

The compressionblocksize setting determines how data is chunked before compression.

Tip: For modern consoles and NVMe SSDs, a block size of 256KB is generally recommended. Tuning this setting leads to the elimination of I/O bottlenecks, ensuring that the decompression thread can stay ahead of the high-speed data stream from the drive.
5. Monitor Compression via Packaging Logs

You can verify Oodle’s activity by inspecting the logs during a project cook or package.

Best Practice: Look for lines starting with Oodle vX.X.X initializing. If you see Zlib instead, Oodle is not correctly configured. Verifying your logs ensures the elimination of accidental “bloated” builds that don’t utilize the optimized Oodle pipeline.
6. Use Leviathan for Maximum Storage Savings

If your project is hitting strict disc space limits (such as on certain console SKUs), you can switch to the Leviathan method.

Tip: Leviathan provides the highest compression ratio available in the suite. While it is slower to decompress than Kraken, its use results in the elimination of “Over Size Limit” errors when trying to fit a large game onto a physical medium or a specific download tier.
7. Avoid Re-compressing Already Compressed Data

Attempting to use Oodle on files that are already compressed (like certain encrypted files or video formats) can actually increase file size and CPU usage.

Best Practice: Use the “Exclude from Compression” list in your Project Packaging settings for video files and pre-compressed archives. This proactive management leads to the elimination of wasted CPU cycles during the loading process.
8. Leverage for Save Game Data

Oodle isn’t just for pak files; you can use the module’s API to compress large SaveGame files or procedurally generated world data.

Tip: Use the FOodleCompressedData utility in C++ to wrap your save buffers. This results in the elimination of massive save files on the user’s drive, which is especially important for games with complex, persistent world states.