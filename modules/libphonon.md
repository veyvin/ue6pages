---
layout: default
title: libPhonon
---

<!-- ai-generation-failed -->

<h1>libPhonon</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/libPhonon/LibPhonon.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Dependencies
To access Steam Audio features in C++, you must include the module in your Build.cs. This eliminates linker errors when you attempt to interface with its specific spatialization or geometry components:
C#
PublicDependencyModuleNames.AddRange(new string[] { "Core", "Engine", "SteamAudio" });
Copy code
Use Steam Audio Geometry Components
For the engine to “see” your world, you must add Steam Audio Geometry components to your Static Meshes. This eliminates the reliance on simple raycasts, allowing the system to calculate reflections and diffraction based on the actual shape of the room.
Assign Phonon Material Settings
Not all surfaces reflect sound the same way. Use Steam Audio Material assets to define how much a surface absorbs or scatters specific frequencies. This eliminates “metallic” or “ringing” echoes in soft environments like carpeted rooms or forested areas.
Choose Between Baked and Real-Time Simulation
For static environments, use the Steam Audio Baker to pre-calculate acoustic data. This eliminates the high CPU cost of real-time wave simulation during gameplay, allowing you to achieve complex “around-the-corner” diffraction effects even on lower-end hardware.
Prioritize Critical Sounds
Acoustic simulation is computationally expensive. Use the “Acoustics” settings in your Sound Attenuation assets to eliminate simulation for background noises or UI sounds, reserving the high-fidelity spatialization for critical gameplay elements like footsteps or enemy gunfire.
Enable “Indirect Sound” for Immersion
Steam Audio can generate “Indirect Sound” (reverb) based on the listener’s location. By enabling this, you eliminate the static nature of standard reverb presets; the echo will naturally change as the player moves from a narrow hallway into a large cathedral.
Use ‘Air Absorption’ for Distance Realism
Combine libphonon with Unreal’s native Air Absorption settings. This eliminates the unnatural clarity of distant sounds by filtering out high frequencies over long ranges, which works in tandem with the spatialization data provided by the plugin.
Verify with the “Stat SteamAudio” Command
Use the console command stat SteamAudio during play-testing to monitor CPU usage and memory footprint. This eliminates performance guesswork, helping you identify if you have too many active real-time sources or if your baked data files are excessively large.