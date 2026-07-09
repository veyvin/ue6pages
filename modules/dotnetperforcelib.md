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

used in the Editor, this library is optimized for “headless” automation and build-farm operations. It “eliminates” the overhead of the standard command-line interface by using structured data parsing (tagged output) to interact with the depot programmatically.

Practical Usage Tips and Best Practices
Access via AutomationTool Context
When writing a BuildCommand in UAT, do not manually instantiate a connection if you can avoid it. Use the built-in P4 property. This “eliminates” the need to manage server addresses and credentials manually, as UAT handles the connection lifecycle for you.
Leverage Async/Await for High Throughput
The library is built on modern C# asynchronous patterns. Always use the Async variants of commands (e.g., SyncAsync, SubmitAsync). This “eliminates” thread blocking during long-running network operations, which is essential for maintaining performance on build agents.
Use Environment Variables for Configuration
The library natively recognizes uebp_ prefixed environment variables (like uebp_PORT and uebp_CLIENT). Setting these on your build machines “eliminates” the risk of hard-coding sensitive credentials in your C# automation scripts.
Dispose of Connections Properly
If you do create a manual IPerforceConnection, always wrap it in a using statement. Failing to dispose of the connection can “eliminate” your server’s available connection slots, leading to “Max Connections Reached” errors that can stall an entire studio’s build pipeline.
Handle Structured Records
Instead of parsing raw string output, work with the library’s Record types (like FStatRecord). This “eliminates” fragile regex-based parsing and ensures your scripts correctly handle complex metadata, such as file attributes and move/add states.
Implement Robust Exception Handling
Perforce operations frequently fail due to network blips or locked files. Always wrap your logic in try-catch blocks specifically looking for PerforceException. This allows your script to “eliminate” the chance of a silent failure and instead provide a clean error log for the build team.
Respect P4IGNORE via Command Flags
When adding files programmatically, ensure you are passing the flags that respect .p4ignore files. This “eliminates” the accidental submission of local Intermediate or Saved folders into the depot, which can clutter the stream for other developers.
Use Connection Pooling for Heavy Tasks
For complex operations involving thousands of small queries, consider using a single persistent connection rather than opening and closing a session for every file. This “eliminates” the “connection storm” overhead that can slow down both the client and the Perforce server.