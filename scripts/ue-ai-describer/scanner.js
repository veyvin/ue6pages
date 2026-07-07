const fs = require('fs');
const path = require('path');

function findMdFiles(rootDir, options = {}) {
  const results = [];
  const categories = options.categories || ['modules', 'plugins'];

  for (const category of categories) {
    const categoryDir = path.join(rootDir, category);
    if (!fs.existsSync(categoryDir)) continue;

    let entries;
    try {
      entries = fs.readdirSync(categoryDir, { withFileTypes: true });
    } catch (e) {
      continue;
    }

    for (const entry of entries) {
      if (entry.isFile() && entry.name.endsWith('.md')) {
        const fullPath = path.join(categoryDir, entry.name);
        const relativePath = path.relative(rootDir, fullPath);
        results.push({
          name: entry.name.replace('.md', ''),
          path: fullPath,
          relativePath,
          dir: categoryDir,
          category: category,
        });
      }
    }
  }

  return results;
}

function readMdFile(filePath) {
  return fs.readFileSync(filePath, 'utf-8');
}

function writeMdFile(filePath, content) {
  fs.writeFileSync(filePath, content, 'utf-8');
}

function parseMdTitle(content) {
  const yamlMatch = content.match(/^---\n([\s\S]*?)\n---/);
  if (yamlMatch) {
    const yaml = yamlMatch[1];
    const titleMatch = yaml.match(/title:\s*(.+)/);
    if (titleMatch) {
      return titleMatch[1].trim();
    }
  }
  const h1Match = content.match(/^#\s+(.+)/m);
  if (h1Match) {
    return h1Match[1].trim();
  }
  return null;
}

function updateMdDescription(filePath, aiContent) {
  const content = readMdFile(filePath);
  const AI_DELIMITER = '\n\n---\n\n### AI Description & Usage Tips\n\n';

  let newContent;
  if (content.includes('### AI Description & Usage Tips')) {
    const parts = content.split(AI_DELIMITER);
    newContent = parts[0] + AI_DELIMITER + aiContent;
  } else {
    const descSection = content.match(/(<h2>Description \/ 描述<\/h2>[\s\S]*?)(<h2>|$)/);
    if (descSection) {
      newContent = content.substring(0, descSection.index + descSection[1].length) + AI_DELIMITER + aiContent + content.substring(descSection.index + descSection[1].length);
    } else {
      newContent = content + AI_DELIMITER + aiContent;
    }
  }

  writeMdFile(filePath, newContent);
  return newContent.length;
}

function hasAIDescription(content) {
  return content && content.includes('### AI Description & Usage Tips');
}

module.exports = {
  findMdFiles,
  readMdFile,
  writeMdFile,
  parseMdTitle,
  updateMdDescription,
  hasAIDescription,
};
