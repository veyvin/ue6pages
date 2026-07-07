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

real Engine that interfaces with the Zen Storage (ZenServer) ecosystem to manage and inspect build-related data.

Description and Purpose

This module provides the logic and command-line interface (CLI) tools for interacting with the Zen Store, Epic’s high-performance content-addressable storage system. While the engine handles much of this automatically during cooking, the BuildStorageTool allows for manual inspection, verification, and manipulation of cooked output data and Derived Data Cache (DDC) stored within Zen. Its primary purpose is to streamline the staging and deployment process by managing the “ue.projectstore” references and ensuring that build artifacts are correctly addressed, deduplicated, and prepared for distribution to target platforms.

Practical Usage Tips and Best Practices
Manage Data Deduplication
Since ZenServer uses content-addressable storage, this tool helps you leverage deduplication across multiple projects or workspaces. Use it to verify that identical assets are only stored once, which can significantly eliminate redundant disk usage on your build machine or local server.
Audit “ue.projectstore” Files
ZenServer tracks data references via ue.projectstore files. Use the BuildStorageTool to ensure these markers are valid. If a project store file is deleted or older than 14 days, Zen’s garbage collection may eliminate the associated cooked data to recoup space; this tool helps you manage those lifecycles.
Bypass Filesystem Bottlenecks
Traditional cooking to loose files on a hard drive is often limited by OS file-handle overhead. By utilizing the Zen Store through this module’s integration, you can eliminate the performance cost of thousands of tiny file writes, resulting in much faster local “cook-on-the-fly” iterations.
Inspect Zen Metadata
When debugging why a build isn’t deploying correctly to a console or mobile device, use the BuildStorageTool (often via the Zen Dashboard utility command prompt) to query metadata. This allows you to verify if specific chunks or blobs of data are present in the local storage before they are sent to the target.
Streamline Staging to Containers
The tool is instrumental in the transition between cooking and staging. It ensures that the transition from Zen’s internal format to .pak, .utoc, and .ucas container files is seamless, allowing for faster deployment to non-shipping build configurations (Debug/Development).
Prepare Assets for Elimination Testing
When running stress tests that involve frequent asset reloading—such as a sequence testing many different elimination VFX and sound assets—ensure your Zen store is fully populated. This tool helps pre-cache these assets in the Zen DDC, preventing frame-rate hitches caused by “on-demand” asset compilation during the test.
Optimize for Shared DDC
In team environments, use this tool to manage the connection between your local Zen storage and a Shared DDC (Unreal Cloud DDC). This ensures that if a teammate has already built a specific set of textures or shaders, your local machine can download the blob directly, eliminating the need for local re-computation.
Manual Garbage Collection
If your local disk is filling up with old build artifacts, you can use the BuildStorageTool commands to trigger or configure the ZenServer garbage collection. This allows you to manually eliminate unreferenced blobs that are no longer needed for any active project workspaces.