---
layout: default
title: GeometryProcessingInterfaces
---

<!-- ai-generation-failed -->

<h1>GeometryProcessingInterfaces</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/GeometryProcessingInterfaces/GeometryProcessingInterfaces.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, GeometryCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ct base classes and interfaces that decouple high-level engine tools from low-level geometric algorithms. It serves as the “glue” that allows systems like Modeling Mode, Geometry Scripting, and the Procedural Content Generation (PCG) framework to access complex mesh processing operations without being tightly bound to a specific implementation.

By providing a unified interface for tasks like mesh simplification, Boolean operations, and UV generation, this module helps eliminate code duplication across the engine and ensures that different plugins can exchange geometric data in a standardized way.

Practical Usage Tips and Best Practices
Access Algorithms via the Module Manager
Instead of hard-coding calls to specific mesh plugins, use the FModuleManager to find and load the interfaces defined in this module. This approach helps you eliminate hard dependencies in your project’s Build.cs, making your code more modular and easier to maintain.
Implement IGeometryProcessingModule for Custom Tools
If you are building a custom mesh processing plugin, inherit from the interfaces in this module. This ensures that your tool can be easily integrated into the existing Unreal Editor menus and utilities, helping to eliminate the need for custom UI “boilerplate.”
Prefer Interfaces for Cross-Plugin Communication
When passing mesh data between a custom C++ module and a plugin like GeometryScript, use the shared interfaces. This helps you eliminate expensive data conversions (such as converting between FMeshDescription and FDynamicMesh3 multiple times), preserving performance during complex operations.
Use for Decoupled Mesh Simplification
The module defines interfaces for mesh reduction. By using these, you can swap between the standard engine simplifier and a custom third-party solution (like Simplygon) through a single configuration change. This practice helps eliminate the risk of being locked into a specific vendor’s API.
Verify Interface Availability at Runtime
Before calling a geometry operation, check if the required interface is valid. This is critical for tools that may run in a commandlet or a server environment where certain editor-only geometry plugins might be eliminated from the build.
Optimize Task Distribution
Many interfaces in this module are designed to work with the Task Graph system. When performing heavy geometric computations, ensure you are utilizing the asynchronous paths provided by the interfaces to eliminate main-thread hitches in the editor.
Distinguish from GeometryFramework
Note that while GeometryFramework handles the UDynamicMesh component and its rendering, GeometryProcessingInterfaces focuses strictly on the algorithms and logic. Keeping this distinction clear in your architecture helps you eliminate confusion regarding which module should handle data storage versus data manipulation.
Leverage for Automated Quality Checks
Use these interfaces to write editor utility scripts that analyze mesh topology (e.g., checking for non-manifold edges or holes). Automating these checks through a standard interface helps you eliminate “bad” geometry before it reaches the final packaging stage.