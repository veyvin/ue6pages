---
layout: default
title: HeadMountedDisplay
---

<!-- ai-generation-failed -->

<h1>HeadMountedDisplay</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/HeadMountedDisplay/HeadMountedDisplay.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, EngineSettings, InputCore, RHI, RenderCore, Renderer</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ndard), the HeadMountedDisplay module remains essential for querying tracking data, managing stereo rendering, and handling late-frame reprojection in a platform-agnostic way.

Practical Usage Tips and Best Practices
Add Dependency to Build.cs
To use HMD functions in C++, add the module to your project’s Build.cs. This “eliminates” linker errors when accessing XR system interfaces.
C#
	    PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "HeadMountedDisplay" });

	    ```

	 

	*   **Access via GEngine->XRSystem**  

	    Never try to cast directly to a specific hardware class. Instead, use the generic `GEngine->XRSystem`. This "eliminates" platform-specific code, ensuring your logic works whether the user is on a Valve Index via SteamVR or a Meta Quest via OpenXR.

	    ```cpp

	    #include "IXRTrackingSystem.h"

	    // ...

	    if (GEngine && GEngine->XRSystem.IsValid())

	    {

	        IHeadMountedDisplay* HMD = GEngine->XRSystem->GetHMDDevice();

	        // Use HMD device

	    }

	    ```

	 

	*   **Check Connection Status Before Logic**  

	    Before executing VR-specific code, verify that an HMD is actually connected and active using `HMD->IsHMDConnected()`. This "eliminates" unnecessary processing and potential crashes in non-VR builds or when the headset is unplugged.

	 

	*   **Handle WorldToMeters Scaling**  

	    Unreal units are in centimeters, but XR runtimes often operate in meters. Use `HMD->GetWorldToMetersScale()` when calculating offsets or manual tracking logic. This "eliminates" scale discrepancies that can cause motion sickness or incorrect depth perception.

	 

	*   **Prefer OpenXR for New Projects**  

	    Since UE 5.1, legacy vendor-specific plugins (like the old OculusVR plugin) are deprecated. Always "eliminate" dependencies on legacy plugins in favor of the **OpenXR** plugin, which utilizes the `HeadMountedDisplay` module interfaces for maximum cross-platform compatibility.

	 

	*   **Safely Get Orientation and Position**  

	    To retrieve the headset's current pose, use the standard `GetOrientationAndPosition` method. This "eliminates" the need for manual matrix math, providing you with a ready-to-use `FQuat` and `FVector`.

	    ```cpp

	    FQuat DeviceRotation;

	    FVector DevicePosition;

	    if (GEngine->XRSystem->GetCurrentPose(IXRTrackingSystem::HMDDeviceId, DeviceRotation, DevicePosition))

	    {

	        // Handle pose

	    }

	    ```

	 

	*   **Use Enhanced Input for XR**  

	    While the HMD module handles tracking, use the **Enhanced Input** system for buttons and triggers. Map your actions to the `XR` specific input keys. This "eliminates" the complexity of remapping controllers for different HMD ecosystems (e.g., Vive Wands vs. Touch Controllers).

	 

	*   **Late-Update for Performance**  

	    If you are manually attaching objects to the HMD in C++, ensure you utilize the "Late Update" feature provided by the module. This "eliminates" the latency (lag) between the user's head movement and the rendered object, which is the primary cause of VR-induced nausea.
Copy code
Access via GEngine->XRSystem
Never try to cast directly to a specific hardware class. Instead, use the generic GEngine->XRSystem. This “eliminates” platform-specific code, ensuring your logic works whether the user is on a Valve Index via SteamVR or a Meta Quest via OpenXR.
C#
	    PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "HeadMountedDisplay" });

	    ```

	 

	*   **Access via GEngine->XRSystem**  

	    Never try to cast directly to a specific hardware class. Instead, use the generic `GEngine->XRSystem`. This "eliminates" platform-specific code, ensuring your logic works whether the user is on a Valve Index via SteamVR or a Meta Quest via OpenXR.

	    ```cpp

	    #include "IXRTrackingSystem.h"

	    // ...

	    if (GEngine && GEngine->XRSystem.IsValid())

	    {

	        IHeadMountedDisplay* HMD = GEngine->XRSystem->GetHMDDevice();

	        // Use HMD device

	    }

	    ```

	 

	*   **Check Connection Status Before Logic**  

	    Before executing VR-specific code, verify that an HMD is actually connected and active using `HMD->IsHMDConnected()`. This "eliminates" unnecessary processing and potential crashes in non-VR builds or when the headset is unplugged.

	 

	*   **Handle WorldToMeters Scaling**  

	    Unreal units are in centimeters, but XR runtimes often operate in meters. Use `HMD->GetWorldToMetersScale()` when calculating offsets or manual tracking logic. This "eliminates" scale discrepancies that can cause motion sickness or incorrect depth perception.

	 

	*   **Prefer OpenXR for New Projects**  

	    Since UE 5.1, legacy vendor-specific plugins (like the old OculusVR plugin) are deprecated. Always "eliminate" dependencies on legacy plugins in favor of the **OpenXR** plugin, which utilizes the `HeadMountedDisplay` module interfaces for maximum cross-platform compatibility.

	 

	*   **Safely Get Orientation and Position**  

	    To retrieve the headset's current pose, use the standard `GetOrientationAndPosition` method. This "eliminates" the need for manual matrix math, providing you with a ready-to-use `FQuat` and `FVector`.

	    ```cpp

	    FQuat DeviceRotation;

	    FVector DevicePosition;

	    if (GEngine->XRSystem->GetCurrentPose(IXRTrackingSystem::HMDDeviceId, DeviceRotation, DevicePosition))

	    {

	        // Handle pose

	    }

	    ```

	 

	*   **Use Enhanced Input for XR**  

	    While the HMD module handles tracking, use the **Enhanced Input** system for buttons and triggers. Map your actions to the `XR` specific input keys. This "eliminates" the complexity of remapping controllers for different HMD ecosystems (e.g., Vive Wands vs. Touch Controllers).

	 

	*   **Late-Update for Performance**  

	    If you are manually attaching objects to the HMD in C++, ensure you utilize the "Late Update" feature provided by the module. This "eliminates" the latency (lag) between the user's head movement and the rendered object, which is the primary cause of VR-induced nausea.
