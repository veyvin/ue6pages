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

ty to upload, download, and validate blobs and “refs” within a storage backend. The BuildStorageTool is essential for workflows involving Unreal Zen Server (local/shared caching) and Horde (Epic’s build health and artifact management system), allowing developers to move large amounts of binary data—such as precompiled binaries, cooked assets, or shader maps—efficiently using content-defined chunking and deduplication.

Practical Usage Tips and Best Practices
1. Use for CI/CD Artifact Distribution

Integrate the BuildStorageTool into your build pipeline to upload successful build artifacts (like PCBS or cooked data) to a Horde server. This allows other developers to pull down the “latest successful build” using Unreal Game Sync (UGS) without having to compile the entire project locally, significantly reducing setup time for non-engineers.

2. Leverage Content Addressing (CAS)

The tool utilizes Content Addressable Storage, meaning it identifies data by its hash rather than its filename. This is a best practice for eliminating redundant data; if two different builds share 90% of the same binary data, the BuildStorageTool will only store and transmit the unique 10%, saving massive amounts of disk space and bandwidth.

3. Patching via Unsync

The BuildStorageTool is often used in conjunction with the Unsync utility. Instead of downloading a fresh 100GB build, the tool identifies the delta between your local version and the server version. It then only downloads the missing chunks, allowing you to update your workspace to a new version in a fraction of the time.

4. Manage Zen Store Caches

Use this tool to inspect and manage your local Zen Store (the high-performance storage service used by the Zen Loader). If your local DDC becomes bloated or corrupted, you can use the tool’s commands to prune old artifacts or validate the integrity of the stored blobs to eliminate visual artifacts or crashes caused by bad cached data.

5. Verify Build Integrity with Aliases

The tool allows you to assign “Aliases” (weak references) to specific blobs. Use aliases to tag builds with metadata like #stable or #milestone. This allows automation scripts to always pull the most reliable artifacts by querying the alias rather than a specific, hardcoded hash.

6. Debugging Connection Issues

If you encounter errors like BlobNotFound or authentication failures, run the tool with verbose logging enabled. The module communicates over HTTP/S with the Horde or Zen backend; ensuring your firewall allows traffic on the Zen default ports (e.g., 8540) is a common fix to eliminate connectivity bottlenecks.

7. Handle Automated Cleanup

Artifacts stored via this module can grow exponentially. Set up expiration policies (Strong Refs) within the tool’s configuration to automatically eliminate old, unused build artifacts after a set period (e.g., 14 days). This prevents your storage backend from running out of space, which would otherwise stall the entire studio’s build pipeline.

8. Optimize Shader Map Sharing

Shader compilation is one of the biggest time-sinks in Unreal. By using the BuildStorageTool to push shader maps to a shared cloud DDC, you ensure that once one machine has compiled a shader, every other machine in the studio can simply download the result. This eliminates the “compiring shaders” progress bar for the rest of the team.