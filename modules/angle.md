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

ty rendering translation layer integrated into Unreal Engine. Developed by Google, its primary purpose is to translate OpenGL ES API calls into DirectX (typically D3D11 or D3D12) calls in real-time.

In Unreal Engine, this module is essential for the Mobile Previewer and the Android Emulator on Windows. It allows developers to run and debug mobile-specific shaders and rendering paths on a Windows desktop using the native DirectX driver, ensuring the visual output closely matches what would be seen on a physical mobile device.

Practical Usage Tips and Best Practices
1. Use for Accurate Mobile Look-Dev

When using Window > Platforms > Android ES3.1 preview mode, the engine utilizes ANGLE to emulate the mobile GPU’s behavior. This is the most accurate way to verify that your materials, post-process effects, and “elimination” VFX (particles/decals) will render correctly on mobile hardware without deploying to a device.

2. Debug via Command-Line Arguments

If you encounter crashes or graphical glitches when launching a mobile preview, you can force specific RHI behaviors for ANGLE using command-line arguments. Use -featureleveles31 or -opengl to ensure the engine initializes the translation layer correctly for your session.

3. Monitor Performance Overhead

While ANGLE is highly optimized, it is still a translation layer. Expect a slight performance delta compared to native DirectX rendering. Do not use ANGLE-based previews for final performance profiling; always use a physical device to measure the true impact of draw calls and “elimination” logic on mobile CPU/GPU thermal limits.

4. Clear the Shader Cache on Glitches

If you notice persistent visual artifacts or “rainbow” textures in your mobile preview, the ANGLE-translated shader cache may be corrupt. Use the -ClearOpenGLBinaryProgramCache command-line flag once to force a total elimination of the cached binaries and trigger a fresh recompile.

5. Verify Material Transparency and Depth

Mobile GPUs handle transparency and depth testing differently than desktop GPUs. Use the ANGLE-powered preview to check for “sorting” issues or depth-buffer artifacts on your character’s “elimination” effects, as these often look fine in the standard Shader Model 6 (SM6) editor but fail on mobile.

6. Identify Unsupported Shader Features

ANGLE will often throw specific warnings in the Output Log if a material uses a feature unsupported by OpenGL ES (such as certain complex texture arrays or high-count loop iterations). Keep the log open when working on mobile materials to catch these incompatibilities early.

7. Toggle Emulated Features in Project Settings

You can fine-tune how ANGLE emulates the mobile experience by adjusting settings in Project Settings > Platforms > Android. Enabling or disabling “Support Vulkan” or “Support OpenGL ES3.1” will change which translation paths the editor prepares, affecting how accurately the preview reflects your target hardware.

8. Ensure Driver Compatibility

ANGLE relies heavily on your Windows DirectX drivers being up to date. If you experience “D3D Device Lost” errors specifically when opening mobile preview windows, it is often an issue with the underlying translation from OpenGL to D3D. Updating your GPU drivers is usually the first step to resolving ANGLE-specific stability issues.