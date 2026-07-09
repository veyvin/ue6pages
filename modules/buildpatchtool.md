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

ngine/Binaries/DotNET/BuildPatchTool) used to process build data for the BuildPatchServices system. It is the backbone of Unreal’s custom patching pipeline, responsible for taking a compiled game build and “chunking” it into small, reusable data blocks.

The tool generates Manifests (.manifest files) that describe the build structure and Chunks that contain the actual file data. This system allows installers to download only the specific data blocks that have changed between versions, effectively “eliminating” the need for users to redownload the entire game for small updates.

Practical Usage Tips and Best Practices
Implement Chunk Deduplication
The tool automatically identifies identical data across different files. By using a consistent -CloudDir (the destination for your chunks) across multiple builds, the tool will “eliminate” redundant data by only uploading new or modified chunks. This significantly reduces storage costs on your CDN.
Optimize Chunk Size for CDNs
You can control the target size of data chunks using the -ChunkSize parameter. A best practice is to find a balance; chunks that are too small increase the number of HTTP requests, while chunks that are too large “eliminate” the granularity of the patch, forcing users to download more data than necessary.
Use File Spanning for Large Files
For massive assets like 4K texture paks, enable file spanning. This allows the BuildPatchTool to break a single large file into multiple chunks. If only a small portion of that texture changes, the user only downloads the affected chunks, “eliminating” the 1GB+ download for a minor visual fix.
Automate via CI/CD Pipelines
Integrate the BuildPatchTool into your build server (e.g., Jenkins or GitHub Actions). Use the -BuildRoot parameter to point to your finished packaged build and -ManifestStream to output the results. This “eliminates” manual errors and ensures every internal playtest build is ready for delta-patching.
Maintain Manifest History
Always keep a library of previous .manifest files. When generating a new patch, the tool uses these manifests to calculate the “delta” or difference between versions. This is the only way to “eliminate” unnecessary data transfer for players moving from Version A to Version B.
Verify Build Integrity with -AppValidate
Use the tool’s validation mode to check existing cloud directories. This command scans your chunks and manifests for corruption or missing files, helping you “eliminate” broken installers before they reach the end user.
Utilize Custom Fields for Metadata
The tool allows you to inject custom strings into the manifest via command-line arguments. Use this to tag builds with “Elimination” event IDs, branch names, or build numbers, which can then be read by your in-game ChunkDownloader to verify version compatibility.
Separate Executables from Content
When possible, organize your build so that the frequently changing .exe or .pdb files are in a different folder than the static high-resolution assets. This helps the BuildPatchTool “eliminate” the churn of content chunks when only a code change has occurred.