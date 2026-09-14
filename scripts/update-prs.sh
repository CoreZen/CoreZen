#!/usr/bin/env bash
# Rewrites the upstream-PR table in README.md between the PRS markers.
# Needs: gh (authenticated), python3.
set -euo pipefail
USER="${1:-CoreZen}"
README="${2:-README.md}"

gh search prs --author "$USER" --limit 100 \
  --json repository,title,url,state,closedAt,createdAt \
  --jq "[ .[] | select(.repository.nameWithOwner | startswith(\"$USER/\") | not) ]" > /tmp/prs.json

python3 - "$README" <<'PY'
import json, sys, re
readme = sys.argv[1]
prs = json.load(open('/tmp/prs.json'))
s = open(readme).read()
pinned = set(re.findall(r'https://github\.com/[^/]+/[^/]+/pull/\d+', re.search(r'<!--START_SECTION:pinned-->.*?<!--END_SECTION:pinned-->', s, re.S).group(0)))
rows = ['| Repo | Contribution | Status |', '|---|---|---|']
for p in sorted(prs, key=lambda p: p['closedAt'] or p['createdAt'], reverse=True):
    if p['state'] == 'closed' or p['url'] in pinned:
        continue  # closed-unmerged, or already in the pinned table
    repo = p['repository']['nameWithOwner']
    status = {'merged': 'Merged', 'open': 'Open'}.get(p['state'], 'Closed')
    rows.append(f"| [{repo}](https://github.com/{repo}) | [{p['title']}]({p['url']}) | {status} |")
table = '\n'.join(rows) if len(rows) > 2 else '<sub>Nothing new yet.</sub>'
new = re.sub(r'(<!--START_SECTION:prs-->\n).*?(\n<!--END_SECTION:prs-->)', lambda m: m.group(1) + table + m.group(2), s, flags=re.S)
open(readme, 'w').write(new)
print(f'{len(rows)-2} PRs written')
PY
