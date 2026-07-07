---
layout: default
title: CmdLink
---

<!-- ai-generation-failed -->

<h1>CmdLink</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/CmdLink/CmdLink.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Projects</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

mands via Named Pipes (on Windows) or similar sockets on other platforms.

This module is most commonly utilized in build automation and external tool integration, such as when UnrealBuildTool (UBT) or the Shader Compile Worker needs to communicate status updates or receive instructions from a parent process without the overhead of a full network stack.

1. Facilitate External Tool Integration

The primary use of CmdLink is to allow external applications to “talk” to a running Unreal process. If you are building a custom launcher or a pipeline tool that needs to trigger actions inside an Editor Utility or a standalone commandlet, CmdLink provides the low-level pipe management to send those string-based commands.

2. Monitor Build and Shader Progress

This module is often active during the compilation of shaders or the execution of build tasks. It handles the communication that allows the Unreal Editor to display progress bars for tasks being performed by background worker processes (like ShaderCompileWorker).

3. Use for Headless Automation

In CI/CD environments where you are running the engine in -nullrhi or -server mode, CmdLink can be used to “inject” commands into the process remotely. This is often more reliable and faster than attempting to use standard input (stdin) redirection, which can be inconsistent across different OS shells.

4. Optimize with Named Pipes

On Windows, CmdLink leverages Named Pipes, which are significantly faster than local loopback sockets for IPC.

Best Practice: When designing tools that need to send high-frequency data to the engine, prefer the pipe implementation provided by CmdLink over local HTTP requests to eliminate network stack latency and firewall interference.
5. Correct Build.cs Dependencies

If you are developing a low-level engine tool or an automation program that requires IPC capabilities, you must manually add the module to your project:

C#
	// In your Tool.Build.cs

	PrivateDependencyModuleNames.Add("CmdLink");
Copy code

Note that this is a Developer module and is typically not included in Shipping builds, so ensure its usage is wrapped in appropriate preprocessor macros.

6. Handle Connection Lifecycles

CmdLink operates on a connection-based model.

Tip: When implementing a listener, always handle “Broken Pipe” or “Disconnected” events. If the parent process (like a build coordinator) crashes, the CmdLink in the child process should detect the loss of the link and shut down gracefully to eliminate “zombie” background processes.
7. Security Considerations

Because CmdLink creates a communication port (pipe) into the engine, it can represent a minor security surface.

Best Practice: Only use CmdLink in trusted development environments. Ensure that the pipe names used by your implementation are unique to your project to prevent other applications on the same machine from accidentally (or maliciously) sending commands to your engine instance.
8. Debugging with Unreal Insights

Since CmdLink is often used for performance-heavy tasks like shader compilation, its activity can be tracked via Unreal Insights.

Tip: If you suspect that IPC overhead is slowing down your build times, look for “CmdLink” or “Pipe” related stalls in the Timing Insights view. This can help you identify if a worker process is waiting too long for a command from the master process.