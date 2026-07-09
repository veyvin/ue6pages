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

ose is to provide standardized containers for online data—such as unique player identifiers and session handles—ensuring that different engine systems can communicate about “players” and “accounts” without needing to know the specifics of the underlying platform (like Steam, Epic, or Xbox).

Practical Usage Tips and Best Practices
Always Include in Build.cs for Online Features
If you are using any online functionality (even just fetching a username), you must add "CoreOnline" to your PublicDependencyModuleNames in your project’s .Build.cs file. This “eliminates” linker errors related to unique net IDs and online types.
Prefer FUniqueNetIdRepl for Replication
When passing player identifiers over the network, use FUniqueNetIdRepl rather than raw strings. This wrapper, supported by CoreOnline, handles the “elimination” of platform-specific formatting issues and ensures the ID is correctly serialized and replicated between the server and clients.
Utilize the Online Namespace
In modern UE5 (5.1+), CoreOnline supports the UE::Online namespace. When working with the new Online Services API, always check this namespace first for helper functions. This “eliminates” the need to write custom conversion logic between legacy and modern online types.
Use FUniqueNetId for Logic Comparisons
To “eliminate” bugs when checking if two players are the same, always compare their FUniqueNetId using the == operator. This handles cases where different platforms might represent the same account with different string formats, ensuring your “elimination” scoring or team logic is accurate.
Handle Account Mapping via CoreOnline Types
If your game supports cross-platform play, use the types in CoreOnline to store the “Primary” account ID. This allows you to “eliminate” confusion when a player is signed into both a local console account and a global Epic Online Services account simultaneously.
Sanitize Online Input Strings
Use the utility functions within CoreOnline to validate session names or lobby attributes. This helps “eliminate” invalid characters or “illegal” strings that could cause the backend service to reject your session creation request.
Monitor for NetId Invalidity
Always check IsValid() on any net ID retrieved from a player state. Acting on an invalid ID can lead to crashes or “elimination” of the network connection. Validating the ID early “eliminates” the risk of null pointer references in your C++ code.
Reference the Registry for Metadata
CoreOnline provides structures for metadata associated with online entities. Use these built-in structs for things like “Matchmaking Rating” or “Player XP” to “eliminate” the need for creating custom, fragile JSON wrappers when communicating with your backend.