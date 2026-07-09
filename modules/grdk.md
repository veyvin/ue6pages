---
layout: default
title: GRDK
---

<!-- ai-generation-failed -->

<h1>GRDK</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Microsoft/GRDK/GRDK.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

+ integration layer for the Microsoft Game Development Kit (GDK) within Unreal Engine. It serves as the primary bridge between the engine and the Microsoft Game Runtime (XGameRuntime), enabling core platform features for Xbox consoles (Series X|S, Xbox One) and the Microsoft Store on Windows. This module handles low-level initialization, user identity management, and the implementation of GDK-specific systems such as cloud-synced save games and streaming installation.

Practical Usage Tips & Best Practices
1. Correctly Configure the GRDKLatest Environment Variable

Unreal Build Tool (UBT) requires a specific environment variable to locate the GDK headers and libraries on your development machine.

Best Practice: Ensure the GRDKLatest environment variable is set to the correct path of your installed Microsoft GDK (e.g., C:\Program Files (x86)\Microsoft GDK\240400\). An incorrect path is the leading cause for the elimination of successful C++ compilation for the WinGDK and Xbox build targets.
2. Enable Lazy Initialization for Faster Boot

By default, the GDK runtime may attempt to initialize all services immediately upon startup, which can slow down the initial splash screen phase.

Tip: Set MSGamingRuntime:bLazyInitialize=true in your DefaultEngine.ini. This defers the initialization of non-essential GDK components until they are actually needed, leading to the elimination of unnecessary boot-time delays for players.
3. Use GDKSaveGameSystem for Cloud Synchronization

Standard Unreal save games do not inherently support the cloud-syncing requirements of the Xbox ecosystem.

Best Practice: Configure your project to use the GDKSaveGameSystem module by adding Platform Features: SaveGameSystemModule=GDKSaveGameSystem to your configuration files. This ensures that player progress is correctly synchronized with the Microsoft cloud, resulting in the elimination of data loss when players switch between different devices.
4. Test Services with the -ForceOSSGDK Command

Xbox Live features (identity, achievements, presence) typically only function when the game is running as a signed Microsoft Store package.

Tip: Use the -ForceOSSGDK command-line argument during development. This forces the engine to apply the GDK configuration even when running a loose-file build from the editor, facilitating the elimination of the need to package the game for every minor online feature test.
5. Integrate the MSGameOSSSelector Plugin

If your project targets multiple PC stores (e.g., Steam and the Microsoft Store), you must dynamically select the correct Online Subsystem.

Best Practice: Enable the MSGameOSSSelector plugin and add +AdditionalModulesToLoad=MSGameOSSSelector to your WindowsEngine.ini. This plugin detects the environment and automatically switches to OnlineSubsystemGDK, ensuring the elimination of hardcoded logic for different store distributions.
6. Automate GDK Redistributable Installation

Players on Windows may not have the necessary Game Input libraries installed, which can cause controllers to fail.

Tip: Set Game Input::IncludeRedistFiles=True in your DefaultEngine.ini. This tells the bootstrapper to run the GameInputRedist.msi installer when the game is launched, which leads to the elimination of input-related support issues on fresh Windows installations.
7. Wrap Async GDK Calls in the Task System

GDK functions (prefixed with X) are often asynchronous and require an XTaskQueueHandle to process.

Best Practice: Always execute GDK-specific asynchronous calls using the Unreal Task System or FAsyncTask. Offloading these calls to background threads ensures the elimination of game-thread hitches while waiting for the Microsoft Game Runtime to return identity or storage results.
8. Monitor LogGameInput for Initialization Errors

Input issues are common when first integrating the GDK into an existing Windows project.

Tip: Check the engine logs for the LogGameInput category. This log provides detailed information on whether the Game Input plugin started correctly and identifies missing libraries, assisting in the elimination of “silent failures” where gamepads simply stop responding.