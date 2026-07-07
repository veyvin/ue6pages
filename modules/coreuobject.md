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

the “Unreal-aware” logic that allows classes to be seen by Blueprints and the Editor.

Every class that uses the UCLASS macro and every property using UPROPERTY relies on this module to function within the engine’s managed memory environment.

Practical Usage Tips and Best Practices
1. Always Use UPROPERTY() for Object Pointers

The Garbage Collector only tracks UObject pointers that are marked with the UPROPERTY() macro. If you store a raw pointer to a UObject without this macro, the engine will eventually trigger the elimination of that object from memory, leaving you with a “dangling pointer” that will cause a crash when accessed.

2. Master the Use of Cast<T>

Because CoreUObject handles runtime type information (RTTI), you should use the templated Cast<T>() function for downcasting. This is a safe cast; if the object is not of the target type (or is null), it returns nullptr. This ensures the elimination of “hard crashes” associated with traditional C-style casts.

3. Use TWeakObjectPtr for Non-Owning References

To reference an object without preventing it from being garbage collected, use TWeakObjectPtr<T>. This is essential for preventing memory leaks. Before using a weak pointer, always check .IsValid() to ensure the object hasn’t undergone elimination by the GC system.

4. Understand the Class Default Object (CDO)

Every UClass has a CDO—a master copy of the object used as a template. When you use the constructor to set default values, you are actually modifying the CDO. At runtime, when you spawn a new instance, the engine copies the values from the CDO, which facilitates the elimination of expensive initialization logic for every new actor.

5. Leverage NewObject<T> for Instantion

Unlike standard C++ new, you must use NewObject<T>() to create instances of UObject-derived classes. This registers the object with the reflection system and the Garbage Collector. For Actors, you use SpawnActor, but for data objects or components, NewObject is the required standard for proper lifecycle management.

6. Minimize Logic in Constructors

The constructor of a UObject is called when the engine is creating the CDO (often at startup). Avoid complex logic or world-dependent calls here. Instead, use PostInitProperties() or BeginPlay() for setup logic. This prevents the elimination of editor stability caused by constructors trying to access systems that aren’t loaded yet.

7. Use FSoftObjectPath for Lazy Loading

To avoid loading massive assets (like high-res textures) into memory immediately, use TSoftObjectPtr or FSoftObjectPath. These are part of the CoreUObject system and allow you to load assets only when they are needed, which is vital for the elimination of “out of memory” errors in large projects.

8. Verify Module Dependencies

If you are writing a custom C++ module, you almost always need to include CoreUObject in your Build.cs file. If you see errors about UObject or GENERATED_BODY being undefined, it is usually because this module is missing from your dependency list:

C#
PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject" });
Copy code