---
layout: default
title: libzip
---

<!-- ai-generation-failed -->

<h1>libzip</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/libzip/libzip.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li><li><span class="label">依赖</span><span class="value">OpenSSL, zlib</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

t provides a cross-platform API for reading, creating, and modifying Zip archives. While Unreal offers high-level tools like the “Zip Up Project” feature and the Oodle-based .pak system for standard packaging, the libzip module is the engine’s low-level workhorse for handling standard .zip files at runtime.

It is primarily used for modding support, runtime asset downloading/patching, and diagnostic tool development. It facilitates the elimination of manual file-stream management by providing a robust, structured way to interact with compressed containers.

Practical Usage Tips and Best Practices
1. Add “libzip” to Build.cs

To use the library in your project, you must link it as a private dependency in your Module.Build.cs. This is essential for the elimination of linker errors when targeting multiple platforms:

C#
	// In your MyProject.Build.cs

	AddEngineThirdPartyPrivateStaticDependencies(Target, "libzip");

	```

	 

	#### 2. Wrap Headers with Macros

	Libzip is a C-style library and can cause macro collisions with Unreal's reflection system. Always wrap your `#include` statements with the engine's third-party safety macros. This practice leads to the **elimination** of "shadowed variable" or "redefinition" compiler errors:

	```cpp

	THIRD_PARTY_INCLUDES_START

	#include <zip.h>

	THIRD_PARTY_INCLUDES_END

	```

	 

	#### 3. Use FPlatformFileManager for Paths

	Libzip expects standard C-style paths. When passing paths from Unreal (`FString`), use `*FPaths::ConvertRelativePathToFull(Path)`. This assists in the **elimination** of "File Not Found" errors, especially on mobile and console platforms where the sandbox file system is strictly enforced.

	 

	#### 4. Manage Lifecycle to Eliminate Leaks

	Libzip types like `zip_t` and `zip_file_t` are not managed by Unreal's Garbage Collector. You must manually call `zip_close()` and `zip_fclose()` when finished. Using a `TUniquePtr` with a custom deleter or a scoped cleanup pattern is a best practice for the **elimination** of memory and file-handle leaks:

	```cpp

	// Example of a safe cleanup pattern

	zip_t* Archive = zip_open(TCHAR_TO_UTF8(*Path), 0, &Error);

	// ... processing ...

	zip_close(Archive); // Important: This also flushes writes to disk

	```

	 

	#### 5. Handle Thread-Safety Carefully

	Libzip is not inherently thread-safe. If you are extracting assets on a background **Task** (to prevent Game Thread hitches), ensure that only one thread accesses a specific `zip_t` handle at a time. Using a `FCriticalSection` (mutex) around archive operations facilitates the **elimination** of race conditions and data corruption.

	 

	#### 6. Coordinate with Oodle or Zlib

	Unreal often uses Oodle or Zlib for internal compression. If you are creating a custom archive format for your game, consider whether a standard `.zip` (via libzip) or a compressed `.pak` (via the engine's PakFile module) is more appropriate. Using standard zip for user-facing mods facilitates the **elimination** of proprietary tool requirements for your community.

	 

	#### 7. Validate Error Codes

	Libzip functions typically return `NULL` or negative integers on failure. Always check the `zip_error_t` or the returned error code. Implementing verbose logging via `UE_LOG` when an archive fails to open assists in the **elimination** of silent failures during complex runtime patching operations.

	 

	#### 8. Verify Non-Shipping Inclusion

	By default, some third-party libraries may be excluded from specific build configurations. If your game relies on libzip for runtime content, verify that it is properly staged in your **Shipping** build. Checking your `Project Settings > Packaging` to ensure additional files are included leads to the **elimination** of "missing library" crashes on end-user machines.
Copy code
2. Wrap Headers with Macros

Libzip is a C-style library and can cause macro collisions with Unreal’s reflection system. Always wrap your #include statements with the engine’s third-party safety macros. This practice leads to the elimination of “shadowed variable” or “redefinition” compiler errors:

C++
	THIRD_PARTY_INCLUDES_START

	#include <zip.h>

	THIRD_PARTY_INCLUDES_END
Copy code
3. Use FPlatformFileManager for Paths

Libzip expects standard C-style paths. When passing paths from Unreal (FString), use *FPaths::ConvertRelativePathToFull(Path). This assists in the elimination of “File Not Found” errors, especially on mobile and console platforms where the sandbox file system is strictly enforced.

4. Manage Lifecycle to Eliminate Leaks

Libzip types like zip_t and zip_file_t are not managed by Unreal’s Garbage Collector. You must manually call zip_close() and zip_fclose() when finished. Using a Scoped Cleanup pattern is a best practice for the elimination of memory and file-handle leaks:

C++
	int Error = 0;

	zip_t* Archive = zip_open(TCHAR_TO_UTF8(*Path), 0, &Error);

	// ... processing ...

	zip_close(Archive); // Important: This also flushes writes to disk
Copy code
5. Handle Thread-Safety Carefully

Libzip is not inherently thread-safe. If you are extracting assets on a background Task (to prevent Game Thread hitches), ensure that only one thread accesses a specific zip_t handle at a time. Using a FCriticalSection (mutex) around archive operations facilitates the elimination of race conditions and data corruption.

6. Coordinate with Oodle or Zlib

Unreal often uses Oodle or Zlib for internal compression. If you are creating a custom archive format for your game, consider whether a standard .zip (via libzip) or a compressed .pak (via the engine’s PakFile module) is more appropriate. Using standard zip for user-facing mods facilitates the elimination of proprietary tool requirements for your community.

7. Validate Error Codes

Libzip functions typically return NULL or negative integers on failure. Always check the zip_error_t or the returned error code. Implementing verbose logging via UE_LOG when an archive fails to open assists in the elimination of silent failures during complex runtime patching operations.

8. Verify Non-Shipping Inclusion

By default, some third-party libraries may be excluded from specific build configurations. If your game relies on libzip for runtime content, verify that it is properly staged in your Shipping build. Checking your Project Settings > Packaging to ensure additional files are included leads to the elimination of “missing library” crashes on end-user machines.