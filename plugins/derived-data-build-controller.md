---
layout: default
title: 派生数据构建控制器 / Derived Data Build Controller
---

<h1>派生数据构建控制器 / Derived Data Build Controller</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/DerivedDataBuildController/DerivedDataBuildController.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">构建分布</div><div class="lang-content">Build Distribution</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">DerivedDataBuildController</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">Derived Data Build Controller</code> 让着色器编译分发到多台机器，统一走 Derived Data Build（<code class="usage-code">UE::DerivedData</code>）API。</li><li>启用插件，并在工程/项目设置里把 Derived Data Build 的后端指向远程构建控制器。</li><li>配置 worker 主机列表与通信协议，让编辑器把 DDC/着色器任务交给 Build Controller 调度。</li><li>首次编译时查看 UnrealBuildTool 与 Derived Data 日志，确认任务确实分发到 worker 而不是本地执行。</li><li>把构建产物写入共享 DDC 供团队复用；清理缓存后对比本地编译与分发编译的耗时差异。</li></ol><p class="usage-note">分发编译的正确性取决于所有 worker 的引擎/着色器版本一致；版本漂移会产出错误缓存。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">Derived Data Build Controller</code> distributes shader compilation across machines through the Derived Data Build (<code class="usage-code">UE::DerivedData</code>) API.</li><li>Enable the plugin and point the Derived Data Build backend at the remote build controller in project/engine settings.</li><li>Configure the worker host list and transport, so the editor hands DDC/shader jobs to the Build Controller for scheduling.</li><li>On the first compile, inspect the UnrealBuildTool and Derived Data logs to confirm jobs actually ran on workers, not locally.</li><li>Write build output into a shared DDC for the team; after clearing the cache, compare local vs. distributed compile times.</li></ol><p class="usage-note">Distributed correctness depends on identical engine/shader versions across workers; drift produces poisoned cache entries.</p></div></div></div>
    </div>

