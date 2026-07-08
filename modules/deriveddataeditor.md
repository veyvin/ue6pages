---
layout: default
title: DerivedDataEditor
---

<!-- ai-generation-failed -->

<h1>DerivedDataEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/DerivedDataEditor/DerivedDataEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DerivedDataCache, DerivedDataWidgets, EditorFramework, EditorSubsystem, Engine, InputCore, MessageLog, OutputLog, Slate, SlateCore, ToolMenus, ToolWidgets, UnrealEd, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ions, status reporting, and manual management tasks associated with this data. It is responsible for the “Compiling Shaders” progress bars, the “Building Texture” notifications, and the background synchronization of assets when using a Cloud DDC or Zen Store. It ensures that the editor remains usable while assets are being processed and provides tools to troubleshoot cache misses or latency issues.

Practical Usage Tips and Best Practices
1. Monitor the DDC Status Bar

In the bottom-right corner of the editor, the DerivedDataEditor module populates the status bar during asset processing. If you notice persistent “Building” notifications, it usually indicates a “cache miss,” meaning your local or shared DDC does not have the required data. This is a cue to check your network connection if you are relying on a shared team cache.

2. Prime the Cache with the Commandlet

To avoid long wait times when opening a project for the first time, use the DerivedDataCache commandlet. Run UnrealEditor.exe ProjectName -run=DerivedDataCache -fill from your terminal. This instructs the module to pre-generate and cache all required data for your project, ensuring a smooth, high-performance experience for the rest of your team.

3. Use “NoShared” for Remote Work

If you are working from home via VPN, the latency to a shared office DDC can actually be slower than just building the data locally. You can override the module’s behavior by launching the editor with the -ddc=NoShared argument. This forces the engine to use only your local disk for derived data, eliminating the “hangups” caused by network latency.

4. Debug with LogDerivedDataCache

If you suspect the DDC is not working or is taking too long to fetch data, search your Output Log for the LogDerivedDataCache category. The DerivedDataEditor module prints detailed performance metrics here, including the time taken to fetch assets and whether the data was retrieved from a local, shared, or cloud source.

5. Relocate the Local Cache to a Fast Drive

By default, the DDC can grow to tens of gigabytes. Use the Editor Preferences (under Data Cache) to move the “Local Derived Data Cache Location” to your fastest NVMe SSD. This significantly speeds up the time it takes for the editor to load processed assets and improves the responsiveness of the Content Browser.

6. Deactivate High-Latency Shared Caches

To prevent the editor from freezing while waiting for a slow server, you can set a latency threshold in your DefaultEngine.ini. Adding DeactivateAt=40 to your shared DDC configuration tells the module to stop attempting to use the shared cache if the ping exceeds 40ms, automatically falling back to local generation.

7. Handle Cache Elimination and Cleanup

When you update a plugin or change a core shader function, the old cached data becomes obsolete. While the engine handles most of this automatically, you can manually trigger an elimination of old data by deleting the DerivedDataCache folder in your project or engine directory. This is a common “first step” in troubleshooting visual artifacts or persistent shader compilation errors.

8. Verify Zen Store Connectivity

For Unreal Engine 5.5 and 5.6, the DerivedDataEditor module heavily utilizes the Zen Store. Ensure the Zen dashboard shows an “Active” status. If the module cannot connect to the Zen local service, it will fall back to legacy file-system caching, which is significantly slower and can lead to increased disk fragmentation.