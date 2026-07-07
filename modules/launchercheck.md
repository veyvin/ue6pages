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

ify that a game was launched through the appropriate platform launcher (such as the Epic Games Launcher).

Description and Purpose

This module provides a simple, high-level C++ interface to perform a “handshake” or environmental check during the application’s boot process. Its primary purpose is to act as a lightweight Digital Rights Management (DRM) and entitlement verification layer. It ensures that players are not bypassing the platform’s ecosystem by launching the .exe directly from the file system. If the module detects that the launcher is not active or that the user does not have the required permissions, it can trigger a restart through the launcher or eliminate the process entirely to prevent unauthorized access.

Practical Usage Tips and Best Practices
Integrate Early in the Boot Sequence
Call the launcher check as early as possible, typically in the StartupModule of your primary game module or within the PreInit phase. Checking entitlements before the engine fully initializes helps you eliminate unnecessary loading of heavy assets if the user isn’t authorized to play.
Handle “Failed to Launch” Gracefully
If the check fails, the module can return an error code or a boolean. Instead of an immediate crash, show a localized message box explaining that the game must be launched via the Epic Games Launcher. This helps you eliminate player confusion and support tickets regarding “silent” game crashes.
Configure for Shipping Builds Only
The launcher check can be an obstacle during daily development. Use preprocessor macros like #if UE_BUILD_SHIPPING to wrap your check logic. This ensures that the check is only active in the final product and helps you eliminate workflow interruptions for your internal QA and dev teams.
Include in the Build.cs Dependency List
To use the API, you must add "LauncherCheck" to your PublicDependencyModuleNames or PrivateDependencyModuleNames in your MyProject.Build.cs file. This ensures the linker can find the necessary platform-specific binaries, helping you eliminate “Unresolved External Symbol” errors during the build.
Use in Conjunction with PortalServices
For more robust DRM, use LauncherCheck alongside the PortalServices module. While LauncherCheck verifies the environment, PortalServices can verify specific DLC ownership. Combining these helps you eliminate bypasses where a user has the launcher open but does not own the specific content.
Test Launcher Restarts
The module can often be configured to automatically restart the application through the launcher if it was opened via the executable. Always test this behavior on a clean machine to ensure the “re-launch” loop works correctly, which helps you eliminate edge cases where the game fails to boot entirely.
Verify Platform-Specific behavior
Be aware that this module’s behavior changes depending on the target platform (Windows vs. macOS). Always use the FLauncherCheck::Check(…) results to drive logic that is compatible with the OS’s process management to eliminate “zombie” processes that stay in memory after a failed check.
Avoid Redundant Checks in Sub-Processes
If your game launches helper processes (like a separate crash reporter or a dedicated server), ensure they do not run the LauncherCheck. Only the main client should perform the verification to eliminate performance overhead and potential conflicts in multi-process environments.