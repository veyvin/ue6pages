---
layout: default
title: FieldNotification
---

<!-- ai-generation-failed -->

<h1>FieldNotification</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/FieldNotification/FieldNotification.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ngine primarily used to support the Model-View-ViewModel (MVVM) pattern in UMG. It provides the INotifyFieldValueChanged interface, which allows an object (a ViewModel) to broadcast a notification whenever a specific property or “field” changes. This creates a high-performance, event-driven bridge between your C++ data logic and your UI, allowing widgets to update automatically only when the data they are bound to is modified.

Practical Usage Tips & Best Practices
1. Use UMVVMViewModelBase as Your Parent Class

While you can implement the INotifyFieldValueChanged interface manually, it is significantly more efficient to inherit from UMVVMViewModelBase.

Best Practice: Inheriting from this base class provides the internal machinery needed for the elimination of boilerplate code, as it already contains the necessary logic to manage and broadcast field changes to the UI.
2. Decorate Properties with the FieldNotify Specifier

To make a property visible to the MVVM binding system and the FieldNotification module, you must use specific UPROPERTY metadata.

Tip: Use UPROPERTY(BlueprintReadOnly, FieldNotify). The FieldNotify tag is what allows the View Binding editor to “subscribe” to that variable. This leads to the elimination of manual “Update UI” function calls throughout your gameplay code.
3. Utilize UE_MVVM_SET_PROPERTY_VALUE for Changes

When updating a variable in C++, you should use the provided MVVM macros rather than direct assignment.

Best Practice: Use UE_MVVM_SET_PROPERTY_VALUE(PropertyName, NewValue). This macro automatically checks if the new value is different from the old one. If it is, it sets the value and triggers the notification, resulting in the elimination of redundant UI refreshes for unchanged data.
4. Manually Notify for Computed Functions

You can also use “FieldNotify” on functions (Getters) that don’t have a backing variable, such as a “Health Percentage” function.

Tip: If you have a function GetHealthPercent(), mark it as a FieldNotify in the UFUNCTION macro. You must then manually call BroadcastFieldValueChanged for that function whenever the underlying Health or MaxHealth variables change. This ensures the elimination of stale data in progress bars or text fields.
5. Prefer FieldNotification over Blueprint Tick

Many developers use the Tick event or “Property Binding” (the dropdown in UMG) to update UI, which runs every single frame.

Best Practice: Transitioning to FieldNotification ensures that the UI only logic runs when the data changes. This architectural shift leads to the elimination of unnecessary CPU overhead, especially in complex HUDs with dozens of moving parts.
6. Keep Variables Protected or Private

To ensure that the notification logic is always fired, variables should not be modified directly from outside the class.

Tip: Make your FieldNotify variables protected or private and provide public Setters that use the SET_PROPERTY_VALUE macro. This encapsulation ensures the elimination of bugs where a variable is updated but the UI fails to reflect the change because the notification was skipped.
7. Broadcast Multiple Fields Simultaneously

Sometimes a single action (like an “item elimination”) might change multiple related values, such as “Score,” “Killstreak,” and “Ammo Refill.”

Best Practice: You can broadcast multiple field changes in a single sequence. Correctly grouping these notifications helps in the elimination of “flickering” UI elements where one part of the HUD updates several frames before another related part.
8. Verify Bindings in the View Binding Diagnostics

If a UI element is not updating, the FieldNotification may not be reaching the widget.

Tip: Use the VM Diagnostics tool in the editor to trace notifications. This allows you to see exactly when a field change is broadcast and which widgets are receiving it, facilitating the elimination of “broken link” issues in your MVVM setup.