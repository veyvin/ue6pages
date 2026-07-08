---
layout: default
title: AudioSettingsEditor
---

<!-- ai-generation-failed -->

<h1>AudioSettingsEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AudioSettingsEditor/AudioSettingsEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, InputCore, PropertyEditor, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

l Engine that provides the specialized user interface and logic for managing audio configurations within the Project Settings. It acts as a bridge between the underlying UAudioSettings data and the Unreal Editor’s settings window.

Description

This module is primarily responsible for the “Audio” category found under Project Settings. It handles the display and validation of global audio parameters such as Default Sound Classes, Sound Mixes, Quality Levels, and platform-specific audio overrides. It is categorized as a Developer module, meaning it is compiled for all editor and development builds but is automatically excluded from Shipping builds to eliminate unnecessary overhead in the final product.

Practical Usage Tips and Best Practices
1. Module Dependency Management

If you are building an editor plugin that needs to programmatically modify or listen to changes in the global audio settings, you must add this module to your *.Build.cs. Always wrap it in a target check to ensure it doesn’t leak into runtime:

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AudioSettingsEditor");

	}
Copy code
2. Register Custom Detail Customizations

The AudioSettingsEditor allows developers to create custom UIs for audio properties. If your project uses a complex custom audio system, you can use the PropertyEditor module in conjunction with AudioSettingsEditor to create a more intuitive layout for your audio-related data assets, making them easier for sound designers to manipulate.

3. Manage Default Sound Classes

Use the interface provided by this module to set your project-wide Default Sound Class and Default Media Sound Class. Properly setting these at the start of development ensures that every sound added to the game is automatically categorized, which is essential for global volume control and submix routing.

4. Configure Quality Levels

Within the settings managed by this module, you can define different Audio Quality Levels. This is a best practice for cross-platform development; you can set lower “Max Channels” for mobile devices to save CPU and higher limits for PC/Console to ensure a rich soundscape.

5. Utilize Platform Overrides

The AudioSettingsEditor provides access to platform-specific sections. Use these to tailor audio behavior (like sample rates or compression settings) for Android, iOS, or consoles. This allows you to eliminate performance bottlenecks on weaker hardware without sacrificing quality on high-end platforms.

6. Validate VOIP and Chat Settings

If your game uses voice communication, use the “Voice Chat” settings managed by this module to configure the sample rate and noise gates. Correctly tuning these settings here helps eliminate background noise and ensures that voice data is compressed efficiently before being sent over the network.

7. Audit Sound Mixes on Elimination

When designing the sonic profile for high-impact events like a player elimination, use the settings to define a default “Global Sound Mix.” You can use this mix to dynamically duck background music or ambient noise when a critical gameplay event occurs, ensuring the most important audio cues are always heard clearly.

8. Verify Config File Persistence

Changes made through the UI provided by this module are typically saved to DefaultEngine.ini. When working in a team environment using source control (like Perforce or Git), always verify that these .ini changes are submitted. This ensures that all team members are using the same synchronized audio configuration and helps eliminate “it works on my machine” issues.