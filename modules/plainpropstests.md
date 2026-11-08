---
layout: default
title: PlainPropsTests
---

<!-- ai-generation-failed -->

<h1>PlainPropsTests</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/PlainPropsTests/PlainPropsTests.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>TestModuleRules</code></span></li>
  </ul>
</div>

    <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>PlainPropsTests 是引擎源码中的模块，具体职责以描述符和源码为准。</p><p>这是引擎源码里的一个 UBT 模块，通过 Build.cs 被其他模块依赖。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>PlainPropsTests is an engine module whose job is defined by its descriptor and source.</p><p>This is a UBT module in engine source that other modules depend on via Build.cs.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>用途：<code class="usage-code">PlainPropsTests</code> 位于 <code class="usage-code">Engine</code>，构建规则 <code class="usage-code">Engine/Source/Programs/PlainPropsTests/PlainPropsTests.Build.cs</code>。描述符未声明依赖。</li><li>依赖：在 <code class="usage-code">YourModule.Build.cs</code> 加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;PlainPropsTests&quot; });</code>；对外暴露 <code class="usage-code">PlainPropsTests</code> 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。</li><li>部署：<code class="usage-code">PlainPropsTests</code> 是运行时模块，可进游戏包；只在真正调用其 API 的模块里声明依赖。</li><li>调用：#include 其 Public 头（常见 <code class="usage-code">PlainPropsTests.h</code> / <code class="usage-code">PlainPropsTestsModule.h</code>），再用 <code class="usage-code">FModuleManager::LoadModulePtr&lt;PlainPropsTestsModule&gt;</code> 或直接使用导出类型。</li><li>传递依赖：<code class="usage-code">PlainPropsTests</code> 未声明额外公开依赖，通常只依赖引擎基础层。</li></ol><p class="usage-note">`PlainPropsTests` 的构建规则位于 `Engine/Source/Programs/PlainPropsTests/PlainPropsTests.Build.cs`，直接依赖 0 个模块，分类 Module。</p></div><div class="lang-content"><ol class="usage-steps"><li>Purpose: <code class="usage-code">PlainPropsTests</code> lives under <code class="usage-code">Engine</code>; build rule <code class="usage-code">Engine/Source/Programs/PlainPropsTests/PlainPropsTests.Build.cs</code>.The descriptor declares no dependencies.</li><li>Depend: in <code class="usage-code">YourModule.Build.cs</code> add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;PlainPropsTests&quot; });</code>. Use Public when exposing <code class="usage-code">PlainPropsTests</code> types, Private if only calling it; then Generate Project Files and rebuild.</li><li>Placement: <code class="usage-code">PlainPropsTests</code> is a runtime module and can ship. Depend on it only where you call its API.</li><li>Call: include Public headers (often <code class="usage-code">PlainPropsTests.h</code> / <code class="usage-code">PlainPropsTestsModule.h</code>), then use <code class="usage-code">FModuleManager::LoadModulePtr&lt;PlainPropsTestsModule&gt;</code> or the exported types directly.</li><li>Transitive deps: <code class="usage-code">PlainPropsTests</code> declares no extra public deps; it typically relies on engine basics.</li></ol><p class="usage-note">`PlainPropsTests` build rule is `Engine/Source/Programs/PlainPropsTests/PlainPropsTests.Build.cs`; depends on 0 modules; category Module.</p></div></div></div>
    </div>

