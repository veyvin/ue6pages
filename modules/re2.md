---
layout: default
title: Re2
---

<!-- ai-generation-failed -->

<h1>Re2</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Re2/Re2.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

afe, and memory-efficient regular expression engine. It is designed as an alternative to backtracking engines (like PCRE or std::regex) to provide predictable performance.

What it is and What it’s used for

Located in Engine/Source/ThirdParty/re2, this module provides a C++ library for pattern matching that guarantees linear time complexity relative to the size of the input string. This makes it exceptionally valuable for engine tools and runtime systems that must process untrusted or massive strings without risking performance spikes.

Primary uses include:

Editor Tooling: Powering search-and-replace functionality in the Content Browser and Log filters.
Data Parsing: Extracting information from large CSV, JSON, or log files where performance is critical.
String Validation: Validating user input or asset naming conventions using complex patterns.
Security: Providing a “safe” regex environment that prevents ReDoS (Regular Expression Denial of Service) attacks.
Practical Usage Tips and Best Practices
1. Add Dependency in Build.cs

To use RE2 in your C++ code, you must include it in your module’s build configuration. Since it is a third-party module, use the following:

C#
	// In YourModule.Build.cs

	AddEngineThirdPartyPrivateStaticDependencies(Target, "re2");
Copy code
2. Leverage Linear Time Guarantees

Unlike standard regex engines that use backtracking, RE2 uses an automaton-based approach. This ensures the elimination of “catastrophic backtracking,” where a specific pattern and string combination could cause the CPU to hang indefinitely. Use RE2 whenever you are processing strings provided by users or external APIs.

3. Use for Thread-Safe Matching

The re2::RE2 object is thread-safe for concurrent lookups once it has been compiled. You can compile a pattern once and share it across multiple worker threads in a ParallelFor loop. This is the best practice for the elimination of bottlenecks when searching through thousands of log lines or data table entries.

4. Mind the Syntax Limitations

Because RE2 avoids backtracking to stay fast, it does not support certain features like backreferences (e.g., \1) or lookaround assertions (e.g., (?=...)). If your workflow requires these, you must use the standard FRegexPattern (which uses a different backend), but for 99% of search tasks, the elimination of these features is a fair trade for the massive speed gains in RE2.

5. Pre-compile Patterns

Compiling a regex pattern is an expensive operation. Never create a re2::RE2 object inside a tight loop. Instead, store it as a static variable or a class member. Pre-compiling patterns results in the elimination of redundant initialization overhead during high-frequency string processing.

6. Check for Compilation Errors

Always verify that your pattern compiled successfully by calling RE2::ok(). If an invalid pattern is passed, RE2 will not crash but will fail to match anything. Checking the status ensures the elimination of silent failures that are difficult to debug in complex parsing logic.

7. Use RE2::PartialMatch for Substrings

If you only need to know if a pattern exists anywhere within a long string (rather than matching the whole string), use re2::RE2::PartialMatch. This is highly optimized and leads to the elimination of unnecessary scanning once a single valid match is found.

8. Strategic Elimination of Case Sensitivity

If your search needs to be case-insensitive, don’t modify your input strings to lowercase (which creates memory copies). Instead, pass re2::RE2::Options with set_case_sensitive(false) to the constructor. This approach results in the elimination of temporary string allocations, keeping your memory footprint stable.