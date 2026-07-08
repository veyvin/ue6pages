---
layout: default
title: MessageLog
---

<!-- ai-generation-failed -->

<h1>MessageLog</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/MessageLog/MessageLog.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, InputCore, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

categorized, and actionable feedback to developers. Unlike the standard Output Log, which is a continuous stream of text, the Message Log is designed to highlight specific issues that require attention, such as compiler errors or map check warnings.

What it is and What it’s used for

Located in Engine/Source/Developer/MessageLog, this module provides the C++ API (FMessageLog) and the UI front-end for the Message Log window. It organizes messages into “Pages” and “Categories” (e.g., Map Check, Blueprint Log, Packaging Results).

Primary uses include:

Actionable Reporting: Creating messages with “tokens” that the user can click to jump directly to a specific Actor or Asset in the editor.
Validation Feedback: Displaying the results of automated tests, Data Validation, or Build/Cook processes in a readable format.
Persistent Warnings: Keeping track of critical errors that must be resolved before a project can be correctly packaged or played.
Compiler Output: Routing errors from the Blueprint or C++ compiler into a central, searchable interface.
Practical Usage Tips and Best Practices
1. Use Actionable Tokens for Fast Debugging

When logging an error about a specific object, use FUObjectToken. This creates a clickable link in the log. Providing a direct link to the offending asset is the best practice for the elimination of time wasted searching through the Content Browser for the source of a bug.

2. Categorize via Custom Log Listings

Avoid dumping all your custom tool messages into the “General” category. You can register your own category using FMessageLogModule::RegisterLogListing. This ensures the elimination of clutter, allowing team members to filter the log to see only the messages relevant to their specific department (e.g., “VFX_Validation”).

3. Implement Severity Levels Correctly

The Message Log supports Error, Warning, and Info. Use Error only for issues that prevent the game from running. Using the correct severity level allows for the elimination of “warning fatigue,” where critical issues are ignored because they are buried under hundreds of non-essential messages.

4. Leverage the “Notify” Feature

When a critical error occurs during a background process, call Notify() on your FMessageLog. This triggers a small pop-up notification in the bottom right of the editor. This ensures the elimination of missed errors that might otherwise go unnoticed if the Message Log window is closed.

5. Clean Up Old Pages

If your custom tool runs frequently, use NewPage() to clear old data or organize logs by timestamp/run. Keeping the log history organized leads to the elimination of confusion regarding whether an error is from the current run or a previous attempt.

6. Combine with FTokenizedMessage for Rich Text

Use FTokenizedMessage::Create to build complex messages that include text, links to documentation (FDocumentationToken), and assets. Rich text logging is a primary strategy for the elimination of vague error descriptions, providing developers with the context they need to fix the issue immediately.

7. Route standard UE_LOG to MessageLog

In your C++ systems, you can use FMessageLog to mirror important UE_LOG entries into the UI. This is particularly useful for tools that run in the editor, ensuring the elimination of the need for artists to keep the technical Output Log open at all times.

8. Strategic Elimination of Resolved Messages

When a user fixes an issue and re-runs a validation script, ensure your code refreshes the log page. The automatic elimination of fixed errors from the view provides immediate positive feedback and ensures the developer’s “to-do” list in the log is always accurate.