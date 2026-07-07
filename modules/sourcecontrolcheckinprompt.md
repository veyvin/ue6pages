---
layout: default
title: SourceControlCheckInPrompt
---

<!-- ai-generation-failed -->

<h1>SourceControlCheckInPrompt</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/SourceControlCheckInPrompt/SourceControlCheckInPrompt.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, Slate, SlateCore, SourceControl, SourceControlWindows, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

t provides the UI framework and logic for the “Submit Files” or “Check-In” dialogs within Unreal Engine.

Description and Purpose

This module acts as the user interface bridge between the Unreal Editor and the underlying source control provider (such as Perforce, Git, or SVN). It is primarily responsible for spawning the SSourceControlCheckInPrompt Slate widget, which allows users to enter changelist descriptions, view a list of modified files, and select which assets to include in a commit. Its primary purpose is to centralize the submission workflow, ensuring that metadata (like JIRA tags or task IDs) can be captured before data is pushed to the server. By providing a unified interface, it helps teams eliminate the risk of accidental “empty” submissions or checking in local-only temporary files.

Practical Usage Tips and Best Practices
Enforce Description Requirements
You can customize the prompt to prevent the “Submit” button from being clickable until a description is entered. This is a best practice to eliminate “empty” changelists in your version control history, which makes tracking down bugs significantly harder for the team.
Integrate with Content Validation
The check-in prompt works in tandem with the Data Validation system. Before the dialog allows a submission, it can trigger IsDataValid checks on the selected assets. This helps you eliminate the possibility of checking in broken blueprints or assets with missing references that would break the build for others.
Utilize the “Submit Tool” (UE 5.5+)
In newer versions of the engine, this module supports the enhanced Submit Tool. Use this to automate pre-submission tasks like “Fixup Redirectors” or “Save All.” Leveraging these automated steps helps you eliminate manual cleanup tasks that developers often forget before a check-in.
Format Descriptions with Regex
For large projects, you can use the prompt’s configuration to enforce a specific format (e.g., requiring a #JIRA-123 prefix). This allows external tools to parse your source control logs automatically, helping to eliminate manual tracking of which features were added in which changelist.
Use the “Keep Files Checked Out” Option
The prompt includes a checkbox to keep files locked after submission. Advise your team to use this only when necessary for multi-part tasks. This practice helps you eliminate “stale locks” where an asset is left checked out indefinitely, preventing other team members from working on it.
Filter Out Unwanted Files
The check-in prompt allows users to uncheck specific files in a batch. Encourage users to review this list to eliminate “dirty” files—like local test levels or temporary configuration tweaks—from being accidentally included in a production-ready submission.
Review Diff Tool Integration
From the check-in prompt, users can right-click an asset to “Diff against Depots.” Encourage artists and designers to use this to see exactly what changed in a Blueprint or DataTable. This helps eliminate “accidental saves” where a file was marked as modified even though no intentional changes were made.
Automate via Editor Utility Widgets
If you have a custom pipeline tool, you can programmatically call the SourceControlCheckInPrompt module to trigger a submission. This allows you to create “One-Click Publish” buttons for specific workflows, which helps you eliminate navigation friction within the Content Browser.