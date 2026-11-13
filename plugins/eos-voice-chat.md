---
layout: default
title: EOS语音聊天 / EOS Voice Chat
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">E</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">EOS Voice Chat</div>
      <div class="hero-title-cn">EOS语音聊天 · IVoiceChat 集成 EOS 语音服务</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Online Platform</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Online/VoiceChat/EOSVoiceChat/EOSVoiceChat.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">IVoiceChat 集成 EOS 语音服务</div><div class="lang-content">IVoiceChat integration of the EOS Voice service</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：IVoiceChat 集成 EOS 语音服务</p><p>属于在线子系统 / 平台服务。</p><p>它打包的模块包括：EOSVoiceChat。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: IVoiceChat integration of the EOS Voice service</p><p>Part of Online Subsystem / platform services.</p><p>It ships these modules: EOSVoiceChat. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">EOS Voice Chat</code>，并确保 <code class="usage-code">OnlineSubsystemEOS</code> 与 EOS SDK 已配置可用。</li><li>在 <code class="usage-code">DefaultEngine.ini</code> 配置 EOS 语音（语音实现、EOS 凭证、<code class="usage-code">[EOSVoiceChat]</code> 相关项），客户端与服务端都启用。</li><li>用 <code class="usage-code">IVoiceChat</code> 接口或 VoiceChat 子系统先 <code class="usage-code">Login</code> 到 EOS 用户，再 <code class="usage-code">JoinChannel</code>（队伍/大厅频道）。</li><li>蓝图里可用 Voice Chat 的 <code class="usage-code">UVoiceChatUserComponent</code> 及相关节点做登录、加入频道、静音、设置输入设备。</li><li>用通道/发送设置控制只在对局内说话，离开时 <code class="usage-code">LeaveChannel</code>。</li><li>起两个客户端 PIE 或多机联机，确认频道内能互相听到，并验证静音/断线行为。</li></ol><p class="usage-note">语音走 IVoiceChat → EOS 语音服务这条链；凭证和频道模型配错时，最常见现象是登录成功但频道里没声音。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">EOS Voice Chat</code> and make sure <code class="usage-code">OnlineSubsystemEOS</code> plus the EOS SDK are configured and working.</li><li>Configure EOS voice in <code class="usage-code">DefaultEngine.ini</code> (voice implementation, EOS credentials, <code class="usage-code">[EOSVoiceChat]</code> entries) and enable it on both client and server.</li><li>Use the <code class="usage-code">IVoiceChat</code> interface or VoiceChat subsystem to <code class="usage-code">Login</code> the EOS user, then <code class="usage-code">JoinChannel</code> (team/lobby channel).</li><li>In Blueprint use the Voice Chat <code class="usage-code">UVoiceChatUserComponent</code> and nodes for login, joining, muting, and setting the input device.</li><li>Use channel/transmit settings so players only talk in-match, and <code class="usage-code">LeaveChannel</code> when leaving.</li><li>Launch two PIE clients or a networked session, confirm players hear each other, and verify mute/disconnect behavior.</li></ol><p class="usage-note">Voice flows through IVoiceChat -&gt; EOS voice service; the classic symptom of a bad credential/channel setup is a successful login with no audio in the channel.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">EOSVoiceChat</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Online/VoiceChat/EOSVoiceChat/EOSVoiceChat.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
