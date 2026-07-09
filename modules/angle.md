---
layout: default
title: ANGLE
---

<!-- ai-generation-failed -->

<h1>ANGLE</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/ANGLE/ANGLE.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ation in Unreal Engine that acts as a compatibility layer between different graphics APIs. It translates OpenGL ES (the standard for mobile and web graphics) into “native” desktop APIs such as DirectX 11, DirectX 12, or Vulkan.

In Unreal Engine, it is primarily used to provide a consistent Mobile Preview experience on Windows. It allows the editor to simulate exactly how a material or shader will look on an Android or iOS device by running the mobile rendering path through the desktop’s DirectX hardware.

1. Module Configuration

ANGLE is a ThirdParty module. You generally do not link to it in your gameplay code. Instead, it is utilized by the engine’s RHI (Rendering Hardware Interface). If you are developing a custom engine-level plugin that requires manual OpenGL ES calls on Windows, you would reference it in your Build.cs:

C#
	// MyPlugin.Build.cs

	AddEngineThirdPartyPrivateStaticDependencies(Target, "ANGLE");
Copy code
2. Practical Usage Tips & Best Practices
Accurate Mobile Look-Dev

Always use the Mobile Preview (PIE) mode when designing materials for mobile platforms. This mode uses ANGLE to translate the shaders. If a material looks correct in the standard Shader Model 6 (SM6) editor but “breaks” or has its visual quality “eliminated” in Mobile Preview, it is likely due to an OpenGL ES limitation that ANGLE is correctly highlighting.

Validate Texture Formats

ANGLE is strict about texture compression and formats allowed in OpenGL ES. If you are seeing rendering artifacts in the editor’s mobile preview, check your Texture Compression Settings. ANGLE helps catch issues where a texture format might be supported by your GPU but is illegal in the mobile specification.

Debugging Shader Complexity

When using the Mobile Patch Level preview, pay attention to the “Mobile Stats” in the material editor. ANGLE helps simulate the instruction limits of mobile GPUs. If your shader exceeds these limits, ANGLE will fail to compile the translated HLSL, alerting you before you ever deploy to a physical device.

Handle Coordinate System Differences

OpenGL uses a different coordinate system convention (bottom-left) compared to DirectX (top-left). ANGLE handles the Y-flip automatically. If you are writing custom HLSL in a Custom Expression Node, be careful with UV manipulations; always test in the ANGLE-powered Mobile Preview to ensure your textures aren’t flipped.

Performance: Don’t Use for Production PC Builds

While ANGLE is highly stable, it is a translation layer. You should never force a shipping Windows build to use OpenGL ES via ANGLE. Native DirectX or Vulkan will always provide better performance. ANGLE’s role is strictly for development, simulation, and cross-platform abstraction.

Use “-FeatureLevelES31” Command Line

You can force the editor to use the ANGLE translation path by launching it with the -FeatureLevelES31 or -opengl command-line arguments. This is useful for “eliminating” environment-specific bugs where a shader works on a high-end PC but fails on mobile-equivalent hardware.

Check for Driver Compatibility

Because ANGLE translates to DirectX, ensure your development machine has up-to-date DirectX End-User Runtimes. If ANGLE cannot find a suitable native back-end to translate to, the Unreal Engine mobile preview will often fallback to a software renderer or crash during the RHI initialization.

Monitor the Log for Translation Errors

If a shader fails to render in the mobile viewport, check the Output Log for “GL_INVALID_OPERATION” or translation errors. ANGLE is very descriptive in its logs; it will often tell you exactly which OpenGL ES feature is being used that the current hardware cannot support, allowing you to optimize your asset accordingly.