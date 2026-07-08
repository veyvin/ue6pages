---
layout: default
title: IoStoreUtilities
---

<!-- ai-generation-failed -->

<h1>IoStoreUtilities</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/IoStoreUtilities/IoStoreUtilities.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetRegistry, CookMetadata, Core, CoreUObject, DerivedDataCache, DevHttp, DeveloperToolSettings, Json, PakFile, Projects, RHI, RSA, RenderCore, SandboxFile, ShaderRuntime, Sockets, StudioTelemetry, Zen</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ngine packaging pipeline. It provides the essential logic for creating, managing, and validating IoStore containers (.utoc and .ucas files), which are the high-performance successors to the legacy .pak file system.

What it is and What it’s used for

Located in Engine/Source/Developer/IoStoreUtilities, this module contains the backend utilities used by the Unreal Automation Tool (UAT) and the Zen Store to finalize cooked data. Unlike the old system that treated files as individual entries in a flat archive, IoStore uses a “Container” format that is optimized for modern I/O APIs and the engine’s internal Zen Loader.

Primary uses include:

Container Creation: Compiling cooked assets into chunked containers during the “Stage” phase of packaging.
Metadata Generation: Producing the .utoc (Table of Contents) files that store the hash-based mapping and offsets for all assets.
Data Compression: Interfacing with compression providers (like Oodle) to compress container blocks for smaller build sizes.
Validation: Checking the integrity of containers to ensure that all internal asset references and global chunks are correctly resolved.
Practical Usage Tips and Best Practices
1. Combine with Oodle for Maximum Efficiency

IoStore is designed to work in tandem with the Oodle plugin. In your Project Settings > Packaging, ensure “Oodle” is selected as your compression format. The utilities module will then use “Kraken” or “Mermaid” compression to significantly reduce the size of your .ucas files, leading to the elimination of bloated installation footprints.

2. Utilize the -iostore Command Line Argument

When packaging from the command line or a build machine using RunUAT.bat BuildCookRun, always include the -iostore flag. This triggers the IoStoreUtilities to generate the modern container format instead of the legacy .pak files, which is a requirement for projects utilizing Nanite or Virtual Texturing.

3. Monitor the Table of Contents (UTOC) Size

The .utoc file acts as the “index” for your game. If you have hundreds of thousands of tiny assets, this file can become quite large. It is a best practice to use the Asset Audit tool to find and merge small assets or use Data Assets to group information, which helps in the elimination of excessive lookup overhead.

4. Validate Containers via Commandlet

If you suspect a corrupted build or missing assets in a packaged game, you can run the IoStore commandlet to verify your containers. This utility can scan the .ucas data against the .utoc hashes to ensure every block is healthy, leading to the elimination of hard-to-track “Missing Object” crashes in shipping builds.

5. Leverage Global Containers for Shared Data

The module creates a global.utoc which contains shared metadata for the entire project. Ensure this file is never manually deleted or moved during your CI/CD process. Without it, the engine cannot resolve the “Global Script Objects,” leading to the immediate elimination of the game’s ability to boot.

6. Optimize Chunking for Patching

In the Project Settings, you can configure how the IoStoreUtilities chunk your data. By setting a specific “Chunk Size” (e.g., 256MB), you ensure that a small change in one asset doesn’t force a user to redownload the entire game. This strategic chunking leads to the elimination of massive, inefficient patches for your players.

7. Check for Zen Server Compatibility

In UE 5.5, the Zen Server is increasingly used as the cooked output store. Ensure that the IoStoreUtilities are correctly writing to your Zen Data Path. You can verify this by checking that your Saved/Cooked/[Platform] folder contains a ue.projectstore file rather than raw .uasset files, which confirms the modern pipeline is active.

8. Strategic Elimination of Stale Cooked Data

The IoStoreUtilities can sometimes fail to update if the Saved/Cooked folder contains mismatched legacy files. Before a final release build, it is a best practice to perform a total elimination of the Saved/Cooked and Saved/StagedBuilds directories. This forces a clean container generation and prevents “ghost” assets from appearing in your final distribution.