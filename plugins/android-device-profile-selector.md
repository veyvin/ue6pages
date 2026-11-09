---
layout: default
title: Android 设备配置文件选择器 / Android Device Profile Selector
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Android Device Profile Selector</div>
      <div class="hero-title-cn">Android 设备配置文件选择器 · Android 设备配置文件选择器用于显示硬件上设备配置文件的选</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Device Profile Selectors</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/AndroidDeviceProfileSelector/AndroidDeviceProfileSelector.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Android 设备配置文件选择器用于显示硬件上设备配置文件的选择</div><div class="lang-content">Android Device Profile Selector used show selection of device profiles on hardware</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：Android 设备配置文件选择器用于显示硬件上设备配置文件的选择</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：AndroidDeviceProfileSelector, AndroidDeviceProfileCommandlets, AndroidDeviceProfileSelectorRuntime。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Android Device Profile Selector used show selection of device profiles on hardware</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: AndroidDeviceProfileSelector, AndroidDeviceProfileCommandlets, AndroidDeviceProfileSelectorRuntime. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Android Device Profile Selector</code>（匹配 <code class="usage-code">AndroidDeviceProfileSelector</code> / 运行时 <code class="usage-code">AndroidDeviceProfileSelectorRuntime</code>，命令行 <code class="usage-code">AndroidDeviceProfileCommandlets</code>）。</li><li>在 <code class="usage-code">Project Settings &gt; Device Profiles</code> 或 <code class="usage-code">Config/DefaultDeviceProfiles.ini</code> 准备 Android 分级配置（如按 Adreno/Mali 档位）。</li><li>编辑匹配规则（GPU 族、GL/Vulkan、内存等），让启动时 <code class="usage-code">AndroidDeviceProfileSelectorRuntime</code> 选中对应 Device Profile。</li><li>包装到不同真机，用控制台 <code class="usage-code">dp.Override</code> 或日志确认实际套用的 Profile，再调 Scalability。</li><li>批量校验可用 <code class="usage-code">AndroidDeviceProfileCommandlets</code>；不要在 Windows PIE 指望 Android 匹配结果。</li></ol><p class="usage-note">启动时按硬件选 Device Profile，不是运行中可挂到 Actor 上的组件。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Android Device Profile Selector</code> (matching <code class="usage-code">AndroidDeviceProfileSelector</code> / runtime <code class="usage-code">AndroidDeviceProfileSelectorRuntime</code>, commandlets <code class="usage-code">AndroidDeviceProfileCommandlets</code>).</li><li>Author Android-tier profiles in <code class="usage-code">Project Settings &gt; Device Profiles</code> or <code class="usage-code">Config/DefaultDeviceProfiles.ini</code> (Adreno/Mali tiers, etc.).</li><li>Edit matching rules (GPU family, GL/Vulkan, memory) so <code class="usage-code">AndroidDeviceProfileSelectorRuntime</code> picks a Device Profile at startup.</li><li>Package to devices and confirm the applied profile via <code class="usage-code">dp.Override</code> or logs, then tune Scalability.</li><li>Use <code class="usage-code">AndroidDeviceProfileCommandlets</code> for bulk checks; Windows PIE will not produce Android matches.</li></ol><p class="usage-note">Selects a Device Profile from hardware at boot; it is not an actor component.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">AndroidDeviceProfileSelector</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AndroidDeviceProfileCommandlets</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AndroidDeviceProfileSelectorRuntime</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/AndroidDeviceProfileSelector/AndroidDeviceProfileSelector.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
