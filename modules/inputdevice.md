---
layout: default
title: InputDevice
---

<!-- ai-generation-failed -->

<h1>InputDevice</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/InputDevice/InputDevice.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

tegration in Unreal Engine. It defines the IInputDevice interface, allowing developers to create custom drivers for non-standard hardware—such as specialized VR controllers, MIDI devices, flight simulators, or biometric sensors—and pipe their data directly into Unreal’s unified input system (Slate and Enhanced Input).

By implementing this module, you enable the engine to treat third-party hardware as first-class citizens, facilitating the elimination of “poll-based” input hacks in your actors in favor of a clean, event-driven architecture.

Practical Usage Tips and Best Practices
1. Implement SendControllerEvents for Main Logic

Do not process gameplay-critical input inside Tick(). Instead, use SendControllerEvents. This function is called by the engine at the appropriate time in the frame to ensure that input events are dispatched before the frame’s physics and logic updates. This practice assists in the elimination of input lag by aligning your device’s data with the engine’s processing window.

2. Cache the IInputMessageHandler

When your device is initialized via SetMessageHandler, store a reference to the IInputMessageHandler. You must use this handler to call functions like OnControllerButtonPressed or OnControllerAnalog. Using the centralized handler is vital for the elimination of redundant input routing logic, as it automatically sends data to both Slate (UI) and the Player Input system.

3. Handle Connection States Gracefully

Always override SetChannelValue and check the EInputDeviceConnectionState. If a device is disconnected, ensure you report a “0” or “Neutral” state for all axes. This leads to the elimination of “ghost inputs” where a character keeps running in a circle because the controller was unplugged while the stick was tilted.

4. Use FForceFeedbackValues for Haptics

If your hardware supports vibration or haptics, implement SetForceFeedbackChannelValues. This allows your custom device to respond to standard Unreal “Play Force Feedback” nodes in Blueprints. Supporting the engine’s native haptic API facilitates the elimination of custom, hardware-specific C++ calls throughout your game code.

5. Thread Safety with Asynchronous Hardware

Many third-party SDKs run their own polling threads. Ensure that you buffer this asynchronous data into a thread-safe queue (like TQueue<FMyHardwareEvent, EQueueMode::Spsc>) and then drain that queue into the engine during the SendControllerEvents call on the Game Thread. This is critical for the elimination of race conditions and memory corruption crashes.

6. Register via IInputDeviceModule

To make the engine aware of your device, you must implement a class inheriting from IInputDeviceModule and return your device instance in CreateInputDevice. Adding your module to the InputDevice category in the .uplugin file ensures the elimination of manual “StartupModule” instantiation, as the engine will automatically load and initialize your driver.

7. Leverage Device Properties (LEDs and Triggers)

UE 5.x introduces UInputDeviceProperty for features like Adaptive Triggers or Controller Lightbars. If your hardware has unique features (like a RGB strip), override SetDeviceProperty. Implementing this system assists in the elimination of non-standard “Device Manager” actors in your levels, centralizing hardware decoration logic within the input driver.

8. Use “showdebug DeviceProperty” for Debugging

When testing custom haptics or trigger effects, use the console command showdebug DeviceProperty. This overlay shows exactly which properties are currently active on which InputDeviceId. Utilizing built-in debug views leads to the elimination of “black box” debugging where you can’t tell if the engine is actually sending a command to your hardware.