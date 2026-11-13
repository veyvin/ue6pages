import axios from 'axios'

export const api = axios.create({
  baseURL: '/api',
  timeout: 60000,
})

/* ===== TEMP MOCK START ===== */
const MOCK = (() => {
  const cats = ['Audio', 'Render', 'Editor', 'Networking', 'AI', 'Media']
  const slug = (n) => n.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')
  const P = [
    ['AudioSynesthesia', 'Audio', 'Suite of tools to profile, debug, and monitor aspects of audio in the Unreal Engine.', 'Engine/Plugins/Runtime/AudioSynesthesia/AudioSynesthesia.uplugin'],
    ['Metasound', 'Audio', 'MetaSounds 是 UE5 的新一代程序化音频渲染系统，支持从音频图生成实时声音。', 'Engine/Plugins/Runtime/Metasound/Metasound.uplugin'],
    ['Quartz', 'Audio', 'Sample-accurate, multiplatform audio scheduling, quantization and signal processing.', 'Engine/Plugins/Runtime/Quartz/Quartz.uplugin'],
    ['Soundscape', 'Audio', 'Framework for creating spatially aware, responsive ambient soundscapes.', 'Engine/Plugins/Runtime/Soundscape/Soundscape.uplugin'],
    ['Lumen', 'Render', 'Fast dynamic global illumination and reflections for next-gen visuals.', 'Engine/Plugins/Renderer/Lumen/Lumen.uplugin'],
    ['Nanite', 'Render', 'Virtualized geometry system that renders billions of triangles at real-time framerates.', 'Engine/Plugins/Renderer/Nanite/Nanite.uplugin'],
    ['Niagara', 'Render', 'Powerful VFX system for particle simulation, fluid and mesh effects.', 'Engine/Plugins/FX/Niagara/Niagara.uplugin'],
    ['Substrate', 'Render', 'Expressive material authoring with layering, blending and physically based shading.', 'Engine/Plugins/Renderer/Substrate/Substrate.uplugin'],
    ['ControlRig', 'Editor', 'Rigging and animation toolset with graph-based control hierarchies.', 'Engine/Plugins/Animation/ControlRig/ControlRig.uplugin'],
    ['Sequencer', 'Editor', 'Cinematic and gameplay authoring with tracks, curves and keys.', 'Engine/Plugins/MovieScene/Sequencer/Sequencer.uplugin'],
    ['MetaHuman', 'Editor', 'Create and animate photorealistic digital humans from a single mesh.', 'Engine/Plugins/MetaHuman/MetaHuman.uplugin'],
    ['PCG', 'Editor', 'Procedural content generation framework driven by node graphs.', 'Engine/Plugins/Experimental/PCG/PCG.uplugin'],
    ['ReplicationGraph', 'Networking', 'Scalable replication architecture for large-scale multiplayer worlds.', 'Engine/Plugins/Runtime/ReplicationGraph/ReplicationGraph.uplugin'],
    ['NetworkPrediction', 'Networking', 'Deterministic, rollback-friendly client-side prediction framework.', 'Engine/Plugins/Runtime/NetworkPrediction/NetworkPrediction.uplugin'],
    ['OnlineSubsystemEOS', 'Networking', 'Epic Online Services integration for sessions, lobbies, friends and achievements.', 'Engine/Plugins/Online/OnlineSubsystemEOS/OnlineSubsystemEOS.uplugin'],
    ['NNERuntimeOrt', 'AI', 'ONNX Runtime neural network inference for editor and runtime.', 'Engine/Plugins/Experimental/NNERuntimeOrt/NNERuntimeOrt.uplugin'],
    ['LearningAgents', 'AI', 'Reinforcement learning agents powered by in-engine neural network training.', 'Engine/Plugins/Experimental/LearningAgents/LearningAgents.uplugin'],
    ['ElectraPlayer', 'Media', 'Hardware-accelerated streaming video decoder for adaptive playback.', 'Engine/Plugins/Media/ElectraPlayer/ElectraPlayer.uplugin'],
    ['WmfMedia', 'Media', 'Windows Media Foundation based media player implementation.', 'Engine/Plugins/Media/WmfMedia/WmfMedia.uplugin'],
    ['AjaMedia', 'Media', 'Professional SDI/NDI capture and output for broadcast pipelines.', 'Engine/Plugins/Media/AjaMedia/AjaMedia.uplugin'],
  ]
  const M = [
    ['Core', 'Runtime', 'Engine/Core/Core.Build.cs', ['CoreUObject']],
    ['CoreUObject', 'Runtime', 'Engine/CoreUObject/CoreUObject.Build.cs', []],
    ['Engine', 'Runtime', 'Engine/Engine/Engine.Build.cs', ['Core', 'CoreUObject', 'RenderCore', 'RHI']],
    ['RenderCore', 'Runtime', 'Engine/RenderCore/RenderCore.Build.cs', ['RHI']],
    ['RHI', 'Runtime', 'Engine/RHI/RHI.Build.cs', ['Core']],
    ['Slate', 'Runtime', 'Engine/Slate/Slate.Build.cs', ['Core', 'InputCore']],
    ['SlateCore', 'Runtime', 'Engine/SlateCore/SlateCore.Build.cs', ['Core']],
    ['UMG', 'Runtime', 'Engine/UMG/UMG.Build.cs', ['Slate', 'SlateCore']],
    ['AIModule', 'Runtime', 'Engine/AIModule/AIModule.Build.cs', ['Core', 'Engine', 'NavigationSystem']],
    ['NavigationSystem', 'Runtime', 'Engine/NavigationSystem/NavigationSystem.Build.cs', ['Engine']],
    ['UnrealEd', 'Editor', 'Editor/UnrealEd/UnrealEd.Build.cs', ['Core', 'Engine', 'Slate']],
    ['Kismet', 'Editor', 'Editor/Kismet/Kismet.Build.cs', ['UnrealEd']],
    ['BlueprintGraph', 'Editor', 'Editor/BlueprintGraph/BlueprintGraph.Build.cs', ['KismetCompiler']],
    ['MovieScene', 'Runtime', 'Runtime/MovieScene/MovieScene.Build.cs', ['Core', 'Engine']],
    ['NetCore', 'Runtime', 'Runtime/Net/Core/NetCore.Build.cs', ['Core']],
    ['AudioMixer', 'Runtime', 'Runtime/AudioMixer/AudioMixer.Build.cs', ['Engine']],
    ['Niagara', 'Runtime', 'Plugins/FX/Niagara/Source/Niagara/Niagara.Build.cs', ['Engine', 'RenderCore', 'RHI']],
    ['GeometryCore', 'Runtime', 'Plugins/Runtime/GeometryProcessing/Source/GeometryCore/GeometryCore.Build.cs', ['Core']],
  ]
  return {
    cats,
    plugins: P.map(([name, category, description, path], i) => ({
      name, slug: slug(name), category, description, path,
      version_name: '1.' + i, author: 'Epic Games', engine_version: '5.5',
      usage_doc: i % 3 !== 0,
    })),
    modules: M.map(([name, type, path, public_deps], i) => ({
      name, slug: slug(name), type, base: 'ModuleRules',
      platform: i % 3 === 0 ? 'Win64' : '', path, public_deps,
      private_deps: i % 4 === 0 ? ['Zlib'] : [],
    })),
  }
})()

