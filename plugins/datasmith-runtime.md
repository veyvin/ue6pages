---
layout: default
title: 数据史密斯运行时 / Datasmith Runtime
---

<h1>数据史密斯运行时 / Datasmith Runtime</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/Enterprise/DatasmithRuntime/DatasmithRuntime.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">其他</div><div class="lang-content">Other</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">DatasmithRuntime</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">Datasmith Runtime</code> 让你在打包后的游戏运行时加载 Datasmith 内容，而不是在编辑器里预先导入。</li><li>启用插件，并在 <code class="usage-code">DefaultEngine.ini</code> 里把 Datasmith 运行时加载相关设置指向该实现。</li><li>在蓝图里取 Datasmith Runtime 子系统，调用加载 <code class="usage-code">.udatasmith</code> 的节点，指定文件 URL/路径与导出到场景的方式。</li><li>监听加载完成回调，再对生成的对象做材质覆盖、坐标校正和碰撞设置。</li><li>它是 Experimental：先用空关卡验证加载耗时与内存峰值，再接入正式关卡流。</li></ol><p class="usage-note">运行时加载在并发/线程上更敏感；正式项目里必须评估大场景加载卡顿与内存峰值。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">Datasmith Runtime</code> loads Datasmith content while the packaged game runs, instead of importing ahead of time in the editor.</li><li>Enable the plugin and point the Datasmith runtime-loading settings in <code class="usage-code">DefaultEngine.ini</code> at this implementation.</li><li>In Blueprint, grab the Datasmith Runtime subsystem and call its load-<code class="usage-code">.udatasmith</code> node with the file URL/path and the spawn-into-scene mode.</li><li>Hook the completion callback, then apply material overrides, coordinate fixes, and collision setup to the spawned objects.</li><li>It is Experimental: validate load time and peak memory in an empty level before wiring it into live level streaming.</li></ol><p class="usage-note">Runtime loading is sensitive to concurrency and threading; profile hitching and peak memory for large scenes before shipping.</p></div></div></div>
    </div>

