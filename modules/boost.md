---
layout: default
title: Boost
---

<!-- ai-generation-failed -->

<h1>Boost</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Boost/Boost.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

tandard gameplay module. It is located within the Engine/Source/ThirdParty/Boost directory. Unreal Engine includes a specific version of Boost (currently v1.82 as of UE 5.4+) primarily to support complex internal systems such as OpenUSD, AutoRTFM, and certain modeling tools.

While Boost provides a vast collection of C++ libraries for linear algebra, multithreading, and image processing, it is generally treated as a “hidden” dependency. Developers are encouraged to use Unreal’s native types (like TArray, TMap, and FString) wherever possible to maintain engine consistency.

Practical Usage Tips and Best Practices
1. Avoid Conflicts with ‘AllowWindowsPlatformTypes’

Boost often uses macro names that conflict with Windows system headers or Unreal’s own definitions.

Best Practice: Always wrap Boost includes with Unreal’s platform-type wrappers. This helps eliminate compiler errors caused by redefinition of macros like check, verify, or any.
C++
	#include "Windows/AllowWindowsPlatformTypes.h"

	#include <boost/asio.hpp>

	#include "Windows/HideWindowsPlatformTypes.h"
Copy code
2. Prevent Macro Shadowing with THIRD_PARTY_INCLUDES

Unreal’s build system is strict about warnings-as-errors. Many Boost headers trigger “shadow variable” or “unused parameter” warnings.

Tip: Surround your Boost includes with the THIRD_PARTY_INCLUDES_START and _END macros to eliminate unnecessary build breaks caused by non-compliant code within the Boost library itself.
3. Link via Build.cs Only When Necessary

If your custom module needs to use Boost, you must explicitly add it to your Build.cs file.

Action: Use AddEngineThirdPartyPrivateStaticDependencies(Target, "Boost");. Note that because Boost is mostly a header-only library, this primarily adds the necessary include paths to your module’s environment.
4. Favor Unreal Native Containers

While boost::container is powerful, it is not reflected by Unreal’s Garbage Collection (GC) system.

Best Practice: Do not store UObject pointers inside Boost containers. If the GC runs, it will not see those references and may eliminate the objects from memory, leading to crashes. Stick to TArray or TMap for any data involving the Unreal reflection system.
5. Use Boost for Specialized Math or Interop

Boost is highly effective for tasks where Unreal’s math library (FMath) might be insufficient, such as advanced graph theory or specific regex requirements.

Tip: If you are building a tool that interfaces with external software (like a custom USD pipeline), use the included Boost library to ensure version parity with the engine’s internal USD implementation.
6. Minimize Template Bloat

Boost is notorious for heavy template usage, which can significantly increase compile times.

Best Practice: Keep Boost usage contained within private source (.cpp) files rather than public headers (.h). This prevents the Boost templates from being pulled into every module that includes your header, which helps eliminate “bottleneck” compilation times.
7. Be Mindful of Exception Handling

Unreal Engine typically disables C++ exceptions (bEnableExceptions = false) for performance and stability.

Tip: Many Boost libraries rely on exceptions. If you use a part of Boost that requires them, you must enable exceptions in your Build.cs, but be aware that this can eliminate certain performance optimizations across your module.
8. Verify VFX Reference Platform Compliance

Unreal Engine maintains Boost versions to align with the VFX Reference Platform standards.

Action: If you are developing a plugin for Fab or a cross-studio pipeline, check the Version.txt in the Boost third-party folder. Sticking to the engine-provided version helps eliminate compatibility issues when sharing code with other studios or artists.