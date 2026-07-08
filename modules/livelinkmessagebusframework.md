---
layout: default
title: LiveLinkMessageBusFramework
---

<!-- ai-generation-failed -->

<h1>LiveLinkMessageBusFramework</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/LiveLinkMessageBusFramework/LiveLinkMessageBusFramework.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, LiveLinkInterface, MessagingCommon, Serialization</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

d discovery logic for Unreal Engine’s Live Link system. It utilizes the engine’s internal Message Bus (a high-performance, asynchronous messaging system) to facilitate communication between external data providers (like Maya, MotionBuilder, or a custom MoCap server) and the Unreal Engine client.

This module is the core technology behind the Message Bus Source, enabling automatic discovery of sources on the same local network. By abstracting the complex socket and protocol management into a structured framework, it facilitates the elimination of manual IP/Port configuration and custom networking code for most animation streaming needs.

Practical Usage Tips and Best Practices
1. Implement ILiveLinkProvider for External Tools

If you are building a standalone C++ application to stream data into Unreal, use the ILiveLinkProvider::CreateLiveLinkProvider function. This automatically handles the discovery handshake via the message bus. This practice leads to the elimination of complex setup for end-users, as the engine will “see” your application as soon as it starts.

2. Use “UpdateSubject” for Structural Changes

When a subject (like a character skeleton) is first connected, or if the bone hierarchy changes, you must call UpdateSubject. This sends the static data (the “blueprint” of the subject) to the engine. Proper use of this function ensures the elimination of data mismatches between your external provider and the Live Link Subject in the editor.

3. Optimize with “UpdateSubjectFrame” for Motion

For the high-frequency streaming of transforms, use UpdateSubjectFrame. This function is optimized for the continuous transmission of frame-specific data like bone rotations and locations. Utilizing this specific framework call facilitates the elimination of latency and jitter that occurs when trying to send static and dynamic data in the same packet.

4. Configure UDP Messaging for Network Discovery

The Message Bus relies on the UDP Messaging plugin. In your Project Settings, ensure that “Enable Transport” is checked and your “Unicast Endpoint” is correctly set (usually 0.0.0.0:0). Correct network configuration is essential for the elimination of “Invisible Source” bugs where the external tool is running but the engine cannot detect it.

5. Handle “Elimination” of Stale Subjects

When your external provider stops streaming or a specific subject is removed, the framework should signal the engine to remove that subject from the Live Link UI. Properly managing the lifecycle of your subjects leads to the elimination of “phantom” subjects in the Live Link Client, preventing designers from accidentally trying to bind to dead data streams.

6. Utilize the Built-in Maya/MotionBuilder Examples

Before writing a custom implementation from scratch, examine the source code for the Maya Live Link plugin located in Engine\Source\Programs\MayaLiveLinkPlugin\. Using these as a template for your own LiveLinkMessageBusFramework implementation assists in the elimination of architectural mistakes and ensures compatibility with engine standards.

7. Buffer Data to Eliminate Network Jitter

The framework allows for buffering on the client side. In the Live Link Subject settings within Unreal, you can adjust the “Interpolation” or “Pre-roll” settings. Tuning these values is a best practice for the elimination of “stuttering” animations caused by minor fluctuations in network packet delivery over a Wi-Fi or congested LAN connection.

8. Verify Build.cs Dependencies

If you are creating an Unreal plugin that acts as a custom Message Bus source, you must include "LiveLinkMessageBusFramework", "LiveLinkInterface", and "Messaging" in your Build.cs. Correctly declaring these dependencies is the first step toward the elimination of linker errors when trying to create a ULiveLinkMessageBusSourceFactory.