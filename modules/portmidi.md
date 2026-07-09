---
layout: default
title: portmidi
---

<!-- ai-generation-failed -->

<h1>portmidi</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/portmidi/portmidi.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

erface) I/O backend for Unreal Engine. It serves as the underlying library for the MIDI Device Support plugin, enabling the engine to communicate with external hardware such as keyboards, faders, and pads.

While MIDI is traditionally an audio protocol, this module treats it as a generic data stream. This allows developers to use MIDI hardware not just for music, but as a tactical control interface for virtual production, lighting (via DMX integration), or complex debug tools during gameplay development.

Practical Usage Tips & Best Practices
1. Activate the MIDI Device Support Plugin

The PortMidi module is a dependency of the MIDI Device Support plugin. It is not active in a default project.

Best Practice: Go to Edit > Plugins and enable MIDI Device Support. This ensures the elimination of “Unrecognized type” errors when you attempt to use MIDI Controller classes in your Blueprints or C++.
2. Prevent Unexpected Garbage Collection

A common pitfall is creating a MIDI Input/Output Controller and not storing it in a persistent variable.

Tip: Once you call Create MIDI Input Device Controller, immediately Promote to Variable in your Blueprint (e.g., in your GameInstance or a dedicated Manager Actor). Caching the reference leads to the elimination of sudden connection drops caused by the engine’s Garbage Collector cleaning up the “unused” object.
3. Manage Device IDs Dynamically

Device IDs are not permanent; they can change if you plug in a new device or restart your computer.

Best Practice: Never hardcode a Device ID (like “1”). Instead, use the Find MIDI Devices node at startup to look for a device by its Name string. This results in the elimination of broken connections when your hardware setup is moved to a different USB port.
4. Account for Game Thread Latency

MIDI messages processed through Blueprints are bound to the Game Thread, which typically runs at the frame rate (e.g., 60 FPS).

Tip: If you require ultra-low latency for musical performances, be aware that high GPU load can delay MIDI processing. Keeping your frame rate stable facilitates the elimination of “jitter” or audible lag when using MIDI to trigger sound effects or MetaSounds.
5. Use Sound Utilities for Data Conversion

Raw MIDI data is sent as integers (0–127), which is rarely useful for direct gameplay parameters like speed or light intensity.

Best Practice: Use the functions in the Sound Utilities plugin to convert MIDI Note numbers to Frequencies (Hz) or Velocity to Gain. Using these built-in math nodes leads to the elimination of manual calculation errors when mapping knobs to gameplay values.
6. Utilize the “Note On/Off” Paradigm

MIDI doesn’t just send a “hit” event; it sends a start and an end signal.

Tip: Always bind events to both On MIDI Note On and On MIDI Note Off. This ensures the elimination of “stuck” logic, such as a light staying on forever because your code only listened for the initial button press and not the release.
7. Leverage for Virtual Production

MIDI controllers with physical sliders (faders) are superior to a mouse for controlling smooth movements.

Best Practice: Map a MIDI slider to a Cine Camera Actor’s Focal Length or Aperture. This allows a physical operator to pull focus manually, resulting in the elimination of the “robotic” feel of programmed camera movements in cinematics.
8. Debug with “Print String” on Raw Data

If a device isn’t responding as expected, it may be sending Control Change (CC) messages instead of Notes.

Tip: Use the Bind Event to On MIDI Event (Raw) and print the status byte and data bytes to the screen. Visualizing the raw stream facilitates the elimination of guesswork when configuring non-standard MIDI hardware or mobile MIDI apps.