<script setup>
import { onMounted, reactive, ref } from 'vue'
import { ConfigAPI, errMsg } from '../api/client.js'
import { useItemsStore } from '../stores/items.js'

const store = useItemsStore()

const form = reactive({
  engine_root: '',
  scan: { plugins_dir: '', source_dir: '', parallel: true },
  ai: { enabled: true, endpoint: '', model: '', api_key: '', timeout: 60, stream_chunk_size: 128 },
  site: { docs_root: '', rebuild_on_start: false },
  cors: { origins: [] },
})

const meta = ref({ path: '', engine_exists: true, env_api_key: false })
const loading = ref(true)
const saving = ref(false)
const testing = ref(false)
const status = ref(null) // { type: 'ok' | 'error', text }
const testResult = ref(null) // { type: 'ok' | 'error', text }

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

onMounted(load)
</script>

<template>
  <div class="page-title-wrap">
    <h1>设置</h1>
    <p>配置保存在后端 <code class="mono">{{ meta.path || 'backend/config.yaml' }}</code>，保存后立即生效</p>
  </div>

  <div v-if="loading" class="empty">加载中…</div>

  <template v-else>
    <div v-if="!meta.engine_exists" class="banner banner-warn">
      当前 engine_root 路径不存在，扫描结果为空。请填写正确的 UE 源码根目录。
    </div>

    <section class="card">
      <div class="card-title">
        <span class="card-title-sep"></span>
        UE 源码 <span class="card-title-cn">Source tree</span>
      </div>
      <div class="form-grid">
        <div class="field full">
          <label for="engine_root">engine_root（引擎根目录）</label>
          <input id="engine_root" v-model="form.engine_root" type="text" class="mono" placeholder="D:/UnrealEngine" />
          <span class="field-hint">包含 Engine 文件夹的目录，例如 D:/UnrealEngine</span>
        </div>
        <div class="field">
          <label for="plugins_dir">plugins_dir（插件目录）</label>
          <input id="plugins_dir" v-model="form.scan.plugins_dir" type="text" class="mono" />
          <span class="field-hint">相对 engine_root，默认 Engine/Plugins</span>
        </div>
        <div class="field">
          <label for="source_dir">source_dir（源码目录）</label>
          <input id="source_dir" v-model="form.scan.source_dir" type="text" class="mono" />
          <span class="field-hint">相对 engine_root，默认 Engine/Source</span>
        </div>
      </div>
      <div class="form-actions">
        <button class="btn" :disabled="store.loading" @click="store.reload()">重新扫描</button>
      </div>
    </section>

    <section class="card" style="margin-top: var(--space-5);">
      <div class="card-title">
        <span class="card-title-sep"></span>
        AI 模型 <span class="card-title-cn">OpenAI-compatible</span>
      </div>

      <div class="form-grid">
        <div class="field full">
          <label class="check">
            <input v-model="form.ai.enabled" type="checkbox" />
            <span>启用 AI 助手</span>
          </label>
        </div>
        <div class="field">
          <label for="endpoint">endpoint（接口地址）</label>
          <input id="endpoint" v-model="form.ai.endpoint" type="text" class="mono" placeholder="https://api.openai.com/v1" />
          <span class="field-hint">会拼接 /chat/completions，任何兼容 OpenAI 的服务都可以</span>
        </div>
        <div class="field">
          <label for="model">model（模型名）</label>
          <input id="model" v-model="form.ai.model" type="text" class="mono" placeholder="gpt-4o-mini" />
        </div>
        <div class="field">
          <label for="api_key">api_key（密钥）</label>
          <input id="api_key" v-model="form.ai.api_key" type="password" class="mono" autocomplete="off" placeholder="留空表示清除；保留掩码则不修改" />
          <span class="field-hint">
            <template v-if="meta.env_api_key">已检测到环境变量 UE_AI_API_KEY，它会覆盖此处的值。</template>
            <template v-else>也可使用环境变量 UE_AI_API_KEY 代替，避免明文保存。</template>
          </span>
        </div>
        <div class="field">
          <label for="timeout">timeout（秒）</label>
          <input id="timeout" v-model.number="form.ai.timeout" type="number" min="5" max="600" />
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

    <div class="form-actions" style="margin-top: var(--space-6);">
      <button class="btn btn-primary" :disabled="saving" @click="save">
        {{ saving ? '保存中…' : '保存设置' }}
      </button>
      <span v-if="status" :class="status.type === 'ok' ? 'chip chip-success' : 'chip chip-warning'">{{ status.text }}</span>
    </div>

    <p class="field-hint" style="margin-top: var(--space-4);">
      提示：CORS 来源与端口属于启动参数，修改后需要重启后端。保存会重写 config.yaml，原有手写注释会被覆盖。
    </p>
  </template>
</template>
