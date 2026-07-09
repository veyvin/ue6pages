---
layout: default
title: ClientPilot
---

<!-- ai-generation-failed -->

<h1>ClientPilot</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/ClientPilot/ClientPilot.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

uman operator. It is primarily used to drive “headless” clients in stress tests, perform automated smoke tests, and facilitate complex multiplayer testing scenarios via the Gauntlet Automation Framework.

Practical Usage Tips & Best Practices
1. Integrate with Gauntlet Controllers

ClientPilot is most effective when used as the execution arm of a UGauntletTestController.

Best Practice: Use your Gauntlet script to handle the high-level test flow (like level loading and state transitions) and use ClientPilot to execute the specific inputs required to move the character or interact with the UI.
2. Utilize for Multiplayer Stress Testing

When testing high-player-count scenarios (e.g., a 100-player battle royale), you cannot manually play every client.

Tip: Deploy multiple “headless” clients (running with -nullrhi) and use ClientPilot to make them move, jump, and fire weapons. This provides a realistic load on the server’s CPU and networking code, helping in the elimination of bottlenecks before a live release.
3. Implement Input Recording and Playback

ClientPilot supports recording a sequence of inputs from a human player and saving them to a data asset or file.

Best Practice: Record standard “golden paths” (like completing a tutorial). During automated nightly builds, have ClientPilot play back these recordings to ensure that new code changes haven’t broken the core gameplay flow.
4. Leverage “ClientPilotBlackboard” for State

The module includes a blackboard system for sharing data between the automation script and the game instance.

Tip: Use the blackboard to store target coordinates or objective IDs. This allows your “Pilot” to react dynamically to the game world (e.g., “Move to the location of the nearest item”) rather than relying on hard-coded input sequences that might break if the map changes.
5. Synchronize with Server State

In multiplayer tests, a client might try to interact with an object before it has replicated.

Best Practice: Always wrap ClientPilot actions in “Wait” logic. Use the module’s capability to check for specific game states or replicated variables before sending the next input command to avoid test failures caused by network latency.
6. Automate Character Elimination Tests

ClientPilot is excellent for verifying combat and health systems.

Tip: Program one client to stand still while another client uses ClientPilot inputs to attack. You can then verify that the elimination event triggers correctly, the UI updates, and the character is properly removed or respawned without manual intervention.
7. Use for Headless UI Validation

While ClientPilot is often used for 3D movement, it can also simulate navigation through UMG menus.

Best Practice: Use it to stress-test the store or inventory systems by rapidly opening and closing widgets. This can reveal memory leaks or race conditions in the UI code that only appear after hundreds of rapid interactions.
8. Monitor Performance via Console Commands

You can trigger ClientPilot commands via the in-game console during development.

Tip: Commands like ClientPilot.Start or ClientPilot.Stop allow you to toggle automation on the fly. This is useful for quickly setting up a “self-playing” scene while you use Unreal Insights to profile the engine’s performance in real-time.