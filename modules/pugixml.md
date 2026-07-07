---
layout: default
title: pugixml
---

<!-- ai-generation-failed -->

<h1>pugixml</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/pugixml/pugixml.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

weight, high-performance pugixml C++ library. It is a DOM-based XML parser that focuses on speed, memory efficiency, and ease of use.

While Unreal Engine provides its own FXmlFile and XmlParser modules, many developers (and engine subsystems) prefer pugixml for handling large XML datasets, such as complex metadata, save files, or configuration data from external tools. It is significantly faster than the standard engine XML parser and provides much better support for XPath queries to locate specific data points.

Practical Usage Tips and Best Practices
1. Add to Build.cs Dependencies

To use pugixml in your C++ project, you must explicitly include the module in your build settings.

Action: Add "pugixml" to your PublicDependencyModuleNames or PrivateDependencyModuleNames in your Project.Build.cs file. This allows the Unreal Build Tool (UBT) to link the library and include the headers, helping you eliminate “file not found” errors during compilation.
2. Use the Correct Header Path

Because this is a third-party library, the include path is slightly different than standard engine classes.

Tip: Use #include "pugixml.hpp" in your source files. Always wrap this include in THIRD_PARTY_INCLUDES_START and THIRD_PARTY_INCLUDES_END macros. This helps you eliminate compiler warnings related to non-engine coding standards found in third-party code.
3. Prefer XPath for Deep Data Extraction

Finding a specific nested value in a standard XML parser often requires nested loops.

Action: Use the select_node or select_nodes functions with an XPath expression (e.g., "/Root/Items/Item[@ID='123']"). This allows you to jump directly to the data you need, which helps you eliminate complex and error-prone manual traversal logic.
4. Manage Memory with pugi::xml_document

The xml_document object owns the memory for the entire parsed tree.

Best Practice: Ensure the xml_document stays in scope as long as you are using xml_node or xml_attribute references. Once the document is destroyed, all pointers to its nodes become invalid. Managing this lifetime carefully helps you eliminate memory corruption and “Access Violation” crashes.
5. Handle String Conversions (FString to Char*)

pugixml primarily uses char* (UTF-8) or wchar_t*, whereas Unreal uses FString.

Action: Use TCHAR_TO_UTF8(*MyFString) when passing data into pugixml, and UTF8_TO_TCHAR(MyNode.child_value()) when bringing data back into Unreal. Correct encoding handling helps you eliminate issues with special characters or localized text being mangled.
6. Utilize the “In-Place” Parsing Option

If you have a large XML string already in memory, you can parse it without making an extra copy.

Tip: Use the parse_buffer_inplace function. This is extremely memory-efficient for large files but modifies the source buffer. Using this method helps you eliminate unnecessary memory allocations and improves performance for large-scale data processing.
7. Validate XML with the Parse Result

pugixml does not throw exceptions; it returns a status object.

Best Practice: Always check the pugi::xml_parse_result object after loading a file. Check result.status and log the result.description() and result.offset if it fails. This allows you to catch malformed files early and helps you eliminate hours of debugging “empty” data.
8. Use for Editor-Only Data Tools

While pugixml is available at runtime, it is exceptionally useful for creating custom importer tools in the Editor.

Tip: Use it to parse exported data from DCC tools like Maya, Blender, or custom level editors. Its speed ensures that even XML files with hundreds of thousands of nodes won’t hang the Editor during the import process, effectively eliminating long wait times for your designers.