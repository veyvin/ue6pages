---
layout: default
title: LiveLinkInterface
---

<!-- ai-generation-failed -->

<h1>LiveLinkInterface</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/LiveLinkInterface/LiveLinkInterface.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ink system in Unreal Engine. It acts as the “contractual” layer between data providers (Sources) and data consumers (the Engine). This module defines the core interfaces, roles, and data structures required to stream real-time animation, transform, and property data from external sources—such as Motion Capture systems, DDC tools (Maya, MotionBuilder), or facial tracking apps—into the engine.

By providing a standardized way to define Subjects and Roles, this module allows developers to create custom streaming integrations that remain compatible with Unreal’s animation blueprints and sequencer, helping to eliminate the need for proprietary, non-standardized networking code for every new device.

Practical Usage Tips and Best Practices
Add Module Dependency
To create custom Live Link sources or handlers in C++, you must add "LiveLinkInterface" to your PublicDependencyModuleNames in your Build.cs file. This provides access to essential classes like ILiveLinkSource and FLiveLinkSubjectKey.
Utilize Live Link Roles
Instead of sending raw data, always wrap your data in a specific Role (e.g., ULiveLinkAnimationRole, ULiveLinkCameraRole). Using the correct role ensures that the engine knows exactly how to interpret the incoming data, helping you eliminate manual bone mapping or coordinate conversion logic in your Animation Blueprints.
Buffer for Smoothness
Live Link data often arrives at different frequencies than the engine’s tick rate. Use the built-in interpolation and buffering settings within the Live Link UI (driven by this module) to eliminate jitter in your character’s movement or camera jitter during high-latency network streams.
Implement ILiveLinkSource for Custom Hardware
If you are building a driver for a new mocap suit or tracking device, implement the ILiveLinkSource interface. This allows your device to appear as a selectable source in the Live Link window, which helps you eliminate the complexity of managing raw UDP/TCP sockets manually within your gameplay code.
Use the Message Bus for DDC Integration
For applications like Maya or Blender, leverage the Message Bus functionality provided by the interface. This allows for automatic discovery of the engine on a local network, helping you eliminate the need for users to manually enter IP addresses to establish a connection.
Optimize with Virtual Subjects
The module supports Virtual Subjects, which allow you to combine or modify multiple live streams into a single output. For example, you can combine a body mocap stream and a facial tracking stream into one “Master Character” subject. This helps you eliminate complexity in the AnimGraph by providing a single source for all character data.
Check Subject Validity
When consuming data in C++ or Blueprints, always verify that the Subject is still active. Streams can drop due to network issues; checking for a valid frame helps you eliminate “T-posing” or snapping to the world origin when a tracker is momentarily obscured.
Leverage Timecode for Precision
The interface supports high-precision timecoding. Ensure your source sends a timecode along with the frame data; this allows the engine to synchronize the stream with the Sequencer and other recorded data, helping you eliminate drift and sync issues during virtual production sessions.