---
layout: default
title: Media
---

<!-- ai-generation-failed -->

<h1>Media</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Media/Media.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, RenderCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

playback of video and audio content. It acts as an abstraction layer, allowing developers to play media from local files, URLs, or live streams without needing to write platform-specific code for every device (Windows, Android, PlayStation, etc.).

It coordinates the relationship between Media Sources (the data), Media Players (the logic), and Media Textures (the visual output). This system is what enables in-game televisions, animated UI backgrounds, and cinematic textures.

Practical Usage Tips and Best Practices
1. Store Media in the “Content/Movies” Folder

For cross-platform compatibility, Unreal Engine has a strict requirement for the location of video files.

Best Practice: Always place your video files in the Content/Movies/ directory of your project. This ensures the engine can locate them using a relative path during packaging, which helps you eliminate “File Not Found” errors on consoles and mobile devices.
2. Use Media Sound Components for Spatialization

Simply playing a video does not automatically handle 3D audio in the world.

Action: Add a Media Sound Component to the Actor holding your video screen and link it to your Media Player. This allows the video’s audio to benefit from the engine’s attenuation and spatialization settings, eliminating flat, non-directional sound.
3. Manage Life Cycles with Media Player Assets

Media Players are assets, meaning multiple objects can reference the same player, but they share the same state (play/pause).

Tip: If you need three different TVs playing three different videos, you must create three separate Media Player assets. Reusing a single asset for different content will eliminate your ability to control the screens independently.
4. Close Media Players When Not in Use

Video decoding is extremely hardware-intensive and consumes significant memory and CPU/GPU cycles.

Best Practice: Call the Close function on your Media Player when the player leaves an area or the video is no longer visible. This releases the hardware decoder and helps you eliminate performance bottlenecks or memory leaks in your level.
5. Precache for Smooth Playback

When using a File Media Source, the engine has to read data from the disk constantly.

Action: For short, frequently replayed videos (like UI loops), enable the Precache File option in the File Media Source settings. This loads the entire video into RAM, helping you eliminate “hitching” or frame-drops caused by slow disk read speeds.
6. Use Electra for Complex Streaming

If your project requires HLS (HTTP Live Streaming) or DASH, the default platform players may be insufficient.

Tip: Enable the Electra Player plugin. It is a robust, cross-platform player integrated into the Media module that supports adaptive bitrate streaming, which helps you eliminate buffering issues for players with varying internet speeds.
7. Synchronize via Sequencer

If you need a video to play in perfect sync with a cinematic cutscene:

Action: Use a Media Track inside a Level Sequence. This allows the Sequencer to “scrub” the video frame-by-frame along with the animation, eliminating desync issues between your skeletal mesh animations and the background video.
8. Validate Support with the Media Framework Utilities

Not all hardware supports all video resolutions or codecs (e.g., some older mobile phones cannot decode 4K H.265).

Best Practice: Use the CanPlaySource or CanPlayUrl nodes in Blueprints before attempting to open a video. This allows you to provide a lower-resolution fallback if necessary, helping you eliminate black screens or crashes on lower-end hardware.