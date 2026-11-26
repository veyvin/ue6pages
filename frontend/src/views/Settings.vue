<script setup>
import { computed, onMounted, reactive, ref } from 'vue'
import { ConfigAPI, UsageDocAPI, errMsg } from '../api/client.js'
import { streamUsageBatch } from '../api/ai.js'
import { rebuildUsageFb, usageFbState } from '../api/usageFb.js'
import { useItemsStore } from '../stores/items.js'

const store = useItemsStore()

const form = reactive({
  engine_root: '',
  scan: { plugins_dir: '', source_dir: '', parallel: true },
  ai: { enabled: true, endpoint: '', model: '', api_key: '', timeout: 60, stream_chunk_size: 128, workers: 4 },
  site: { usage_docs_root: 'usage_docs' },
  cors: { origins: [] },
})

const meta = ref({ path: '', engine_exists: true, env_api_key: false })
const loading = ref(true)
const saving = ref(false)
const testing = ref(false)
const status = ref(null) // { type: 'ok' | 'error', text }
const testResult = ref(null) // { type: 'ok' | 'error', text }

// ---- AI 批量生成《使用方法》 ----
const batchForm = reactive({ kind: 'all', limit: 0, overwrite: false })
const batchRunning = ref(false)
const batchSummary = ref(null) // { total, seconds, ok, skip, fail }
const batchErrors = ref([])    // ['插件 · Foo：HTTP 401 ...', ...]
const batchProgress = reactive({ total: 0, ok: 0, skip: 0, fail: 0, current: '' })
const configStats = ref(null) // {root, plugins:{total,have}, modules:{total,have}}
const fbBusy = ref(false)
const fbStatus = ref(null)
let batchAbort = null

const kindOptions = [
  { value: 'all', label: '全部' },
  { value: 'plugin', label: '插件' },
  { value: 'module', label: '模块' },
]

const aiReady = computed(() => form.ai.enabled && Boolean(form.ai.api_key || meta.value.env_api_key))

const batchDone = computed(() => batchProgress.ok + batchProgress.skip + batchProgress.fail)
const batchDonePercent = computed(() => (
  batchProgress.total ? Math.min(100, Math.round((batchDone.value / batchProgress.total) * 100)) : 0
))
const batchSegments = computed(() => {
  const total = batchProgress.total || 1
  return {
    ok: (batchProgress.ok / total) * 100,
    skip: (batchProgress.skip / total) * 100,
    fail: (batchProgress.fail / total) * 100,
  }
})

function coverPct(s) {
  return s?.total ? Math.min(100, Math.round((s.have / s.total) * 100)) : 0
}

function clearErrors() {
  batchErrors.value = []
}

async function load() {
  loading.value = true
  try {
    const data = await ConfigAPI.get()
    Object.assign(form, structuredClone(data.config))
    meta.value = {
      path: data.path,
      engine_exists: data.engine_exists,
      env_api_key: data.env_api_key,
    }
    UsageDocAPI.stats().then((s) => { configStats.value = s }).catch(() => {})
  } catch (err) {
    status.value = { type: 'error', text: '读取配置失败：' + errMsg(err) }
  } finally {
    loading.value = false
  }
}

async function save() {
  saving.value = true
  status.value = null
  try {
    const data = await ConfigAPI.update(JSON.parse(JSON.stringify(form)))
    Object.assign(form, structuredClone(data.config))
    meta.value = {
      path: data.path,
      engine_exists: data.engine_exists,
      env_api_key: data.env_api_key,
    }
    await store.reload()
    status.value = { type: 'ok', text: '已保存并重新扫描' }
  } catch (err) {
    status.value = { type: 'error', text: '保存失败：' + errMsg(err) }
  } finally {
    saving.value = false
  }
}

async function testAi() {
  testing.value = true
  testResult.value = null
  try {
    const r = await ConfigAPI.testAi()
    testResult.value = { type: 'ok', text: `连接成功（${r.model}）：${r.reply}` }
  } catch (err) {
    testResult.value = { type: 'error', text: errMsg(err) }
  } finally {
    testing.value = false
  }
}

