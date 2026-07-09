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

that provides the implementation for the Opus codec (via the libopus library). Unlike generic music formats, Opus is designed specifically for low-latency, high-quality audio streaming over networks.

In UE5, this module is the backbone for VoIP (Voice over IP) through the Online Subsystem and Pixel Streaming audio delivery. It serves as the bridge that translates compressed Opus bitstreams arriving over the network into raw PCM (Pulse Code Modulation) data that the Unreal Audio Mixer can process and play.

Practical Usage Tips & Best Practices
1. Add Module Dependency in Build.cs

If you are writing custom audio handling or VoIP logic in C++, you must explicitly include the module in your project.

Best Practice: Add "OpusAudioDecoder" to your PublicDependencyModuleNames in your .Build.cs file. Including this dependency results in the elimination of “Unresolved External Symbol” errors when attempting to use Opus-related audio info classes in your code.
2. Stick to 48kHz Sample Rates

Opus is internally designed to work most efficiently at a 48kHz sample rate. While it supports lower rates, 48kHz is the engine’s preferred standard for high-fidelity communication.

Tip: Ensure your capture and playback settings are aligned to 48,000Hz. Matching the internal Opus frequency facilitates the elimination of expensive resampling overhead on the CPU, which is particularly vital for mobile and XR platforms.
3. Optimize Bitrate for VoIP

One of the greatest strengths of the Opus module is its extreme efficiency at low bitrates.

Best Practice: For voice chat, a bitrate between 24kbps and 32kbps is usually the “sweet spot” for clear communication. Tuning this value leads to the elimination of significant network congestion in multiplayer games without noticeably sacrificing voice quality.
4. Leverage FOpusAudioInfo for Custom Streams

The FOpusAudioInfo class (found in OpusAudioInfo.h) is the primary C++ interface for decoding Opus data manually.

Tip: If you are streaming custom audio from a web server or third-party API, use FOpusAudioInfo to parse the headers and decode chunks into PCM. Utilizing the engine’s built-in wrapper results in the elimination of the need to write your own complex wrapper around raw libopus calls.
5. Monitor CPU Usage on Mobile

Because the OpusAudioDecoder is a software-based decoder, it consumes CPU cycles rather than utilizing dedicated hardware chips.

Best Practice: When targeting mobile devices, limit the number of simultaneous Opus streams (e.g., limit voice chat to the 4-5 closest players). Proactive stream management leads to the elimination of performance hitches during intense combat where the CPU is already under heavy load.
6. Use with Pixel Streaming for Low Latency

The Pixel Streaming plugin relies on this module to handle the audio half of the WebRTC protocol.

Tip: If you experience “robotic” or lagging audio in Pixel Streaming, check the -PixelStreamingEncoderTargetBitrate argument. Ensuring the decoder has enough data leads to the elimination of artifacts and maintains the “real-time” feel of the stream.
7. Verify Network Packet Loss Concealment (PLC)

The Opus codec has built-in logic to “guess” missing audio data when packets are lost over the internet.

Best Practice: Ensure your network protocol (UDP) is passing packets directly to the decoder logic. Relying on Opus’s internal PLC results in the elimination of harsh “pops” and “clicks” when a player’s internet connection fluctuates.
8. Toggle AudioLink for External Integration

UE5’s AudioLink can route audio from the engine to external middleware (like FMOD or Wwise) or vice-versa.

Tip: Use the console variable au.audiolink.enabled 1 if you need to route Opus-decoded VoIP streams through external audio processing chains. This flexibility facilitates the elimination of isolated “audio islands” where VoIP and game sounds cannot interact.