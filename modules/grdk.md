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

opment Kit module) is the integration layer for building, running, and shipping Unreal Engine games on Xbox consoles and the Windows Store.

Description and Purpose

This module acts as the primary interface between Unreal Engine and the Microsoft Gaming Runtime. It replaces legacy XInput and Xbox Live implementations with a unified API that handles everything from identity management (Xbox Live profiles) to storage, networking, and commerce. The “GRDK” nomenclature typically refers to the environment and build-logic used to target the WinGDK and Xbox platforms. It is essential for developers who need to implement platform-specific features like “Play Anywhere,” cross-progression, or Xbox achievement systems.

Practical Usage Tips and Best Practices
Set the GRDKLatest Environment Variable
Before compiling your project for Windows GDK or Xbox, you must have the Microsoft GDK installed and the GRDKLatest environment variable set to the correct version path. Failing to set this will eliminate the Unreal Build Tool’s (UBT) ability to locate the necessary headers and libraries for compilation.
Implement the MSGameOSSSelector Plugin
For cross-platform titles, use the MSGameOSSSelector plugin. This ensures that the engine automatically selects OnlineSubsystemGDK when the game is launched as a packaged Microsoft Store app. This automation helps you eliminate logic errors where the game might incorrectly attempt to use Steam or Epic Online Services on a Microsoft platform.
Configure Game Input for Windows
Switch to the Game Input (Windows) plugin managed within the GDK module. This is a next-generation API that provides unified support for gamepads, racing wheels, and flight sticks. Using this modern API helps you eliminate the need for older, separate plugins like Raw Input or XInput.
Automate Remote Deployment and Launching
Leverage the Xbox PC Remote Tools integrated with the GDK module. You can use the RunUAT BuildCookRun command with the -deploy and -device flags to send builds directly to a remote PC or console. This process helps you eliminate the slow manual transfer of large build folders over the network.
Handle User Login Flows Early
When using the GDK, the “User” is the central entity. Ensure your game handles the “User Picker” or “Silent Sign-in” flow immediately upon launch. Proper user handling is required to eliminate issues with SaveGame systems that rely on a valid GDK User ID to associate data.
Use Architecture-Specific Configuration Files
Place GDK-specific overrides in Config/Windows/MSGameOSS/WindowsEngine.ini. This allows you to define platform-specific NetDriverDefinitions or SaveGameSystemModules without affecting your standard Win64 builds. This separation helps you eliminate configuration bloat and potential platform conflicts.
Validate Identity and Service Config IDs
Ensure the TitleID, IdentityName, and SCID (Service Configuration ID) in your Project Settings match the Microsoft Partner Center exactly. Incorrect IDs will eliminate your access to Xbox Live services, preventing you from testing multiplayer or cloud saves during development.
Check Bootstrap Settings for Redistributables
In your DefaultEngine.ini, set GameInput::IncludeRedistFiles=True. This tells the bootstrapper to run the GameInputRedist.msi installer when the game is first run by a player. This step is vital to eliminate support tickets from users whose controllers are not recognized because of missing system drivers.