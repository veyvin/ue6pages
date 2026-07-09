---
layout: default
title: CinematicCamera
---


<h1>CinematicCamera</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/CinematicCamera/CinematicCamera.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DeveloperSettings, Engine, MovieScene, MovieSceneTracks, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

or the Cine Camera Actor and its associated components. Unlike the standard Camera module which provides basic perspective projection, the Cinematic Camera simulates real-world physical camera properties, including focal length, aperture (f-stop), sensor dimensions (filmback), and sophisticated focus tracking logic.

It is the industry-standard tool for virtual cinematography in Unreal Engine, used for creating high-end cinematics in Sequencer, virtual production (ICVFX), and photorealistic gameplay perspectives.

Practical Usage Tips and Best Practices
1. Use Physical Filmback Presets

Avoid manually guessing sensor sizes. The module provides accurate presets for 16:9 DSLR, Super 35mm, and IMAX. Choosing the correct filmback is crucial because it dictates the “Crop Factor” and how your focal length (mm) behaves, ensuring your virtual shots match real-world lenses.

2. Master the “Aperture” (f-stop) for Depth of Field

To achieve a cinematic “bokeh” effect (blurred background), lower the Current Aperture (e.g., f/1.8 or f/2.8). In the UCineCameraComponent, this directly affects the Depth of Field. Remember that opening the aperture also increases the amount of light in a physically-based lighting setup, so you may need to adjust your Exposure (ISO/Shutter Speed) accordingly.

3. Enable “Draw Debug Focus Plane”

Focusing in a 3D space can be difficult. Enable Draw Debug Focus Plane in the camera settings to see a translucent purple plane in your viewport. This shows exactly where the camera is focused. Move your Manual Focus Distance until the plane intersects your character’s eyes to ensure a sharp “elimination” of blur on your subject.

4. Leverage Focus Tracking

Instead of manually keyframing focus distance in Sequencer, use the Focus Settings > Tracking feature. By selecting an Actor (or a specific Component) to track, the camera will automatically update its focus distance every frame. You can add a Focus Offset to fine-tune the result if the actor’s pivot point isn’t precisely where you want the focus to land.

5. Utilize Lens Presets (Prime vs. Zoom)

The module includes common lens presets like 30mm Prime or 85mm Prime. Using these presets helps “eliminate” the “digital” look of a generic 90-degree FOV camera. For a classic cinematic look, use an 85mm lens for close-up portraits and a 24mm or 35mm lens for wide establishing shots.

6. Coordinate with Sequencer “Camera Cuts”

When using multiple Cine Camera Actors in a cinematic, always use a Camera Cut Track in Sequencer. This ensures the engine correctly switches between cameras and handles the transition of physical properties (like motion blur and focus) without “popping” or visual artifacts.

7. Crop Settings and Aspect Ratio

If your project requires a specific cinematic aspect ratio (like 2.39:1 Anamorphic), adjust the Crop Settings in the Cine Camera. This allows you to see the “letterbox” bars in the viewport, ensuring your composition remains perfect for the final render without needing to mask the UI later.

8. Optimize for Performance

Physical Depth of Field is GPU-intensive. To “eliminate” performance hitches during gameplay, you can use the CVar r.DepthOfFieldQuality to scale the quality. For cinematics, use the Movie Render Queue to render at the highest quality (Cinematic) settings, which are often too heavy for real-time play.

C++ Interaction: Accessing Camera Data

If you need to programmatically adjust cinematic properties, you must include the module in your Build.cs:

C#
PublicDependencyModuleNames.AddRange(new string[] { "CinematicCamera" });
Copy code

Then, you can access the component in C++:

C++
	#include "CineCameraComponent.h"

	#include "CineCameraActor.h"

	 

	void AMyDirector::FocusOnTarget(ACineCameraActor* Camera, AActor* Target)

	{

	    if (Camera && Target)

	    {

	        UCineCameraComponent* CineCam = Camera->GetCineCameraComponent();

	        

	        // Set to tracking focus

	        FCameraFocusSettings& FocusSettings = CineCam->FocusSettings;

	        FocusSettings.FocusMethod = ECameraFocusMethod::Tracking;

	        FocusSettings.TrackingFocusSettings.ActorToTrack = Target;

	        

	        UE_LOG(LogTemp, Log, TEXT("CineCamera now tracking target."));

	    }

	}
Copy code
Best Practices Summary
Composition: Use the “Rule of Thirds” or “Golden Ratio” overlays available in the Cine Camera viewport settings.
Stability: Use Camera Shake Base classes with Cine Cameras to add subtle handheld movement, which “eliminates” the sterile, robotic look of a static digital camera.
Sensor size: Match your sensor size to your target output (e.g., 16:9 Digital for most games, 2.35:1 for film).