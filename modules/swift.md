---
layout: default
title: Swift
---

<!-- ai-generation-failed -->

<h1>Swift</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Apple/Swift/Swift.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

elopers to write high-level game logic, UI, and platform-specific integrations using the Swift programming language. It is primarily designed to enhance development for Apple platforms (iOS, macOS, visionOS) by providing a modern, memory-safe alternative to C++ while maintaining seamless interop with the engine’s core.

By leveraging the Swift module, you can eliminate much of the boilerplate associated with Objective-C++ “glue” code and use Swift’s modern syntax to call into Unreal’s C++ APIs or expose Swift functions to Blueprints.

Practical Usage Tips and Best Practices
Enable Swift Support in Build.cs
To use Swift in your module, you must explicitly enable it in your .Build.cs file by setting bEnableSwiftSupport = true;. You also need to add "Swift" to your PublicDependencyModuleNames. This tells the Unreal Build Tool (UBT) to invoke the Swift compiler alongside Clang, helping you eliminate manual build step configurations.
Use Generated Bridging Headers
Unreal automatically generates a bridging header (e.g., MyModule-Swift.h) that allows your C++ code to see your Swift classes. To call Swift from C++, simply include this generated header in your .cpp files. This automated process helps you eliminate the need to manually maintain complex header maps.
Expose Classes with @objc and Unreal Macros
For a Swift class to be visible to Unreal’s C++ and Reflection systems, it must inherit from NSObject (or a supported Unreal base) and be marked with @objc. While full UCLASS support in Swift is evolving, using @objc and the UnrealSwift interop macros helps you eliminate friction when passing data between the two languages.
Mind the Memory Management Split
Swift uses Automatic Reference Counting (ARC), while Unreal uses its own Garbage Collector (GC) for UObjects. When passing a UObject to Swift, use the provided wrapper types to ensure the object isn’t prematurely reclaimed by the GC. This awareness helps you eliminate “use-after-free” crashes during cross-language execution.
Prefer Swift for Platform-Specific APIs
Use the Swift module to handle Apple-specific features like StoreKit, Game Center, or ARKit. Swift has first-class support for these frameworks, allowing you to eliminate the awkwardness of calling modern Apple APIs through legacy C++ wrappers.
Leverage Swift’s Safety for Game Logic
Use Swift for complex “business logic” or UI state management where its strict null-safety (optionals) can shine. Moving error-prone logic from raw C++ pointers to Swift optionals helps you eliminate a large category of common null-pointer dereference bugs.
Check Xcode Version Compatibility
Swift support in UE 5.5+ requires a modern version of Xcode (refer to engine release notes, typically Xcode 15 or 16). Ensure all team members are on a synchronized version of the toolchain to eliminate “Module not found” or binary compatibility errors during local builds.
Handle Cleanup on Elimination
If your Swift code registers observers or listeners (e.g., to NotificationCenter), ensure they are removed when the parent Unreal Actor or Component is destroyed. Properly managing the “elimination” of Swift listeners helps you eliminate memory leaks and unexpected behavior when levels are reloaded.