---
layout: default
title: AudioFormatADPCM
---

<!-- ai-generation-failed -->

<h1>AudioFormatADPCM</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/AudioFormatADPCM/AudioFormatADPCM.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AdpcmAudioDecoder, Core, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

der in Unreal Engine that implements Adaptive Differential Pulse Code Modulation. This is a “time-domain” compression codec, which differs from “frequency-domain” codecs like Ogg Vorbis or Opus.

It is primarily used for low-latency, low-CPU overhead audio playback. While it does not achieve the high compression ratios of Ogg Vorbis, it requires significantly less processing power to decompress. This makes it an ideal choice for mobile platforms, older consoles, or projects with extremely high voice counts where CPU performance is a bottleneck.

1. Identify Ideal Use Cases

ADPCM is best suited for short, punchy sound effects like footsteps, UI clicks, or rapid-fire weapon sounds. Because it is computationally “cheap” to decode, you can play back dozens of ADPCM sounds simultaneously without the CPU spikes associated with decompressing multiple Ogg or Opus streams.

2. Configure via Project Settings

You can set ADPCM as your default encoding for specific platforms. Navigate to Project Settings > Platforms > [Target Platform] > Audio. Under the Audio category, you can change the Standard Compression Type to ADPCM. This ensures that all sounds cooked for that platform use this codec unless overridden.

3. Balance Quality vs. CPU

ADPCM is technically a “lossy” format. It works by predicting the next audio sample based on previous ones and only storing the difference.

Tip: For high-fidelity music or ambient soundscapes, stick to Ogg Vorbis or Opus. For sound effects where a slight “hiss” or loss of high-end detail is unnoticeable, use ADPCM to save CPU cycles.
4. Optimize for Mobile Platforms

Mobile devices often have limited CPU resources for audio threading. By utilizing the audioformatadpcm module for the majority of your sound effects, you can eliminate audio-related hitches and reserve CPU overhead for gameplay logic and rendering.

5. Managing File Size Trade-offs

ADPCM typically results in a file size that is roughly 1/4th of the original uncompressed PCM (WAV) file. However, it is still significantly larger than an Ogg Vorbis file at similar quality.

Best Practice: Use ADPCM for sounds that must be “resident” in memory or played with zero latency, but avoid using it for long-form audio like voice-overs or music tracks to prevent bloated package sizes.
6. Use for High Voice-Count Scenarios

If your game features large-scale battles where hundreds of sounds (explosions, debris, vocalizations) fire at once, ADPCM is your best ally. It allows the audio engine to maintain high concurrency (the number of sounds playing at once) without hitting the platform’s CPU limit, preventing the elimination of important audio cues due to “voice stealing.”

7. Avoid Re-Compression Artifacts

Since ADPCM is lossy, avoid “double compression.” Always import high-quality, 16-bit uncompressed .wav files into Unreal. The audioformatadpcm module will handle the conversion during the cooking process. Compressing an already low-quality MP3 into ADPCM will result in noticeable digital artifacts and noise.

8. Verification via “stat soundwave”

To ensure your sounds are correctly using the ADPCM codec at runtime, use the console command stat soundwave. This overlay will show you the format of currently playing assets. If you see “ADPCM” listed next to your sound effects, the module is working correctly and your CPU-saving optimizations are in effect.