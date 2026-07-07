---
layout: default
title: SerializedRecorderInterface
---

<!-- ai-generation-failed -->

<h1>SerializedRecorderInterface</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/SerializedRecorderInterface/SerializedRecorderInterface.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, LiveLinkInterface</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

to handle high-frequency data capture and binary serialization during recording sessions.

Description and Purpose

This module provides the ISerializedRecorder interface, which is a critical component of the Virtual Production pipeline. Unlike standard property recording—which tracks variables on the Game Thread—this module is designed to capture raw asynchronous data streams, such as high-fidelity facial motion capture, raw Live Link packets, or high-frequency sensor telemetry. Its primary purpose is to eliminate the performance overhead of real-time keyframe creation. By serializing raw data into a compact binary buffer during a take and “baking” it into Sequencer tracks only after the recording has stopped, it ensures the engine remains performant during live performances.

Practical Usage Tips and Best Practices
Inherit for Custom Hardware Integration
When building a plugin for specialized hardware (like a custom MoCap suit or biometric sensor), implement the ISerializedRecorder interface. This is the best practice to eliminate Game Thread hitches, as it allows you to push raw data into the recorder’s buffer from a dedicated background thread.
Follow the “Capture Now, Bake Later” Pattern
Use the interface to store raw TArray<uint8> byte streams during the “Live” phase. Avoid creating UObject assets or performing complex math while the recording is active. This strategy helps you eliminate dropped frames during critical takes where CPU cycles are limited.
Utilize Timecode for Sample Alignment
Always stamp your serialized data packets using the FQualifiedFrameTime provided by the engine’s TimecodeProvider. This allows the post-recording process to eliminate temporal drift, ensuring your high-frequency samples align perfectly with the rendered frames.
Pre-allocate Serialization Buffers
Frequent memory re-allocations during a long take can cause CPU spikes. When implementing the interface, estimate your data rate and pre-size your FMemoryWriter or FArchive buffers. This helps eliminate non-deterministic performance during a recording session.
Use for Lossless Live Link Capture
Standard Live Link recording can lose data if the engine frame rate dips. By using a recorder that implements this interface, you can store every incoming packet regardless of the render rate. This allows the final “Bake” pass to eliminate jitter by interpolating from the full raw history.
Implement Robust Post-Processing Logic
The interface includes a finalization stage (often called during the “Bake” or “Stop” event). Use this stage to convert your binary buffers into standard UMovieSceneTrack keyframes. This ensures you eliminate the risk of crashing the editor by moving heavy data-processing tasks to a point where the live performance has ended.
Apply Delta Compression to Streams
If your serialized data is redundant (e.g., a sensor that only updates when moved), implement basic delta compression before passing the buffer to the interface. This helps you eliminate massive file sizes for long takes and reduces the time needed for the final data conversion.
Monitor Buffer Health via Stats
Use stat VirtualProduction or custom CSV_PROFILE markers to monitor the size of your serialized buffers. If you see memory usage growing exponentially without being cleared, you must optimize your data throughput to eliminate memory exhaustion during long-form motion capture sessions.