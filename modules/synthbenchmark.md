---
layout: default
title: SynthBenchmark
---

<!-- ai-generation-failed -->

<h1>SynthBenchmark</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/SynthBenchmark/SynthBenchmark.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, RHI, RenderCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

within Unreal Engine designed to quickly estimate the relative power of a user’s CPU and GPU.

Description and Purpose

Unlike deep profiling tools like Unreal Insights, SynthBenchmark executes a series of “synthetic” tests—short, intensive mathematical and rendering tasks—to generate a performance index. Its primary purpose is to provide the data used by the Scalability system to auto-configure graphics settings. When you call “Auto-Detect” in the settings menu, this module runs its benchmarks to calculate a PerfIndex. By using this module, the engine can eliminate the guesswork involved in supporting diverse hardware, ensuring the game starts with a playable frame rate on both low-end laptops and high-end workstations.

Practical Usage Tips and Best Practices
Trigger via Console for Testing
You can manually trigger the benchmark by entering the console command SynthBenchmark. This will output the CPU and GPU performance indices to the log. This is useful during development to eliminate confusion about whether a performance drop is due to code changes or hardware throttling.
Run During First-Boot Experience
A best practice is to execute the benchmark the first time a player launches the game. You can then use the ApplyHardwareBenchmarkResults function in UGameUserSettings to eliminate the friction of a player having to manually adjust sliders before they can play.
Monitor Thermal Throttling
If you run the benchmark repeatedly and see the PerfIndex dropping, it is a clear sign of thermal throttling. Use this module’s results to eliminate false “optimization” bugs that are actually caused by the hardware slowing down due to heat.
Use Results to Set Scalability Groups
The values returned by the benchmark map to Scalability Groups (0 for Low, 3 for Epic, etc.). By binding your graphics presets to these indices, you can eliminate the risk of a high-end feature (like Ray Tracing) being enabled on a GPU that cannot support it.
Account for Laptop Battery Modes
Be aware that the benchmark results will differ significantly if a laptop is unplugged. It is a best practice to re-run a lightweight version of the benchmark if the power state changes to eliminate sudden frame rate drops when a user disconnects their charger.
Integrate with UGameUserSettings C++
In C++, you can call RunHardwareBenchmark on your UGameUserSettings object. This utilizes the SynthBenchmark module internally. This is the cleanest way to eliminate manual boilerplate code when implementing an auto-detect feature.
Verify PerfIndexThresholds in Config
The mapping of benchmark scores to quality levels is defined in BaseScalability.ini under [PerfIndexThresholds]. You should tune these values for your specific project to eliminate instances where the auto-detector incorrectly targets “Ultra” settings for a mid-range card.
Avoid Running During Gameplay
The benchmarks are “synthetic” and designed to consume 100% of available resources for a few seconds. Never trigger this module while a level is active, as it will eliminate the player’s frame rate and likely cause a temporary system hang.