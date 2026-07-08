---
layout: default
title: libWebSockets
---

<!-- ai-generation-failed -->

<h1>libWebSockets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/libWebSockets/libWebSockets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li><li><span class="label">依赖</span><span class="value">OpenSSL</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

libwebsockets C library. It provides the core networking logic for real-time, bidirectional communication between an Unreal Engine client/server and an external WebSocket server.

While higher-level plugins like Remote Control and Pixel Streaming use this under the hood, the module itself is used by developers to build custom integrations—such as real-time chat systems, live telemetry feeds, or connectivity with cloud-based game backends (e.g., Node.js or Go servers). It handles the complexities of the WebSocket handshake, framing, and SSL/TLS encryption, helping you eliminate the need to write raw socket-level boilerplate.

Practical Usage Tips and Best Practices
Add Module Dependencies Correctly
To use this in your C++ code, you must include the WebSockets module (which wraps libwebsockets) in your Build.cs file. This ensures the linker can find the necessary headers and static libraries.
C++
	    PublicDependencyModuleNames.AddRange(new string[] { "WebSockets", "Json", "JsonUtilities" });

	    ```

	 

	*   **Utilize the FWebSocketsModule Singleton**  

	    Always access the system through `FWebSocketsModule::Get()`. Use this to call `CreateWebSocket(Url, Protocol)`, which returns a `TSharedPtr<IWebSocket>`. Storing this as a shared pointer helps you **eliminate** memory leaks and ensures the connection's lifecycle is managed automatically.

	 

	*   **Handle Callbacks on the Game Thread**  

	    WebSocket events (like `OnMessage` or `OnConnected`) are asynchronous. However, Unreal’s implementation typically dispatches these back to the **Game Thread**. Avoid performing heavy computational work or blocking calls inside these delegates, as it will cause the game to hitch.

	 

	*   **Validate SSL/TLS for Production**  

	    For secure connections (`wss://`), the module uses the engine's built-in SSL implementation (OpenSSL). Ensure your server certificates are valid; if you use self-signed certificates for testing, you may need to adjust the `BaseEngine.ini` settings to **eliminate** "Certificate Verification Failed" errors.

	 

	*   **Manage the Connection Lifecycle in Actors**  

	    If an Actor owns a WebSocket, ensure you call `Socket->Close()` and unbind all delegates in `EndPlay` or `BeginDestroy`. Failing to unbind delegates can lead to crashes where the socket attempts to call a function on an Actor that has already been garbage collected.

	 

	*   **Check Connection Status Before Sending**  

	    Before calling `Socket->Send()`, always check `Socket->IsConnected()`. Sending data over a dead or connecting socket is a common source of "Silent Failure" bugs. Implementing a simple "Outbox" or "Retry" queue can help you **eliminate** data loss during brief network flickers.

	 

	*   **Optimize Data Paybags with JSON**  

	    Since WebSockets are stream-based, combine the `WebSockets` module with the `Json` module. Using `FJsonSerializer` to pack your data into strings before sending allows you to **eliminate** the difficulty of manual bit-packing and makes your network traffic human-readable for debugging.

	 

	*   **Monitor Performance with 'stat Net'**  

	    Use the console command `stat Net` to monitor general networking overhead. While this module is highly efficient, sending thousands of small messages per second can increase CPU usage. Batching your data into fewer, larger packets can help you **eliminate** unnecessary network driver overhead.
Copy code
Utilize the FWebSocketsModule Singleton
Always access the system through FWebSocketsModule::Get(). Use this to call CreateWebSocket(Url, Protocol), which returns a TSharedPtr<IWebSocket>. Storing this as a shared pointer helps you eliminate memory leaks and ensures the connection’s lifecycle is managed automatically.
Handle Callbacks on the Game Thread
WebSocket events (like OnMessage or OnConnected) are asynchronous. However, Unreal’s implementation typically dispatches these back to the Game Thread. Avoid performing heavy computational work or blocking calls inside these delegates, as it will cause the game to hitch.
Validate SSL/TLS for Production
For secure connections (wss://), the module uses the engine’s built-in SSL implementation (OpenSSL). Ensure your server certificates are valid; if you use self-signed certificates for testing, you may need to adjust the BaseEngine.ini settings to eliminate “Certificate Verification Failed” errors.
Manage the Connection Lifecycle in Actors
If an Actor owns a WebSocket, ensure you call Socket->Close() and unbind all delegates in EndPlay or BeginDestroy. Failing to unbind delegates can lead to crashes where the socket attempts to call a function on an Actor that has already been garbage collected.
Check Connection Status Before Sending
Before calling Socket->Send(), always check Socket->IsConnected(). Sending data over a dead or connecting socket is a common source of “Silent Failure” bugs. Implementing a simple “Outbox” or “Retry” queue can help you eliminate data loss during brief network flickers.
Optimize Data Paybags with JSON
Since WebSockets are stream-based, combine the WebSockets module with the Json module. Using FJsonSerializer to pack your data into strings before sending allows you to eliminate the difficulty of manual bit-packing and makes your network traffic human-readable for debugging.
Monitor Performance with ‘stat Net’
Use the console command stat Net to monitor general networking overhead. While this module is highly efficient, sending thousands of small messages per second can increase CPU usage. Batching your data into fewer, larger packets can help you eliminate unnecessary network driver overhead.