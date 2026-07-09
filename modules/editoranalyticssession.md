---
layout: default
title: EditorAnalyticsSession
---

<!-- ai-generation-failed -->

<h1>EditorAnalyticsSession</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/EditorAnalyticsSession/EditorAnalyticsSession.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

responsible for managing the lifecycle and health tracking of an Unreal Editor instance. It manages the “Heartbeat” system, which maintains a persistent file on disk to record session start times, durations, and exit statuses. Its primary purpose is to provide telemetry data that helps developers and Epic Games understand editor stability, identify the frequency of “abnormal” shutdowns (crashes or power losses), and track how long various tools are used during a development session.

Practical Usage Tips & Best Practices
1. Monitor the Heartbeat for Crash Detection

The module maintains a heartbeat file that is updated at a regular interval while the editor is active.

Best Practice: On startup, the module checks if the previous session’s heartbeat file was closed gracefully. If not, it flags the session as an “Abnormal Shutdown.” Use this logic in your studio’s internal tools to automate the elimination of manual crash reporting by detecting failed sessions automatically.
2. Configure Heartbeat Frequency

The frequency at which the session file is updated can impact performance or accuracy.

Tip: You can adjust the heartbeat interval in the BaseEditor.ini or via console variables. Setting a shorter interval provides more accurate “time-spent” data but increases disk I/O; find a balance to ensure the elimination of unnecessary performance overhead during long work sessions.
3. Integrate with Studio Telemetry (Horde)

For large teams, the data gathered by this module is invaluable for pipeline engineering.

Best Practice: Route the analytics produced by this module to a central dashboard like Horde or a custom ELK stack. This allows you to visualize which engine versions or plugins are causing the most instability, leading to the elimination of persistent workflow bottlenecks across the team.
4. Handle “Ghost” Sessions

Sometimes, if the editor process hangs and is manually terminated by a Task Manager, the session may remain “active” in the analytics logic.

Tip: Use the FEditorAnalyticsSession API to check for orphaned session files on editor launch. Cleaning these up ensures the elimination of skewed “Total Time Spent” metrics that don’t represent actual development work.
5. Track Specific Tool Usage

Beyond just “is the editor open,” this module can be extended to track the usage of specific sub-editors like Niagara or Sequencer.

Best Practice: Use the LogEditorSessionAttr functions to add custom attributes to the current session. Tracking which tools are most popular helps in the elimination of unused legacy plugins that may be bloating your editor build.
6. Deactivate During Automated Testing

When running automated commandlets or high-frequency unit tests, the constant creation and destruction of analytics sessions can create noise.

Tip: Use the -NoAnalytics command-line argument when running build scripts or automated tests. This results in the elimination of “test noise” in your production stability reports, keeping your data clean.
7. Respect User Privacy and GDPR

Because this module tracks session duration and machine IDs, it is subject to privacy regulations.

Best Practice: Always ensure that analytics collection is “Opt-In” for your team or external testers. Providing a clear way to disable the EditorAnalyticsSession via the Privacy settings ensures the elimination of legal risks or privacy concerns within your organization.
8. Verify Data with the Analytics Debugger

If you are unsure what data is being sent or recorded, Unreal provides internal tools to inspect the outgoing packets.

Tip: Use the Analytics Provider Debugger to see the session events in real-time. This is the fastest way to verify that your custom attributes are being recorded correctly, facilitating the elimination of malformed telemetry strings.