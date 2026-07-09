---
layout: default
title: AVIWriter
---

<!-- ai-generation-failed -->

<h1>AVIWriter</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AVIWriter/AVIWriter.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

for capturing and encoding video into the AVI (Audio Video Interleave) container format. It provides the low-level logic to interface with the Windows-only VCM (Video Compression Manager) to create video files directly from the engine’s viewport or Sequencer. While it is largely considered a legacy system in favor of the modern Movie Render Queue, it remains available for simple, rapid video exports in specific developer workflows.

Practical Usage Tips & Best Practices
1. Distinguish from Movie Render Queue (MRQ)

The aviwriter module is part of the older “Render Movie” system.

Best Practice: Use this module only for quick, low-fidelity previews or “dailies” where file size and encoding speed are more important than visual perfection. For final cinematics, high-quality lighting (Lumen), or specialized passes, use Movie Render Queue instead.
2. Windows Platform Limitation

The implementation of aviwriter relies on the Microsoft AVI library.

Tip: This module is essentially Windows-only. If you are developing on macOS or Linux, or need to automate video captures on a Linux-based render farm, you must use the CommandLineEncoder (FFmpeg) or an image sequence (PNG/EXR) rather than this module.
3. Manage Large File Sizes

The AVI format is an older container that does not support modern, high-efficiency compression like H.265.

Best Practice: Be wary of long captures. Uncompressed AVI files can easily reach dozens of gigabytes in minutes. If you are using this for long-duration recordings, ensure the target drive has significant free space to avoid a crash during the final file-writing stage.
4. Configure via Capture Settings

When using the legacy “Render Movie” window in Sequencer, the options selected under “Video Sequence” directly drive the aviwriter module. Use the Compression Quality slider to balance between visual artifacts and file size. Lower quality settings will increase the elimination of fine detail in exchange for faster writing and smaller footprints.

5. Avoid Audio Desync

The aviwriter module can struggle with maintaining perfect audio-video synchronization during heavy frame-rate fluctuations.

Tip: If you require perfectly synced audio, it is often better to export the video as an AVI and the audio as a separate .wav file, then combine them in an external video editor.
6. Use for Rapid UI/UX Previews

Because AVI encoding via this module is relatively “lightweight” compared to the heavy processing of MRQ, it is an excellent choice for recording quick UI animations or Blueprint logic demonstrations to share with team members over messaging platforms like Slack or Discord.

7. Clean Up Temporary Capture Data

When a capture fails or is cancelled, the aviwriter may leave partial .avi files in your Saved/VideoCaptures folder. Periodically check this directory for the elimination of these “zombie” files to reclaim disk space, especially after a failed long-form render.

8. Transition to Apple ProRes or Avid DNx

For developers who need a single-file video output (rather than image sequences) but require professional quality, look toward the AppleProResMedia or AvidDNxMedia plugins. These modern modules provide better performance and fidelity than the legacy aviwriter while still offering the convenience of a single video file.