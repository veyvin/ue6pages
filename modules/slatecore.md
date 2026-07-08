---
layout: default
title: SlateCore
---

<!-- ai-generation-failed -->

<h1>SlateCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/SlateCore/SlateCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, DeveloperSettings, InputCore, Json, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

work. While the Slate module provides the actual widget library (buttons, checkboxes, etc.), SlateCore defines the essential architecture: the base SWidget class, the layout system (geometry and alignment), input event handling, styling structures, and the rendering primitives.

It is used to define how UI elements occupy space and interact with the engine’s core systems. Mastering SlateCore is necessary for developers building high-performance custom widgets or deep editor extensions, as it allows you to eliminate the overhead of the UMG wrapper when building complex, data-heavy tools.

Practical Usage Tips and Best Practices
Separate Module Dependencies
In your .Build.cs file, always list "Slate" and "SlateCore" separately. While they are often used together, keeping them distinct helps the Unreal Build Tool (UBT) optimize dependency graphs. This practice helps you eliminate compilation ambiguity in cross-module editor projects.
Master the Two-Pass Layout System
SlateCore uses a two-pass system: ComputeDesiredSize (bottom-up) and OnArrangeChildren (top-down). Ensure your custom widgets calculate their size accurately in the first pass to eliminate layout flickering or “popping” when the UI is resized or updated.
Use FReply to Manage Input Flow
Every input event (like OnMouseButtonDown) returns an FReply. Use FReply::Handled() to stop an event from bubbling up to parent widgets or FReply::Unhandled() to let it pass through. This precision helps you eliminate “input leakage” where clicking a button accidentally triggers an action in the viewport behind it.
Leverage SInvalidationPanel for Performance
Slate can be CPU-intensive if the entire hierarchy ticks every frame. Wrap complex, static UI sections in an SInvalidationPanel. This module then caches the widget’s visual state, helping you eliminate redundant paint calls and significantly reducing the “Slate Tick” time in the profiler.
Prefer Slate Attributes (TAttribute) over Polling
Instead of manually updating a text field every frame, bind it to a TAttribute. This allows the widget to pull data only when needed or via a delegate. Using attributes helps you eliminate “hard-coded” logic and ensures the UI stays synchronized with the underlying data model automatically.
Utilize FGeometry for Coordinate Conversion
When handling mouse positions or drag-and-drop, always use the FGeometry provided in the event. Its functions, like AbsoluteToLocal, are the only reliable way to handle high-DPI scaling. Using these native functions helps you eliminate coordinate offset bugs on 4K monitors or non-standard aspect ratios.
Optimize Styling with FSlotBase
When creating container widgets (like boxes or grids), use FSlotBase to manage child padding and alignment. Centralizing these properties within the slot architecture helps you eliminate “magic numbers” in your C++ code, making the UI easier to theme and maintain.
Unregister Delegates on Widget Elimination
When a widget is destroyed (the “elimination” of the UI element), ensure any active STimer or global delegates it registered are cleared. Because Slate widgets are managed by TSharedPtr rather than Garbage Collection, failing to unbind delegates can lead to memory leaks or “dangling pointer” crashes that you must eliminate for a stable editor experience.