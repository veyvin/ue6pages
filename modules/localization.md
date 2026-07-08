---
layout: default
title: Localization
---

<!-- ai-generation-failed -->

<h1>Localization</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Localization/Localization.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DesktopPlatform, Json, JsonUtilities, Projects, SourceControl</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

.locres) that the engine reads at runtime.

This module works in tandem with the International Components for Unicode (ICU) library to handle culture-specific formatting—such as dates, currencies, and pluralization. Its primary goal is to provide a robust pipeline that allows developers to eliminate hard-coded strings and move toward a global-ready project.

Practical Usage Tips and Best Practices
Always Use FText for User-Facing Strings
Never use FString or FName for text that a player will see. Only FText is localization-aware and contains the “Namespace” and “Key” required for the localization gatherer. Using FText helps you eliminate the risk of untranslatable text appearing in your final UI.
Leverage the Localization Dashboard
Accessed via Tools > Localization Dashboard, this interface automates the gathering, exporting, and importing of text. Use it to manage your “Cultures” (languages) in one place, which helps you eliminate the complexity of manually editing translation manifest files.
Use Namespace for Better Organization
When creating text in C++, use the LOCTEXT_NAMESPACE macro. This groups related strings together (e.g., "InventorySystem"), making it easier for translators to understand the context of a word. Proper namespacing helps you eliminate confusion when the same word (like “Close”) has different meanings in different menus.
C++
	#define LOCTEXT_NAMESPACE "MenuSystem"

	FText ButtonText = LOCTEXT("PlayButton", "Play Game");

	#undef LOCTEXT_NAMESPACE
Copy code
Utilize Asset Localization for Visuals
If your game has textures or audio files containing language-specific content (e.g., a “Stop” sign or voice lines), use the Asset Localization feature. By placing a localized version of an asset in the L10N folder, the engine will automatically swap it at runtime, helping you eliminate the need for complex logic to switch textures based on language.
Implement Text Formatting for Dynamic Data
Use FText::Format instead of string concatenation. This allows translators to reorder variables based on the rules of their language, which is essential to eliminate grammatical errors in languages where the word order differs from English.
C++
	// Correct: "You have eliminated {Count} enemies."

	FText Msg = FText::Format(LOCTEXT("ElimMsg", "You have eliminated {0} enemies."), FText::AsNumber(EnemyCount));
Copy code
Export to Portable Object (.po) Files
The Localization module supports exporting your text to the .po format, which is the industry standard for translation software (like Poedit or Crowdin). This workflow helps you eliminate the friction of having translators work inside the Unreal Editor.
Test with ‘Culture Preview’ and ‘Word Count’
Use the “Preview” setting in the Localization Dashboard to view your UI in different languages directly in the editor. Also, keep an eye on the Word Count tool to estimate translation costs and eliminate unexpected budget overruns late in development.
Configure Culture Settings for Packaging
In Project Settings > Packaging, ensure you include the correct “Internationalization Support” data (e.g., EFIGS, CJK). Including only the data you need helps you eliminate unnecessary bulk in your final build size while ensuring all characters display correctly.