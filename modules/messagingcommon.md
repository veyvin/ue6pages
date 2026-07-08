---
layout: default
title: MessagingCommon
---

<!-- ai-generation-failed -->

<h1>MessagingCommon</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/MessagingCommon/MessagingCommon.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

asses required for the Unreal Engine Message Bus. It serves as the foundational bridge between the low-level Messaging API and higher-level implementations like UDP Messaging or Live Link.

Its primary purpose is to define how messages are addressed, routed, and contextualized across different threads or network instances. By providing a standardized way to wrap data into “Message Contexts,” it allows disparate systems—such as the Editor, a running Game instance, or external tools like Maya—to communicate without having direct dependencies on one another. This helps you eliminate tight coupling between your game systems and external automation tools.

Practical Usage Tips and Best Practices
Define Messages as Simple Structs
Messages in this framework should be defined as USTRUCT types. This module treats these structs as data packets. Keep them “lean” by using POD (Plain Old Data) and avoiding UObject pointers, which helps you eliminate serialization overhead and memory management issues during cross-thread communication.
Use FMessageAddress for Routing
Every message sender and recipient is identified by an FMessageAddress (a unique GUID). When building complex tools, use these addresses to “target” specific listeners. This allows you to eliminate broadcast “noise” by sending messages directly to a known entity rather than the entire bus.
Leverage IMessageContext for Metadata
When a message is received, it is wrapped in an IMessageContext. Use this to inspect the sender’s address, the timestamp, and the “Forwarding” history. Accessing this metadata helps you eliminate logic errors when multiple instances (like different PIE sessions) are sending the same type of message.
Implement Message Scoping
Use the EMessageScope enumeration to define how far a message should travel. For instance, setting a scope to Process ensures the message never leaves the local application, helping you eliminate unnecessary network traffic on the Message Bus.
Handle Thread Safety via Message Handlers
The Message Bus is inherently asynchronous. When subscribing to a message type, specify a ENamedThreads target (e.g., GameThread). This ensures the module dispatches the callback on the correct thread, helping you eliminate race conditions and crashes when updating UI or Actors from a background message.
Bridge to Networked Instances via UDP
While MessagingCommon defines the “what,” the UDP Messaging plugin defines the “how” for networking. Ensure your Project Settings allow for the “Static Endpoints” if you are trying to communicate with a mobile device on a different subnet. This helps you eliminate connection timeouts in multi-device testing.
Utilize the Message Bus for Tooling
For custom Editor Utility Widgets or standalone C++ programs, use this module to send “Remote Control” commands to a running game. It is the best way to eliminate the need for custom socket programming when building internal development tools.
Clean Up Subscriptions on Elimination
When the object owning a message subscription is destroyed (the “elimination” of a tool or actor), always call Unsubscribe. Failing to do so can lead to the Message Bus attempting to call functions on garbage-collected memory, which you must eliminate to ensure engine stability.