---
layout: default
title: AnimationEditorWidgets
---

<!-- ai-generation-failed -->

<h1>AnimationEditorWidgets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AnimationEditorWidgets/AnimationEditorWidgets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnimationCore, ApplicationCore, Core, CoreUObject, Engine, GraphEditor, InputCore, PropertyEditor, Slate, SlateCore, ToolMenus, ToolWidgets, UnrealEd, WidgetRegistration</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rovides a collection of specialized Slate widgets designed for animation authoring and playback control. It contains the UI building blocks used to create timelines, scrub bars, and track-based editors within the Persona (Animation) editor and related tools.

This module is primarily used by tools developers to build custom animation windows, allowing them to integrate standardized playback controls, frame-accurate scrubbing, and keyframe visualization into their own editor extensions.

Practical Usage Tips and Best Practices
1. Add Editor-Specific Module Dependencies

Since this module contains Slate logic that only exists in the Editor, it must be added to your [Project].Build.cs within a conditional block. Including it in a runtime build will cause packaging failures.

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "AnimationEditorWidgets", "Persona", "Slate", "SlateCore" });

	}
Copy code
2. Utilize SAnimTimeline for Custom Playback

If you are building a custom animation tool, use the SAnimTimeline widget. It provides a standardized look and feel for animation tracks. It handles the drawing of time rulers and the “playhead,” ensuring your tool feels consistent with the rest of the Unreal Engine animation suite.

3. Implement SScrubControlPanel for Standard Controls

For simple playback needs (Play, Pause, Skip, Loop), use the SScrubControlPanel. This widget encapsulates all the standard transport buttons. You can bind your own delegates to the playback commands to control how your specific animation or “elimination” sequence preview behaves.

4. Synchronize with the Persona Asset Editor

When using these widgets, it is best practice to link them to an IAnimationEditor instance. This allows your custom widgets to stay in sync with the current selection, playback speed, and scrub position of the main Persona window, providing a unified experience for the animator.

5. Leverage Frame-Accurate Scrubbing

The widgets in this module support various time formats (Frames, Seconds, or SMF). Always provide a way for users to toggle between “Seconds” and “Frames” in your UI settings, as technical animators often require frame-accurate positioning to verify the exact moment of an elimination event or contact point.

6. Handle Interaction Logic via Delegates

Most widgets in this module, such as the SAnimScrubBar, rely heavily on delegates (e.g., OnScrubPositionChanged). Ensure your C++ handler functions are efficient, as these delegates fire every frame during a scrub operation. Avoid performing heavy logic or actor spawning directly inside these calls.

7. Customize Timeline Colors and Styling

The module utilizes the FEditorStyle and specialized animation brushes. If you need to differentiate between different types of data on a timeline (such as Notifies versus Curves), you can pass custom styling parameters to the widgets to ensure clear visual hierarchy and “elimination” of UI clutter.

8. Implement Zoom and Pan Support

For complex animations, users need to zoom into specific sections of the timeline. The timeline widgets in this module support ViewRange attributes. Bind these to a shared “view state” object so that zooming in one part of your tool (like a curve editor) automatically zooms the timeline in your animation editor widget.