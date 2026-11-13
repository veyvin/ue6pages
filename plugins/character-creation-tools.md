---
layout: default
title: 角色创建工具 / Character Creation Tools
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Character Creation Tools</div>
      <div class="hero-title-cn">角色创建工具 · 共享字符编辑工具和交互式工具框架外壳。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>MetaHuman</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">5</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/MetaHuman/CharacterCreationTools/CharacterCreationTools.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">共享字符编辑工具和交互式工具框架外壳。</div><div class="lang-content">Shared character editing tools and interactive tool framework shells.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：共享字符编辑工具和交互式工具框架外壳。</p><p>MetaHuman 家族：数字人生成、面捕、校准或运行时绑定，建立在 Control Rig / Live Link 之上。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：CharacterEditState, CharacterEditTools, CharacterEditInteractiveTools, CharacterEditToolsEditor, CharacterMeshConformer。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Shared character editing tools and interactive tool framework shells.</p><p>MetaHuman family: digital-human generation, face capture, calibration, or runtime, on Control Rig / Live Link.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: CharacterEditState, CharacterEditTools, CharacterEditInteractiveTools, CharacterEditToolsEditor, CharacterMeshConformer. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 MetaHuman 插件 <code class="usage-code">Character Creation Tools</code>（<code class="usage-code">CharacterEditState</code>、<code class="usage-code">CharacterEditTools</code>、<code class="usage-code">CharacterEditInteractiveTools</code>、<code class="usage-code">CharacterMeshConformer</code>、<code class="usage-code">CharacterEditToolsEditor</code>）。</li><li>打开或新建 MetaHuman <code class="usage-code">Character</code> 资产，进入角色编辑器视口；本插件提供共享编辑状态与 Interactive Tools Framework 外壳，不是单独的动画采样节点。</li><li>用视口里的交互工具刷体型、头部或服装参数；工具会话状态走 <code class="usage-code">CharacterEditState</code>，不要自己往 Actor 上挂同名组件当玩法。</li><li>需要把服装/配件贴合身体时走 <code class="usage-code">CharacterMeshConformer</code>：选目标骨骼网格与源网格，执行 conform，检查绑定与法线。</li><li>改完后从角色编辑器导出/更新骨骼网格与 Control Rig，再放到关卡或 Sequencer 里看绑定，而不是在 AnimBP 里“采样 Character Creation Tools 资产”。</li><li><code class="usage-code">CharacterEditToolsEditor</code> 只留在 Editor Target；运行时数字人播放依赖 MetaHuman 运行时绑定，不要把编辑工具链进 Shipping。</li></ol><p class="usage-note">给 MetaHuman 角色编辑器的共享工具壳，不是运行时角色控制器。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the MetaHuman plugin <code class="usage-code">Character Creation Tools</code> (<code class="usage-code">CharacterEditState</code>, <code class="usage-code">CharacterEditTools</code>, <code class="usage-code">CharacterEditInteractiveTools</code>, <code class="usage-code">CharacterMeshConformer</code>, <code class="usage-code">CharacterEditToolsEditor</code>).</li><li>Open or create a MetaHuman <code class="usage-code">Character</code> asset and enter the character editor viewport. This plugin is the shared edit-state and Interactive Tools Framework shell, not an AnimBP sampler.</li><li>Sculpt body/head/wardrobe with the viewport interactive tools; session state lives in <code class="usage-code">CharacterEditState</code>. Do not treat those types as gameplay components on a pawn.</li><li>Fit clothing or accessories with <code class="usage-code">CharacterMeshConformer</code>: pick target skeletal mesh and source mesh, run conform, then check skinning and normals.</li><li>Export/update the skeletal mesh and Control Rig from the character editor, then place that mesh in a level or Sequencer. Do not “sample a Character Creation Tools asset” on an animation track.</li><li>Keep <code class="usage-code">CharacterEditToolsEditor</code> on an Editor target. Runtime MetaHuman playback uses the runtime binding stack, not these authoring tools.</li></ol><p class="usage-note">Shared authoring shell for the MetaHuman character editor, not a runtime character controller.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (5)</div><div class="module-item"><span class="dot"></span><span class="name mono">CharacterEditState</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CharacterEditTools</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CharacterEditInteractiveTools</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CharacterEditToolsEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CharacterMeshConformer</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/MetaHuman/CharacterCreationTools/CharacterCreationTools.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
