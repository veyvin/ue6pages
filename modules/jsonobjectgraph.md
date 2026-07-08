---
layout: default
title: JsonObjectGraph
---

<!-- ai-generation-failed -->

<h1>JsonObjectGraph</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/JsonObjectGraph/JsonObjectGraph.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

g to reference the FJsonObjectGraph class or its associated helpers.
C++
	    PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Json", "JsonObjectGraph" });

	    ```

	 

	*   **Preserve Object Identity with IDs**  

	    The module works by assigning a unique ID to every UObject in the graph. In the resulting JSON, object pointers are replaced by these IDs. This helps you **eliminate** "shallow copy" issues where deserializing a child would normally create a disconnected twin rather than pointing back to the original parent.

	 

	*   **Use for Deep Serialization**  

	    When you need to save an entire "Actor and all its components" or a "Skill Tree made of many UObjects," use `FJsonObjectGraph::SerializeObjectGraph`. This function traverses the graph starting from a root object, ensuring that every referenced object is captured in the JSON payload.

	 

	*   **Implement IJsonObjectGraphInterface for Custom Logic**  

	    If you need to exclude specific properties or perform custom math during serialization, have your UObject implement `IJsonObjectGraphInterface`. This allows you to override `OnPostSerialize` or `OnPreSerialize`, helping you **eliminate** redundant data like transient runtime timers from your saved JSON.

	 

	*   **Handle Circular References Safely**  

	    Standard JSON serializers often crash or recurse infinitely when Object A points to B and B points to A. `JsonObjectGraph` is explicitly designed to handle these loops by tracking already-processed objects, helping you **eliminate** stack overflow crashes in complex data structures.

	 

	*   **Combine with FJsonStructSerializerBackend**  

	    For maximum control, use the module in tandem with the `FJsonStructSerializerBackend`. This allows you to format the output with specific settings (like condensed vs. pretty-print), ensuring your data remains human-readable for debugging while staying compact for disk storage.

	 

	*   **Validate After Deserialization**  

	    When calling `FJsonObjectGraph::DeserializeObjectGraph`, always perform a validation pass on the resulting objects. Since JSON can be manually edited, this step helps you **eliminate** game-breaking bugs caused by missing references or invalid data types injected by a user.

	 

	*   **Optimize with Package Filtering**  

	    If your graph references large assets (like textures or meshes), ensure you configure the serializer to treat these as external references (by path) rather than trying to serialize the asset data itself. This helps you **eliminate** massive, bloated JSON files that would otherwise attempt to embed binary asset data.
Copy code
Preserve Object Identity with IDs
The module works by assigning a unique ID to every UObject in the graph. In the resulting JSON, object pointers are replaced by these IDs. This helps you eliminate “shallow copy” issues where deserializing a child would normally create a disconnected twin rather than pointing back to the original parent.
Use for Deep Serialization
When you need to save an entire “Actor and all its components” or a “Skill Tree made of many UObjects,” use FJsonObjectGraph::SerializeObjectGraph. This function traverses the graph starting from a root object, ensuring that every referenced object is captured in the JSON payload.
Implement IJsonObjectGraphInterface for Custom Logic
If you need to exclude specific properties or perform custom math during serialization, have your UObject implement IJsonObjectGraphInterface. This allows you to override OnPostSerialize or OnPreSerialize, helping you eliminate redundant data like transient runtime timers from your saved JSON.
Handle Circular References Safely
Standard JSON serializers often crash or recurse infinitely when Object A points to B and B points to A. JsonObjectGraph is explicitly designed to handle these loops by tracking already-processed objects, helping you eliminate stack overflow crashes in complex data structures.
Combine with FJsonStructSerializerBackend
For maximum control, use the module in tandem with the FJsonStructSerializerBackend. This allows you to format the output with specific settings (like condensed vs. pretty-print), ensuring your data remains human-readable for debugging while staying compact for disk storage.
Validate After Deserialization
When calling FJsonObjectGraph::DeserializeObjectGraph, always perform a validation pass on the resulting objects. Since JSON can be manually edited, this step helps you eliminate game-breaking bugs caused by missing references or invalid data types injected by a user.
Optimize with Package Filtering
If your graph references large assets (like textures or meshes), ensure you configure the serializer to treat these as external references (by path) rather than trying to serialize the asset data itself. This practice helps you eliminate massive, bloated JSON files that would otherwise attempt to embed binary asset data.