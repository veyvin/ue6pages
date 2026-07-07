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

ates Unreal Engine with the Android native notification system. It allows developers to schedule and manage notifications that appear in the Android system tray, even when the application is not actively running.

This module acts as a wrapper for the GCM/FCM (Firebase Cloud Messaging) and local intent-based notification services, ensuring that “Register for Remote Notifications” and “Schedule Local Notification” calls in C++ or Blueprints are correctly translated into Android Intents.

Practical Usage Tips and Best Practices
1. Configure C++ Module Dependencies

To use notification-specific classes or handle notification-related events in C++, you must add the module to your Build.cs file. Note that it should be wrapped in an Android platform check to avoid compilation errors on other platforms.

C#
	// In YourProject.Build.cs

	if (Target.Platform == UnrealTargetPlatform.Android)

	{

	    PublicDependencyModuleNames.Add("AndroidLocalNotification");

	}
Copy code
2. Enable Remote Notifications Support

For the module to function, you must manually enable it in the project settings. If this is not enabled, the underlying Java classes will not be initialized.

Location: Project Settings > Project > All Settings
Search for: “Enable Remote Notifications Support”
Requirement: This must be enabled for both local and remote notifications to work on Android.
3. Manage Android 13+ Permissions

Starting with Android 13 (API Level 33), notifications require a runtime permission.

Best Practice: Before calling Schedule Local Notification, use the Check Android Permission node or C++ equivalent for android.permission.POST_NOTIFICATIONS. If the permission is denied, the user will be effectively eliminated from receiving your updates.
4. Configure Notification Channels

Modern Android versions require “Channels” to categorize notifications.

Best Practice: In Project Settings > Platforms > Android, ensure you define your default notification channel. Without a valid channel ID, the Android OS may block the notification from appearing.
5. Handle App Launch from Notification

When a user taps a notification, the app is launched with specific “Activation Event” data.

Tip: Use the Get Launch Notification node in your GameInstance or initial Level Blueprint. Check if the app was launched via a notification and use the “Action” string to direct the user to a specific menu or reward, rather than just the main menu.
6. Set Up the “Restore on Reboot” Feature

By default, scheduled notifications may be cleared if the device restarts.

Best Practice: Enable “Enable Local Notification Restore on Reboot” in the Android Project Settings. This adds a RECEIVE_BOOT_COMPLETED receiver to your AndroidManifest.xml, ensuring your scheduled events survive a device power cycle.
7. Icon and Small Icon Customization

Android requires a specific “Small Icon” (usually a white silhouette on a transparent background) for the status bar.

Tip: Place your custom notification icons in Build/Android/res/drawable/. If you do not provide a proper silhouette icon, Android will often display a generic white square, which can harm the perceived quality of your game.
8. Prevent Notification Spam

Local notifications are persistent. If you schedule a notification every time a player closes the app, you may clutter their tray.

Best Practice: Always call Clear All Local Notifications before scheduling new ones. This ensures that old or redundant alerts are eliminated, providing a cleaner user experience.