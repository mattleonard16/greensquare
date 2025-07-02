# Daily Green Check Bot

Automated GitHub Action that creates one commit per day at a random time between 08:00 and 20:00 Pacific Time to maintain green squares on your contribution graph.

## How it works

- **Daily trigger**: Runs at 14:50 UTC (07:50 PT) via GitHub Actions cron schedule
- **Random timing**: Sleeps 0-12 hours randomly to commit between 08:00-20:00 PT
- **Smart sleep splitting**: GitHub limits runner timeouts to 6h; the script splits long sleeps accordingly
- **Timezone aware**: Handles PST/PDT automatically using luxon
- **Clean commits**: Sets proper git author/committer dates for accurate contribution graph timing

## Files

- `.github/workflows/daily.yml` - GitHub Action workflow
- `src/commit.js` - Node script that touches heartbeat.md and commits
- `package.json` - Dependencies (luxon for timezone handling)
- `heartbeat.md` - File that gets updated each run

## Testing

Run locally without pushing:
```bash
npm install
npm test
```

## Setup

1. Push this repo to GitHub
2. Enable Actions in repo settings
3. Test manually using the "workflow_dispatch" button in Actions tab
4. Verify permissions allow the bot to commit and push

## Important Notes

- Keep repo private - GitHub's spam policy discourages automated activity in public repos
- Uses only built-in GITHUB_TOKEN, no additional secrets needed
- Disable workflow in Actions tab to pause the bot
- First run should be tested manually to ensure permissions work 