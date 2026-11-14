---
layout: default
title: 蓝图图形格式化程序 / Blueprint Graph Formatter
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">B</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Blueprint Graph Formatter</div>
      <div class="hero-title-cn">蓝图图形格式化程序 · 根据团队编码标准格式化蓝图图表：从左到右执行、直线、放置输入、安</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Experimental</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/BlueprintGraphFormatter/BlueprintGraphFormatter.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">根据团队编码标准格式化蓝图图表：从左到右执行、直线、放置输入、安装注释框、堆叠事件块。在图表中按 G（在键盘快捷键下重新绑定）。</div><div class="lang-content">Formats Blueprint graphs to the team coding standard: left-to-right execution, straight wires, placed inputs, fitted comment boxes, stacked event blocks. Press G in a graph (rebind under Keyboard Shortcuts).</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：根据团队编码标准格式化蓝图图表：从左到右执行、直线、放置输入、安装注释框、堆叠事件块。在图表中按 G（在键盘快捷键下重新绑定）。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：BlueprintGraphFormatter, BlueprintGraphFormatterToolset。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Formats Blueprint graphs to the team coding standard: left-to-right execution, straight wires, placed inputs, fitted comment boxes, stacked event blocks. Press G in a graph (rebind under Keyboard Shortcuts).</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: BlueprintGraphFormatter, BlueprintGraphFormatterToolset. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在 <code class="usage-code">Edit &gt; Plugins</code> 启用实验性 <code class="usage-code">Blueprint Graph Formatter</code>（模块 <code class="usage-code">BlueprintGraphFormatter</code>、<code class="usage-code">BlueprintGraphFormatterToolset</code>）并重启。</li><li>打开任意蓝图的 Event Graph 或函数图，确认图中已有执行链、输入参数节点和注释框。</li><li>在图表内按 <code class="usage-code">G</code>：插件会把执行排成从左到右、拉直连线、摆放输入、收缩注释框并堆叠事件块。</li><li>若快捷键冲突，到 <code class="usage-code">Edit &gt; Editor Preferences &gt; Keyboard Shortcuts</code> 搜索 Graph Formatter / Format Blueprint Graph，改绑后再格式化。</li><li>先框选一小段乱线图验证规则，再对整张图按 <code class="usage-code">G</code>；逻辑不变，只改节点坐标与线型。</li><li>编辑器 AI 助手若已接 Toolset，可通过 <code class="usage-code">BlueprintGraphFormatterToolset</code> 对同一套排版规则做自动格式化；不要把这两个模块加进游戏 <code class="usage-code">Build.cs</code>。</li></ol><p class="usage-note">Experimental：只整理布局，不改编译结果。快捷键默认 `G`，可在 Keyboard Shortcuts 重绑。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable experimental <code class="usage-code">Blueprint Graph Formatter</code> in <code class="usage-code">Edit &gt; Plugins</code> (modules <code class="usage-code">BlueprintGraphFormatter</code>, <code class="usage-code">BlueprintGraphFormatterToolset</code>) and restart.</li><li>Open a Blueprint Event Graph or function graph that already has execution wires, input nodes, and comment boxes.</li><li>Press <code class="usage-code">G</code> in the graph: execution is laid out left-to-right, wires straightened, inputs placed, comment boxes fitted, and event blocks stacked.</li><li>If <code class="usage-code">G</code> conflicts, rebind under <code class="usage-code">Edit &gt; Editor Preferences &gt; Keyboard Shortcuts</code> (Graph Formatter / Format Blueprint Graph) and format again.</li><li>Prove the rules on a small selection before formatting the whole graph; node logic is untouched, only layout.</li><li>Editor AI assistants can reuse the same rules through <code class="usage-code">BlueprintGraphFormatterToolset</code>. Do not add either module to a game <code class="usage-code">Build.cs</code>.</li></ol><p class="usage-note">Experimental: layout only, no compile-behavior change. Default hotkey is `G`; rebind in Keyboard Shortcuts.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">BlueprintGraphFormatter</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">BlueprintGraphFormatterToolset</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/BlueprintGraphFormatter/BlueprintGraphFormatter.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
