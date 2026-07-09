---
layout: default
title: AndroidLocalNotification
---

<!-- ai-generation-failed -->

<h1>AndroidLocalNotification</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Android/AndroidLocalNotification/AndroidLocalNotification.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, Launch</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

at allows Unreal Engine projects to schedule and manage local OS notifications on Android devices. Unlike push notifications, which require a remote server (like Firebase), local notifications are triggered entirely by the application logic on the user’s device.

This module is primarily used to drive player re-engagement by alerting users of in-game events—such as energy refills, completed building upgrades, or “elimination” challenges—even when the application is not actively running in the foreground.

Practical Usage Tips and Best Practices
Configure Project Settings and Permissions Before using the module, you must enable notifications in the Project Settings. Navigate to Platforms > Android and ensure that “Enable Local Notifications” is checked. For modern Android versions (API 33+), you must also request the POST_NOTIFICATIONS permission at runtime using the Android Permission nodes or C++.
Register Notifications on App Startup To ensure the OS is ready to receive and display alerts, call the Register for Remote Notifications node (which also handles local setup) during your initial loading sequence or in the BeginPlay of your Game Instance. This initializes the platform bridge.
Schedule Using “From Now” for Consistency The most reliable way to set an alert is using the Schedule Local Notification from Now node. This avoids issues with time zone shifts or system clock inaccuracies by calculating the delay in seconds relative to the current moment.
Utilize the “Activation Event” for Deep Linking When scheduling a notification, you can provide an Activation Event string. When the user taps the notification, the app launches, and you can retrieve this string using the Get Launch Notification node. Use this to send the player directly to a specific menu, such as a “Daily Elimination Challenge” screen.
Include Module Dependency in C++ If you are implementing custom notification logic in C++, you must add the module to your Build.cs file to access the underlying Android notification wrapper.
C#
	// In YourProject.Build.cs

	if (Target.Platform == UnrealTargetPlatform.Android)

	{

	    PublicDependencyModuleNames.Add("AndroidLocalNotification");

	}
Copy code
Handle App Foreground Logic By default, Android often suppresses notifications if the app is already in the foreground. Use your game logic to check if the app is active; if it is, consider displaying a custom UMG-based alert instead of a system notification to “eliminate” redundant OS pop-ups while the player is already engaged.
Manage Notification Channels The module interfaces with Android’s Notification Channels. You should group your notifications logically (e.g., “Social,” “Gameplay Alerts”). This allows users to silence specific types of alerts (like marketing) while keeping critical alerts (like “Match Found”) active.
Clear Pending Notifications on Launch It is a best practice to call Clear All Local Notifications when the player successfully launches the game. This ensures that the notification drawer is cleaned up and that old alerts for tasks the player is currently completing are “eliminated.”