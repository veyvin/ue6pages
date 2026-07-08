---
layout: default
title: TinyXML2
---

<!-- ai-generation-failed -->

<h1>TinyXML2</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/TinyXML2/TinyXML2.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

grated into Unreal Engine. It is located in Engine/Source/ThirdParty/tinyxml2 and is exposed as an engine module for use in C++ projects.

While Unreal Engine provides a native XmlParser module, tinyxml2 is often preferred for high-performance DOM manipulation, tools development, or scenarios where you need a standard-compliant, non-UObject-based parser. It is significantly faster and uses less memory than the native FXmlFile for large or complex XML structures.

Practical Usage Tips and Best Practices
Add to Build.cs Dependencies
To use the library, you must add it to your module’s dependency list. This tells the Unreal Build Tool to link the library correctly, helping you eliminate “unresolved external symbol” errors.
C++
	    // MyModule.Build.cs

	    PrivateDependencyModuleNames.AddRange(new string[] { "Core", "tinyxml2" });

	    ```

	 

	*   **Use Third-Party Include Guards**  

	    Because TinyXML-2 is a third-party library, always wrap its include in Unreal’s safety macros. This helps you **eliminate** compiler warnings related to shadow variables or non-standard preprocessor usage.

	    ```cpp

	    #include "CoreMinimal.h"

	    THIRD_PARTY_INCLUDES_START

	    #include <tinyxml2.h>

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	*   **Handle Platform Type Collisions**  

	    If your XML logic interacts with Windows-specific APIs, wrap the includes in `AllowWindowsPlatformTypes.h` and `HideWindowsPlatformTypes.h`. This ensures that TinyXML-2’s types don't clash with Unreal's redefined types, helping you **eliminate** cryptic "already defined" linker errors.

	 

	*   **Prefer for Memory-Sensitive Data**  

	    The native `FXmlFile` creates many small strings and allocations. For very large XML files (like exported localization data or massive level manifests), use `tinyxml2::XMLDocument`. It is significantly faster and more memory-efficient, which helps you **eliminate** hitches during synchronous asset loading.

	 

	*   **Utilize the 'Print' for Debugging**  

	    TinyXML-2 includes an `XMLPrinter` class. Use this to quickly dump your DOM to an `FString` or a log file during development. This visibility helps you **eliminate** logic errors in your XML generation by verifying the structure before it is saved to disk.

	 

	*   **Manage Encoding Explicitly**  

	    TinyXML-2 assumes UTF-8. When passing strings from Unreal (which uses UTF-16 internally for `FString`), convert them using `TCHAR_TO_UTF8()`. Conversely, use `UTF8_TO_TCHAR()` when reading data back into Unreal. This helps you **eliminate** "garbled text" or encoding artifacts in your UI.

	 

	*   **Check for Success at Every Step**  

	    Unlike some Unreal APIs that fail silently, TinyXML-2 returns specific error codes (e.g., `XML_SUCCESS`). Always check the `ErrorID()` of the `XMLDocument` after loading. This defensive coding helps you **eliminate** crashes when a malformed or empty XML file is encountered.

	 

	*   **Leverage for Non-UObject Workflows**  

	    If you are writing a standalone tool (using the `Program` target type) that doesn't link against the `Engine` module, TinyXML-2 is your best choice for XML. It has fewer dependencies than the `XmlParser` module, helping you **eliminate** unnecessary bloat in your tool's final executable size.
