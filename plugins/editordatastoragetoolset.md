---
layout: default
title: 编辑器数据存储工具集 / EditorDataStorageToolset
---

<h1>编辑器数据存储工具集 / EditorDataStorageToolset</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/Toolsets/EditorDataStorageToolset/EditorDataStorageToolset.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">其他</div><div class="lang-content">Other</div></div></span></li><li><span class="label">模块</span><span class="value">EditorDataStorageToolset</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">EditorDataStorageToolset</code> 并重启（Experimental）。</li><li>确认编辑器正在使用数据存储 (TEDS)，例如大纲视图背后的实体/行数据。</li><li>让编辑器 AI 助手通过工具集注册表调用该工具集的查询接口。</li><li>读取返回的实体与列数据，做只读检查（有哪些实体、每个实体有哪些字段）。</li><li>需要改动时改走其它写入路径，避免直接篡改 TEDS。</li></ol><p class="usage-note">这是给编辑器 AI 助手用的只读/查询工具集，用来检查运行时 TEDS；Experimental，不进 Shipping 游戏。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">EditorDataStorageToolset</code> and restart (Experimental).</li><li>Confirm the editor is using the Data Storage (TEDS), e.g. the entity/row data behind the Outliner.</li><li>Have the in-editor AI assistant call this toolset&#x27;s query API through the Toolset Registry.</li><li>Read the returned entities and columns for read-only inspection (which entities exist and which fields each has).</li><li>Route any changes through other write paths instead of mutating TEDS directly.</li></ol><p class="usage-note">A read/query toolset for the in-editor AI assistant to inspect TEDS at runtime; Experimental and not a shipping game feature.</p></div></div></div>
    </div>

