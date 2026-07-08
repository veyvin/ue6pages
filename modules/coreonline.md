---
layout: default
title: CoreOnline
---

<!-- ai-generation-failed -->

<h1>CoreOnline</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/CoreOnline/CoreOnline.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

orm-agnostic representations of online concepts—such as unique player IDs, account identifiers, and error results—ensuring that high-level gameplay code can interact with Steam, Epic Online Services (EOS), Xbox Live, or PSN without needing to know the specific implementation details of each.

Practical Usage Tips and Best Practices
Prefer FUniqueNetId for Player Identification
Always use the FUniqueNetId (or its wrapper FUniqueNetIdRepl) to identify players in C++. This opaque type is designed to handle different ID formats across platforms, allowing you to eliminate hard-coded logic that relies on platform-specific string formats.
Utilize FOnlineError for Robust Debugging
Instead of using simple booleans for success or failure, use the FOnlineError type provided by this module. It includes detailed error codes and human-readable strings, which helps you eliminate guesswork when a login or session creation fails in a live environment.
Include Module in Core Build Dependencies
If you are building a custom online integration or a multiplayer game, add CoreOnline to your PublicDependencyModuleNames in Build.cs. This is required to access the basic types used by virtually all other online modules, helping to eliminate “unresolved external” linker errors.
Leverage FUniqueNetIdRepl for Networking
When replicating a player ID over the network in a UPROPERTY, always use FUniqueNetIdRepl. This wrapper handles the serialization and bit-packing of the ID automatically, which helps to eliminate bandwidth waste and ensures the ID is correctly reconstructed on the client.
Use CoreOnline for Platform-Agnostic Results
When designing your own online functions, return TOnlineResult. This template class from CoreOnline provides a standardized way to pass either the requested data or an error object, helping you eliminate messy out-parameters in your function signatures.
Handle Account ID Transitions
With the transition to Online Services (v2), CoreOnline now includes the FAccountId type. If you are starting a new project in UE 5.6, begin adopting FAccountId and FPlatformUserId early to eliminate future technical debt as the engine moves away from legacy Online Subsystem types.
Avoid Raw Pointer Casts for Net IDs
Never attempt to cast a FUniqueNetId to a specific platform type (like FUniqueNetIdSteam) unless absolutely necessary. Use the virtual functions provided by the base class (like ToString() or IsValid()) to eliminate crashes caused by unexpected platform data structures.
Check Validity Before Use
Online identifiers can often be null or invalid during the login flow. Always call .IsValid() on your IDs before passing them to session or friend functions to eliminate null pointer exceptions and ensure the stability of your online services logic.