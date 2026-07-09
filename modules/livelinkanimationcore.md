---
layout: default
title: LiveLinkAnimationCore
---

<!-- ai-generation-failed -->

<h1>LiveLinkAnimationCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/LiveLinkAnimationCore/LiveLinkAnimationCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, LiveLinkInterface</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

k data-streaming framework and Unreal Engine’s Animation Blueprint system. While the base Live Link module handles the network connection and data reception, this module provides the specific animation nodes, retargeting logic, and skeletal structures required to apply that data to a character. It is the primary engine component used for real-time motion capture (MoCap), facial performance streaming (like Live Link Face), and DDC tool syncing (Maya/MotionBuilder).

Practical Usage Tips & Best Practices
1. Use the Live Link Pose Node in AnimBPs

The most direct way to use this module is through the Live Link Pose node within an Animation Blueprint’s AnimGraph.

Best Practice: Place this node as early as possible in your graph if you intend to layer additional logic (like IK or physics) on top of the live data. This allows for the elimination of jitter by letting the engine’s built-in smoothing and IK solvers clean up the raw MoCap data before final output.
2. Implement Custom Remap Assets

Different MoCap systems use different bone naming conventions (e.g., “LeftUpLeg” vs. “thigh_l”). The ULiveLinkRetargetAsset class within this module handles this translation.

Tip: Create a Blueprint derived from LiveLinkRetargetAsset and override the GetRemappedBoneName function. This facilitates the elimination of manual bone renaming in your external software by dynamically mapping incoming names to your Unreal Skeleton’s names.
3. Leverage Virtual Subjects for Multi-Source Data

Often, you may have body data coming from one source and facial data from another (e.g., an iPhone).

Best Practice: Use the Live Link Hub or the Virtual Subject feature to combine these into a single stream. This results in the elimination of complex AnimGraph setups, as you only need a single Live Link Pose node to drive the entire character’s performance.
4. Monitor Subject Status with “On Live Link Updated”

The module provides a specialized component called the Live Link Skeletal Animation Component.

Tip: Use this component’s OnLiveLinkUpdated event to trigger logic only when new data arrives. This is more efficient than using a standard Tick event and assists in the elimination of “stale” poses where the character remains frozen in a T-pose if the stream is interrupted.
5. Optimize Performance via Thread Safety

Animation updates in Unreal occur on a worker thread. The nodes in LiveLinkAnimationCore are designed to be thread-safe to prevent game-thread bottlenecks.

Best Practice: Avoid calling heavy C++ or Blueprint logic inside your Remap Asset’s functions. Keeping these functions “pure” ensures the elimination of thread-sync hitches, maintaining a high frame rate even during complex performance captures.
6. Utilize Buffering and Interpolation

Raw network data can be “bursty,” leading to visual stutters in the animation.

Tip: In the Live Link panel, adjust the Interpolation and Offset settings for your subject. Adding a small buffer (e.g., 0.03s) results in the elimination of frame-skipping and ensures smooth motion even over unstable Wi-Fi connections.
7. Debug with the Live Link Debugger

If a character isn’t moving, it is often difficult to tell if the issue is the network, the skeleton, or the material.

Best Practice: Use the console command LiveLink.ShowDebug 1. This overlay displays active subjects and their frame rates, leading to the elimination of guesswork when troubleshooting connectivity issues between your MoCap hardware and the engine.
8. Use “Evaluate Live Link Frame” for Non-Skeletal Data

Sometimes you need to drive simple transforms or light intensities via Live Link without a full skeleton.

Tip: Use the Evaluate Live Link Frame node in a standard Blueprint. This allows you to pull specific property values (like a camera’s focal length or a light’s color) directly from the stream, ensuring the elimination of manual keyframing for virtual production environments.