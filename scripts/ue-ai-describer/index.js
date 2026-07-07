const fs = require('fs');
const path = require('path');
const UEAIClient = require('./ue-ai-client');
const { findMdFiles, readMdFile, updateMdDescription, hasAIDescription } = require('./scanner');

const STATE_FILE = process.env.UE_AI_STATE_FILE || path.join(__dirname, '..', '..', '.ue-ai-describer-state.json');
const DEFAULT_ROOT = '/workspace';
const AI_DELIMITER = '\n\n---\n\n### AI Description & Usage Tips\n\n';
const MAX_RETRIES = 3;

function loadState() {
  if (fs.existsSync(STATE_FILE)) {
    try {
      return JSON.parse(fs.readFileSync(STATE_FILE, 'utf-8'));
    } catch (e) {
      console.warn('Failed to parse state file, starting fresh');
    }
  }
  return { processed: [], failed: [] };
}

function saveState(state) {
  fs.writeFileSync(STATE_FILE, JSON.stringify(state, null, 2), 'utf-8');
}

function buildQuestion(itemName, category) {
  const typeName = category === 'plugins' ? 'plugin' : 'module';
  return `Introduce the Unreal Engine "${itemName}" ${typeName}. Give a brief description (what it is, what it's used for), then list 5-8 practical usage tips or best practices. Format as markdown with clear headings. Be concise and practical.`;
}

async function askWithRetry(client, question, maxRetries = MAX_RETRIES) {
  let lastError = null;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const answer = await client.ask(question, { timeout: 120000 });
      if (answer && answer.length > 50) {
        return answer;
      }
      lastError = new Error('Answer too short or empty');
    } catch (e) {
      lastError = e;
      console.log(`    Attempt ${attempt} failed: ${e.message}`);

      if (e.message.includes('403') || e.message.includes('Forbidden')) {
        console.log('    Cloudflare detected, reloading page...');
        try {
          await client.page.reload({ waitUntil: 'domcontentloaded' });
          await client._waitForReady();
        } catch (reloadErr) {
          console.log('    Reload failed');
        }
      }
    }

    if (attempt < maxRetries) {
      const waitMs = 5000 * attempt;
      console.log(`    Waiting ${waitMs / 1000}s before retry...`);
      await new Promise(r => setTimeout(r, waitMs));
    }
  }

  throw lastError;
}

async function processItem(client, item, state, dryRun = false) {
  const name = item.name;
  const category = item.category;
  console.log(`\n========================================`);
  console.log(`Processing: ${name} (${category})`);
  console.log(`Path: ${item.relativePath}`);

  try {
    const content = readMdFile(item.path);

    if (hasAIDescription(content) && state.processed.includes(item.path)) {
      console.log('  Already processed, skipping.');
      return 'skipped';
    }

    const question = buildQuestion(name, category);
    console.log('  Asking AI...');

    const answer = await askWithRetry(client, question);
    const aiContent = answer.trim();
    console.log(`  Answer length: ${aiContent.length} chars`);

    if (!dryRun) {
      const newLen = updateMdDescription(item.path, aiContent);
      console.log(`  Description updated! New length: ${newLen} chars`);
    } else {
      console.log('  [DRY RUN] Would update description');
      console.log(`  Preview:\n${aiContent.substring(0, 300)}...`);
    }

    if (!state.processed.includes(item.path)) {
      state.processed.push(item.path);
    }
    saveState(state);
    return 'success';
  } catch (e) {
    console.error(`  Error: ${e.message}`);
    state.failed = state.failed.filter(f => f.path !== item.path);
    state.failed.push({ path: item.path, error: e.message, time: Date.now() });
    saveState(state);
    return 'failed';
  }
}

async function main() {
  const args = process.argv.slice(2);

  function getArg(name) {
    const full = `--${name}=`;
    const found = args.find(a => a.startsWith(full));
    return found ? found.substring(full.length) : null;
  }

  function hasFlag(name) {
    return args.includes(`--${name}`);
  }

  const rootDir = args[0] || DEFAULT_ROOT;
  const dryRun = hasFlag('dry-run');
  const daily = parseInt(getArg('daily') || '0');
  const limit = parseInt(getArg('limit') || '0');
  const offset = parseInt(getArg('offset') || '0');
  const resumeFailed = hasFlag('retry-failed');
  const headless = hasFlag('headless') || process.env.CI === 'true';
  const userDataDir = process.env.UE_AI_USER_DATA_DIR || path.join(__dirname, '.playwright-user-data');

  console.log('UE AI Plugin/Module Describer');
  console.log('=============================');
  console.log(`Root: ${rootDir}`);
  console.log(`Dry run: ${dryRun}`);
  console.log(`Headless: ${headless}`);
  console.log(`State file: ${STATE_FILE}`);
  if (daily) console.log(`Daily mode: ${daily} per day`);
  if (limit) console.log(`Limit: ${limit}`);
  if (offset) console.log(`Offset: ${offset}`);
  if (resumeFailed) console.log(`Retry failed: true`);

  console.log('\nScanning for markdown files...');
  const items = findMdFiles(rootDir);
  console.log(`Found ${items.length} items (modules + plugins)`);

  if (items.length === 0) {
    console.log('No items found. Exiting.');
    return;
  }

  const state = loadState();
  console.log(`State: ${state.processed.length} processed, ${state.failed.length} failed`);

  let toProcess;
  if (resumeFailed) {
    toProcess = items.filter(p => state.failed.some(f => f.path === p.path));
    console.log(`Retrying ${toProcess.length} failed items`);
  } else {
    toProcess = items.filter(p => !state.processed.includes(p.path));
    console.log(`Pending: ${toProcess.length}`);
  }

  if (toProcess.length === 0) {
    console.log('All items processed!');
    return;
  }

  if (offset > 0) {
    toProcess = toProcess.slice(offset);
    console.log(`Offset applied: starting from item ${offset}, ${toProcess.length} remaining`);
  }

  const batchSize = daily || limit;
  if (batchSize > 0) {
    toProcess = toProcess.slice(0, batchSize);
    console.log(`Processing batch of ${toProcess.length} items`);
  }

  console.log('\nInitializing AI client...');
  const client = new UEAIClient({
    headless: headless,
    userDataDir: userDataDir,
  });

  try {
    await client.init();
    console.log('AI client ready!');

    let success = 0;
    let failed = 0;
    let skipped = 0;

    for (let i = 0; i < toProcess.length; i++) {
      const item = toProcess[i];
      console.log(`\n[${i + 1}/${toProcess.length}]`);
      const result = await processItem(client, item, state, dryRun);

      if (result === 'success') success++;
      else if (result === 'failed') failed++;
      else skipped++;

      console.log(`Progress: ${success} ok, ${failed} fail, ${skipped} skip`);

      if (i < toProcess.length - 1) {
        const delay = 3000 + Math.random() * 2000;
        console.log(`  Waiting ${Math.round(delay / 1000)}s...`);
        await new Promise(r => setTimeout(r, delay));
      }
    }

    console.log('\n========================================');
    console.log('Done!');
    console.log(`  Success: ${success}`);
    console.log(`  Failed:  ${failed}`);
    console.log(`  Skipped: ${skipped}`);
    console.log(`  Total:   ${toProcess.length}`);
    console.log(`  State:   ${state.processed.length} total processed`);

    process.exit(failed > 0 && success === 0 ? 1 : 0);
  } catch (e) {
    console.error('Fatal error:', e.message);
    console.error(e.stack);
    process.exit(2);
  } finally {
    await client.close();
  }
}

main();
