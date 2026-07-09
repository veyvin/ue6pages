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

specifically to handle Startup Movies and Loading Screens. Unlike the high-level Media Framework (which handles in-game TVs or cinematics), the MoviePlayer operates on a dedicated thread, allowing it to continue playing video or rendering UI even when the main Game Thread is completely blocked by heavy asset loading.

It is the primary mechanism for ensuring that a game does not appear to “hang” or “freeze” during level transitions or initial boot-up.

Practical Usage Tips & Best Practices
1. Use for Thread-Safe Loading UI

The MoviePlayer runs on its own thread to ensure smooth playback while the engine is busy.

Best Practice: When creating a loading screen widget via ILoadingScreenAttributes, ensure your Slate code is thread-safe. Avoid accessing UObjects or game-thread-only variables inside the loading UI, as this will lead to crashes. Proper isolation results in the elimination of hitching during intense CPU spikes.
2. Place Startup Movies in the Correct Directory

The MoviePlayer has strict requirements for where it looks for files to play before the engine is fully initialized.

Tip: Always place your startup videos in your project’s Content/Movies/ folder. The engine specifically looks for this path during the early boot sequence. Using this standardized location ensures the elimination of “File Not Found” errors during the initial splash screen sequence.
3. Configure via ILoadingScreenAttributes

To display a loading screen between levels in C++, you must interface with the GetMoviePlayer() singleton and pass it a set of attributes.

Best Practice: Set the bAutoCompleteWhenLoadingCompletes flag to true if you want the movie to stop as soon as the level is ready. If you want the player to see the full cinematic, set it to false. Proper configuration leads to the elimination of abrupt transitions that can break player immersion.
4. Leverage Slate for Interactive Loading Elements

While the MoviePlayer can play .mp4 files, it also supports a WidgetLoadingScreen attribute.

Tip: You can pass a SWidget (Slate) to the MoviePlayer to show progress bars or spinning icons. Because this is rendered on the movie thread, the animation will stay fluid even if the game is loading a 10GB level. This facilitates the elimination of “frozen” loading bars that frustrate users.
5. Handle “Open Level” stutters

Calling UGameplayStatics::OpenLevel is a blocking operation that normally destroys the current viewport.

Best Practice: Trigger the MoviePlayer’s SetupLoadingScreen just before calling a level change. The MoviePlayer will take over the rendering context, leading to the elimination of the black frame that usually occurs when the engine tears down the old world to build the new one.
6. Utilize “Wait for Manual Stop”

In some cases, you may want to keep the loading screen up until the player presses a button, even if the level is fully loaded.

Tip: Enable bWaitForManualStop in your attributes. This allows the game to perform post-load logic (like spawning the player or initializing network data) in the background while the UI stays up, resulting in the elimination of “pop-in” where the player sees the world before it is fully settled.
7. Optimize Video Encoding for Startup

Startup movies are played very early, often before the full GPU driver features are active.

Best Practice: Encode your startup movies in standard H.264 (MP4) with a reasonable bitrate. Avoid overly exotic codecs or extremely high resolutions for the initial boot movie. Using compatible formats ensures the elimination of startup crashes on lower-end hardware or specific consoles.
8. Verify with the “-nodisplay” Command

Sometimes it is hard to tell if a loading screen is working correctly or if the game is just fast.

Tip: Use the console command TestLoadingScreen or launch with a simulated slow drive to verify behavior. Testing under load ensures the elimination of race conditions where the loading screen might try to close before it has fully initialized its own Slate widgets.