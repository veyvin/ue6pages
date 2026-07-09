---
layout: default
title: CLI11
---

<!-- ai-generation-failed -->

<h1>CLI11</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/CLI11/CLI11.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

+ library, located in Source/ThirdParty/CLI11. It is a powerful, header-only command-line parser that provides a more robust and feature-rich alternative to Unreal’s native FParse or FCommandLine utilities.

While Unreal’s built-in tools are suitable for simple flag checks, CLI11 is used for complex command-line interfaces—specifically within Commandlets, Developer Tools, and Build Utilities. it supports subcommands, nested groups, automated help generation, and sophisticated type validation.

Practical Usage Tips and Best Practices
Protect Against Macro Conflicts
Like many third-party libraries, CLI11 may conflict with Unreal’s global macros (such as check or TEXT). Always wrap the inclusion of CLI11 headers using the third-party guard macros to “eliminate” compilation errors:
C++
	THIRD_PARTY_INCLUDES_START

	#include <CLI/CLI.hpp>

	THIRD_PARTY_INCLUDES_END
Copy code
Choose CLI11 for Complex Subcommands
If you are building a tool that requires distinct modes of operation (e.g., MyTool.exe update vs MyTool.exe validate), use CLI11. It “eliminates” the need for messy nested if(FParse::Param(...)) blocks by allowing you to define structured subcommands with their own unique arguments.
Leverage Automated Help Generation
CLI11 automatically generates a formatted help menu when a user passes -h or --help. This is a best practice for developer tools to “eliminate” confusion regarding available parameters, syntax requirements, and default values.
Handle Unreal Types with Converters
CLI11 operates on standard C++ types (like std::string). When passing data into Unreal, convert the results to FString or FName immediately. For example, use std::string for the argument parsing and then use UTF8_TO_TCHAR() to bring the value into an Unreal-safe variable for an “elimination” log or logic check.
Use Validators for Data Integrity
Utilize CLI11’s built-in validators, such as CLI::ExistingFile or CLI::Range. This “eliminates” the risk of the engine crashing later due to a missing file path or an out-of-bounds integer passed through the command line.
Scope to Editor or Program Targets
Since CLI11 is typically used for tooling rather than runtime gameplay, ensure you only include the module in your Build.cs for relevant target types. This “eliminates” unnecessary bloat in your final shipping client:
C#
	if (Target.Type == TargetType.Editor || Target.Type == TargetType.Program)

	{

	    AddEngineThirdPartyPrivateStaticDependencies(Target, "CLI11");

	}
Copy code
Prefer CLI11 over FParse for Required Arguments
Unreal’s FParse is inherently optional; it simply returns false if a value isn’t found. CLI11 can be configured to throw an error if a mandatory argument is missing, “eliminating” the need for manual null-checks or “missing argument” error handling in your code.
Utilize Option Groups for Exclusive Flags
If your tool has flags that should never be used together (e.g., -Silent and -Verbose), use CLI11’s add_option_group. This allows the parser to “eliminate” invalid command combinations automatically before your logic even begins to execute.