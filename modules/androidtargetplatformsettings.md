---
layout: default
title: AndroidTargetPlatformSettings
---

<!-- ai-generation-failed -->

<h1>AndroidTargetPlatformSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Android/AndroidTargetPlatformSettings/AndroidTargetPlatformSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DesktopPlatform, Engine, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

at provides the underlying infrastructure for managing Android-specific project settings. It acts as the interface between the Unreal Engine Editor and the configuration data used to package, deploy, and optimize games for the Android ecosystem.

It primarily handles the logic for the Project Settings > Android and Android SDK panels, ensuring that values like APK packaging rules, permissions, and hardware architecture support are correctly serialized into the project’s configuration files (e.g., DefaultEngine.ini).

Practical Usage Tips and Best Practices
Scoping to Editor Builds Because this module is part of the Target Platform system used by the cook and package process, it must never be included in a runtime build. Always wrap its dependency in your Build.cs to avoid the “elimination” of your build during the packaging phase.
C++
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AndroidTargetPlatformSettings");

	}
Copy code
Validate SDK and NDK Paths via C++ If you are building a custom pipeline tool or a “Project Check” utility, you can access the UAndroidRuntimeSettings class (supported by this module) to programmatically verify if the developer has the correct NDK version or SDK API level installed before attempting a build.
Automation via Command Line Many settings handled by this module can be overridden via the command line during automated builds. For example, you can bypass the UI and “eliminate” manual configuration steps by passing parameters like -set:KeyStorePassword=YourPass when running the Unreal Automation Tool (UAT).
Manage Architecture Support Use the settings provided by this module to toggle between arm64-v8a and x86_64. For modern production builds, it is a best practice to disable older 32-bit architectures to reduce the final APK/AAB size and “eliminate” unnecessary compilation time.
Utilize Config Rules System This module supports the Config Rules system. By placing a configrules.txt in your Build/Android directory, you can define logic that overrides settings at runtime based on the specific device hardware (e.g., reducing texture quality if the device has less than 4GB of RAM).
UPL (Unreal Plugin Language) Integration While this module manages the high-level settings, specific XML modifications to the AndroidManifest.xml should be handled via UPL. The settings module provides the “Extra Settings” text boxes that UPL scripts often query to determine which permissions to inject.
Optimize Multi-User Development Since these settings are stored in DefaultEngine.ini, ensure your version control (Perforce/Git) does not “eliminate” or ignore this file. However, individual local paths to the Android SDK should be kept in BaseEditorPerProjectUserSettings.ini to avoid conflicting with other team members’ local install paths.
Performance Profiling Setup Within the settings managed by this module, ensure “Support Backbuffer Sampling” is configured correctly for your target GPU. Disabling unnecessary rendering features here is the most effective way to “eliminate” GPU bottlenecks on low-end Android mobile devices.