---
layout: default
title: CoreUObject
---

<!-- ai-generation-failed -->

<h1>CoreUObject</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/CoreUObject/CoreUObject.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AutoRTFM, Core, CorePreciseFP, DerivedDataCache, Json, Projects, TraceLog, libpas</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

tem. While the Core module provides basic C++ utilities (like strings and containers), CoreUObject introduces the UObject Ecosystem. This includes the reflection system, garbage collection (GC), metadata, serialization, and the class hierarchy (UClass).

Without this module, Unreal would just be a standard C++ library. CoreUObject allows the engine to “know” about your classes at runtime, enabling features like the Details Panel in the Editor, Blueprint visual scripting, and automatic memory management.

Practical Usage Tips and Best Practices
1. Always Use UPROPERTY() for UObject Pointers

To ensure the elimination of memory leaks and “dangling pointers,” any pointer to a UObject-derived class must be marked with the UPROPERTY() macro. This registers the reference with the Garbage Collector. If you fail to do this, the GC may delete the object while you are still using it, leading to a crash.

2. Master NewObject and CreateDefaultSubobject

Never use the standard C++ new keyword for UObjects. Use NewObject<T>() for creating objects at runtime. For components or subobjects created within a class constructor, use CreateDefaultSubobject<T>(). This ensures the object is correctly registered within the CoreUObject hierarchy and the elimination of manual memory tracking.

3. Understand the Class Default Object (CDO)

Every UClass has a CDO—a master copy of the object created at startup. When you change a default value in a constructor, you are changing the CDO. Accessing the CDO via GetClass()->GetDefaultObject() is an efficient way to check default properties without spawning a new instance, assisting in the elimination of unnecessary memory allocation.

4. Use Weak Object Pointers for Non-Owners

If a class needs to reference an object but shouldn’t “own” it (preventing it from being garbage collected), use TWeakObjectPtr<T>. This allows the referenced object to be deleted if nothing else is holding it, and you can safely check IsValid() before use. This is vital for the elimination of circular dependencies.

5. Minimize UObject Count for GC Performance

Garbage collection performs a “Reachability Analysis” by walking through all UObjects. Having millions of tiny UObjects can cause frame-rate hitches when the GC runs. For small, high-frequency data (like inventory items or math coordinates), use USTRUCTs instead of UObjects to assist in the elimination of GC overhead.

6. Leverage IsValid() Over Null Checks

When checking if a UObject pointer is safe to use, prefer IsValid(MyObject) over if (MyObject != nullptr). IsValid checks both that the pointer is not null AND that the object is not currently “Pending Kill” (marked for elimination). This prevents accessing objects that are halfway through the destruction process.

7. Utilize the Reflection System for Generic Logic

CoreUObject allows you to iterate over properties of a class at runtime using TFieldIterator<FProperty>. This is powerful for building automated tools, such as a system that automatically logs all variables in a class for debugging, leading to the elimination of tedious manual logging code.

8. Use Data Assets for Constant Data

If you have a UObject that only stores data (like weapon stats), derive it from UDataAsset. These are handled efficiently by the CoreUObject system and the Editor, allowing designers to tweak values without touching code, which facilitates the elimination of hard-coded magic numbers.