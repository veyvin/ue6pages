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

ables) and command-line tools where complex argument structures, subcommands, and advanced validation are required.

It is located in Engine/Source/ThirdParty/CLI11 and is used by modern internal tools like the UnrealHeaderTool (C++ version) and various build utilities to provide a professional CLI experience.

Practical Usage Tips and Best Practices
1. Use for Standalone “Programs”

CLI11 is best suited for standalone C++ programs (built via .Target.cs with TargetType.Program) rather than standard gameplay modules.

Best Practice: If you are building a custom data-processing tool or a build-pipeline utility, use CLI11. For standard gameplay flags (like -log), stick to the native FParse system to maintain engine consistency and eliminate unnecessary complexity.
2. Link as a Third-Party Dependency

To use CLI11 in your tool’s Build.cs file, you must explicitly link it as a third-party dependency to include the correct header paths.

Action: Add the following line to your module’s Build.cs:
C#
	    AddEngineThirdPartyPrivateStaticDependencies(Target, "CLI11");

	    ```

	 

	#### 3. Wrap Includes for Platform Compatibility

	Because CLI11 is a third-party library, its headers may occasionally conflict with Unreal’s macro system (like `check` or `verify`).

	*   **Tip:** Always wrap the inclusion of CLI11 headers using Unreal’s third-party guard macros to **eliminate** compiler warnings or macro shadowing.

	    ```cpp

	    THIRD_PARTY_INCLUDES_START

	    #include "CLI11/CLI11.hpp"

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	#### 4. Leverage Subcommands for Complex Tools

	CLI11 excels at "Git-style" subcommands (e.g., `MyTool.exe upload` vs `MyTool.exe download`).

	*   **Best Practice:** Instead of using dozens of loose flags, organize your tool's logic into subcommands. This makes the CLI more discoverable and allows you to **eliminate** conflicting arguments by scoping them to specific modes of operation.

	 

	#### 5. Implement Advanced Validation

	One of the strongest features of CLI11 is its built-in validators (e.g., checking if a file exists or if a number is within a range).

	*   **Tip:** Use `CLI::ExistingFile` or `CLI::Range` when defining your options. This allows the parser to automatically reject invalid input and print a helpful error message before your code even starts running, **eliminating** the need for manual "Sanity Check" logic.

	 

	#### 6. Handle Unreal Strings (FString vs std::string)

	CLI11 is a standard C++ library and operates on `std::string`.

	*   **Action:** When passing arguments to CLI11, convert Unreal’s `FString` or `TCHAR*` to `std::string`. After parsing, convert the results back to `FString` using `UTF8_TO_TCHAR()` if your tool needs to interact with other Unreal Engine modules.

	 

	#### 7. Automate Help Text Generation

	CLI11 automatically generates a formatted `--help` output based on the descriptions you provide for your options.

	*   **Best Practice:** Always provide a descriptive string for every option and subcommand. This ensures that your tool is self-documenting, **eliminating** the need for external `README` files for basic usage instructions.

	 

	#### 8. Use with 'FCommandLine::Get()'

	If you are integrating CLI11 into an existing Unreal Program, you can feed it the engine's command-line string.

	*   **Tip:** Use `CLI11_PARSE(App, std::string(TCHAR_TO_UTF8(FCommandLine::Get())))` to allow the CLI11 parser to process the arguments passed to the executable via the Unreal Engine launcher or build system.
Copy code
3. Wrap Includes for Macro Compatibility

Unreal Engine’s macro system (especially check and verify) can sometimes conflict with standard C++ libraries.

Tip: Always wrap the CLI11 header inclusion with Unreal’s third-party guard macros. This will eliminate compiler warnings or macro shadowing errors during the build.
C#
	    AddEngineThirdPartyPrivateStaticDependencies(Target, "CLI11");

	    ```

	 

	#### 3. Wrap Includes for Platform Compatibility

	Because CLI11 is a third-party library, its headers may occasionally conflict with Unreal’s macro system (like `check` or `verify`).

	*   **Tip:** Always wrap the inclusion of CLI11 headers using Unreal’s third-party guard macros to **eliminate** compiler warnings or macro shadowing.

	    ```cpp

	    THIRD_PARTY_INCLUDES_START

	    #include "CLI11/CLI11.hpp"

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	#### 4. Leverage Subcommands for Complex Tools

	CLI11 excels at "Git-style" subcommands (e.g., `MyTool.exe upload` vs `MyTool.exe download`).

	*   **Best Practice:** Instead of using dozens of loose flags, organize your tool's logic into subcommands. This makes the CLI more discoverable and allows you to **eliminate** conflicting arguments by scoping them to specific modes of operation.

	 

	#### 5. Implement Advanced Validation

	One of the strongest features of CLI11 is its built-in validators (e.g., checking if a file exists or if a number is within a range).

	*   **Tip:** Use `CLI::ExistingFile` or `CLI::Range` when defining your options. This allows the parser to automatically reject invalid input and print a helpful error message before your code even starts running, **eliminating** the need for manual "Sanity Check" logic.

	 

	#### 6. Handle Unreal Strings (FString vs std::string)

	CLI11 is a standard C++ library and operates on `std::string`.

	*   **Action:** When passing arguments to CLI11, convert Unreal’s `FString` or `TCHAR*` to `std::string`. After parsing, convert the results back to `FString` using `UTF8_TO_TCHAR()` if your tool needs to interact with other Unreal Engine modules.

	 

	#### 7. Automate Help Text Generation

	CLI11 automatically generates a formatted `--help` output based on the descriptions you provide for your options.

	*   **Best Practice:** Always provide a descriptive string for every option and subcommand. This ensures that your tool is self-documenting, **eliminating** the need for external `README` files for basic usage instructions.

	 

	#### 8. Use with 'FCommandLine::Get()'

	If you are integrating CLI11 into an existing Unreal Program, you can feed it the engine's command-line string.

	*   **Tip:** Use `CLI11_PARSE(App, std::string(TCHAR_TO_UTF8(FCommandLine::Get())))` to allow the CLI11 parser to process the arguments passed to the executable via the Unreal Engine launcher or build system.
