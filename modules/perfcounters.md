---
layout: default
title: PerfCounters
---

<!-- ai-generation-failed -->

<h1>PerfCounters</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/PerfCounters/PerfCounters.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, HTTPServer, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

monitoring utility primarily used for dedicated servers and headless engine instances. It allows the engine to expose real-time performance metrics (CPU usage, memory, frame time) and custom game-specific data through a built-in HTTP server.

This module is the backbone of live-service monitoring, allowing external tools (such as Prometheus or Grafana) to query the state of a running server via a JSON endpoint. By providing a remote “heartbeat” and command interface, it facilitates the elimination of “black box” server behavior, enabling developers to diagnose performance regressions or crashes in a live environment without needing a debugger attached.

Practical Usage Tips and Best Practices
1. Enable via Command Line and Macros

To use the module, your build must be compiled with the WITH_PERFCOUNTERS=1 macro (typically enabled in Server and Development configurations). At runtime, you must specify a port using the -statsPort=NNNNN command-line argument. This setup leads to the elimination of port conflicts on multi-tenant server hardware.

2. Monitor Game-Specific Metrics

Beyond engine stats, use the IPerfCounters interface to track game logic, such as ActiveAIPlayerCount or CurrentMatchState. Registering these leads to the elimination of guesswork during load testing, as you can correlate game state changes directly with CPU/memory spikes in your telemetry dashboard.

3. Implement Remote Executive Commands

Bind a delegate to OnPerfCounterExecCommand to allow authorized remote users to trigger console commands via HTTP (e.g., curl http://IP:Port/exec?c=gc). This facilitates the elimination of the need for a persistent SSH or RCON connection to perform basic maintenance or diagnostic tasks on a running instance.

4. Secure the Stats Port

The PerfCounters HTTP listener is unauthenticated by default. You must ensure your server’s firewall restricts access to this port to trusted internal IP ranges. Implementing strict network rules leads to the elimination of security risks where malicious actors could query server metrics or execute remote commands.

5. Use JSON for Automated Alerts

The module serves data in JSON format at the root / endpoint. Configure your monitoring stack to poll this endpoint and trigger alerts if specific values (like FrameTime) exceed a threshold. This proactive monitoring assists in the elimination of “silent” performance degradation before it impacts the player experience.

6. Start the HTTP Listener Explicitly

In some engine versions, you may need to call FHttpServerModule::Get().StartAllListeners() after initializing your counters to begin serving data. Verifying the listener status in your logs leads to the elimination of “Connection Refused” errors when your external monitoring tools attempt to scrape the server.

7. Avoid High-Frequency Updates

While it’s tempting to update counters every tick, doing so for dozens of values can add unnecessary overhead to the game thread. Updating counters at a fixed interval (e.g., once per second) leads to the elimination of performance noise, ensuring the telemetry system itself does not become a bottleneck.

8. Conditionally Load the Module

Since PerfCounters is often unnecessary for client builds, wrap your module loading and counter logic in #if WITH_PERFCOUNTERS blocks. This practice leads to the elimination of unnecessary memory footprint and module dependencies in your final distribution.