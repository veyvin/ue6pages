---
layout: default
title: WinInet
---

<!-- ai-generation-failed -->

<h1>WinInet</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Windows/WinInet/WinInet.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>

    <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>WinInet 是引擎源码中的模块，具体职责以描述符和源码为准。</p><p>这是第三方库的 UBT 封装，通常由上层引擎模块使用，而不是游戏直接依赖。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>WinInet is an engine module whose job is defined by its descriptor and source.</p><p>This is a UBT wrapper around a third-party library; engine modules consume it, games rarely depend on it directly.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">WinInet</code>（Win Inet）：它是对一个第三方库的 UBT 封装，向引擎暴露该库的功能。位于 <code class="usage-code">Engine</code>，构建规则 <code class="usage-code">Engine/Source/ThirdParty/Windows/WinInet/WinInet.Build.cs</code>。描述符未声明依赖。</li><li>部署：<code class="usage-code">WinInet</code> 第三方库封装，优先依赖引擎已包好的上层模块。</li><li>怎么用：一般不要直接依赖它；优先用引擎里已封装好该库的上层模块。确需使用时把本模块加进 Build.cs，并包含其第三方头文件。</li><li>依赖：在 <code class="usage-code">YourModule.Build.cs</code> 加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;WinInet&quot; });</code>；对外暴露 <code class="usage-code">WinInet</code> 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。</li><li>调用：不要 include 引擎模块头去用它；优先用引擎里封装该库的上层模块，仅必要时包含 ThirdParty 目录下的第三方头文件。</li></ol><p class="usage-note">`WinInet`：它是对一个第三方库的 UBT 封装，向引擎暴露该库的功能；构建规则 `Engine/Source/ThirdParty/Windows/WinInet/WinInet.Build.cs`，直接依赖 0 个模块。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">WinInet</code> (Win Inet): it wraps a third-party library and exposes its functionality to the engine. Located under <code class="usage-code">Engine</code>; build rule <code class="usage-code">Engine/Source/ThirdParty/Windows/WinInet/WinInet.Build.cs</code>. The descriptor declares no dependencies.</li><li>Placement: <code class="usage-code">WinInet</code> is a third-party library wrapper; prefer the engine module that wraps it.</li><li>How to use: usually do not depend on it directly; prefer the engine module that already wraps it. If truly needed, add it to Build.cs and include the third-party headers.</li><li>Depend: in <code class="usage-code">YourModule.Build.cs</code> add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;WinInet&quot; });</code>. Use Public when exposing <code class="usage-code">WinInet</code> types, Private if only calling it; then Generate Project Files and rebuild.</li><li>Call: do not include engine module headers to use it; use the engine module that wraps this library, and only include its ThirdParty headers when truly needed.</li></ol><p class="usage-note">`WinInet`: it wraps a third-party library and exposes its functionality to the engine; build rule `Engine/Source/ThirdParty/Windows/WinInet/WinInet.Build.cs`; depends on 0 modules.</p></div></div></div>
    </div>

