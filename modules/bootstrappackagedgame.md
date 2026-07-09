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

he environment is correctly set up before “handing off” execution to the main game process.

1. Module Configuration

This is a low-level engine module that is automatically included by the Unreal Automation Tool (UAT) during the staging and packaging process. Developers rarely need to add it to their Build.cs manually, but its source code (found in Engine/Source/Programs/Windows/BootstrapPackagedGame) is the place to look if you need to understand the entry point of your packaged application.

2. Practical Usage Tips & Best Practices
Automatic Prerequisite Checking

One of the primary roles of this module is to check if the required Unreal Prerequisites (DirectX, VC++ Redistributables) are installed.

Best Practice: In your Project Settings under Windows > Packaging, ensure “Include Prerequisites” is enabled. The bootstrapper will then automatically detect missing components and prompt the user to install them, “eliminating” potential startup crashes on fresh Windows installations.
Transparent Command-Line Passthrough

The bootstrapper is designed to be “invisible” to command-line arguments. Any flags you pass to the root .exe (e.g., -log, -windowed, or custom game-logic flags) are captured by the BootstrapPackagedGame logic and passed directly to the internal game binary. You do not need to perform any special handling to ensure your arguments reach the game.

Handling Portable Installations

The bootstrapper uses relative paths to locate the main game binary. This makes your packaged folder “portable.” You can move the entire project folder to a different drive or machine, and the BootstrapPackagedGame shim will still correctly resolve the path to the internal Win64 binary without needing absolute path registration in Windows.

Icon Customization

The icon you see on the root .exe of your packaged game is applied via this module during the “Stage” phase of packaging.

Tip: Always set your project icon in Project Settings > Windows > Game Icon. The packaging tool will inject this .ico file into the bootstrapper executable, “eliminating” the default Unreal Engine logo from the user’s view.
“Eliminating” redundant processes

The bootstrapper is a “Fire and Forget” launcher. Once it successfully launches the main game process, the shim process terminates itself. This ensures that the bootstrapper does not remain in memory consuming resources or appearing as a secondary “ghost” process in the Windows Task Manager.

Troubleshooting Launch Failures

If your packaged game fails to open but the internal binary (found in [Project]/Binaries/Win64/) works fine, the issue is likely with the bootstrapper’s ability to find its dependencies.

Tip: Check the Manifest_NonUFSFiles_Win64.txt in your build folder. This manifest is used by the bootstrapper to verify the file structure; if it is missing or corrupted, the bootstrapper may fail to initiate the launch.
Use for Administrative Elevation

If your game requires administrative privileges (e.g., for certain anti-cheat measures or writing to protected folders), you can modify the app.manifest within the BootstrapPackagedGame source (if building the engine from source) to require “Administrator” execution level. This ensures the entire process chain is elevated from the moment the user double-clicks the icon.

Working with “Fixed Seed” and Encryption

If your project uses signed paks or encrypted data, the bootstrapper ensures the correct environment variables are set so the internal binary can access the decryption keys stored in the metadata. Attempting to run the internal binary directly without the environment initialized by the bootstrapper can sometimes “eliminate” access to encrypted assets.