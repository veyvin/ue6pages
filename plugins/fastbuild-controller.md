---
layout: default
title: 快速构建控制器 / FastBuild Controller
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">F</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">FastBuild Controller</div>
      <div class="hero-title-cn">快速构建控制器 · 添加对使用 FastBuild 的着色器编译分发的支持</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Build Distribution</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/FastBuildController/FastBuildController.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">添加对使用 FastBuild 的着色器编译分发的支持</div><div class="lang-content">Adds support for shader compiling distribution using FastBuild</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：添加对使用 FastBuild 的着色器编译分发的支持</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：FastBuildController。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Adds support for shader compiling distribution using FastBuild</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: FastBuildController. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>先安装 FastBuild 并配好分布式编译环境（broker/worker、<code class="usage-code">FASTBUILD_BROKER</code> 等环境变量），确保 broker 可被访问。</li><li>启用 <code class="usage-code">FastBuildController</code> 插件，让着色器编译可以走 FastBuild 的分布式后端。</li><li>在项目设置或 <code class="usage-code">DefaultEngine.ini</code> 里打开着色器编译分发，指定 broker 与 worker 列表（或多个 worker 节点）。</li><li>启动若干 FastBuild worker 节点，回到编辑器触发着色器编译（改材质、加光源或 <code class="usage-code">RecompileShaders</code>）。</li><li>在日志里搜 FastBuild/Broker 相关行，确认编译任务被分发到 worker，而不是本机串行编译。</li><li>对比开启前后的着色器编译耗时验证分发生效；节点掉线时先查 broker 连通性与防火墙。</li></ol><p class="usage-note">本质是着色器编译的分发，不是输入控制器；要先把 broker/worker 环境配好才能看到分发。</p></div><div class="lang-content"><ol class="usage-steps"><li>Install FastBuild and set up distributed compilation (broker/workers, <code class="usage-code">FASTBUILD_BROKER</code> and related env vars) so the broker is reachable.</li><li>Enable the <code class="usage-code">FastBuildController</code> plugin so shader compilation can use FastBuild&#x27;s distributed backend.</li><li>In project settings or <code class="usage-code">DefaultEngine.ini</code>, turn on shader compile distribution and specify the broker plus worker list (or multiple worker nodes).</li><li>Start some FastBuild worker nodes, then back in the editor trigger a shader compile (change a material, add a light, or run <code class="usage-code">RecompileShaders</code>).</li><li>Search the log for FastBuild/Broker lines to confirm tasks are dispatched to workers rather than compiled serially locally.</li><li>Compare shader-compile time before and after to confirm distribution works; if a node drops, check broker reachability and firewall first.</li></ol><p class="usage-note">It is shader-compile distribution, not an input controller; set up the broker/worker environment first to see tasks dispatch.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">FastBuildController</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/FastBuildController/FastBuildController.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
