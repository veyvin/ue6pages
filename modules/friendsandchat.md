---
layout: default
title: FriendsAndChat
---

<!-- ai-generation-failed -->

<h1>FriendsAndChat</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/FriendsAndChat/FriendsAndChat.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e designed to manage social interactions within Unreal Engine. It serves as the primary bridge between the Online Subsystem (OSS)—specifically the IOnlineFriends and IOnlineChat interfaces—and the Slate-based UI components used for social overlays.

This module is responsible for rendering friends lists, managing active chat windows, and handling user presence (online/offline/away status). It is frequently used in projects requiring a “Social Overlay” similar to those found in the Epic Games Launcher or modern multiplayer titles, facilitating the elimination of fragmented social UIs by providing a unified communication hub.

Practical Usage Tips and Best Practices
1. Utilize for Social Overlays

When building a multiplayer game that requires a persistent chat or friends list (like a lobby system), use this module to leverage the engine’s built-in social widgets. This facilitates the elimination of the need to build complex scrolling lists and message-handling logic from scratch in UMG.

2. Bind to OnRelationshipUpdated Events

The module relies on the OnRelationshipUpdated delegate from the Social Interface. Ensure your UI logic listens for this event to reflect real-time changes when a player accepts an invite or blocks another user. This practice ensures the elimination of stale data in the player’s social view.

3. Implement “Restart Required” Logic for Privacy

Some social settings (like visibility or chat filtering) may require a session refresh. Use the engine’s notification system to alert the player if a change requires them to rejoin a lobby, aiding in the elimination of desynchronized privacy states between the client and the server.

4. Optimize Presence Updates

Frequent presence updates (e.g., updating a friend’s location every few seconds) can saturate network bandwidth. Use this module to cache presence data locally and only request updates at set intervals, which is a best practice for the elimination of unnecessary network overhead in high-population social hubs.

5. Handle “Elimination” and Status Changes

Use the chat system to broadcast system messages, such as when a player leaves a party or is removed from a session. Properly formatting these system notifications within the FriendsAndChat widgets leads to the elimination of player confusion regarding sudden changes in party composition.

6. Leverage UMG Wrapper Classes

The module ships with base classes for UMG widgets. Instead of modifying the C++ module directly, create a UMG Widget that inherits from the module’s base classes to customize the “look and feel” of the chatbox. This facilitates the elimination of code conflicts when upgrading to newer engine versions.

7. Verify OSS Module Dependencies

The FriendsAndChat module requires a functional Online Subsystem (like Steam or EOS). Ensure the OnlineSubsystem and relevant platform modules are listed in your Build.cs. Correct dependency management leads to the elimination of “Null Subsystem” errors when the social UI fails to initialize.

8. Secure Chat with Sanitization

When passing text through the chat components of this module, always implement a sanitization pass to filter prohibited language or malicious strings. Integrating a robust filter helps in the elimination of toxic behavior and ensures compliance with platform safety requirements.