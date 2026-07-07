---
layout: default
title: Perforce
---

<!-- ai-generation-failed -->

<h1>Perforce</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Perforce/Perforce.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li><li><span class="label">依赖</span><span class="value">SSL</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

tes Epic’s preferred version control system, Perforce (P4), directly into the Unreal Editor and engine toolsets.

Description and Purpose

This module implements the ISourceControlProvider interface, allowing the engine to communicate with a Perforce server using the P4 C++ API. Its primary purpose is to manage the “Read-Only” status of assets, handle file checkouts, and manage changelists without requiring the user to leave the Unreal Editor. By utilizing this module, teams can eliminate file conflicts through “Exclusive Checkouts,” ensuring that only one person can modify a binary asset (like a Blueprint or Map) at a time, which is critical for collaborative game development.

Practical Usage Tips and Best Practices
Configure via P4CONFIG Files
Instead of manually entering credentials in the editor, create a .p4config file in your project root. Setting the workspace and server here is a best practice to eliminate login errors for new team members, as the module will automatically detect the settings upon opening the project.
Enforce Exclusive Checkouts for Binary Assets
Because Blueprints and Levels cannot be merged like text files, ensure your Perforce Typemap is configured with the +l (exclusive lock) flag for .uasset and .umap files. This helps you eliminate “lost work” scenarios where two developers modify the same file and one person’s changes are overwritten.
Use Shallow Workspace Paths
Windows has a 260-character path limit. Map your Perforce workspace to a shallow directory (e.g., D:\P4\ProjectName). This helps the module eliminate “Path Too Long” errors when trying to sync or check out deeply nested assets within the Content browser.
Enable “Perform Revision Control Operations Implicitly”
In the Editor Preferences under Source Control, enable implicit operations. This allows the engine to automatically check out an asset the moment you modify it, helping you eliminate the friction of manually right-clicking and selecting “Check Out” for every small change.
Sync via Unreal Game Sync (UGS)
While the Perforce module handles editor-side checkouts, use Unreal Game Sync for getting the latest engine and project updates. UGS is designed to work alongside the Perforce module to eliminate “dirty” local builds by automatically syncing and building the latest binaries for the team.
Submit via the “Submit Content” Dialog
Use the built-in submit window to add descriptive changelist notes and link to Jira tasks. This ensures that every elimination of a bug or addition of a feature is documented in the file history, which is essential for tracking down when a specific issue was introduced.
Monitor Connection via the Source Control Icon
The color-coded icon in the bottom-right of the editor indicates your connection status. A red icon means the connection is lost; clicking it to “Reconnect” is the fastest way to eliminate “File is Read-Only” warnings that prevent you from saving your work.
Optimize Performance with Workspace Filtering
If your depot is massive, use “Workspace Mappings” to only sync the parts of the project you need. By reducing the number of files the module has to track, you eliminate lag in the Content Browser when the engine performs its periodic status checks against the server.