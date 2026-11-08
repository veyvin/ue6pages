---
layout: default
title: 层次结构表 / Hierarchy Table
---

<h1>层次结构表 / Hierarchy Table</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/Animation/HierarchyTable/HierarchyTable.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">HierarchyTableRuntime, HierarchyTableEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Hierarchy Table</code>（运行时 <code class="usage-code">HierarchyTableRuntime</code>，编辑器 <code class="usage-code">HierarchyTableEditor</code>）。</li><li>用层级表数据结构组织成组的层级实体（如骨骼、变换树），表达父子关系。</li><li>在编辑器里用 <code class="usage-code">HierarchyTableEditor</code> 查看/编辑，运行时通过 Runtime 模块读写。</li><li>Experimental：接口可能变动；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">层级化数据表基础框架；动画等是它的专用类型扩展。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Hierarchy Table</code> (runtime <code class="usage-code">HierarchyTableRuntime</code>, editor <code class="usage-code">HierarchyTableEditor</code>).</li><li>Use the hierarchy-table data structure to organize grouped hierarchical entities (e.g. bones, transform trees) with parent/child relations.</li><li>Inspect/edit with <code class="usage-code">HierarchyTableEditor</code> in the editor; read/write at runtime via the Runtime module.</li><li>Experimental: contract may change; editor modules go to Editor targets only.</li></ol><p class="usage-note">The base hierarchical data-table framework; animation is a specialized type extension of it.</p></div></div></div>
    </div>

