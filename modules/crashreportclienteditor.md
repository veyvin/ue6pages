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

ocess) and presenting the user with the option to provide comments, logs, and screenshots before the report is sent to Epic Games or a custom internal server.

Practical Usage Tips and Best Practices
Configure Privacy via Editor Preferences
You can control the behavior of this module by navigating to Edit > Editor Preferences > Privacy. Here, you can “eliminate” automatic report sending by setting it to “Don’t Send,” which is often a best practice for studios working on highly confidential projects.
Customizing the Crash Reporter for Your Team
For large studios, you can customize the appearance of the crash reporter (such as your company logo and server URL) in the DefaultEngine.ini under the [CrashReportClient] section. This helps “eliminate” confusion for developers, ensuring they know the report is going to their internal tools team rather than Epic Games.
Use -Unattended for Automated Testing
When running automated tests or build farm processes, use the -Unattended command-line argument. This module will then “eliminate” all UI prompts and either discard the report or send it automatically based on your configuration, preventing the build machine from hanging on a pop-up.
Include Symbols for Meaningful Reports
A crash report is only useful if it can be symbolicated. Ensure that your build pipeline stores the .pdb (Windows) or .dsym (macOS) files. This allows the CrashReportClientEditor to associate the “elimination” point with a specific line of C++ code in your project.
Leverage GPU Crash Debugging
If you are experiencing frequent “Device Removed” errors, enable the -gpucrashdebugging flag. This module will then gather additional NVIDIA Aftermath or AMD data, which helps “eliminate” the guesswork when diagnosing driver-level or shader-related crashes.
Monitor the Saved/Logs Directory
Before the report is even sent, the data is staged in the Saved/Crashes folder of your project. If you are unable to send a report due to network restrictions, you can manually inspect these files to “eliminate” the bug using the stored Uminidump and log files.
Utilize the User Comment Field
Encourage your team to always fill out the “What were you doing?” field in the UI provided by this module. Detailed steps (e.g., “Right-clicked a Blueprint during an elimination event”) “eliminate” the time spent by engineers trying to reproduce the crash from just a callstack.
Check bAgreeToCrashUpload in Engine.ini
For head-mounted display (HMD) or VR development where the UI might not be visible, ensure bAgreeToCrashUpload=true is set in the Engine.ini. This “eliminates” the need for the developer to take off the headset to manually click “Send” after an editor crash.