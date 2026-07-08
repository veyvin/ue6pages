---
layout: default
title: AdvancedWidgets
---

<!-- ai-generation-failed -->

<h1>AdvancedWidgets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AdvancedWidgets/AdvancedWidgets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, InputCore, PropertyEditor, Slate, SlateCore, UMG, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

s specialized, high-functionality UI components beyond the standard UMG set. While standard widgets handle basic layouts, AdvancedWidgets offers complex controls like radial sliders and color gradient pickers, bridging the gap between basic UI and professional-grade creative tools.

Description

The module is used to provide sophisticated interaction methods, primarily for tools, editors, or gameplay systems requiring fine-tuned input (such as character creators or photo modes). It contains both Slate (C++) and UMG (Blueprint) versions of its components, making it versatile for both engine-level tools and in-game interfaces.

Practical Usage Tips and Best Practices
1. Configure Module Dependencies

To use these widgets in C++, you must add the module to your *.Build.cs file. Unlike the core UMG module, this is not included by default in most templates.

C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "UMG", "AdvancedWidgets" });
Copy code
2. Utilize the Radial Slider for Compact Input

The URadialSlider is the standout component of this module. It is significantly more space-efficient than a horizontal slider for “dial-style” inputs. Use it for properties like “Rotation” or “Volume” where a circular metaphor is more intuitive for the user.

3. Implement the Color Gradient Picker

The module includes the SColorGradientPicker (Slate) and its UMG wrapper. This is essential for features like dynamic sky systems or particle color over time. It allows users to define multiple color stops and interpolation types, which is far more powerful than a simple single-color picker.

4. Leverage Slate Brushes for Custom Styling

Advanced Widgets rely heavily on FSlateBrush for their visual identity (e.g., the “knob” or “track” of a radial slider). To maintain a consistent UI, create a Slate Widget Style Asset in the Editor to store your brushes and colors, rather than hard-coding them into individual widget instances.

5. Optimization: Avoid High-Frequency Binding

Widgets like the Radial Slider often trigger updates every frame during user interaction. Instead of using “Property Binding” (the dropdown menu next to a value in UMG), use Event-Based Updates. Bind logic to the OnValueChanged delegate to eliminate unnecessary overhead during the UI tick.

6. Use Sparse Class Data for Tooling

If you are building editor-facing tools using these widgets, take advantage of the module’s support for sparse data structures. This helps keep the memory footprint low when you have many instances of complex widgets that share the same default styling or configuration.

7. Combine with Common UI

For cross-platform projects, wrap your AdvancedWidgets inside Common UI containers. While AdvancedWidgets provide the “control logic,” Common UI provides the navigation and focus management required for gamepad and console support, ensuring your radial sliders are accessible to all input methods.

8. Debugging with the Widget Reflector

Because AdvancedWidgets have complex internal hierarchies (especially the gradient picker), use the Widget Reflector (Ctrl+Shift+W) to inspect the slot padding and alignment. This is the fastest way to troubleshoot why a radial slider might be clipping or why a gradient stop is not responding to click events.