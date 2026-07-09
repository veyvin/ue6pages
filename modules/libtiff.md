---
layout: default
title: LibTiff
---

<!-- ai-generation-failed -->

<h1>LibTiff</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/LibTiff/LibTiff.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

that integrates the Tag Image File Format (TIFF) library into the engine’s ecosystem. While Unreal Engine primarily uses compressed formats like DXT or BC7 for real-time rendering, libtiff is essential for the high-fidelity import pipeline and data-heavy workflows.

It is primarily used to handle high-bit-depth textures (16-bit and 32-bit), high-resolution heightmaps for landscapes, and scientific or geospatial data where lossy compression (like JPEG) would “eliminate” critical detail.

Practical Usage Tips and Best Practices
1. Use for High-Precision Landscapes

When importing landscape heightmaps, TIFF is superior to PNG. PNG is limited to 16-bit integer data, whereas TIFF can handle 32-bit floating-point data. This extra precision helps “eliminate” the “stepping” or “staircase” artifacts often seen on smooth mountain slopes in the Landscape system.

2. Preferred Format for Displacement Maps

For high-end character or environment art, use TIFF for displacement and height maps. Because the libtiff module supports uncompressed or LZW-compressed 16-bit channels, it preserves the subtle gradients needed for Nanite micro-poly detail that standard 8-bit formats would “eliminate.”

3. Manage Module Dependencies

If you are writing a custom C++ importer or an Editor tool that needs to parse TIFF files directly, you must add the module to your Build.cs file. Note that this is typically an External module dependency.

C#
AddEngineThirdPartyPrivateStaticDependencies(Target, "libtiff");
Copy code
4. Avoid TIFF for Runtime Textures

While libtiff allows the engine to read TIFFs during the import process, you should never attempt to use raw TIFF data at runtime for UI or materials. Always let the engine “eliminate” the TIFF container by converting it into an internal UTexture2D asset, which is then compressed into a GPU-friendly format (e.g., Oodle or ZLib).

5. Be Mindful of File Size

TIFF files can be massive because they often store data uncompressed. To “eliminate” unnecessary disk usage in your source control (like Perforce or Git), ensure your TIFFs are saved using LZW or Zip compression. These are lossless formats supported by the libtiff module that significantly reduce file size without losing a single pixel of data.

6. Coordinate with Geospatial Tools (GDAL)

If you are working with real-world satellite data (GeoTIFF), the standard libtiff module handles the image data, but the metadata (coordinate systems) may require additional parsing. For NASA-level accuracy, use an external tool to convert GeoTIFFs to a standard 16-bit/32-bit TIFF before importing to ensure the libtiff module reads the height values correctly.

7. Handle Alpha Channels Carefully

TIFFs can store multiple layers and complex alpha channels. When importing via the libtiff pipeline, ensure your export settings in Photoshop or Substance are set to “Finalize” the layers. Multiple alpha channels in a single TIFF can sometimes confuse the standard importer, leading to the accidental “elimination” of your transparency data.

8. Verify Bit-Depth in the Texture Editor

After importing a TIFF, open the Texture Asset. Check the Displayed and Source bit-depth. If the libtiff module successfully processed a high-bit-depth file, you should see “RGBA16” or “Gray16” in the details. If it shows “8-bit,” your source file may have been flattened or downsampled before it reached the engine.

Performance & Best Practices
Import Time: Importing large (8k+) 32-bit TIFFs can be slow as the engine must process the data through the libtiff wrapper and then build mips. Use the Derived Data Cache (DDC) to ensure your team doesn’t have to re-process these large files repeatedly.
Data Packing: For masks (Roughness, Metallic, Ambient Occlusion), you can use a 16-bit TIFF to pack multiple high-precision masks into the R, G, and B channels, providing much cleaner material transitions.