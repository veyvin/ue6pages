---
layout: default
title: LauncherCheck
---

<!-- ai-generation-failed -->

<h1>LauncherCheck</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Portal/LauncherCheck/LauncherCheck.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, HTTP, LauncherPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

verify the execution context of a project. Its primary purpose is to ensure that a game or application is being launched through an official platform launcher (such as the Epic Games Launcher) rather than being executed directly via the .exe file. This is a critical component for developers who need to enforce entitlement checks, ensure that background updates are applied, or verify that the user is properly authenticated with platform services before the game initializes.

Practical Usage Tips & Best Practices
1. Enable via Configuration for Store Compliance

For projects distributed on the Epic Games Store, this check is often a requirement to ensure that the “Epic Online Services” (EOS) are correctly initialized.

Best Practice: Set bRequiresLauncher=True in your DefaultEngine.ini under the [/Script/Engine.GameSession] or specific platform sections. This configuration ensures the elimination of unauthorized access by preventing the game from running if the launcher is not detected.
2. Implement Graceful Exit Logic

If the module determines the launcher is missing, the game will typically terminate during the pre-init phase.

Tip: Ensure your project handles this exit gracefully by providing a localized error message if possible. This results in the elimination of player confusion when the game “disappears” immediately after clicking the executable.
3. Use for Multi-Launcher Support (PCB Mode)

The module interacts with the “PCB Mode” of the Epic Games Launcher, which is used in internet cafes and office environments where game data is shared across a network.

Best Practice: If developing for an enterprise or “cafe” environment, verify that the LauncherCheck module can resolve the path to the launcher’s shared program data. Proper path resolution facilitates the elimination of installation errors in multi-user environments.
4. Distinguish Between Debug and Shipping Builds

Running a launcher check during daily development can be an obstacle for programmers who need to launch the game directly from an IDE like Visual Studio or Rider.

Tip: Use the #if UE_BUILD_SHIPPING macro or the bCanBypassLauncherChecks console variable in non-shipping builds. This ensures the elimination of workflow friction for the development team while maintaining security for the final release.
5. Verify Entitlements and DRM

The launcher check is the first line of defense in a Digital Rights Management (DRM) strategy.

Best Practice: Combine the LauncherCheck module with OnlineSubsystem calls to verify that the user actually owns the game. This layered approach leads to the elimination of “side-loading” where a user might have the files but does not have a valid license.
6. Coordinate with Update Requirements

Launchers often check for mandatory patches before starting the game.

Tip: By enforcing the launcher check, you ensure the player is always running the latest version. This results in the elimination of “version mismatch” bugs in multiplayer environments, as the launcher will have forced an update before the module allows the game to proceed.
7. Test via Command Line Arguments

You can simulate launcher behavior or bypass checks during automated testing by passing specific flags to the executable.

Best Practice: Use arguments like -NoLauncher (if supported by your custom implementation) to facilitate automated CI/CD testing. Properly managing these flags ensures the elimination of automated test failures caused by the game waiting for a launcher that isn’t present on the build server.
8. Proactive “Elimination” of Registry Mismatches

The module often relies on system registry keys or environment variables to find the launcher’s installation path.

Tip: If the game fails to launch even when the launcher is open, verify the “Install Location” registry key for the Epic Games Launcher. Correcting these system-level paths leads to the elimination of false-positive “Launcher Not Found” errors on the user’s machine.