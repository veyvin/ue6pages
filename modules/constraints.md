---
layout: default
title: Constraints
---

<!-- ai-generation-failed -->

<h1>Constraints</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/Animation/Constraints/Constraints.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnimationCore, Core, CoreUObject, Engine, MovieScene, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ctual actor attachment structure.

It is heavily utilized in Sequencer, Control Rig, and Animation Mode to handle complex interactions, such as a character picking up a prop or a camera tracking a moving target.

Practical Usage Tips and Best Practices
1. Leverage the Constraints Manager

When you create your first constraint, the engine automatically spawns a Constraints Manager actor in your level. Use this actor as a centralized hub to view, enable, or disable every constraint in the scene. This is the most efficient way to manage large-scale animations and ensures the elimination of “lost” constraints hidden deep within actor components.

2. Use for Non-Destructive Attachments

Standard actor attachment can be rigid and difficult to animate over time. Use the Constraints module to “attach” a weapon to a character’s hand during a cinematic. This allows you to toggle the influence on and off via Sequencer keys, leading to the elimination of complex “AttachToComponent” Blueprint logic during cutscenes.

3. Maintain Offsets by Default

When creating a constraint (Parent, LookAt, etc.), the “Maintain Offset” option is typically enabled. This preserves the relative distance and rotation between the objects at the moment of creation. If your object “snaps” to the parent unexpectedly, verify this setting to ensure the elimination of unwanted positional jumps.

4. Bake Constraints for Final Animation

Once a constrained animation is finalized, use the Bake function to convert the constraint’s influence into standard keyframes on the child object. This is a best practice for performance, as it allows for the elimination of the live constraint solver calculations during runtime playback or export.

5. Scripting with ConstraintsScriptingLibrary

For technical artists and pipeline engineers, the UConstraintsScriptingLibrary provides a Python and C++ API to automate constraint creation. You can programmatically create “Transformable Handles” for components or Control Rig bones, which is essential for the elimination of manual setup in large-batch animation processing.

6. Compensate Keyframes After Pose Changes

If you adjust the transform of a parent object after a constraint has already been keyed, you may notice a “pop” in the animation. Use the Compensate Key (or Compensate All Keys) command. This re-calculates the offset to match the new parent position, resulting in the elimination of visual hitches.

7. Combine with Control Rig for Complex Rigs

Constraints are natively compatible with Control Rig. You can constrain a specific Control Rig handle to a world-space actor (like a “LookAt” target). This allows animators to drive complex skeletal behavior using simple level actors, facilitating the elimination of restrictive, baked-in rig hierarchies.

8. Toggle “Dynamic Offset” for Rigid Locking

By default, you can still keyframe a child object even while it is constrained. If you want the child to follow the parent strictly with no additional local movement allowed, disable Dynamic Offset. This locks the relationship, ensuring the elimination of accidental “drifting” of the child object relative to its parent.