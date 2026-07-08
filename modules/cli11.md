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

CLI11 library, a header-only C++11 library specifically designed for parsing command-line arguments. While Unreal Engine has its own FCommandLine and FParse utilities, they are primarily intended for simple key-value pairs.

The cli11 module provides a much more robust, declarative, and feature-rich framework for building standalone command-line tools, commandlets, and developer utilities. It supports subcommands, typed options (int, float, string), flag grouping, and automated help generation, allowing developers to “eliminate” the tedious manual string manipulation typically required for complex tools.

Practical Usage Tips and Best Practices
Restrict to Developer Tools Because cli11 is a ThirdParty module used for parsing input, it is best suited for Programs (standalone apps) or Editor-only modules. To “eliminate” unnecessary binary bloat, do not include it in your runtime game modules unless you are building a specialized server-side management tool.
Bridge Unreal Strings to CLI11 Unreal uses FString (TCHAR), while CLI11 expects std::string. Use the TCHAR_TO_UTF8 macro to convert Unreal’s command line into a format the parser can handle:
C#
	// In MyTool.Build.cs

	if (Target.Type == TargetType.Program || Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    AddEngineThirdPartyPrivateStaticDependencies(Target, "cli11");

	}

	```

	 

	#### 2. Scope the CLI Namespace

	The library uses the `CLI` namespace. To "eliminate" potential collisions with Unreal’s own classes (like `FCLI`), do not use `using namespace CLI;`. Instead, use explicit namespacing or a scoped alias inside your function:

	```cpp

	#include "CLI/CLI.hpp"

	 

	void MyCommandlet(const FString& Params)

	{

	    CLI::App App{"My Unreal Tool"};

	    // Logic here...

	}

	```

	 

	#### 3. Bridge FCommandLine to CLI11

	Unreal stores the command line as a single `FString` or a `TArray<FString>`. `CLI11` expects standard C-style `argc`/`argv` or a vector of strings. Use `FCommandLine::Get()` to feed the parser:

	```cpp

	// Convert Unreal string to a format CLI11 understands

	FString CmdLine = FCommandLine::Get();

	TArray<FString> Tokens;

	FCommandLine::Parse(reinterpret_cast<const TCHAR*>(*CmdLine), Tokens, false);

	 

	std::vector<std::string> StdTokens;

	for (const FString& Token : Tokens) 

	{ 

	    StdTokens.push_back(TCHAR_TO_UTF8(*Token)); 

	}

	 

	App.parse(StdTokens);

	```

	 

	#### 4. Leverage Subcommands for Complex Tools

	If you are building a tool with multiple modes (e.g., `Update`, `Package`, `Verify`), use `App.add_subcommand()`. This allows you to "eliminate" massive `if/else` blocks and creates a clean, git-like interface where each mode has its own help and arguments.

	 

	#### 5. Use Native Unreal Types via String Conversion

	`CLI11` works best with standard types (`int`, `std::string`). When receiving paths, parse them as `std::string` and then convert them back to `FString` using `UTF8_TO_TCHAR` for use within Unreal's file systems. This ensures you maintain compatibility with Unreal's Unicode requirements.

	 

	#### 6. Custom Validation with CLI11 Validators

	Use the `.check()` modifier to "eliminate" invalid inputs before your logic even runs. For example, if your tool requires a path to a specific `.uproject` file, use `CLI::ExistingFile`:

	```cpp

	std::string ProjectPath;

	App.add_option("-p,--project", ProjectPath, "Path to .uproject")

	   ->required()

	   ->check(CLI::ExistingFile);

	```

	 

	#### 7. Wrap in Exception Handling

	`CLI11` throws exceptions by design (e.g., `CLI::ParseError`). Since Unreal often compiles with exceptions disabled, ensure you use the `CLI11_PARSE` macro or wrap your `App.parse()` in a way that captures the error and outputs it to `UE_LOG` or `FMessageDialog` rather than crashing.

	 

	#### 8. Generate Automated Help for Build Farms

	One of the best features of `cli11` is the automated `--help` flag. Use this to "eliminate" documentation desync. When your CI/CD pipeline or build farm engineers need to know the parameters for your custom tool, they can simply run `MyTool.exe --help` to get an up-to-date manifest of all available options.
Copy code
Leverage Subcommands for Complex Utilities If you are building a tool that performs multiple different actions (e.g., Export, Import, Validate), use the add_subcommand() feature. This allows you to “eliminate” massive if/else blocks by creating scoped parsers for each specific task.
Use Validators for Input Safety CLI11 provides built-in validators like CLI::ExistingFile or CLI::Range. Use these to “eliminate” invalid inputs before your logic even runs, ensuring that your tool doesn’t crash because a user provided a path to a non-existent folder.
Automated Help Generation Always provide a description for your options using the second parameter of add_option(). This allows CLI11 to automatically generate a professional --help output, which “eliminates” the need to maintain separate documentation for your tool’s parameters.
Handle Exceptions for Non-Exception Builds Unreal Engine often disables C++ exceptions. Since CLI11 uses exceptions for error handling, you should use the CLI11_PARSE(app, argc, argv) macro or a try-catch block (if enabled in your Build.cs) to “eliminate” crashes during parsing errors, such as missing required arguments.
Integrate with Build.cs Correctly To use this module, you must add it to your Build.cs file. Use AddEngineThirdPartyPrivateStaticDependencies to ensure the header paths are correctly resolved by the Unreal Build Tool (UBT):
C#
	// In MyTool.Build.cs

	if (Target.Type == TargetType.Program || Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    AddEngineThirdPartyPrivateStaticDependencies(Target, "cli11");

	}

	```

	 

	#### 2. Scope the CLI Namespace

	The library uses the `CLI` namespace. To "eliminate" potential collisions with Unreal’s own classes (like `FCLI`), do not use `using namespace CLI;`. Instead, use explicit namespacing or a scoped alias inside your function:

	```cpp

	#include "CLI/CLI.hpp"

	 

	void MyCommandlet(const FString& Params)

	{

	    CLI::App App{"My Unreal Tool"};

	    // Logic here...

	}

	```

	 

	#### 3. Bridge FCommandLine to CLI11

	Unreal stores the command line as a single `FString` or a `TArray<FString>`. `CLI11` expects standard C-style `argc`/`argv` or a vector of strings. Use `FCommandLine::Get()` to feed the parser:

	```cpp

	// Convert Unreal string to a format CLI11 understands

	FString CmdLine = FCommandLine::Get();

	TArray<FString> Tokens;

	FCommandLine::Parse(reinterpret_cast<const TCHAR*>(*CmdLine), Tokens, false);

	 

	std::vector<std::string> StdTokens;

	for (const FString& Token : Tokens) 

	{ 

	    StdTokens.push_back(TCHAR_TO_UTF8(*Token)); 

	}

	 

	App.parse(StdTokens);

	```

	 

	#### 4. Leverage Subcommands for Complex Tools

	If you are building a tool with multiple modes (e.g., `Update`, `Package`, `Verify`), use `App.add_subcommand()`. This allows you to "eliminate" massive `if/else` blocks and creates a clean, git-like interface where each mode has its own help and arguments.

	 

	#### 5. Use Native Unreal Types via String Conversion

	`CLI11` works best with standard types (`int`, `std::string`). When receiving paths, parse them as `std::string` and then convert them back to `FString` using `UTF8_TO_TCHAR` for use within Unreal's file systems. This ensures you maintain compatibility with Unreal's Unicode requirements.

	 

	#### 6. Custom Validation with CLI11 Validators

	Use the `.check()` modifier to "eliminate" invalid inputs before your logic even runs. For example, if your tool requires a path to a specific `.uproject` file, use `CLI::ExistingFile`:

	```cpp

	std::string ProjectPath;

	App.add_option("-p,--project", ProjectPath, "Path to .uproject")

	   ->required()

	   ->check(CLI::ExistingFile);

	```

	 

	#### 7. Wrap in Exception Handling

	`CLI11` throws exceptions by design (e.g., `CLI::ParseError`). Since Unreal often compiles with exceptions disabled, ensure you use the `CLI11_PARSE` macro or wrap your `App.parse()` in a way that captures the error and outputs it to `UE_LOG` or `FMessageDialog` rather than crashing.

	 

	#### 8. Generate Automated Help for Build Farms

	One of the best features of `cli11` is the automated `--help` flag. Use this to "eliminate" documentation desync. When your CI/CD pipeline or build farm engineers need to know the parameters for your custom tool, they can simply run `MyTool.exe --help` to get an up-to-date manifest of all available options.
Copy code
Use for Build Farm Automation Use cli11 to build custom “Pre-flight” or “Cook-validation” tools. By providing a clean interface for your build farm scripts, you can “eliminate” configuration errors in your CI/CD pipeline, making it easier for engineers to maintain the automation logic.