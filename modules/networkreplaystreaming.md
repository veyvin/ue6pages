---
layout: default
title: NetworkReplayStreaming
---

<!-- ai-generation-failed -->

<h1>NetworkReplayStreaming</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/NetworkReplayStreaming/NetworkReplayStreaming/NetworkReplayStreaming.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core, Json, NetCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

eplay System. It acts as a bridge between the DemoNetDriver (which records network traffic) and the storage medium where that data is kept. This module allows you to record gameplay sessions and play them back later by streaming the replicated data back into the game world.

It supports multiple “Streamer” implementations, such as the LocalFileStreamer (for local disk), the HttpStreamer (for remote servers), and the InMemoryStreamer (for “Instant Replay” or “Elimination Cam” features). By leveraging this module, you can eliminate the need for custom, frame-by-frame recording logic, as it reuses the engine’s existing replication system.

Practical Usage Tips and Best Practices
Choose the Right Streamer Factory
In your DefaultEngine.ini, you can set the DefaultFactoryName to determine how replays are stored. Use LocalFileNetworkReplayStreaming for single-player or local replays, and HttpNetworkReplayStreaming for dedicated server environments where replays are uploaded to a central database. This helps you eliminate local storage bottlenecks on client machines.
Optimize Checkpoint Frequency
Checkpoints are “snapshots” of the world that allow players to jump to specific times in a replay. Use the CVar demo.CVarCheckpointUploadDelayInSeconds to balance between file size and scrubbing speed. Higher frequency makes seeking faster but increases disk usage; tuning this helps you eliminate long wait times when a user “scrubs” the timeline.
Implement ‘Elimination Cams’ with Memory Streaming
For competitive shooters, use the InMemoryNetworkReplayStreaming factory. This stores the last X seconds of gameplay in a circular buffer in RAM. This allows you to play back an “elimination” sequence immediately without hitting the hard drive, which helps you eliminate hitches or stutters during high-action moments.
Use ‘ReplayRewindable’ for Critical Actors
If an actor needs to maintain its state accurately during scrubbing, set bReplayRewindable = true. This ensures the actor is not destroyed and recreated during a “GoToTime” request, helping you eliminate visual glitches or logic resets for important gameplay entities like the local player or scoreboards.
Amortize Recording Costs
Recording a checkpoint can be CPU-intensive. Use the CVar demo.CheckpointSaveMaxMSPerFrame to spread the cost of saving a checkpoint across multiple frames. This practice helps you eliminate “hiccups” or frame drops that occur when the system tries to serialize the entire world state in a single tick.
Manage Backward Compatibility
The replay system supports versioning. Use FNetworkVersion::GetLocalNetworkVersionOverride to assign a version to your builds. If a replay is recorded on an older version, the module can skip removed properties, which helps you eliminate crashes when players try to watch replays from an older patch of your game.
Utilize Replay Spectator Controllers
Define a specific ReplaySpectatorPlayerControllerClass in your GameMode. This controller can have different relevancy rules than a normal player, such as a larger “Culling Distance.” This allows the replay to record events happening far away from the player, helping you eliminate “empty” areas when viewing the game from a free-roaming camera.
Clean Up Replay Data on Elimination
When a match ends or a replay is no longer needed (the “elimination” of the session data), ensure you call DeleteReplay. For the HTTP streamer, this sends a DELETE request to your server. Properly managing the lifecycle of these files helps you eliminate “ghost” files that clutter up the user’s storage or your cloud database.