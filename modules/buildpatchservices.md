---
layout: default
title: BuildPatchServices
---

<!-- ai-generation-failed -->

<h1>BuildPatchServices</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Online/BuildPatchServices/BuildPatchServices.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, AnalyticsET, Core, CoreUObject, HTTP, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

foundation for Unreal Engine’s patching and installation system. It is the core technology used by the Epic Games Launcher to deliver updates efficiently. It handles the “heavy lifting” of patch generation: chunking large files into smaller pieces, generating manifests, performing delta patching (downloading only changed data), and verifying file integrity via hashing.

1. Master the Build.cs Dependency

To utilize the BuildPatchServices API in your C++ code, you must include the module in your project’s dependency list. Without this, the linker will fail to resolve the patcher and manifest interfaces.

C#
	// Inside YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { 

	    "Core", 

	    "CoreUObject", 

	    "Engine", 

	    "BuildPatchServices" // Required for IBuildPatchServices

	});

	```

	 

	### 2. Understand the Manifest vs. Chunk Relationship

	The system works on two distinct layers:

	*   **Manifest (.manifest):** A text or binary file containing metadata about your build—a list of every file, its size, its hash, and which "chunks" it is composed of.

	*   **Chunks (.chunk):** The actual binary data. The system breaks your `.pak` files into small, re-usable pieces. If you change 1MB of data in a 10GB file, only the affected chunks are updated.

	 

	### 3. Asynchronous Verification for UX

	Verification (hashing) of large builds can take minutes. Never run `IBuildPatchServices::VerifyInstall` on the Game Thread.

	*   **Best Practice:** Always use the provided delegates (`FBuildPatchProgress` and `FBuildPatchComplete`) to monitor progress on a background thread and update your UI via an `AsyncTask` to the Game Thread.

	 

	```cpp

	// Basic C++ snippet for accessing the service

	#include "Interfaces/IBuildPatchServicesModule.h"

	 

	void AMyGameLauncher::VerifyGameData(FString ManifestPath, FString InstallDirectory)

	{

	    IBuildPatchServicesModule& BPSModule = FModuleManager::LoadModuleChecked<IBuildPatchServicesModule>("BuildPatchServices");

	    

	    FBuildPatchAppManifestPtr Manifest = BPSModule.LoadManifestFromFile(ManifestPath);

	    if (Manifest.IsValid())

	    {

	        // Define your verification configuration

	        // Use delegates to prevent Game Thread blocking

	    }

	}

	```

	 

	### 4. Optimize Chunk Size for Your CDN

	In your Build Configuration (usually in the `DefaultEngine.ini` or via Command Line arguments during cooking), you can adjust the target chunk size.

	*   **Tip:** For mobile, smaller chunks (~1MB-5MB) are better for unstable connections. For desktop/console, larger chunks (~10MB-20MB) improve download throughput by reducing the number of HTTP requests.

	 

	### 5. Use Delta Patching to Save Bandwidth

	The greatest strength of this module is **Delta Patching**. When moving from Version A to Version B, the system compares manifests and only requests the chunks unique to Version B.

	*   **Best Practice:** Ensure your CDN supports "Range Requests" (HTTP 206). `BuildPatchServices` heavily relies on requesting specific byte-ranges of chunk files to minimize data transfer.

	 

	### 6. Implement Staging and Resuming

	The module inherently supports "resumable" downloads. If the user loses internet or closes the launcher, the system tracks which chunks are already in the "Staging" directory.

	*   **Tip:** Always set a dedicated `StagingDirectory` in your patch configuration. This prevents half-finished files from cluttering your actual game directory and makes cleanup easy if a patch is cancelled.

	 

	### 7. Perform Pre-Patch Disk Space Checks

	Before starting a patch, use the manifest to calculate the required space.

	*   **Insight:** A patch requires `CurrentSize + NewSize + StagingSize` during the process. Use the `GetDownloadSize()` and `GetBuildSize()` functions in the manifest interface to check if the user has enough space before they waste bandwidth on a download that will eventually fail.

	 

	### 8. Match Build IDs for Multi-Platform Support

	If you are deploying for multiple platforms (e.g., Windows and Mac), use distinct `BuildID` strings in your manifests. This prevents the patching service from accidentally trying to update a Windows install using Mac chunks, which would lead to a corrupted and unbootable game client.
Copy code
2. Understand Manifests vs. Chunks

The system relies on two components:

Manifest (.manifest): A metadata file containing the build structure, file hashes, and a list of required chunks.
Chunks (.chunk): The actual binary data. The system breaks .pak files into small, re-usable pieces. If a 10GB file changes by only 1MB, only the affected chunks are updated.
3. Use Asynchronous Verification

Verification (hashing) of large builds can take significant time. Never run IBuildPatchServices::VerifyInstall on the Game Thread.

Best Practice: Always use the provided delegates (FBuildPatchProgress and FBuildPatchComplete) to monitor progress on a background thread. This allows you to update your UI without stalling the engine.
4. Optimize Chunk Size for Target Platforms

In your Build Configuration (or via command line during cooking), you can adjust the target chunk size.

Tip: For mobile, smaller chunks (~1MB-5MB) are better for unstable connections. For desktop/console, larger chunks (~10MB-15MB) improve download throughput by reducing the total number of HTTP requests.
5. Leverage Delta Patching

The greatest strength of this module is Delta Patching. When moving from Version A to Version B, the system compares manifests and only requests the specific chunks unique to Version B.

Requirement: Ensure your CDN supports “Range Requests” (HTTP 206). The module heavily relies on requesting specific byte-ranges of chunk files to minimize bandwidth usage.
6. Implement Staging and Resuming

The module inherently supports “resumable” downloads. If the user loses internet or closes the application, the system tracks which chunks are already in the “Staging” directory.

Best Practice: Always set a dedicated StagingDirectory in your patch configuration. This prevents half-finished files from cluttering your actual game directory and makes cleanup easy if a patch is cancelled.
7. Perform Pre-Patch Disk Space Checks

Before starting a patch, use the manifest metadata to calculate the required space.

Insight: A patch requires CurrentSize + NewSize + StagingSize during the process. Use the GetDownloadSize() and GetBuildSize() functions in the manifest interface to check if the user has enough space before they waste bandwidth on a download that will eventually fail.
8. Match Build IDs for Multi-Platform Support

If you are deploying for multiple platforms (e.g., Windows and Mac), use distinct BuildID strings in your manifests. This prevents the patching service from accidentally trying to update a Windows install using Mac chunks, which would lead to a corrupted and unbootable game client. Always check the BuildID during the initialization of the patch process to eliminate cross-platform data corruption.