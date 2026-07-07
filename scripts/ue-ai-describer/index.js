const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const STATE_FILE = '.ue-ai-describer-state.json';
const TARGET_DIR = process.argv[2] || '.';

async function loadState() {
  const statePath = path.join(TARGET_DIR, STATE_FILE);
  if (fs.existsSync(statePath)) {
    return JSON.parse(fs.readFileSync(statePath, 'utf8'));
  }
  return { processed: [], lastRun: null };
}

async function saveState(state) {
  const statePath = path.join(TARGET_DIR, STATE_FILE);
  fs.writeFileSync(statePath, JSON.stringify(state, null, 2));
}

async function findMarkdownFiles(dir) {
  const files = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory() && !entry.name.startsWith('.') && entry.name !== 'node_modules') {
      files.push(...await findMarkdownFiles(fullPath));
    } else if (entry.isFile() && entry.name.endsWith('.md')) {
      files.push(fullPath);
    }
  }
  return files;
}

async function generateDescription(browser, filePath, content) {
  // TODO: 填入具体的 AI 服务交互逻辑
  // 从原私有仓库的脚本中复制实际的 Playwright 自动化逻辑到这里
  //
  // 示例框架：
  // const page = await browser.newPage();
  // await page.goto('https://your-ai-service.com');
  // ... 填入登录、输入内容、获取描述等操作 ...
  // const description = await page.locator('.result').textContent();
  // await page.close();
  // return description;

  console.warn('Warning: generateDescription() is not implemented. Please fill in the AI service interaction logic.');
  return 'AI generated description placeholder';
}

async function main() {
  console.log('Starting UE AI Describer...');
  console.log('Target directory:', path.resolve(TARGET_DIR));

  const state = await loadState();
  const files = await findMarkdownFiles(TARGET_DIR);

  console.log(`Found ${files.length} markdown files`);

  const browser = await chromium.launch({ headless: true });

  try {
    for (const file of files) {
      const relativePath = path.relative(TARGET_DIR, file);
      if (state.processed.includes(relativePath)) {
        console.log(`Skipping already processed: ${relativePath}`);
        continue;
      }

      console.log(`Processing: ${relativePath}`);
      const content = fs.readFileSync(file, 'utf8');

      // 检查是否已有 AI 描述
      if (content.includes('<!-- AI_DESCRIPTION -->')) {
        console.log(`Already has AI description: ${relativePath}`);
        state.processed.push(relativePath);
        continue;
      }

      try {
        const description = await generateDescription(browser, file, content);
        const updatedContent = content + '\n\n<!-- AI_DESCRIPTION -->\n' + description + '\n<!-- /AI_DESCRIPTION -->\n';
        fs.writeFileSync(file, updatedContent);
        state.processed.push(relativePath);
        console.log(`Updated: ${relativePath}`);
      } catch (error) {
        console.error(`Failed to process ${relativePath}:`, error.message);
      }

      // 增量保存状态
      await saveState(state);
    }
  } finally {
    await browser.close();
  }

  state.lastRun = new Date().toISOString();
  await saveState(state);
  console.log('Done!');
}

main().catch(console.error);
