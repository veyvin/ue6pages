---
layout: default
title: SblCore
---

<!-- ai-generation-failed -->

<h1>SblCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/SwitchboardListener/SblCore/SblCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, JWT, Json, JsonUtilities, MsQuic, MsQuicRuntime, NVAPI, Networking, NvmlWrapper, Projects, Public, SwitchboardCommon, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

cused module that provides the foundational logic for the State Tree and Smart Objects systems in Unreal Engine. It is designed to handle high-performance, data-driven logic by providing a “Blackboard” system that is more efficient than the traditional Behavior Tree Blackboards.

This module is used primarily for managing shared data between different states in a State Tree or for passing context to Smart Objects. By using SBLCore, you can eliminate the performance overhead associated with object-based data lookups, as it uses a compact memory layout to store and access properties.

Practical Usage Tips and Best Practices
Integrate with State Trees
Use SBLCore when defining the data schema for your State Tree Assets. It acts as the “memory” for the tree. By defining your variables here, you ensure that tasks and conditions can share data seamlessly, which helps you eliminate redundant calculations across different states.
Prefer Structs for Performance
SBLCore is optimized for handling USTRUCT data. When passing data to a State Tree or Smart Object, wrap your variables in a struct. This flat memory layout helps the engine eliminate pointer-chasing and cache misses during high-frequency AI evaluations.
Use Property Binding over Casting
The SBL system relies on Property Bindings to link data between the Blackboard and the Tasks. Instead of casting to a specific Actor or Component inside your logic, bind the property directly in the Editor. This practice helps you eliminate hard dependencies and makes your logic more modular.
Leverage Schema Validation
Every SBL-based system requires a Schema (e.g., UStateTreeSchema). Ensure your schema explicitly defines what data is “required” versus “optional.” This helps the compiler eliminate runtime errors by catching missing data references during the “Compile” phase of the State Tree.
Limit Blackboard Size for MassEntity
If you are using SBLCore in conjunction with MassEntity (for large-scale crowds), keep your blackboard data as small as possible. Since this data is replicated or processed for thousands of entities, minimizing the byte count per agent helps you eliminate memory bloat and CPU bottlenecks.
Debug via the State Tree Debugger
Use the State Tree Debugger to visualize the values stored in the SBLCore buffers during runtime. This allows you to see exactly when a value changes, helping you eliminate logic bugs where a state transition fails because of an unexpected variable value.
Utilize ‘External Data’ References
SBLCore allows you to reference “External Data” (like a USkeletalMeshComponent). Use this to provide context to your AI without duplicating the data. This helps you eliminate memory synchronization issues, as the Blackboard simply points to the source of truth.
Clear Transient Data on State Elimination
When a state is exited (the “elimination” of that logic block), ensure that transient blackboard data is reset if it shouldn’t persist. This prevents “stale” data from leaking into the next state, which helps you eliminate unpredictable AI behavior during complex transitions.