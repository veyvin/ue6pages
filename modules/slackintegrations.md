---
layout: default
title: SlackIntegrations
---

<!-- ai-generation-failed -->

<h1>SlackIntegrations</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/SlackIntegrations/SlackIntegrations.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, HTTP</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

designed to facilitate automated communication between the engine and Slack workspaces via webhooks and API calls.

Description and Purpose

Found within the engine’s Developer modules, SlackIntegrations provides a C++ interface (ISlackIntegrationsModule) for sending messages, formatted blocks, and attachments to Slack channels. Its primary purpose is to serve as a standardized bridge for DevOps and Pipeline automation. Instead of writing custom JSON and HTTP logic for every internal tool, developers use this module to push notifications regarding Build Status, Automation Test Results, or Editor Performance reports. Because it is a Developer module, it is intended for use in the Editor or commandlet environments and is generally eliminated from final Shipping builds to prevent security risks and unnecessary overhead.

Practical Usage Tips and Best Practices
Implement via Module Manager
To safely access the module in your C++ tools, load it through the FModuleManager. This allows you to check if the module is available before calling functions, helping you eliminate hard crashes if the plugin or module is disabled in certain build configurations:
C++
	    if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	    {

	        PrivateDependencyModuleNames.Add("SlackIntegrations");

	    }

	    ```

	 

	*   **Initialize via the Module Manager**  

	    Access the functionality by loading the module interface. This is the standard way to **eliminate** hard dependencies and safely check if the integration is available:

	    ```cpp

	    ISlackIntegrationsModule& SlackModule = FModuleManager::LoadModuleChecked<ISlackIntegrationsModule>("SlackIntegrations");

	    ```

	 

	*   **Prefer Incoming Webhooks for Simplicity**  

	    The module is most commonly used with **Slack Incoming Webhooks**. This allows you to send messages by simply providing a URL. It helps you **eliminate** the complexity of OAuth2 flows or managing full Bot User tokens if you only need one-way notifications.

	 

	*   **Secure Webhook URLs in `DefaultEngine.ini`**  

	    Never hardcode your Slack Webhook URL in C++. Instead, store it in your project's configuration files under a custom section. This allows you to **eliminate** security risks by using different URLs for development and production environments or excluding sensitive config from public repositories.

	 

	*   **Format with Slack "Blocks" for Readability**  

	    Don't just send raw text. Use the module's support for attachments or Slack's Block Kit formatting to include color-coded bars (e.g., Green for "Build Success," Red for "Build Failure"). This practice helps you **eliminate** confusion when scanning busy dev channels.

	 

	*   **Use for Automation Test Reports**  

	    Bind the Slack output to your `FAutomationTestFramework` callbacks. Automatically posting a summary of failed tests to a `#qa-alerts` channel is a best practice to **eliminate** delays in identifying regressions in the codebase.

	 

	*   **Throttle High-Frequency Notifications**  

	    Slack has rate limits. If you are recording automated performance metrics, do not send a message for every individual frame drop. Batch your data and send a single summary report at the end of the session to **eliminate** being throttled or banned by the Slack API.

	 

	*   **Implement Async Message Handling**  

	    Sending a network request can cause a brief hitch. Ensure your Slack notifications are sent asynchronously (which the module handles internally via the `HttpRequest` system) to **eliminate** frame-rate spikes in the editor while the message is being transmitted.
Copy code
Add Target Checks in Build.cs
Since this is a developer-only tool, ensure you wrap the dependency in a target check within your module’s Build.cs file. This practice ensures the module is eliminated from your game’s final distribution:
C++
	    if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	    {

	        PrivateDependencyModuleNames.Add("SlackIntegrations");

	    }

	    ```

	 

	*   **Initialize via the Module Manager**  

	    Access the functionality by loading the module interface. This is the standard way to **eliminate** hard dependencies and safely check if the integration is available:

	    ```cpp

	    ISlackIntegrationsModule& SlackModule = FModuleManager::LoadModuleChecked<ISlackIntegrationsModule>("SlackIntegrations");

	    ```

	 

	*   **Prefer Incoming Webhooks for Simplicity**  

	    The module is most commonly used with **Slack Incoming Webhooks**. This allows you to send messages by simply providing a URL. It helps you **eliminate** the complexity of OAuth2 flows or managing full Bot User tokens if you only need one-way notifications.

	 

	*   **Secure Webhook URLs in `DefaultEngine.ini`**  

	    Never hardcode your Slack Webhook URL in C++. Instead, store it in your project's configuration files under a custom section. This allows you to **eliminate** security risks by using different URLs for development and production environments or excluding sensitive config from public repositories.

	 

	*   **Format with Slack "Blocks" for Readability**  

	    Don't just send raw text. Use the module's support for attachments or Slack's Block Kit formatting to include color-coded bars (e.g., Green for "Build Success," Red for "Build Failure"). This practice helps you **eliminate** confusion when scanning busy dev channels.

	 

	*   **Use for Automation Test Reports**  

	    Bind the Slack output to your `FAutomationTestFramework` callbacks. Automatically posting a summary of failed tests to a `#qa-alerts` channel is a best practice to **eliminate** delays in identifying regressions in the codebase.

	 

	*   **Throttle High-Frequency Notifications**  

	    Slack has rate limits. If you are recording automated performance metrics, do not send a message for every individual frame drop. Batch your data and send a single summary report at the end of the session to **eliminate** being throttled or banned by the Slack API.

	 

	*   **Implement Async Message Handling**  

	    Sending a network request can cause a brief hitch. Ensure your Slack notifications are sent asynchronously (which the module handles internally via the `HttpRequest` system) to **eliminate** frame-rate spikes in the editor while the message is being transmitted.
Copy code
Prefer Incoming Webhooks for Simple Alerts
The module is most efficient when used with Slack Incoming Webhooks. This allows you to post messages using a simple URL without managing complex OAuth2 tokens. It is the best way to eliminate implementation complexity for one-way notifications like “Build Complete.”
Secure Webhook URLs in Configuration
Never hardcode Slack URLs or API keys in your source code. Store them in DefaultEngine.ini or use environment variables on your build server. This helps you eliminate the risk of sensitive credentials being committed to public or shared source control repositories.
Utilize Slack “Blocks” for Readability
Rather than sending raw text, use the module’s support for the Slack Block Kit. Use sections and “accessory” elements to include images or color-coded status bars (e.g., Green for success, Red for failure). This helps eliminate visual noise in busy development channels.
Automate Post-Build Reports
Integrate the Slack client into your BuildGraph or automated cook scripts. Automatically posting a summary of warnings or the location of the new build to a #dev-builds channel is a best practice to eliminate friction in the team’s daily workflow.
Implement Async Handling to Avoid Hitches
The module uses the engine’s HttpRequest system, which is asynchronous. Always ensure your UI or editor tools do not “block” the main thread while waiting for a Slack confirmation. This ensures you eliminate frame-rate spikes or editor freezes when a message is being transmitted.
Throttle High-Frequency Logs
Slack API has strict rate limits. Do not send a message for every individual error in a log. Instead, batch your notifications into a single summary report at the end of a process. This helps you eliminate the risk of being throttled or having your webhook temporarily disabled by Slack.