Copy code
4. Leverage “Git-Style” Subcommands

CLI11 excels at creating tools with subcommands (e.g., MyTool.exe pack vs MyTool.exe unpack).

Best Practice: Instead of using dozens of loose boolean flags, organize your tool’s logic into subcommands. This makes the interface more discoverable and allows you to eliminate argument conflicts by scoping options to specific modes.
5. Implement Advanced Input Validation

CLI11 provides built-in “Validators” that check inputs before your main code even runs.

Tip: Use validators like CLI::ExistingFile, CLI::Range, or CLI::IsMember. This allows the parser to automatically reject invalid data and print helpful error messages, eliminating the need for manual “if-checks” at the start of your main() function.
6. Feed Unreal’s Command Line to the Parser

When running a program through the Unreal environment, you can pass the engine’s global command line into the CLI11 app.

Action: In your main or Run function, use:
C#
	    AddEngineThirdPartyPrivateStaticDependencies(Target, "CLI11");

	    ```

	 

	#### 3. Wrap Includes for Platform Compatibility

	Because CLI11 is a third-party library, its headers may occasionally conflict with Unreal’s macro system (like `check` or `verify`).

	*   **Tip:** Always wrap the inclusion of CLI11 headers using Unreal’s third-party guard macros to **eliminate** compiler warnings or macro shadowing.

	    ```cpp

	    THIRD_PARTY_INCLUDES_START

	    #include "CLI11/CLI11.hpp"

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	#### 4. Leverage Subcommands for Complex Tools

	CLI11 excels at "Git-style" subcommands (e.g., `MyTool.exe upload` vs `MyTool.exe download`).

	*   **Best Practice:** Instead of using dozens of loose flags, organize your tool's logic into subcommands. This makes the CLI more discoverable and allows you to **eliminate** conflicting arguments by scoping them to specific modes of operation.

	 

	#### 5. Implement Advanced Validation

	One of the strongest features of CLI11 is its built-in validators (e.g., checking if a file exists or if a number is within a range).

	*   **Tip:** Use `CLI::ExistingFile` or `CLI::Range` when defining your options. This allows the parser to automatically reject invalid input and print a helpful error message before your code even starts running, **eliminating** the need for manual "Sanity Check" logic.

	 

	#### 6. Handle Unreal Strings (FString vs std::string)

	CLI11 is a standard C++ library and operates on `std::string`.

	*   **Action:** When passing arguments to CLI11, convert Unreal’s `FString` or `TCHAR*` to `std::string`. After parsing, convert the results back to `FString` using `UTF8_TO_TCHAR()` if your tool needs to interact with other Unreal Engine modules.

	 

	#### 7. Automate Help Text Generation

	CLI11 automatically generates a formatted `--help` output based on the descriptions you provide for your options.

	*   **Best Practice:** Always provide a descriptive string for every option and subcommand. This ensures that your tool is self-documenting, **eliminating** the need for external `README` files for basic usage instructions.

	 

	#### 8. Use with 'FCommandLine::Get()'

	If you are integrating CLI11 into an existing Unreal Program, you can feed it the engine's command-line string.

	*   **Tip:** Use `CLI11_PARSE(App, std::string(TCHAR_TO_UTF8(FCommandLine::Get())))` to allow the CLI11 parser to process the arguments passed to the executable via the Unreal Engine launcher or build system.
Copy code
7. Automate “Help” Generation

CLI11 automatically generates formatted help text based on the descriptions you provide for your options.

Best Practice: Always provide a descriptive string for every option (e.g., app.add_option("-f", file, "Path to the config file");). This ensures that users can simply type --help to see a full manual, eliminating the need for external documentation for basic tool usage.
8. Convert Between std::string and FString

Because CLI11 is a standard C++ library, it uses std::string.

Tip: Use the TCHAR_TO_UTF8 and UTF8_TO_TCHAR macros when moving data between CLI11 and Unreal’s FString. This ensures that your tool handles file paths and names correctly across different platforms, eliminating encoding errors.