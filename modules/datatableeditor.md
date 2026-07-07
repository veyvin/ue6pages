---
layout: default
title: DataTableEditor
---


<h1>DataTableEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/DataTableEditor/DataTableEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, DeveloperSettings, EditorFramework, Engine, InputCore, Json, PropertyEditor, Slate, SlateCore, ToolMenus, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

terface and logic for creating, viewing, and modifying Data Tables within the Unreal Editor. It acts as the backend for the spreadsheet-like grid view, allowing developers to manage large sets of structured data based on a specific FTableRowBase C++ struct or Blueprint Structure.

This module bridges the gap between external data (CSV/JSON) and the engine’s internal data structures, providing tools for searching, filtering, and reimporting data without requiring manual entry for every row.

Practical Usage Tips and Best Practices
1. Use the ‘RowType’ Meta Tag for Filtering

When you expose a FDataTableRowHandle or a UDataTable* in C++ or Blueprints, the editor will show every table in the project by default, which can be overwhelming.

Best Practice: Add the meta = (RowType = "YourStructName") tag to your variable. This tells the DataTableEditor to filter the dropdown to only show tables that match that specific struct, helping you eliminate selection errors in complex projects.
2. Establish a “Source of Truth” Workflow

Data Tables can be edited manually in the editor or imported from external .csv or .json files.

Tip: Decide early whether the “Source of Truth” is the external file or the Unreal Asset. If using external files, always use the Reimport function in the DataTableEditor. This ensures you eliminate data desynchronization where manual editor changes are accidentally overwritten by an old CSV.
3. Leverage the Search and Filter Bar

For tables with hundreds or thousands of rows (like item databases or localization strings), manual scrolling is inefficient.

Action: Use the search bar at the top of the DataTableEditor window. It supports searching by Row Name and cell content. Using these filters helps you eliminate the time wasted hunting for specific entries in massive datasets.
4. Validate Data via ‘OnPostDataImport’

The DataTableEditor doesn’t automatically know if your data values are “logical” (e.g., a “Health” value shouldn’t be negative).

Best Practice: In C++, override OnPostDataImport in your row struct or a custom factory. You can run logic to check for errors immediately after an import, allowing you to eliminate “broken” data before it ever reaches the gameplay systems.
5. Use Composite Data Tables for Team Collaboration

Standard Data Tables are binary files, meaning only one person can check them out of source control (like Perforce) at a time.

Tip: Use Composite Data Tables. These allow you to “parent” multiple smaller Data Tables into one master list. This helps eliminate workflow bottlenecks by allowing different team members to work on separate “sub-tables” simultaneously.
6. Utilize ‘FDataTableRowHandle’ for Designer UX

Instead of asking a designer to type a row name as a string, which is prone to typos:

Action: Use FDataTableRowHandle in your Blueprints or C++ classes. This provides a user-friendly UI with two dropdowns—one for the Table and one for the Row. This effectively eliminates “Invalid Row Name” runtime crashes caused by simple spelling mistakes.
7. Export to JSON for Bulk External Edits

While CSV is common for Excel, JSON is often better for programmatic changes or external tool integration.

Tip: Right-click a Data Table in the Content Browser and select Export as JSON. You can then use external scripts to perform bulk math operations or logic passes and reimport the result. This helps eliminate the tedium of manual entry for repetitive data updates.
8. Audit Rows with the ‘Property Matrix’

Sometimes you need to compare specific columns across many rows without opening each row’s individual details.

Action: Select multiple rows in the DataTableEditor and open the Property Matrix. This gives you a dedicated bulk-editing view, making it easy to spot outliers and eliminate inconsistent values across your entire data set.