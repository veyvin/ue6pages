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

rough thousands of files by creating logical, project-specific, or user-specific asset groupings.

Practical Usage Tips and Best Practices
Understand the Three Share Types
The Collection Manager differentiates between Local, Private, and Shared collections. Use “Shared” for assets that need to be seen by the whole team (e.g., an “Elimination VFX” group) and “Local” for personal organization that you want to “eliminate” from the source control submission.
Utilize for Bulk Property Matrix Edits
Instead of selecting assets individually across multiple folders, add them all to a temporary Collection. You can then right-click the collection and open the Property Matrix to perform mass edits. This “eliminates” the risk of missing specific assets during a large-scale refactor.
Automate via Scripting Subsystem
In UE 5.6+, use the Collection Manager Scripting Subsystem in Blueprints or Python to automate organization. You can script a tool that automatically “eliminates” assets from a “Work-in-Progress” collection and adds them to a “Review-Ready” collection once they pass a validation check.
Avoid Hard References
Collections are purely metadata; they do not create hard references between assets. This is a best practice for “eliminating” accidental memory bloat, as adding an asset to a collection won’t cause that asset to be loaded into memory whenever the collection is queried.
Use Dynamic Collections for Smart Filtering
Unlike static collections, Dynamic Collections use search queries (e.g., Name:Weapon AND Triangles > 10000). This is a powerful way to “eliminate” manual sorting, as any new asset matching those criteria will automatically appear in the collection.
Leverage for Build Validation
Create a “Required for Demo” collection. You can then use the ICollectionManager in C++ to verify that every asset in that collection has been correctly assigned to a specific Primary Asset Label. This helps “eliminate” missing-asset errors in your final packaged builds.
Clean Up Empty Collections Regularly
Old collections can clutter the Content Browser. It is a best practice to “eliminate” empty or obsolete collections during your project’s milestone clean-up phases to keep the “Collections” view manageable for the entire team.
Handle Redirections Correctly
If you move or rename an asset, the Collection Manager handles the update automatically. However, if you are working with source control, ensure you “Fix Up Redirectors” in your folders to “eliminate” potential pathing issues within your shared collections.