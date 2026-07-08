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

ne that provides high-performance, lock-free synchronization primitives. It is primarily designed for high-frequency, low-latency communication between different threads, such as the Game Thread and the Rendering Thread.

What it is and What it’s used for

The module contains the implementation for TAtomicQueue, a lock-free, thread-safe queue. Unlike standard containers (like TArray or TQueue) which might require a FCriticalSection (mutex) to prevent data corruption, TAtomicQueue uses atomic operations to manage its internal state.

Primary uses include:

Cross-Thread Message Passing: Sending small commands or pointers from the Game Thread to a background worker or the Render Thread without stalling the CPU.
Task Graph Internals: Powering the low-level scheduling of tasks where locking would cause unacceptable performance hitches.
Producer-Consumer Pipelines: Handling streams of data (like audio buffers or telemetry events) where one thread generates data and another processes it.
Practical Usage Tips and Best Practices
1. Use for High-Contention Scenarios

Prefer TAtomicQueue only when you have multiple threads accessing a queue simultaneously at a high frequency. If your queue is only accessed once per frame, a standard TQueue with a lock is often easier to debug and has negligible performance difference.

2. Adhere to SPSC vs. MPMC Constraints

Understand the specific implementation you are using. Lock-free queues are often optimized for Single-Producer Single-Consumer (SPSC) or Multi-Producer Multi-Consumer (MPMC) patterns. Using an SPSC queue with multiple producers will lead to memory corruption and eliminate thread safety.

3. Keep Data Payloads Small

Lock-free queues work best when storing pointers or small, trivially copyable types (like int32 or float). Avoid pushing large structs or FString objects directly; instead, push a pointer to the data and manage the lifetime of that data separately.

4. Manage Object Lifetimes Carefully

Since the queue is lock-free, there is no inherent “owner” of the objects inside. Ensure that objects pushed onto the queue are not deleted by the producer thread while the consumer is still trying to process them. Using TSharedPtr or a pre-allocated object pool can help manage this safely.

5. Avoid Busy-Waiting

When consuming from an atomic queue, don’t use a while(Queue.IsEmpty()) loop that spins indefinitely. This consumes 100% of a CPU core’s cycles. Instead, use a synchronization event (like FEvent) to wake the consumer thread only when new data is available.

6. Minimize Memory Allocations

Many lock-free implementations perform best when they are “fixed-size” or use a pre-allocated linked list. Frequent memory allocations (using new or malloc) during a Push operation can introduce locks at the OS level, defeating the purpose of using a lock-free atomic container.

7. Prefer the Task System for General Logic

Unless you are building a low-level engine subsystem, consider using the Tasks System (UE::Tasks) instead of raw atomic queues. The Tasks System handles the thread safety and scheduling for you, using these atomic primitives internally while providing a much safer and more readable API.

8. Verify with Thread Sanitizers

Lock-free code is notoriously difficult to debug. When implementing logic with TAtomicQueue, use tools like Unreal Insights to check for thread contention or stalls. If you encounter mysterious crashes, use a thread sanitizer to ensure your producer-consumer logic isn’t violating the atomic nature of the container.