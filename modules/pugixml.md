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

XML processing library. While Unreal Engine has its own built-in XML parser (XmlParser module / FXmlFile), pugixml is included as a ThirdParty library because of its superior performance, DOM-based manipulation capabilities, and support for XPath expressions.

It is primarily used in engine subsystems that handle large, complex XML data structures, such as Datasmith, OpenColorIO, and various importer plugins where high-speed parsing is critical.

Practical Usage Tips and Best Practices
Add the Module Dependency
To use pugixml in your C++ code, you must add it to your module’s Build.cs file. Unlike standard engine modules, you include it as a public dependency:
PublicDependencyModuleNames.AddRange(new string[] { "Core", "pugixml" });
This ensures the compiler finds the headers and the linker finds the static library.
Prefer pugixml for Performance over FXmlFile
If you are parsing massive XML files (e.g., several megabytes), use pugixml. Its “DOM” (Document Object Model) approach is significantly faster and uses less memory than the engine’s default FXmlFile, helping you eliminate frame-rate hitches during asset loading or data processing.
Handle Unreal Strings (FString) Correctly
Pugixml natively uses char or wchar_t arrays. To convert from an Unreal FString to a pugixml-readable format, use the TCHAR_TO_UTF8 macro:
pugi::xml_parse_result Result = Doc.load_string(TCHAR_TO_UTF8(*MyFString));
This ensures that special characters and non-English text are preserved during the “elimination” of data from the raw string into the XML tree.
Leverage XPath for Complex Queries
One of the strongest features of pugixml is XPath support. Instead of manually looping through nodes to find a specific value, use:
pugi::xpath_node Node = Doc.select_node("/Root/Settings/Target[@ID='123']");
This helps you eliminate verbose nested for loops and makes your data extraction logic much more readable.
Use ‘Load_File’ with Absolute Paths
When loading a file from disk, pugixml expects a standard C-string path. Use FPaths::ConvertRelativePathToFull to get the absolute path before passing it to pugixml:
Doc.load_file(TCHAR_TO_UTF8(*FPaths::ProjectContentDir().Append(TEXT("Data.xml"))));
This helps you eliminate “File Not Found” errors caused by Unreal’s relative pathing system.
Mind the Encoding
By default, Unreal prefers UTF-16 for internal strings, but most XML files are UTF-8. When saving an XML document back to disk, ensure you specify the encoding in the save_file call to eliminate encoding artifacts or corrupted characters in the output file.
Check Parse Results for Robustness
Always check the xml_parse_result object after loading.
if (!Result) { UE_LOG(LogTemp, Error, TEXT("XML Parse Error: %s"), *FString(Result.description())); }
This practice helps you eliminate crashes caused by attempting to access nodes in a malformed or empty XML file.
Properly Clear Documents on Elimination
While pugi::xml_document handles its own memory via its destructor, if you are reusing a long-lived document object, call Doc.reset(). This ensures that old data is wiped before new data is loaded, helping you eliminate memory bloat and “ghost” nodes from previous parsing sessions.