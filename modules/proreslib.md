---
layout: default
title: ProResLib
---

<!-- ai-generation-failed -->

<h1>ProResLib</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Apple/ProResLib/ProResLib.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ovides the native encoding and decoding capabilities for the Apple ProRes video codec.

Description and Purpose

This module acts as the core library for handling high-quality, intermediate video formats inside the engine. It is the primary engine behind the Apple ProRes Media plugin and is heavily utilized by the Movie Render Queue (MRQ) for high-fidelity cinematic exports. Its primary purpose is to provide a high-bitrate, post-production-friendly video format that supports up to 12-bit color depth and alpha channels. By using ProResLib, developers can eliminate the quality loss associated with highly compressed formats like H.264, ensuring that rendered frames are suitable for professional color grading and visual effects compositing.

Practical Usage Tips and Best Practices
Enable the Apple ProRes Media Plugin
Before you can utilize this module in the editor, you must enable the “Apple ProRes Media” plugin in the Plugins menu. This is a best practice to eliminate “Missing Codec” errors when trying to select ProRes as an export format in the Movie Render Queue.
Select the Correct Codec Profile (422 vs 4444)
Use ProRes 422 HQ for standard high-quality video exports. If your workflow requires transparency (alpha channels) for compositing in software like After Effects or Nuke, switch to ProRes 4444 or 4444 XQ. This will eliminate the need for separate matte passes by embedding the alpha directly into the video file.
Use Electra Protron for Smooth Scrubbing
In UE 5.6, the Electra Protron player is optimized for ProRes files. If you are using ProRes video as a texture in your scene, enable Protron in the Project Settings. This helps you eliminate frame dropping and hitching when scrubbing through a sequence in the editor or during live performances.
Manage Large File Sizes
ProRes is a “visually lossless” but heavy format. A few minutes of 4K ProRes 4444 can easily exceed 50GB. Always verify your target drive has sufficient high-speed storage before starting an MRQ render to eliminate “Disk Full” errors that could corrupt your final output.
Optimize for Virtual Production (In-Camera VFX)
For LED wall setups, use ProRes as the source format for plate playback. The codec’s design allows for fast decoding with low CPU overhead. This helps you eliminate playback latency, ensuring the background plates remain perfectly synced with the camera’s movement and the physical actors.
Embed Timecodes for Post-Production
When rendering via MRQ using this module, ensure the “Include Timecode” option is enabled. This embeds metadata that professional editing software can read, which is the best way to eliminate manual synchronization work when handing off renders to an external editorial team.
Verify Software Compatibility
While ProRes is a standard on macOS, ensure your Windows playback software (like VLC or MPC-HC) and your NLE (Non-Linear Editor) are updated to support the specific ProRes version you are exporting. This will eliminate “Codec Not Found” warnings when reviewing your renders outside of Unreal.
Avoid Using for Final Distribution
ProRes is an intermediate format, not a delivery format for end-users. After your edit is complete, transcode the ProRes file to H.264 or AV1 for the final game trailer or cutscene. This helps you eliminate unnecessary download sizes for your audience while keeping your master files at maximum quality.