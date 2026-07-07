---
layout: default
title: SlateUGS
---

<!-- ai-generation-failed -->

<h1>SlateUGS</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/SlateUGS/SlateUGS.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AppFramework, ApplicationCore, Core, DesktopPlatform, PakFile, Projects, Slate, SlateCore, StandaloneRenderer, ToolWidgets, UGSCore, UnixCommonStartup</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e Sync (UGS) functionality and metadata directly into the Unreal Editor interface.

Description and Purpose

While the main Unreal Game Sync application runs as a standalone Windows program to manage Perforce syncing and precompiled binaries, the SlateUGS module allows the editor to communicate with the UGS ecosystem. It provides Slate widgets and status bars (such as SSugsBar) that display the current sync state, build health, and “badges” from the Metadata Service within the editor. Its primary purpose is to keep developers informed about the project’s health without requiring them to alt-tab to the standalone client. By surfacing build failures or “good” changelists, it helps teams eliminate the risk of working on a broken version of the project.

Practical Usage Tips and Best Practices
Enable via the “UGS” Plugin
The module is typically part of the Unreal Game Sync developer plugin. Ensure this plugin is enabled in your .uproject to see the UGS status bar in the bottom right of the editor. This is a best practice to eliminate confusion among team members regarding whether they are on the “latest” stable build.
Configure the Metadata API URL
For the module to display build badges (e.g., “Editor Build Success”), you must provide the correct ApiUrl in your UnrealGameSync.ini. Setting this correctly allows the editor to pull real-time data from your Horde or UGS Metadata Server, helping you eliminate “silent” build breaks.
Monitor Build Badges for Stability
The SlateUGS UI displays colored badges for different build targets. Before performing a critical task like a map bake or a large content check-in, check these badges. If a badge is red, it indicates a failure in the CI/CD pipeline, allowing you to eliminate unnecessary work on a compromised branch.
Utilize the “Sync to this” Shortcut
The module provides a UI context to sync to specific changelists. If you encounter a bug, you can use the UGS-integrated menus to quickly roll back. This helps eliminate the manual effort of finding changelists in the Perforce P4V client.
Leverage Precompiled Binaries (PCBs)
One of the core strengths of the UGS system is supporting PCBs for artists. The SlateUGS module notifies the user when a new set of binaries is available for their current sync. Using this feature helps eliminate the need for non-engineers to compile the engine locally, saving hours of iteration time.
Identify Locked Files
Through its Perforce integration, the module can surface lock icons on assets. This provides a visual cue within the editor that another user has a file checked out, helping to eliminate merge conflicts before they occur.
Customize the Status Panel Color
You can set a StatusPanelColor in the UnrealGameSync.ini for different branches (e.g., Red for Main, Blue for Dev). The SlateUGS widgets will reflect this color in the editor, providing an instant visual confirmation of which stream the developer is currently in to eliminate accidental check-ins to the wrong branch.
Debug via the “UGS” Console Command
If the status bar is not updating, you can use UGS-specific console commands to refresh the metadata. This helps you eliminate synchronization lag between the standalone UGS client and the Unreal Editor’s internal Slate display.