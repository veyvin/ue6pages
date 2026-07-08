---
layout: default
title: MovieSceneCapture
---

<!-- ai-generation-failed -->

<h1>MovieSceneCapture</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/MovieSceneCapture/MovieSceneCapture.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AVIWriter, AssetRegistry, AudioMixer, Core, CoreUObject, Engine, ImageWriteQueue, Json, JsonUtilities, RHI, RenderCore, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

r recording and exporting cinematic content from Unreal Engine. It provides the core interfaces and logic for capturing the viewport’s frame buffer and encoding it into various formats, such as image sequences or video files.

While it is primarily known as the legacy rendering system (pre-dating the Movie Render Queue), it still provides the underlying architecture for basic “Render Movie” functionality in Sequencer and specialized capture workflows. It is used to transform a real-time Level Sequence into a high-quality video file, helping you eliminate the frame-rate fluctuations of real-time playback for final presentation.

Practical Usage Tips and Best Practices
Understand its Legacy Status
For high-end cinematic production, Unreal Engine 5.0+ recommends the Movie Render Queue (MRQ) over the legacy MovieSceneCapture. However, for quick drafts or simple automation where sub-sampling and spatial anti-aliasing are not required, this module remains a faster, “real-time” export option.
Utilize Warm-up Frames
Always configure Warm-up Frames (found in the Capture Settings). This allows systems like Niagara particles, cloth physics, and temporal anti-aliasing (TAA) to settle before the recording begins. This helps you eliminate “popping” or jittery visual artifacts at the very start of your exported video.
Leverage Filename Tokens
Use tokens like {fps}, {frame}, and {camera} in your Output Format settings. This module automatically parses these strings to generate organized file structures. Proper naming conventions help you eliminate the risk of overwriting previous renders when iterating on different shots.
Enable Cinematic Engine Scalability
In the Capture Settings, ensure Cinematic Engine Scalability is enabled. This module will force the engine to its highest quality settings (LODs, shadow resolution, and texture streaming) regardless of your current editor viewport settings, helping you eliminate low-quality assets in your final output.
Manage Output Directories via C++
If you are building custom tools, use the FMovieSceneCaptureSettings struct to programmatically define output paths. Always verify that the target directory has write permissions before starting a capture to eliminate “Failed to Write” errors during long overnight rendering sessions.
Configure Custom Frame Rates
Match your capture frame rate to your intended delivery (e.g., 24fps or 60fps). This module uses a fixed-time-step approach during capture, which helps you eliminate the “stuttering” or dropped frames that occur if you simply record the screen with external software.
Use ‘Close’ on Capture Completion
When creating a custom capture implementation in C++, ensure you properly call the “Finalize” or “Close” methods on the capture object. Failing to do so can result in corrupted video headers; following this ensures the “elimination” of the capture process successfully seals the file.
Automate via Command Line
The MovieSceneCapture system is highly compatible with command-line arguments (e.g., -MovieSceneCaptureType="Automated"). This is the best way to eliminate the need for manual interaction when setting up a render farm or a continuous integration (CI) pipeline for cinematic reviews.