---
layout: default
title: BuildStorageTool
---

<!-- ai-generation-failed -->

<h1>BuildStorageTool</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/BuildStorageTool/BuildStorageTool.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, ApplicationCore, Core, DesktopPlatform, Json, OutputLog, PakFile, Projects, Slate, SlateCore, Sockets, StandaloneRenderer, StorageServerWidgets, StudioTelemetry, ToolWidgets, UnixCommonStartup, Zen</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Engine’s modern build artifact and distribution systems, specifically Horde and the Zen Storage architecture. Its primary purpose is to manage, upload, and retrieve “build artifacts”—pre-compiled binaries, cooked content, and debug symbols—to a centralized storage solution. This allows teams to share “ready-to-use” versions of the project, significantly reducing the time spent locally compiling code or cooking assets.

Practical Usage Tips & Best Practices
1. Integration with UGS (Unreal Game Sync)

The BuildStorageTool works behind the scenes when using Unreal Game Sync to download Precompiled Binaries (PCBs).

Best Practice: Use this system to allow artists and designers to sync the latest version of the project and jump straight into the Editor without ever opening an IDE or waiting for a local C++ compilation.
2. Leverage for Distributed Cooking

In large-scale projects, cooking assets for multiple platforms (PS5, Xbox, PC) can take hours. This module interfaces with ZenServer, which uses content-addressable storage to de-duplicate data. If one machine has already cooked a specific texture for a platform, the BuildStorageTool ensures other machines can simply pull that artifact rather than re-cooking it.

3. Facilitate Faster Symbol Access

Instead of forcing every developer to download gigabytes of .pdb (symbol) files, the BuildStorageTool can interact with a symbol server or Horde artifact store. This allows a debugger to pull only the specific symbols needed for a crash dump, leading to the elimination of massive, unnecessary downloads.

4. Automated Cleanup via Garbage Collection

Storage for build artifacts can grow exponentially. The module follows Zen Storage rules where data is retained based on the presence of a .projectstore file.

Tip: Be aware that artifacts older than 14 days (default) without a reference may be subject to elimination by the Zenserver garbage collector to reclaim disk space.
5. Use “Unsync” for Delta Patching

The tool logic supports “chunked” data transfers. When updating a build, it only downloads the specific data “chunks” that have changed rather than the entire executable or pak file. This is a best practice for remote workers with limited bandwidth to keep their workspaces up to date efficiently.

6. Optimize CI/CD Build Pipelines

When setting up a build farm (using Horde or Jenkins), use this module to “push” successful builds to a central repository. This ensures that the “Last Known Good” (LKG) build is always available for the QA team to pull instantly for testing, resulting in the elimination of downtime between build completion and test start.

7. Debugging with Zen Dashboard

If you suspect issues with how build artifacts are being stored or retrieved, use the Zen Dashboard (accessible via the Derived Data button in the Editor). This provides a visual interface for the storage metrics managed by this module and allows you to manually trigger storage maintenance commands.

8. Virtual Asset Synchronization

This module is a core part of the Virtual Assets workflow. It handles the movement of “Bulk Data” (the heavy part of an asset) between the local machine and the shared DDC/Build Storage. By only syncing the metadata initially, it allows for the elimination of long sync times in Perforce, only pulling the actual data when the asset is opened in the Editor.