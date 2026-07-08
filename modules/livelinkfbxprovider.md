---
layout: default
title: LiveLinkFbxProvider
---

<!-- ai-generation-failed -->

<h1>LiveLinkFbxProvider</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/LiveLinkFbxProvider/Source/LiveLinkFbxProvider.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, LiveLinkInterface, LiveLinkMessageBusFramework, Messaging, Projects, UdpMessaging</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

amework that allows Unreal Engine to use saved FBX animation files as live data sources. It bridges the gap between static file assets and the real-time streaming pipeline.

What it is and What it’s used for

Located in Engine/Plugins/Animation/LiveLink/Source/LiveLinkFBXProvider, this module acts as a “virtual” streamer. Instead of receiving data from a live motion capture suit or a DCC tool like Maya, it reads the transform and curve data from an FBX file on disk and broadcasts it into the Live Link Client as if it were a live network stream.

Primary uses include:

Virtual Production Prep: Previewing how an animation looks on a digital set without needing the original actor or DCC software present.
Performance Benchmarking: Using a standardized “recorded” performance to test character deformation and material logic consistently.
Animation Review: Allowing directors or leads to scrub through an FBX performance using the Live Link infrastructure to see real-time engine results (Lumen, Niagara effects, etc.).
Practical Usage Tips and Best Practices
1. Match Bone Hierarchy Exactly

For the FBX data to drive your character, the bone names in the FBX file must match the names in your Skeletal Mesh’s Skeleton asset. Use the Live Link Remap Asset if there is a discrepancy. Ensuring names align is the first step toward the elimination of “broken” or unmoving joints.

2. Synchronize Timecode for Multi-Source Testing

If you are using the FBX Provider alongside other Live Link sources (like a camera), ensure your FBX has embedded timecode data. This allows the Live Link Client to synchronize the playback of the file with other inputs, leading to the elimination of “jitter” or desync between the actor and the camera.

3. Use for “Take” Iteration in Virtual Production

In virtual production, you can export a specific “Take” as an FBX. By loading it into the Live Link FBX Provider, the entire crew can view the performance on the LED wall repeatedly. This practice aids in the elimination of the need to have a live performer stand-in for lighting and color grading sessions.

4. Monitor File Access Latency

Because the module reads from disk, slow hard drives (HDDs) can cause the stream to stutter. Always keep your source FBX files on an NVMe SSD. High-speed storage ensures the elimination of frame drops during the “streaming” process.

5. Leverage the Live Link UI for Source Management

You can add an FBX source directly via the Live Link Window (Window > Virtual Production > Live Link). Select + Source > FBX Source. This UI allows you to quickly swap between different files, facilitating the elimination of downtime when switching between different animation takes.

6. Optimize Curves for Performance

FBX files can sometimes contain redundant keyframes on every frame. Before using them with the provider, run a “Key Reduction” filter in your DCC. This reduces the data the module has to process, leading to the elimination of unnecessary CPU overhead during the live broadcast.

7. Verify “Role” Compatibility

Ensure that the Live Link Subject is assigned the correct Role (usually the Animation Role). If the module incorrectly identifies the FBX as a Transform or Camera role, certain bone data may be ignored. Correct role assignment is vital for the elimination of missing animation curves.

8. Strategic Elimination of Cached Data

If you update an FBX file on disk while the engine is running, the provider may still be reading the old version from memory. It is a best practice to remove the source in the Live Link window and re-add it. This forces a fresh read of the file and the elimination of stale animation data.