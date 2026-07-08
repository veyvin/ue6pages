---
layout: default
title: IasTool
---

<!-- ai-generation-failed -->

<h1>IasTool</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/IoStoreOnDemand/IasTool.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, IoStoreOnDemandUtilities, Projects</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nd-line utility and supporting library used for automated visual validation in Unreal Engine. It is the primary engine tool for comparing two images to determine if they are visually equivalent within specific mathematical tolerances.

What it is and What it’s used for

Located in Engine/Source/Programs/ImageAnalysisTool, this module is a core component of the Automation System. It is used to compare “Ground Truth” (baseline) screenshots against “Incoming” (new) screenshots generated during automated rendering tests.

Primary uses include:

Regression Testing: Detecting unintended changes in rendering, materials, or VFX after engine updates or code changes.
Per-Pixel Comparison: Analyzing differences between images using various metrics like RMSE (Root Mean Square Error) or Peak Signal-to-Noise Ratio (PSNR).
Batch Processing: Comparing large sets of images produced by the Functional Test system across different platforms (e.g., comparing a Windows render to an Xbox render).
CI/CD Validation: Automatically failing build pipeline tasks if a screenshot deviates significantly from the approved baseline.
Practical Usage Tips and Best Practices
1. Use Through RunUAT

While it is a standalone program, the most stable way to invoke the IASTool is via the Unreal Automation Tool (UAT). Use the command RunUAT.bat ImageComparison ... to ensure all environment paths and dependencies are correctly initialized, which leads to the elimination of manual setup errors.

2. Configure Tolerances for TAA Noise

Temporal Anti-Aliasing (TAA) and ray-tracing effects introduce non-deterministic pixel noise. Never use a 0% tolerance. A best practice is to set a “Low” or “Medium” tolerance in your DefaultEditor.ini to allow for slight per-pixel variations while still catching significant rendering breaks.

3. Leverage the “Difference” Image

When a comparison fails, IASTool generates a “Difference” texture (usually a heat map). Use this image to identify exactly where the failure occurred. If the difference is concentrated on a single mesh, the issue is likely a material change; if it is screen-wide, it points to a post-processing or lighting regression.

4. Account for Floating Point Drift

Different GPUs (NVIDIA vs. AMD) or APIs (DX12 vs. Vulkan) may produce slightly different color values due to floating-point rounding. Use the MaxDifference threshold setting to ignore these tiny shifts, ensuring the elimination of “false positive” test failures across multi-platform build farms.

5. Exclude UI via Masking

If your screenshots contain dynamic UI elements (like a frame rate counter), the comparison will always fail. Use the IASTool’s masking features or ensure you use the Functional UIScreenshot Test actor which can isolate specific layers, ensuring only the 3D world is being validated.

6. Automate Baseline Updates

When a rendering change is intentional (e.g., an art pass), you must update the ground truth. Use the Screenshot Comparison Tool in the Session Frontend to “Approve” new images. This command internally uses IASTool to overwrite the old baseline with the new incoming image.

7. Use PSNR for Quality Analysis

For high-fidelity projects, use the PSNR (Peak Signal-to-Noise Ratio) metric instead of simple RGB delta. PSNR is a better indicator of how the human eye perceives quality loss, which is a best practice when validating the impact of new texture compression or LOD settings.

8. Strategic Elimination of Stale Baselines

Baselines can become outdated as lighting or post-processing evolves. Periodically audit your Saved/Automation/Baselines folder and perform a total elimination of unused or extremely old baseline images. This keeps your project repository lean and prevents the automation system from comparing against irrelevant data.