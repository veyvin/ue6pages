---
layout: default
title: MaterialX
---

<!-- ai-generation-failed -->

<h1>MaterialX</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/MaterialX/MaterialX.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

(developed by ILM) that allows for the transfer of rich material and shading data between different DCC (Digital Content Creation) tools and Unreal Engine.

Description and Purpose

The primary purpose of this module is to provide a standardized way to import look-development data from external software like Maya, Houdini, or Substance without having to manually rebuild complex shader networks in Unreal Engine. It acts as a bridge that parses .mtlx files and translates them into Unreal Material Graphs or Substrate networks. By leveraging this module, technical artists can eliminate the time-consuming process of re-connecting texture samplers and math nodes across different platforms, ensuring visual consistency throughout the production pipeline.

Practical Usage Tips and Best Practices
Prioritize Autodesk Standard Surface
For the most reliable results, author your MaterialX files using the Autodesk Standard Surface (OpenPBR) node. This is the most mature mapping within the module, helping you eliminate conversion errors or “broken” nodes during the import process.
Enable the Substrate Plugin
MaterialX support is heavily tied to Unreal Engine’s Substrate framework. To get the highest fidelity and support for complex layered materials, enable Substrate in your project settings. This allows the module to eliminate the limitations of the traditional “Legacy” shading model.
Prefer Textures Over Complex Math
While MaterialX supports procedural math nodes, Unreal’s translator is most efficient when handling texture-based inputs. Using baked textures for your MaterialX inputs is the best way to eliminate “unsupported node” warnings and ensure your materials look identical to their source.
Use the USD Integration
MaterialX is often embedded within USD (Universal Scene Description) files. When importing a USD stage, the MaterialX module works under the hood to translate the shading data. Keeping your .mtlx files linked within your USD hierarchy helps you eliminate the need for separate material import steps.
Test with the MaterialX Viewer First
Before importing into Unreal, verify your file in the standalone MaterialXView tool. If the material does not render correctly there, it will not render correctly in Unreal. This pre-check helps you eliminate troubleshooting time within the engine.
Avoid View-Dependent Nodes
Nodes that rely on specific camera vectors or screen-space information in other DCCs may not translate perfectly. Try to eliminate or simplify view-dependent logic in your MaterialX graph to ensure the Unreal translator can generate a stable, real-time material.
Monitor the Output Log for Missing Nodes
When you import a .mtlx file, keep the Output Log open. The module will list any nodes it could not translate. Identifying these specific failures allows you to manually replace them in the resulting Material Instance, helping you eliminate visual gaps in the shader.
Leverage for Cross-Platform “Single Source of Truth”
Use MaterialX as your master format if your project spans multiple renderers (e.g., Arnold for cinematics and Unreal for gameplay). This strategy helps you eliminate look-dev drift, where the character’s skin or metal looks different in different parts of the production.