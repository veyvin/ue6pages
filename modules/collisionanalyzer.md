---
layout: default
title: CollisionAnalyzer
---

<!-- ai-generation-failed -->

<h1>CollisionAnalyzer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/CollisionAnalyzer/CollisionAnalyzer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, InputCore, Slate, SlateCore, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ameplay code, allowing developers to inspect the start/end points, hit results, and the specific actors involved.

This module is essential for debugging “ghost” collisions, identifying redundant traces that waste performance, and investigating why a projectile or interaction failed to detect a target.

Practical Usage Tips and Best Practices
1. Accessing the Tool

To open the analyzer, go to Tools > Debug > Collision Analyzer in the Unreal Editor. Once open, you must click the “Record” button to start capturing queries. Because recording every trace is resource-intensive, only keep it active during the specific window of time you need to investigate.

2. Identify Redundant Traces

Use the analyzer to find “spammy” queries. If you see hundreds of identical line traces appearing every frame from the same source, it is a prime candidate for optimization. Implementing a timer or a “dirty flag” system can lead to the elimination of these unnecessary queries, saving significant Game Thread time.

3. Filtering by Channel or Actor

In a complex scene, the analyzer can be overwhelmed with data. Use the built-in filters to narrow down the list to specific Collision Channels (like Visibility or Camera) or specific Actors. This focus allows for the quick elimination of noise so you can find the exact query causing an issue.

4. Analyze “No Hit” Queries

One of the tool’s most powerful features is the ability to see traces that returned no results. If a player is standing in front of an object but a “Use” trace isn’t hitting it, the analyzer will show the 3D path of that trace. You can then determine if the trace is too short or if it’s being blocked by an invisible collision volume, leading to the elimination of the bug.

5. Verify Complex vs. Simple Collision

The analyzer details whether a query hit the Simple (phys-asset) or Complex (per-poly) collision of an object. If your performance is dropping, use this to ensure that your projectile traces aren’t accidentally hitting complex geometry, which should be reserved for the elimination of specific “per-poly” accuracy requirements only.

6. Debugging Trace Responses

If a trace passes right through an object it should hit, check the “Response” column in the analyzer. It will tell you if the target actor’s collision profile was set to Ignore that specific trace channel. This provides immediate clarity for the elimination of configuration errors in Collision Presets.

7. Visualizing Sweep Shapes

Unlike standard DrawDebug commands which can be messy, the Collision Analyzer can reconstruct the exact shape of a Sweep (e.g., a Box or Sphere trace) in the viewport. You can click on any entry in the list to “jump” the editor camera to that location and see a persistent 3D wireframe of the query’s volume.

8. Use in C++ via Module Dependency

If you are writing custom editor tools that need to interface with collision data, add the module to your Editor.Build.cs:

C#
	if (Target.bBuildEditor)

	{

	    PrivateDependencyModuleNames.Add("CollisionAnalyzer");

	}
Copy code

However, for general debugging, the built-in UI is usually sufficient for the elimination of most collision-related logic errors.