function startBatch() {
  if (batchRunning.value) return
  batchProgress.ok = 0
  batchProgress.skip = 0
  batchProgress.fail = 0
  batchProgress.current = ''
  batchSummary.value = null
  batchErrors.value = []
  batchRunning.value = true
  batchAbort = new AbortController()
  streamUsageBatch(
    {
      kind: batchForm.kind,
      slugs: [],
      limit: Number(batchForm.limit) || 0,
      overwrite: batchForm.overwrite,
    },
    {
      onFrame: (f) => {
        if (f.type === 'start') {
          batchProgress.total = (f.total || 0) + (f.skipped_existing || 0)
          batchProgress.skip = f.skipped_existing || 0
        } else if (f.type === 'item') {
          batchProgress.current = f.name
          if (f.status === 'ok') batchProgress.ok++
          else if (f.status === 'skip') batchProgress.skip++
          else if (f.status === 'fail') {
            batchProgress.fail++
            const label = f.kind === 'plugin' ? '插件' : '模块'
            batchErrors.value.push(`${label} · ${f.name}：${f.error || '未知错误'}`)
          }
        } else if (f.type === 'summary') {
          batchSummary.value = f
        }
      },
      onError: (err) => {
        batchErrors.value.push('连接中断：' + errMsg(err))
      },
    },
    { signal: batchAbort.signal },
  ).finally(async () => {
    batchRunning.value = false
    batchProgress.current = ''
    try {
      await rebuildUsageFb()
      await store.loadAll(true)
      configStats.value = await UsageDocAPI.stats()
    } catch {
      /* 后端未启动时详情仍可读 gh-pages 的 usage.fb */
    }
  })
}

function stopBatch() {
  batchAbort?.abort()
  batchRunning.value = false
}

async function deployUsageFb() {
  fbBusy.value = true
  fbStatus.value = null
  try {
    const info = await rebuildUsageFb()
    await store.loadAll(true)
    fbStatus.value = {
      type: 'ok',
      text: `已写入 ${info.path || '/assets/usage.fb'}（${info.docs} 条，${info.bytes} 字节）`,
    }
  } catch (err) {
    fbStatus.value = { type: 'error', text: errMsg(err) }
  } finally {
    fbBusy.value = false
  }
}

onMounted(load)
</script>

