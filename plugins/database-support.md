---
layout: default
title: 数据库支持 / Database Support
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">D</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Database Support</div>
      <div class="hero-title-cn">数据库支持 · 抽象数据库支持</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Database</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/Database/DatabaseSupport/DatabaseSupport.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">抽象数据库支持</div><div class="lang-content">Abstract Database Support</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：抽象数据库支持</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：DatabaseSupport。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Abstract Database Support</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: DatabaseSupport. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Database Support</code>（模块 <code class="usage-code">DatabaseSupport</code>）；这是抽象连接层，本身不带可视化查询窗口。</li><li>游戏或工具模块 <code class="usage-code">Build.cs</code> 依赖 <code class="usage-code">DatabaseSupport</code>，并同时启用具体后端（通常是 <code class="usage-code">SQLite</code> / SQLite Database 插件）以提供真正的 <code class="usage-code">FDataBaseConnection</code>。</li><li><code class="usage-code">#include</code> 数据库记录集头文件，通过后端工厂打开连接字符串（本地 <code class="usage-code">.db</code> 或配置的 DSN），拿到 <code class="usage-code">FDataBaseConnection</code>。</li><li>调用 <code class="usage-code">Execute</code> 跑 SQL，用 <code class="usage-code">FDataBaseRecordSet</code> 迭代列；把结果填进游戏结构体或编辑器报表，而不是在蓝图里搜同名组件。</li><li>错误路径检查连接失败和 SQL 返回码；只读查询与写库分开事务，避免把玩家存档和调试库混在一个文件。</li><li>包装进游戏时带上所选后端插件；仅启用 <code class="usage-code">DatabaseSupport</code> 而不接 SQLite 等实现，运行时没有可用驱动。</li></ol><p class="usage-note">抽象 DB API，必须搭配 SQLite 等具体插件才能真正连库。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Database Support</code> (module <code class="usage-code">DatabaseSupport</code>). It is an abstract connection layer and has no visual query window.</li><li>Depend on <code class="usage-code">DatabaseSupport</code> in your game/tool <code class="usage-code">Build.cs</code> and also enable a concrete backend (typically the SQLite Database plugin) that supplies <code class="usage-code">FDataBaseConnection</code>.</li><li>Include the record-set headers, open a connection string (local <code class="usage-code">.db</code> or configured DSN) through the backend factory, and obtain <code class="usage-code">FDataBaseConnection</code>.</li><li>Run SQL with <code class="usage-code">Execute</code>, iterate <code class="usage-code">FDataBaseRecordSet</code> columns, and copy rows into gameplay structs or editor reports — there is no same-named actor component.</li><li>Handle connect failures and SQL return codes; keep read queries and writes in separate transactions so player saves never share a debug database file.</li><li>Package the chosen backend with the game. Enabling only <code class="usage-code">DatabaseSupport</code> without SQLite (or another driver) leaves you with no runtime engine.</li></ol><p class="usage-note">Abstract DB API; pair it with SQLite or another driver or nothing connects.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">DatabaseSupport</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/Database/DatabaseSupport/DatabaseSupport.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
