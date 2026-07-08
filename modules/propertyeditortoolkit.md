---
layout: default
title: PropertyEditorToolkit
---

<!-- ai-generation-failed -->

<h1>PropertyEditorToolkit</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/PropertyEditorToolkit/PropertyEditorToolkit.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, EditorStyle, Engine, InputCore, PropertyEditor, PropertyPath, Slate, SlateCore, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

tools and interfaces necessary to create standalone property-editing windows and custom Details Panel experiences. While the PropertyEditor module handles the high-level registration of customizations, PropertyEditorToolkit contains the actual implementation logic for the widgets (like IDetailsView) and the utilities that allow you to programmatically generate or manipulate property rows outside of the standard inspector.

It is primarily used by tools developers to build custom Editor Windows that need to display object properties in a searchable, filterable, and UI-consistent manner. By leveraging this module, you can eliminate the need to write complex Slate code for every individual variable, instead relying on the engine’s reflection system to auto-generate the interface.

Practical Usage Tips and Best Practices
Use IPropertyRowGenerator for Custom Lists
If you need to display a specific list of properties without the overhead of a full IDetailsView widget, use IPropertyRowGenerator. This allows you to generate Slate widgets for a specific subset of properties, helping you eliminate UI clutter in specialized tool windows.
Force UI Refreshes via IPropertyUtilities
When your C++ code modifies a property in a way that the editor doesn’t immediately detect, use IPropertyUtilities::ForceRefresh(). This utility ensures the UI stays synchronized with the underlying data, helping you eliminate “stale” values where the screen doesn’t match the actual variable state.
Implement ‘Reset to Default’ Logic
Always ensure your custom property widgets support the “Reset to Default” yellow arrow. You can do this by utilizing the CreateDefaultPropertyWidget() method on your property handles. Providing this standard behavior helps you eliminate UX friction for artists who expect consistent behavior across all tools.
Avoid Raw Pointers for Property Handles
Always store references to properties as TSharedPtr<IPropertyHandle>. These handles are part of a reference-counted system; using raw pointers can lead to crashes if the details panel is rebuilt or the object is garbage collected. Using shared pointers helps you eliminate memory access violations.
Leverage EditCondition Metadata
Use the EditCondition metadata specifier in your UPROPERTY declarations (e.g., meta = (EditCondition = "bIsActive")). The PropertyEditorToolkit automatically handles the graying out or hiding of rows based on these conditions, which helps you eliminate complex manual visibility logic in your C++ code.
Use AddExternalObjectProperty for Composite Views
You can use IDetailLayoutBuilder::AddExternalObjectProperty to display properties from an object other than the one currently being inspected. This is useful for “Global Settings” windows, helping you eliminate the need for the user to click back and forth between different assets.
Throttle Updates for High-Frequency Data
If your tool displays data that changes every frame (like a real-time transform), don’t refresh the entire panel every tick. Use a timer or only refresh on interaction. This practice helps you eliminate editor “hitchiness” caused by excessive Slate rebuilding.
Unregister Cleanly on Module Elimination
When your editor module is shut down (the “elimination” of the module during a hot-reload or exit), ensure you call UnregisterCustomClassLayout. Failing to unregister customizations will cause the editor to point to deleted memory, which you must eliminate to ensure editor stability.