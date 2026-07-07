---
layout: default
title: PluginWarden
---

<!-- ai-generation-failed -->

<h1>PluginWarden</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/PluginWarden/PluginWarden.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core, CoreUObject, EditorFramework, Engine, InputCore, LauncherPlatform, PortalServices, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

for entitlement verification and license management for plugins purchased through Fab or the Unreal Engine Marketplace.

Description and Purpose

This module is responsible for communicating with the Epic Games backend to ensure that the current user has the legal right (an entitlement) to use a specific plugin within the project. Its primary purpose is to verify license keys and account-based permissions during the engine’s startup and when browsing the plugin library. By integrating this system, the engine can eliminate unauthorized use of premium tools while providing a seamless “click-to-verify” workflow for developers who have purchased legitimate commercial licenses.

Practical Usage Tips and Best Practices
Resolve “Plugin Not Authorized” Errors
If a purchased plugin fails to load with an authorization error, check the PluginWarden status in your logs. Often, simply logging out and back into the Epic Games Launcher is the fastest way to eliminate credential desync issues that prevent the warden from verifying your seat.
Ensure Offline Grace Periods
The PluginWarden is designed to allow for temporary offline use. However, it requires a successful “handshake” while online at least once. If you are preparing for an offline development session (e.g., traveling), launch the project once while connected to the internet to eliminate the risk of being locked out of your plugins.
Use for Enterprise License Management
For large studios, PluginWarden helps manage “per-seat” licenses. If you receive a warning that too many seats are active, use the warden’s interface (via the Plugins menu) to deactivate unused instances. This helps you eliminate license compliance risks across a distributed team.
Monitor Startup Logs for Warnings
If the engine takes an unusually long time to start, check the logs for LogPluginWarden. If the module is struggling to reach the backend, it can cause a hang. You can often eliminate these delays by verifying your firewall isn’t blocking the specific Epic Games API endpoints used for entitlement checks.
Manage Fab Entitlements Post-Migration
As plugins move to Fab, the PluginWarden is the primary system that reconciles old Marketplace purchases with the new store. If a plugin is missing, use the “Refresh” or “Verify” options within the Plugins window to trigger the warden to update your local entitlement cache.
Differentiate Between Project and Engine Plugins
PluginWarden behaves differently depending on where a plugin is installed. To eliminate potential verification loops, prefer installing commercial plugins to the Engine/Plugins/Marketplace folder rather than the local project folder when working across multiple projects with a single license.
Validate Beta and Trial Versions
Some developers offer time-limited trials. The PluginWarden tracks the expiration dates of these entitlements. Keep an eye on the “Days Remaining” status in the plugin description to eliminate sudden workflow interruptions when a trial period ends.
Check for Dependency Authorization
If a premium plugin depends on another premium plugin, the PluginWarden must verify both. If the “parent” plugin is disabled or unauthorized, the warden will automatically eliminate the child plugin’s ability to load, so always verify the full dependency chain in the .uplugin descriptor.