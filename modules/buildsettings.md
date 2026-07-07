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

vides C++ access to metadata about the current build. It acts as a bridge between the Unreal Build Tool (UBT) and the compiled binary, allowing the engine to “know” when it was built, which branch it came from, and what versioning parameters were used during the compilation process.

This module is primarily used for telemetry, debugging, and version watermarking, ensuring that developers and QA teams can precisely identify the origin of any specific executable.

Practical Usage Tips and Best Practices
1. Include the Module Dependency

To access build metadata in your own classes, you must first add the module to your Build.cs file. Since this information is generally useful for internal tracking, you may want to gate it for non-shipping builds or specific modules.

C#
PublicDependencyModuleNames.Add("BuildSettings");
Copy code
2. Implement a Debug Watermark

Use the FBuildSettings class to display build information on your HUD or UI. This is incredibly helpful for QA reports. By calling FBuildSettings::GetBuildDate(), you can show exactly when the current executable was compiled, assisting in the elimination of confusion regarding whether a tester is on the latest build.

3. Track Branch Information

If your studio uses multiple streams (e.g., Main, Release, Feature_X), use FBuildSettings::GetCurrentBranch() to log the source branch. This ensures that any crashes reported via telemetry can be traced back to the correct code repository, streamlining the bug-fixing process.

4. Distinguish Between Build Configurations

While you can use preprocessor macros like UE_BUILD_SHIPPING, the BuildSettings module can be used at runtime to query build-time flags. This is useful for custom logging systems that need to format strings differently based on whether the build was intended for internal “Development” or external “Shipping.”

5. Verify Build Version Compatibility

In multiplayer environments, you can use the strings provided by BuildSettings to perform a version check during the handshake process. Comparing build IDs helps in the elimination of “mismatched version” errors that occur when a client tries to connect to a server running a different iteration of the code.

6. Automate Telemetry Metadata

When sending crash reports or performance metrics to an external database, include the results from FBuildSettings::GetCompatibleMinEngineVersion(). This allows data analysts to group performance regressions by engine version and build date, making it easier to spot when a specific change impacted frame rates.

7. Combine with Version.h for Precision

For the most accurate versioning, combine BuildSettings with the macros found in Version.h. While Version.h gives you the static engine version (e.g., 5.6.0), BuildSettings provides the dynamic context of your specific project’s build, such as the timestamp and branch name.

8. Use for Asset “Baking” Validation

During the cook process, you can use build settings to embed a “Build Stamp” into your data. If a packaged game tries to load an asset that was cooked on a different date than the executable, you can trigger a warning. This is a powerful way to ensure the elimination of stale or incompatible cooked data in a local build environment.