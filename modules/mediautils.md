---
layout: default
title: MediaUtils
---

<!-- ai-generation-failed -->

<h1>MediaUtils</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/MediaUtils/MediaUtils.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, ImageWrapper, ImageWriteQueue, Media, SignalProcessing</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Media Framework that provides common data structures, helper classes, and synchronization logic used by various media player plugins.

Description and Purpose

While specific plugins like ElectraPlayer or WmfMedia handle the actual decoding of video files, MediaUtils provides the shared plumbing that makes these players work consistently within the engine. Its primary purpose is to offer thread-safe containers for media samples, timing utilities for audio/video synchronization, and common interfaces for media playback state. By centralizing these low-level helpers, the module allows developers to eliminate redundant code when building custom media players or extending existing playback functionality.

Practical Usage Tips and Best Practices
Utilize TMediaSampleQueue for Thread Safety
When building a custom media source, use the TMediaSampleQueue template provided by this module to store decoded frames. This queue is designed to handle high-frequency data transfer between the decoding thread and the engine’s render thread, helping you eliminate race conditions and memory corruption.
Synchronize with FMediaTimeline
Use the FMediaTimeline class to manage playback time and seeking logic. This utility handles the complexities of frame-rate conversion and time-stamping, which is the best way to eliminate “desync” issues where audio and video tracks drift apart over time.
Leverage MediaTickers for Background Tasks
The module provides a “Ticker” system that can execute logic at specific intervals independently of the main game thread. Use this to handle periodic buffer checks or stream health monitoring to eliminate hitches on the Game Thread during heavy media streaming.
Handle Metadata via FMediaPropertyValue
When retrieving information like resolution, bitrate, or codec details from a stream, use the FMediaPropertyValue struct. This standardized format allows different parts of your UI or C++ logic to read media attributes consistently, helping you eliminate type-conversion errors.
Use FMediaClock for Global Sync
If your project requires multiple video textures to play in perfect unison (common in virtual production or multi-screen setups), use the FMediaClock provided by this module. It provides a single source of truth for time, allowing you to eliminate frame-variance between different media assets.
Implement Custom Sample Sinks
If you need to process video data (e.g., for AI analysis or custom VFX) before it hits the screen, inherit from the sample sink interfaces in this module. This allows you to intercept the raw data stream and eliminate the need for expensive “ReadPixels” operations from a rendered texture.
Monitor Buffer Health with FMediaPool
Use the memory pooling utilities in MediaUtils to manage the allocation of large video buffers. Proper pool management ensures that the engine reuses memory blocks for incoming frames, which helps you eliminate frequent allocations that lead to memory fragmentation and crashes.
Debug via Media Log Categories
This module defines several internal log categories (e.g., LogMediaUtils). If your video is stuttering or failing to load, check the Output Log for these specific tags. They often provide low-level timing data that helps you eliminate bottlenecks in the data-loading pipeline.