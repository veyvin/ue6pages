---
layout: default
title: ScreenShotComparisonTools
---

<!-- ai-generation-failed -->

<h1>ScreenShotComparisonTools</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/ScreenShotComparisonTools/ScreenShotComparisonTools.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AutomationMessages, Core, CoreUObject, DesktopPlatform, ImageWrapper, Json, JsonUtilities, RenderCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

r automated visual regression testing. It provides the backend logic for the Screenshot Comparison Tool found in the Unreal Session Frontend. This module is responsible for comparing a “New” screenshot (captured during a test) against a “Ground Truth” (an approved reference image) to identify rendering regressions or visual bugs.

By calculating pixel-by-pixel differences and applying tolerance filters, this module helps you eliminate the need for manual visual inspections of every level or UI element after a build. It is an essential component for any automated Quality Assurance (QA) pipeline in Unreal Engine.

Practical Usage Tips and Best Practices
Select Appropriate Tolerance Levels
Rendering is rarely 100% deterministic due to anti-aliasing (TAA/TSR) and noise. Use the built-in tolerance profiles—Low, Medium, or High—to account for these variations. Choosing the right tolerance helps you eliminate “false positive” failures caused by minor sub-pixel shifts or compression artifacts.
Use Functional Screenshot Test Actors
Instead of writing custom C++ capture logic, place Functional Screenshot Test Actors in your levels. These actors are designed to work natively with this module and allow you to set specific camera overrides and resolutions, which helps you eliminate inconsistencies between different test runs.
Manage Ground Truth via the Session Frontend
When a test fails because of a legitimate visual change (e.g., an intentional lighting update), use the Session Frontend to “Approve” the new image. This module then updates the reference image, helping you eliminate outdated baselines and keeping your test suite current.
Override Resolution for High-Fidelity Checks
You can set a global resolution for screenshots in Editor Preferences > Automation > Screenshots. However, for critical UI elements, use the local override on the Test Actor to force a higher resolution. This ensures you eliminate aliasing issues that could mask small visual regressions.
Use RGBA Channel Masking
If your test only cares about specific data (like an alpha mask or a depth pass), configure the comparison settings to ignore specific color channels. This targeted approach helps you eliminate noise from unrelated rendering passes, making your tests more robust.
Integrate with CI/CD Pipelines
Run your screenshot tests through the Unreal Automation Tool (UAT) as part of your nightly builds. Automatically generating these comparison reports helps you eliminate “regression creep,” where small visual bugs go unnoticed for weeks until they become difficult to fix.
Isolate UI with Custom Depth Masking
When capturing screenshots of specific 3D objects, enable the bMaskUsingCustomDepth option. This module can then use the depth buffer to “cut out” the background, helping you eliminate test failures caused by background changes that are irrelevant to the specific object being tested.
Clean Up Unapproved Images on Task Elimination
Upon the “elimination” of a test cycle, unapproved screenshots are stored in the Saved/Automation/Incoming folder. Periodically clear this folder to eliminate unnecessary disk bloat on your build machine and ensure you are only looking at the most recent test failures.