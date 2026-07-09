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

bridging the Unreal Editor’s Source Control API with the Helix Core (P4) versioning system. It implements the ISourceControlProvider interface, allowing the engine to perform file operations like checking out assets, submitting changelists, and resolving conflicts directly from the Content Browser.

Since Epic Games uses Perforce internally, this module is the most robust and feature-complete version control integration available in the engine, supporting advanced workflows like Unreal Game Sync (UGS) and Streams.

Practical Usage Tips & Best Practices
1. Configure a Proper Typemap

Before adding assets to the depot, you must set up a server-side Typemap to ensure binary files are handled correctly.

Best Practice: Ensure .uasset and .umap files are set to binary+l (exclusive checkout). This ensures the elimination of merge conflicts in binary files, as only one developer can modify an asset at a time.
2. Use Shallow Workspace Paths

Windows has a 260-character file path limit. Unreal projects often have deep folder hierarchies (e.g., Content/Environment/Industrial/Assets/Textures/...).

Tip: Map your Perforce workspace to a very shallow root, such as D:/P4/ProjectName/. This leads to the elimination of “Path Too Long” errors that can prevent the engine from saving or loading deeply nested assets.
3. Leverage P4CONFIG Files

A .p4config file is a text file placed in your project root that stores your P4PORT, P4USER, and P4CLIENT settings.

Best Practice: Create a .p4config file and point the environment variable to it. This facilitates the elimination of connection prompts within the Unreal Editor, as the module will automatically detect and use the local connection settings.
4. Optimize NTFS Performance

Large Perforce workspaces involve frequent file reads and metadata updates which can be slowed down by default OS settings.

Tip: Disable the NTFS “Last Accessed” timestamp by running fsutil behavior set disablelastaccess 3 as an administrator. This results in the elimination of unnecessary disk I/O overhead during massive workspace syncs.
5. Exclude Temporary Directories

Not every file in an Unreal project should be in the depot. Including temporary files will bloat your server and slow down your team.

Best Practice: Use a .p4ignore file to exclude Saved/, Intermediate/, DerivedDataCache/, and .vs/ folders. This ensures the elimination of redundant file uploads and keeps the depot focused only on source data.
6. Utilize Unreal Game Sync (UGS)

For teams working with the engine source code, UGS is a specialized front-end that uses the Perforce module to synchronize and build the project.

Tip: Use UGS to sync to specific “Good” changelists marked by your build machine. This results in the elimination of broken builds for the rest of the team by ensuring everyone stays on a verified stable version of the code and assets.
7. Handle .ini Checkouts Correctly

Many project settings are stored in .ini files. If these are not checked out, changes made in the Project Settings menu will be lost.

Best Practice: When the editor prompts you to “Make Writable” or “Check Out” a config file, always choose Check Out. This proactive management leads to the elimination of configuration drift where settings only exist on one developer’s machine.
8. Monitor Connection with “Stat SourceControl”

If the editor becomes sluggish when right-clicking assets, the Perforce module may be struggling with network latency.

Tip: Use the console command stat SourceControl to see the timing of server requests. Identifying slow server responses facilitates the elimination of editor “hitching” by allowing you to address network issues or optimize your P4 workspace settings.