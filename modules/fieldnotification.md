---
layout: default
title: FieldNotification
---

<!-- ai-generation-failed -->

<h1>FieldNotification</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/FieldNotification/FieldNotification.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

d to notify listeners when specific properties or “fields” within a class have changed.

Description and Purpose

This module introduces the INotifyFieldValueChanged interface and the underlying infrastructure for Unreal Engine’s Model-View-ViewModel (MVVM) pattern. Unlike traditional delegates, which can be memory-heavy when scaled, FieldNotification uses a Field ID system (based on bitmasks or indices) to broadcast changes. Its primary purpose is to drive reactive UI—allowing UMG widgets to “bind” to properties in C++ and update only when the data actually changes. This architecture is essential for creating complex, data-driven interfaces while maintaining high performance.

Practical Usage Tips and Best Practices
Derive from UMVVMViewModelBase
While you can implement the interface manually, it is best practice to derive your classes from UMVVMViewModelBase. This class provides a robust default implementation of the system and built-in macros that eliminate the need to manage your own field ID lists and bitmasks.
Use the FieldNotify Specifier
Mark your properties with the FieldNotify specifier inside the UPROPERTY macro. This registers the variable with the notification system. To maintain data integrity, combine this with a custom Setter function to ensure that any modification to the value also triggers the required notification.
Leverage Setter Macros for Efficiency
Use the UE_MVVM_SET_PROPERTY_VALUE macro inside your C++ setter functions. This macro automatically performs an equality check; it will only update the value and broadcast the change if the new value is different from the old one. This helps eliminate redundant UI refreshes and unnecessary logic execution.
Implement “Computed” Fields with Functions
You can mark a UFUNCTION as a FieldNotify (it must be const, return a single value, and take no arguments). This is useful for UI elements that depend on multiple variables—for example, a “Health Bar Color” function that depends on a “Health” integer. When the health changes, you manually notify the function’s ID to eliminate out-of-date visual states.
Batch Notifications with FieldIDs
If you are updating multiple related properties at once (e.g., loading a full character profile), you can broadcast multiple field IDs in a single pass. This is more efficient than firing individual delegates and helps eliminate “partial state” flickers where the UI updates some elements before others are ready.
Add Necessary Module Dependencies
To use these features in C++, you must add "FieldNotification" and "ModelViewViewModel" to your PublicDependencyModuleNames in the project’s .Build.cs file. Forgetting these dependencies will eliminate your ability to compile code referencing the FieldNotify macros or base classes.
Prioritize for Discrete State Changes
FieldNotification is best suited for state changes like Health, Ammo, or Gold. For high-frequency data that changes every frame (like a character’s exact world position), traditional “Tick” or specialized HUD code is often better. Using notifications for per-frame variables can eliminate the performance benefits the system was designed to provide.
Validate UI Bindings in the Editor
Use the View Binding panel in UMG to verify that your C++ fields are correctly exposed. If a field does not appear, check that it is marked BlueprintReadOnly or BlueprintReadWrite. Proper exposure will eliminate debugging time spent wondering why the UI isn’t reacting to gameplay events, such as a character elimination.