---
layout: default
title: LauncherPlatform
---

<!-- ai-generation-failed -->

<h1>LauncherPlatform</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Portal/LauncherPlatform/LauncherPlatform.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, HTTP</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

w-level execution and process management required to run Unreal Engine applications outside of the primary Editor process. It acts as the interface between the high-level Project Launcher UI and the operating system’s process control.

What it is and What it’s used for

Located in Engine/Source/Developer/LauncherPlatform, this module is primarily responsible for the “Launch” and “Run” phases of the development pipeline. It abstracts the complexities of starting standalone game instances, server processes, or specialized commandlets across different operating systems.

Primary uses include:

Process Spawning: Executing the game executable with specific command-line arguments (e.g., -game, -log, -windowed).
Process Tracking: Monitoring the lifecycle of a launched application to detect crashes, exits, or hangs.
Pipe Communication: Capturing the standard output (stdout) and error logs from a sub-process and redirecting them to the Editor’s Output Log.
Automation Integration: Providing the hooks for the Unreal Automation Tool (UAT) to trigger local play sessions during automated testing loops.
Practical Usage Tips and Best Practices
1. Use for Local Multiplayer Testing

When testing networking, the LauncherPlatform module allows you to launch multiple “Standalone” instances of your game. By configuring a custom profile in the Project Launcher, you can spawn a client and a server simultaneously. This is a best practice for the elimination of “PIE-only” bugs that don’t appear in the editor’s simulated networking.

2. Capture Logs for Remote Debugging

If a standalone build fails to start, check the Output Log in the Editor. The LauncherPlatform module pipes the external process’s initialization log directly to you. Reviewing these logs early is essential for the elimination of silent failures caused by missing DLLs or incorrect command-line paths.

3. Monitor for “Ghost Processes”

If you force-close the Editor, sometimes the LauncherPlatform module loses its handle on the sub-processes it spawned. Always check your OS Task Manager for orphaned game instances. Manual elimination of these ghost processes is necessary to free up system memory and CPU resources before starting a new test session.

4. Leverage Zen Store for Faster Launches

In UE 5.4+, the LauncherPlatform interacts with the Zen Store to stream assets rather than waiting for a full package. Ensure your “Launch” settings are configured to use “On-the-fly” cooking. This leads to the elimination of long deployment times, allowing you to get into the game in seconds.

5. Pass Custom Arguments via Project Launcher

You can use the “Advanced” section of your Launch Profile to pass specific flags like -benchmark or -fpscap=60. This allows the LauncherPlatform to initialize the game in a controlled state, which is a best practice for the elimination of variables when performing performance profiling.

6. Verify Executable Paths

If you move your project or change the build configuration (e.g., from Development to Debug), the LauncherPlatform may look for a non-existent binary. Perform a “Clean” and “Rebuild” of your project to ensure the module has a valid target, aiding in the elimination of “File Not Found” errors during launch.

7. Use for Dedicated Server Validation

To test a “Real” server environment without packaging, use a Launch Profile set to the Server target. The LauncherPlatform will spawn the server process in a separate console window. This is the primary method for the elimination of logic errors that only occur when the game is running without a local player.

8. Strategic Elimination of Background Apps

The LauncherPlatform requires significant system overhead to pipe logs and manage process handles. For the most accurate performance testing, close unnecessary background applications (like browsers or heavy IDEs) before hitting “Launch.” This ensures the elimination of external CPU spikes that could skew your frame time data.