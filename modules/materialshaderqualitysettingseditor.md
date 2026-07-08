---
layout: default
title: MaterialShaderQualitySettingsEditor
---

<!-- ai-generation-failed -->

<h1>MaterialShaderQualitySettingsEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/MaterialShaderQualitySettingsEditor/MaterialShaderQualitySettingsEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, InputCore, MaterialShaderQualitySettings, PropertyEditor, Slate, SlateCore, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

at provides the user interface and logic for managing shader quality overrides across different platforms and quality tiers. It specifically handles the “Android Material Quality” and “iOS Material Quality” sections found within Project Settings.

This module is used by technical artists and rendering engineers to selectively disable or simplify expensive material features (like high-quality reflections, lightmap directionality, or normal map calculations) for specific hardware. By providing a centralized UI for these overrides, it helps you eliminate the performance overhead of complex shaders on mobile or low-end devices without requiring manual changes to every individual material asset.

Practical Usage Tips and Best Practices
Access via Project Settings
Navigate to Project Settings > Platforms and look for the Material Quality sections (e.g., Android Material Quality - Vulkan). Use this module’s interface to toggle overrides like “Force Fully Rough” or “Disable Material Normal Calculation” to globally optimize your project’s look and feel for specific tiers.
Utilize the ‘Update Preview Shaders’ Button
After making changes in the Quality Settings UI, you must click the Update Preview Shaders button. This module triggers a background recompile of the shader cache, helping you eliminate discrepancies between your settings and what is actually being rendered in the viewport.
Leverage the ‘Quality Switch’ Node
In the Material Editor, use the Quality Switch expression. This module ensures that when you change the preview level in the editor, the “High,” “Medium,” or “Low” pins on that node update correctly. This allows you to eliminate expensive math from a material when the engine is set to a lower quality tier.
Force ‘Fully Rough’ for Mobile
One of the most effective optimizations provided by this module is the Force Fully Rough override. Enabling this for low-end mobile tiers removes the specular calculation from materials, which helps you eliminate significant GPU cycles on devices that cannot handle complex reflections.
Optimize Shadow Mapping Quality
Use the Mobile Shadow Mapping Quality dropdown within these settings to scale down shadow resolution or filtering quality for specific platforms. This allows you to eliminate memory bandwidth bottlenecks on mobile devices that have limited VRAM.
Enable ‘Discard Quality During Cook’
For final distribution, ensure “Discard Quality During Cook” is enabled for unused tiers. This ensures the module’s logic excludes unnecessary shader permutations from your packaged build, helping you eliminate bloated “shders.code” files and reducing the overall download size of your game.
Preview Hardware with ‘Preview Rendering Level’
Combine this module’s settings with the Settings > Preview Rendering Level menu in the main toolbar. By switching the editor to “Android Vulkan” or “iOS Metal,” you can see exactly how the quality overrides you configured will look, helping you eliminate visual bugs before testing on a physical device.
Monitor Shader Permutation Counts
Be careful when enabling many different quality overrides, as each combination can increase the total number of shader permutations. Use the “Shader Statistics” window to monitor the impact of your settings, which helps you eliminate excessively long build times caused by a “permutation explosion.”