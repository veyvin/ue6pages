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

ating the “wrapper” executable found in the root directory of a packaged Windows project. When you package a game, Unreal generates a small .exe in the root (e.g., MyGame.exe) and a larger, actual engine executable inside the Binaries/Win64 folder.

Its primary purpose is to act as a secure and intelligent entry point that handles prerequisite checks, identifies the correct platform architecture (x64 vs. ARM64), manages command-line arguments, and launches the actual engine process with the correct environment variables.

Practical Usage Tips and Best Practices
1. Distinguish Between the Wrapper and the Binary

Understand that the .exe in your root folder is the Bootstrap executable, while the one in [ProjectName]/Binaries/Win64/ is the actual game. If you are creating custom installers or shortcuts, always point to the root Bootstrap executable. This ensures that the engine’s expected directory structure and environment remain intact, assisting in the elimination of “Missing DLL” errors.

2. Automate GameInput Redistributables

As of recent engine versions (UE 5.4+), you can configure the bootstrapper to automatically run the GameInputRedist.msi installer if it is missing from the user’s system. To enable this, add the following to your DefaultEngine.ini:

ini
	[GameInput]

	IncludeRedistFiles=True
Copy code

The bootstrapper will handle the installation attempt before the game launches, ensuring the elimination of input-related crashes on fresh Windows installs.

3. Seamless Command-Line Passing

The Bootstrap module is designed to forward all command-line arguments to the main game executable. If you need to launch your packaged game with specific flags (e.g., -log, -windowed, or -dx12), you can pass them directly to the root .exe. The bootstrapper ensures these are sanitized and passed through correctly to the engine.

4. Architecture Detection (x64 vs. ARM64)

In projects targeting multiple Windows architectures, the bootstrapper acts as a selector. It detects the host machine’s architecture and launches the appropriate binary. This prevents the user from accidentally running a binary that would perform poorly under emulation, leading to the elimination of architecture-mismatch performance issues.

5. Prerequisite Handling and Manifests

The bootstrapper checks for the presence of the Visual C++ Redistributable and other core dependencies defined in the project’s deployment manifest. If these are missing, it can trigger the UEPrereqSetup_x64.exe. Ensure your distribution package includes these prerequisite installers in the expected subfolders so the bootstrapper can find them.

6. Customizing the Application Icon

The icon seen on the root Bootstrap executable is controlled by the Project Settings > Platforms > Windows > Application Icon setting. Because the bootstrapper is a separate small build process, changing this setting requires a full repackage of the project to update the icon on the wrapper .exe.

7. Avoid Bypassing for Steam/Epic Games Store

When uploading your game to digital storefronts, set the “Launch Executable” to the root Bootstrap .exe. Storefront overlays (like Steam Overlay) rely on the process tree started by the bootstrapper. Bypassing it can lead to the elimination of social features or achievement tracking.

8. Use for Secure Launching

The bootstrapper can be extended (via engine source modification) to perform early-stage integrity checks or anti-cheat initialization before the heavy engine DLLs are even loaded into memory. This provides a “clean” entry point for the elimination of unauthorized memory tampering during the early boot phase.