---
layout: default
title: CookOnTheFly
---

<!-- ai-generation-failed -->

<h1>CookOnTheFly</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/CookOnTheFly/CookOnTheFly.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Networking, Sockets</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

and server system that allows Unreal Engine to “cook” (convert) assets for a target platform on-demand while the game is running. Instead of waiting for a full, hours-long “Cook by the Book” process, the game client requests only the assets it currently needs over a network socket from a host PC running the editor or a cook server.

It is a vital workflow tool for rapid iteration, allowing developers to change textures, meshes, or Blueprints in the editor and see those changes reflected instantly on a console or mobile device without a full repackage.

1. Module Configuration

To use or extend the Cook on the Fly server logic in C++, you must include it in your Build.cs. Note that this is typically used in editor or commandlet contexts.

C#
	// MyProject.Build.cs

	if (Target.bBuildEditor)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "CookOnTheFly", "CookMetadata" });

	}
Copy code
2. Practical Usage Tips & Best Practices
Optimize with the Zen Server (UE 5.0+)

In modern versions of Unreal, Cook on the Fly is heavily integrated with the Zen Server. The Zen Server acts as a centralized data repository and streaming service. Using Zen “eliminates” the traditional bottlenecks of the older COTF protocol by providing faster data deduplication and more reliable asset streaming to your target devices.

Configure the File Host IP Correctly

For the client to find the cook server, you must pass the server’s local IP address to the game client’s command line. Use the flag -filehostip=XXX.XXX.X.X. Without this, the client will fail to connect and “eliminate” its ability to load any assets not already present in the base executable.

Leverage Iterative Cooking

Always use the -iterate flag when starting your cook server. This ensures the server only recooks assets that have actually changed since the last session. This “eliminates” redundant processing time, making the “on the fly” experience feel significantly more responsive during long development sessions.

Monitor Network Bandwidth

COTF sends raw cooked data over your local network. If you are testing high-resolution 4K textures or massive skeletal meshes, ensure you are on a wired Gigabit connection. Weak Wi-Fi can cause massive hitches or timeouts, which may “eliminate” the stability of your test session.

Use for “Partial” Game Testing

If you are working on a specific level, you don’t need to cook the entire game. COTF only cooks what the player encounters. This “eliminates” the need to manage massive build folders on your mobile or console devkit, as only the “active” assets consume the limited storage space on the device.

Handle Shader Compilation

Shaders are often the biggest hurdle in COTF. Ensure your host machine has a warmed-up Derived Data Cache (DDC). If the cook server has to compile shaders while the client is waiting for a material, the game will freeze. Pre-compiling shaders “eliminates” these “white material” placeholders and stalls.

Debugging Connection Issues

If the client hangs at a loading screen, check the Cook Server log on your PC. It will show real-time requests from the device. If you see “Asset Not Found” errors, it usually means the asset is outside the project’s content root or has a redirector issue that needs to be “eliminated” by fixing up redirectors in the Content Browser.

Transition to “Cook by the Book” for Performance

Never use Cook on the Fly for performance profiling or final QA. Because data is being pulled over a network, load times and frame hitches are unrepresentative of the final product. COTF should be “eliminated” from the workflow once you move from “feature iteration” to “optimization and polish” phases.