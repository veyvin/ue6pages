---
layout: default
title: 默认安装包管理器 / Default Install Bundle Manager
---

<h1>默认安装包管理器 / Default Install Bundle Manager</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/DefaultInstallBundleManager/DefaultInstallBundleManager.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">DefaultInstallBundleManager</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">Default Install Bundle Manager</code> 是 <code class="usage-code">InstallBundleManager</code> 的默认实现，运行时负责下载、打补丁并挂载内容包（chunk）。</li><li>在 <code class="usage-code">DefaultGame.ini</code> 的 <code class="usage-code">[/Script/InstallBundleManager.InstallBundleManager]</code> 配置安装来源（如 HTTPChunkInstall）与 bundle 定义。</li><li>启用插件后，通过 <code class="usage-code">UInstallBundleManager</code> 子系统调用 <code class="usage-code">RequestAsyncInstallBundle</code> 下载指定 bundle，并轮询进度。</li><li>下载完成后调用挂载接口把 chunk 内容加载进来，再用资源引用或 <code class="usage-code">MountPak</code> 取用其中的资产。</li><li>这是 Experimental 的平台级 API：先在目标平台验证分块、断点续传与挂载行为，再接入正式内容分发。</li></ol><p class="usage-note">bundle 定义与打包 chunk 规则必须和 `DefaultGame.ini` 对齐，否则运行时会找不到要下载的分块。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">Default Install Bundle Manager</code> is the default <code class="usage-code">InstallBundleManager</code> implementation that downloads, patches, and mounts content bundles (chunks) at runtime.</li><li>Configure install sources (e.g. HTTPChunkInstall) and bundle definitions under <code class="usage-code">[/Script/InstallBundleManager.InstallBundleManager]</code> in <code class="usage-code">DefaultGame.ini</code>.</li><li>After enabling, call <code class="usage-code">RequestAsyncInstallBundle</code> on the <code class="usage-code">UInstallBundleManager</code> subsystem to download a named bundle and poll its progress.</li><li>When the download completes, call the mount interface to load the chunk content, then reference assets from it or <code class="usage-code">MountPak</code>.</li><li>This is an Experimental platform-level API: verify chunking, resume, and mounting on the target platform before wiring it into real content delivery.</li></ol><p class="usage-note">Bundle definitions must match your chunk packaging rules in `DefaultGame.ini`, or the runtime can&#x27;t find the chunks to download.</p></div></div></div>
    </div>

