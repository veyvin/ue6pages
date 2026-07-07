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

-platform C API for real-time MIDI input and output within Unreal Engine.

Description and Purpose

This module serves as the foundational back-end for the MIDI Device Support plugin. While Unreal Engine handles the high-level Blueprint nodes and C++ classes for MIDI, PortMidi handles the low-level communication with the operating system’s MIDI drivers (such as Windows MM, macOS CoreMIDI, or Linux ALSA). Its primary purpose is to provide a unified way to discover connected MIDI hardware—like keyboards, faders, and pads—and process incoming or outgoing MIDI messages. By using this module, developers can eliminate the complexity of writing platform-specific MIDI code, allowing for interactive music systems, VJ setups, or MIDI-driven Virtual Production tools.

Practical Usage Tips and Best Practices
Always Cache the MIDI Controller Variable
When creating a MIDI Input or Output Controller in Blueprints or C++, you must store the reference in a variable. If you do not, the engine’s Garbage Collection will eliminate the object, causing your MIDI connection to drop unexpectedly even if the hardware is still plugged in.
Use the Sound Utilities Plugin for Conversions
MIDI data arrives as raw bytes (0–127). To make this data useful, combine this module with the Sound Utilities plugin. This allows you to easily convert MIDI note numbers to frequencies (Hz) or velocities to decibels, helping you eliminate manual math errors in your logic.
Manage Game Thread Latency
By default, MIDI events are processed on the Game Thread, which is subject to the project’s frame rate. To eliminate noticeable “input lag” in musical performances, keep your frame rate high and stable, or use the Quartz system to schedule audio events accurately regardless of frame fluctuations.
Filter MIDI Messages Early
MIDI devices often spam “Active Sensing” or “Clock” messages that can clutter your logs and slow down processing. Use a switch or filter node immediately after the “On MIDI Event” to eliminate any status bytes that your game logic doesn’t specifically require (like Note On/Off or Control Change).
Identify Devices by Name, Not ID
Device IDs can change if you plug hardware into different USB ports. Use the “Get MIDI Input Device ID by Name” function to find your hardware. This is a best practice to eliminate broken connections when moving a project between different computers or hardware configurations.
Bridge MIDI to MetaSounds
In UE 5.6, you can pass MIDI data directly into MetaSounds via input parameters. This is the most efficient way to drive real-time synthesis. Use the MIDI module to capture a knob turn and map it to a MetaSound “Filter Cutoff” to eliminate the “stepping” sound often heard with low-resolution data.
Monitor Connection Status in Virtual Production
If using MIDI for camera cranes or lighting rigs, use the “On Device Connection Changed” delegates. Implementing a “Reconnect” routine is the best way to eliminate production downtime if a cable is accidentally unplugged during a live take.
Check the Log for PortMidi Initialization
If your MIDI device isn’t showing up, check the Output Log for LogMIDIDevice. If PortMidi fails to initialize a specific port, the log will provide a specific error code from the driver. Reviewing these logs is the fastest way to eliminate hardware compatibility issues before they impact development.