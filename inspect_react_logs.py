import json
from collections import Counter
from pathlib import Path

path = Path('examples/data/solutions.json')
if not path.exists():
    raise FileNotFoundError(path)

with path.open('r', encoding='utf-8') as f:
    data = json.load(f)

counts = Counter()
toolnames = Counter()
sample = None
for sid, sol in data.items():
    if sol.get('baseline') != 'react':
        continue
    if sample is None:
        sample = (sid, sol)
    for msg in sol.get('log', []):
        if msg.get('type') == 'ai':
            if msg.get('name'):
                counts['ai_with_name'] += 1
                toolnames[msg.get('name')] += 1
            if 'tool_calls' in msg:
                counts['tool_calls_field'] += 1
            for k in ['tool_input', 'tool_name', 'tool', 'tool_call', 'tool_execution', 'tool_calls', 'invalid_tool_calls']:
                if k in msg:
                    counts[f'has_{k}'] += 1
            if msg.get('usage_metadata'):
                counts['has_usage_metadata'] += 1
            if msg.get('response_metadata'):
                counts['has_response_metadata'] += 1

print('counts:', counts)
print('toolnames:', toolnames.most_common(20))
if sample:
    sid, sol = sample
    print('sample id', sid, 'loglen', len(sol.get('log', [])))
    for i, msg in enumerate(sol.get('log', [])[:40], 1):
        if msg.get('type') == 'ai':
            print('---', i, 'name=', repr(msg.get('name')), 'keys=', list(msg.keys()))
            if 'usage_metadata' in msg:
                print(' usage_metadata', msg['usage_metadata'])
            if 'response_metadata' in msg:
                print(' response_metadata', msg['response_metadata'])