Copy code
Use Third-Party Include Macros
Since this is an external library, wrap the include in Unreal’s safety macros. This prevents the compiler from throwing warnings about variable shadowing or non-standard syntax, which helps you eliminate clutter in your build logs.
C++
	    // MyModule.Build.cs

	    PrivateDependencyModuleNames.AddRange(new string[] { "Core", "tinyxml2" });

	    ```

	 

	*   **Use Third-Party Include Guards**  

	    Because TinyXML-2 is a third-party library, always wrap its include in Unreal’s safety macros. This helps you **eliminate** compiler warnings related to shadow variables or non-standard preprocessor usage.

	    ```cpp

	    #include "CoreMinimal.h"

	    THIRD_PARTY_INCLUDES_START

	    #include <tinyxml2.h>

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	*   **Handle Platform Type Collisions**  

	    If your XML logic interacts with Windows-specific APIs, wrap the includes in `AllowWindowsPlatformTypes.h` and `HideWindowsPlatformTypes.h`. This ensures that TinyXML-2’s types don't clash with Unreal's redefined types, helping you **eliminate** cryptic "already defined" linker errors.

	 

	*   **Prefer for Memory-Sensitive Data**  

	    The native `FXmlFile` creates many small strings and allocations. For very large XML files (like exported localization data or massive level manifests), use `tinyxml2::XMLDocument`. It is significantly faster and more memory-efficient, which helps you **eliminate** hitches during synchronous asset loading.

	 

	*   **Utilize the 'Print' for Debugging**  

	    TinyXML-2 includes an `XMLPrinter` class. Use this to quickly dump your DOM to an `FString` or a log file during development. This visibility helps you **eliminate** logic errors in your XML generation by verifying the structure before it is saved to disk.

	 

	*   **Manage Encoding Explicitly**  

	    TinyXML-2 assumes UTF-8. When passing strings from Unreal (which uses UTF-16 internally for `FString`), convert them using `TCHAR_TO_UTF8()`. Conversely, use `UTF8_TO_TCHAR()` when reading data back into Unreal. This helps you **eliminate** "garbled text" or encoding artifacts in your UI.

	 

	*   **Check for Success at Every Step**  

	    Unlike some Unreal APIs that fail silently, TinyXML-2 returns specific error codes (e.g., `XML_SUCCESS`). Always check the `ErrorID()` of the `XMLDocument` after loading. This defensive coding helps you **eliminate** crashes when a malformed or empty XML file is encountered.

	 

	*   **Leverage for Non-UObject Workflows**  

	    If you are writing a standalone tool (using the `Program` target type) that doesn't link against the `Engine` module, TinyXML-2 is your best choice for XML. It has fewer dependencies than the `XmlParser` module, helping you **eliminate** unnecessary bloat in your tool's final executable size.
Copy code
Handle String Conversions (UTF-8)
TinyXML-2 works exclusively with UTF-8 char* strings. Since Unreal uses UTF-16 for FString, you must use TCHAR_TO_UTF8() when writing to XML and UTF8_TO_TCHAR() when reading. This ensures you eliminate character encoding artifacts in your data.
Prefer for Memory-Intensive XML
The native XmlParser creates many small FString objects, which can be slow. For massive XML files (like exported localization data), use tinyxml2::XMLDocument. Its efficient memory pooling helps you eliminate performance hitches during synchronous file loading.
Check Return Codes for Safety
Most TinyXML-2 functions return a XMLError enum (e.g., XML_SUCCESS). Always validate these results, especially when loading files from disk. Checking these codes helps you eliminate crashes caused by malformed or missing XML files.
Use XMLPrinter for Debugging
TinyXML-2 includes a built-in XMLPrinter class. Use this to dump your current XML structure to the log (UE_LOG) during development. Seeing the raw structure helps you eliminate logic errors in your hierarchy before saving to disk.
Isolate from UObject Hierarchy
TinyXML-2 does not use the Unreal Reflection system or Garbage Collector. If you store pointers to XML nodes in an Actor, you must manually manage their lifecycle. Properly deleting the XMLDocument ensures the elimination of the entire tree from memory, helping you eliminate memory leaks.
Use for Standalone Program Targets
If you are writing a “Program” target (a standalone .exe without the full Engine), TinyXML-2 is much easier to link than the XmlParser module. Using it helps you eliminate unnecessary engine dependencies in your utility tools.