---
layout: default
title: MediaAssets
---

<!-- ai-generation-failed -->

<h1>MediaAssets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/MediaAssets/MediaAssets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioExtensions, AudioMixer, Core, CoreUObject, Engine, Media, MediaUtils, RHI, RenderCore, Renderer, SignalProcessing</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

layback within Unreal Engine. It provides the C++ and Blueprint interfaces for managing Media Players, Media Textures, and various Media Sources (such as file, stream, or platform-specific sources).

This module bridges the gap between external media files and the engine’s rendering pipeline. By outputting video data directly into a UMediaTexture, it enables developers to treat videos as standard textures within the Material Editor. This facilitates the elimination of complex platform-specific video decoding logic, providing a unified workflow for in-game cinematics, UI videos, and dynamic textures.

Practical Usage Tips and Best Practices
1. Always Place Media in the “Content/Movies” Folder

To ensure that your video files are correctly found and packaged into the final build, they must be placed in the Content/Movies directory of your project. Straying from this convention often results in the elimination of video playback in packaged builds, as the engine’s cooking process specifically looks for non-uasset files in that folder.

2. Implement the Electra Player for Cross-Platform Stability

For the most consistent results across Windows, macOS, Linux, and Mobile, enable the Electra Player plugin. The MediaAssets module will prioritize Electra if configured, leading to the elimination of playback discrepancies caused by varying native OS codecs (like WMF on Windows vs. AVFoundation on macOS).

3. Use “Play on Open” with Caution

While the UMediaPlayer has a “Play on Open” checkbox, it is often better to disable it and trigger playback via Blueprints or C++ once the OnMediaOpened delegate fires. This practice leads to the elimination of “Black Frame” hitches where the video attempts to play before the hardware decoder has fully initialized the first frame.

4. Manage Audio via Media Sound Components

Video audio does not play automatically through the world. You must add a UMediaSoundComponent to an Actor and associate it with your Media Player. This facilitates the elimination of silent videos and allows you to utilize the engine’s spatialization, attenuation, and MetaSound systems for your video audio.

5. Close Media Streams for “Elimination” of Memory Leaks

Media playback consumes significant GPU and CPU resources. Always call the Close function on your Media Player when a video is no longer visible or needed (e.g., when a UI menu is closed). Failing to do so prevents the elimination of active decoder instances, which can lead to performance degradation or crashes on memory-constrained devices.

6. Optimize Resolution for UI Elements

Don’t use 4K video files for small UI icons or background loops. High-resolution videos require massive memory bandwidth. Downscaling your source media to the actual required size leads to the elimination of “stuttering” frames and keeps the game’s overall frame rate stable during video playback.

7. Handle “Elimination” of Playback on App Suspend

On mobile platforms (Android/iOS), the MediaAssets module may lose its connection to the hardware decoder when the app is minimized. You should listen for the ApplicationWillEnterBackgroundDelegate to pause or close the player. This assists in the elimination of “Dead Context” errors when the user returns to the game.

8. Use Media Plate for World Environments

For placing videos on meshes in a level, use the Media Plate Actor (introduced in UE 5.1). It wraps the MediaAssets logic into a user-friendly actor that handles the material and texture setup automatically. Using this tool leads to the elimination of manual material creation errors and provides better performance for streaming high-bitrate content.