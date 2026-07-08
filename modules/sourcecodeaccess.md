---
layout: default
title: SourceCodeAccess
---

<!-- ai-generation-failed -->

<h1>SourceCodeAccess</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/SourceCodeAccess/SourceCodeAccess.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Settings, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

eal Editor to communicate with external Integrated Development Environments (IDEs) and text editors. It defines the generic interface (ISourceCodeAccessor) that all IDE plugins—such as Visual Studio, VS Code, Rider, and Xcode—must implement to allow the engine to open source files, navigate to specific lines, and sync project files.

This module is the backbone of the “Go to C++ Declaration” feature in the editor. By abstracting the IDE logic, it helps you eliminate hard-coded dependencies on a specific compiler or editor, allowing team members to use their preferred development environment seamlessly.

Practical Usage Tips and Best Practices
Configure via Editor Preferences
You can choose your preferred IDE in the Editor Preferences under General > Source Code. Changing this setting updates which ISourceCodeAccessor implementation is currently active. Use this to eliminate frustration when the engine keeps opening a secondary IDE instead of your primary one.
Implement a Custom Accessor for Niche Editors
If your team uses a specific editor (like Vim or Emacs), you can create a plugin that implements the ISourceCodeAccessor interface. Registering your custom accessor with the ISourceCodeAccessModule helps you eliminate manual file searching by enabling the “Open in IDE” buttons within the Unreal Editor.
Use ‘OpenFileAtLine’ for Debugging Tools
If you are building a custom logging tool or a crash reporter extension, you can call ISourceCodeAccessor::OpenFileAtLine. This allows your tool to immediately jump to the exact source file and line number where an error occurred, helping you eliminate the time spent navigating large folder structures.
Check for IDE Availability
Before attempting to open a file programmatically, use CanAccessSourceCode(). This check ensures that a valid IDE is installed and configured on the user’s machine, helping you eliminate silent failures or crashes when a developer lacks the necessary build tools.
Leverage ‘RefreshAvailability’ for Dynamic Discovery
If a user installs a new IDE while the editor is running, the SourceCodeAccess module may not see it immediately. Calling RefreshAvailability() triggers a re-scan of the system for supported IDEs, helping you eliminate the need to restart the Unreal Editor to pick up new software installations.
Sync Project Files Programmatically
The module provides the Tick() function which many accessors use to detect if project files (like .sln or .csproj) need to be regenerated. If your plugin modifies .build.cs files, triggering an accessor sync helps you eliminate IntelliSense errors caused by out-of-date project definitions.
Handle Multi-Project Workspaces
When working in a large repository with multiple .uproject files, ensure your accessor implementation correctly identifies the “Active” project. Providing the correct project path to the accessor helps you eliminate instances where the IDE opens the wrong solution file.
Cleanup on Accessor Elimination
When your custom source code plugin is disabled or uninstalled (the “elimination” of the module), ensure you call UnregisterAccessor via the ISourceCodeAccessModule. Failing to unregister can leave “ghost” options in the Editor Preferences, which you must eliminate to keep the user interface clean and functional.