api.defaults.adapter = async (config) => {
  const url = (config.url || '').split('?')[0]
  let data
  if (url === '/stats') {
    data = { total_plugins: MOCK.plugins.length, total_modules: MOCK.modules.length, categories: MOCK.cats, engine_version: '5.5' }
  } else if (url === '/plugins') {
    data = MOCK.plugins
  } else if (url === '/modules') {
    data = MOCK.modules
  } else if (url.startsWith('/plugins/')) {
    const p = MOCK.plugins.find(x => x.slug === url.slice(9))
    data = p ? { ...p, modules: [{ name: p.name + 'Runtime', type: 'Runtime' }, { name: p.name + 'Editor', type: 'Editor' }] } : { detail: 'not found' }
  } else if (url.startsWith('/modules/')) {
    data = MOCK.modules.find(x => x.slug === url.slice(9)) || { detail: 'not found' }
  } else if (url === '/config') {
    data = {
      path: 'backend/config.yaml', engine_exists: true, env_api_key: false,
      config: {
        engine_root: 'D:/UnrealEngine',
        scan: { plugins_dir: 'Engine/Plugins', source_dir: 'Engine/Source', parallel: true },
        ai: { enabled: true, endpoint: 'https://api.openai.com/v1', model: 'gpt-4o-mini', api_key: '', timeout: 60, stream_chunk_size: 128, workers: 4 },
        site: { usage_docs_root: 'usage_docs' },
        cors: { origins: [] },
      },
    }
  } else if (url === '/usage-docs/stats') {
    data = { root: 'usage_docs', plugins: { total: MOCK.plugins.length, have: 14 }, modules: { total: MOCK.modules.length, have: 6 } }
  } else if (url.startsWith('/usage-docs/')) {
    data = url.endsWith('/audiosynesthesia')
      ? { found: true, mtime: Date.now() / 1000 - 3600, content: '## 概览\n\n这是示例使用说明，用于验证 Markdown 排版。\n\n## 启用\n\n1. 打开插件浏览器\n2. 勾选 `AudioSynesthesia`\n\n```cpp\n#include "AudioSynesthesia.h"\n```\n\n- 依赖 `AudioMixer`\n- 支持打包\n\n| 平台 | 状态 |\n| --- | --- |\n| Win64 | OK |\n| Android | OK |' }
      : { found: false, content: '', mtime: 0 }
  } else {
    data = {}
  }
  return { data, status: 200, statusText: 'OK', headers: {}, config }
}
/* ===== TEMP MOCK END ===== */

/** 把 axios / FastAPI 的错误转成可读文本。 */
export function errMsg(err) {
  const detail = err?.response?.data?.detail
  if (typeof detail === 'string') return detail
  if (detail) return JSON.stringify(detail)
  return err?.message || String(err)
}

export const ItemsAPI = {
  getStats:    ()          => api.get('/stats').then(r => r.data),
  listPlugins: (params)    => api.get('/plugins', { params }).then(r => r.data),
  getPlugin:   (slug)      => api.get(`/plugins/${slug}`).then(r => r.data),
  listModules: (params)    => api.get('/modules', { params }).then(r => r.data),
  getModule:   (slug)      => api.get(`/modules/${slug}`).then(r => r.data),
  rescan:      ()          => api.post('/rescan').then(r => r.data),
}

export const ConfigAPI = {
  get:    ()        => api.get('/config').then(r => r.data),
  update: (config)  => api.put('/config', config).then(r => r.data),
  testAi: ()        => api.post('/ai/test').then(r => r.data),
}

export const UsageDocAPI = {
  get:   (kind, slug) => api.get(`/usage-docs/${kind}/${slug}`).then(r => r.data),
  stats: ()           => api.get('/usage-docs/stats').then(r => r.data),
}