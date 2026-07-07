---
layout: default
title: CookMetadata
---

<!-- ai-generation-failed -->

<h1>CookMetadata</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/CookMetadata/CookMetadata.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rocess (the stage where assets are converted into platform-specific formats). Its primary role is to provide an interface and storage mechanism for “metadata” that is generated during the build but needs to be persisted or analyzed alongside the cooked assets.

This module is the bridge that allows the engine to track and store extra information about assets (such as versioning, dependency hashes, or custom build-time tags) that doesn’t necessarily belong inside the asset’s runtime binary but is critical for the Asset Manager, ZenServer, or incremental patching systems.

Practical Usage Tips and Best Practices
1. Implement ICookMetadata for Custom Audits

If you are building a custom build pipeline, you can use the ICookMetadata interface to attach custom data to the cook process.

Best Practice: Use this to store “Build-Time Hashes” of external dependencies (like a raw XML file used to generate a Data Asset). This helps eliminate the risk of using out-of-date external data by allowing the cook-checker to verify if the metadata still matches the source.
2. Use for Class-Agnostic Versioning

As discussed in Unreal’s asset management strategies, CookMetadata is ideal for tracking versions of assets that are not yet loaded into memory.

Tip: Instead of loading a 2GB mesh just to check its “Version” variable, store that version in the CookMetadata. The Asset Manager can read this metadata instantly to eliminate unnecessary memory spikes during the cook or patch-generation phase.
3. Integrate with ZenServer

In UE 5.4+, ZenServer uses metadata to handle the streaming of cooked data.

Action: Ensure your project is configured to use ZenServer as a cooked output store. CookMetadata helps ZenServer identify chunks and dependencies more efficiently, which helps eliminate slow staging and deployment times for large projects.
4. Automate Cook-Time Asset Exclusion

The CookMetadata can be used by a custom UAssetManager to decide which assets should actually be written to disk.

Best Practice: Use metadata to flag assets as “Development Only” or “Test Level.” By checking these flags during the ModifyCook phase, you can eliminate non-shipping assets from your final build automatically.
5. Monitor Metadata Size in Large Projects

While metadata is small compared to textures, in projects with millions of assets, the metadata itself can become a bottleneck for the filesystem.

Tip: If you see long “metadata gathering” times in your cook logs, audit what data you are storing. Use the stat commands in the cooker to eliminate redundant or overly verbose metadata strings that aren’t used by the runtime.
6. Leverage for Build-Time Validation

You can hook the CookMetadata module into the EditorValidatorSubsystem.

Action: During the cook, write validation results (like “Texture has no Mips”) into a metadata file. This allows your CI/CD pipeline to parse a single metadata report to eliminate the need to scan every individual asset after the cook is finished.
7. Use for Delta Patching Analysis

When using the BuildPatchTool, CookMetadata provides the “footprint” of the build.

Tip: Compare the metadata of two different cooks to identify which assets changed their “metadata signature” even if their binary size stayed the same. This helps eliminate confusion when trying to figure out why a patch is larger than expected.
8. Avoid Storing Runtime Secrets

Because metadata is often stored in plain-text or easily accessible formats within the Saved/Cooked folder:

Best Practice: Never store security keys, sensitive player data, or proprietary algorithms in CookMetadata. Keep this module strictly for build-pipeline info to eliminate potential security vulnerabilities in your distributed game.