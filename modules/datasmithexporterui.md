---
layout: default
title: DatasmithExporterUI
---

<!-- ai-generation-failed -->

<h1>DatasmithExporterUI</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Datasmith/DatasmithExporterUI/DatasmithExporterUI.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DatasmithCore, DatasmithExporter, DesktopPlatform, DirectLink, InputCore, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

o provide a standardized user interface for asset export configurations within the Datasmith ecosystem. It primarily handles the “Options” dialog that appears when a user initiates an export from a supported CAD or 3D modeling application to the .udatasmith format.

Its role is to bridge the gap between the low-level Datasmith SDK and the user, ensuring that settings for geometry tessellation, animation handling, and metadata inclusion are presented consistently. By centralizing these UI elements, the module helps eliminate the need for developers to rewrite complex Slate code for every unique Datasmith plugin.

Practical Usage Tips and Best Practices
Implement a Unified Options Window Use the SDatasmithOptionsWindow class to create your export dialogs. This ensures your exporter follows the standard Unreal Engine visual language, helping to eliminate user confusion when switching between different Datasmith plugins (e.g., Revit vs. 3ds Max).
Leverage FDatasmithLogger for Feedback The module is designed to work closely with the FDatasmithLogger. Always route export warnings (like missing textures or unsupported geometry) to the logger so the UI can display them in the message log. This helps eliminate “silent failures” where assets are missing in Unreal without explanation.
Provide Clear Progress Information Integrate with the IDatasmithProgressManager to drive the UI progress bars. For large architectural scenes, users need to see active feedback; a responsive progress UI helps eliminate the perception that the host application has hung during a long export process.
Use Asynchronous Error Reporting Avoid using modal pop-up dialogs (OK/Cancel) for every error encountered during the export loop. Instead, collect errors and present them in a summary at the end of the process via the UI. This practice helps eliminate workflow interruptions for the user.
Bridge TCHAR to UTF8 for SDK Compatibility The Datasmith SDK often expects UTF8 strings, while the UI module uses Unreal’s FString (TCHAR). When passing data from a UI text field to the exporter backend, use the TCHAR_TO_UTF8 macro to eliminate character encoding errors or corrupted metadata.
Implement a “Quiet” Mode for Automation When designing your UI logic, ensure you include a “Quiet” or “Headless” flag. This allows build farm scripts or batch processors to eliminate the UI entirely, preventing the export process from blocking on a machine where no user is present to click “Export.”
Store and Restore User Preferences Use the GConfig system to save the user’s last-used settings within the UI module. By automatically populating the dialog with the previous session’s values, you eliminate repetitive data entry for users who frequently export with the same parameters.
Validate Relative Paths for Sidecar Folders Ensure the UI logic validates that the “sidecar” folder (where textures and meshes are stored) uses relative paths. The Datasmith UI should prevent users from selecting absolute paths that might break the link when the .udatasmith file is moved to another workstation, thereby eliminating broken asset references.