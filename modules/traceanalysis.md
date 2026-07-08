---
layout: default
title: TraceAnalysis
---

<!-- ai-generation-failed -->

<h1>TraceAnalysis</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/TraceAnalysis/TraceAnalysis.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Asio, Cbor, Core, OpenSSL, Sockets, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

tem, responsible for consuming and interpreting .utrace files or live streams. While TraceLog handles the instrumentation (writing data), TraceAnalysis handles the processing (reading data). It translates raw, binary event streams into a structured format that can be used by Unreal Insights, the Trace Desktop app, or custom diagnostic tools.

By implementing custom analyzers within this module, you can eliminate the need for manual log mining by creating automated performance reports and data providers that feed into the Unreal Insights UI.

Practical Usage Tips and Best Practices
Define Targeted Analyzers
Create classes derived from IAnalyzer to process specific events. Use the OnAnalysisBegin function to register “routes” for only the events you care about. By filtering events at the entry point, you eliminate the processing overhead of scanning the entire trace stream for irrelevant data.
Implement Providers for Data Storage
Analyzers should be stateless; they should pass the data they extract to an IProvider. The provider stores the processed data in a way that is optimized for UI queries. This separation helps you eliminate data corruption and ensures that your analysis logic remains clean and modular.
Use ‘TraceAnalyzer.exe’ for Automation
Unreal provides a standalone command-line tool, TraceAnalyzer.exe, located in the Engine/Binaries/Win64 folder. You can use this tool to batch-process trace files on a build server to eliminate the need for developers to manually open the UI to check for performance regressions.
Handle Thread Safety via Locking
Trace data often arrives from multiple threads simultaneously. When writing data from an analyzer to a provider, ensure you use the appropriate scope locks. Proper synchronization helps you eliminate race conditions that can lead to crashes or “garbage data” in your performance graphs.
Version Your Trace Events
As your project evolves, the structure of your trace events may change. Implement version checking within your IAnalyzer to handle older .utrace files. This backward compatibility helps you eliminate “invalid file” errors when reviewing traces from previous milestones or branches.
Debug with ‘TraceAnalysisDebug.h’
If your custom analyzer isn’t picking up events, use the macros in TraceAnalysisDebug.h to enable verbose logging for the analysis process. Increasing the debug level helps you eliminate configuration errors by showing exactly which event routes are being hit in the stream.
Avoid ‘RootAllEvents’ for Performance
While the RootAllEvents function exists, it should be avoided unless you are building a generic statistics tool. Subscribing to every event in a heavy trace can significantly slow down the analysis. Instead, use specific event names to eliminate unnecessary CPU cycles during the parsing phase.
Manage Resources during Analysis Elimination
When an analysis session ends (the “elimination” of the FAnalysisContext), ensure your providers and analyzers release any temporary memory or file handles. Cleaning up these resources helps you eliminate memory leaks in the Unreal Insights process during long-running debugging sessions.