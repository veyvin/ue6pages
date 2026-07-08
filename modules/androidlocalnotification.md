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

ngine that interfaces with the native Android NotificationManager API. It allows developers to schedule and manage notifications directly on the user’s device without requiring a remote server or persistent internet connection.

This module is essential for mobile developers to implement engagement features such as “Energy Refilled” alerts, daily reward reminders, or notification of timed “elimination” events in-game.

Practical Usage Tips and Best Practices
Module Dependency and Build Setup To use this module in C++, you must include it in your project’s Build.cs. It is best practice to wrap this in a platform check to prevent errors when compiling for other platforms like Windows or iOS.
C++
	    // In YourProject.Build.cs

	    if (Target.Platform == UnrealTargetPlatform.Android)

	    {

	        PrivateDependencyModuleNames.Add("AndroidLocalNotification");

	    }

	    ```

	 

	*   **Handle Android 13+ Permissions**

	    Since Android 13 (API 33), local notifications require the `POST_NOTIFICATIONS` permission. You must call the **Register for Remote Notifications** Blueprint node (or `RegisterForRemoteNotifications` in C++) during your first-run experience to trigger the system-level permission dialog; otherwise, scheduled notifications will be silently blocked by the OS.

	 

	*   **Enable Reboot Persistence**

	    By default, Android clears all scheduled notifications when a device is restarted. To fix this, navigate to **Project Settings > Platforms > Android** and enable **"Restore scheduled local notification on reboot."** This adds the necessary `RECEIVE_BOOT_COMPLETED` intent filter to your manifest automatically.

	 

	*   **Use Notification IDs to Prevent Spam**

	    Use `ScheduleLocalNotificationAtTimeOverrideId` instead of the generic schedule function. By providing a fixed **ID**, you ensure that if you schedule a "Come back and play!" notification multiple times, it will overwrite the previous one rather than creating five separate entries in the user’s tray.

	 

	*   **Utilize the ActivationEvent String**

	    The `ActivationEvent` is a powerful string metadata field. When the user taps a notification, you can retrieve this string using `GetLaunchNotification` in your `GameInstance`. Use this to route the player to specific menus (e.g., if the string is `"DAILY_REWARD"`, open the store immediately upon launch).

	 

	*   **Format for Time Zones**

	    When scheduling, distinguish between **Local Time** and **UTC**. For "Daily Rewards," use Local Time so the notification arrives at 9:00 AM for every player regardless of their region. For "Elimination" events in a global tournament, use UTC to ensure everyone is notified at the exact same moment.

	 

	*   **Custom Icons via UPL**

	    The default Unreal icon is often used for notifications. To provide a custom branded icon, you must use **Unreal Plugin Language (UPL)** to inject resource tags into your manifest and place your `.png` icons in the `Build/Android/res/drawable` folder. The system looks for an icon named `ic_stat_notify` by default.

	 

	*   **Clear Notifications on App Launch**

	    It is a common UX pitfall to leave old notifications in the tray after the player has already opened the game manually. In your `BeginPlay`, call `CancelLocalNotification` using the IDs for your generic reminders to "eliminate" stale notifications that are no longer relevant.
Copy code
Handle Android 13+ Permissions Since Android 13 (API level 33), applications must explicitly request the POST_NOTIFICATIONS permission. Use the Register for Remote Notifications Blueprint node (or the C++ equivalent) to trigger the system permission dialog. Without this, the OS will silently “eliminate” any notifications you attempt to send.
Enable Reboot Persistence By default, Android clears all scheduled notifications when the device restarts. To ensure your notifications survive a reboot, go to Project Settings > Android and check the box for “Restore scheduled local notification on reboot.” This automatically adds the necessary RECEIVE_BOOT_COMPLETED permissions to your Android Manifest.
Overwrite Notifications with Unique IDs Use the ScheduleLocalNotificationAtTimeOverrideId function instead of the generic schedule node. By providing a specific ID, you can update an existing notification instead of creating duplicates. This prevents “spamming” the user’s tray if multiple “elimination” warnings are triggered for the same event.
Use the ActivationEvent String for Deep Linking The ActivationEvent parameter is a metadata string passed back to your game when the user taps the notification. In your GameInstance or GameMode, check GetLaunchNotification on startup to read this string. You can use it to send the player directly to a specific shop item or game level.
Clear Notifications on Manual App Launch If a player opens your game manually before a scheduled notification triggers, that notification may still appear later and feel redundant. Use CancelLocalNotification with the specific ID or CancelAllLocalNotifications in your BeginPlay to “eliminate” stale reminders once the player is already active.
Time Zone Awareness When scheduling, decide between Local Time and UTC. For “Daily Rewards,” use Local Time so the player receives it at 9:00 AM in their own time zone. For global tournament “elimination” deadlines, use UTC to ensure the notification fires at the exact same moment for all players worldwide.
Customizing the Notification Icon The engine uses a default icon unless specified otherwise. To use your own branding, you must place your .png icons in Build/Android/res/drawable and use Unreal Plugin Language (UPL) to point the manifest to your custom resource. The system typically looks for an icon named ic_stat_notify.