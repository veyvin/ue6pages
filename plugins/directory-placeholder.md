---
layout: default
title: 目录占位符 / Directory Placeholder
---

<h1>目录占位符 / Directory Placeholder</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Developer/DirectoryPlaceholder/DirectoryPlaceholder.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">源代码控制</div><div class="lang-content">Source Control</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">DirectoryPlaceholder</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">Directory Placeholder</code> 提供一个占位资产类型，用来把「空文件夹」也纳入源码管理（空目录本身不会被提交）。</li><li>启用后（纯编辑器工具），在内容浏览器对着空文件夹右键 <code class="usage-code">Create Advanced Asset → Misc → Directory Placeholder</code>。</li><li>给占位资产命名，提交时它随文件夹一起进入 Perforce/Git，团队拉取后空目录结构得以保留。</li><li>当文件夹里真正有了内容，可以删掉占位资产，目录仍随其中的内容一起版本化。</li><li>它只在编辑器侧：别把 <code class="usage-code">DirectoryPlaceholder</code> 模块加进 Game Target，否则打包徒增依赖。</li></ol><p class="usage-note">占位资产只是为了让空目录进版本库；有内容后及时清理，避免无意义的资产堆积。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">Directory Placeholder</code> adds a placeholder asset type so even empty folders get tracked by source control (bare empty dirs are not committed).</li><li>After enabling (it is editor-only), right-click the empty folder in the Content Browser and pick <code class="usage-code">Create Advanced Asset → Misc → Directory Placeholder</code>.</li><li>Name the placeholder; on commit it enters Perforce/Git with the folder, preserving the empty directory structure for everyone who syncs.</li><li>Once the folder holds real content, delete the placeholder; the directory stays versioned alongside its contents.</li><li>It is editor-side only: never add the <code class="usage-code">DirectoryPlaceholder</code> module to a Game target, or packaging gains a needless dependency.</li></ol><p class="usage-note">The placeholder only exists to version an empty folder; clean it up once content lands to avoid clutter.</p></div></div></div>
    </div>

