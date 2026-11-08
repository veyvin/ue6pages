---
layout: default
title: UAF 默认通知 / UAF Default Notifies
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">U</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">UAF Default Notifies</div>
      <div class="hero-title-cn">UAF 默认通知 · 默认 UAF 通知子类加上本机 C++ 通知处理程序（播放声音、</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Animation</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/UAF/UAFDefaultNotifies/UAFDefaultNotifies.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">默认 UAF 通知子类加上本机 C++ 通知处理程序（播放声音、播放 Niagara Effect）。演示 UAF 本机 (C++) 通知处理程序 API。</div><div class="lang-content">Default UAF notify subclasses plus native C++ notify handlers (Play Sound, Play Niagara Effect). Demonstrates the UAF native (C++) notify handler API.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：默认 UAF 通知子类加上本机 C++ 通知处理程序（播放声音、播放 Niagara Effect）。演示 UAF 本机 (C++) 通知处理程序 API。</p><p>Niagara/VFX 家族：在 Niagara 模块栈或资产上扩展特效，而不是另起一套粒子系统。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：UAFDefaultNotifies。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Default UAF notify subclasses plus native C++ notify handlers (Play Sound, Play Niagara Effect). Demonstrates the UAF native (C++) notify handler API.</p><p>Niagara/VFX family: extend effects in the Niagara stack or assets, not a separate particle engine.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: UAFDefaultNotifies. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">UAF Default Notifies</code>（模块 <code class="usage-code">UAFDefaultNotifies</code>）。</li><li>它提供默认 UAF 通知子类，加上本机 C++ 通知处理程序（播放声音、播放 Niagara 效果）。</li><li>用它演示并使用 UAF 本机(C++)通知处理程序 API：在动画通知点触发音效/特效。</li><li>属 UAF 通知内置库；运行时模块可进包。</li></ol><p class="usage-note">默认 UAF 通知子类 + 本机 C++ 通知处理程序（声音/Niagara）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">UAF Default Notifies</code> (module <code class="usage-code">UAFDefaultNotifies</code>).</li><li>It provides default UAF notify subclasses plus native C++ notify handlers (play sound, play Niagara effect).</li><li>Use it to demo/use the native (C++) notify-handler API: trigger SFX/VFX at animation notify points.</li><li>It is a built-in UAF notify library; runtime modules can ship.</li></ol><p class="usage-note">Default UAF notify subclasses + native C++ notify handlers (sound/Niagara).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">UAFDefaultNotifies</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/UAF/UAFDefaultNotifies/UAFDefaultNotifies.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
