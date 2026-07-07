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

c Games to provide a high-performance, robust bridge between C# applications and the Perforce Helix Core version control system. Unlike the standard P4.NET components, this library is specifically optimized for Unreal Engine’s massive scale, handling the unique requirements of syncing and managing hundreds of gigabytes of game data.

It is a core dependency for the Unreal Build Tool (UBT), Unreal Automation Tool (UAT), Horde, and UnrealGameSync (UGS). It allows these C# tools to perform operations like syncing files, submitting changelists, and querying server metadata programmatically.

Practical Usage Tips and Best Practices
1. Leverage the ‘uebp_’ Environment Variables

The library is designed to work seamlessly with Unreal’s build environment variables.

Best Practice: When writing custom C# automation, use variables like uebp_PORT, uebp_USER, and uebp_CLIENT. This allows your scripts to automatically inherit the correct connection settings from the active session or build machine, eliminating the need to hard-code sensitive credentials.
2. Utilize Managed Workspaces in Horde

One of the most powerful features of this library is its role in Managed Workspaces.

Tip: If you are building tools for a CI/CD pipeline, use the library’s managed workspace logic. It allows a single agent to quickly “re-seat” a workspace to a different stream, eliminating the massive time and disk space overhead of creating a brand-new workspace for every build.
3. Implement Parallel Sync for Large Projects

The library provides advanced support for numParallelSyncThreads to maximize network throughput.

Action: When performing a sync via C#, configure the library to use multiple threads (typically 8 to 16). This helps you eliminate network bottlenecks, drastically reducing the time it takes to get an engine or project workspace ready for compilation.
4. Use ‘fstat’ for Efficient Metadata Queries

Iterating through thousands of files to check their status can be extremely slow if done incorrectly.

Tip: Use the library’s fstat wrapper to query batches of files at once. This allows you to retrieve the “Have” status, “Action” state, and local file paths in a single server request, eliminating the latency caused by per-file server pings.
5. Handle Tagged Output for Parsing

The library interacts with the Perforce CLI using “tagged” output mode (-Ztag).

Best Practice: Always process the dictionary-based result sets provided by the library rather than trying to parse raw string output. This structured approach helps you eliminate parsing errors that occur when Perforce changes its console output formatting.
6. Clean Up with ‘RevertInternalAsync’

Automated build processes often leave behind opened or modified files if they fail halfway through.

Action: Always include a cleanup step using RevertInternalAsync (or its equivalent in your implementation) in a finally block. This ensures that the build machine’s workspace is returned to a clean state, eliminating “Clash” or “File already opened” errors in subsequent build runs.
7. Prefer the Native Client for Speed

The library supports both the standard p4.exe and a bundled native library for interaction.

Tip: Set preferNativeClient=true in your configuration. The native library integration avoids the overhead of spawning a new process for every single Perforce command, eliminating thousands of small process-startup delays during complex automation tasks.
8. Use ‘DoNotUpdateHaveList’ for Read-Only Builds

In some CI scenarios, you might want to fetch files without letting the server know the client has them.

Action: Use the SyncOptions.DoNotUpdateHaveList flag. This allows you to sync data for a “throwaway” build without bloating the Perforce server’s “Have” table, which helps eliminate unnecessary database growth on the Perforce server.