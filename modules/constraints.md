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

ral relationships between objects, such as Actors, Components, or Control Rig controls. Unlike physics constraints (which handle rigid body collisions), this module is designed for Animation Authoring, allowing one transform to drive another through rules like “Parent,” “LookAt,” “Rotation,” or “Translation” constraints.

It is primarily used in Sequencer and the Level Editor to “eliminate” the need for permanent actor attachment or complex manual keyframing when objects need to interact dynamically (e.g., a character picking up a prop).

1. Module Configuration

To interface with the constraints system in C++, you must add the module to your Build.cs.

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "Constraints", "CoreUObject", "Engine" });

	```

	 

	```cpp

	#include "ConstraintsScriptingLibrary.h"

	#include "ConstraintsManager.h"

	#include "TransformConstraint.h"

	```

	 

	### 2. Practical Usage Tips & Best Practices

	 

	#### Prefer the Scripting Library for C++ Implementation

	Instead of manually instantiating constraint classes, use `UConstraintsScriptingLibrary`. It provides static methods like `CreateTransformableComponentHandle` and `AddConstraint` that handle the complex setup of parent/child handles and registration with the **Constraints Manager**. This "eliminates" boilerplate code and ensures your constraints are compatible with the Sequencer UI.

	 

	#### Master Keyframe Compensation

	When a constraint is toggled on or off mid-animation, the child object can "pop" to a new location. In C++, ensure you handle **Compensation**. The system can automatically generate a "compensation key" that adjusts the child's local transform so its world-space position remains identical the moment the constraint takes over. This "eliminates" visual discontinuities in your cutscenes.

	 

	#### Use the Constraints Manager for Global Control

	Every level with constraints automatically spawns a `AConstraintsManager` actor. In C++, you can access this via `UConstraintsScriptingLibrary::GetManager(World)`. Use it to query all active constraints in a scene. This is the most efficient way to "eliminate" orphaned constraints that might be lingering after an actor is deleted.

	 

	#### Implement "Maintain Offset" by Default

	When creating a Parent or LookAt constraint, the `bMaintainOffset` flag is your best friend. If true, the child keeps its current relative transform to the parent instead of snapping directly to the parent's pivot. This "eliminates" the need for invisible "offset actors" or complicated socket math when attaching props to a character's hand.

	 

	#### Leverage Dynamic Offsets for Layered Animation

	The **Dynamic Offset** feature allows you to continue keyframing a child object even while it is constrained. If you disable Dynamic Offset, the child is strictly locked to the parent's movement. Enabling it allows you to "eliminate" the rigidity of a constraint, letting you add secondary motion (like a hand shaking while holding a heavy object) on top of the parent's transform.

	 

	#### Bake Constraints for Final Performance

	Constraints carry a small CPU cost because they evaluate every frame. For final cinematic delivery, use the **Bake** functionality (`ConstraintsLibrary::Bake`). This converts the procedural constraint movement into standard keyframes on the child object. Once baked, you can "eliminate" the constraint itself, reducing the computation load for the final game build.

	 

	#### Distinguish Between Level and Sequence Constraints

	Be aware of where your constraints are stored. **Level Constraints** exist in the world persistently, while **Sequence Constraints** are stored within a specific `ULevelSequence`. If you only need a constraint for a specific cinematic, always ensure it is registered within the Sequencer context to "eliminate" clutter in your persistent level.

	 

	#### Utilize Tickable Constraints for Real-Time logic

	If you are extending the system, look at `UTickableConstraint`. This base class allows you to define custom C++ logic that runs during the engine's tick phase. It is perfect for creating specialized constraints, like a "Camera Shake Constraint" that only activates when a target actor reaches a certain velocity, "eliminating" the need for complex Tick functions in your Actor classes.
Copy code
2. Practical Usage Tips & Best Practices
Use the Scripting Library for C++ Setup

Instead of manually instantiating constraint classes, use UConstraintsScriptingLibrary. It provides static methods like CreateTransformableComponentHandle and AddConstraint that handle the complex internal registration with the Constraints Manager. This “eliminates” boilerplate and ensures your constraints show up correctly in the Sequencer UI.

Master Keyframe Compensation

When a constraint is toggled on or off mid-animation, the child object can “pop” to a new location. Use the Compensation logic to automatically generate keys that adjust the child’s local transform so its world-space position remains identical at the moment of the state change. This “eliminates” visual snapping in your cinematics.

Leverage the Constraints Manager Actor

Every level using these features spawns a AConstraintsManager. In C++, you can access this via FConstraintsManagerController. It serves as a centralized hub to view and manage all active relationships. Monitoring this manager helps “eliminate” orphaned constraints that might persist after an object is deleted.

Enable “Maintain Offset” by Default

When creating a Parent or LookAt constraint, the bMaintainOffset flag is critical. If true, the child keeps its current relative transform to the parent. This “eliminates” the need for invisible “offset helper” actors or complex socket math when a character needs to grab an object exactly where it sits.

Utilize Dynamic Offsets for Layered Animation

The Dynamic Offset feature allows you to continue keyframing a child object even while it is actively constrained. If you disable it, the child is strictly locked to the parent’s movement. Enabling it allows you to “eliminate” the rigidity of the system, letting you add secondary hand-animation on top of a constrained prop.

Bake Constraints for Final Performance

Constraints carry a small CPU cost because they evaluate every frame. For final cinematic delivery or gameplay export, use the Bake functionality. This converts the procedural movement into standard keyframes on the child’s transform track. Once baked, you can “eliminate” the constraint itself to save processing power.

Control Evaluation Order

In complex scenes (e.g., Character A holds a box, which Character B then grabs), the order in which constraints evaluate matters. Use the Constraints Manager to reorder the evaluation stack. This “eliminates” jitter or one-frame lags caused by a child being evaluated before its parent has moved.

Distinguish Between Level and Sequence Constraints

Constraints created in the viewport are “Level Constraints” and persist in the world. Constraints created while Sequencer is open are often “Sequence Constraints.” Be mindful of this distinction to “eliminate” confusion where a constraint might unexpectedly disappear when a specific Level Sequence is closed.