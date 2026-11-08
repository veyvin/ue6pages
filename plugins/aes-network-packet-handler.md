---
layout: default
title: AES 网络数据包处理程序 / AES network packet handler
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">AES network packet handler</div>
      <div class="hero-title-cn">AES 网络数据包处理程序 · 提供数据包处理程序组件来执行 AES 加密和解密。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Misc</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/PacketHandlers/AESHandlerComponent/AESHandlerComponent.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">提供数据包处理程序组件来执行 AES 加密和解密。</div><div class="lang-content">Provides a packet handler component to do AES encryption and decryption.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：提供数据包处理程序组件来执行 AES 加密和解密。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：AESHandlerComponent。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Provides a packet handler component to do AES encryption and decryption.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: AESHandlerComponent. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">AES network packet handler</code>（模块 <code class="usage-code">AESHandlerComponent</code>）。</li><li>在两端 <code class="usage-code">DefaultEngine.ini</code> 的 <code class="usage-code">[PacketHandlerComponents]</code> 设置 <code class="usage-code">Components=AESHandlerComponent</code>（组件名与 GCM 插件不同）。</li><li>配置预共享 AES 密钥，保证 dedicated server 与客户端一致。</li><li>联机进关验证加密通道；该实现没有 GCM 那种认证标签。</li><li>不要在蓝图组件列表里搜索并添加这个 Handler。</li><li>能进 Shipping，但安全上更推荐改用 <code class="usage-code">AESGCMHandlerComponent</code>。</li></ol><p class="usage-note">旧版 AES 包处理，缺少 GCM 完整性校验，新项目应改用 AES-GCM。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">AES network packet handler</code> (module <code class="usage-code">AESHandlerComponent</code>).</li><li>Set <code class="usage-code">[PacketHandlerComponents]</code> <code class="usage-code">Components=AESHandlerComponent</code> in both ends’ <code class="usage-code">DefaultEngine.ini</code> (a different component name from the GCM plugin).</li><li>Configure a pre-shared AES key so dedicated server and clients match.</li><li>Join a networked session to verify the encrypted channel; this path has no GCM authentication tag.</li><li>Do not search Blueprint component lists to add this handler onto an actor.</li><li>It can ship, but <code class="usage-code">AESGCMHandlerComponent</code> is the stronger choice.</li></ol><p class="usage-note">Legacy AES packet encryption without GCM integrity; new projects should use AES-GCM instead.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AESHandlerComponent</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/PacketHandlers/AESHandlerComponent/AESHandlerComponent.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
