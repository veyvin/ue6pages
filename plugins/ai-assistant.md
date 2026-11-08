---
layout: default
title: 人工智能助手 / AI Assistant
---

<h1>人工智能助手 / AI Assistant</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/AIAssistant/AIAssistant.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">其他</div><div class="lang-content">Other</div></div></span></li><li><span class="label">模块</span><span class="value">AIAssistant</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 插件 <code class="usage-code">AI Assistant</code>（模块 <code class="usage-code">AIAssistant</code>）并重启。</li><li>从编辑器 <code class="usage-code">Window</code> 菜单或工具栏打开 AI Assistant 聊天面板（编辑器内助手，不是 <code class="usage-code">AIModule</code> 行为树）。</li><li>按面板提示完成登录或模型选择后，针对当前资产、蓝图或关卡提问。</li><li>若要让助手调用工作区工具，再启用 <code class="usage-code">Agent Capability</code> 与 <code class="usage-code">Agent Plugin Toolset</code>。</li><li>官方 Description 为空，面板入口和 API 会变；不要把 <code class="usage-code">AIAssistant</code> 加进 Shipping。</li></ol><p class="usage-note">Experimental 编辑器助手，无稳定官方说明，不能当运行时游戏 AI。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">AI Assistant</code> (module <code class="usage-code">AIAssistant</code>) and restart.</li><li>Open the AI Assistant chat from the editor <code class="usage-code">Window</code> menu or toolbar (an in-editor assistant, not <code class="usage-code">AIModule</code> behavior trees).</li><li>Sign in or pick a model as the panel requires, then ask about the current asset, Blueprint, or level.</li><li>Enable <code class="usage-code">Agent Capability</code> and <code class="usage-code">Agent Plugin Toolset</code> as well if the assistant should call workspace tools.</li><li>Epic ships no Description; the panel and API can change — do not add <code class="usage-code">AIAssistant</code> to Shipping.</li></ol><p class="usage-note">Experimental in-editor assistant with no stable official description; it is not runtime game AI.</p></div></div></div>
    </div>

