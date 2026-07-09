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

ly contained within the Core module’s container library. While developers often refer to this functionality as the “atomic queue” pattern, it is implemented through classes like TLockFreePointerList and TQueue with atomic operating modes.

These structures are used for high-performance, thread-safe communication between the Game Thread, Render Thread, and Worker Threads without the overhead of traditional mutexes or critical sections.

Practical Usage Tips and Best Practices
1. Choose the Correct Queue Mode

Unreal’s TQueue can be configured for different thread-safety needs. When using it for multi-threaded communication, always specify EQueueMode::Mpsc (Multiple Producer, Single Consumer) or EQueueMode::Spsc (Single Producer, Single Consumer). Using the correct mode reduces internal contention and maximizes throughput.

2. Avoid Heavy Objects in Atomic Queues

Atomic structures perform best when handling small, trivial data types or pointers. Do not pass large, complex structs by value. Instead, pass a pointer to the data. This ensures that the “atomic” part of the operation remains fast and doesn’t stall the CPU pipeline with large memory copies.

3. Manage Lifetime of Queued Pointers

The queue itself does not manage the memory of the objects it holds. If you push a pointer to a queue, you must ensure that the object is not “eliminated” (deleted) before the consumer thread has a chance to process it. For UObjects, use TWeakObjectPtr or ensure the object is properly referenced elsewhere to prevent garbage collection.

4. Use for Render Command Enqueuing

One of the most common uses for atomic queues is sending data from the Game Thread to the Render Thread. Use these structures to buffer transform updates or state changes that the Render Thread needs to process at the start of its next frame, avoiding expensive locks that would hitch the frame rate.

5. Be Mindful of the ABA Problem

When implementing low-level logic using TLockFreePointerList, be aware of the “ABA problem” (where a node is removed and re-added, making an atomic check pass incorrectly). Unreal’s built-in lock-free structures include internal safeguards, but if you are writing custom atomic logic, use the FSnapshot or versioning patterns provided in the Templates/Atomic.h header.

6. Minimize Consumer Polling

Even though atomic queues are “lock-free,” constant polling (checking IsEmpty() in a tight loop) can waste CPU cycles. Combine your queue with an FEvent or a Task System dependency to wake the consumer thread only when new data is available.

7. Prefer the Tasks System for General Work

If you are using an atomic queue just to fire off background functions, consider using the Tasks System (UE::Tasks::Launch) instead. The Tasks System uses highly optimized atomic queues internally and handles thread affinity and load balancing for you, which is safer and more efficient than manual queue management.

C++ Implementation Example: Thread-Safe Queue

This example demonstrates a basic Multiple Producer, Single Consumer (Mpsc) pattern using TQueue.

C++
	#include "Containers/Queue.h"

	 

	// Definition of a thread-safe message queue

	TQueue<FString, EQueueMode::Mpsc> MessageQueue;

	 

	void AMyActor::SendMessageFromThread(FString Content)

	{

	    // Multiple threads can safely call Enqueue

	    MessageQueue.Enqueue(Content);

	}

	 

	void AMyActor::Tick(float DeltaTime)

	{

	    // Only the Game Thread should consume (Single Consumer)

	    FString OutMessage;

	    while (MessageQueue.Dequeue(OutMessage))

	    {

	        UE_LOG(LogTemp, Log, TEXT("Received Thread Message: %s"), *OutMessage);

	    }

	}
Copy code
Performance & Best Practices
Module Dependency: Ensure your Build.cs includes "Core" (which is standard for all projects).
Cache Contention: Keep your atomic variables and queues aligned to cache lines where possible to avoid “false sharing,” which can occur when two threads modify different variables on the same cache line.
Memory Barriers: Use std::atomic or TAtomic with explicit memory ordering (like MemoryOrder_Release and MemoryOrder_Acquire) only if you have deep experience with memory visibility; otherwise, stick to the high-level TQueue which handles barriers for you.