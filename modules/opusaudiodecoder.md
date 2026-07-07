---
layout: default
title: OpusAudioDecoder
---

<!-- ai-generation-failed -->

<h1>OpusAudioDecoder</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/OpusAudioDecoder/Module/OpusAudioDecoder.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

integration and decoding logic for the Opus codec within the Unreal Audio Engine.

Description and Purpose

Opus is a highly versatile, open-source audio format designed for low-latency streaming and high-quality speech and music. The OpusAudioDecoder module is primarily utilized for VoIP (Voice over IP), Pixel Streaming, and high-efficiency audio assets where minimizing bandwidth and latency is critical. Its primary purpose is to decompress Opus data streams into a raw PCM format that the Unreal Audio Mixer can process. By leveraging this module, developers can eliminate the high bandwidth costs associated with uncompressed voice data while maintaining superior audio clarity compared to older codecs like Speex or ADPCM.

Practical Usage Tips and Best Practices
Prioritize for VoIP Systems
Opus is the engine’s default for voice communication. Use the OpusAudioDecoder logic to handle incoming voice packets from other players. Because it supports variable bitrates, it can dynamically adapt to network conditions, helping you eliminate robotic-sounding voice artifacts or “crackling” during heavy network congestion.
Leverage for Pixel Streaming Audio
In Pixel Streaming applications, the audio is encoded in Opus to ensure it reaches the web browser with minimal delay. If your stream has audio lag, check the WebRTC settings related to Opus. Optimizing the packet size is a best practice to eliminate desync between the video and the audio in the browser.
Optimize for Mobile Data
If your game targets mobile users on cellular networks, use Opus for streaming background music or dialogue. Its high compression ratio allows you to deliver high-fidelity audio at low bitrates (e.g., 32-64 kbps), which helps you eliminate long buffering times and excessive data usage for your players.
Utilize for Long Ambient Tracks
For long, non-looping ambient recordings or voice-overs, consider using Opus. While Ogg Vorbis is common for general sound effects, Opus is often more efficient for spoken word, helping you eliminate bloat in your packaged build size without sacrificing the character’s performance quality.
Manage Decoder Concurrency
Decoding multiple Opus streams simultaneously can increase CPU usage. Set sensible Concurrency limits on your Sound Classes to eliminate CPU spikes, especially on platforms with fewer cores where many simultaneous voice streams could impact the game’s frame rate.
Understand the “Sweet Spot” Bitrates
For most game applications, an Opus bitrate of 24kbps is sufficient for clear voice, and 96-128kbps is excellent for stereo music. Setting bitrates higher than necessary provides diminishing returns; staying within these bounds helps you eliminate wasted memory and processing power.
Configure VoIP Buffer Settings
If voice communication feels delayed, adjust the Voice.BufferDelay console variable. This module uses these buffers to reassemble packets. Finding the right balance between a small buffer (low latency) and a large buffer (stability) is the best way to eliminate audio dropouts in high-latency network environments.
Check Platform Support for Hardware Decoders
While the OpusAudioDecoder is a software-based solution, some platforms handle Opus more efficiently than others. On consoles, always profile your audio thread using Unreal Insights to ensure the software decoding of Opus streams doesn’t eliminate the performance gains you’ve made in other areas of the engine.