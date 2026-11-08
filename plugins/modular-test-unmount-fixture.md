---
layout: default
title: 模块化测试卸载夹具 / Modular Test Unmount Fixture
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Modular Test Unmount Fixture</div>
      <div class="hero-title-cn">模块化测试卸载夹具 · 框架自测试安装和卸载的惰性夹具。不是测试同伴；不包含任何测试。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Testing</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Tests/ModularTestUnmountFixture/ModularTestUnmountFixture.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">框架自测试安装和卸载的惰性夹具。不是测试同伴；不包含任何测试。</div><div class="lang-content">Inert fixture the framework self-tests mount and unmount. Not a test companion; contains no tests.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：框架自测试安装和卸载的惰性夹具。不是测试同伴；不包含任何测试。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：ModularTestUnmountFixture。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Inert fixture the framework self-tests mount and unmount. Not a test companion; contains no tests.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: ModularTestUnmountFixture. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Modular Test Unmount Fixture</code>（模块 <code class="usage-code">ModularTestUnmountFixture</code>）。</li><li>它是框架自测试用的“惰性夹具”（mount/unmount 会被自测挂载/卸载），本身不含任何测试。</li><li>无需手动跑；由框架自测使用。</li><li>这是测试夹具，不要当测试套件用。</li></ol><p class="usage-note">框架自测用的惰性 mount/unmount 夹具（不含测试）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Modular Test Unmount Fixture</code> (module <code class="usage-code">ModularTestUnmountFixture</code>).</li><li>It is an inert fixture the framework self-tests mount and unmount; it contains no tests itself.</li><li>No need to run it manually; the framework self-tests use it.</li><li>It is a test fixture, not a test suite.</li></ol><p class="usage-note">An inert mount/unmount fixture for framework self-tests (contains no tests).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">ModularTestUnmountFixture</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Tests/ModularTestUnmountFixture/ModularTestUnmountFixture.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
