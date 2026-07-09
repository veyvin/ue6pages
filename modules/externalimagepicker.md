---
layout: default
title: ExternalImagePicker
---

<!-- ai-generation-failed -->

<h1>ExternalImagePicker</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/ExternalImagePicker/ExternalImagePicker.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, DesktopPlatform, ImageCore, ImageWrapper, PropertyEditor, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Picker" to the PrivateDependencyModuleNames in your Build.cs file. This “eliminates” linker errors when you attempt to instantiate the picker widget in your Slate code.
Implement via SExternalImagePicker
The core of this module is the SExternalImagePicker widget. Use it within a SAssignNew or SNew block. It handles the “Browse” button and the thumbnail display automatically, which “eliminates” the need for you to build a custom file-loading UI from scratch.
Handle Path Logic (Absolute vs. Relative)
The picker returns an absolute file path. It is a best practice to convert this to a project-relative path (using FPaths::MakePathRelativeTo) before saving it to a config file. This “eliminates” path breakage when sharing the project with other team members via source control.
Copy to Project Directory
If a user picks an image from their “Downloads” folder, your tool should offer to copy that file into the project’s Resources or Content folder. This “eliminates” the risk of “missing file” errors when the project is moved or built on a different machine.
Validate Extensions and Dimensions
Use the OnExternalImagePicked delegate to run validation logic. If your tool requires a specific aspect ratio or size (e.g., 512x512), check the image header immediately. This “eliminates” the possibility of the user selecting an “illegal” file format that would crash a later stage of the pipeline.
Set Target Image for Preview
The widget can take an TargetImagePath attribute. If this path is valid, the widget will display a thumbnail of the currently selected external image. This “eliminates” visual ambiguity, allowing the user to confirm they have selected the correct file without opening a separate file explorer.
Editor-Only Constraint
Because this module resides in the Developer folder, it is strictly for editor-time use. It will be “eliminated” from the build during the packaging process. Never attempt to use this for runtime gameplay features; for in-game file picking, you would need to implement a platform-specific OS wrapper.
Use for Custom Asset Icons
If you are building a custom asset type, you can use the ExternalImagePicker in your IAssetTypeActions or IDetailCustomization to allow users to assign a unique disk-based icon to that asset, “eliminating” the generic default icon in specialized tool views.