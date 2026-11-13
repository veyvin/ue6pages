---
layout: default
title: 级联至 Niagara 转换器 V2 / Cascade To Niagara Converter V2
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Cascade To Niagara Converter V2</div>
      <div class="hero-title-cn">级联至 Niagara 转换器 V2 · 基于实验性 C++ 的 Cascade 到 Niagara 转换</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>FX</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/FX/CascadeNiagaraConverterV2/CascadeNiagaraConverterV2.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">基于实验性 C++ 的 Cascade 到 Niagara 转换器。</div><div class="lang-content">Experimental C++ based Cascade to Niagara converter.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Niagara 是虚幻引擎的下一代实时特效系统，用来制作火焰、烟雾、粒子、流体等。技术美术可以在模块栈里自己扩展行为，不必每次都找程序员。发射器可复用，同一次模拟也能用 Sprite、Ribbon、Mesh 多种方式渲染。</p><p>属于特效/Niagara 工具链。</p><p>它打包的模块包括：CascadeNiagaraConverterV2。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">参考文档：<a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-visual-effects-system-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-visual-effects-system-in-unreal-engine</a></p></div><div class="lang-content"><p>Niagara is Unreal’s next-generation real-time VFX system for fire, smoke, particles, and fluids. Technical artists can add behavior in the module stack without a programmer. Emitters are reusable, and one simulation can render as sprites, ribbons, and meshes at once.</p><p>Part of the FX / Niagara toolchain.</p><p>It ships these modules: CascadeNiagaraConverterV2. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Docs: <a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-visual-effects-system-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-visual-effects-system-in-unreal-engine</a></p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用实验性 <code class="usage-code">Cascade To Niagara Converter V2</code>（模块 <code class="usage-code">CascadeNiagaraConverterV2</code>）。这是 C++ 本机管线，不是第一代 Python 转换器。</li><li>不要与 <code class="usage-code">Cascade To Niagara Converter</code> 同时对同一资产点转换，以免生成两套互相覆盖的 Niagara System。</li><li>右键 <code class="usage-code">Particle System</code>，用 V2 的 Convert 命令（菜单项带 V2/C++ Converter）生成同目录 Niagara System。</li><li>打开结果，对照 Cascade：GPU 粒子、碰撞、Event Generator、Mesh 材质、SubUV、Facing Mode 常需手修；V2 映射发射器/模块，但不保证像素级一致。</li><li>把关卡与蓝图里的 <code class="usage-code">ParticleSystemComponent</code> 换成 <code class="usage-code">NiagaraComponent</code>，确认 LOD 与终结条件。</li><li>批量可对内容目录跑转换器命令让/编辑器脚本调用 <code class="usage-code">CascadeNiagaraConverterV2</code>，每次看转换日志而不是只看是否出资产。</li><li>不要把该模块加入游戏 <code class="usage-code">Build.cs</code>；实验接口可能改。</li></ol><p class="usage-note">C++ 实验转换器。第一代脚本转换器是 `cascade-to-niagara-converter`；两者选其一做批量迁移。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable experimental <code class="usage-code">Cascade To Niagara Converter V2</code> (module <code class="usage-code">CascadeNiagaraConverterV2</code>). This is the native C++ pipeline, not the first-generation Python converter.</li><li>Do not run <code class="usage-code">Cascade To Niagara Converter</code> on the same asset at the same time or you will get two overlapping Niagara Systems.</li><li>Right-click the <code class="usage-code">Particle System</code> and use the V2 Convert command (menu labeled V2/C++ Converter) to emit a Niagara System beside the original.</li><li>Open the result and compare: GPU particles, collisions, Event Generators, mesh materials, SubUV, and Facing Mode often need a TD pass. V2 maps emitters/modules; it is not pixel-identical.</li><li>Replace <code class="usage-code">ParticleSystemComponent</code> with <code class="usage-code">NiagaraComponent</code> in levels and Blueprints; recheck LOD and completion.</li><li>For batches, run the converter commandlet / editor script against <code class="usage-code">CascadeNiagaraConverterV2</code> and read conversion logs, not just whether an asset appeared.</li><li>Do not add this module to a game <code class="usage-code">Build.cs</code>. The experimental API may change.</li></ol><p class="usage-note">Experimental C++ converter. The script-based first generation is `cascade-to-niagara-converter`. Pick one for a given batch.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">CascadeNiagaraConverterV2</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/FX/CascadeNiagaraConverterV2/CascadeNiagaraConverterV2.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
