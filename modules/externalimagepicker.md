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

to provide a bridge between the local filesystem and Unreal Engine’s asset pipeline. It is primarily used when the engine needs to “import” or “reference” an image file from outside the project directory for use as metadata or branding, such as project thumbnails, platform-specific launch icons, or splash screens.

This module provides a standardized UI for browsing, validating, and automatically copying external images into the appropriate project directories (like the /Build/ or /Config/ folders). It helps eliminate the manual process of renaming and moving files to specific platform folders required by the packaging system.

Practical Usage Tips and Best Practices
Standardize Project Thumbnails
Use the picker via the Project Settings > Description tab to set a project thumbnail. This ensures the image is correctly sized and placed in the project root, which helps eliminate generic placeholders in the Epic Games Launcher or the project browser.
Automatic Path Management
When you select an image via the ExternalImagePicker, the module doesn’t just link the file; it typically copies it into the project’s Build/[Platform] directory. This is critical to eliminate “missing file” errors when you move your project to a different workstation or a build server.
Adhere to Format Requirements
While the picker allows you to browse many types, it works best with .png for icons and .ico for Windows application icons. Using the recommended formats at the picker level helps eliminate conversion errors during the final packaging phase.
Observe Size Constraints
Pay attention to the resolution requirements listed next to the picker (e.g., 192x192 for certain icons). Selecting an oversized image can cause the picker to show a warning; resizing your source image beforehand helps eliminate distortion or aspect ratio issues in the final application.
Use for Platform-Specific Branding
In the Project Settings > Platforms section, use the picker to define unique splash screens for different devices (e.g., Android vs. iOS). This allows you to eliminate a “one-size-fits-all” approach and provide a native feel for each target platform.
Validate via Preprocessor Guards
If you are calling the ExternalImagePicker logic from C++, ensure your code is wrapped in #if WITH_EDITOR. This module is an editor-only tool and must be eliminated from any runtime or shipping builds to prevent linker errors.
Avoid Dynamic Runtime Calls
The ExternalImagePicker is designed for static configuration during development. To eliminate potential security risks and performance hits, do not attempt to use this module for gameplay features like “User Profile Pictures”; instead, use the ImageWrapper module and standard file I/O for runtime image loading.
Monitor the /Build/ Folder
Since the picker copies files into the /Build/ directory, ensure this directory is not ignored by your version control (like .gitignore). Checking these files in helps eliminate broken icon references for other team members who sync the project.