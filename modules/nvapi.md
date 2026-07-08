---
layout: default
title: NVAPI
---

<!-- ai-generation-failed -->

<h1>NVAPI</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/NVIDIA/nvapi/NVAPI.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

API SDK. It acts as a specialized bridge that allows the engine to communicate directly with NVIDIA GPUs and drivers to access hardware-specific features that are not available through standard graphics APIs like DirectX or Vulkan.

What it is and What it’s used for

Located in Engine/Source/ThirdParty/NVIDIA/nvapi, this module provides the headers and binaries required to interface with NVIDIA-specific technology. While the RHI (Render Hardware Interface) handles general drawing, NVAPI is used for deeper hardware control and optimization.

Primary uses include:

Hardware Detection: Identifying specific GPU architectures (e.g., Ada Lovelace, Ampere) and driver versions to enable or disable features.
Performance Technologies: Providing the foundational support for DLSS (Deep Learning Super Sampling), Reflex (Latency Reduction), and Frame Generation.
Advanced Rendering: Accessing specialized features like Variable Rate Shading (VRS), Multi-View Rendering, and SLI/Crossfire configurations.
Diagnostic Tools: Powering systems like NVIDIA Nsight Aftermath for debugging GPU crashes and “Device Removed” errors.
Practical Usage Tips and Best Practices
1. Enable GPU Crash Debugging (Aftermath)

If your project suffers from intermittent GPU crashes, enable Nsight Aftermath by adding r.GPUCrashDebugging=1 to your ConsoleVariables.ini. This utilizes NVAPI to provide a detailed “dump” of exactly what the GPU was doing at the moment of failure, leading to the elimination of guesswork during stability testing.

2. Check Hardware Support via Blueprint or C++

Before enabling high-end features, use the QuerySupport functions provided by the DLSS or Streamline plugins (which wrap NVAPI). Checking if a feature like Frame Generation is supported on the user’s specific card ensures the elimination of crashes or “black screen” errors on older or non-NVIDIA hardware.

3. Require DX12 for Modern NVIDIA Features

Most modern technologies accessed via NVAPI (such as DLSS 3 and Reflex) require the DirectX 12 RHI. Ensure your project is targeting DX12 in the Platforms settings; failing to do so will result in the elimination of access to these high-performance features even on high-end RTX cards.

4. Use “With DLSS” Macros in C++

When writing custom engine modifications that interface with NVIDIA tools, wrap your code in #if WITH_DLSS or similar macros. This ensures that your project remains cross-platform and prevents the elimination of your ability to compile for consoles or mobile devices that do not use the NVAPI.

5. Monitor System Latency with Reflex

Utilize the NVIDIA Reflex markers provided through this module to monitor “Motion-to-Photon” latency. Lowering system latency via the Reflex “Low Latency Mode” is the primary strategy for the elimination of “floaty” input feel in competitive first-person shooters.

6. Optimize Screen Percentage with DLSS

When DLSS is active, the engine’s standard “Screen Percentage” is superseded by DLSS Quality levels (Quality, Balanced, Performance). Educate users that 50% screen percentage with DLSS Performance is superior to 100% native with TAA, resulting in the elimination of performance bottlenecks without sacrificing visual clarity.

7. Leverage Unified Memory Diagnostics

On laptops or systems with limited VRAM, NVAPI can provide detailed reports on memory pressure. Monitoring these values allows the engine to scale back texture streaming dynamically, leading to the elimination of “Out of Video Memory” crashes during intense gameplay sequences.

8. Strategic Elimination of Legacy Driver Support

If your project utilizes the latest ray-tracing features through NVAPI, set a minimum required driver version in your project’s configuration. Enforcing a modern driver version results in the elimination of bug reports caused by outdated NVIDIA “Game Ready” drivers that lack support for the latest engine-level optimizations.