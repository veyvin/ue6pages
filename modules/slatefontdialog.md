---
layout: default
title: SlateFontDialog
---

<!-- ai-generation-failed -->

<h1>SlateFontDialog</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/SlateFontDialog/SlateFontDialog.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AppFramework, Core, CoreUObject, InputCore, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

zed, Slate-based interface for selecting and configuring font assets and properties.

Description and Purpose

This module serves as the primary C++ bridge for spawning the Font Picker window within the Unreal Editor. It provides a consistent UI (SFontDialog) that allows users to browse through available font families, select specific typefaces (Regular, Bold, Italic), and adjust sizing or styling parameters. Its primary purpose is to provide a unified experience for tools that require font input—such as UI designers, text-based localization tools, or custom editor extensions. By using this module, developers can eliminate the need to build a custom file browser or property list just to let a user choose a font, as it handles the logic of scanning the project’s font assets automatically.

Practical Usage Tips and Best Practices
Implement as a Modal Dialog
When calling the font dialog, it is best practice to spawn it as a Modal Window. This forces the user to complete their selection or cancel before returning to the main editor, which helps eliminate state conflicts where a font might be changed while another tool is attempting to use it.
Add “Slate” and “SlateCore” Dependencies
Since this module is built on the Slate framework, you must include "Slate", "SlateCore", and "SlateFontDialog" in your module’s PrivateDependencyModuleNames inside your .Build.cs file. Ensuring these are present will eliminate linker errors during compilation.
Check for Editor-Only Context
The SlateFontDialog is intended strictly for use within the Unreal Editor. Always wrap your calls to this module in #if WITH_EDITOR blocks to ensure that the code is eliminated from packaged game builds, as the dialog will not function (and will cause crashes) in a runtime environment.
Handle Null Selections Gracefully
Users often close the dialog without making a selection or by clicking “Cancel.” Always check the return value or the validity of the selected font object before applying it to your settings. This helps you eliminate null-pointer exceptions in your custom editor tools.
Use for Custom Editor Utility Widgets
If you are building an Editor Utility Widget (EUW) for a localization or UI overhaul tool, you can expose a button that triggers the C++ font dialog. This provides a more “native” feel than a simple dropdown menu, helping you eliminate friction for artists who are used to standard Windows or macOS font pickers.
Filter Font Types via Options
The dialog can be configured to show only certain types of fonts. If your tool specifically requires a Composite Font or a Runtime Font, use the dialog’s configuration struct to filter the results. This helps eliminate user error by preventing the selection of incompatible font assets.
Synchronize with UMG Font Variables
If your tool updates a UMG Widget’s font, ensure you trigger a refresh of the Widget’s SynchronizeProperties() after the dialog closes. This allows the user to see the font change in the viewport immediately, which helps to eliminate the need for manual UI refreshes.
Utilize the Shared Font Cache
The module interacts with the engine’s global font cache. When a font is selected via the dialog, the engine may pre-load the atlas for that font. To eliminate memory bloat in the editor, ensure your custom tools don’t keep multiple font dialog instances alive in the background.