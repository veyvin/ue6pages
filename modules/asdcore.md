---
layout: default
title: ASDCore
---

<!-- ai-generation-failed -->

<h1>ASDCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Windows/ASDCore/ASDCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Unreal Engine that provides the data structures and foundational logic for managing Stage Data within the engine’s virtual production and cinematic pipelines. It is closely associated with the Stage Data ecosystem, which allows developers to synchronize and track the state of various assets and actors across a networked environment, such as a multi-user editing session or a live LED volume stage.

Its primary role is to provide a unified way to store, serialize, and replicate the properties of “staged” objects, ensuring that all participants in a production see the same asset configurations and transformations in real-time.

Practical Usage Tips and Best Practices
Implement Stage Data Containers
When building custom tools for virtual production, use the base classes provided by ASDCore to create your own stage data containers. This ensures that your custom properties—such as light intensity for a virtual shoot or “elimination” markers for a combat replay—are correctly tracked by the stage management system.
Configure Module Dependencies
To use ASDCore in your C++ project, add it to your Build.cs file. It is typically required when working with the Stage Monitor or custom LiveLink integrations.
C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "ASDCore", "StageDataCore" });
Copy code
Leverage for Multi-User Synchronization
Use the structures in ASDCore to define which properties should be synchronized during a Multi-User Editing session. By using the core stage data logic, you can ensure that changes to an actor’s state are propagated without manually writing complex replication code for every individual property.
Monitor Stage State via Stage Monitor
The ASDCore module provides the data backend that the Stage Monitor tool reads. If you are not seeing your data appear in the monitor, verify that your objects are correctly registered with the Stage Data Provider and that the ASDCore-defined structs are being populated.
Use for Versioned Asset Tracking
In high-stakes environments like live broadcasts, use ASDCore to track the “Asset Version” of staged actors. This allows you to “eliminate” the risk of different machines running different versions of a character or environment, which could lead to visual desynchronization.
Optimize via Delta Updates
The module is designed to handle frequent updates. When sending data through the ASDCore framework, prefer sending only the changed properties (deltas) rather than the entire state. This helps “eliminate” network congestion in bandwidth-sensitive environments like nDisplay clusters.
Integrate with Live Link
ASDCore can be used as a storage backend for Live Link data. If you are building a custom Live Link source, consider using ASDCore to archive the incoming data stream, allowing for easier playback and review of live performances later in Sequencer.
Validate Data via Stage Data Core Interfaces
Ensure your custom data types implement the necessary serialization interfaces defined in ASDCore. This allows the engine to automatically “eliminate” invalid data packets before they are processed by the stage management system, preventing potential crashes during live sessions.