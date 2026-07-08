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

integration layer for the Microsoft Game Development Kit (GDK) within Unreal Engine.

Description

The GRDK module provides the necessary APIs and glue code to bridge Unreal Engine with the Microsoft Gaming Runtime. It is primarily used for projects targeting Xbox Series X|S, Xbox One, and the Windows Store (PC). This module handles low-level platform requirements, including user identity management, Xbox Live services, and hardware-specific optimizations. It serves as the prerequisite for high-level features like Achievements, Cloud Saves, and Multiplayer matchmaking on the Microsoft ecosystem.

Practical Usage Tips and Best Practices
1. Environment Variable Configuration

Before you can compile or use the module, you must have the Microsoft GDK installed and the GRDKLatest environment variable set correctly on your development machine. The Unreal Build Tool (UBT) uses this variable to locate the platform-specific headers and libraries required to link the GRDK module into your project.

2. Use the OnlineSubsystemGDK Selector

When targeting the Microsoft Store or Xbox, leverage the OnlineSubsystemGDK plugin. A best practice for modern UE projects is to use the MS Game OSS Selector module. This plugin automatically detects if the game is running as a packaged Microsoft Store app and toggles the GDK-based online services, preventing the elimination of online functionality when moving between development and retail environments.

3. Implement Game Input for Windows

The GDK introduces a modern input API. You should enable the Game Input (Windows) plugin, which relies on the GRDK module. This API provides superior support for “special” devices like racing wheels and flight sticks compared to legacy XInput. Ensure you include the Game Input redistributable by setting GameInput::IncludeRedistFiles=True in your DefaultEngine.ini.

4. Handle “Engagement” and User Login

On GDK-supported platforms, specifically Xbox, you must handle the “Press Start” engagement screen to map a physical controller to a user identity. Use the Common User Subsystem alongside the GRDK module to manage this flow. This ensures that when a player is eliminated or logs out, the game correctly saves their profile data to the appropriate Microsoft account.

5. Remote Deployment and Debugging

The GRDK module supports remote deployment via Xbox PC Remote Tools. In the editor’s “Launch On” menu, you can add remote Windows PCs or Xbox consoles. This allows you to deploy and test GDK-specific features (like the Microsoft Store overlay) directly from your workstation, significantly speeding up the iteration loop for console-specific bug fixes.

6. Command Line Forcing

During testing, you can force the GDK online configuration by using the launch argument -ForceOSSGDK. Conversely, use -ForceNoOSSGDK to disable it. This is a critical best practice for debugging scenarios where you need to verify if a bug is specific to the Microsoft Gaming Runtime or the core engine logic.

7. Manage Memory Constraints

Xbox consoles have stricter memory management and “Title Memory” limits compared to open PCs. Use the GDK-specific memory profilers to monitor your allocation. The GRDK module helps report these platform-specific memory pressures back to the engine, allowing you to trigger the elimination of non-essential assets or clear the DDC cache before the OS terminates the game process for exceeding limits.

8. Verify Sandbox Settings

When testing achievements or multiplayer via the GRDK module, ensure your machine is set to the correct Xbox Live Sandbox (e.g., RETAIL or a private dev sandbox). If the sandbox is mismatched, the GRDK module will fail to initialize user services, resulting in “Service Unavailable” errors during login attempts.