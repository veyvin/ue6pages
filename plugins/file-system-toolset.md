---
layout: default
title: 文件系统工具集 / File System Toolset
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">F</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">File System Toolset</div>
      <div class="hero-title-cn">文件系统工具集 · 通过 AI Toolset Registry 读取文件、写入文本</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/FileSystemToolset/FileSystemToolset.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">通过 AI Toolset Registry 读取文件、写入文本并下载 HTTPS 资源。</div><div class="lang-content">Reads files, writes text, and downloads HTTPS resources through the AI Toolset Registry.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：通过 AI Toolset Registry 读取文件、写入文本并下载 HTTPS 资源。</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：FileSystemToolset, FileSystemToolsetTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Reads files, writes text, and downloads HTTPS resources through the AI Toolset Registry.</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: FileSystemToolset, FileSystemToolsetTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用实验性 <code class="usage-code">File System Toolset</code>（<code class="usage-code">FileSystemToolset</code>，测试 <code class="usage-code">FileSystemToolsetTests</code>），并打开 <code class="usage-code">Toolset Registry</code> / 编辑器 AI（MCP）会话。</li><li>助手应列出读文件、写文本、HTTPS 下载等工具；在对话里让它读取工程内一个已知文本路径，确认返回内容而不是通用「搜索 Details」。</li><li>写文本只应落在工具允许的工作区路径；让它改一个临时 <code class="usage-code">.txt</code> 后用资源管理器核对，不要授权整个磁盘根。</li><li>HTTPS 下载用于拉公开文档/清单，检查输出日志里的 URL 与落地文件；证书失败时看引擎 HTTP 模块，不是蓝图组件。</li><li><code class="usage-code">FileSystemToolsetTests</code> 只在自动化里跑。不要把 <code class="usage-code">FileSystemToolset</code> 写进游戏 <code class="usage-code">Build.cs</code>；Shipping 不需要 AI 读盘工具。</li></ol><p class="usage-note">给编辑器 AI 的读写/下载工具，不是 `IFileManager` 游戏存档 API。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable experimental <code class="usage-code">File System Toolset</code> (<code class="usage-code">FileSystemToolset</code>, tests <code class="usage-code">FileSystemToolsetTests</code>) and open <code class="usage-code">Toolset Registry</code> / an editor AI (MCP) session.</li><li>The assistant should list read-file, write-text, and HTTPS-download tools. Ask it to read a known in-project text path and confirm the contents — not a generic Details search.</li><li>Writes must stay inside allowed workspace paths. Have it patch a temp <code class="usage-code">.txt</code> and verify on disk; do not grant the whole drive root.</li><li>Use HTTPS download for a public doc/manifest; check Output Log URL and the saved file. Cert failures are the engine HTTP stack, not a Blueprint component.</li><li>Run <code class="usage-code">FileSystemToolsetTests</code> only under automation. Do not add <code class="usage-code">FileSystemToolset</code> to a game <code class="usage-code">Build.cs</code>; shipping games do not need AI disk tools.</li></ol><p class="usage-note">Editor-AI read/write/download tools, not `IFileManager` save-game APIs.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">FileSystemToolset</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">FileSystemToolsetTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/FileSystemToolset/FileSystemToolset.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
