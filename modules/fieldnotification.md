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

Practices
1. Inherit from UMVVMViewModelBase

While you can implement the INotifyFieldValueChanged interface manually, the easiest way to utilize this module is to derive your C++ classes from UMVVMViewModelBase. This base class handles the boilerplate logic of the notification system, allowing you to focus on your data and logic.

2. Use the FieldNotify Specifier

To expose a property to the notification system, you must use the FieldNotify specifier in your UPROPERTY macro. This generates a “Field ID” that the MVVM system uses to track the variable.

C++
	UPROPERTY(BlueprintReadWrite, FieldNotify, Setter, Getter)

	float Health;
Copy code

Note: To maintain proper encapsulation, it is a best practice to keep these variables protected or private and use the generated Getters and Setters.

3. Use Macros for Value Updates

When updating a field in C++, use the UE_MVVM_SET_PROPERTY_VALUE macro. This macro is efficient because it automatically checks if the new value is different from the old value before assigning it and broadcasting the change. This prevents redundant UI updates and leads to the elimination of unnecessary performance overhead.

C++
	void AMyViewModel::SetHealth(float NewHealth)

	{

	    UE_MVVM_SET_PROPERTY_VALUE(Health, NewHealth);

	}
Copy code
4. Broadcast Function Results

You can also use Field Notifications for functions. This is useful for “derived” data, such as a “Health Percentage” function that depends on both CurrentHealth and MaxHealth.

C++
	UFUNCTION(BlueprintPure, FieldNotify)

	float GetHealthPercent() const;
Copy code

When CurrentHealth changes, you must manually call UE_MVVM_BROADCAST_FIELD_VALUE_CHANGED(GetHealthPercent) to tell the UI to re-run that function.

5. Keep FieldNotify Functions Pure and Const

Any function marked with FieldNotify must be BlueprintPure, const, and take no arguments. The notification system is designed to “pull” a single value from the function when notified; if the function has side effects or requires input parameters, it will break the MVVM binding logic.

6. Avoid Manual Broadcast Overuse

Only use UE_MVVM_BROADCAST_FIELD_VALUE_CHANGED when a value has actually changed or when a derived function needs refreshing. Constant broadcasting will negate the performance benefits of the system. The elimination of unnecessary broadcasts is key to keeping the UI thread responsive.

7. Leverage FieldID for Performance

In C++, you can refer to fields using their FFieldNotificationId. This is much faster than string-based lookups. The module provides generated names for your fields, typically in the format FFieldNotificationClassDescriptor::FieldInternalName.

8. Use for Gameplay-to-UI Separation

The primary best practice for this module is the elimination of direct dependencies between gameplay actors and UI widgets. Instead of a HealthComponent calling a function on a Widget, the HealthComponent updates a Viewmodel, and the FieldNotification module handles the hand-off to the UI automatically.