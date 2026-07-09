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

process of preparing, validating, and publishing content for Fab (formerly the Unreal Engine Marketplace). Its primary function is to act as a “pre-flight” checklist, ensuring that assets, plugins, and projects adhere to the strict technical standards required for public distribution. By automating the verification of folder structures, naming conventions, and file dependencies, this module helps developers identify critical issues before they attempt to upload their work to the publisher portal.

Practical Usage Tips & Best Practices
1. Run the Validation Tool Early

The MarketplaceKit includes a validation suite that scans your project for common rejection reasons, such as hardcoded absolute paths or missing icons.

Best Practice: Do not wait until the project is finished to run the validator. Frequent use during development allows for the elimination of massive refactoring tasks that occur when a naming convention error is discovered across hundreds of assets at the end of a cycle.
2. Enforce Strict Folder Hierarchies

Fab requires a specific root-level structure (typically Content/[ProductMovingPart]) to prevent asset collisions when users import multiple packs.

Tip: Use the MarketplaceKit to verify that all your assets reside within a single, uniquely named top-level folder. This organization results in the elimination of “file overwrite” warnings for your customers and improves your product’s professional rating.
3. Proactive “Elimination” of Redirectors

Internal “Redirectors” (invisible files left behind when moving assets) are a common cause of broken links in distributed packages.

Best Practice: Right-click your main content folder and select Fixup Redirectors in Folder before running the MarketplaceKit validation. This ensures the elimination of “Missing Asset” errors that would otherwise occur when a customer tries to load your content in a clean project.
4. Audit External Dependencies

The module checks if your assets rely on plugins or content from other Marketplace/Fab products that the user might not own.

Tip: Use the “Reference Viewer” in conjunction with MarketplaceKit to ensure all dependencies are either engine-default or contained within your own package. This facilitates the elimination of “Plugin Missing” startup crashes for the end-user.
5. Verify Plugin Descriptor Files (.uplugin)

For plugin developers, the module validates the Modules and Plugins sections of your descriptor file.

Best Practice: Ensure your “WhitelistPlatforms” are correctly defined. Properly configured descriptors lead to the elimination of build failures when the Fab backend attempts to compile your plugin for platforms you didn’t intend to support.
6. Optimize Asset Sizes and Texture Groups

Large, unoptimized files can lead to slow downloads and poor performance for customers.

Tip: Use the validation logs to identify textures that aren’t using the correct TextureGroup (e.g., World vs. UI). Setting these correctly leads to the elimination of unnecessary memory consumption, as the engine can now manage Mip-maps and streaming properly.
7. Standardize Naming Conventions

Fab reviewers often look for standardized prefixes (e.g., T_ for Textures, M_ for Materials).

Best Practice: Use the Global Asset Picker within the kit to spot-check naming inconsistencies. Maintaining a clean naming convention ensures the elimination of technical debt and makes your product much easier for customers to navigate and search.
8. Use the “Zip Project” Function for Submissions

The module provides a specialized routine to package the project for submission, stripping out temporary files like the DerivedDataCache and Intermediate folders.

Tip: Always use this built-in export tool rather than manually zipping the project folder. This ensures the elimination of “bloat” files, significantly reducing the upload size and preventing the accidental inclusion of sensitive local configuration data.