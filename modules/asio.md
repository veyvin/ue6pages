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

ersion of the Asio C++ library (often associated with Boost, though Unreal uses the non-Boost version). It provides a consistent, high-performance asynchronous I/O model for networking and low-level concurrency. In Unreal, it is primarily utilized as the networking backbone for specialized plugins like WebRTC, Pixel Streaming, and certain OpenXR implementations that require low-latency data streaming.

Practical Usage Tips & Best Practices
1. Add as a Private Dependency

Since Asio is a low-level third-party library, it should almost always be added as a Private dependency in your Build.cs file. This prevents its headers from being force-included into other modules that might not need them, reducing compilation times and potential naming conflicts.

C#
	// MyProject.Build.cs

	PrivateDependencyModuleNames.AddRange(new string[] { "Asio" });
Copy code
2. Use Third-Party Include Macros

Asio heavily utilizes standard C++ features and preprocessor logic that can conflict with Unreal’s strict warning-as-error build settings (especially regarding shadowed variables or non-standard extensions). Always wrap Asio includes with the following macros:

C++
	#include "CoreMinimal.h"

	 

	THIRD_PARTY_INCLUDES_START

	#include "asio.hpp"

	THIRD_PARTY_INCLUDES_END
Copy code
3. Wrap Windows Headers for Platform Interop

Asio frequently includes Windows.h on PC platforms. To prevent “macro redefinition” errors (a common conflict between Windows and Unreal), you must surround your Asio includes with Unreal’s platform type guards.

C++
	#include "Windows/AllowWindowsPlatformTypes.h"

	THIRD_PARTY_INCLUDES_START

	#include "asio.hpp"

	THIRD_PARTY_INCLUDES_END

	#include "Windows/HideWindowsPlatformTypes.h"
Copy code
4. Manage io_context Lifetimes Carefully

The asio::io_context is the heart of any Asio-based system. In Unreal, you should never run an io_context directly on the Game Thread, as io_context::run() is a blocking call. Instead, initialize it within a dedicated FRunnable thread or a background task.

5. Integrate with Unreal’s Task System

While Asio has its own internal threading model, for better engine-wide performance, you should try to bridge Asio completion handlers with Unreal’s Tasks System or GThreadPool. This ensures that when an I/O operation completes, the subsequent gameplay logic is executed on a thread that Unreal is already managing.

6. Prohibit UObject Interaction in Async Handlers

Asio completion handlers (lambdas or functions) run on background threads. It is unsafe to modify UObject properties or call Blueprint functions directly from an Asio thread. If an Asio operation results in a gameplay event—such as the elimination of a network-controlled entity—you must use AsyncTask(ENamedThreads::GameThread, ...) to pipe that result back to the main thread.

7. Avoid Mixing with FSocket

Do not try to use asio::ip::tcp::socket and Unreal’s FSocket on the same underlying file descriptor. While both are wrappers for Berkeley sockets, they maintain different internal states. Use Asio exclusively for high-throughput, asynchronous streaming (like video or raw binary data) and FSocket or UNetDriver for standard game state replication.

8. Graceful Elimination of Async Operations

When your Actor or Component is destroyed (EndPlay), you must properly stop the io_context and cancel pending asynchronous operations. Failure to call io_context::stop() and join the background thread will lead to a crash when an Asio completion handler attempts to access memory that has undergone elimination.