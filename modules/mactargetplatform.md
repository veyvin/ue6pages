---
layout: default
title: MacTargetPlatform
---

<!-- ai-generation-failed -->

<h1>MacTargetPlatform</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Mac/MacTargetPlatform/MacTargetPlatform.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, DesktopPlatform, MacTargetPlatformControls, MacTargetPlatformSettings, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

build and packaging system. It contains the platform-specific logic required to identify, configure, and compile Unreal Engine projects for macOS.

What it is and What it’s used for

Located in Engine/Source/Developer/MacTargetPlatform, this module is utilized by the Unreal Build Tool (UBT) and the Unreal Automation Tool (UAT) to define the macOS environment. It handles everything from SDK version detection to the generation of specialized application bundles (.app).

Primary uses include:

Target Detection: Identifying the macOS version, CPU architecture (Intel vs. Apple Silicon), and available Metal features.
Packaging Logic: Defining how assets are staged into the macOS application bundle and managing the creation of the Info.plist and entitlements files.
Modern Xcode Integration: Implementing the settings for the “Modern Xcode” workflow, which streamlines code signing and provisioning for Apple platforms.
Architectural Configuration: Managing “Universal Binaries” to ensure games can run natively on both x86_64 and arm64 hardware.
Practical Usage Tips and Best Practices
1. Enable the Modern Xcode Workflow

In UE 5.3+, it is a best practice to enable the modern workflow via BaseEngine.ini under [/Script/MacTargetPlatform.XcodeProjectSettings]. Set bUseModernXcode=true. This allows for the elimination of complex manual code signing processes by leveraging Xcode’s automatic provisioning.

2. Target Universal Binaries for Steam/EGS

When preparing a shipping build for digital stores, use the -specifiedarchitecture=arm64+x86_64 argument in your UAT commands. This ensures the elimination of performance issues for users on older Intel Macs while providing native speed for Apple Silicon users within a single package.

3. Manage Metal Shader Versions

Within the MacTargetPlatform settings (Project Settings > Platforms > macOS), specify the “Metal Language Version.” Keeping this up to date is essential for the elimination of rendering artifacts when using modern features like Lumen or Nanite (which requires Metal 3.0+).

4. Monitor VMA Limits for Large Projects

MacOS has strict limits on Virtual Memory Areas (VMA). If your project crashes with “Out of Memory” on a machine with plenty of RAM, it may be due to VMA fragmentation. Tuning the allocator or reducing the number of unique loaded assets can help in the elimination of these stability issues.

5. Verify SDK and Xcode Compatibility

Always check the MacOS Development Requirements documentation for your specific engine version. For example, UE 5.6 requires Xcode 15.2+. Ensuring your tools match the engine’s requirements leads to the elimination of “Platform not supported” errors during the compilation phase.

6. Utilize Remote Mac Building

If your primary development is on Windows, the MacTargetPlatform module supports “Remote Building” via SSH. Ensure your Windows machine has the correct SSH keys and the Mac has “Remote Login” enabled. This workflow allows for the elimination of the need to constantly switch seats between PC and Mac.

7. Strategic Elimination of Unnecessary Architectures

For internal testing or iteration, don’t build Universal Binaries. Select only your current machine’s architecture (e.g., arm64) in the Project Launcher. This results in the elimination of redundant compilation time, significantly speeding up your iteration loop.

8. Notarize Builds Early

Apple requires all macOS apps to be notarized to run without security warnings. The MacTargetPlatform settings allow you to input your Apple Developer credentials. Automating this in your build pipeline ensures the elimination of “Developer cannot be verified” errors for your playtesters.