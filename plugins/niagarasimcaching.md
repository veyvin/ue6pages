---
layout: default
title: NiagaraSim 缓存 / NiagaraSimCaching
---

<h1>NiagaraSim 缓存 / NiagaraSimCaching</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/FX/NiagaraSimCaching/NiagaraSimCaching.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">外汇</div><div class="lang-content">FX</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">NiagaraSimCaching, NiagaraSimCachingEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">NiagaraSimCaching</code>（运行时 <code class="usage-code">NiagaraSimCaching</code>，编辑器 <code class="usage-code">NiagaraSimCachingEditor</code>）。</li><li>它为 Niagara 提供模拟缓存：把模拟结果烘成缓存再回放，省算力/可确定性。</li><li>对复杂效果先录制 Sim Cache，运行时播放缓存（Sequencer/玩法可用）。</li><li>Game 模块依赖运行时模块；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">Niagara 模拟缓存（烘缓存再回放，省算力/确定性）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">NiagaraSimCaching</code> (runtime <code class="usage-code">NiagaraSimCaching</code>, editor <code class="usage-code">NiagaraSimCachingEditor</code>).</li><li>It provides simulation caching for Niagara: bake the simulation to a cache, then play it back for perf/determinism.</li><li>Record a Sim Cache for a complex effect and play it back at runtime (usable in Sequencer/gameplay).</li><li>Game modules depend on runtime modules; editor modules go to Editor targets only.</li></ol><p class="usage-note">Niagara simulation caching (bake then replay for perf/determinism).</p></div></div></div>
    </div>

