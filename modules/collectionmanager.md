---
layout: default
title: CollectionManager
---

<!-- ai-generation-failed -->

<h1>CollectionManager</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/CollectionManager/CollectionManager.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core, CoreUObject, DeveloperSettings, DirectoryWatcher, SourceControl</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

tions within the Content Browser. Collections are virtual folders that allow you to group assets together without moving them from their physical locations on disk.

While the AssetTags subsystem handles simple tagging, the CollectionManager module (and its associated ICollectionManager interface) provides deep integration with source control, allowing for “Shared,” “Private,” and “Local” collections. This is the primary API used by pipeline engineers to automate asset organization and team workflows.

Practical Usage Tips and Best Practices
1. Distinguish Between Collection Share Types

When creating collections via C++ or the CollectionManager Scripting Subsystem (introduced in UE 5.6), you must explicitly define the share type.

Best Practice: Use Shared for project-wide organization (like “Gold Assets”), Private for personal tasks tracked in source control, and Local for temporary working groups. Correct usage helps eliminate clutter in the Shared folder for other team members.
2. Automate Asset Audits

You can use the ICollectionManager to programmatically find assets that don’t meet your project’s technical standards.

Tip: Write an Editor Utility script that finds all textures without Mips or meshes with too many material slots and adds them to a “Fix Me” collection. This helps eliminate technical debt by providing artists with a clear “to-do” list.
3. Use Static vs. Dynamic Collections
Static Collections: Contain manually added references to specific assets.
Dynamic Collections (Smart Filters): Use search queries (e.g., Type=StaticMesh AND Triangles > 10000).
Best Practice: Use Dynamic Collections for broad categories and Static Collections for curated sets. This will eliminate the need to manually update lists as new assets are imported.
4. Clean Up “Orphaned” Collections

Collections are stored as small files. Over time, unused collections can accumulate and slow down Content Browser searches.

Action: Periodically use DestroyCollection for temporary or experiment-based collections once they are no longer needed. This helps eliminate “search noise” and keeps the collection tree manageable for the whole team.
5. Integrate with Content Validation

Unreal’s Data Validation system can be hooked into the Collection Manager.

Tip: Configure your build pipeline to automatically run validation only on assets found within specific “Release” collections. This allows you to eliminate unnecessary validation time on “Work-in-Progress” assets.
6. Leverage Collection Containers for Plugins

In UE 5.6+, Collection Containers allow collections to be associated with specific plugins or modular projects rather than the base game.

Action: If you are developing a modular feature, store its collections within its own container. This ensures that when the plugin is removed, its associated collections are also removed, eliminating broken or empty references in the main project.
7. Avoid Hard-Coding Collection Names

When accessing collections via the API, do not use hard-coded strings throughout your codebase.

Best Practice: Store collection names in a Developer Settings class or a Data Asset. This allows you to rename collections in the editor and update the reference in one place, eliminating “Collection Not Found” errors in your tools.
8. Utilize the ‘Redirectors’ Command

Moving assets that are part of a collection can sometimes leave behind “Redirectors” that clutter the collection’s data.

Action: After a major asset migration, right-click your Content folder and select “Fix Up Redirectors in Folder.” This ensures the Collection Manager points directly to the new asset location, eliminating potential loading delays or broken references.