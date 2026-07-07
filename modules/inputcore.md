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

are abstraction layer for user input. It defines the core data structures and identifiers for physical input devices, such as the FKey type and the EKeys enumeration.

While higher-level systems like Enhanced Input handle the logic of “Actions” and “Contexts,” InputCore is responsible for the literal representation of keys (e.g., EKeys::W, EKeys::LeftMouseButton, or EKeys::Gamepad_FaceButton_Bottom). It provides the bridge between raw hardware signals and the engine’s gameplay framework.

Practical Usage Tips and Best Practices
1. Add the Module Dependency

Because InputCore is a foundational module, it is often required whenever you reference a specific key in C++.

Action: Ensure "InputCore" is included in your PublicDependencyModuleNames within your project’s .Build.cs file. This is the most common cause of “unresolved external symbol” errors when referencing EKeys, and adding it will eliminate linker issues.
2. Use FKey for Dynamic Key References

When building UI or settings menus where a user can rebind keys, do not store keys as strings or integers.

Best Practice: Always use the FKey struct. It is a lightweight wrapper that handles serialization, display names, and icon lookups automatically. Using FKey helps you eliminate brittle string-matching logic in your input-remapping systems.
3. Leverage EKeys for Hardware-Specific Logic

Sometimes you need to check for a specific physical key press regardless of the “Action” assigned to it (e.g., for a “Press Any Key” screen).

Tip: Use EKeys::AnyKey in your input listeners. This allows the engine to detect a signal from any device (keyboard, mouse, or gamepad) simultaneously, eliminating the need to write separate checks for every possible hardware input.
4. Display Icon-Friendly Names

InputCore provides built-in functions to get human-readable names for keys.

Action: Call MyFKey.GetDisplayName() to get a localized string for the UI (e.g., “Left Ctrl” instead of “LeftControl”). This ensures your interface is professional and user-friendly while eliminating the need for manual translation tables for every key.
5. Differentiate Between Key and Axis

Some FKey entries represent digital buttons (on/off), while others represent analog axes (0.0 to 1.0).

Tip: Use MyFKey.IsMouseButton() or MyFKey.IsGamepadKey() to filter inputs in your code. Checking the key’s properties via InputCore helps you eliminate logic errors where a mouse-move event accidentally triggers code intended only for button presses.
6. Use for UI-Only Input Handling

In some cases, you may want UI widgets to respond to specific keys (like “Escape” to close a menu) without creating a formal Input Action.

Action: Override NativeOnKeyDown in your C++ UserWidget and compare the InKeyEvent.GetKey() against EKeys::Escape. This provides a fast path for menu navigation and eliminates the overhead of the Enhanced Input system for simple UI interactions.
7. Prefer Enhanced Input for Gameplay

While InputCore is powerful, it should not be used for primary gameplay movement or combat logic.

Best Practice: Use InputCore only to define the mappings inside an Input Mapping Context (IMC). Let the Enhanced Input module handle the actual triggering and modifiers. This separation helps you eliminate “hard-coded” controls, making it easier to support multiple platforms.
8. Verify Platform Compatibility

Not all keys defined in EKeys exist on all platforms (e.g., there is no EKeys::MiddleMouseButton on a standard console controller).

Tip: If you are writing platform-specific code, use #if PLATFORM_WINDOWS or similar macros around specific EKeys references. This helps you eliminate compilation errors when packaging for consoles or mobile devices that lack specific hardware inputs.