---
layout: default
title: ExternalRpcRegistry
---

<!-- ai-generation-failed -->

<h1>ExternalRpcRegistry</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/ExternalRPCRegistry/ExternalRpcRegistry.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, HTTP, HTTPServer, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

real Engine that acts as a central authority for registering and exposing engine functions to external processes. It is a critical component of the Remote Control (RC) and Virtual Production ecosystems, providing a structured way for the engine to tell external tools (like web dashboards, Python scripts, or custom C++ apps) which functions are available to be called remotely via RPC (Remote Procedure Call).

Unlike standard Blueprint-to-Blueprint communication, this module focuses on the “registration” phase—ensuring that external requests are validated and mapped to the correct internal UFunction or C++ logic, facilitating the elimination of manual “glue code” between Unreal and external hardware or software.

Practical Usage Tips and Best Practices
1. Use as the Foundation for Custom Control Panels

If you are building a custom web UI to control lighting or cameras on a film set, use this module to register specific actor functions. This allows your web app to “discover” available commands, leading to the elimination of hard-coded endpoint errors in your external application.

2. Implement Validation via Metadata

When registering functions through the RPC registry, use UFUNCTION metadata (like Category or custom tags) to filter which functions are exposed. This is a best practice for the elimination of security risks, ensuring that sensitive or performance-heavy functions are not accessible to the external network.

3. Leverage for Multi-User Editing Workflows

The ExternalRpcRegistry is often utilized in Multi-User sessions to synchronize actions across different instances of the editor. By registering specific events, you can ensure that an action taken on one machine is replicated to others via an RPC call, aiding in the elimination of desync between team members.

4. Monitor Registration via the Remote Control API

This module works in tandem with the RemoteControl plugin. You can query the registry via HTTP to get a list of all currently registered functions. This dynamic discovery is essential for the elimination of outdated documentation, as the registry always represents the live state of the engine.

5. Handle Threading with “Main Thread” Guarding

Most functions called through the ExternalRpcRegistry will eventually interact with UObjects. Since external calls arrive on network threads, ensure your implementation uses AsyncTask(ENamedThreads::GameThread, ...) to execute the logic. This prevents crashes and assists in the elimination of race conditions.

6. Register Temporary Functions for Live Events

For live broadcast scenarios, you can programmatically add or remove functions from the registry during runtime. This allows you to expose specific “one-time” triggers for a show, facilitating the elimination of cluttered interfaces once a specific event or scene has concluded.

7. Combine with JSON Serialization

Data passed through the ExternalRpcRegistry is typically serialized into JSON. Ensure your C++ structs are marked with USTRUCT() and use types that serialize cleanly (like float, int32, and FString). This preparation leads to the elimination of data corruption during the external-to-internal transfer.

8. Verify Module Dependencies in Build.cs

To use the registry in your own C++ systems, you must add "ExternalRpcRegistry" and "RemoteControl" to your PrivateDependencyModuleNames in your Build.cs. Correct dependency management is the primary step for the elimination of “Unresolved External Symbol” errors during compilation.