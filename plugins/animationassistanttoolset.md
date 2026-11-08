---
layout: default
title: 动画助手工具集 / AnimationAssistantToolset
---

<h1>动画助手工具集 / AnimationAssistantToolset</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/Toolsets/AnimationAssistantToolset/AnimationAssistantToolset.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">其他</div><div class="lang-content">Other</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏</div><div class="lang-content">Epic Games</div></div></span></li><li><span class="label">模块</span><span class="value">AnimationAssistantToolset</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental <code class="usage-code">AnimationAssistantToolset</code>，并确保 <code class="usage-code">Toolset Registry</code>（以及要用的 MCP / AI Assistant）已开。</li><li>在编辑器 AI 助手或外部 MCP 客户端里选用 Animation 工具集，而不是自己往关卡里拖组件。</li><li>用该工具集提供的 Control Rig / Sequencer / <code class="usage-code">LevelSequence</code> 接口建序列、加绑定、改 Rig 层次（对应 <code class="usage-code">animation_toolset</code> 下的 Sequencer 与 Control Rig 工具）。</li><li>操作后在 Sequencer 与 Control Rig 编辑器核对轨道/骨骼是否写回资产。</li><li>不要把 <code class="usage-code">AnimationAssistantToolset</code> 加入 Game Target 或 Shipping；它只给助手自动化。</li></ol><p class="usage-note">Experimental Toolset：给编辑器 AI/自动化的读写工具，不是运行时动画系统。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">AnimationAssistantToolset</code> and keep <code class="usage-code">Toolset Registry</code> (plus MCP / AI Assistant if you use them) on.</li><li>Pick the Animation toolset in the in-editor assistant or an external MCP client — do not drop a component into the level.</li><li>Drive Control Rig, Sequencer, and <code class="usage-code">LevelSequence</code> through those tools (create sequences, add bindings, edit rig hierarchy — the <code class="usage-code">animation_toolset</code> Sequencer and Control Rig tools).</li><li>After a call, confirm tracks/bones actually landed in Sequencer and the Control Rig editor.</li><li>Do not add <code class="usage-code">AnimationAssistantToolset</code> to a Game target or shipping build; it is assistant automation only.</li></ol><p class="usage-note">Experimental toolset for the editor AI/automation, not a runtime animation system.</p></div></div></div>
    </div>

