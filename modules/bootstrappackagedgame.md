---
layout: default
title: BootstrapPackagedGame
---

<!-- ai-generation-failed -->

<h1>BootstrapPackagedGame</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Windows/BootstrapPackagedGame/BootstrapPackagedGame.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

g the Windows packaging process. It generates the “Bootstrap Executable” (typically the .exe found in the root of your packaged folder), which acts as a wrapper or “launcher” for the actual game binary located deeper within the Binaries/Win64 directory.

Its primary purpose is to provide a user-friendly entry point that handles prerequisite checks, locates the correct engine files, and passes command-line arguments to the real executable.

Practical Usage Tips and Best Practices
1. Understand the Folder Hierarchy

The bootstrap executable is designed to live in the root of your packaged build, while the “real” game logic resides in [ProjectName]/Binaries/Win64/[ProjectName].exe. For the bootstrap to work, you must maintain this relative path structure; moving the root executable without moving the Binaries folder will result in a failure to launch.

2. Customize the Application Icon

By default, the bootstrap executable may use the Unreal Engine logo. To change this, you must set your custom icon in Project Settings > Platforms > Windows > Game Icon. The packaging process uses the BootstrapPackagedGame logic to “stamp” this icon onto the launcher executable during the cook/package phase.

3. Automatic Prerequisite Handling

The bootstrap executable is responsible for checking if the required redistributables (like the Visual C++ Runtime or DirectX) are installed. If you include the Prerequisites Installer in your packaging settings, the bootstrap can be configured to trigger the installer if it detects that the user’s machine is missing vital components.

4. Silent Command-Line Passing

Any command-line arguments passed to the bootstrap executable (e.g., -log, -windowed, or -multihome) are automatically forwarded to the internal game binary. This allows you to create desktop shortcuts with custom arguments that the bootstrap will handle transparently.

5. Admin Rights Elevation

If your game requires administrative privileges to run (e.g., for certain anti-cheat measures or writing to protected folders), you can configure the Manifest settings in the Windows platform settings. The BootstrapPackagedGame module will then generate an executable that triggers the Windows UAC prompt upon launch.

6. Troubleshooting “Missing DLL” Errors

If a packaged game fails to launch immediately upon clicking the root .exe, the issue is often that the bootstrap cannot find the entry point in the Binaries folder. Check the [ProjectName].log in the Saved/Logs folder; the bootstrap usually logs the exact path it is attempting to reach before it terminates.

7. Elimination of Splash Screen Lag

The bootstrap executable can display a splash screen immediately while the heavy engine DLLs are still loading into memory. To optimize the user experience, ensure your splash screen image is a lightweight BMP or PNG in the Project Settings, allowing for the elimination of the “dead time” where the user wonders if the game is actually starting.

8. Verify Architecture Compatibility

The bootstrap executable is compiled specifically for the target architecture (usually Win64). If you are creating a custom build pipeline or using a specialized version of the engine, ensure that the BootstrapPackagedGame project in the Unreal Engine source solution is compiled with the same settings as your game to avoid “Application Error” crashes on startup.