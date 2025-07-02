import { DateTime } from 'luxon';
import { readFileSync, writeFileSync, existsSync } from 'fs';
import { execSync } from 'child_process';

const now = DateTime.now().setZone('America/Los_Angeles');
const timestamp = now.toISO();

let content = '';
if (existsSync('heartbeat.md')) {
  content = readFileSync('heartbeat.md', 'utf8');
}

content += `Bot heartbeat: ${timestamp}\n`;
writeFileSync('heartbeat.md', content);

process.env.GIT_AUTHOR_DATE = timestamp;
process.env.GIT_COMMITTER_DATE = timestamp;

execSync('git config user.name "Green Square Bot"');
execSync('git config user.email "bot@example.com"');
execSync('git add heartbeat.md');
execSync('git commit -m "Bot heartbeat"'); 