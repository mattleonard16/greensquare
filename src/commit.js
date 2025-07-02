import { DateTime } from 'luxon';
import { readFileSync, writeFileSync, existsSync } from 'fs';
import { execSync } from 'child_process';

try {
  const now = DateTime.now().setZone('America/Los_Angeles');
  const timestamp = now.toISO();
  
  console.log(`🤖 Bot heartbeat at ${timestamp}`);

  let content = '';
  if (existsSync('heartbeat.md')) {
    content = readFileSync('heartbeat.md', 'utf8');
  }

  content += `Bot heartbeat: ${timestamp}\n`;
  writeFileSync('heartbeat.md', content);
  console.log('✅ Updated heartbeat.md');

  process.env.GIT_AUTHOR_DATE = timestamp;
  process.env.GIT_COMMITTER_DATE = timestamp;

  execSync('git add heartbeat.md', { stdio: 'inherit' });
  console.log('✅ Staged heartbeat.md');
  
  execSync('git commit -m "Bot heartbeat"', { stdio: 'inherit' });
  console.log('✅ Created commit');
  
} catch (error) {
  console.error('❌ Error:', error.message);
  process.exit(1);
} 