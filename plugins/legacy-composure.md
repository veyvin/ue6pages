---
layout: default
title: 传统的沉着 / Legacy Composure
---

<h1>传统的沉着 / Legacy Composure</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Compositing/Composure/Composure.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">合成</div><div class="lang-content">Compositing</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">Composure, ComposureEditor, ComposureLayersEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">Legacy Composure</code> 是不再开发的遗留实时合成系统，新项目用 Composure（<code class="usage-code">CompositeCore</code>）方向的版本。</li><li>已有工程若仍依赖旧 Composure，按引擎提示迁移到新合成管线。</li><li>运行时依赖 <code class="usage-code">Composure</code>，编辑器模块 <code class="usage-code">ComposureEditor</code> / <code class="usage-code">ComposureLayersEditor</code> 只进 Editor Target。</li><li>迁移后尽量禁用本遗留插件，避免新旧合成并存。</li></ol><p class="usage-note">遗留实时合成系统，不再开发，迁移到新 Composure。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">Legacy Composure</code> is the no-longer-developed legacy real-time compositing system; new projects use the Composure (<code class="usage-code">CompositeCore</code>) path.</li><li>Existing projects still on old Composure should migrate to the new compositing pipeline as prompted.</li><li>Runtime depends on <code class="usage-code">Composure</code>; editor modules <code class="usage-code">ComposureEditor</code> / <code class="usage-code">ComposureLayersEditor</code> go to Editor targets only.</li><li>After migration, prefer disabling this legacy plugin so old and new compositing don&#x27;t coexist.</li></ol><p class="usage-note">The legacy real-time compositing system, no longer developed; migrate to the new Composure.</p></div></div></div>
    </div>

