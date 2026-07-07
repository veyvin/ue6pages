---
layout: default
title: PlainPropsTests
---

<!-- ai-generation-failed -->

<h1>PlainPropsTests</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/PlainPropsTests/PlainPropsTests.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>TestModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

idate the functionality of the PlainProps system, which is Unreal Engine’s high-performance, compact reflection and serialization framework.

Description and Purpose

PlainProps is a modernized reflection system (often associated with the Zen asset delivery and IoStore systems) designed to be faster and more memory-efficient than the traditional UProperty system for specific data-heavy tasks. The PlainPropsTests module contains a collection of C++ tests—built using the Catch2 framework—that verify the integrity of data serialization, schema generation, and delta compression. Its primary purpose is to ensure that when the engine translates complex C++ structures into “plain” bitstreams for network transfer or disk storage, no data is corrupted. This helps developers eliminate regressions in the engine’s core data-handling pipeline.

Practical Usage Tips and Best Practices
Run via UnrealBuildTool for Speed
Since this is a Low-Level Test (LLT) module, you can execute it without launching the full Unreal Editor. Use the command UnrealBuildTool.exe PlainPropsTests Win64 Development to build the test executable. This allows you to eliminate the overhead of the editor UI when you only need to verify serialization logic.
Filter Tests by Tag
The module uses Catch2 tags to group tests (e.g., [bitstream], [schema]). When running the executable, use the tag syntax (e.g., PlainPropsTests.exe [bitstream]) to run only specific tests. This is a best practice to eliminate wasted time running the entire suite when you are only debugging a specific part of the system.
Utilize for Custom Reflection Debugging
If you are implementing custom data types that must interface with the Zen/IoStore pipeline, use the source code in PlainPropsTests as a reference. Seeing how the engine tests its own “Plain Properties” helps you eliminate architectural errors in your own data structures.
Check for Schema Compatibility
A major focus of these tests is “Schema Evolution”—ensuring that newer versions of a data structure can still read older versions. If you are experiencing crashes when loading old assets, run these tests to see if a recent engine change caused an elimination of backward compatibility in the serialization layer.
Monitor Bitstream Efficiency
The tests often check for bit-perfect serialization. When working with high-frequency network data, you can use these tests to understand how PlainProps packs data. This knowledge helps you eliminate bloat by choosing data types that the system can compress most effectively.
Integrate into CI/CD Pipelines
Because these tests are “Explicit Tests” (requiring their own .Target.cs file), they are ideal for automated build machines. Running them on every commit helps eliminate “silent” serialization bugs that might not crash the editor but could corrupt saved game data or network packets.
Use the –debug Flag
When running the PlainPropsTests.exe, pass the --debug argument. This will print low-level messages regarding test start times and completion status. If a test hangs, this is the best way to eliminate ambiguity and identify exactly which property or struct caused the infinite loop or hang.
Validate Delta Compression
PlainProps is often used to send only the changes between two states. The tests in this module verify that the “delta” (the difference) is calculated and applied correctly. Use these tests to ensure that the elimination of redundant data transfer in your networking code doesn’t result in out-of-sync states between the client and server.