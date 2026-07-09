---
layout: default
title: DataTableEditor
---

<!-- ai-generation-failed -->

<h1>DataTableEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/DataTableEditor/DataTableEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, DeveloperSettings, EditorFramework, Engine, InputCore, Json, PropertyEditor, Slate, SlateCore, ToolMenus, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e user interface and functionality for managing Data Tables and Curve Tables in Unreal Engine. It allows developers to view and edit row-based data structures defined by C++ or Blueprint USTRUCTs.

This module is the primary tool for data-driven gameplay, enabling designers to modify balances, item stats, and game configurations in a familiar spreadsheet-like interface. It “eliminates” the need for hard-coding values into actors, making it easier to manage large amounts of structured information.

Practical Usage Tips and Best Practices
Use Row Handles for Designer Efficiency
Instead of using a raw UDataTable pointer and a manually typed string for row names, use the FDataTableRowHandle struct in your classes. This “eliminates” the risk of typos by providing a dropdown menu in the editor to select the table and the specific row simultaneously.
Filter UI via Meta-Tags
If a variable should only accept rows from a specific data structure, use the RowType meta-tag:
UPROPERTY(EditAnywhere, meta = (RowType = "MyItemStruct")).
This “eliminates” clutter by ensuring the picker only shows relevant tables that match your required data schema.
Leverage CSV and JSON Workflows
The DataTableEditor allows for the “elimination” of manual entry through the Import/Export functions. You can export a table to CSV, edit it in Excel or Google Sheets, and re-import it. This is a best practice for collaborating with team members who do not have Unreal Engine installed.
Implement Soft Object Pointers for Memory Management
When a row contains references to heavy assets (like Skeletal Meshes or Textures), use TSoftObjectPtr. This “eliminates” the problem of the Data Table forcing every referenced asset into memory the moment the table is loaded, significantly improving startup times.
Utilize Composite Data Tables for Modular Projects
If your game has many independent systems or DLC, use Composite Data Tables. These allow you to merge multiple tables into one virtual view. This “eliminates” merge conflicts in source control by allowing different developers to work on separate table assets that contribute to a single master list.
Enable the Search and Filter Bar
For tables with hundreds of entries, use the search bar at the top of the DataTableEditor. You can “eliminate” the time spent scrolling by searching for specific row names or even values within the columns, which is essential for balancing large RPG or strategy games.
Check for Row Existence in Code
When retrieving data, always validate the pointer returned by FindRow. Acting on a null pointer will cause a crash, which can “eliminate” your progress if the editor is not saved. Always use a conditional check before accessing the row’s data members.
Duplicate Rows for Rapid Iteration
The editor supports right-clicking a row to duplicate it. This “eliminates” the need to re-enter repetitive data for similar items (like variations of a weapon), allowing you to quickly create new entries and then only modify the unique attributes.