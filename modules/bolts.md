---
layout: default
title: Bolts
---

<!-- ai-generation-failed -->

<h1>Bolts</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/IOS/Bolts/Bolts.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e Bolts-Tasks library, originally developed by Facebook. It is a lightweight, asynchronous programming framework used to manage complex sequences of background tasks without falling into “callback hell.”

In the context of Unreal Engine, this module is primarily a dependency for mobile-specific plugins, particularly those involving Facebook SDK integration, social features, or certain mobile advertising backends. It provides a way to handle asynchronous operations (like network requests or database queries) using “Tasks” that can be chained together, ensuring that each step executes only after the previous one completes.

1. Understand its Role as a Dependency

In most Unreal projects, you will not interact with the Bolts module directly. It is typically pulled in automatically when you enable social or mobile plugins. If you are troubleshooting build errors related to “Bolts,” ensure that your mobile SDKs (like the Facebook plugin) are correctly configured in your Build.cs.

2. Chaining Asynchronous Operations

The core of Bolts is the Task object. If you are writing custom integration code for mobile services, use the continueWith: pattern (or its C++ equivalent in the module) to chain logic. This ensures that the next block of code only runs once the current background task—such as authenticating a user—has finished.

3. Avoid Blocking the Game Thread

Like all asynchronous systems in Unreal, ensure that the work being done inside a Bolts task is actually offloaded to a background thread. Performing heavy computations inside a task that is forced to run on the Game Thread will eliminate the performance benefits and cause the UI to hitch.

4. Correct Header Inclusion

If you need to interface with Bolts in C++ (for example, when extending a third-party mobile plugin), ensure you include the correct module dependency in your Project.Build.cs file:

C#
PublicDependencyModuleNames.AddRange(new string[] { "Bolts" });
Copy code

This is essential for the linker to resolve the task-based symbols during the compilation of your mobile targets.

5. Handle Task Failures Gracefully

Bolts tasks can succeed, fail, or be cancelled.

Best Practice: Always check the state of the task in your continuation blocks. If a task fails (e.g., a network timeout during a social login), your code must handle the error to prevent the game logic from hanging or crashing.
6. Use for Sequential API Calls

If a mobile service requires you to call API A, then API B using a result from A, and finally API C, Bolts is the ideal tool. It allows you to write this sequence linearly rather than nesting multiple levels of delegates, which makes the code significantly easier to debug and maintain.

7. Thread Safety with UI Updates

Bolts tasks often complete on background threads.

Important: If a task completion needs to trigger a UI change (like updating a player’s name on a widget), you must dispatch that call back to the Game Thread (using AsyncTask(ENamedThreads::GameThread, ...)). Attempting to update UMG directly from a Bolts background task will result in a crash.
8. Memory Management and Lifetimes

Be cautious with the lifetime of objects captured in Bolts task lambdas. If you capture this or a pointer to a local actor, and that actor is eliminated (destroyed) before the background task completes, the task will attempt to access invalid memory.

Tip: Always use weak pointers (TWeakObjectPtr) when capturing Unreal Actors or Objects inside asynchronous task callbacks.