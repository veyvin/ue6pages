---
layout: default
title: AutomationController
---

<!-- ai-generation-failed -->

<h1>AutomationController</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AutomationController/AutomationController.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetRegistry, AutomationMessages, AutomationTest, Core, CoreUObject, EditorFramework, Engine, HTTP, Json, JsonUtilities, MessageLog, ScreenShotComparisonTools, UnrealEdMessages</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the AutomationTest framework defines how a test runs, the AutomationController is responsible for coordinating those tests across one or more engine instances (local or remote), making it essential for Quality Assurance (QA) and Continuous Integration (CI) pipelines.

Practical Usage Tips and Best Practices
1. Decouple Discovery from Execution

The module separates finding tests from running them. When using the Session Frontend, always click Refresh to allow the AutomationController to query the loaded modules for new tests. If you’ve recently added a C++ test and it isn’t appearing, ensure the module containing the test is correctly loaded in the current session.

2. Utilize Filters to Prevent Bloat

In large projects, the list of available tests can be overwhelming. Use the AutomationController filtering system to group tests by Smoke, Engine, or Project. Marking your most critical unit tests as “Smoke” allows you to run a lightweight validation pass in seconds, ensuring that a simple code change hasn’t “eliminated” core functionality.

3. Parallel Execution on Remote Instances

One of the module’s most powerful features is the ability to coordinate tests across multiple machines. By selecting multiple instances in the Session Browser, the AutomationController can distribute a large test suite across several devices, significantly reducing the total time required for full project validation.

4. Automated Reporting via Command Line

For CI/CD pipelines (like Jenkins or GitHub Actions), you can trigger the AutomationController logic via command-line arguments. Use -ExecCmds="Automation RunTests [TestName]" to run specific tests and -ReportOutputPath="[Path]" to have the controller generate machine-readable JSON or HTML reports.

5. Handle “Eliminated” Test Targets

When running tests on remote devices (like consoles or mobile), the connection may drop. The AutomationController tracks the “health” of each session instance. If a device crashes during a test, the controller will mark the test as “Aborted” rather than “Failed,” which is a critical distinction when debugging hardware-specific crashes.

6. Leverage Screen Shot Comparison

The module integrates with the Screenshot Comparison Tool. When an automation test captures a frame, the AutomationController handles the metadata transfer to the comparison tool, allowing you to visually verify UI or rendering changes against a “Ground Truth” image.

7. Monitor the “Worker” State

If tests are queued but not starting, check the Worker status in the Session Frontend. The AutomationController relies on the engine being in a “ready” state; if the engine is currently “hitching” or performing a heavy asset load, the controller will defer test execution to prevent false-negative results caused by performance spikes.

C++ Access and Implementation

To interact with the controller via code (for example, building a custom Editor Utility to trigger tests), you access the module’s interface:

C++
	#include "IAutomationControllerModule.h"

	 

	void UMyAutomationHelper::RunProjectSmokeTests()

	{

	    // Get the Automation Controller Module

	    IAutomationControllerModule& AutomationModule = FModuleManager::LoadModuleChecked<IAutomationControllerModule>("AutomationController");

	    

	    TSharedPtr<IAutomationControllerManager> Manager = AutomationModule.GetAutomationController();

	 

	    if (Manager.IsValid())

	    {

	        // Update the list of available tests

	        Manager->RequestTestsReply(EAutomationArtifactType::None);

	        

	        // Set a filter (e.g., only Smoke tests)

	        Manager->SetFilter(EAutomationTestFilterType::Smoke);

	        

	        // Command the controller to begin execution

	        Manager->RunTests();

	    }

	}
Copy code
Performance & Best Practices
Module Dependency: Always wrap "AutomationController" in an #if WITH_EDITOR or Developer module block in your Build.cs, as it is not intended for use in Shipping builds.
Log Verbosity: If tests are failing without clear errors, use the console command Log LogAutomationController Verbose to see the internal communication between the controller and the test workers.
Cleanup: Ensure your tests use the PostTest cleanup logic. The AutomationController expects the environment to be reset after each test; failing to do so can cause “pollution” where one test’s failure causes a cascade of “eliminations” in subsequent tests.