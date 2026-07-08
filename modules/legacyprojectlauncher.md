---
layout: default
title: LegacyProjectLauncher
---

<!-- ai-generation-failed -->

<h1>LegacyProjectLauncher</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/LegacyProjectLauncher/LegacyProjectLauncher.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, DesktopPlatform, InputCore, LauncherServices, Slate, SlateCore, ToolWidgets, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ng logic for the original “Project Launcher” tool in Unreal Engine. It serves as a comprehensive UI wrapper for the AutomationTool (UAT), allowing developers to manage the Build, Cook, Package, and Deploy (BCPD) pipeline without using command-line arguments.

While the engine has moved toward more modern deployment flows (like “Turnkey”), this module remains essential for creating Custom Launch Profiles. It is primarily used for advanced distribution tasks, such as managing patches, creating DLC, and targeting specific device groups, facilitating the elimination of manual packaging errors through saved, repeatable configurations.

Practical Usage Tips and Best Practices
1. Create Custom Profiles for Iteration

Avoid using the “Default” launch profiles for complex tasks. Create a Custom Launch Profile within the launcher to save specific settings like “Cook on the fly” or “Skip build.” This practice leads to the elimination of repetitive setup time when switching between debugging a level and packaging a final build.

2. Generate and Audit UAT Commands

The Project Launcher generates a long string of command-line arguments for RunUAT.bat (visible in the log window). Copying these commands is a best practice for the elimination of guesswork when setting up a headless Continuous Integration (CI) system, as you can verify exactly what flags the editor uses.

3. Manage Patching and DLC

This module contains the “Advanced” settings required for generating .pak file patches. By specifying a “Base Build” to the launcher, it calculates the difference between versions. This facilitates the elimination of massive download sizes for players, as only the changed data is packaged into the patch.

4. Use “Cook on the fly” for Rapid Testing

When testing on a physical device, set the “Cook” option to “On the fly.” This allows the device to request assets from your PC over the network as needed. It leads to the elimination of the long “Wait for Cook” phase, allowing you to jump into the game almost immediately after a code change.

5. Verify Build.cs for Editor Tools

If you are building an Editor Utility Widget that needs to trigger a build, you must include "LegacyProjectLauncher" in your Editor.Build.cs. Proper module linking is required for the elimination of linker errors when trying to programmatically start a launch profile from your custom UI.

6. Optimize Chunking for Storage

Use the “Advanced” packaging settings in the launcher to enable Chunking. This allows the module to split your game into multiple smaller .pak files. This assists in the elimination of memory pressure on devices with limited storage and allows for “Ready to Play” features where only the first chunk is required to start the game.

7. Handle Process “Elimination” Safely

The launcher has the ability to “Terminate” a running instance of your game on a remote device before deploying a new one. Ensure your game handles the FCoreDelegates::OnPreExit delegate to ensure that this elimination of the app process doesn’t result in corrupted save data or incomplete log writes.

8. Monitor Logs for “Cooker Busy” Errors

If multiple people are using the same shared build machine, the Project Launcher might fail if the cooker is already active. Checking the “Output Log” tab within the launcher facilitates the elimination of “silent failures” by providing real-time feedback from the underlying Automation Tool processes.