---
layout: default
title: MovieSceneTracks
---

<!-- ai-generation-failed -->

<h1>MovieSceneTracks</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/MovieSceneTracks/MovieSceneTracks.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnimGraphRuntime, AnimationBlueprintLibrary, AnimationCore, AudioMixer, BlueprintGraph, Constraints, Core, CoreUObject, DataLayerEditor, EditorFramework, Engine, MovieScene, PropertyPath, SlateCore, TimeManagement</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ontaining the standard implementations for the most common types of animation and data tracks used in Level Sequences.

What it is and What it’s used for

Located in Engine/Source/Runtime/MovieSceneTracks, this module provides the logic, data structures, and evaluation templates for the “default” tracks found in the Sequencer UI. While the MovieScene module handles the high-level timing and evaluation logic, MovieSceneTracks contains the specific “knowledge” of how to animate properties like transforms, visibility, and audio.

Primary uses include:

Property Animation: Implementing tracks for float, bool, color, and string properties on Actors.
Transform Logic: Handling 3D space movement via UMovieScene3DTransformTrack.
Component Control: Managing specialized tracks for Camera Cut, Audio, Particles (Niagara), and Skeletal Mesh animations.
Standardized Sections: Defining the behavior of “Sections” (the colored blocks in the timeline) for various data types.
Practical Usage Tips and Best Practices
1. Use the “Restore State” Property Wisely

By default, many tracks in this module are set to Restore State when the sequence finishes. If you want an object to stay in its final animated position (e.g., a door remaining open), set the track’s “When Finished” property to Keep State. This is the primary method for the elimination of “snapping” artifacts where objects jump back to their original positions.

2. Leverage Hierarchical Bias for Overlaps

When multiple sections on a track overlap, the Hierarchical Bias setting determines which one takes precedence. Higher values win. Proper use of bias ensures the elimination of flickering or fighting between competing animation sections on the same Actor.

3. Optimize with Channel Masking

For Transform tracks, you can disable individual channels (like Scale X/Y/Z) if they aren’t being animated. This reduces the number of curves the engine has to evaluate, leading to the elimination of unnecessary CPU overhead during cinematic playback, especially in scenes with hundreds of animated props.

4. Batch Process with Python Scripting

If you need to add the same track type to 50 different Actors, use the Python API (which interfaces with this module). Automated track creation leads to the elimination of repetitive manual work and ensures that all tracks share identical settings like “Pre-roll” or “Post-roll.”

5. Implement Pre-roll for Physics and VFX

For tracks controlling particles or physics-enabled objects, use the Pre-roll feature. This evaluates the track logic several frames before the “Start” point, allowing simulations to settle. This results in the elimination of “popping” where particles or cloth suddenly burst into motion on the first frame of a cut.

6. Utilize “Weight” for Blending

Many tracks in this module support a Weight channel. Use this to blend between different animation sections (like two different skeletal animations or two different light intensities). Smooth weighting is a best practice for the elimination of harsh, instant transitions in your cinematics.

7. Monitor Evaluation Performance

Complex sequences with thousands of keyframes can impact frame rate. Use the stat sequencer console command to see how much time the tracks are taking to evaluate. Identifying and simplifying heavy tracks leads to the elimination of performance hitches in real-time cutscenes.

8. Strategic Elimination of Unused Keyframes

Over-keying (having a keyframe on every single frame) can bloat the asset size and slow down evaluation. Use the Key Reducer tool within Sequencer to perform the elimination of redundant keyframes that don’t contribute to the final curve shape, keeping the track data lean and efficient.