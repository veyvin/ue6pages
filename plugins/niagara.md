---
layout: default
title: 尼亚加拉 / Niagara
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">N</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Niagara</div>
      <div class="hero-title-cn">尼亚加拉 · 尼亚加拉效应系统。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>FX</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">8</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/FX/Niagara/Niagara.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">尼亚加拉效应系统。</div><div class="lang-content">Niagara effect systems.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Niagara 是虚幻引擎的下一代实时特效系统，用来制作火焰、烟雾、粒子、流体等。技术美术可以在模块栈里自己扩展行为，不必每次都找程序员。发射器可复用，同一次模拟也能用 Sprite、Ribbon、Mesh 多种方式渲染。</p><p>属于特效/Niagara 工具链。</p><p>它打包的模块包括：NiagaraCore, Niagara, NiagaraAnimNotifies, NiagaraShader, NiagaraVertexFactories, NiagaraBlueprintNodes, NiagaraEditor, NiagaraEditorWidgets。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">参考文档：<a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-visual-effects-system-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-visual-effects-system-in-unreal-engine</a></p></div><div class="lang-content"><p>Niagara is Unreal’s next-generation real-time VFX system for fire, smoke, particles, and fluids. Technical artists can add behavior in the module stack without a programmer. Emitters are reusable, and one simulation can render as sprites, ribbons, and meshes at once.</p><p>Part of the FX / Niagara toolchain.</p><p>It ships these modules: NiagaraCore, Niagara, NiagaraAnimNotifies, NiagaraShader, NiagaraVertexFactories, NiagaraBlueprintNodes, NiagaraEditor, NiagaraEditorWidgets. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Docs: <a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-visual-effects-system-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-visual-effects-system-in-unreal-engine</a></p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Niagara</code>（模块 <code class="usage-code">NiagaraCore</code>、<code class="usage-code">Niagara</code>、<code class="usage-code">NiagaraShader</code>、<code class="usage-code">NiagaraVertexFactories</code>、<code class="usage-code">NiagaraBlueprintNodes</code>，编辑器 <code class="usage-code">NiagaraEditor</code> 等）。</li><li>它是引擎的下一代实时特效系统：火焰、烟雾、粒子、流体；可在模块栈里扩展行为。</li><li>创建 Niagara 系统/发射器，在模块栈里组合行为，按 Sprite/Ribbon/Mesh 渲染。</li><li>Game 模块依赖运行时模块；<code class="usage-code">NiagaraEditor</code>/<code class="usage-code">NiagaraEditorWidgets</code> 等只进 Editor Target。</li></ol><p class="usage-note">Niagara 实时特效系统本体（火焰/烟/粒子/流体）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Niagara</code> (modules <code class="usage-code">NiagaraCore</code>, <code class="usage-code">Niagara</code>, <code class="usage-code">NiagaraShader</code>, <code class="usage-code">NiagaraVertexFactories</code>, <code class="usage-code">NiagaraBlueprintNodes</code>, editor <code class="usage-code">NiagaraEditor</code>, etc.).</li><li>It is the engine&#x27;s next-gen VFX system: fire, smoke, particles, fluids; behaviors extend in the module stack.</li><li>Create Niagara systems/emitters, compose behaviors in the module stack, and render as Sprite/Ribbon/Mesh.</li><li>Game modules depend on runtime modules; <code class="usage-code">NiagaraEditor</code>/<code class="usage-code">NiagaraEditorWidgets</code> etc. go to Editor targets only.</li></ol><p class="usage-note">The core Niagara real-time VFX system (fire/smoke/particles/fluids).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (8)</div><div class="module-item"><span class="dot"></span><span class="name mono">NiagaraCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Niagara</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">NiagaraAnimNotifies</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">NiagaraShader</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">NiagaraVertexFactories</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">NiagaraBlueprintNodes</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">NiagaraEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">NiagaraEditorWidgets</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/FX/Niagara/Niagara.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
