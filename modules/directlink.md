---
layout: default
title: DirectLink
---

<!-- ai-generation-failed -->

<h1>DirectLink</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Datasmith/DirectLink/DirectLink.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Messaging, MessagingCommon</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

that enables a live, synchronized connection between external 3D design applications and Unreal Engine. It facilitates a “push-button” workflow that removes the need for intermediate file exports.

What it is and What it’s used for

DirectLink acts as a communication bridge that allows Unreal Engine to receive incremental updates from source applications like Revit, Rhino, SketchUp, 3ds Max, and Solidworks. Instead of exporting and re-importing .udatasmith files, DirectLink establishes a network-aware connection that tracks changes in the source scene and mirrors them in the Unreal viewport.

Primary uses include:

Near Real-Time Visualization: Seeing architectural or design changes reflected in Unreal Engine immediately after clicking “Sync” in the source app.
Incremental Updating: Only sending modified geometry or metadata over the link, rather than the entire scene, which drastically speeds up the iteration loop.
Runtime Data Ingestion: Allowing packaged applications (like a custom product configurator) to receive new 3D data from a source application while the game is running.
Multi-Source Aggregation: Connecting multiple different applications (e.g., Revit for architecture and Rhino for furniture) into a single Unreal Engine Level simultaneously.
Practical Usage Tips and Best Practices
1. Manage AutoSync Carefully

While many plugins (like SketchUp) offer a “Toggle AutoSync” feature, use it with caution on complex scenes. Frequent automatic updates can cause the engine to hitch during heavy mesh rebuilds. For large architectural models, it is often better to keep AutoSync off and use the manual Synchronize button to push updates only when a milestone is reached.

2. Utilize the Datasmith Hub

The DirectLink module relies on the Datasmith Hub, a background service that manages connections. If your source application cannot find Unreal Engine, ensure the Hub is running in your system tray. The Hub allows the link to persist even if you close and reopen the Unreal Editor, ensuring the elimination of connection setup overhead.

3. Handle Relative Offsets in Unreal

When you move an object in Unreal that was imported via DirectLink, the engine stores that movement as a Relative Offset. If you then move the same object in your source application (e.g., 3ds Max), the Unreal version will move but will maintain its relative offset. To reset an object to its exact source location, simply zero out its Transform values in the Unreal Details panel.

4. Avoid Heavy Material Overwrites in Unreal

DirectLink tries to preserve your work, but radical changes to material assignments in the source application can sometimes overwrite custom Unreal material assignments. A best practice is to do your material “look-dev” in Unreal and avoid changing material names or IDs in the source app once the link is established.

5. Network-Based Remote Connections

DirectLink is not limited to a single machine; it can work over a local area network (LAN). As long as both machines are on the same subnet and the Datasmith Hub is active, a designer on one PC can push updates to an Unreal Engine instance running on a high-end rendering workstation in another room.

6. Use for Runtime Applications

You can implement DirectLink in your packaged projects using the Datasmith Runtime nodes. By spawning a DatasmithRuntimeActor and using the “Open Connection with Index” node, you can allow your end-users to link their own CAD software to your custom Unreal application for real-time collaborative reviews.

7. Verify Unit Consistency

To prevent scaling issues, ensure your source application’s units match Unreal’s (Centimeters). While the DirectLink module attempts to scale data automatically, discrepancies in “System Units” vs. “Display Units” in apps like 3ds Max can occasionally lead to incorrectly sized actors. Always check a reference scale (like a 1m cube) upon first synchronization.

8. Strategic Elimination of Stale Data

If a scene becomes cluttered or objects are not disappearing after being deleted in the source app, use the Reimport or Clear command on the Datasmith Scene Actor. This forces the DirectLink module to flush its cache and perform a full reconciliation with the source application, ensuring the Unreal Level perfectly matches the source.