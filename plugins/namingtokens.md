---
layout: default
title: 命名令牌 / NamingTokens
---

<h1>命名令牌 / NamingTokens</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Developer/NamingTokens/NamingTokens.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">编辑</div><div class="lang-content">Editor</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">NamingTokens, NamingTokensUI, NamingTokensUncookedOnly, NamingTokensEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用编辑器插件 <code class="usage-code">NamingTokens</code>（模块 <code class="usage-code">NamingTokens</code>、<code class="usage-code">NamingTokensUI</code>、<code class="usage-code">NamingTokensUncookedOnly</code>，编辑器 <code class="usage-code">NamingTokensEditor</code>）并重启。</li><li>它定义可在字符串求值期间识别的标记（token），用于命名模板（如资产/关卡命名）。</li><li>在命名规则里插入 token，按当前上下文动态展开。</li><li>这是编辑器/开发者插件，只进 Editor Target，不进 Shipping。</li></ol><p class="usage-note">字符串求值时识别的命名 token（命名模板用），编辑器向。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the editor plugin <code class="usage-code">NamingTokens</code> (modules <code class="usage-code">NamingTokens</code>, <code class="usage-code">NamingTokensUI</code>, <code class="usage-code">NamingTokensUncookedOnly</code>, editor <code class="usage-code">NamingTokensEditor</code>) and restart.</li><li>It defines tokens recognized during string evaluation, for naming templates (asset/level naming).</li><li>Insert tokens into naming rules to expand dynamically per current context.</li><li>It is an editor/developer plugin for Editor targets only; it does not ship.</li></ol><p class="usage-note">Tokens recognized during string evaluation for naming templates, editor-oriented.</p></div></div></div>
    </div>

