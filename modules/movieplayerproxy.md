---
layout: default
title: MoviePlayerProxy
---

<!-- ai-generation-failed -->

<h1>MoviePlayerProxy</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/MoviePlayerProxy/MoviePlayerProxy.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

communication between the main engine thread and the Loading Screen Movie Player. It ensures that UI and video playback can continue smoothly even when the main thread is blocked by heavy level-loading operations.

What it is and What it’s used for

Located in Engine/Source/Runtime/MoviePlayerProxy, this module serves as a proxy layer for the IMoviePlayer interface. Its primary purpose is to manage the handoff and synchronization of rendering tasks to the Slate Thread.

Primary uses include:

Asynchronous Playback: Allowing startup movies or loading videos to play without “hitching” while the engine initializes or loads massive chunks of data.
Slate Thread Synchronization: Bridging the gap between the game thread and the dedicated Slate rendering thread, which remains active during loading.
Media Framework Transition: Acting as a modern interface for legacy movie player systems while projects transition toward the newer, more robust Media Framework.
Thread Safety: Providing safe access to movie player states (like “IsPlaying”) from various engine subsystems without causing race conditions.
Practical Usage Tips and Best Practices
1. Use for Seamless Level Transitions

When calling OpenLevel, the game thread often stalls. The MoviePlayerProxy allows you to maintain a responsive UI during this stall. This is the primary method for the elimination of “frozen” frames that otherwise occur during heavy IO operations.

2. Keep Loading UI Logic in Slate

Because the MoviePlayerProxy relies on a separate thread, any UI shown during this time should be built using Slate C++ rather than UMG Blueprints. UMG logic often relies on the game thread to tick, whereas Slate can run independently, leading to the elimination of unresponsive loading bars.

3. Initialize Early in the Module Lifecycle

If you are building a custom loading screen system, register your proxy settings in the PostEngineInit or StartupModule phase. Early registration ensures the elimination of black frames or “flicker” between the engine splash screen and your game’s first loading movie.

4. Monitor the “IsLoadingFinished” State

Always check the IsLoadingFinished state via the proxy before attempting to hide your loading screen. Attempting to force-close the movie player while the proxy is still receiving data can cause crashes; proper checking results in the elimination of transition-related memory access violations.

5. Leverage for Startup Video Playback

The MoviePlayerProxy is the engine’s default path for playing mandatory legal screens or studio logos. Configuring these in the Project Settings > Movies section utilizes this module to ensure the elimination of audio/video desync while the engine’s core systems are still waking up.

6. Avoid Complex Logic in Movie Callbacks

The proxy handles callbacks when a movie finishes or is skipped. Keep the logic inside these callbacks extremely light. Heavy logic here can stall the Slate thread, which leads to the elimination of the very performance gains the proxy was designed to provide.

7. Use “WaitForMovieToFinish” Strategically

If your game logic requires the movie to play in full (such as a narrative intro), use the WaitForMovieToFinish command. This forces the game thread to sync with the proxy, resulting in the elimination of situations where the player is dropped into the level before the cinematic context is established.

8. Strategic Elimination of Legacy Video Formats

The MoviePlayerProxy works most efficiently with modern, engine-friendly formats like .mp4 (H.264). Performing an elimination of high-bitrate or obscure video codecs in favor of optimized files reduces the CPU load on the proxy thread, leaving more resources available for the actual map loading process.