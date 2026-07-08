---
layout: default
title: AnalyticsCSV
---

<!-- ai-generation-failed -->

<h1>AnalyticsCSV</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Analytics/AnalyticsCSV/AnalyticsCSV.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Engine that records telemetry data locally to the user’s machine in Comma-Separated Values (CSV) format. Unlike cloud-based providers that require an active internet connection and a remote dashboard, this module allows for offline data collection and local debugging of event-driven logic.

Description

The module implements the IAnalyticsProvider interface to convert RecordEvent calls into rows within a .csv file. It is primarily used during development to verify that analytics events are firing correctly, to profile player behavior in local playtests, or to generate data for manual analysis in spreadsheet software like Excel or Google Sheets.

Practical Usage Tips and Best Practices
1. Configure via DefaultEngine.ini

To activate the CSV provider, you must specify it as your active analytics module in your project’s configuration. This is usually done within a specific target platform or development-only config:

ini
	[Analytics]

	ProviderModuleName=AnalyticsCSV
Copy code
2. Locate Output in the Saved Folder

By default, the module writes its output to your project’s Saved/Analytics/ directory. Each session generates a unique file. When debugging, you can keep this folder open to verify that files are being created and populated in real-time as you play in the editor (PIE).

3. Use for Offline Playtest Analysis

If you are conducting playtests in an environment with restricted internet access, the AnalyticsCSV module is the best way to capture player metrics. You can later collect these files and merge them into a master spreadsheet to analyze player pathing, item usage, or event frequency.

4. Differentiate from FileLogging

While the FileLogging provider outputs events in a JSON-like format for readability, AnalyticsCSV is superior for data processing. CSV files are significantly easier to import into data visualization tools (like Power BI or Tableau) to create charts and graphs of your game’s telemetry.

5. Verify Event Recording on Elimination

Use this module to ensure that game-critical events are recorded properly. For example, you can trigger an event upon a player’s elimination and immediately open the CSV file to confirm that all associated parameters (such as the location of the elimination, the weapon used, and the session time) were captured correctly.

6. Avoid Shipping with Local Analytics

Recording analytics to a local disk can lead to ever-growing file sizes that bloat the user’s storage over time. It is a best practice to use the AnalyticsCSV provider only in Development or Test builds. Ensure your DefaultEngine.ini resets the provider to a cloud service (or None) for Shipping builds.

7. Batching and Performance

Even though writing to disk is local, frequent I/O operations can impact performance on slower drives. If you are recording high-frequency data (multiple events per second), consider wrapping your calls in logic that checks the current frame rate, or use the AnalyticsMulticast module to send data to CSV only during specific testing phases to eliminate performance hitches.

8. Sanitize Parameter Names

CSV headers are generated based on the attribute names you pass in C++ or Blueprints. To maintain a clean spreadsheet, avoid using spaces or special characters in your attribute keys (e.g., use Weapon_ID instead of Weapon ID). This ensures the resulting CSV remains compatible with automated data-parsing scripts.