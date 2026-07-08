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

e’s input system. While higher-level plugins like “Enhanced Input” handle complex mapping and logic, InputCore defines the low-level constants and structures that represent physical hardware—such as keys, mouse buttons, gamepad triggers, and touch gestures.

Its primary purpose is to provide the FKey structure and the EKeys namespace. These allow the engine to identify what was pressed before higher-level systems decide what it does. Using this module helps eliminate the need for platform-specific hardware code in your gameplay logic.

Practical Usage Tips and Best Practices
Include in Build.cs for C++ Projects
To use input constants (like EKeys::W) in your C++ classes, you must add the module to your [ProjectName].Build.cs file. It is typically added to PublicDependencyModuleNames so your headers can safely reference FKey.
C++
	    // MyProject.Build.cs

	    PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore" });

	    ```

	 

	*   **Use FKey for Universal Input References**  

	    In C++, avoid using strings or integers to represent keys. Always use `FKey`. It is a reflected struct that handles everything from serialization to displaying the correct localized key name (e.g., "Space Bar") in the UI.

	 

	*   **Reference Keys via EKeys Namespace**  

	    When you need to check for a specific hardware key in code, use the `EKeys` namespace. This helps **eliminate** magic strings and ensures your code is platform-agnostic for common inputs.

	    ```cpp

	    #include "InputCoreTypes.h"

	 

	    if (MyFKey == EKeys::LeftMouseButton) { /* ... */ }

	    ```

	 

	*   **Identify Input Types (IsGamepad, IsMouseButton)**  

	    `FKey` contains built-in helper methods to identify the source of an input. Use `MyKey.IsGamepadKey()` or `MyKey.IsMouseButton()` to **eliminate** complex switch statements when you need to change UI icons based on the last used device.

	 

	*   **Handle 'AnyKey' for Generic Interaction**  

	    The module defines a special constant `EKeys::AnyKey`. This is highly useful for "Press any key to start" screens or global input listeners. It allows you to **eliminate** the need to manually check every possible keyboard and gamepad button.

	 

	*   **Access Localized Key Names**  

	    To display a key name to the user (e.g., in a "Press [Key] to Open" prompt), use `MyKey.GetDisplayName()`. This returns an `FText` that is automatically localized and correctly formatted by the **ICU** module, helping you **eliminate** hard-coded English strings.

	 

	*   **Leverage Platform-Specific Keys**  

	    The `InputCore` module includes definitions for platform-specific hardware, such as the `PS4_` or `XboxOne_` prefixes for console-specific buttons. Using these within `#if PLATFORM_` blocks helps you **eliminate** input logic errors when porting your game to different consoles.

	 

	*   **Use in UI with InputKeySelector**  

	    If you are building a key-binding menu in UMG, the `UInputKeySelector` widget relies directly on the `InputCore` types. Understanding the underlying `FKey` behavior allows you to more effectively filter which keys are "mappable" (e.g., **eliminating** the Windows Key or Escape from being rebound).
Copy code
Reference Keys via EKeys Namespace
When you need to check for a specific hardware key in code, always use the EKeys namespace. This ensures your code remains platform-agnostic and helps eliminate “magic strings” or hard-coded integers that are difficult to maintain.
Identify Input Sources (Gamepad vs. Mouse)
The FKey struct contains built-in helper methods to identify the source of an input. Use MyKey.IsGamepadKey() or MyKey.IsMouseButton() to eliminate complex switch statements when you need to change UI icons dynamically based on the last used device.
Use for “Press Any Key” Logic
The module defines a special constant EKeys::AnyKey. This is highly useful for title screens or global listeners. Using this helps you eliminate the tedious task of manually checking every possible keyboard and gamepad button for a simple interaction.
Access Localized Display Names
To display a key name to the user (e.g., in a “Press [Key] to Open” prompt), use MyKey.GetDisplayName(). This returns an FText that is automatically localized and correctly formatted by the engine, helping you eliminate the risk of displaying unreadable raw key codes.
Handle Platform-Specific Keys
The InputCore module includes definitions for specialized hardware, such as the PS4_ or XboxOne_ prefixes for console-specific buttons. Using these within #if PLATFORM_ blocks helps you eliminate input logic errors when porting your game to different hardware.
Filter Mappable Keys in UI
If you are building a key-binding menu in UMG, the UInputKeySelector widget relies directly on InputCore types. Understanding FKey properties allows you to filter which keys are “mappable,” helping you eliminate the ability for players to accidentally bind critical system keys like Escape or the Windows Key.
Leverage for Debugging Input
You can use FKey::ToString() to log the name of a key during development. This is an effective way to eliminate confusion when debugging custom input hardware or complex chorded actions.