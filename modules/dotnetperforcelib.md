---
layout: default
title: DotNetPerforceLib
---

<!-- ai-generation-failed -->

<h1>DotNetPerforceLib</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Shared/EpicGames.Perforce.Native/DotNetPerforceLib.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">OpenSSL</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Engine source tree designed to provide high-performance, managed access to Perforce (P4) version control. It serves as the primary interface for Unreal Engine’s .NET-based tools—such as UnrealBuildTool (UBT), AutomationTool (UAT), and the Horde CI/CD system—allowing them to communicate efficiently with Perforce servers.

Unlike standard command-line wrappers, this library often utilizes a bundled native C++ Perforce API to perform operations like syncing, submitting, and workspace management. This architecture is designed to eliminate the overhead of spawning multiple p4.exe processes during complex build and automation tasks.

Practical Usage Tips and Best Practices
Utilize Native Client Support
When configuring automation scripts or Horde agents, enable the preferNativeClient option within the library’s settings. This allows the system to use the precompiled C++ Perforce library, which helps eliminate performance bottlenecks often found when relying on external shell execution of the P4 client.
Implement Managed Workspaces
In high-concurrency environments like build farms, use the “Managed Workspace” feature. This allows the library to track local file states (CAS) and “eliminate” redundant file transfers when switching between different streams or branches, significantly reducing sync times and server load.
Configure Parallel Sync Threads
For large-scale projects, adjust the numParallelSyncThreads property. By increasing the number of concurrent threads used for fetching files, you can eliminate idle CPU time during the sync phase of a build, though you should balance this against your Perforce server’s maximum connection limits.
Leverage the Have Table for Speed
When performing repeated syncs on a stable build machine, ensure useHaveTable is set to true. This allows the library to query the server-side “have” list rather than scanning the entire local disk, helping to eliminate unnecessary file system I/O during workspace validation.
Use Partitioned Workspaces
If your automation generates massive amounts of metadata, configure the library to use Partitioned Workspaces. This practice helps eliminate journal bloat on your Perforce server, which can otherwise lead to performance degradation across the entire studio as the CI system scales.
Wrap Connection Logic in Try/Catch
Perforce operations are prone to network timeouts or authentication failures. Always wrap calls to Connect() and SyncAsync() in robust error-handling blocks to eliminate “zombie” build processes that hang indefinitely when the Perforce server is unreachable.
Optimize Path Handling for Long Paths
When working on Windows, ensure the library is configured to handle long file paths (over 260 characters). This is critical for deep Unreal project hierarchies; failing to do so can lead to sync errors that you must eliminate by enabling LongPaths support in both the OS and the Perforce client settings.
Monitor Connection Health
Use the library’s health-check capabilities to poll the Perforce server status before initiating large operations. By verifying server availability and latency upfront, you can eliminate failed build jobs early in the pipeline, saving time and compute resources.