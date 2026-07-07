const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');

chromium.use(StealthPlugin());

const ASSISTANT_URL = 'https://dev.epicgames.com/community/assistant/unreal-engine/conversation';

function takeScreenshot(page, name) {
  try {
    const dir = path.join(process.cwd(), 'debug-screenshots');
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
    const filePath = path.join(dir, `${name}.png`);
    page.screenshot({ path: filePath, fullPage: true }).catch(() => {});
    console.log(`  [screenshot] ${name}`);
  } catch (e) {}
}

function cleanResponse(text, question) {
  // 1. 截掉页面底部的固定 UI 元素
  const uiMarkers = [
    'You might find these useful',
    'Your feedback lets Epic',
    'Chatting with the Unreal Engine assistant',
    'Switch to UEFN',
    'Using In-Game Ads',
    'Using Ad Mob',
  ];

  for (const marker of uiMarkers) {
    const idx = text.indexOf(marker);
    if (idx !== -1) {
      text = text.substring(0, idx).trim();
    }
  }

  // 2. 去掉开头的 prompt 部分
  // 策略1: 直接匹配完整 question
  const idx = text.indexOf(question);
  if (idx !== -1) {
    let result = text.substring(idx + question.length).trim();
    result = result.replace(/^[\s:：]+/, '');
    return result;
  }

  // 策略2: 匹配 question 的前 30 个字符
  const prefix = question.substring(0, 30);
  const idx2 = text.indexOf(prefix);
  if (idx2 !== -1) {
    let result = text.substring(idx2 + prefix.length).trim();
    const match = result.match(/[A-Z].*/s);
    if (match) {
      return match[0];
    }
    return result;
  }

  // 策略3: 如果文本以 prompt 词开头，截掉
  const promptPatterns = [
    /^Introduce the Unreal Engine[^.]+\.(.*)/s,
    /^Give a brief description[^.]+\.(.*)/s,
  ];
  for (const pattern of promptPatterns) {
    const match = text.match(pattern);
    if (match) {
      return match[1].trim();
    }
  }

  return text;
}

class UEAIClient {
  constructor(options = {}) {
    this.headless = options.headless !== false;
    this.userDataDir = options.userDataDir || './.playwright-user-data';
    this.browser = null;
    this.context = null;
    this.page = null;
  }

  async init() {
    const launchOptions = {
      headless: this.headless,
      args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-blink-features=AutomationControlled',
        '--start-maximized',
        '--window-size=1920,1080',
      ],
    };

    console.log('  Launching browser...');
    this.browser = await chromium.launchPersistentContext(this.userDataDir, launchOptions);
    this.context = this.browser;
    this.page = await this.context.newPage();

    await this.page.setViewportSize({ width: 1920, height: 1080 });

    console.log('  Navigating to assistant page...');
    await this.page.goto(ASSISTANT_URL, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await this.page.waitForLoadState('networkidle', { timeout: 30000 }).catch(() => {});

    takeScreenshot(this.page, '01-page-loaded');

    console.log('  Waiting for page to be ready...');
    await this._waitForReady();
    console.log('  Client ready!');
  }

  async _waitForReady() {
    const maxWait = 120000;
    const startTime = Date.now();
    let lastTitle = '';

    while (Date.now() - startTime < maxWait) {
      await this.page.waitForTimeout(2000);

      let title;
      try {
        title = await this.page.title();
      } catch (e) {
        continue;
      }

      if (title !== lastTitle) {
        console.log(`  Page title: ${title}`);
        lastTitle = title;
      }

      if (title.includes('Just a moment') || title.includes('Please Wait') || title.includes('Security')) {
        console.log('  Cloudflare challenge detected, waiting...');
        continue;
      }

      const textareaSelectors = [
        'textarea[data-testid="prompt-input"]',
        'textarea[placeholder*="Ask"]',
        'textarea[name="prompt"]',
        'textarea',
      ];

      for (const selector of textareaSelectors) {
        try {
          const textarea = await this.page.$(selector);
          if (textarea) {
            const isVisible = await textarea.isVisible();
            if (isVisible) {
              console.log(`  Found textarea with selector: ${selector}`);
              takeScreenshot(this.page, '02-textarea-found');
              await this.page.waitForTimeout(1000);
              return;
            }
          }
        } catch (e) {}
      }
    }

    takeScreenshot(this.page, 'error-ready-timeout');
    throw new Error('Timeout waiting for page to be ready');
  }

