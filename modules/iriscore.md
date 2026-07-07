---
layout: default
title: IrisCore
---

<!-- ai-generation-failed -->

<h1>IrisCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Net/Iris/IrisCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, NetCore, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

cation system. Introduced to replace the aging “OOD” (Object Oriented Design) replication system, Iris is a high-performance, push-based replication framework designed specifically for massive player counts and highly interactive worlds (as seen in Fortnite).

While the legacy system relies on “polling” (constantly checking if properties have changed), Iris uses a data-driven approach that minimizes interactions between game logic and the network driver. This significantly reduces server CPU overhead and provides a more scalable architecture for modern multiplayer games.

Practical Usage Tips and Best Practices
1. Enable via Build and Target Configuration

Iris is opt-in and requires specific configuration to activate.

Action: In your *.Target.cs file, set bUseIris = true;. In your module’s *.Build.cs, call SetupIrisSupport(Target);. Finally, enable the plugin in your .uproject file. This ensures the necessary dependencies are linked, eliminating compilation errors when referencing Iris-specific APIs.
2. Transition to Push-Based Replication

Iris performs best when it doesn’t have to scan actors for changes.

Best Practice: Ensure net.IsPushModelEnabled=1 is set in your DefaultEngine.ini. Use the MARK_PROPERTY_DIRTY_FROM_NAME macros in C++ to signal changes. This allows Iris to eliminate the expensive “Compare Properties” phase that traditionally bogs down server performance.
3. Utilize Net Object Filters

Unlike the legacy IsNetRelevantFor virtual function, Iris uses a high-performance filtering system.

Tip: Use the Filtering API to control which connections receive which actors. Iris provides built-in filters like NetObjectGridFilter. By using these data-driven filters, you eliminate thousands of virtual function calls per frame, which is critical for supporting 100+ players.
4. Leverage Data Streams

Iris introduces DataStreams to handle different types of replicated data (e.g., properties vs. RPCs).

Action: If you have custom, high-bandwidth data needs (like telemetry or large state syncs), implement a custom UDataStream. This allows you to set specific bandwidth limits and priorities per stream, helping you eliminate network congestion for critical gameplay data.
5. Optimize with SphereNetObjectPrioritizer

Prioritization in Iris determines which actors get bandwidth when it is limited.

Tip: Actors with a replicated WorldPosition automatically use the SphereNetObjectPrioritizer. You can tune these settings to ensure that actors closest to the player are updated more frequently, effectively eliminating “teleporting” or “laggy” movement for nearby enemies.
6. Use the Iris Replication Bridge

To interact with the system from game code, you must use the UActorReplicationBridge.

Action: Use this bridge to retrieve an actor’s FNetRefHandle. This handle is the “ID” Iris uses to track the actor internally. Using the handle-based API instead of raw actor pointers helps Iris eliminate memory tracking overhead and improves cache locality.
7. Profile with Iris-Specific Insights

Standard network profiling tools may not show the full picture when Iris is active.

Best Practice: Use Unreal Insights with the “Networking” and “Iris” traces enabled. This provides a deep dive into how Iris is batching objects and which filters are consuming the most time, allowing you to eliminate bottlenecks in your replication logic.
8. Maintain Backward Compatibility

Iris is designed to work with existing UPROPERTY(Replicated) declarations.

Tip: You do not need to rewrite your entire codebase to use Iris. Most existing Blueprint and C++ replication will “just work.” Focus your optimization efforts on high-frequency actors (like projectiles or vehicles) to eliminate the most significant performance drains first.