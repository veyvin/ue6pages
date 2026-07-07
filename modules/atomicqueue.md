---
layout: default
title: AtomicQueue
---

<!-- ai-generation-failed -->

<h1>AtomicQueue</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/AtomicQueue/AtomicQueue.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

w-level, high-performance C++ utility providing lock-free, thread-safe queue implementations. It is primarily used for high-concurrency scenarios where multiple threads need to exchange data (such as tasks, events, or telemetry) without the heavy performance penalty of traditional mutex-based locking.

At its core, it provides the TAtomicQueue template, which leverages atomic primitives to manage head and tail pointers. This ensures that data can be enqueued and dequeued across different threads (like the Game Thread and a Render or Task thread) with minimal contention.

C++ Usage Example

To use TAtomicQueue, you generally define it within a class that manages cross-thread communication.

C++
	#include "Containers/AtomicQueue.h"

	#include "Async/Async.h"

	 

	// Define a simple data structure to pass

	struct FGameEvent { int32 ID; FString Name; };

	 

	class FEventManager

	{

	    // A thread-safe queue for events

	    TAtomicQueue<FGameEvent> PendingEvents;

	 

	public:

	    void SendEvent(int32 ID, FString Name)

	    {

	        // Enqueue from any thread

	        PendingEvents.Enqueue({ID, Name});

	    }

	 

	    void ProcessEvents()

	    {

	        FGameEvent Event;

	        // Dequeue until empty - typically called on the Game Thread

	        while (PendingEvents.Dequeue(Event))

	        {

	            UE_LOG(LogTemp, Log, TEXT("Processing Event: %d - %s"), Event.ID, *Event.Name);

	        }

	    }

	};

	```

	 

	---

	 

	### Practical Usage Tips & Best Practices

	 

	#### 1. Prefer for High-Frequency Logic

	Use `TAtomicQueue` over `TQueue` with `EQueueMode::Mpsc` (Multi-Producer Single-Consumer) when performance is critical. While `TQueue` is versatile, `TAtomicQueue` is specifically optimized for lock-free operations and is generally faster for high-frequency "fire-and-forget" data passing.

	 

	#### 2. Mind the Memory Alignment

	Lock-free structures are highly susceptible to **false sharing** (where different threads modify data on the same CPU cache line). Ensure your data structures are padded or aligned using `alignas(64)` (or the engine's `CACHE_LINE_SIZE` macro) if you notice performance degradation during high-contention scenarios.

	 

	#### 3. Single-Consumer Pattern is Safest

	While the queue supports multiple producers, it is most efficient and easiest to manage with a **single consumer**. Design your system so that only one dedicated "Worker" or "Manager" thread is responsible for calling `Dequeue`, which eliminates the risk of complex race conditions during data processing.

	 

	#### 4. Avoid Heavy Data Structures

	The queue stores copies of the data passed to it. To keep the lock-free operations fast, pass **pointers**, **handles**, or **small structs** (like IDs) rather than large, complex objects like `TArray` or long `FString` instances. This minimizes the time spent in the critical atomic section.

	 

	#### 5. Check for Emptiness Before Processing

	If you are polling the queue (e.g., every frame in `Tick`), use `IsEmpty()` before starting a `while(Dequeue)` loop. This can prevent unnecessary atomic operations if no data has been produced since the last check, saving valuable CPU cycles.

	 

	#### 6. Not a Replacement for Task System

	Do not use `TAtomicQueue` to build your own complex task scheduler. Unreal's **Task System** (`UE::Tasks`) is already built on top of these low-level primitives and handles dependency tracking, priority, and thread-pool management much more effectively than a manual queue implementation.

	 

	#### 7. Module Dependency Setup

	`TAtomicQueue` is part of the `Core` module. You do not need to add a specialized module to your `Build.cs` beyond the defaults, but you must include the specific header:

	```cpp

	#include "Containers/AtomicQueue.h"

	```

	 

	#### 8. Beware of the ABA Problem

	When using low-level lock-free containers, be aware of the "ABA Problem" (where a location is read, changed, and changed back, making it appear as if nothing happened). While `TAtomicQueue` handles the internal pointers safely, if you are passing raw pointers to objects, ensure those objects are not deleted and re-allocated between a `Dequeue` attempt and its completion. Use `TSharedPtr` or unique IDs to be safe.
Copy code
Practical Usage Tips & Best Practices
1. Prefer for High-Frequency Logic

Use TAtomicQueue over TQueue with EQueueMode::Mpsc (Multi-Producer Single-Consumer) when performance is critical. While TQueue is versatile, TAtomicQueue is specifically optimized for lock-free operations and is generally faster for high-frequency “fire-and-forget” data passing.

2. Mind the Memory Alignment

Lock-free structures are highly susceptible to false sharing (where different threads modify data on the same CPU cache line). Ensure your data structures are padded or aligned using alignas(64) (or the engine’s CACHE_LINE_SIZE macro) if you notice performance degradation during high-contention scenarios.

3. Single-Consumer Pattern is Safest

While the queue supports multiple producers, it is most efficient and easiest to manage with a single consumer. Design your system so that only one dedicated “Worker” or “Manager” thread is responsible for calling Dequeue, which eliminates the risk of complex race conditions during data processing.

4. Avoid Heavy Data Structures

The queue stores copies of the data passed to it. To keep the lock-free operations fast, pass pointers, handles, or small structs (like IDs) rather than large, complex objects like TArray or long FString instances. This minimizes the time spent in the critical atomic section.

5. Check for Emptiness Before Processing

If you are polling the queue (e.g., every frame in Tick), use IsEmpty() before starting a while(Dequeue) loop. This can prevent unnecessary atomic operations if no data has been produced since the last check, saving valuable CPU cycles.

6. Not a Replacement for Task System

Do not use TAtomicQueue to build your own complex task scheduler. Unreal’s Task System (UE::Tasks) is already built on top of these low-level primitives and handles dependency tracking, priority, and thread-pool management much more effectively than a manual queue implementation.

7. Module Dependency Setup

TAtomicQueue is part of the Core module. You do not need to add a specialized module to your Build.cs beyond the defaults, but you must include the specific header:

C++
#include "Containers/AtomicQueue.h"
Copy code
8. Beware of the ABA Problem

When using low-level lock-free containers, be aware of the “ABA Problem” (where a location is read, changed, and changed back, making it appear as if nothing happened). While TAtomicQueue handles the internal pointers safely, if you are passing raw pointers to objects, ensure those objects are not deleted and re-allocated between a Dequeue attempt and its completion. This prevents the elimination of data integrity.