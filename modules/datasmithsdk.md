---
layout: default
title: DatasmithSDK
---

<!-- ai-generation-failed -->

<h1>DatasmithSDK</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Enterprise/Datasmith/DatasmithSDK/DatasmithSDK.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">DatasmithCore, DatasmithExporter, DatasmithExporterUI, UdpMessaging</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Exporter” plugins for third-party 3D applications (such as CAD, BIM, or DCC software). It provides the C++ interfaces necessary to translate a source application’s native scene—including geometry, hierarchies, PBR materials, lights, cameras, and metadata—into the .udatasmith format for Unreal Engine.

Unlike standard file formats like FBX, the SDK is designed to be “Engine-Aware,” allowing developers to preserve the design intent and complex data structures of the source software while optimizing them for real-time performance.

1. Adopt the Two-Phase Architecture

The SDK is designed to be used in two distinct steps to maintain data integrity.

Best Practice: First, use the DatasmithCore module to parse your host application and build an in-memory IDatasmithScene. Only once the hierarchy and properties are finalized should you use the DatasmithExporter to serialize the data to disk. This decoupling allows you to perform post-processing (like renaming or metadata injection) without affecting the original source data.
2. Leverage Metadata for Automation

One of the most powerful features of the Datasmith SDK is the ability to attach IDatasmithMetaDataElement to any actor.

Tip: Export as much non-visual data as possible (e.g., “FireRating,” “Weight,” “PartNumber”). Once inside Unreal, you can use Blueprints or Python scripts to read this metadata and automatically assign gameplay logic, tags, or physics properties, significantly reducing manual work for the end user.
3. Implement Direct Link for Real-Time Sync

The SDK includes the Direct Link API, which allows your exporter to send updates over a network socket instead of writing files.

Best Practice: For tools used in iterative design, prioritize Direct Link implementation. It allows users to see their changes in Unreal Engine instantly as they move objects or tweak materials in the source application, eliminating the friction of constant “Export-Import” cycles.
4. Optimize Texture Resolutions

Many professional 3D applications use textures with non-standard or excessively high resolutions that can degrade real-time performance.

Tip: Use the SDK’s utility functions to resize or reformat textures during the export phase. Aim for “Power of Two” dimensions (e.g., 1024x1024 or 2048x2048). This ensures that Unreal Engine can compress the textures for the GPU and generate Mipmaps efficiently upon import.
5. Preserve Instancing and Hierarchy

Avoid the temptation to flatten the scene hierarchy or merge objects to “simplify” the export.

Best Practice: Preserve the original parent-child relationships and use IDatasmithMeshActorElement to reference shared geometry. Datasmith handles instancing automatically; if you merge everything into a single mesh, you eliminate Unreal’s ability to perform occlusion culling, leading to poor runtime frame rates.
6. Correct Module Dependencies

When integrating the SDK into your own C++ project or engine plugin, you must include the primary modules in your Build.cs file:

C++
	    TSharedRef<IDatasmithScene> MyScene = FDatasmithSceneFactory::CreateScene(TEXT("MyScene"));

	    // ... Perform Export ...

	    // Ensure the scene is released once serialization is finished

	    ```

	 

	### 3. Use Metadata for Downstream Automation

	One of the SDK’s most powerful features is the ability to attach `IDatasmithMetaDataElement` to any actor.

	*   **Tip:** Instead of just exporting geometry, export engineering data (e.g., "Weight," "Manufacturer," "FireRating"). Inside Unreal, you can use Python or Blueprints to read this metadata on import and automatically assign physics properties, tags, or gameplay logic.

	 

	### 4. Reformat Textures to Power-of-Two

	Many CAD and BIM applications use non-standard texture resolutions (e.g., 700x700) that Unreal Engine cannot compress efficiently.

	*   **Best Practice:** Use the utility functions in the SDK to reformat textures during the export phase. Converting textures to "Power of Two" (1024, 2048, etc.) before writing the `.udatasmith` file ensures that the engine can generate Mipmaps and use GPU-friendly compression immediately upon import.

	 

	### 5. Preserve Scene Granularity

	Avoid the temptation to merge all objects in a room into a single mesh during export.

	*   **Tip:** Export objects as individual `IDatasmithMeshElement` instances. Datasmith handles instancing automatically (multiple actors pointing to one mesh). If you merge everything, you eliminate Unreal’s ability to perform occlusion culling, which will severely degrade runtime performance.

	 

	### 6. Implement DirectLink for Live Iteration

	The Datasmith SDK includes **DirectLink**, allowing your exporter to send updates over a network socket instead of writing files.

	*   **Best Practice:** If you are building a tool for designers, implement DirectLink. It allows the user to see their changes in Unreal Engine in real-time as they work in the source application, removing the friction of constant "Export-Import" cycles.

	 

	### 7. Correct Build.cs Dependencies

	If you are integrating the SDK into an engine plugin or tool, you must include the following modules to access the full API:

	```csharp

	// In your .Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { 

	    "DatasmithCore", 

	    "DatasmithExporter" 

	});

	```

	 

	### 8. Use the SDK's Built-in Logger

	When an export fails due to a corrupt mesh or missing texture, the user needs actionable feedback.

	*   **Tip:** The SDK provides a logging interface. Use it to flag problematic assets during the export process. These logs are displayed in the Unreal Datasmith Messages window, helping users fix their source models without needing to look at C++ logs or debuggers.

	 

	### Example: Basic Export Setup

	```cpp

	#include "DatasmithSceneFactory.h"

	#include "DatasmithExporter.h"

	#include "IDatasmithSceneElements.h"

	 

	void ExportMyScene(const TCHAR* OutputPath)

	{

	    // 1. Create the Scene

	    TSharedRef<IDatasmithScene> DatasmithScene = FDatasmithSceneFactory::CreateScene(TEXT("MyCustomExport"));

	 

	    // 2. Add an Actor

	    TSharedRef<IDatasmithMeshActorElement> MeshActor = FDatasmithSceneFactory::CreateMeshActor(TEXT("Wall_01"));

	    DatasmithScene->AddActor(MeshActor);

	 

	    // 3. Setup the Exporter

	    FDatasmithSceneExporter Exporter;

	    Exporter.SetName(DatasmithScene->GetName());

	    Exporter.SetOutputPath(OutputPath);

	 

	    // 4. Export to Disk

	    Exporter.Export(DatasmithScene);

	}

	 
Copy code

Ensure you are using the correct version of the SDK that matches your target Unreal Engine version to prevent binary compatibility issues.

7. Explicit Memory Management

Because Datasmith scenes can be massive (containing millions of polygons and thousands of textures), memory management is critical.

Constraint: You must explicitly release the IDatasmithScene and its elements once the export process is complete. In a long-running host application session, failing to eliminate these objects will lead to a significant memory leak and eventual application instability.
8. Use the SDK Logger for Troubleshooting

The SDK provides a specialized logging interface to communicate issues back to the user.

Tip: Use Datasmith_LogWarning and Datasmith_LogError to flag missing textures or unsupported geometry during the export. These messages are displayed in the Unreal Datasmith Messages window, helping the user identify and fix specific issues in their source model before they are imported.