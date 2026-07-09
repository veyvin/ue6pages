---
layout: default
title: BandwidthDebugDelegates
---

<!-- ai-generation-failed -->

<h1>BandwidthDebugDelegates</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Online/Experimental/BandwidthDebugDelegates/BandwidthDebugDelegates.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

in Unreal Engine’s networking stack. It provides a centralized set of delegates that developers can bind to in order to monitor raw network traffic, packet events, and bandwidth usage in real-time.

Instead of modifying low-level NetDriver or NetConnection code, this module allows you to “hook” into the network stream to extract metadata for debugging tools, custom UI overlays, or telemetry systems. It is essential for developers who need to visualize how much data specific actors or RPCs are consuming during gameplay.

Practical Usage Tips and Best Practices
Bind to Global Debug Delegates
Use the singleton access provided by the module (often found via FBandwidthDebugDelegates::Get()) to subscribe to events like packet transmission or receipt. This allows you to “eliminate” the need to subclass the UNetDriver just to log traffic.
Implement Custom Network Overlays
Use the data from these delegates to drive a custom “Network Debug” UI. By binding to bandwidth-per-connection delegates, you can show real-time graphs to players or testers, helping them identify if a specific “elimination” effect or massive physics update is causing a bandwidth spike.
Validate Packet Loss and Jitter
These delegates often provide access to raw packet headers or delivery notifications. Use this to “eliminate” guesswork when debugging “teleporting” players; if the delegates report high packet drop rates precisely when a certain ability is used, you’ve found your culprit.
Integrate with Unreal Insights
While the engine has built-in Networking Insights, you can use these delegates to send custom “user markers” to the trace stream. This helps you correlate specific gameplay events (like a match-ending “elimination”) with a sudden surge in bandwidth within the Insights timeline.
Filter Traffic by Actor Class
In your delegate callbacks, check the NetGUID or class of the objects being replicated. This is a best practice for “eliminating” noise in your logs—only log data for specific “heavy” actors (like vehicles or destructibles) that you are currently optimizing.
Conditional Compilation for Performance
Ensure that any code binding to these delegates is wrapped in #if !UE_BUILD_SHIPPING blocks. Monitoring raw bandwidth via delegates adds overhead to the network thread; you should “eliminate” this logic in final builds to ensure maximum performance for players.
Add Module Dependencies
To access these delegates in C++, you must add the module to your Build.cs. It is typically used in conjunction with Engine and NetCore.
C#
	// In YourProject.Build.cs

	if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PublicDependencyModuleNames.Add("BandwidthDebugDelegates");

	}
Copy code
Monitor Outbound Congestion
Use the delegates to track the “saturation” of the outbound buffer. If the delegates report that the “bytes queued” is consistently rising, you can programmatically trigger an “elimination” of non-essential traffic, such as lowering the frequency of cosmetic particle replication until the network stabilizes.