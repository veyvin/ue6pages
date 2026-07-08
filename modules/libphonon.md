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

e Tips and Best Practices
Enable the Steam Audio Plugin
Libphonon is accessed through the Steam Audio plugin. Ensure the plugin is enabled in your project and set “Steam Audio” as your Spatialization Plugin, Reverb Plugin, and Occlusion Plugin in the Project Settings > Windows (or target platform) > Audio. This synchronization helps you eliminate conflicts between competing audio processing units.
Assign Steam Audio Geometry Components
For the module to calculate reflections and occlusion, you must add a Steam Audio Geometry component to your Static Meshes or use the Steam Audio Static Mesh actor. This allows Libphonon to “see” the world, helping you eliminate instances where sounds fail to bounce or occlude correctly in complex environments.
Use Phonon Material Assets
The module relies on physical properties to determine how much sound is absorbed or reflected. Create and assign Steam Audio Material assets to your geometry. Choosing “Concrete” vs. “Carpet” within these settings allows the engine to eliminate unrealistic, overly bright echoes in rooms that should be acoustically dampened.
Bake Static Propagation for Performance
Real-time calculation of complex sound paths can be CPU intensive. Use the Steam Audio Baker to pre-calculate (bake) sound propagation for static lights and geometry. This helps you eliminate CPU spikes and frame-rate hitches that occur when many spatialized sounds are triggered simultaneously.
Configure HRTF for Headphones
Libphonon provides high-quality HRTF (Head-Related Transfer Function). Remind users to test with headphones, as HRTF is designed to simulate 3D positioning for binaural output. Using these settings correctly helps you eliminate the “flat” stereo feel and provides players with precise directional “elimination” awareness in competitive shooters.
Optimize the ‘Occlusion Sample Count’
In the Steam Audio settings, you can adjust the number of samples used for occlusion traces. Lowering this count for background ambient sounds while keeping it high for critical gameplay cues helps you eliminate unnecessary processing overhead without sacrificing tactical clarity.
Utilize Indirect Sound (Reverb) Carefully
The module can generate procedural reverb based on room shape. To eliminate a “muddy” mix, avoid using both Steam Audio’s procedural reverb and standard Unreal Reverb Volumes in the same space. Stick to the Libphonon-driven reflections for a more cohesive and physically accurate acoustic environment.
Monitor CPU Usage with ‘stat SteamAudio’
Use the console command stat SteamAudio to view the real-time performance of the Libphonon module. This display shows the time taken for spatialization and occlusion tasks, allowing you to eliminate performance bottlenecks by adjusting baking settings or reducing the complexity of your acoustic geometry.