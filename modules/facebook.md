---
layout: default
title: Facebook
---

<!-- ai-generation-failed -->

<h1>Facebook</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Facebook/Facebook.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li><li><span class="label">依赖</span><span class="value">Swift</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

SS) that provides integration between Unreal Engine and the Meta/Facebook platform. It is primarily used to facilitate social features, authentication, and data sharing within mobile and PC games.

What it is and What it’s used for

Located under the Plugins/Online directory, the OnlineSubsystemFacebook module acts as a wrapper for the Facebook SDK. It translates Unreal’s generic Online Subsystem interfaces into Facebook-specific API calls.

Primary uses include:

Identity & Authentication: Allowing players to log into your game using their Facebook credentials (SSO).
Social Graph Integration: Retrieving a player’s friends list (who also play the game) to facilitate invites or leaderboards.
Presence & Sharing: Enabling players to share achievements, screenshots, or high scores directly to their Facebook feed.
User Profile Data: Accessing basic user information like name, profile picture URL, and locale to personalize the UI.
Practical Usage Tips and Best Practices
1. Configure the Module in DefaultEngine.ini

To enable the module, you must register it in your project’s configuration files. Adding the Facebook App ID and related settings is required for the engine to initialize the SDK correctly.

ini
	[OnlineSubsystemFacebook]

	bEnabled=true

	AppId="YOUR_APP_ID"

	ClientToken="YOUR_CLIENT_TOKEN"
Copy code

Ensure you also add Facebook to your DefaultPlatformService if it is your primary login method.

2. Handle Permissions Incrementally

Facebook requires specific permissions for different data (e.g., public_profile, user_friends). A best practice is to request only the minimum required permissions during the initial login. Requesting too many permissions upfront can lead to higher player drop-off rates and the elimination of user trust.

3. Use the Identity Interface for Login

Avoid calling Facebook SDK functions directly. Instead, use the IOnlineIdentity interface provided by the Online Subsystem. This keeps your code cross-platform; if you later add Google or Steam login, the core logic remains the same, requiring only a change in the subsystem name.

4. Manage Login State Changes

Users may revoke app permissions or log out via the Facebook website. Always bind to the OnLoginStatusChanged delegate. This ensures your game can react immediately if the session becomes invalid, allowing for a graceful elimination of the current social session and a return to the main menu.

5. Cache Profile Pictures Locally

Retrieving a profile picture via the Facebook Graph API returns a URL. Do not download this URL every time the UI opens. Use a DownloadImage node or a custom C++ downloader to cache the texture locally in memory for the duration of the session to prevent UI stuttering and excessive API calls.

6. Verify Android/iOS Proguard Rules

When packaging for mobile, the Facebook SDK often requires specific Proguard or Linker rules to prevent the “stripping” of necessary Java/Objective-C code. Check the Facebook_UPL.xml file within the plugin to ensure your project’s build settings are correctly injecting the required dependencies into the final binary.

7. Use the “Friends” Interface for Social Features

To show a “Play with Friends” list, use IOnlineFriends::ReadFriendsList. Note that Facebook only returns friends who have also authorized your specific game. If the list returns empty, verify that your Facebook App is in “Live” mode rather than “Development” mode, as dev mode restricts data to testers only.

8. Strategic Elimination of Hard References

If your game is cross-platform, wrap Facebook-specific logic in a Blueprint Interface or a generic Data Asset. This prevents the rest of your gameplay code from having a “hard dependency” on the Facebook module, which makes it much easier to compile the game for platforms where Facebook is not supported (like certain consoles).