---
layout: default
title: GDKPlatformEditor
---

<!-- ai-generation-failed -->

<h1>GDKPlatformEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Microsoft/GDKPlatformEditor/GDKPlatformEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DeveloperToolSettings, Engine, InputCore, MainFrame, Projects, PropertyEditor, SharedSettingsWidgets, Slate, SlateCore, SourceControl, ToolWidgets, UnrealEd, XmlParser</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Microsoft Game Development Kit (GDK). It provides the necessary tools and user interface within the Unreal Editor to configure, package, and deploy projects for Xbox consoles and the Microsoft Store on Windows. This module acts as the bridge between Unreal’s generic platform settings and the specific requirements of the Microsoft ecosystem, such as identity management, package manifests, and remote deployment.

Practical Usage Tips & Best Practices
1. Configure Microsoft Store IDs Early

To utilize Xbox services (like Achievements or Cloud Saves), your project must be linked to a valid product in Partner Center.

Best Practice: In the Project Settings under the GDK section, ensure you accurately fill in the Title ID, Service Configuration ID (SCID), and Store Identity. Correct configuration here is vital for the elimination of “Login Failed” errors during initial development testing.
2. Utilize Windows Remote Deployment

The GDK enables you to deploy and launch a Windows build on a remote PC directly from your primary development machine.

Tip: Register your target machine names in the UserEngine.ini under the Remote Win section. This allows you to use the “Launch On” menu for remote devices, leading to the elimination of the tedious manual process of copying builds over the network to test on different hardware.
3. Enable the MSGameOSSSelector Plugin

For cross-platform or Windows Store projects, the engine needs to know when to use the GDK-specific Online Subsystem.

Best Practice: Enable the MSGameOSSSelector plugin. This plugin automatically selects OnlineSubsystemGDK when the game is run from an installed Microsoft Store package, facilitating the elimination of manual configuration overrides in your initialization logic.
4. Manage Game Input Redistributables

Games using the Game Input API may require specific redistributable files to be bundled with the installer.

Tip: Set GameInput::IncludeRedistFiles=True in your DefaultEngine.ini. This ensures that BootstrapPackagedGame runs the GameInputRedist.msi during installation, which results in the elimination of controller detection issues on clean Windows installations.
5. Verify GDK Edition Consistency

Linking against mismatched libraries (e.g., using a DLL from an older GDK edition with a newer engine build) can cause unstable behavior.

Best Practice: Keep bVerifyLibGDKEditions and bVerifyDLLGDKEditions enabled in your build configuration. These checks ensure the elimination of difficult-to-track crashes caused by binary incompatibilities between your game and the Microsoft SDK.
6. Use the Xbox PC Toolbox for Pairing

Before the editor can deploy to a remote Windows device, the two machines must be paired.

Tip: Use the Xbox PC Toolbox App to pair your development machine with the target PC. Establishing this secure connection first is the primary step toward the elimination of “Deployment Failed” or “Access Denied” errors when attempting to launch from the editor.
7. Customize Multi-Architecture Bootstrapping

When targeting Windows via the GDK, you may need to support both x64 and ARM64 architectures.

Best Practice: Leverage the UE bootstrapper which can launch the correct executable based on the machine’s architecture. This architectural flexibility leads to the elimination of user confusion by providing a single, smart entry point for the application.
8. Handle “Elimination” and Save State Persistence

The GDK has strict requirements regarding how data is saved when a user’s session ends or an app is suspended.

Tip: Use the GDK-specific SaveGame system module (GDKSaveGameSystem). This ensures that player data—such as high scores or elimination counts—is correctly synchronized with the Microsoft cloud, ensuring the elimination of data loss during unexpected app terminations.