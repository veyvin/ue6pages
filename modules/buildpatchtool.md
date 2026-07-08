---
layout: default
title: BuildPatchTool
---

<!-- ai-generation-failed -->

<h1>BuildPatchTool</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/BuildPatchTool/BuildPatchTool.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, AutomationController, AutomationWorker, BuildPatchServices, BuildSettings, Core, CoreUObject, GoogleTest, HTTP, Messaging, Networking, Projects</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

-line utility provided by Epic Games. It is the primary engine-side mechanism for generating Chunk-based patches for distribution. Unlike traditional binary patching that compares two full builds, the BuildPatchTool decomposes a game’s file structure into small, reusable “chunks” and generates a Manifest file (.manifest) that describes how to reconstruct the build.

It is primarily used by the Epic Games Store (EGS) pipeline and custom game launchers to provide highly efficient delta updates, allowing players to download only the specific data blocks that have changed between versions.

Practical Usage Tips and Best Practices
Define Optimal Chunk Sizes
Use the -ChunkSize parameter to balance download efficiency and disk overhead. A best practice is to use 1MB to 8MB chunks. Smaller chunks allow for finer-grained updates (less wasted download), while larger chunks improve disk I/O performance during the patching process.
Implement Cloud Storage Integration
The tool can automatically upload generated chunks and manifests to cloud providers like Amazon S3. Use the -CloudDir argument to point to your staging bucket. To eliminate manual upload steps, integrate this into your CI/CD pipeline immediately after the “Cook” and “Stage” steps.
Always Verify Manifests
Before pushing an update live, use the -Mode=Verify command. This ensures that the generated manifest correctly represents the source files and that no chunks were corrupted during generation. This is a critical step to eliminate broken installations for your players.
Use Compact Binary Manifests
For large games, text-based manifests can become quite large. Use the -Compactify flag to generate a binary manifest. This reduces the metadata size that the client must download before the patch begins, which helps eliminate startup latency for your game launcher.
Leverage Custom Attributes for File Logic
You can use the -FileAttributes parameter to tag specific files (e.g., “Required,” “Optional,” or “HighPriority”). This allows your custom launcher to eliminate the need to download high-resolution texture chunks if the player has selected “Low Quality” settings in the launcher options.
Prune Legacy Chunks Regularly
Over many updates, your cloud storage will accumulate “orphaned” chunks that are no longer referenced by the latest manifest. Periodically run the tool with the -Mode=Compact or a custom cleanup script to eliminate these obsolete files and reduce your cloud storage costs.
Optimize for Shared Data (Deduplication)
The BuildPatchTool is excellent at deduplication. If multiple files share identical data blocks, it will only create one chunk for that data. To maximize this, eliminate non-deterministic data in your build (like timestamps inside compiled binaries) so that the chunk signatures remain identical across builds.
Use BuildPatchServices for Custom Launchers
If you are building your own C++ launcher, do not try to parse the manifest manually. Instead, include the BuildPatchServices module in your launcher’s Build.cs. This module is designed to consume the output of the BuildPatchTool, providing a robust API for downloading and installing patches while helping to eliminate implementation errors.