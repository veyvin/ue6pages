---
layout: default
title: NVAftermath
---

<!-- ai-generation-failed -->

<h1>NVAftermath</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/NVIDIA/NVaftermath/NVaftermath.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

o Unreal Engine. It is a diagnostic tool designed specifically for Windows-based developers using NVIDIA GeForce GPUs to troubleshoot “GPU Hangs” and “Device Removed” crashes.

When a GPU crash occurs, the standard CPU callstack is usually unhelpful because the GPU was executing commands sent frames ago. This module provides “GPU Breadcrumbs,” which allow developers to see exactly which rendering command (e.g., a specific shadow pass or compute shader) was being processed at the instant the hardware failed.

Practical Usage Tips & Best Practices
1. Enable via Command Line or Config

Aftermath is not active by default due to a minor memory overhead. You must explicitly enable it to begin gathering data.

Best Practice: Add r.GPUCrashDebugging=1 to your ConsoleVariables.ini or launch the editor/game with the -gpucrashdebugging command-line argument. This ensures the elimination of “blind” debugging when trying to reproduce sporadic rendering crashes.
2. Analyze the “GPU Stack Dump” in Logs

When the engine crashes with Aftermath enabled, it prints a specialized “GPU Stack Dump” to the log file.

Tip: Look for the [Aftermath] prefix in your Saved/Logs files. It will show a trail such as Scene > Lights > DirectLight. This allows for the elimination of guesswork by pinpointing the specific rendering pass that caused the timeout.
3. Use to Debug TDR (Timeout Detection and Recovery)

Windows will reset the GPU driver if a command takes longer than 2 seconds (a TDR event).

Best Practice: Use Aftermath to identify if a specific expensive shader (like a complex Ray Tracing Global Illumination pass) is triggering the TDR. Identifying the culprit leads to the elimination of driver resets through better optimization or task splitting.
4. Combine with RHI Breadcrumbs

While Aftermath provides NVIDIA-specific data, Unreal also has its own internal breadcrumb system.

Tip: Use -gpucrashdebugging -gpubreadcrumbs together. This provides two layers of validation, facilitating the elimination of false positives and giving you a clearer picture of the state of the Render Hardware Interface (RHI) during a failure.
5. Monitor for Out-of-Memory (OOM) Errors

A significant portion of GPU crashes are simply caused by exhausting VRAM.

Best Practice: Check the Aftermath status in the log for “Page Fault” or “Out of Memory.” Using this data results in the elimination of crashes by allowing you to identify which assets (textures or meshes) are pushing the GPU beyond its physical memory limits.
6. Isolate Crashes to Specific Shaders

Aftermath can often point to the exact shader resource causing a page fault.

Tip: If the log indicates a crash in a specific compute shader, use the information to check for out-of-bounds array access or null resource pointers. This leads to the elimination of “Illegal Access” errors in your custom Niagara or Global Shaders.
7. Performance Considerations

While NVIDIA Aftermath is designed to be lightweight, it does have a non-zero impact on GPU performance and memory.

Best Practice: Only enable Aftermath during active debugging sessions or in “Test” builds. Do not ship your final “Shipping” build with it enabled unless you specifically need it for a “Beta” period to ensure the elimination of unnecessary performance overhead for your end-users.
8. Verify Driver Compatibility

Aftermath requires specific support within the NVIDIA display driver to function.

Tip: Ensure your development team is using the latest “Game Ready” or “Studio” drivers. Keeping drivers updated results in the elimination of “Aftermath failed to initialize” warnings in your output log, ensuring you always have valid crash data when you need it.