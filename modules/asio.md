---
layout: default
title: Asio
---

<!-- ai-generation-failed -->

<h1>Asio</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/asio/Asio.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, OpenSSL</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

igned for asynchronous network and low-level I/O programming. Unlike Unreal’s high-level SocketSubsystem, Asio provides a robust, proactor-pattern framework for handling thousands of concurrent connections with high efficiency.

Description

In Unreal Engine, Asio is located in Engine/Source/ThirdParty/Asio. It is not a reflected UObject module; rather, it is a low-level toolset used primarily by internal plugins like Pixel Streaming, WebRTC, and OpenColorIO to manage non-blocking communication. It is the go-to choice when you need to implement custom network protocols (e.g., raw TCP/UDP, Serial ports, or specialized WebSockets) that must perform outside the constraints of the game thread.

Practical Usage Tips and Best Practices
1. Link as an External Dependency

To use Asio in your C++ project, you must add it to your module’s *.Build.cs file using the specialized third-party macro. Do not add it to PublicDependencyModuleNames, as it lacks a ModuleRules setup for standard linking.

C#
	// In YourProject.Build.cs

	AddEngineThirdPartyPrivateStaticDependencies(Target, "Asio");

	 

	// Asio is header-only, but sometimes needs this for compatibility

	PublicDefinitions.Add("ASIO_STANDALONE");

	PublicDefinitions.Add("ASIO_NO_EXCEPTIONS");

	```

	 

	#### 2. Run on a Dedicated Thread (`FRunnable`)

	Asio relies on an `asio::io_context::run()` loop, which is a blocking call. **Never call this on the Game Thread**, as it will freeze the engine. Instead, wrap your Asio logic inside an `FRunnable` thread to keep your network processing independent of the frame rate.

	 

	#### 3. Bridge to Game Thread via TaskGraph

	When an Asio callback receives data, you likely need to update a game actor or UI. Since Asio runs on a background thread, you must dispatch these updates back to the Game Thread using `AsyncTask` to avoid race conditions:

	```cpp

	// Inside an Asio callback (Background Thread)

	AsyncTask(ENamedThreads::GameThread, [Data]()

	{

	    // Safely update Unreal Actors or UI here

	    MyActor->ProcessNetworkData(Data);

	});

	```

	 

	#### 4. Handle Shutdown and Elimination Gracefully

	If you don't stop the `io_context` properly, your background thread may hang during shutdown, leading to a "ghost" process or a crash when the module is unloaded. Ensure you call `io_context.stop()` and join your `FRunnable` thread inside `BeginDestroy` or `EndPlay`:

	```cpp

	void FMyNetworkWorker::Stop()

	{

	    IOContext.stop(); // Signals the Asio loop to terminate

	}

	```

	 

	#### 5. Use `TSharedPtr` for Session Management

	Asio’s asynchronous handlers require that the objects they operate on stay alive until the callback completes. Use `TSharedPtr` and `TSharedFromThis` for your connection classes. This ensures that even if a player is **eliminated** or the connection object is marked for deletion, the memory remains valid until the pending I/O operation finishes.

	 

	#### 6. Opt-out of C++ Exceptions

	Unreal Engine generally disables C++ exceptions for performance and platform compatibility. Ensure your Asio implementation is configured with `#define ASIO_NO_EXCEPTIONS`. You must then provide a custom `asio::detail::throw_exception` handler or rely on `error_code` parameters in all Asio function calls to handle failures.

	 

	#### 7. Prefer Asio for Non-Game Data

	If you are building standard multiplayer gameplay, stick to Unreal’s **Replication** system. Use Asio only for "side-channel" data, such as:

	*   Integrating with a local specialized hardware peripheral (via Serial/COM).

	*   Connecting to a high-performance telemetry backend.

	*   Building a custom proxy server for large-scale data streaming.

	 

	#### 8. Beware of `std::` Types

	Asio often defaults to using `std::string` or `std::vector`. While functional, you should convert these to `FString` or `TArray` as soon as the data enters Unreal-space to take advantage of the engine's memory tracking and logging tools (`UE_LOG`).
Copy code
2. Run on a Dedicated Thread (FRunnable)

Asio relies on an asio::io_context::run() loop, which is a blocking call. Never call this on the Game Thread, as it will freeze the engine. Instead, wrap your Asio logic inside an FRunnable thread to keep your network processing independent of the frame rate.

3. Bridge to Game Thread via TaskGraph

When an Asio callback receives data, you likely need to update a game actor or UI. Since Asio runs on a background thread, you must dispatch these updates back to the Game Thread using AsyncTask to avoid race conditions:

C++
	// Inside an Asio callback (Background Thread)

	AsyncTask(ENamedThreads::GameThread, [Data]()

	{

	    // Safely update Unreal Actors or UI here

	    MyActor->ProcessNetworkData(Data);

	});
Copy code
4. Handle Shutdown and Elimination Gracefully

If you don’t stop the io_context properly, your background thread may hang during shutdown, leading to a “ghost” process or a crash when the module is unloaded. Ensure you call io_context.stop() and join your FRunnable thread inside BeginDestroy or EndPlay:

C++
	void FMyNetworkWorker::Stop()

	{

	    IOContext.stop(); // Signals the Asio loop to terminate

	}
Copy code
5. Use TSharedPtr for Session Management

Asio’s asynchronous handlers require that the objects they operate on stay alive until the callback completes. Use TSharedPtr and TSharedFromThis for your connection classes. This ensures that even if a player is eliminated or the connection object is marked for deletion, the memory remains valid until the pending I/O operation finishes.

6. Opt-out of C++ Exceptions

Unreal Engine generally disables C++ exceptions for performance and platform compatibility. Ensure your Asio implementation is configured with #define ASIO_NO_EXCEPTIONS. You must then provide a custom asio::detail::throw_exception handler or rely on error_code parameters in all Asio function calls to handle failures.

7. Prefer Asio for Non-Game Data

If you are building standard multiplayer gameplay, stick to Unreal’s Replication system. Use Asio only for “side-channel” data, such as:

Integrating with a local specialized hardware peripheral (via Serial/COM).
Connecting to a high-performance telemetry backend.
Building a custom proxy server for large-scale data streaming.
8. Beware of std:: Types

Asio often defaults to using std::string or std::vector. While functional, you should convert these to FString or TArray as soon as the data enters Unreal-space to take advantage of the engine’s memory tracking and logging tools (UE_LOG).