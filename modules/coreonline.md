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

t provides the shared data types and utility structures required for online functionality. It acts as the “common language” between the core engine and the more complex Online Subsystem (OSSv1) or the newer Online Services (OSSv2).

Instead of providing high-level logic like matchmaking or friend lists, this module defines the standard identifiers and error containers used across all platforms (Steam, Epic, Xbox, PSN, etc.). It is a mandatory dependency for any C++ project that handles player identities or online results in a platform-agnostic way.

Practical Usage Tips and Best Practices
1. Include as a Public Dependency

Any module that handles player IDs or online error results needs this in its Build.cs. It is often paired with OnlineSubsystem or OnlineServicesInterface.

Action: Add it to your module dependencies to access types like FUniqueNetId:
C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { 

	    "Core", 

	    "CoreUObject", 

	    "Engine", 

	    "CoreOnline" // Required for FUniqueNetId, FOnlineError, etc.

	});

	```

	 

	#### 2. Use FUniqueNetIdWrapper for Identity

	While `FUniqueNetId` is an abstract interface, `FUniqueNetIdWrapper` is the concrete struct you should use for storing and passing IDs.

	*   **Best Practice:** Always use the wrapper when storing a player's ID in a class member. It handles the underlying shared pointer safely and ensures that your C++ code remains compatible whether the player is on Steam, Epic, or LAN.

	 

	#### 3. Standardize Error Handling with FOnlineError

	This module provides the `FOnlineError` struct, which is the unified way to communicate why an online operation failed.

	*   **Tip:** When writing custom online wrappers, return an `FOnlineError` instead of a simple boolean. This allows you to capture the `ErrorCode` (string), `ErrorMessage` (text for UI), and the `FailureType` (enum), which helps **eliminate** "silent" failures in multiplayer logic.

	 

	#### 4. Leverage FAccountObjectId for OSSv2

	If you are moving to the newer **Online Services (OSSv2)**, you will encounter `FAccountId`.

	*   **Best Practice:** Understand that `FAccountId` (found in CoreOnline) is the new standard for the modular online system. It is designed to be smaller and more performant than the old `FUniqueNetId`, helping **eliminate** memory overhead when managing large friend lists or lobby memberships.

	 

	#### 5. Safe ID Comparisons

	Never compare `FUniqueNetId` pointers directly.

	*   **Tip:** Use the `==` operator on the wrappers or the `IsValid()` method. CoreOnline ensures these operators are overloaded to compare the actual binary data of the ID rather than the memory address, **eliminating** bugs where two players appear different just because their ID objects were allocated separately.

	 

	#### 6. Serialization with FUniqueNetIdRepl

	If you need to send a player's unique identity over the network (RPCs or Replication):

	*   **Action:** Use `FUniqueNetIdRepl`. This is a specialized version of the ID found in CoreOnline specifically designed for `NetSerialize`. It automatically handles the bit-packing required to send platform-specific IDs efficiently across the wire.

	 

	#### 7. Interface with the OnlineError Console Command

	CoreOnline provides the backend for certain debugging commands.

	*   **Tip:** You can use console commands to simulate or inspect online errors. While the high-level logic is in the Subsystem, the definitions in CoreOnline allow the engine to translate raw platform errors into human-readable strings, which is essential for **eliminating** confusion during cross-play testing.

	 

	#### 8. Use 'CoreOnline' for Data Assets

	If you want to store "Whitelists" or "Admin Lists" in a `UDataAsset`:

	*   **Best Practice:** Use `FString` or `FUniqueNetIdRepl` for storage. Since `FUniqueNetId` is not a `UObject`, you cannot mark a raw pointer to it as a `UPROPERTY`. Using the wrapper types from CoreOnline ensures your data is correctly reflected, GC-safe, and editable in the Unreal Editor.
Copy code
2. Use FUniqueNetIdWrapper for Safe Storage

While FUniqueNetId is an abstract interface, FUniqueNetIdWrapper is the concrete struct you should use for storing and passing IDs in your classes.

Best Practice: Always use the wrapper when storing a player’s ID as a class member. It handles the underlying shared pointer safely, helping eliminate memory leaks or crashes when a player logs out.
3. Standardize Responses with FOnlineError

This module provides the FOnlineError struct, which is the unified way to communicate why an online operation failed.

Tip: When writing custom online wrappers, return an FOnlineError instead of a simple boolean. This allows you to capture the ErrorCode (string), ErrorMessage (text for UI), and the FailureType (enum), which helps eliminate “silent” failures in your UI logic.
4. Transition to FAccountId for OSSv2

If you are moving to the newer Online Services (OSSv2), you will encounter FAccountId instead of the older FUniqueNetId.

Best Practice: Understand that FAccountId is designed to be smaller and more performant. Using the types defined in CoreOnline ensures your project is ready for the transition to OSSv2, eventually eliminating the overhead of the legacy subsystem.
5. Safe ID Comparisons

Never compare raw FUniqueNetId pointers directly using ==, as this only compares the memory address.

Tip: Use the == operator on the wrappers or the IsValid() method. CoreOnline ensures these operators are overloaded to compare the actual binary data of the ID, eliminating bugs where two identical players appear different because their ID objects were allocated separately.
6. Utilize FUniqueNetIdRepl for Replication

If you need to send a player’s identity over the network via RPCs or Property Replication:

Action: Use FUniqueNetIdRepl. This is a specialized version of the ID found in CoreOnline specifically designed for NetSerialize. It automatically handles the bit-packing required to send platform-specific IDs efficiently, which helps eliminate wasted bandwidth.
7. Interface with OnlineError Console Commands

CoreOnline provides the backend definitions that allow the engine to translate raw platform error codes into human-readable strings.

Tip: Use this during development to debug platform-specific issues. Proper error translation helps eliminate confusion when a console-specific error (like a PSN network timeout) occurs during cross-play testing.
8. Use CoreOnline Types in Data Assets

If you want to create “Whitelists” or “Admin Lists” in a UDataAsset:

Best Practice: Use FUniqueNetIdRepl for storage. Since raw IDs are not UObject types, they cannot be marked as UPROPERTY easily. Using the wrapper types from CoreOnline ensures your data is correctly reflected and editable in the Unreal Editor, eliminating the need for custom serialization.