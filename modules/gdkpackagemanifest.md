---
layout: default
title: GDKPackageManifest
---

<!-- ai-generation-failed -->

<h1>GDKPackageManifest</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Microsoft/GDKPackageManifest/GDKPackageManifest.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, GRDK, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ploying games to Xbox consoles and the Microsoft Store on Windows.

This module acts as a translator, taking engine-side data—such as project icons, identity strings, and capability declarations—and formatting them into the specific XML schema required by the Microsoft GDK. This automation is essential for the elimination of manual XML errors that would otherwise lead to deployment failures or store rejection.

Practical Usage Tips and Best Practices
1. Synchronize Identity with Partner Center

Ensure the Package Identity Name and Publisher ID in your Project Settings match exactly what is provided in the Microsoft Partner Center. The GDKPackageManifest module uses these strings to generate the manifest’s identity block; a mismatch will cause an immediate elimination of your ability to upload or test the build on retail hardware.

2. Declare Capabilities for Network Features

If your game uses multiplayer, voice chat, or cloud saves, you must declare these capabilities in the GDK settings. The module will then inject the correct <Capability> tags into the manifest. Failing to do this leads to the elimination of network functionality once the game is running in a retail-like environment.

3. Manage Localized Strings Carefully

The GDK manifest requires specific handling for localized “Display Names.” Use the module’s support for resource files (.resw) rather than hard-coding names into the XML. This practice facilitates the elimination of certification issues when submitting your game to multiple global regions.

4. Audit Resource Constraints for Xbox

The manifest defines how much memory and CPU resources the OS allocates to your game. Use the module’s settings to ensure your “Title” and “System” memory pools are correctly defined for your target Xbox hardware (e.g., Series X vs. Series S), aiding in the elimination of “Out of Memory” crashes during the boot sequence.

5. Verify Icon and Splash Screen Paths

The GDKPackageManifest expects specific dimensions for branding assets (like the 44x44 or 150x150 logos). If the module cannot find these files at the specified paths in your Build/GDK folder, the manifest generation will fail. Validating these assets early leads to the elimination of packaging bottlenecks.

6. Use the Manifest for Protocol Handling

If your game supports “Deep Linking” (e.g., launching directly into a friend’s lobby from a web link), you must register the URI protocol in the GDK settings. The module will handle the complex XML registration, which is a best practice for the elimination of friction in the player’s join-flow.

7. Leverage for “Smart Delivery” Configuration

When building for both Xbox One and Xbox Series X|S, the manifest must correctly identify the hardware-specific features. The module helps manage the TargetDeviceFamily settings, ensuring the elimination of incorrect binary deployment when players download your game on different console generations.

8. Validate with the Windows App Certification Kit (WAC)

After the module generates your package, always run the WAC test as a final validation step. This tool checks the manifest for common errors that the GDKPackageManifest module might not catch (such as invalid publisher strings). This process ensures the elimination of potential submission delays.