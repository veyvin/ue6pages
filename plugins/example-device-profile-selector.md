---
layout: default
title: 设备配置文件选择器示例 / Example Device Profile Selector
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">E</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Example Device Profile Selector</div>
      <div class="hero-title-cn">设备配置文件选择器示例 · 使用的示例设备配置文件选择器显示硬件上设备配置文件的选择</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Device Profile Selectors</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/ExampleDeviceProfileSelector/ExampleDeviceProfileSelector.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">使用的示例设备配置文件选择器显示硬件上设备配置文件的选择</div><div class="lang-content">Example Device Profile Selector used show selection of device profiles on hardware</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：使用的示例设备配置文件选择器显示硬件上设备配置文件的选择</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：ExampleDeviceProfileSelector。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Example Device Profile Selector used show selection of device profiles on hardware</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: ExampleDeviceProfileSelector. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">ExampleDeviceProfileSelector</code> 是引擎里 <code class="usage-code">IDeviceProfileSelector</code> 接口的参考实现。先在 <code class="usage-code">Plugins/Runtime/ExampleDeviceProfileSelector</code> 下读它的 <code class="usage-code">.cpp</code>，看它如何按硬件、分辨率、GPU 等条件匹配设备配置。</li><li>启用插件后，在 <code class="usage-code">Config/DefaultEngine.ini</code> 的 <code class="usage-code">[/Script/Engine.Engine]</code> 把 <code class="usage-code">DeviceProfileSelectorModule</code> 指向示例模块名，观察它如何为当前硬件挑中一个 profile。</li><li>把这个示例当模板：复制它的类，在 <code class="usage-code">GetDeviceProfileName</code> 一类的决策函数里换成你自己设备（机型、SoC、显存）的判定逻辑。</li><li>在 <code class="usage-code">Window &gt; Developer Tools &gt; Device Profiles</code> 里对照当前生效的 profile，确认选择结果和你写死的规则一致。</li><li>用不同机型/DPI 的构建，或命令行 <code class="usage-code">-deviceprofile=</code> 强制切换，验证选择器返回的是预期 profile 而不是回退到默认。</li><li>要自己实现时只需实现 <code class="usage-code">IDeviceProfileSelectorModule</code> 并注册为插件模块，不必依赖示例模块本体；示例仅作学习与拷贝来源。</li></ol><p class="usage-note">它只是接口参考实现，真正用途是照它写出自己的「按硬件选设备配置」模块。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">ExampleDeviceProfileSelector</code> is the engine&#x27;s reference implementation of <code class="usage-code">IDeviceProfileSelector</code>. Open its <code class="usage-code">.cpp</code> under <code class="usage-code">Plugins/Runtime/ExampleDeviceProfileSelector</code> and read how it matches a device profile by hardware, resolution, GPU, etc.</li><li>Enable it, then in <code class="usage-code">Config/DefaultEngine.ini</code> under <code class="usage-code">[/Script/Engine.Engine]</code> point <code class="usage-code">DeviceProfileSelectorModule</code> at the example module and watch how it picks a profile for the current hardware.</li><li>Use the example as a template: copy its class and replace the decision function (e.g. <code class="usage-code">GetDeviceProfileName</code>) with your own rules for device model, SoC, or VRAM.</li><li>In <code class="usage-code">Window &gt; Developer Tools &gt; Device Profiles</code>, compare against the profile that actually becomes active to confirm the selection matches your hard-coded rules.</li><li>Test with builds for different devices/DPI, or force <code class="usage-code">-deviceprofile=</code> on the command line, and verify the selector returns the expected profile instead of falling back to default.</li><li>To ship your own, just implement <code class="usage-code">IDeviceProfileSelectorModule</code> and register it as a plugin module — you do not depend on the example itself; it is only a learning/copy source.</li></ol><p class="usage-note">It is only a reference implementation; the real use is copying it to write your own hardware-based device-profile selection module.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">ExampleDeviceProfileSelector</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/ExampleDeviceProfileSelector/ExampleDeviceProfileSelector.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
