---
layout: default
title: RHICore
---

<!-- ai-generation-failed -->

<h1>RHICore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/RHICore/RHICore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

agnostic implementations and shared utility code for the various Render Hardware Interface (RHI) backends.

Description and Purpose

While the RHI module defines the abstract interface (the “what”), RHICore provides the common machinery and base classes (the “how”) used by modern graphics APIs like DirectX 12, Vulkan, and Metal. Its primary purpose is to reduce code duplication across different RHI drivers by centralizing logic for complex tasks such as Resource State Tracking, Descriptor Management, and Pipeline State Object (PSO) caching. By using RHICore, engine contributors can eliminate the need to reinvent fundamental rendering patterns for every new platform, ensuring that low-level optimizations—like transition batching—are applied consistently across all high-end renderers.

Practical Usage Tips and Best Practices
Leverage RHICore for Custom RHI Extensions
If you are writing a custom RHI or a low-level rendering plugin, inherit from FRHICoreShaderResourceView or FRHICoreUnorderedAccessView. These base classes provide standardized member variables and lifecycle management, helping you eliminate boilerplate code while staying compatible with the engine’s global resource tracking.
Use Common Resource State Trackers
Modern APIs require manual memory barriers. RHICore contains FRHICoreResourceState, a shared utility for tracking the current state (e.g., Readable, Writable, Present) of a GPU resource. Utilizing this helper is the best way to eliminate redundant transitions and prevent “Read-After-Write” (RAW) hazards in custom rendering passes.
Implement PSO Caching via Base Classes
Compiling shaders at runtime causes hitches. RHICore provides the logic for FRHICoreGraphicsPipelineState and its associated hashing mechanisms. When implementing a new rendering feature, ensure your state structures are hash-compatible with RHICore’s logic to eliminate duplicate PSO creation and improve runtime performance.
Utilize the Descriptor Heap Helpers
Managing thousands of resource handles (SRVs/UAVs) is a major bottleneck in DX12 and Vulkan. RHICore includes shared logic for descriptor allocation and “staged” updates. Following these patterns in your low-level code helps you eliminate CPU-side overhead when binding large numbers of textures to a shader.
Batch Transitions with RHICore Logic
Individual resource transitions are expensive. Use the RHICore-provided transition batchers to group multiple barrier calls into a single command list operation. This is a critical best practice to eliminate driver-level stalls and maximize GPU throughput in complex scenes with many render targets.
Monitor for RHI-Specific Performance Pitfalls
Even though RHICore is platform-agnostic, it exposes common “Fast Paths” used by the renderer. When profiling, look for LogRHICore entries; the module often logs warnings when it detects inefficient resource usage patterns (like frequent “Lock/Unlock” operations), helping you eliminate bottlenecks before they reach the platform-specific driver.
Check for Thread-Safe Resource Initialization
RHICore handles much of the thread-local storage (TLS) logic for RHI Command Lists. When writing parallel rendering code, rely on RHICore’s context-management utilities to eliminate race conditions when enqueuing commands from multiple worker threads.
Stay Updated with Engine Versioning
As Unreal Engine moves towards more “Bindless” rendering architectures, RHICore is frequently updated with new resource management strategies. Regularly review the RHICore header files when upgrading your engine version to eliminate deprecated patterns and take advantage of the latest low-level GPU optimizations.