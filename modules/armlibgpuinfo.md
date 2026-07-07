---
layout: default
title: ArmlibGPUInfo
---

<!-- ai-generation-failed -->

<h1>ArmlibGPUInfo</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/ARM/ArmlibGPUInfo/ArmlibGPUInfo.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ngine 5 designed to interface directly with the ARM Mali GPU hardware library (libGLES_mali). It is primarily used on Android devices to retrieve granular hardware metadata, driver details, and performance information that are not exposed through the standard Android NDK or generic Vulkan/OpenGL APIs.

This module is a key component for hardware-aware scaling on Mali devices. It allows the engine to populate “Source Strings” (like SRC_GpuFamily) used by the Android Device Profile Matching Rules and the configrules.txt system to apply specific performance tiers or workarounds for Mali-based chipsets.

1. Enable Module for Android-Only Builds

Since this module interacts with Android-specific binary libraries, it must be gated within your Build.cs. Including it for non-mobile platforms will result in compilation errors as the underlying ARM libraries won’t exist.

C#
	if (Target.Platform == UnrealTargetPlatform.Android)

	{

	    // Required to access ARM-specific GPU info and counters

	    PublicDependencyModuleNames.Add("armlibgpuinfo");

	}

	```

	 

	### 2. Querying Granular GPU Hardware Info

	You can use the module to identify the exact architecture of a Mali GPU (e.g., Bifrost, Valhall). This is more precise than generic GPU family strings and can be used to enable specialized shader paths in C++.

	 

	```cpp

	#include "ArmLibGpuInfo.h"

	 

	void GetMaliDetails()

	{

	#if PLATFORM_ANDROID

	    // The module provides static access to detected hardware info

	    FString GpuArch = FArmLibGpuInfo::GetGpuArchitecture();

	    int32 CoreCount = FArmLibGpuInfo::GetNumCores();

	    

	    UE_LOG(LogAndroid, Log, TEXT("Mali GPU Architecture: %s, Cores: %d"), *GpuArch, CoreCount);

	#endif

	}

	```

	 

	### 3. Use for Dynamic Thermal Throttling

	Unlike standard APIs that only provide general device temperature, `armlibgpuinfo` can often access more specific GPU thermal zones. Use this to proactively lower your resolution scale or disable expensive post-processing (like high-quality Bloom or Depth of Field) before the OS forces a hard throttle that drops your frame rate significantly.

	 

	### 4. Correcting "Unknown" Mali Devices

	If you encounter a new Mali device that returns an "Unknown" GPU string in the logs, it usually means the generic RHI identification failed. You can use the `armlibgpuinfo` module's raw output to create a custom entry in your `BaseDeviceProfiles.ini` using the `SRC_GpuFamily` source type, ensuring the device receives the correct scalability settings.

	 

	### 5. Accessing Driver-Specific Workarounds

	Mali drivers frequently have specific bugs related to certain OpenGL/Vulkan extensions. The `armlibgpuinfo` module provides detailed driver version strings (e.g., `r26p0`). Use this in your C++ initialization logic to disable problematic features (like specific blending modes or compute shader instructions) only on the affected driver versions, preventing the elimination of visual artifacts without penalizing newer, fixed drivers.

	 

	### 6. Verification via LogAndroid

	To see if the module is functioning correctly on your test device, search your log for `LogAndroid` or `LogRHI`. You should see entries populated by this module such as:

	- `Mali GPU Family: Bifrost`

	- `Mali Driver Version: rXXpX`

	If these are missing or show generic "Generic" values, ensure your Android NDK is correctly configured to include the ARM-specific sysroot.

	 

	### 7. Performance Profiling with HWCPipe

	The `armlibgpuinfo` module is often used as a dependency for **HWCPipe**, a tool used to read ARM hardware counters (Cycle counts, Texture pipe utilization, etc.). If you are building custom performance overlays or in-house profiling tools for mobile, this module provides the necessary hooks to pull these hardware-level counters without using a debugger.

	 

	### 8. Handling Multi-Core Scalability

	Mali GPUs scale their performance by increasing the number of "cores" (e.g., a Mali-G78 MP14 has 14 cores). Use `armlibgpuinfo` to query the core count at runtime. This allows you to set your `r.MobileContentScaleFactor` dynamically—high-core-count devices can run at native resolution, while low-core variants of the same chip can be downsampled for better stability.
Copy code
2. Identify Granular Hardware Generations

You can use the module to identify the exact architecture of a Mali GPU (e.g., Bifrost, Valhall). This is more precise than generic GPU family strings and can be used to enable specialized shader paths or rendering features in C++.

3. Use for Precision Device Profiling

The information gathered by this module is used to feed the Device Profile system. By identifying whether a device is a high-core-count variant (e.g., Mali-G78 MP14) versus a low-core variant, you can dynamically set your r.MobileContentScaleFactor to ensure high resolution on capable devices while downsampling on lower-end ones to maintain frame rate.

4. Driver-Specific Bug Workarounds

Mali drivers frequently have specific behaviors related to certain OpenGL/Vulkan extensions. The armlibgpuinfo module provides detailed driver version strings (e.g., r26p0). Use this in your project logic to disable problematic features only on affected driver versions, preventing the elimination of visual stability without penalizing users on newer, fixed drivers.

5. Verify Hardware via Logs

To see if the module is functioning correctly on your test device, search your log for LogAndroid or LogRHI. You should see entries populated by this module, such as:

Mali GPU Family: Valhall
Mali Driver Version: rXXpX If these are missing or show generic values, ensure your Android NDK is correctly configured and the device is running a compatible Mali driver.
6. Correcting “Unknown” Mali Devices

If you encounter a new Mali device that returns an “Unknown” GPU string in the logs, you can use the module’s raw output to create a custom entry in your BaseDeviceProfiles.ini. Use the SRC_GpuFamily source type with a regex match for the specific Mali series identified by the module to ensure it receives the correct scalability settings.

7. Performance Monitoring with HWCPipe

The armlibgpuinfo module is often a prerequisite for using HWCPipe, an ARM tool used to read hardware counters (Cycle counts, Texture pipe utilization, etc.). If you are building custom performance overlays for mobile, this module provides the hooks to pull these hardware-level metrics without requiring an external debugger.

8. Handling Multi-Core Scalability

Mali GPUs scale their performance by increasing the number of “cores.” Use the data provided by this module to query core counts. This allows you to scale GPU-intensive effects like Mobile Screen Space Reflections or Bloom Quality based on the actual compute capacity of the Mali chip rather than just the Android OS version.