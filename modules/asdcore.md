---
layout: default
title: ASDCore
---

<!-- ai-generation-failed -->

<h1>ASDCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Windows/ASDCore/ASDCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ork within Unreal Engine designed to facilitate the communication, acquisition, and management of assets sourced through Epic Games’ ecosystem, primarily Fab. It serves as the underlying bridge between the Unreal Editor and the external asset repositories, handling the secure downloading, versioning, and local integration of content.

This module is essential for modern development pipelines that rely on the seamless “direct-to-engine” import of high-quality assets, textures, and plugins without requiring manual file management.

Practical Usage Tips and Best Practices
Editor-Only Scoping The ASDCore module is strictly an Editor-only utility. It handles the management of asset metadata and downloads during the development phase. Ensure it is only included in your Editor.Build.cs file; including it in a runtime build will cause the packaging process to “eliminate” your binary due to linker errors.
Verify Fab Connectivity If assets are failing to import or appear corrupted, check the logs for LogASDCore. This module is sensitive to network interruptions. Ensuring a stable connection is the best way to “eliminate” partial download errors that lead to broken asset references.
Manage Local Cache Bloat ASDCore stores downloaded metadata and temporary files in the project’s DerivedDataCache (DDC) and Saved folders. Periodically “eliminate” old cached data if you find your disk space is disappearing after importing many large assets from Fab.
Synchronize Multi-User Environments In a collaborative environment using Perforce or Git, remember that ASDCore handles the acquisition of assets, but the resulting files must be submitted to source control manually. Ensure one team member imports the asset and submits it to “eliminate” the risk of others having missing references.
Handle Asset Versioning When an asset is updated on Fab, ASDCore may notify the editor of a newer version. It is a best practice to backup your current work before updating, as the new version will “eliminate” and replace the local version of the asset, potentially breaking existing scene references.
Troubleshoot Import Conflicts If a plugin or asset fails to install, ASDCore often generates a lock file in the Intermediate directory. If the editor crashes during an import, manually “eliminate” the ASD related folders in the project’s Intermediate directory to reset the module’s state.
Optimize Large Downloads When importing massive Megascans or high-resolution environments via ASDCore, avoid running heavy compilation tasks in the background. ASDCore uses high-priority disk I/O, and competing processes can “eliminate” the speed benefits of the direct import system.
Permissions and Firewall Rules Ensure that your workstation’s firewall allows the Unreal Editor to communicate with Epic’s asset domains. If blocked, ASDCore will fail silently, “eliminating” your ability to browse or download new content directly into the Content Browser.