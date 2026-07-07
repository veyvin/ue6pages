---
layout: default
title: BenchmarkTool
---

<!-- ai-generation-failed -->

<h1>BenchmarkTool</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/BenchmarkTool/BenchmarkTool.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Projects</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

signed for automated hardware assessment and performance synthesis. It is primarily used to determine the relative “power” of the local CPU and GPU to automatically set initial scalability settings (like resolution scale, view distance, and shadow quality) when a user first launches the game.

This module is the engine’s internal implementation of the Synthetic Benchmark. It runs a series of intensive, short-duration math and rendering tests to generate a score, which is then mapped to the engine’s scalability buckets (Low, Medium, High, Epic, Cinematic).

1. Execute via SynthBenchmark Command

You can trigger the benchmark manually at runtime or in the editor using the console command SynthBenchmark. This will perform the tests and output the results to the log. This is the fastest way to see how the engine perceives your current hardware’s performance relative to its internal “WorkScale.”

2. Use for Initial Quality Auto-Detection

The most practical use for this module is during the “First Time Setup” of your game. Instead of forcing a default quality, call the benchmark in your Game User Settings logic.

Best Practice: Use UGameUserSettings::RunHardwareBenchmark() which internally utilizes the BenchmarkTool to detect and apply the optimal settings for the user’s hardware automatically.
3. Leverage Command Line for CI/CD

In automated build pipelines or performance testing environments, you can force the engine to run the benchmark and then exit using the -benchmark command-line argument.

Tip: Combine this with -benchmarkseconds=N to limit the duration of the test. This is useful for verifying that a build’s performance hasn’t regressed on specific hardware tiers during automated testing.
4. Isolate CPU vs. GPU Performance

The BenchmarkTool provides separate scores for the CPU and GPU.

Practical Tip: If your game is highly CPU-bound (like a strategy game with many units), use the CPU score to scale logic-heavy features (like AI complexity or animation update rates) while using the GPU score for visual fidelity.
5. Account for Laptop Power States

The benchmark is sensitive to the current power state of the machine.

Warning: If a user runs the benchmark while their laptop is unplugged or in “Power Saver” mode, the BenchmarkTool will return a low score and apply “Low” settings. Always include a “Reset to Defaults” button in your UI to allow users to re-run the assessment once they have plugged in their device.
6. Avoid Frequent Re-runs

Running a synthetic benchmark is resource-intensive and creates a “hitch” in the application.

Best Practice: Only run the benchmark once during the initial install or when the user explicitly requests a “Hardware Re-scan.” Running it every time the game starts is unnecessary and creates an annoying delay for the player.
7. Filter Out Background Noise

For the most accurate results, the benchmark should be run when no other heavy applications are active.

Tip: If you are running the BenchmarkTool for performance profiling, ensure you have closed web browsers and other developer tools. Background noise can artificially lower the score, leading to the engine setting lower quality levels than the hardware is actually capable of.
8. Use Results to Eliminate Compatibility Issues

You can use the numerical results from the BenchmarkTool to block players from entering certain high-fidelity modes (like Ray Tracing) if their hardware score falls below a specific threshold. This helps eliminate crashes or unplayable frame rates by proactively preventing users from selecting settings their hardware cannot sustain.