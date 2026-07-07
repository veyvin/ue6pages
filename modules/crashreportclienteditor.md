---
layout: default
title: CrashReportClientEditor
---

<!-- ai-generation-failed -->

<h1>CrashReportClientEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/CrashReportClient/CrashReportClientEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>CrashReportClient</code></span></li><li><span class="label">依赖</span><span class="value">Concert, EditorAnalyticsSession, Messaging</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

provides the interface and integration between the Unreal Editor and the Crash Report Client (CRC). When the Unreal Editor crashes, this module ensures that the relevant metadata—such as the call stack, log files, and project information—is correctly captured and passed to the standalone Crash Report Client process.

It acts as the configuration bridge that allows developers to customize how the editor handles its own failures and where those reports are sent, whether to Epic Games or a private internal crash-tracking server.

Practical Usage Tips and Best Practices
1. Customizing the Receiver URL

By default, the editor sends reports to Epic. If you are a studio with your own crash-tracking server (like Sentry or BugSplat), you can redirect these reports.

Best Practice: Add a [CrashReportClient] section to your project’s DefaultEngine.ini. Setting the DataRouterUrl allows you to eliminate the need to manually collect logs from team members by centralizing them on your own dashboard.
2. Include Logs for Faster Debugging

By default, the editor may only send the minidump. To truly understand why a developer’s editor crashed, you need the log.

Tip: Enable bSendLogFile=true in your configuration. This ensures the ProjectName.log is attached to the report, helping you eliminate guesswork by seeing the exact sequence of events leading up to the crash.
3. Set the Company Name for Filtering

In large environments or co-development scenarios, it is helpful to know which branch or team the crash originated from.

Action: Use the CompanyName setting in the config. This string is included in the metadata and allows your server-side tools to filter crashes by department or project, eliminating confusion when multiple teams use the same crash-tracking endpoint.
4. Configure Unattended Bug Reports

For automated build machines or CI/CD agents that run the editor in a “headless” commandlet mode, there is no user to click “Send.”

Best Practice: Set bSendUnattendedBugReports=true. This allows the CrashReportClientEditor to automatically dispatch reports from your build farm, helping you eliminate silent failures in your automated pipelines.
5. Balance Privacy with Data Collection

The module allows you to toggle whether a user can be contacted or if they can provide comments.

Tip: Set bAllowToBeContacted=true if you want your internal tools team to be able to reach out to the developer who crashed. However, if working with sensitive third-party IP, you may want to eliminate user comments to prevent the accidental leakage of confidential information in the text field.
6. Use for Editor Utility Development

If you are building complex Editor Utility Widgets that are prone to crashing the editor during development:

Action: Keep the Crash Report Client enabled during your tools-dev phase. The “Callstack” provided by this module is often more readable than a standard debugger break, helping you eliminate logic errors in your custom editor extensions more quickly.
7. Opt-out via Editor Preferences

If you are working in a highly secure environment where data cannot leave the local network:

Tip: Navigate to Editor Preferences > Privacy > Bug Reports and set it to “Don’t Send.” This tells the CrashReportClientEditor to eliminate any outbound network requests, ensuring your project data remains local.
8. Verify Symbols for Report Accuracy

A crash report is useless without “symbols” (PDB files) to translate hex codes into function names.

Best Practice: Ensure your crash-tracking server has access to the symbols for your specific editor build. Without these, the module can only report raw addresses, which will eliminate your ability to effectively diagnose the root cause of the crash.