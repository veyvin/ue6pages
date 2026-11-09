---
layout: default
title: 计算框架 / Compute Framework
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Compute Framework</div>
      <div class="hero-title-cn">计算框架 · 支持用户编写的 GPU 计算图</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Rendering</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.9</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">5</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/ComputeFramework/ComputeFramework.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">支持用户编写的 GPU 计算图</div><div class="lang-content">Support for user authored GPU compute graphs</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：支持用户编写的 GPU 计算图</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：ComputeFramework, ComputeFrameworkEditor, ComputeDataInterface, EditableComputeGraph, EditableComputeGraphEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Support for user authored GPU compute graphs</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: ComputeFramework, ComputeFrameworkEditor, ComputeDataInterface, EditableComputeGraph, EditableComputeGraphEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Compute Framework</code>（运行时 <code class="usage-code">ComputeFramework</code>、<code class="usage-code">ComputeDataInterface</code>、<code class="usage-code">EditableComputeGraph</code>；编辑器 <code class="usage-code">ComputeFrameworkEditor</code>、<code class="usage-code">EditableComputeGraphEditor</code>）。</li><li>这是 GPU compute 图基础设施：<code class="usage-code">UComputeGraph</code> 描述 Kernel 与 <code class="usage-code">UComputeDataInterface</code> 的拓扑并编译着色器。动画变形器、PCG GPU 等在此之上做资源，很少在内容浏览器里「新建 Compute Graph」当独立玩法资产。</li><li>自研变形器/GPU 系统时：子类 <code class="usage-code">UComputeGraph</code>，添加 Kernel Invocation 与 Data Interface，改图后调用 <code class="usage-code">UpdateResources</code>（着色器异步编译，用 <code class="usage-code">HasKernelResourcesPendingShaderCompilation</code> 轮询）。</li><li>运行时用 <code class="usage-code">FComputeGraphInstance::CreateDataProviders</code> 按 BindingIndex 绑定场景对象，校验 <code class="usage-code">ValidateGraph</code> / <code class="usage-code">ValidateProviders</code>，再在渲染线程走 <code class="usage-code">GetRenderProxy()</code>。</li><li>游戏 <code class="usage-code">Build.cs</code> 加 <code class="usage-code">ComputeFramework</code>（需要接口再加 <code class="usage-code">ComputeDataInterface</code>）。<code class="usage-code">EditableComputeGraph*</code> 与 <code class="usage-code">*Editor</code> 模块不要进 Game Target。不要在 PPV 里找 Show Flag 当开关。</li></ol><p class="usage-note">给变形器/PCG 等用的 GPU 图运行时，不是 Niagara，也不是后期处理开关。蓝图几乎无入口。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Compute Framework</code> (runtime <code class="usage-code">ComputeFramework</code>, <code class="usage-code">ComputeDataInterface</code>, <code class="usage-code">EditableComputeGraph</code>; editor <code class="usage-code">ComputeFrameworkEditor</code>, <code class="usage-code">EditableComputeGraphEditor</code>).</li><li>It is GPU compute-graph infrastructure: <code class="usage-code">UComputeGraph</code> links kernels to <code class="usage-code">UComputeDataInterface</code>s and compiles shaders. Animation deformers and PCG GPU sit on top — you rarely create a standalone “Compute Graph” gameplay asset.</li><li>For a custom deformer/GPU system, subclass <code class="usage-code">UComputeGraph</code>, add kernel invocations and data interfaces, then <code class="usage-code">UpdateResources</code> (shader compile is async; poll <code class="usage-code">HasKernelResourcesPendingShaderCompilation</code>).</li><li>At runtime <code class="usage-code">FComputeGraphInstance::CreateDataProviders</code> binds scene objects by BindingIndex. <code class="usage-code">ValidateGraph</code> / <code class="usage-code">ValidateProviders</code>, then execute via <code class="usage-code">GetRenderProxy()</code> on the render thread.</li><li>Game <code class="usage-code">Build.cs</code> gets <code class="usage-code">ComputeFramework</code> (and <code class="usage-code">ComputeDataInterface</code> if you author interfaces). Keep <code class="usage-code">EditableComputeGraph*</code> and <code class="usage-code">*Editor</code> modules out of Game Targets. There is no Post Process Volume show-flag switch.</li></ol><p class="usage-note">GPU graph runtime for deformers/PCG — not Niagara and not a post-process toggle. Essentially no Blueprint entry point.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (5)</div><div class="module-item"><span class="dot"></span><span class="name mono">ComputeFramework</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ComputeFrameworkEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ComputeDataInterface</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EditableComputeGraph</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EditableComputeGraphEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/ComputeFramework/ComputeFramework.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
