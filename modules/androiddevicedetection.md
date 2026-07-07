---
layout: default
title: AndroidDeviceDetection
---


<h1>AndroidDeviceDetection</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Android/AndroidDeviceDetection/AndroidDeviceDetection.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, DesktopPlatform, Engine, Json, JsonUtilities, PIEPreviewDeviceSpecification, Slate, SlateCore, Zen</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ine responsible for discovering and identifying Android hardware connected to the development machine. It acts as the bridge between the Unreal Editor and the Android Debug Bridge (ADB).

This module is primarily used by the Device Manager and the Project Launcher to populate the list of available target devices. It queries connected hardware for specific metadata—such as CPU architecture (ARM64, x86_64), GPU family (Adreno, Mali), and authorized status—to ensure the engine can correctly package and deploy builds to the intended mobile target.

1. Verify ADB Path in SDK Settings

The module relies entirely on a valid ADB installation. If your devices are not appearing, ensure the path to the Android SDK is correctly set in Project Settings > Platforms > Android SDK. If the path is incorrect, the detection module will fail to initialize, effectively eliminating your ability to deploy to hardware.

2. Handle “Unauthorized” Status

The module detects if a device is connected but hasn’t yet trusted the PC. In the Device Manager, these appear as “Unauthorized.”

Tip: If this occurs, check your phone for the “Allow USB Debugging?” prompt. Select “Always allow” to permit the detection module to pull the device’s unique identifier and hardware specifications.
3. Use for Device Profile Matching

The information gathered by this module (such as SRC_GpuFamily and SRC_AndroidVersion) is what Unreal uses to apply Device Profiles. You can test how the detection module identifies your device by looking at the BaseDeviceProfiles.ini. Use these detected strings to create specific scalability overrides for your hardware.

4. Restarting the Detection Service

If a device is physically plugged in but not visible in Unreal, you can force the module to refresh by restarting the ADB server via the command line:

adb kill-server
adb start-server The AndroidDeviceDetection module will automatically pick up the new server broadcast and repopulate the device list.
5. Monitor via LogAndroidDeviceDetection

For deep troubleshooting of connection issues, you can check the Output Log. Use the filter to look for LogAndroidDeviceDetection. This log will reveal if the module is failing to parse the device’s properties or if there is a version mismatch between the engine’s expected ADB version and the one installed on the system.

6. Connection Mode Matters (PTP vs. MTP)

The module sometimes fails to detect devices set to “Charging Only” or “MTP” (Media Transfer Protocol) mode.

Best Practice: If the device is not detected, switch the USB configuration on the Android device to PTP (Picture Transfer Protocol) or MIDI. Some manufacturers’ driver implementations work more reliably with the detection module when set to these modes.
7. Filter Architecture in Project Launcher

The detection module reports the device’s architecture back to the Project Launcher. To save time and avoid build failures, ensure your “Build UAT” settings match what the module detected (e.g., don’t try to deploy an ARMv7 build to an ARM64-only device detected by the module).

8. Wireless Detection Support

The module also supports devices connected via ADB over Wi-Fi. Once a device is paired via IP address using the console (adb connect [IP]), the AndroidDeviceDetection module treats it as a locally connected device, allowing for wireless “Launch On” functionality and remote debugging within the Editor.