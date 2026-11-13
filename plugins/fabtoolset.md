---
layout: default
title: 晶圆厂工具集 / FabToolset
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">F</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">FabToolset</div>
      <div class="hero-title-cn">晶圆厂工具集 · 允许助手列出用户在 Fab 上拥有的资产并将其安装到正在运行的编</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Experimental</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/FabToolset/FabToolset.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">允许助手列出用户在 Fab 上拥有的资产并将其安装到正在运行的编辑器中的工具</div><div class="lang-content">Tools allowing the assistant to list the assets a user owns on Fab and install them into the running editor</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：允许助手列出用户在 Fab 上拥有的资产并将其安装到正在运行的编辑器中的工具</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：FabToolset。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Tools allowing the assistant to list the assets a user owns on Fab and install them into the running editor</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: FabToolset. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">FabToolset</code> 是给编辑器内 AI 助手用的工具集，启用后助手才有权限列出你 Fab 账号拥有的资产并安装。</li><li>在带 AI 助手的编辑器会话里，让助手「列出我 Fab 上拥有的资产」，确认它返回的是你账号下的资产清单。</li><li>选定某个资产后，让助手「把这个资产安装到当前编辑器」，观察它下载并导入到内容浏览器。</li><li>安装完成后在内容浏览器核对资产是否真正落地；若是插件类资产，再到 <code class="usage-code">编辑 &gt; 插件</code> 启用并重启。</li><li>因为它是 Experimental 工具，先在测试项目里跑通整条安装链路，再用于正式项目。</li><li>它只服务编辑器自动化流程，打包游戏时不必把它当作运行时依赖。</li></ol><p class="usage-note">为 AI 助手开后门去列/装 Fab 资产；Experimental，先在测试项目验证安装链路。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">FabToolset</code> is a toolset for the in-editor AI assistant. Enable it so the assistant is allowed to list the assets your Fab account owns and install them.</li><li>In an editor session with the AI assistant, ask it to list the assets you own on Fab and confirm it returns your account&#x27;s asset list.</li><li>Pick an asset and ask the assistant to install it into the running editor, then watch it download and import into the Content Browser.</li><li>After installation, verify the asset actually landed in the Content Browser; if it is a plugin, enable it under <code class="usage-code">Edit &gt; Plugins</code> and restart.</li><li>Because it is an Experimental tool, run the full install path in a test project before using it on a production project.</li><li>It serves editor automation only; you do not need it as a runtime dependency when packaging the game.</li></ol><p class="usage-note">Grants the AI assistant the ability to list/install Fab assets. Experimental — validate the install path in a test project first.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">FabToolset</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/FabToolset/FabToolset.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
