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

t development for the Xbox ecosystem and the Windows Store. It handles platform-specific project settings, packaging configurations, and deployment workflows required for Microsoft platforms. Its primary role is to expose the GDK-specific metadata (such as Identity names and Title IDs) and to facilitate the “Launch On” functionality for remote Xbox consoles or Windows PC targets. By centralizing these configurations, it allows developers to manage Microsoft Store certification requirements and platform-specific hardware settings directly within the editor.

Practical Usage Tips and Best Practices
Configure Project Identity for Certification
Use the GDK settings within the Project Settings menu to define your Title ID, Service Configuration ID (SCID), and Identity Name. Ensuring these match your Microsoft Partner Center configuration exactly will eliminate authentication failures when testing Xbox Services like achievements or leaderboards.
Manage Remote Deployment Targets
The module enables the “Launch On” menu for GDK devices. Use the Xbox PC Toolbox to pair your development PC with remote Xbox consoles. Once paired, they will appear in the editor, allowing you to eliminate the time spent manually moving builds via external drives or network shares.
Optimize Packaging for the Microsoft Store
When preparing a final build, use the GDK-specific packaging settings to include the necessary MicrosoftGame.config file. This module ensures the file is correctly generated and validated, which helps you eliminate rejection during the initial Microsoft Store ingestion process.
Configure the Online Subsystem (OSS) Selector
In UE 5.6 and later, use the MSGameOSSSelector plugin settings managed by this module. This allows the game to automatically select OnlineSubsystemGDK when running from an installed package, helping you eliminate manual configuration errors when switching between Steam, Epic, and Microsoft platforms.
Utilize Architecture-Specific INI Files
The GDK platform supports architecture-specific configurations. You can place settings in /Config/Windows/MSGameOSS/ to target specific GDK behaviors. This modular approach helps you eliminate clutter in your main DefaultEngine.ini while maintaining platform-specific overrides for saving systems or networking.
Toggle GDK-Specific Rendering Features
Use the GDK platform settings to enable or disable platform-specific rendering paths, such as DirectX 12 Agility SDK features. Fine-tuning these settings for the target hardware allows you to eliminate GPU performance bottlenecks specific to the Xbox Series S or X architectures.
Verify Game Input Redistribution
If your project uses the “Game Input for Windows” plugin, ensure the “IncludeRedistFiles” option is enabled in the GDK platform settings. This ensures the installer for the Game Input redistributable is included in your package, which will eliminate potential controller detection issues for end users.
Debug via Xbox PC Remote Tools
Leverage the remote deployment and launching support provided by this module. By using the -deploy and -device flags in your build scripts (UAT), you can automate the process of testing an elimination sequence or gameplay loop on a target device directly from your development environment.