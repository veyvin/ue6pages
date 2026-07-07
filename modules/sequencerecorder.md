---
layout: default
title: SequenceRecorder
---

<!-- ai-generation-failed -->

<h1>SequenceRecorder</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/SequenceRecorder/SequenceRecorder.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetRegistry, CinematicCamera, Core, CoreUObject, EditorFramework, EditorStyle, EditorWidgets, Engine, InputCore, Kismet, LevelEditor, LevelSequence, LiveLinkInterface, MovieScene, MovieSceneTracks, NetworkReplayStreaming, Projects, PropertyEditor, SceneOutliner, SequenceRuntimeRecorder, Sequencer, SerializedRecorderInterface, Slate, SlateCore, TimeManagement, UnrealEd, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ed to capture real-time gameplay, actor movements, and physics simulations into a Level Sequence.

Description and Purpose

This module allows developers to “record” the state of the world while playing in the editor (PIE) or simulating. It tracks the transforms, animations, and property changes of selected actors and saves them as keyframe data. Its primary purpose is to generate cinematic assets from live performances or complex physics interactions that would be difficult to keyframe manually. While largely superseded by the newer Take Recorder plugin for professional virtual production, the SequenceRecorder module remains in the engine to support automated recording workflows and legacy projects. It helps developers eliminate the time-consuming process of manually animating actors that already have functional gameplay logic.

Practical Usage Tips and Best Practices
Prefer Take Recorder for Modern Workflows
In UE 5.6, the Take Recorder (built on top of the newer TakeRecorder module) is the successor to this module. Use Take Recorder for better performance and UI, but keep the Sequence Recorder module enabled if you have custom C++ automation scripts that rely on the ISequenceRecorder interface.
Use “Record to Possessable” to Edit Existing Actors
By default, recording creates a “Spawnable” actor in the sequence. If you want the animation to apply directly to the actor already in your level, change the setting to “Possessable.” This helps you eliminate duplicate actors when you move from the recording phase to the polishing phase.
Reduce Keyframe Density with Tolerance
The module can generate a massive amount of data (one key per frame). Adjust the Key Reduction Tolerance settings in the Sequence Recorder window. This will eliminate redundant keyframes on static or slow-moving tracks, making the resulting sequence much easier to edit and less memory-intensive.
Synchronize via Timecode
If you are recording multiple actors or external inputs, ensure you have a Timecode Provider active. Using a consistent clock helps the module eliminate “drift” between different recorded tracks, ensuring that a character’s footfalls match the audio or environmental effects recorded simultaneously.
Filter Recorded Properties
You do not always need to record every property of an actor. Use the Classes and Properties to Record filters to specify exactly which variables (e.g., RelativeLocation, bIsFiring) should be tracked. This is a best practice to eliminate “data noise” and keep your sequence files small.
Record Skeletal Mesh Animation to Assets
When recording a character, the module can save the performance as a new Anim Sequence asset. Ensure the “Record to Animation” checkbox is marked. This allows you to eliminate the dependency on the Level Sequence if you only need the raw animation data for use in an Animation Blueprint later.
Warm Up Before Recording
Physics and particle simulations often need a few seconds to settle. Start your recording a few seconds early and use the “Start Delay” feature. This helps you eliminate “jitter” or “explosive” physics behavior that can occur on the very first frame of a simulation.
Avoid Recording During Low Frame Rates
Sequence Recorder is sensitive to the editor’s performance. If the frame rate drops, the recorded data may become stuttered. To eliminate this, use the “Fixed Frame Rate” setting in the Project Settings during the recording session to ensure every frame of motion is captured accurately.