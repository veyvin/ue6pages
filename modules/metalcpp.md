---
layout: default
title: MetalCPP
---

<!-- ai-generation-failed -->

<h1>MetalCPP</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/MetalCPP/MetalCPP.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>CPlusPlus</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

he engine to interface with Apple’s Metal-cpp headers, providing a low-level C++ interface for the Metal graphics API.

Description and Purpose

Traditionally, Metal programming requires Objective-C or Swift. The MetalCpp module integrates Apple’s official C++ wrapper, allowing Unreal Engine’s renderer to interact with the Metal RHI (Rendering Hardware Interface) using pure C++. Its primary purpose is to simplify the cross-platform development pipeline by allowing developers and engine engineers to write macOS and iOS graphics logic without switching languages. This helps eliminate the “language barrier” overhead between the C++ engine core and Apple’s native graphics drivers, resulting in more maintainable and performant rendering code for Apple Silicon.

Practical Usage Tips and Best Practices
Implement via TargetRules and ModuleRules When working with Metal-specific C++ logic, ensure you include MetalCpp in your PublicDependencyModuleNames within your .Build.cs file. This ensures the compiler correctly locates the Metal-cpp headers, helping you eliminate “File Not Found” errors during the compilation of Mac or iOS targets.
Strictly Manage Autorelease Pools Even though the syntax is C++, the underlying Metal objects are still managed by Objective-C’s Reference Counting (ARC). Wrap your Metal-cpp logic in NS::AutoreleasePool blocks to eliminate memory leaks that occur when GPU resources are allocated frequently but never released by the system.
Verify Platform Compatibility Gates The MetalCpp module is only valid for Apple platforms. Always wrap your code in #if PLATFORM_MAC || PLATFORM_IOS preprocessor macros. This is a best practice to eliminate build failures when compiling for Windows, Linux, or consoles where the Metal headers do not exist.
Use NS::String for Metal Identifiers Metal-cpp requires NS::String for object labeling and debugging names. Use the provided conversion utilities to pass engine names into Metal. Properly labeling your buffers and textures in this way is the best way to eliminate confusion when profiling with Xcode’s GPU Frame Capture.
Synchronize with the RHI Thread Unreal’s rendering logic is typically multi-threaded. When using Metal-cpp to call low-level commands, ensure you are operating on the Render Thread or the RHI Thread. Direct calls from the Game Thread can lead to race conditions; adhering to the RHI architecture helps you eliminate flickering and crashes.
Leverage Metal 3.0 Features If your project targets modern Apple Silicon (M1/M2/M3), use the module to access Metal 3.0 features like Mesh Shaders or Fast Resource Loading. This allows the engine to eliminate traditional vertex-processing bottlenecks, significantly improving performance in high-fidelity scenes.
Avoid Raw Pointer Mismanagement Metal-cpp uses a “retain/release” pattern similar to SharedPtr. Always use the ->release() method on objects when you are finished with them if they were created via alloc, new, or copy. Following this pattern helps you eliminate dangling references that cause the GPU driver to crash.
Profile via Xcode Instruments While Unreal Insights is powerful, the MetalCpp module is designed to work seamlessly with Apple Instruments. Use the “Metal System Trace” to see exactly how your C++ calls are being translated into GPU commands, which helps you eliminate stalls in the command buffer.