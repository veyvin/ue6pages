---
layout: default
title: MoviePlayer
---

<!-- ai-generation-failed -->

<h1>MoviePlayer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/MoviePlayer/MoviePlayer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, Engine, HTTP, HeadMountedDisplay, InputCore, MoviePlayerProxy, RHI, RenderCore, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ck of startup movies and loading screens on a separate thread from the main game logic.

Description and Purpose

While the Media Framework is used for in-game textures and UI videos, the MoviePlayer module is specifically intended for transitions where the main thread is blocked (such as level loading). Its primary purpose is to maintain a responsive UI and smooth video playback while the engine is busy loading assets. It utilizes the IGameMoviePlayer interface to run on its own thread, which helps eliminate “freezing” or “hitching” during heavy disk I/O operations, ensuring the player always sees a smooth loading animation or cinematic.

Practical Usage Tips and Best Practices
Initialize in the Startup Module
To setup a custom loading screen, access the module via GetMoviePlayer() during your game module’s startup. Configuring the loading screen settings early is a best practice to eliminate “black frames” between the initial engine splash screen and your game’s first cinematic.
Configure FLoadingScreenAttributes
Use the FLoadingScreenAttributes struct to define how your movie behaves. Setting bAutoCompleteWhenLoadingCompletes to true allows the movie to finish naturally, while setting it to false helps you eliminate jarring cuts by waiting for a user input (like “Press any key to continue”).
Use Slate for Loading UI
Because the MoviePlayer runs on a separate thread, it cannot use standard UMG widgets (which are tied to the Game Thread). You must use Slate (C++) to define any overlay text or progress bars. Using Slate ensures the UI remains interactive, helping you eliminate the appearance of a crashed application.
Optimize Movie File Compatibility
The MoviePlayer is more sensitive to codecs than the standard Media Framework. Always encode your startup movies as H.264 (.mp4) with a constant bitrate. This ensures the player can initialize the decoder quickly, which helps you eliminate startup delays or audio/video desync.
Check bWaitForManualStop
If your game has a long “Post-Load” initialization (like spawning many actors), use bWaitForManualStop = true. This keeps the movie playing until you explicitly call StopMovie(), allowing you to eliminate the visual glitch of a player seeing an unpopulated or “half-loaded” level.
Limit Complex Logic on the Loading Thread
Avoid performing heavy calculations or memory allocations within your loading screen Slate code. Since this shares resources with the asset loader, keeping your UI simple is the best way to eliminate resource contention that could actually slow down your level loading times.
Enable “Sync with Engine” for VR
When developing for XR, ensure your MoviePlayer settings respect the head-tracking refresh rate. If the loading screen doesn’t update, it can cause motion sickness. Proper thread synchronization in the MoviePlayer helps you eliminate “swimming” or static images in a headset during transitions.
Transition to Media Framework for In-Game Use
Remember that the MoviePlayer is for “blocking” loads. Once the level is active, you should switch to the Media Framework for any FMVs or UI videos. Understanding this distinction helps you eliminate architectural errors where developers try to use the MoviePlayer for standard gameplay cinematics.