---
layout: default
title: InputCore
---

<!-- ai-generation-failed -->

<h1>InputCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/InputCore/InputCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

user input. It provides the base definitions for all hardware input sources, including keyboard keys, mouse buttons, gamepad triggers, and touch gestures.

While the Enhanced Input module handles the high-level logic (how actions map to players), InputCore provides the low-level constants (EKeys) and types (FKey) that represent the physical buttons themselves. Its primary purpose is to “eliminate” the need for hardcoded strings or platform-specific scan codes when identifying user input.

Practical Usage Tips and Best Practices
Always Add to Public Dependencies
Almost every gameplay-related module will require InputCore. Ensure "InputCore" is in the PublicDependencyModuleNames of your Build.cs. This “eliminates” the common unresolved external symbol error when trying to use EKeys or FKey in your header files.
Prefer FKey Over Strings
When storing an input reference in a variable, always use the FKey struct. This “eliminates” errors caused by typos in string-based comparisons and allows the variable to be picked from a convenient searchable dropdown in the Unreal Editor Details panel.
Leverage EKeys for Native Comparison
Use the EKeys namespace for direct hardware checks. For example, if (Key == EKeys::LeftMouseButton) is more performant than string-based logic and “eliminates” ambiguity between different input devices.
Utilize Key Metadata for UI
The FKey struct contains methods like GetDisplayName(). Use this to “eliminate” the need for custom lookup tables when building a settings menu; it automatically provides a localized string (e.g., “Left Shift”) for the key assigned by the player.
Check Input Categories
InputCore defines categories for keys (e.g., IsGamepadKey(), IsMouseButton()). Use these to “eliminate” logic errors when building “Press any key to continue” screens—you can easily filter out mouse movement or touch events while only listening for physical button presses.
Use IsBindable() to Filter Lists
If you are creating a custom key-binding widget, use the FKey::IsBindable() check. This “eliminates” the risk of players trying to bind “Eliminate” actions to reserved keys like the Escape key or system-level inputs that the engine cannot safely override.
Handle Virtual Keyboards
InputCore is responsible for the bridge to virtual keyboards on mobile and console. Use the types defined here to “eliminate” platform-specific code when checking if a hardware keyboard is present or if the software keyboard is currently active.
Avoid Overriding InputCore for Custom Hardware
If you are adding support for a non-standard device (like a specialized flight stick), do not modify InputCore directly. Instead, register your new keys with the IInputDevice interface in a separate plugin. This “eliminates” the need for a custom engine fork while still making your new hardware keys available throughout the engine.