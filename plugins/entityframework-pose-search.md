---
layout: default
title: EntityFramework 姿势搜索 / EntityFramework Pose Search
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">E</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">EntityFramework Pose Search</div>
      <div class="hero-title-cn">EntityFramework 姿势搜索 · EntityFramework 的姿势搜索集成。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Animation</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/EntityFrameworkPoseSearch/EntityFrameworkPoseSearch.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">EntityFramework 的姿势搜索集成。</div><div class="lang-content">Pose Search integration for EntityFramework.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：EntityFramework 的姿势搜索集成。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：EntityFrameworkPoseSearch。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Pose Search integration for EntityFramework.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: EntityFrameworkPoseSearch. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>同时启用 <code class="usage-code">EntityFramework</code> 与 <code class="usage-code">EntityFrameworkPoseSearch</code>（均为 Experimental，接口可能变），确保两者一起加载。</li><li>让实体使用 <code class="usage-code">EntitySkeletalAnimation</code> 组件承载骨骼动画，姿势搜索的输入就来自它的骨骼姿态。</li><li>创建 <code class="usage-code">Pose Search Database</code> 资产，把动画序列加入，并选匹配的 Schema/Channel 配置。</li><li>在实体侧构建查询（历史/轨迹、目标通道），把数据库接进实体的动画选择流程。</li><li>在 PIE 用 Pose Search 调试视图看选中的姿势，先在空关卡验证再进正式内容。</li></ol><p class="usage-note">这是 EntityFramework（ECS 式实体）体系里的姿势搜索；脱离 EntityFramework 的骨架动画它无从取数，纯 Actor 流程里不适用。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable both <code class="usage-code">EntityFramework</code> and <code class="usage-code">EntityFrameworkPoseSearch</code> (both Experimental — APIs may shift) so they load together.</li><li>Drive entities with the <code class="usage-code">EntitySkeletalAnimation</code> component; pose search reads from its skeletal pose.</li><li>Create a <code class="usage-code">Pose Search Database</code>, add animation sequences, and pick a matching Schema/Channel configuration.</li><li>Build the query on the entity side (history/trajectory, target channels) and wire the database into the entity&#x27;s animation selection.</li><li>Tune with the Pose Search debug view in PIE, proving it in an empty level before real content.</li></ol><p class="usage-note">This is pose search inside the EntityFramework entity (ECS-style) stack; it needs EntityFramework skeletal animation and doesn&#x27;t apply to a plain Actor workflow.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">EntityFrameworkPoseSearch</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/EntityFrameworkPoseSearch/EntityFrameworkPoseSearch.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
