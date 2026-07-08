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

used TIFF (Tagged Image File Format) library. It provides the engine with the ability to read and write complex, high-bit-depth image data that goes beyond the capabilities of standard consumer formats like PNG or JPEG.

What it is and What it’s used for

Located in Engine/Source/ThirdParty/libtiff, this module is a core dependency for the engine’s asset ingestion pipeline. Unlike many other image libraries, libtiff is specialized for scientific and professional-grade data, supporting various compression schemes and multi-channel configurations.

Primary uses include:

Landscape Heightmap Import: Processing 16-bit and 32-bit grayscale TIFFs, which are the standard export format for terrain generators like Gaea and World Machine.
GIS and Satellite Data: Handling Geospatial TIFFs (GeoTIFF) used in large-scale world building and simulation.
High Dynamic Range (HDR) Imaging: Importing textures that require floating-point precision for lighting and visual effects.
Photogrammetry Workflows: Ingesting high-fidelity source images for texture baking and mesh generation.
Practical Usage Tips and Best Practices
1. Use 16-bit Grayscale for Landscapes

When exporting heightmaps from external tools, always choose 16-bit TIFF over 8-bit formats. The libtiff module allows Unreal to interpret these 65,536 levels of gray, leading to the elimination of “stair-stepping” or banding artifacts on your terrain slopes.

2. Prefer LZW or No Compression

TIFF supports many compression types. For the best compatibility with Unreal’s importer, use LZW or None. While libtiff supports many schemes, using specialized or proprietary compression can lead to the elimination of import stability or cause the engine to fail to recognize the file header.

3. Adhere to Power-of-Two Dimensions

Even though TIFF is a flexible container, Unreal Engine still requires textures to be power-of-two (e.g., 2048, 4096) for mipmapping and streaming. Using non-power-of-two TIFFs will result in the elimination of texture streaming capabilities, forcing the engine to keep the full-resolution asset in memory at all times.

4. Convert 32-bit Float to 16-bit for Landscapes

While libtiff can read 32-bit float data, the Unreal Landscape system natively uses 16-bit integers for its heightfield. If you import a 32-bit TIFF, the engine must perform a conversion. It is a best practice to normalize your data in your terrain tool first to ensure the elimination of data loss during this conversion.

5. Strip Metadata for Smaller Source Assets

TIFF files often contain large amounts of metadata (camera info, GPS data). This isn’t used by the engine but increases the size of your Source folder. Using a tool to strip unnecessary tags before import helps in the elimination of bloated project sizes on your version control system.

6. Utilize for Data-Driven Textures

If you are creating custom technical shaders that require precise data (like flow maps or complex masks), use TIFF. The libtiff module ensures that your data is read exactly as authored, aiding in the elimination of the compression noise that usually ruins technical textures when using JPEGs.

7. Verify sRGB Settings on Import

When importing a TIFF intended as a mask or heightmap, ensure the sRGB checkbox is unchecked in the Texture Editor. Because libtiff provides raw data, leaving sRGB enabled will apply a gamma curve that distorts your values, leading to the elimination of accuracy in your displacement or masks.

8. Strategic Elimination of Legacy RAW Files

Historically, developers used .raw files for terrain because they lacked a header. With the robust libtiff module in UE5, it is better to use TIFF for heightmaps. The inclusion of a file header in TIFF prevents the elimination of time spent manually entering bit-depth and resolution settings during every import.