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

ming data received by the Live Link system and the Unreal Engine animation pipeline.

Description and Purpose

While the base Live Link module handles the networking and reception of data from external sources (like MotionBuilder, Maya, or iPhone facial capture), LiveLinkAnimationCore specifically provides the logic to interpret that data as animation. Its primary purpose is to define the Live Link Role for animation and provide the specialized nodes for Animation Blueprints. It allows the engine to map incoming bone transforms, curve values, and blend shapes onto a Skeletal Mesh in real-time, enabling high-fidelity performance capture and virtual production workflows.

Practical Usage Tips and Best Practices
Use the Live Link Pose Node
The most common way to utilize this module is by placing the Live Link Pose node inside your Animation Blueprint’s AnimGraph. Selecting the correct “Subject Name” here is the most efficient way to eliminate latency and drive your character with external motion data instantly.
Implement a Retarget Asset
Incoming data rarely matches your character’s skeleton perfectly. Create a Live Link Retarget Asset (a C++ or Blueprint class) to define how source bones map to target bones. Proper mapping helps you eliminate “spaghetti” limbs or inverted joints during a live session.
Leverage Property/Curve Remapping
If your source (like an iPhone) uses different naming conventions for blend shapes than your character model (e.g., EyeBlink vs Blink_L), use the remapping functions within this module. This allows you to eliminate the need to rename hundreds of morph targets on your 3D assets.
Synchronize via Live Link Hub
In professional setups, use the Live Link Hub application alongside this module. It centralizes multiple sources and streams them to the engine as a single coordinated clock. This helps you eliminate jitter and out-of-sync issues between facial capture and body motion.
Utilize the “Use Interpolation” Setting
Live Link data can sometimes be choppy due to network fluctuations. Enabling interpolation within the Live Link Pose node settings allows the engine to smooth out the transition between frames, which helps you eliminate visual “popping” or stuttering in the character’s movement.
Check Subject Validity with “Get Live Link Subjects”
Before applying a pose, use the C++ or Blueprint functions provided by this module to verify if a subject is actually active and “valid.” Checking this status helps you eliminate the “T-Pose” glitch that occurs when a character suddenly loses its tracking source.
Optimize with “Offset” and “Scale” Adjustments
If your capture volume’s origin doesn’t match your Unreal level’s world origin, use the offset properties in the Live Link controller. Adjusting these values directly in the animation core helps you eliminate the need for manual, frame-by-frame transform corrections in Sequencer.
Profile Latency with the Live Link Debugger
Use the Live Link UI to monitor the “Timing” of incoming animation packets. If the delay is too high, you can adjust the “Buffer Size” in the source settings. Finding the right balance between buffer depth and latency helps you eliminate “floaty” controls in interactive virtual productions.