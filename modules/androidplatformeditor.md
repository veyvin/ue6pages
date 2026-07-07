---
layout: default
title: AndroidPlatformEditor
---

<!-- ai-generation-failed -->

<h1>AndroidPlatformEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Android/AndroidPlatformEditor/AndroidPlatformEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AndroidDeviceDetection, AndroidRuntimeSettings, AudioSettingsEditor, Core, CoreUObject, DesktopPlatform, DesktopWidgets, EditorWidgets, Engine, InputCore, MainFrame, MaterialShaderQualitySettings, MaterialShaderQualitySettingsEditor, PropertyEditor, RHI, RenderCore, ShaderPlatformConfigEditor, SharedSettingsWidgets, Slate, SlateCore, SourceControl</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

UI, and settings required to configure, package, and deploy Unreal Engine projects to Android devices. It provides the integration between the Unreal Editor and the Android SDK/NDK toolchain, housing the logic for the “Project Settings > Android” and “Android SDK” panels.

This module is used by developers to manage APK/App Bundle packaging, manifest overrides, distribution signing (keystores), and hardware-specific configurations (like Vulkan support or texture compression formats).

Practical Usage Tips and Best Practices
1. Manage Editor-Only Dependencies

Since this module handles editor UI and deployment logic, it must only be referenced within Editor targets. Ensure your Build.cs includes it within a conditional block to avoid packaging errors for the runtime game.

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "AndroidPlatformEditor" });

	}
Copy code
2. Utilize Manifest Additions for Custom Logic

Avoid manually editing the AndroidManifest.xml in the Intermediate folder, as it is overwritten every build. Instead, use the Advanced APK Packaging section (managed by this module) to add tags. You can also place text files in your project’s /Build/Android/ folder (e.g., ManifestRequirementsAdditions.txt) to inject custom permissions or activities.

3. Use Project-Level SDK Overrides

While global SDK paths are set in the Editor Preferences, you can use this module’s settings in Project Settings to override the SDK, NDK, and Java versions for a specific project. This is critical when maintaining multiple projects that require different NDK versions (e.g., NDK r25b vs r21d).

4. Configure Distribution Signing Early

The module provides the interface for entering Keystore information. To prevent deployment failures, ensure your .keystore file is placed in Build/Android/. Never check your Keystore passwords into public source control; use the “Distribution Signing” fields carefully and consider environment variables for automated build machines.

5. Debug via the Intermediate Folder

If your app fails to launch, check the generated manifest at Project/Intermediate/Android/arm64/AndroidManifest.xml. This module assembles this file from various sources; verifying the output here is the best way to ensure your “Extra Tags” or “Permissions” were injected correctly.

6. Optimize Build Targets for Testing

In the Android settings provided by this module, you can toggle support for specific architectures (ARM64, x86_64). During daily development, disable unused architectures to significantly reduce packaging time. Ensure only ARM64 is enabled for modern Google Play Store compliance.

7. Track Hardware Support via Visual Indicators

The module’s settings allow you to enable or disable support for Vulkan and OpenGL ES3.2. Use the “Build” section to define the “Minimum SDK Version” and “Target SDK Version.” Setting a higher Minimum SDK (e.g., 24 or 26) can eliminate the need to support ancient hardware, simplifying your shader compilation and testing.

8. Verify Elimination of Redundant Permissions

Google Play often rejects apps with unnecessary permissions (like READ_PHONE_STATE). Use the Extra Permissions and Permission Overrides fields to ensure you have performed the elimination of any default permissions added by third-party plugins that your specific game does not actually require.