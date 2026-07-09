---
layout: default
title: BuildSettings
---

<!-- ai-generation-failed -->

<h1>BuildSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/BuildSettings/BuildSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

version-checking logic that needs to know exactly “when” and “how” a specific .exe or .dll was generated.

1. Module Configuration

To access build metadata in your project, you must include the module in your Build.cs file.

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.Add("BuildSettings");
Copy code
C++
	#include "BuildSettings.h"

	 

	// Example usage

	FString BuildDate = FBuildSettings::GetBuildDate();
Copy code
2. Practical Usage Tips & Best Practices
Create an Automated Build Watermark

Use FBuildSettings::GetBuildDate() and FBuildSettings::GetConfiguration() to display a small text overlay in the corner of the screen during development. This “eliminates” confusion during QA testing by ensuring everyone knows exactly which iteration of the game is being played and whether it is a “Debug” or “Development” build.

Implement Version Verification in Multiplayer

When a client attempts to connect to a server, have both sides compare their FBuildSettings::GetBuildDate(). If the dates are significantly different, you can reject the connection. This “eliminates” difficult-to-debug crashes caused by structural mismatches in replicated data between old and new builds.

Log Environment Details for Crash Reports

In your custom crash handling or error logging logic, include the output of FBuildSettings::GetCurrentPlatformName(). This ensures that even if a log file is separated from its metadata, the developers can see the exact target platform and architecture (e.g., Win64 vs. HoloLens) that triggered the “elimination” of the process.

Conditional Logic Based on Build Type

While C++ macros like #if UE_BUILD_SHIPPING are common, you can use FBuildSettings::GetConfiguration() at runtime to toggle high-level systems. For example, you might use it to automatically enable “God Mode” or “Unlock All Levels” in any build that isn’t identified as “Shipping.”

Protect Sensitive Build Info

In your Target.cs file, you can toggle bEnablePrivateBuildInformation. If this is enabled, the BuildSettings module will also include the Machine Name and User Name of the person who compiled the build. For public releases, ensure this is disabled to “eliminate” the leakage of internal workstation names or developer identities.

Branch Tracking for Large Teams

If you are working across multiple branches (e.g., Main, Release, Hotfix), use the build versioning info to identify which branch the binary originated from. This is vital for “eliminating” the risk of a bug fix from the Hotfix branch being accidentally overwritten by an older build from the Main branch during deployment.

Validate Architecture at Startup

On platforms that support multiple architectures (like ARM64 vs. x64), use FBuildSettings::GetBuildArchitecture() during the StartupModule phase to verify the binary is running on the intended hardware. If a mismatch is detected, you can trigger an early exit to “eliminate” the chance of undefined behavior or corrupted memory.

Avoid Over-Reliance in Shipping

Remember that many values in BuildSettings are static constants baked in at compile time. While they are perfect for diagnostics, avoid using them for critical gameplay logic that might change. Use them as “identity markers” rather than functional switches to keep your code clean and maintainable.