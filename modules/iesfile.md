---
layout: default
title: IESFile
---

<!-- ai-generation-failed -->

<h1>IESFile</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/IESFile/IESFile.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

c data files (.ies) into a format the engine can use for rendering. IES (Illuminating Engineering Society) files are industry-standard ASCII files that describe the real-world distribution and intensity of light from a specific fixture, accounting for lenses, reflectors, and bulb shapes.

This module allows Unreal Engine to import these files and convert them into a 1D texture (gradient) that functions as a multiplier for a light’s brightness. It is primarily used for Point, Spot, and Rect Lights, facilitating the elimination of “perfect” or unrealistic light falloff in favor of physically accurate lighting patterns.

Practical Usage Tips and Best Practices
1. Enable “Use IES Brightness” for Physical Accuracy

In the details panel of your light, you can toggle Use IES Brightness. When enabled, the engine uses the actual Lumens value stored within the IES file rather than the light’s default intensity. This is a best practice for the elimination of guesswork when trying to match real-world architectural lighting specifications.

2. Manage Exposure with “IES Brightness Scale”

IES files can often be significantly brighter than default engine lights, potentially blowing out your scene’s exposure. Instead of changing your global camera settings, use the IES Brightness Scale property on the light actor. This allows for the elimination of over-exposure while maintaining the unique shape and distribution of the light profile.

3. Prefer IES Profiles Over Light Functions for Shape

While Light Functions use materials to mask light, IES profiles are much more performant because they are processed as a 1D texture look-up. Using IES profiles for complex fixture patterns leads to the elimination of the instruction overhead and pixel shader costs associated with dynamic light function materials.

4. Audit ASCII Content in a Text Editor

Because IES files are human-readable ASCII, you can open them in any text editor to verify metadata like the manufacturer, lamp type, and wattage. If a file fails to import, checking the text for formatting errors facilitates the elimination of corrupted data before it reaches the engine’s importer.

5. Show Engine Content for Free Profiles

Unreal Engine comes with a library of pre-made IES profiles. To access them, enable Show Engine Content in the Content Browser and navigate to the Engine/EditorResources/IES folder. Utilizing these high-quality defaults assists in the elimination of time spent searching for external files during the early blocking-out phase of a level.

6. Watch for 1D Texture Artifacts

Since an IES profile is essentially a 1D gradient swept around an axis, very low-resolution IES data can sometimes cause stepping or “banding” in the light’s falloff. If this occurs, using a higher-quality IES file or increasing the texture resolution in the asset settings leads to the elimination of these visual artifacts.

7. Use for Realistic “Elimination” of Uniform Shadows

Standard digital lights often cast uniform, boring shadows. By applying an IES profile that reflects the internal geometry of a real light fixture, you introduce subtle irregularities into the light cone. This practice is essential for the elimination of the “CG look,” making your interiors feel grounded and realistic.

8. Verify Build.cs for Custom Importers

If you are writing a custom C++ tool to batch-import lighting data, you must include the "IESFile" module in your Build.cs. Proper module referencing is the only way to access the FIESFile struct and its parsing logic, ensuring the elimination of linker errors in your custom lighting pipeline.