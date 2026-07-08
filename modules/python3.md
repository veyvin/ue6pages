---
layout: default
title: Python3
---

<!-- ai-generation-failed -->

<h1>Python3</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Python3/Python3.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the core integration of the Python 3 interpreter within Unreal Engine. It provides a bridge between the engine’s C++ reflection system and the Python scripting language, allowing developers to manipulate assets, control the editor, and automate complex pipeline tasks using standard Python syntax.

Currently shipping with an embedded version of Python 3.11, this module is the industry-standard choice for technical artists and pipeline engineers. It enables the elimination of manual, repetitive tasks by providing a high-level API to perform bulk asset edits, automate imports, and integrate the Unreal Editor with external DCC (Digital Content Creation) tools like Maya, Houdini, and Blender.

Practical Usage Tips and Best Practices
1. Enable Developer Mode for Stub Generation

In Project Settings > Plugins > Python, enable Developer Mode. This triggers the module to generate a unreal.py stub file in your project’s Intermediate/PythonStub folder. Using this file with an IDE like VS Code or PyCharm leads to the elimination of “guessing” API names by providing full auto-completion and type hinting for the entire unreal library.

2. Utilize the /Content/Python Directory

Unreal Engine automatically adds the /Content/Python folder of your project and any enabled plugins to the Python sys.path. Placing your scripts and third-party modules here leads to the elimination of complex environment variable management, as the Python3 module will discover and load them automatically upon editor startup.

3. Leverage the ‘unreal’ Module for Reflection

The import unreal command gives you access to almost every class, function, and property exposed to the engine’s reflection system. Instead of writing custom C++ for every tool, use Python to call unreal.EditorAssetLibrary functions. This facilitates the elimination of slow C++ compile times for high-level editor logic.

4. Manage Dependencies via Pip Requirements

You can specify third-party library dependencies in your plugin’s .uplugin file using the PythonRequirements field. The Python3 module uses pip to install these during the build or launch process. This practice assists in the elimination of “Missing Module” errors when sharing your scripts with other team members who may not have the required libraries installed.

5. Use Remote Execution for External Tool Integration

The module includes a Python Remote Execution feature (accessible via the unreal_remote_execution library). This allows you to send Python commands to a running instance of Unreal Engine from an external terminal or DCC. This leads to the elimination of context-switching, allowing you to “push” assets or commands into the engine directly from your primary work environment.

6. Combine Python with Editor Utility Widgets

You can call Python scripts directly from Editor Utility Blueprints using the “Execute Python Script” node. This allows you to build professional UIs in UMG while using Python for the “heavy lifting” logic. This hybrid approach leads to the elimination of complex Blueprint “spaghetti” for tasks that are more easily handled by Python’s string and file manipulation libraries.

7. Avoid Using Python for Runtime Gameplay

The Python3 module is strictly an editor-side and commandlet utility. It is not intended for runtime gameplay logic on consoles or mobile devices. Adhering to this boundary leads to the elimination of performance and packaging failures, as Python is stripped out of shipping builds to maintain optimal runtime efficiency.

8. Optimize Performance with unreal.ScopedEditorTransaction

When performing bulk operations (like renaming 1,000 assets), wrap your code in a with unreal.ScopedEditorTransaction("My Task"): block. This leads to the elimination of “Undo Buffer” bloat, as it collapses all 1,000 actions into a single undo entry, preventing the editor from hanging while recording individual changes.