Copy code
Check Connection Status Before Logic
Before executing VR-specific code, verify that an HMD is actually connected and active using HMD->IsHMDConnected(). This “eliminates” unnecessary processing and potential crashes in non-VR builds or when the headset is unplugged.
Handle WorldToMeters Scaling
Unreal units are in centimeters, but XR runtimes often operate in meters. Use HMD->GetWorldToMetersScale() when calculating offsets or manual tracking logic. This “eliminates” scale discrepancies that can cause motion sickness or incorrect depth perception.
Prefer OpenXR for New Projects
Since UE 5.1, legacy vendor-specific plugins (like the old OculusVR plugin) are deprecated. Always “eliminate” dependencies on legacy plugins in favor of the OpenXR plugin, which utilizes the HeadMountedDisplay module interfaces for maximum cross-platform compatibility.
Safely Get Orientation and Position
To retrieve the headset’s current pose, use the standard GetOrientationAndPosition method. This “eliminates” the need for manual matrix math, providing you with a ready-to-use FQuat and FVector.
C#
	    PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "HeadMountedDisplay" });

	    ```

	 

	*   **Access via GEngine->XRSystem**  

	    Never try to cast directly to a specific hardware class. Instead, use the generic `GEngine->XRSystem`. This "eliminates" platform-specific code, ensuring your logic works whether the user is on a Valve Index via SteamVR or a Meta Quest via OpenXR.

	    ```cpp

	    #include "IXRTrackingSystem.h"

	    // ...

	    if (GEngine && GEngine->XRSystem.IsValid())

	    {

	        IHeadMountedDisplay* HMD = GEngine->XRSystem->GetHMDDevice();

	        // Use HMD device

	    }

	    ```

	 

	*   **Check Connection Status Before Logic**  

	    Before executing VR-specific code, verify that an HMD is actually connected and active using `HMD->IsHMDConnected()`. This "eliminates" unnecessary processing and potential crashes in non-VR builds or when the headset is unplugged.

	 

	*   **Handle WorldToMeters Scaling**  

	    Unreal units are in centimeters, but XR runtimes often operate in meters. Use `HMD->GetWorldToMetersScale()` when calculating offsets or manual tracking logic. This "eliminates" scale discrepancies that can cause motion sickness or incorrect depth perception.

	 

	*   **Prefer OpenXR for New Projects**  

	    Since UE 5.1, legacy vendor-specific plugins (like the old OculusVR plugin) are deprecated. Always "eliminate" dependencies on legacy plugins in favor of the **OpenXR** plugin, which utilizes the `HeadMountedDisplay` module interfaces for maximum cross-platform compatibility.

	 

	*   **Safely Get Orientation and Position**  

	    To retrieve the headset's current pose, use the standard `GetOrientationAndPosition` method. This "eliminates" the need for manual matrix math, providing you with a ready-to-use `FQuat` and `FVector`.

	    ```cpp

	    FQuat DeviceRotation;

	    FVector DevicePosition;

	    if (GEngine->XRSystem->GetCurrentPose(IXRTrackingSystem::HMDDeviceId, DeviceRotation, DevicePosition))

	    {

	        // Handle pose

	    }

	    ```

	 

	*   **Use Enhanced Input for XR**  

	    While the HMD module handles tracking, use the **Enhanced Input** system for buttons and triggers. Map your actions to the `XR` specific input keys. This "eliminates" the complexity of remapping controllers for different HMD ecosystems (e.g., Vive Wands vs. Touch Controllers).

	 

	*   **Late-Update for Performance**  

	    If you are manually attaching objects to the HMD in C++, ensure you utilize the "Late Update" feature provided by the module. This "eliminates" the latency (lag) between the user's head movement and the rendered object, which is the primary cause of VR-induced nausea.
Copy code
Use Enhanced Input for XR
While the HMD module handles tracking, use the Enhanced Input system for buttons and triggers. Map your actions to the XR specific input keys. This “eliminates” the complexity of remapping controllers for different HMD ecosystems (e.g., Vive Wands vs. Touch Controllers).
Late-Update for Performance
If you are manually attaching objects to the HMD in C++, ensure you utilize the “Late Update” feature provided by the module. This “eliminates” the latency (lag) between the user’s head movement and the rendered object, which is the primary cause of VR-induced nausea.