---
layout: default
title: AndroidPlatformEditor
---


<h1>AndroidPlatformEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Android/AndroidPlatformEditor/AndroidPlatformEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AndroidDeviceDetection, AndroidRuntimeSettings, AudioSettingsEditor, Core, CoreUObject, DesktopPlatform, DesktopWidgets, EditorWidgets, Engine, InputCore, MainFrame, MaterialShaderQualitySettings, MaterialShaderQualitySettingsEditor, PropertyEditor, RHI, RenderCore, ShaderPlatformConfigEditor, SharedSettingsWidgets, Slate, SlateCore, SourceControl</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

user interface and logic behind Android-specific project settings in Unreal Engine. It provides the “Platforms > Android” settings panel, handles the validation of Android SDK/NDK paths, and manages the integration of Turnkey for automated toolchain installation.

It is primarily used by developers to configure APK packaging, manifest requirements, distribution signing (keystores), and Google Play Services integration without manually editing XML or Gradle files.

1. Module Configuration

Because this module is part of the Unreal Editor’s platform support, you generally do not need to link it to your game’s runtime module. However, if you are writing custom editor tools or automation scripts that modify Android settings via C++, you must include it in your Editor module’s dependencies:

C#
	// MyProjectEditor.Build.cs

	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { 

	        "AndroidPlatformEditor",

	        "Settings"

	    });

	}
Copy code
2. Practical Usage Tips & Best Practices
Leverage Turnkey for SDK Management

Starting with recent versions of UE5, use the “Platforms > SDK Management > Android > Install SDK” option provided by this module. This uses Turnkey to automatically download and configure the exact versions of the SDK, NDK, and JDK required for your specific engine release, “eliminating” the common version-mismatch errors found in manual setups.

Configure Project-Specific Overrides

If you work on multiple projects requiring different API levels, avoid setting global environment variables (like ANDROID_HOME). Instead, use the Project SDK Override section in the Android settings. The AndroidPlatformEditor saves these directly to your project’s DefaultEngine.ini, ensuring that building one project doesn’t break the environment for another.

Use Manifest Additions for Custom Permissions

Instead of modifying the engine’s base Java/XML templates, use the Advanced APK Packaging section. You can add extra tags to the <manifest>, <application>, or <activity> sections directly in the editor.

Best Practice: Use the ManifestRequirementsAdditions.txt file located in Build/Android/ for complex permission sets to keep the Editor UI clean.
Standardize the Android Package Name

The AndroidPlatformEditor requires a specific format (com.Company.Project). Ensure this is set early. Changing this late in development can cause “elimination” of saved game data on devices, as the Android OS treats a different package name as a completely different application.

Optimize Storage with App Bundles (AAB)

Inside the Android settings, always enable Generate Bundle (AAB) for distribution. This allows Google Play to serve optimized APKs to users based on their device’s specific architecture and screen density, significantly reducing the initial download size.

Manage Distribution Signing Securely

The module provides fields for Keystore files and aliases.

Tip: Store your .keystore file in the Build/Android/ folder. This allows the editor to find it relatively, making it easier for team members to share the project via source control without manually re-linking the signing files.
Handle Screen Orientation and Notch Support

Use the Resolution and Window Management settings to define how your game handles display cutouts (notches). If your UI is being “eliminated” or cut off by a camera hole-punch, ensure “Render in cutout area” is toggled correctly and that you are using UMG Safe Zones.

Validate with the “Configure Now” Button

If you see a red bar in the Android settings stating “Project is not configured for the Android platform,” click the Configure Now button. This triggers the AndroidPlatformEditor to generate the necessary Gradle wrapper files and folder structures in your project directory required for successful packaging.