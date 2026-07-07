---
layout: default
title: AudioAnalyzer
---

<!-- ai-generation-failed -->

<h1>AudioAnalyzer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AudioAnalyzer/AudioAnalyzer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioMixer, Core, CoreUObject, Engine, SignalProcessing</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ne 5 that enables the extraction of meaningful data from audio signals. It serves as the base for both Non-Real-Time (NRT) analysis—which pre-calculates data from sound waves—and Real-Time analysis, which processes live audio streams.

This module is primarily used to drive audio-reactive visuals (VFX), gameplay events (rhythm games), and UI visualizations. It provides the core interfaces and classes that specific plugins, like Audio Synesthesia, build upon to detect loudness, constant Q, and onsets.

1. Distinguish Between NRT and Real-Time

Choose the right sub-system based on your needs.

NRT (Non-Real-Time): Use for offline analysis where timing must be 100% accurate (e.g., a rhythm game where notes must line up with a song). This generates an asset that stores analysis data.
Real-Time: Use for reactive environments where audio changes dynamically (e.g., a visualization that reacts to a player’s microphone or environmental sounds).
2. Leverage Audio Synesthesia for High-Level Tasks

The AudioAnalyzer module is a low-level framework. For practical development, always use the Audio Synesthesia plugin (which inherits from this module). It provides ready-to-use components like LoudnessNRT, OnsetNRT, and ConstantQNRT that handle the complex math of frequency transforms and perceptual weighting.

3. Minimize CPU Impact of Real-Time Analysis

Real-time analysis involves heavy Fast Fourier Transform (FFT) calculations.

Best Practice: Limit the number of active real-time analyzers. If multiple actors need to react to the same sound, have one “Master Analyzer” broadcast the data to others via a Delegate or Blueprint Interface to avoid redundant calculations.
4. Optimize NRT Settings for Memory

NRT assets can become large if settings are too granular.

Tip: Tune the Analysis Period. A period of 0.01s (100Hz) is usually sufficient for rhythm games. Decreasing this further increases accuracy but can significantly bloat the asset size and memory footprint.
5. Use Submixes for Targeted Analysis

You don’t have to analyze the entire master output. You can send specific sounds (e.g., just the “Music” Sound Class) to a dedicated Sound Submix. By pointing your analyzer at a specific submix, you can isolate the frequency data of the music without the “noise” of footsteps or gunshots interfering with your visuals.

6. Synchronize with Quartz for Sample Accuracy

When using analysis data to trigger gameplay events, use the Quartz system alongside the analyzer. While the analyzer provides the “what” (the frequency/loudness), Quartz provides the “when” (sample-accurate timing). This combination is essential to ensure that the elimination of a target or a visual pulse happens exactly on the beat.

7. Handle Background Threading

Analysis is computationally expensive and is typically performed on a background thread. When pulling data from an AudioAnalyzer in C++, ensure you are not blocking the Game Thread. Most built-in Unreal analyzers handle this automatically, but if you are extending the base UAudioAnalyzer class, you must manage thread safety for your data buffers.

8. Use Audio Insights for Debugging

Unreal Engine’s Audio Insights tool (found in the Developer Tools menu) is the best way to visualize what the analyzer sees. It provides real-time oscilloscopes, spectrograms, and spectrum analyzers. Use this to verify that your frequency bands and noise floors are set correctly before committing to your gameplay logic.