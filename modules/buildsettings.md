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

{

	    PrivateDependencyModuleNames.Add("BuildSettings");

	}

	```

	 

	#### 2. Create an Automatic Version Watermark

	Use `BuildSettings::GetBuildDate()` to display a timestamp in the corner of the screen for non-shipping builds. This helps in the **elimination** of confusion when reviewers send screenshots of bugs from outdated versions.

	```cpp

	#include "BuildSettings.h"

	 

	FString VersionOverlay = FString::Printf(TEXT("Build Date: %s | Config: %s"), 

	    *BuildSettings::GetBuildDate(), 

	    *BuildSettings::GetBuildConfiguration());

	```

	 

	#### 3. Secure Private Information

	By default, "Private Build Information" (like the machine name or the username of the person who compiled the build) is disabled for security. If you need this for internal tracking, you must enable it in your `Target.cs` file:

	```csharp

	// MyProject.Target.cs

	bEnablePrivateBuildInformation = true;

	```

	*Note: Ensure this is disabled for public releases to maintain the **elimination** of potential security leaks regarding your internal build infrastructure.*

	 

	#### 4. Log Build Info on Startup

	Implement a simple logging block in your `GameInstance` or `ModuleStartup` to print the build details. This is invaluable when analyzing log files sent by remote playtesters.

	```cpp

	UE_LOG(LogTemp, Log, TEXT("Running Branch: %s"), *BuildSettings::GetBuildBranch());

	```

	 

	#### 5. Use Configuration for Runtime Logic

	While you should generally use `#if UE_BUILD_SHIPPING` for pre-processor logic, `BuildSettings::GetBuildConfiguration()` is useful for runtime checks where you want to display the configuration name in a UI menu or "About" screen without using macros.

	 

	#### 6. Differentiate from EngineVersion

	Do not confuse `BuildSettings` with `FEngineVersion`. `FEngineVersion` tells you which version of the **Unreal Engine** you are using (e.g., 5.6.0). `BuildSettings` tells you the metadata of your **Project's specific compilation**. Always use both to get a full picture of the environment.

	 

	#### 7. Verify Branch Consistency

	In large teams with multiple feature branches, use `BuildSettings::GetBuildBranch()` to perform a "sanity check" on startup. You can throw a warning if a developer is accidentally running a "Main" branch binary against "Release" branch content, assisting in the **elimination** of mismatched asset bugs.

	 

	#### 8. Avoid Gameplay-Critical Reliance

	Never use `BuildSettings` for gameplay logic (e.g., changing weapon damage based on the build date). Because this module is part of the `Developer` folder, it may be stripped or behave differently in certain monolithic shipping builds. Keep its usage strictly for **diagnostics, UI metadata, and logging**.
Copy code
2. Create an Automatic Version Watermark

Use BuildSettings::GetBuildDate() to display a timestamp in the corner of the screen via UMG or a Debug Overlay. This helps in the elimination of confusion when reviewers send screenshots of bugs from outdated versions, as the build time is burned into the image.

3. Log Build Info on Startup

Implement a simple logging block in your GameInstance or ModuleStartup to print the build details. This is invaluable when analyzing log files sent by remote playtesters to confirm they are on the correct branch.

C++
	#include "BuildSettings.h"

	 

	UE_LOG(LogTemp, Log, TEXT("Running Branch: %s"), *BuildSettings::GetBuildBranch());
Copy code
4. Secure Private Information

By default, “Private Build Information” (such as the machine name or the username of the person who compiled the build) is disabled. If you need this for internal tracking of “who made this build,” you must enable it in your .Target.cs file:

C#
bEnablePrivateBuildInformation = true;
Copy code

Note: Ensure this is disabled for public releases to maintain the elimination of potential security leaks regarding your internal infrastructure.

5. Verify Branch Consistency

In large teams with multiple feature branches, use BuildSettings::GetBuildBranch() to perform a “sanity check” on startup. You can throw a warning if a developer is accidentally running a “Main” branch binary against “Release” branch content, assisting in the elimination of mismatched asset bugs.

6. Differentiate from EngineVersion

Do not confuse BuildSettings with FEngineVersion. FEngineVersion tells you which version of the Unreal Engine you are using (e.g., 5.6.0). BuildSettings tells you the metadata of your Project’s specific compilation. Always use both for comprehensive versioning.

7. Use Configuration for Runtime UI

While you should use #if UE_BUILD_SHIPPING for pre-processor logic, BuildSettings::GetBuildConfiguration() is useful for runtime checks where you want to display the configuration name in a UI “About” screen or a bug report form without using complex macros.

8. Avoid Gameplay-Critical Reliance

Never use BuildSettings for gameplay logic (e.g., changing player stats based on the build date). Because this module is part of the Developer folder, it may behave differently or be stripped in certain monolithic shipping builds. Keep its usage strictly for diagnostics and metadata.