  async ask(question, options = {}) {
    const timeout = options.timeout || 120000;
    console.log('  Asking AI via UI...');

    // 找到 textarea
    const textareaSelectors = [
      'textarea[data-testid="prompt-input"]',
      'textarea[placeholder*="Ask"]',
      'textarea[name="prompt"]',
      'textarea',
    ];

    let textarea = null;
    for (const selector of textareaSelectors) {
      try {
        textarea = await this.page.$(selector);
        if (textarea && await textarea.isVisible()) {
          console.log(`  Using textarea selector: ${selector}`);
          break;
        }
      } catch (e) {}
    }

    if (!textarea) {
      takeScreenshot(this.page, 'error-no-textarea');
      throw new Error('No textarea found');
    }

    // 清空并输入问题
    await textarea.click();
    await this.page.waitForTimeout(500);
    await textarea.fill('');
    await this.page.waitForTimeout(500);
    await textarea.type(question, { delay: 30 });
    console.log('  Question typed');
    await this.page.waitForTimeout(1000);

    takeScreenshot(this.page, '03-question-entered');

    // 发送
    await textarea.press('Enter');
    console.log('  Pressed Enter to send');
    await this.page.waitForTimeout(2000);

    takeScreenshot(this.page, '04-after-send');

    // 等待问题出现在页面上
    console.log('  Waiting for question to appear...');
    try {
      await this.page.waitForFunction(
        ({ q }) => document.body.innerText.includes(q.substring(0, 40)),
        { timeout: 15000 },
        { q: question }
      );
    } catch (e) {
      console.log('  Question may not have appeared on page');
    }

    // 记录问题出现后的文本作为 baseline
    await this.page.waitForTimeout(2000);
    const beforeText = await this.page.evaluate(() => document.body.innerText);
    console.log(`  Text after question: ${beforeText.length} chars`);

    // 等待回答出现（文本继续增加并稳定）
    console.log('  Waiting for answer...');
    const startTime = Date.now();
    let lastLength = beforeText.length;
    let stableCount = 0;

    while (Date.now() - startTime < timeout) {
      await this.page.waitForTimeout(3000);

      const currentText = await this.page.evaluate(() => document.body.innerText);
      const newChars = currentText.length - beforeText.length;

      if (currentText.length > lastLength) {
        lastLength = currentText.length;
        stableCount = 0;
        console.log(`  Answer growing: ${newChars} new chars (total ${currentText.length})`);
      } else if (currentText.length === lastLength && newChars > 100) {
        stableCount++;
        console.log(`  Answer stable: ${stableCount}/4 (${newChars} new chars)`);
        if (stableCount >= 4) {
          const newText = currentText.substring(beforeText.length);
          const cleaned = cleanResponse(newText, question);
          console.log(`  Cleaned answer: ${cleaned.length} chars`);
          if (cleaned.length > 50) {
            takeScreenshot(this.page, '05-response-complete');
            return cleaned;
          }
        }
      } else if (newChars <= 100) {
        console.log(`  Text not growing enough: ${newChars} new chars`);
      }
    }

    // 超时 fallback：返回新增文本
    const currentText = await this.page.evaluate(() => document.body.innerText);
    const newText = currentText.substring(beforeText.length);
    const cleaned = cleanResponse(newText, question);

    if (cleaned.length > 50) {
      console.log(`  Returning partial answer: ${cleaned.length} chars`);
      return cleaned;
    }

    takeScreenshot(this.page, 'error-response-timeout');
    throw new Error('Timeout waiting for answer');
  }

  async close() {
    if (this.context) {
      await this.context.close();
    }
  }
}

module.exports = UEAIClient;