<template>
  <div class="settings-page">
    <div class="page-head">
      <div class="kicker">
        <span class="kicker-dot"></span>
        System / Config
        <span class="kicker-dim">/ local backend</span>
      </div>
      <h1 class="page-title">设置 <span class="serif">Settings</span></h1>
      <p class="page-sub">
        配置保存在后端 <span class="mono">{{ meta.path || 'backend/config.yaml' }}</span>，保存后立即生效。
      </p>
    </div>

    <div v-if="loading" class="empty">加载中…</div>

    <template v-else>
      <div v-if="!meta.engine_exists" class="banner banner-warn">
        当前 engine_root 路径不存在，扫描结果为空。请填写正确的 UE 源码根目录。
      </div>

      <div class="settings-stack">
        <section class="panel">
          <div class="panel-head">
            <span class="panel-index">01</span>
            <div>
              <h2 class="panel-title">UE 源码 <span class="serif">Source tree</span></h2>
              <p class="panel-desc">指定引擎根目录与扫描范围，保存后重新建立索引。</p>
            </div>
          </div>

          <div class="form-grid">
            <div class="field full">
              <label for="engine_root">engine_root / 引擎根目录</label>
              <input id="engine_root" v-model="form.engine_root" type="text" class="mono" placeholder="D:/UnrealEngine" />
              <span class="field-hint">包含 Engine 文件夹的目录，例如 D:/UnrealEngine</span>
            </div>
            <div class="field">
              <label for="plugins_dir">plugins_dir / 插件目录</label>
              <input id="plugins_dir" v-model="form.scan.plugins_dir" type="text" class="mono" />
              <span class="field-hint">相对 engine_root，默认 Engine/Plugins</span>
            </div>
            <div class="field">
              <label for="source_dir">source_dir / 源码目录</label>
              <input id="source_dir" v-model="form.scan.source_dir" type="text" class="mono" />
              <span class="field-hint">相对 engine_root，默认 Engine/Source</span>
            </div>
          </div>

          <div class="form-actions">
            <button class="btn btn-dark" :disabled="store.loading" @click="store.reload()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <polyline points="23 4 23 10 17 10" />
                <polyline points="1 20 1 14 7 14" />
                <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15" />
              </svg>
              重新扫描
            </button>
            <span class="field-hint">扫描不修改源码，只读取 .uplugin 与 *.Build.cs</span>
          </div>
        </section>

        <section class="panel">
          <div class="panel-head">
            <span class="panel-index">02</span>
            <div>
              <h2 class="panel-title">AI 模型 <span class="serif">OpenAI-compatible</span></h2>
              <p class="panel-desc">兼容 OpenAI 接口的服务均可接入，用于详情页讲解与批量文档生成。</p>
            </div>
          </div>

          <div class="form-grid">
            <div class="field full">
              <label class="check">
                <input v-model="form.ai.enabled" type="checkbox" />
                <span>启用 AI 助手</span>
              </label>
            </div>
            <div class="field">
              <label for="endpoint">endpoint / 接口地址</label>
              <input id="endpoint" v-model="form.ai.endpoint" type="text" class="mono" placeholder="https://api.openai.com/v1" />
              <span class="field-hint">会拼接 /chat/completions，任何兼容 OpenAI 的服务都可以</span>
            </div>
            <div class="field">
              <label for="model">model / 模型名</label>
              <input id="model" v-model="form.ai.model" type="text" class="mono" placeholder="gpt-4o-mini" />
            </div>
            <div class="field">
              <label for="api_key">api_key / 密钥</label>
              <input id="api_key" v-model="form.ai.api_key" type="password" class="mono" autocomplete="off" placeholder="留空表示清除；保留掩码则不修改" />
              <span class="field-hint">
                <template v-if="meta.env_api_key">已检测到环境变量 UE_AI_API_KEY，它会覆盖此处的值。</template>
                <template v-else>也可使用环境变量 UE_AI_API_KEY 代替，避免明文保存。</template>
              </span>
            </div>
            <div class="field">
              <label for="timeout">timeout / 秒</label>
              <input id="timeout" v-model.number="form.ai.timeout" type="number" min="5" max="600" />
            </div>
            <div class="field">
              <label for="workers">workers / 批量并发生成数</label>
              <input id="workers" v-model.number="form.ai.workers" type="number" min="1" max="32" />
              <span class="field-hint">批量生成《使用方法》时的并行 AI 请求数，1-32</span>
            </div>
          </div>

          <div class="form-actions">
            <button class="btn" :disabled="testing" @click="testAi">
              {{ testing ? '测试中…' : '测试 AI 连接' }}
            </button>
            <span class="field-hint">测试使用已保存的配置，修改后请先保存。</span>
          </div>
          <div v-if="testResult" class="banner" :class="testResult.type === 'ok' ? 'banner-ok' : 'banner-error'" style="margin-top: var(--space-3); word-break: break-all;">
            {{ testResult.text }}
          </div>
        </section>

        <section class="panel">
          <div class="panel-head">
            <span class="panel-index">03</span>
            <div>
              <h2 class="panel-title">AI 批量生成 <span class="serif">Usage docs</span></h2>
              <p class="panel-desc">为扫描到的条目批量生成《使用方法》，写入磁盘供详情页读取。</p>
            </div>
          </div>

          <p class="settings-note" style="margin-bottom: var(--space-4);">
            写入 <span class="mono">{{ configStats?.root || form.site.usage_docs_root || 'usage_docs' }}</span>
            目录。CI 已不再调用 AI；这里生成的内容会显示在每个条目的详情页。
          </p>

          <div v-if="configStats" class="coverage-grid">
            <div class="coverage-item">
              <div class="coverage-head">
                <span>插件 <i>Plugins</i></span>
                <b>{{ configStats.plugins.have }}<i>/{{ configStats.plugins.total }}</i></b>
              </div>
              <div class="coverage-bar"><i :style="{ width: coverPct(configStats.plugins) + '%' }"></i></div>
            </div>
            <div class="coverage-item">
              <div class="coverage-head">
                <span>模块 <i>Modules</i></span>
                <b>{{ configStats.modules.have }}<i>/{{ configStats.modules.total }}</i></b>
              </div>
              <div class="coverage-bar"><i :style="{ width: coverPct(configStats.modules) + '%' }"></i></div>
            </div>
          </div>

          <div class="form-grid" style="margin-top: var(--space-4);">
            <div class="field">
              <label>生成范围</label>
              <div class="seg-inline" role="group" aria-label="生成范围">
                <button
                  v-for="opt in kindOptions"
                  :key="opt.value"
                  type="button"
                  :class="{ active: batchForm.kind === opt.value }"
                  :aria-pressed="batchForm.kind === opt.value"
                  :disabled="batchRunning"
                  @click="batchForm.kind = opt.value"
                >{{ opt.label }}</button>
              </div>
            </div>
            <div class="field">
              <label for="batch-limit">数量上限（0 = 全部）</label>
              <input id="batch-limit" v-model.number="batchForm.limit" type="number" min="0" />
              <span class="field-hint">可先填 5 试跑看效果</span>
            </div>
            <div class="field">
              <label>已有文档</label>
              <label class="check" for="batch-overwrite">
                <input id="batch-overwrite" v-model="batchForm.overwrite" type="checkbox" />
                <span>覆盖重新生成（不勾选则跳过已有用法的条目）</span>
              </label>
            </div>
            <div class="field">
              <label for="usage-root">usage_docs_root / 存储目录</label>
              <input id="usage-root" v-model="form.site.usage_docs_root" type="text" class="mono" placeholder="usage_docs" />
              <span class="field-hint">相对 backend/ 目录或绝对路径；修改后请点下方保存设置</span>
            </div>
          </div>

          <div class="form-actions">
            <button
              class="btn btn-dark"
              :disabled="batchRunning || !aiReady"
              :title="aiReady ? '' : '请先启用 AI 并填写 API Key 后保存'"
              @click="startBatch"
            >
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z" />
              </svg>
              {{ batchRunning ? '生成中…' : '开始批量生成' }}
            </button>
            <button v-if="batchRunning" class="btn" @click="stopBatch">停止</button>
            <span v-if="!aiReady" class="field-hint">AI 未启用或未配置 API Key，请在上方保存后再生成。</span>
            <span v-else class="field-hint">并发 {{ form.ai.workers }} · 失败条目记录在下方日志</span>
          </div>

          <div v-if="batchRunning || batchSummary" class="batch-progress">
            <div class="batch-progress-head">
              <span class="batch-state" :class="{ running: batchRunning }">{{ batchRunning ? '运行中' : '已完成' }}</span>
              <span class="batch-current mono">{{ batchProgress.current || '待开始' }}</span>
              <span class="batch-pct">{{ batchDonePercent }}%</span>
            </div>
            <div
              class="batch-bar"
              role="progressbar"
              :aria-valuenow="batchDonePercent"
              aria-valuemin="0"
              aria-valuemax="100"
            >
              <i class="ok" :style="{ width: batchSegments.ok + '%' }"></i>
              <i class="skip" :style="{ width: batchSegments.skip + '%' }"></i>
              <i class="fail" :style="{ width: batchSegments.fail + '%' }"></i>
            </div>
            <div class="batch-stats">
              <span class="ok"><b>{{ batchProgress.ok }}</b>成功</span>
              <span class="skip"><b>{{ batchProgress.skip }}</b>跳过</span>
              <span class="fail"><b>{{ batchProgress.fail }}</b>失败</span>
              <span class="total"><b>{{ batchDone }}</b>/ {{ batchProgress.total }} 已处理</span>
            </div>
          </div>

          <div v-if="batchSummary" class="banner" :class="batchSummary.fail ? 'banner-warn' : 'banner-ok'" style="margin-top: var(--space-3);">
            完成：成功 {{ batchSummary.ok }} · 跳过 {{ batchSummary.skip }} · 失败 {{ batchSummary.fail }} ·
            用时 {{ batchSummary.seconds }}s（输出目录 {{ batchSummary.output_root || configStats?.root }}）
          </div>

          <div v-if="batchErrors.length" class="batch-log-wrap">
            <div class="batch-log-head">
              <span class="batch-log-title"><span class="dot"></span>错误日志 · {{ batchErrors.length }}</span>
              <button class="btn-quiet" @click="clearErrors">清空</button>
            </div>
            <div class="batch-log">{{ batchErrors.join('\n') }}</div>
          </div>

          <div class="form-actions" style="margin-top: var(--space-4);">
            <button class="btn" :disabled="fbBusy" @click="deployUsageFb">
              {{ fbBusy ? '打包中…' : '部署 usage.fb' }}
            </button>
            <span class="field-hint">
              写入 <span class="mono">/assets/usage.fb</span>，前端与 gh-pages 走同一路径。
              当前：{{ usageFbState().docs || 0 }} 条
              <template v-if="usageFbState().source"> · {{ usageFbState().source }}</template>
            </span>
          </div>
          <div v-if="fbStatus" class="banner" :class="fbStatus.type === 'ok' ? 'banner-ok' : 'banner-error'" style="margin-top: var(--space-3);">
            {{ fbStatus.text }}
          </div>
        </section>
      </div>

      <div class="settings-savebar">
        <div class="settings-savebar-copy">
          <span class="settings-savebar-kicker">Config / persist</span>
          <span class="settings-savebar-text">保存后立即生效，并重新扫描源码树。</span>
        </div>
        <span
          v-if="status"
          class="chip chip-light"
          :class="status.type === 'ok' ? 'chip-success' : 'chip-warning'"
        >{{ status.text }}</span>
        <button class="btn btn-lime" :disabled="saving" @click="save">
          {{ saving ? '保存中…' : '保存设置' }}
        </button>
      </div>

      <p class="settings-note">
        提示：CORS 来源与端口属于启动参数，修改后需要重启后端。保存会重写 config.yaml，原有手写注释会被覆盖。
      </p>
    </template>
  </div>
</template>
