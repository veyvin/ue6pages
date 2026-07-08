---
layout: default
title: DirectShow
---

<!-- ai-generation-failed -->

<h1>DirectShow</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/DirectShow/DirectShow.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ne that provides a bridge to the Windows DirectShow framework. While modern Unreal Engine development primarily uses the Electra Media Player or Windows Media Foundation (WMF), the DirectShow module remains in the engine to support specific legacy codecs and older video capture hardware that may not be compatible with the newer Media Foundation APIs.

It is primarily used for projects that must interface with specialized industrial cameras, older webcams, or specific proprietary video formats that rely on the DirectShow filter graph for decoding.

Practical Usage Tips and Best Practices
1. Use Only as a Fallback

Treat DirectShow as a secondary option behind WMF and Electra. Most modern .mp4 (H.264/H.265) files perform better and are more stable under WMF. Reserve the DirectShow module for the elimination of compatibility issues with legacy .avi or .wmv files that newer players fail to open.

2. Install Necessary Codec Packs

DirectShow relies on codecs installed at the system level (on the Windows OS). If a video fails to play, you may need to install a codec pack like K-Lite or LAV Filters. This is a requirement for the elimination of “Format Not Supported” errors when working with non-standard video containers.

3. Preferred for Legacy Capture Cards

Some older HDMI capture cards or medical imaging devices only provide DirectShow drivers. If your device does not appear in the Media Player under the WMF category, switching the player override to DirectShow can facilitate the elimination of “No Video Input” errors for these specific hardware types.

4. Configure Player Overrides

In your File Media Source or Stream Media Source asset, look at the Player Overrides section. Explicitly set the “Windows” platform to use DirectShowPlayer. This is a best practice for the elimination of “Automatic” selection logic that might default to a player that cannot handle your specific codec.

5. Monitor for Memory Leaks

DirectShow is an older COM-based API and can sometimes struggle with modern engine thread management. When opening and closing many video streams rapidly, monitor your process memory in the Task Manager. This proactive monitoring assists in the elimination of memory bloat caused by unreleased DirectShow filter graphs.

6. Verify Synchronous Loading Stalls

Unlike the Electra player, which is highly asynchronous, DirectShow can sometimes block the main thread while building its filter graph. If you notice the editor hanging when a video starts, consider pre-loading the media source earlier in a loading screen to ensure the elimination of mid-game hitches.

7. Handle Audio spatialization Carefully

DirectShow audio often bypasses the standard Unreal Engine MetaSounds or Audio Engine processing by sending it directly to the OS default output. For proper 3D spatialization, you may need to use a Media Sound Component. This setup is essential for the elimination of “flat” 2D audio in a 3D environment.

8. Check for “Merit” Conflicts

Windows uses a “Merit” system to decide which DirectShow filter to use. If you have multiple codec packs installed, they may conflict. Use a tool like GraphStudioNext to see how Windows is rendering the file; this technical insight leads to the elimination of playback artifacts caused by conflicting system filters.