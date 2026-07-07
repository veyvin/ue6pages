---
layout: default
title: AgilitySDK
---

<!-- ai-generation-failed -->

<h1>AgilitySDK</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Windows/AgilitySDK/AgilitySDK.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li><li><span class="label">依赖</span><span class="value">DirectX</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

n Unreal Engine 5 that decouples DirectX 12 feature support from the Windows Operating System version. It allows UE5 to utilize the latest DX12 features—such as Shader Model 6.6+, Enhanced Barriers, and Work Graphs—on older versions of Windows 10 and 11 that do not yet have these capabilities in the system-level d3d12.dll.

In UE5, this module is essential for modern rendering pipelines, specifically Nanite, which requires advanced shader instructions provided by the SDK to function correctly across various hardware and OS configurations.

1. Control the Version in Target.cs

You can specify which Agility SDK version your project targets by modifying your [ProjectName].Target.cs file. This is useful if you need to lock into a specific version for stability or unlock a cutting-edge feature.

C#
	// In MyProject.Target.cs

	public class MyProjectTarget : TargetRules

	{

	    public MyProjectTarget(TargetInfo Target) : base(Target)

	    {

	        Type = TargetType.Game;

	        DefaultBuildSettings = BuildSettingsVersion.Latest;

	        IncludeOrderVersion = EngineIncludeOrderVersion.Latest;

	        

	        // Example: Pinning to a specific Agility SDK version if needed

	        // The default version is usually managed by the Engine's D3D12 settings

	        // D3D12AgilitySDKVersion = 611; 

	    }

	}

	```

	 

	### 2. Verify Activation via Logs

	To ensure the Agility SDK is actually being used at runtime, check your project’s log file (`Saved/Logs`). Search for **"D3D12 Agility SDK"**.

	- If working: You will see a log entry stating `D3D12 Agility SDK runtime found.`

	- If failing: It will fall back to the System DirectX 12, which may disable features like Nanite if the Windows version is outdated.

	 

	### 3. Distribution and the "D3D12" Subfolder

	When you package a project, Unreal automatically places the necessary Agility SDK binaries (`D3D12Core.dll` and `d3d12SDKLayers.dll`) into the `Binaries/Win64/D3D12/` subfolder of your packaged build. 

	- **Best Practice:** Never move or delete this subfolder. The Windows loader is instructed by the UE5 executable to look in this specific path to load the "Agile" version of DX12 rather than the system one.

	 

	### 4. Required for Nanite and SM6

	In UE 5.1 and later, the Agility SDK is essentially a requirement for **Nanite** on many Windows 10 builds. Nanite relies on **Shader Model 6.6** features (like Atomic64 instructions). Without Agility SDK support, the engine might downgrade to an older Shader Model, causing Nanite meshes to disappear or revert to fallback meshes.

	 

	### 5. Managing Disk Space in Source Control

	The Agility SDK binaries are stored in `Engine/Binaries/ThirdParty/D3D12AgilitySDK/`. If you are using a source-controlled engine build (like a GitHub fork), ensure these binaries are not ignored by your `.gitignore`. If they are missing, your team’s builds will lack the latest DX12 capabilities, leading to "GPU Not Supported" errors even on high-end cards.

	 

	### 6. Debugging with Console Variables

	You can force certain Agility SDK behaviors using console variables or command-line arguments. This is useful for testing compatibility on older machines:

	- **Command Line:** `-d3d12` (Ensures DX12 is used, which triggers Agility SDK loading).

	- **CVar:** `r.D3D12.GpuValidation=1` (Requires the Agility SDK debug layers, which are often bundled within the SDK framework during development).

	 

	### 7. Global Windows Settings

	If you are developing a custom launcher or installer for your game, ensure you do not force the application to run in "Compatibility Mode" for older Windows versions. This can sometimes block the Agility SDK from correctly hooking into the D3D12 loader, forcing the game to use a legacy version of DirectX that lacks UE5's modern rendering features.

	 

	### 8. Handling "Agility SDK version mismatch"

	If you see errors regarding a version mismatch, it usually means your `Binaries/Win64/D3D12` folder contains DLLs from an older engine version. 

	- **Solution:** Clean your `Binaries` and `Intermediate` folders and rebuild the project. The Unreal Build Tool (UBT) will recopy the correct versioned DLLs from the Engine's ThirdParty directory to your project's binary folder.
Copy code
2. Verify Activation via Logs

Always check your project logs (Saved/Logs) to ensure the SDK is loading. Look for the string: D3D12 Agility SDK runtime found. If this is missing, the engine has fallen back to the System DX12, which may result in the elimination of Nanite support or other high-end rendering features on that specific machine.

3. Maintain the Binaries Directory Structure

When a project is packaged, Unreal automatically places D3D12Core.dll and d3d12SDKLayers.dll into the Binaries/Win64/D3D12/ subfolder.

Best Practice: Never move or delete this subfolder in your packaged build. The Windows loader is specifically instructed to look in this directory to load the “Agile” version of DX12 instead of the system default.
4. Required for Nanite and SM6.6

UE 5.1+ relies heavily on Shader Model 6.6 (specifically Atomic64 instructions) for Nanite. Without a functioning Agility SDK, the engine may downgrade to an older Shader Model. This often results in Nanite meshes failing to render or reverting to low-quality fallback meshes, effectively eliminating the visual fidelity of the scene.

5. Source Control Considerations

The SDK binaries are located in Engine/Binaries/ThirdParty/D3D12AgilitySDK/. If you are using a source-controlled engine (e.g., from GitHub), ensure these binaries are not excluded by your .gitignore. If they are missing, your team’s builds will lack modern DX12 capabilities, often leading to “GPU Not Supported” errors.

6. Avoid Compatibility Mode

Ensure that neither the Editor nor your packaged game is set to “Windows Compatibility Mode” in the file properties. Compatibility mode can block the Agility SDK from correctly hooking into the D3D12 loader, forcing the application to use legacy system DLLs and preventing the initialization of modern rendering features.

7. Debugging with Console Variables

If you suspect the Agility SDK is causing stability issues, you can test the system DX12 fallback by using the command line argument -noagilitysdk. Note that this will likely disable Nanite and other SM6-dependent features, but it is a vital step for troubleshooting driver-level crashes.

8. Handling Version Mismatches

If you encounter errors regarding a “Version Mismatch,” it typically means your Binaries folder contains stale DLLs from a previous engine version.

Tip: Clean your Binaries and Intermediate folders. Re-running the Unreal Build Tool (UBT) will ensure the correct DLLs are copied from the Engine’s ThirdParty directory to your project’s binary folder.