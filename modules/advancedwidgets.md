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

t provides specialized UI components and layout logic extending the standard Slate and UMG palettes. It is primarily used to solve specific UX challenges—such as circular layouts, segmented progress tracking, and high-density text displays—that would otherwise require complex custom materials or manual math.

Practical Usage Tips & Best Practices
1. Add Module Dependency in C++

To access AdvancedWidgets classes (like URadialBox) in C++, you must explicitly include the module in your project’s Build.cs file. It is a runtime module, so it belongs in your private or public dependencies.

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { 

	    "Core", 

	    "CoreUObject", 

	    "Engine", 

	    "InputCore", 

	    "AdvancedWidgets" // Add this line

	});

	```

	 

	#### 2. Mastering Radial Box Layouts

	The `URadialBox` relies on `FRadialBoxSettings`. Instead of setting positions manually, use these settings to control the **Starting Angle**, **Total Angle**, and whether items should **Distribute Evenly**.

	*   *Tip*: A "Starting Angle" of 0 typically points to the right (3 o'clock). Set it to -90 to start at the top.

	 

	#### 3. Use Sectional Progress Bars for "Pips"

	Instead of creating 10 individual images for a 10-segment health bar, use `USectionalProgressBar`. 

	*   **Best Practice**: Use the `SectionCount` property to define segments and adjust the `FillEdgePadding` to ensure the progress bar looks correct when partially filled.

	 

	#### 4. Slate Construction Pattern

	When creating an `SRadialBox` in C++, use the declarative syntax. Remember that child widgets are added to slots just like a `SVerticalBox`, but their position is determined by the Radial Box's internal math.

	 

	```cpp

	#include "Widgets/Layout/SRadialBox.h"

	 

	ChildSlot

	[

	    SNew(SRadialBox)

	    .StartingAngle(-90.0f)

	    .bDistributeEvenly(true)

	    + SRadialBox::Slot()

	    [

	        SNew(SButton) // This button will appear at the top

	    ]

	];

	```

	 

	#### 5. Performance of Radial Layouts

	The Radial Box calculates the geometry of its children every time the layout is dirtied (e.g., when a child is added or the angle changes). While efficient, avoid animating the "Starting Angle" or "Total Angle" every frame via C++ unless necessary; try to handle rotation via a **Render Transform** on the widget itself for better performance.

	 

	#### 6. Coordinate with Materials

	For `USectionalProgressBar`, the visual "split" between segments is often driven by the widget's style. Ensure your `WidgetStyle` (specifically the `BackgroundBarImage` and `FillBarImage`) uses a **Box** or **Border** draw type with appropriate margins to prevent the segments from looking stretched.

	 

	#### 7. Verify Module Availability

	Since `AdvancedWidgets` is a separate module, if you are developing a **Plugin**, ensure your `.uplugin` file also lists `AdvancedWidgets` in the `Plugins` or `Modules` dependency section to ensure it loads correctly in the Editor and packaged builds.

	 

	#### 8. Blueprint Integration

	If you only need these widgets in UMG, you don't need C++ code. Once the module is linked (or if the engine version includes it by default), search for "Radial Box" in the UMG Palette. If it’s missing, ensure the **Advanced Widgets Plugin** is enabled in the **Edit > Plugins** menu.
Copy code
2. Configure Radial Box Layouts

The Radial Box (URadialBox) is ideal for weapon wheels or circular inventory menus. Instead of manually positioning children, use the Starting Angle and Total Angle properties.

Best Practice: A “Starting Angle” of -90 points to the top (12 o’clock). Use “Distribute Evenly” to ensure gaps remain consistent as you add or remove items.
3. Use Sectional Progress Bars for Health Pips

The Sectional Progress Bar (USectionalProgressBar) allows you to divide a bar into discrete segments (pips). This is significantly more efficient than spawning individual image widgets for a segmented health or energy bar.

Tip: Use the SectionCount property to define how many pips exist and adjust the FillEdgePadding to ensure the progress indicator doesn’t overlap the segment borders.
4. Leverage Slate Declarative Syntax

When working in C++, the Slate version (SRadialBox) follows the standard declarative pattern. This allows you to build complex circular UI hierarchies quickly without the overhead of the UMG designer.

C++
	#include "Widgets/Layout/SRadialBox.h"

	 

	ChildSlot

	[

	    SNew(SRadialBox)

	    .StartingAngle(-90.0f)

	    .bDistributeEvenly(true)

	    + SRadialBox::Slot()

	    [

	        SNew(SButton) // Automatically positioned by the RadialBox

	    ]

	];
Copy code
5. Animate via Render Transforms

While you can animate properties like StartingAngle in the Radial Box, doing so forces a layout recalculation for all children.

Performance Tip: If you want to spin a weapon wheel, it is often more performant to apply a Render Transform (Rotation) to the entire Radial Box widget rather than updating the layout-driving angle property every frame.
6. Coordinate Styles with Materials

For widgets like the Sectional Progress Bar, ensure your WidgetStyle (specifically the Background and Fill images) uses the Box or Border draw type. This prevents the “pips” from looking stretched or distorted when the bar is resized.

7. Combine with Common UI

AdvancedWidgets work seamlessly with the Common UI plugin. You can place a CommonButton inside a RadialBox to get high-end gamepad navigation and circular layouts simultaneously, which is the standard approach for modern console “radial menus.”

8. Ensure Plugin Activation

If you cannot find the Radial Box or Sectional Progress Bar in the UMG Designer palette, go to Edit > Plugins and ensure the Advanced Widgets plugin is enabled. Although it is a module, it is often packaged as a built-in engine plugin that must be active for the widgets to appear in the editor.