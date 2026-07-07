---
layout: default
title: MarketplaceKit
---

<!-- ai-generation-failed -->

<h1>MarketplaceKit</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/IOS/MarketplaceKit/MarketplaceKit.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

process of preparing, validating, and submitting content to Fab (formerly the Unreal Engine Marketplace).

Description and Purpose

This module acts as the technical bridge between a developer’s local project and the commercial distribution pipeline. Its primary purpose is to ensure that assets meet the strict technical standards required for public distribution. It provides automated checks for folder structures, naming conventions, and asset dependencies. By utilizing this kit, creators can eliminate the common “back-and-forth” with the curation team caused by technical rejections, as it identifies violations—such as hard-coded paths or missing redirectors—before the content is even uploaded.

Practical Usage Tips and Best Practices
Run the Automated Validation Tool
Before submitting, use the validation tool provided by this module to scan your project. It checks for common pitfalls like empty folders or invalid characters in filenames. Running this scan early helps you eliminate the risk of your submission being rejected for “Technical Non-Compliance.”
Enforce the “Plugins” Folder Structure
If you are submitting a plugin, ensure all your assets are contained within the plugin’s Content folder rather than the project’s root Content folder. MarketplaceKit looks for this isolation to eliminate dependency errors when a customer installs your product into their own unique project.
Clean Up Redirectors Regularly
Unreal creates “Redirectors” when you move files, which can break when assets are migrated to a new engine version. Use the “Fix Up Redirectors” command in folders flagged by MarketplaceKit to eliminate broken references that would otherwise prevent your assets from loading for the end-user.
Verify Multi-Engine Version Compatibility
Use the module’s configuration to test your content against multiple engine versions (e.g., 5.3, 5.4, and 5.5). This allows you to eliminate version-specific bugs, such as deprecated nodes in Blueprints or shader incompatibilities, ensuring a broader reach for your product.
Use the “Prepare for Distribution” Commandlet
MarketplaceKit includes commandlets that strip out unnecessary developer data (like autosaves and local config files). Running this preparation step helps you eliminate “bloat” from your final upload, reducing the download size for your customers.
Check for Hard-Coded Asset Paths
One of the most frequent causes of rejection is using absolute file paths in C++ or Blueprints. MarketplaceKit flags these instances, allowing you to switch to soft object references or relative paths to eliminate “Asset Not Found” crashes on the customer’s machine.
Optimize Texture and Mesh Settings
The kit can highlight assets that exceed standard performance budgets (e.g., textures that aren’t powers of two). Following these suggestions helps you eliminate performance issues for users with lower-end hardware, leading to better reviews and fewer refund requests.
Consolidate External Dependencies
If your project relies on other third-party plugins or libraries, MarketplaceKit will help you identify them. You must ensure these dependencies are clearly documented or included as per Fab’s guidelines to eliminate “Missing Plugin” errors when the customer tries to open your map.