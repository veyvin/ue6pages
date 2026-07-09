---
layout: default
title: FunctionalTesting
---

<!-- ai-generation-failed -->

<h1>FunctionalTesting</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/FunctionalTesting/FunctionalTesting.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AIModule, AssetRegistry, AutomationController, Core, CoreUObject, EditorFramework, Engine, ImageWrapper, LevelEditor, MessageLog, NavigationSystem, RHI, RenderCore, SessionFrontend, Slate, SlateCore, SourceControl, UMG, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

tions (e.g., “Jump” or “Fire”). This allows for the elimination of manual “play-in-editor” sessions to verify that your input mapping contexts and modifiers are correctly configured.
3. Isolate Tests with Clean Levels

Functional tests should be self-contained to avoid “flaky” results caused by outside interference.

Best Practice: Create dedicated “Test Maps” that contain only the necessary geometry and the FunctionalTest actor. This results in the elimination of variable factors like random AI spawns or global lighting changes that might cause a test to fail inconsistently.
4. Leverage “Register Auto Destroy Actor”

Tests often involve spawning temporary actors (like projectiles or enemies) that can clutter the world.

Tip: Use the RegisterAutoDestroyActor function in your test logic. When the test finishes, the framework automatically handles the elimination of these spawned actors, ensuring the next test starts with a clean slate.
5. Use Meaningful Actor Names for Discovery

In the Session Frontend, functional tests are discovered based on the name of the Actor in the level.

Best Practice: Use a clear naming convention like FTest_Ability_DoubleJump. This makes it easy to find specific tests in a long list and facilitates the elimination of confusion when identifying which specific mechanic failed during a nightly build.
6. Assert State via “Finish Test”

The FinishTest node is the primary way to report success or failure to the automation system.

Tip: Always provide a descriptive string in the “Message” pin of the FinishTest node when a test fails. Detailed logging assists in the elimination of long debugging sessions by pointing exactly to what went wrong (e.g., “Player did not reach the trigger volume within 5 seconds”).
7. Test for “Elimination” and Game Over States

Automated tests are perfect for verifying that characters are correctly removed from the world when they lose all health.

Best Practice: Script a test where an AI takes lethal damage, and use a timer or event listener to verify the elimination of that AI actor. This confirms that your cleanup and “Game Over” logic triggers as expected without manual intervention.
8. Integrate with World Partition

For large open-world projects, you may need to test if objects interact correctly across cell boundaries.

Tip: Place functional tests at the edges of World Partition cells. Running these tests helps in the elimination of bugs related to actor persistence or streaming, where an object might disappear or lose its state when the player moves away.