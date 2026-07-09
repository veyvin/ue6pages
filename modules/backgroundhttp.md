---
layout: default
title: BackgroundHTTP
---

<!-- ai-generation-failed -->

<h1>BackgroundHTTP</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Online/BackgroundHTTP/BackgroundHTTP.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, BackgroundHTTPFileHash, BackgroundHttpIOS, Core, CoreUObject, Engine, HTTP</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nreal Engine designed to handle long-running, asynchronous HTTP tasks—specifically large file downloads—that can persist even when the application is moved to the background or suspended by the operating system.

Unlike the standard HTTP module, which is typically tied to the active application lifecycle, BackgroundHttp leverages native platform APIs (like NSURLSession on iOS or DownloadManager on Android) to ensure that critical downloads (such as DLC or patches) continue even if the player switches apps or locks their device.

Practical Usage Tips and Best Practices
1. Add Module Dependencies

To use this module, you must add it to your Build.cs file. It is often paired with HTTP for small metadata requests and JSON for parsing manifest files.

C#
	PublicDependencyModuleNames.AddRange(new string[] { "Http", "BackgroundHttp" });

	```

	 

	#### 2. Distinguish Large Downloads from API Calls

	Never use `BackgroundHttp` for standard REST API calls (like logging in or fetching player stats). The standard `HTTP` module is much faster and lighter for small JSON payloads. Use `BackgroundHttp` exclusively for large binary assets (e.g., `.pak` files) where interruption is likely.

	 

	#### 3. Verify Disk Space Before Starting

	Since background downloads are typically large, always use `FPlatformMisc::GetDiskFreeSpace` before initializing a request. If the download fails midway due to a full disk, the OS may "eliminate" the task without a clear error message in the engine logs, leading to a confusing user experience.

	 

	#### 4. Handle Mobile App Suspension

	On iOS and Android, the engine's main thread is often frozen when backgrounded. `BackgroundHttp` is thread-safe and interacts with the OS-level download service. When the app resumes, the `IBackgroundHttpManager` will automatically fire the completion or progress delegates for all work finished while the engine was "sleeping."

	 

	#### 5. Implement Resumable Logic

	`BackgroundHttp` supports resumable downloads natively on most platforms. If a user loses connection or manually closes the app, you can re-create the request with the same URL. The module will check the local temporary directory for a partial file and attempt to resume from the last byte received, rather than starting over.

	 

	#### 6. Use Notification Objects for UI

	If you need to show a persistent progress bar in the UI that survives level transitions, bind your delegates to a **Global Game Instance Subsystem** rather than an Actor or Widget. This prevents your callbacks from being "eliminated" by garbage collection if the player moves from the "Launcher" level to the "Main Menu" while the download is still active.

	 

	#### 7. Clean Up Temporary Files

	The module stores partial downloads in a platform-specific cache folder. If a request is cancelled or fails permanently, ensure you call `Manager->DeleteTemporaryFilesForRequest(Request)` to prevent orphaned data from bloating the user's storage.

	 

	---

	 

	### C++ Implementation Example: Basic Background Download

	 

	To start a background request, you access the manager through the module singleton:

	 

	```cpp

	#include "BackgroundHttpModule.h"

	#include "Interfaces/IBackgroundHttpRequest.h"

	#include "Interfaces/IBackgroundHttpManager.h"

	 

	void UMyDownloadSubsystem::StartAssetDownload(FString URL, FString SavePath)

	{

	    // 1. Get the Background HTTP Manager

	    FBackgroundHttpModule& BackgroundHttpModule = FModuleManager::LoadModuleChecked<FBackgroundHttpModule>("BackgroundHttp");

	    TSharedPtr<IBackgroundHttpManager> Manager = BackgroundHttpModule.GetBackgroundHttpManager();

	 

	    if (Manager.IsValid())

	    {

	        // 2. Create the Request

	        TSharedRef<IBackgroundHttpRequest> Request = Manager->CreateRequest();

	        Request->SetURL(URL);

	        Request->SetVerb(TEXT("GET"));

	        

	        // 3. Bind Completion Delegate

	        Request->OnProcessRequestComplete().BindUObject(this, &UMyDownloadSubsystem::HandleDownloadComplete);

	 

	        // 4. Bind Progress Delegate (optional)

	        // Note: Progress reports (int64 Current, int64 Total)

	        Request->OnProgressUpdated().BindUObject(this, &UMyDownloadSubsystem::HandleDownloadProgress);

	 

	        // 5. Send the request to the OS

	        Request->ProcessRequest();

	    }

	}

	 

	void UMyDownloadSubsystem::HandleDownloadComplete(FBackgroundHttpRequestPtr Request, bool bWasSuccess)

	{

	    if (bWasSuccess)

	    {

	        UE_LOG(LogTemp, Log, TEXT("Background Download Finished: %s"), *Request->GetURL());

	    }

	}

	```

	 

	### Performance & Debugging

	*   **Log Verbosity:** Use `Log LogBackgroundHttp Verbose` in the console to see the hand-off between Unreal and the native OS download managers.

	*   **Platform Specifics:** On iOS, background downloads are subject to "Discretionary" scheduling by the OS, meaning they may be delayed if the battery is low or the device is on cellular data.

	*   **ChunkDownloader:** For large-scale patching, consider using the **ChunkDownloader** plugin, which is a high-level wrapper that uses `BackgroundHttp` internally to manage manifest-based asset delivery.
Copy code
2. Distinguish Large Downloads from API Calls

Never use BackgroundHttp for standard REST API calls (like logging in or fetching player stats). The standard HTTP module is much faster and lighter for small JSON payloads. Use BackgroundHttp exclusively for large binary assets (e.g., .pak files) where interruption is likely.

3. Verify Disk Space Before Starting

Since background downloads are typically large, always use FPlatformMisc::GetDiskFreeSpace before initializing a request. If the download fails midway due to a full disk, the OS may “eliminate” the task without a clear error message in the engine logs, leading to a confusing user experience.

4. Handle Mobile App Suspension

On iOS and Android, the engine’s main thread is often frozen when backgrounded. BackgroundHttp is thread-safe and interacts with the OS-level download service. When the app resumes, the IBackgroundHttpManager will automatically fire the completion or progress delegates for all work finished while the engine was “sleeping.”

5. Implement Resumable Logic

BackgroundHttp supports resumable downloads natively on most platforms. If a user loses connection or manually closes the app, you can re-create the request with the same URL. The module will check the local temporary directory for a partial file and attempt to resume from the last byte received, rather than starting over.

6. Use Notification Objects for UI

If you need to show a persistent progress bar in the UI that survives level transitions, bind your delegates to a Global Game Instance Subsystem rather than an Actor or Widget. This prevents your callbacks from being “eliminated” by garbage collection if the player moves from the “Launcher” level to the “Main Menu” while the download is still active.

7. Clean Up Temporary Files

The module stores partial downloads in a platform-specific cache folder. If a request is cancelled or fails permanently, ensure you call Manager->DeleteTemporaryFilesForRequest(Request) to prevent orphaned data from bloating the user’s storage.

C++ Implementation Example: Basic Background Download

To start a background request, you access the manager through the module singleton:

C++
	#include "BackgroundHttpModule.h"

	#include "Interfaces/IBackgroundHttpRequest.h"

	#include "Interfaces/IBackgroundHttpManager.h"

	 

	void UMyDownloadSubsystem::StartAssetDownload(FString URL, FString SavePath)

	{

	    // 1. Get the Background HTTP Manager

	    FBackgroundHttpModule& BackgroundHttpModule = FModuleManager::LoadModuleChecked<FBackgroundHttpModule>("BackgroundHttp");

	    TSharedPtr<IBackgroundHttpManager> Manager = BackgroundHttpModule.GetBackgroundHttpManager();

	 

	    if (Manager.IsValid())

	    {

	        // 2. Create the Request

	        TSharedRef<IBackgroundHttpRequest> Request = Manager->CreateRequest();

	        Request->SetURL(URL);

	        Request->SetVerb(TEXT("GET"));

	        

	        // 3. Bind Completion Delegate

	        Request->OnProcessRequestComplete().BindUObject(this, &UMyDownloadSubsystem::HandleDownloadComplete);

	 

	        // 4. Bind Progress Delegate (optional)

	        // Note: Progress reports (int64 Current, int64 Total)

	        Request->OnProgressUpdated().BindUObject(this, &UMyDownloadSubsystem::HandleDownloadProgress);

	 

	        // 5. Send the request to the OS

	        Request->ProcessRequest();

	    }

	}

	 

	void UMyDownloadSubsystem::HandleDownloadComplete(FBackgroundHttpRequestPtr Request, bool bWasSuccess)

	{

	    if (bWasSuccess)

	    {

	        UE_LOG(LogTemp, Log, TEXT("Background Download Finished: %s"), *Request->GetURL());

	    }

	    else

	    {

	        UE_LOG(LogTemp, Error, TEXT("Download failed or was eliminated by OS."));

	    }

	}
Copy code
Performance & Debugging
Log Verbosity: Use Log LogBackgroundHttp Verbose in the console to see the hand-off between Unreal and the native OS download managers.
Platform Specifics: On iOS, background downloads are subject to “Discretionary” scheduling by the OS, meaning they may be delayed if the battery is low or the device is on cellular data.
ChunkDownloader: For large-scale patching, consider using the ChunkDownloader plugin, which is a high-level wrapper that uses BackgroundHttp internally to manage manifest-based asset delivery.