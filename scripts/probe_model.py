"""Select the available Mistral 7B model and issue the Step 6 probe."""
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
import requests

BASE = 'https://openrouter.ai/api/v1'

def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def main():
    key = os.environ.get('OPENROUTER_API_KEY')
    if not key:
        Path('results/model-probe.md').write_text('# Model probe\n\nStopped: OPENROUTER_API_KEY is absent or empty inside the container. No API request made.\n')
        raise RuntimeError('OPENROUTER_API_KEY is absent or empty inside the container')
    print('OPENROUTER_API_KEY present (value not displayed).', flush=True)
    response = requests.get(BASE + '/models', timeout=120)
    response.raise_for_status()
    payload = response.json()
    save(Path('results/openrouter-models.json'), payload)
    ids = {m['id'] for m in payload['data'] if 'mistral-7b' in m['id'].lower()}
    print('Matching model IDs:', *sorted(ids), sep='\n', flush=True)
    desired = 'mistralai/mistral-7b-instruct-v0.2'
    if desired in ids:
        model = desired
        reason = 'The exact v0.2 model is listed, matching historical open-mistral-7b.'
    else:
        candidates = ['mistralai/mistral-7b-instruct-v0.3', 'mistralai/mistral-7b-instruct-v0.1', 'mistralai/mistral-7b-instruct']
        model = next((m for m in candidates if m in ids), None)
        if model is None:
            Path('results/model-probe.md').write_text('# Model probe\n\nStopped: no identifiable Mistral 7B Instruct version is listed.\n\nMatching IDs: ' + repr(sorted(ids)) + '\n')
            raise RuntimeError('No identifiable Mistral 7B Instruct model available')
        reason = f'v0.2 is not listed; {model} is the nearest listed Instruct version. Prefer the next release over an equally distant older release.'
    records = json.loads(Path('bundle/Defects4J-dataset.json').read_text(encoding='utf-8', errors='ignore'))
    record = min((r for r in records if r['project_name'] == 'Lang'), key=lambda r: int(r['token_number_zeroshot']))
    prompt = Path('prompts/rendered') / 'Lang' / str(record['bug-id']) / record['class'] / 'ZSL.txt'
    body = {'model': model, 'temperature': 0.7, 'max_tokens': 4096, 'messages': [{'role': 'user', 'content': prompt.read_text()}]}
    root = Path('runs/probe')
    root.mkdir(parents=True, exist_ok=True)
    if (root / 'raw-response.json').exists():
        raise RuntimeError('Existing probe response: refuse duplicate call without review')
    for attempt in range(1, 5):
        target = root if attempt == 1 else root / f'attempt-{attempt}'
        target.mkdir(exist_ok=True)
        save(target / 'request.json', body)
        start = time.monotonic()
        stamp = datetime.now(timezone.utc).isoformat()
        try:
            r = requests.post(BASE + '/chat/completions', headers={'Authorization': 'Bearer ' + key}, json=body, timeout=300)
        except requests.RequestException as e:
            save(target / 'run.json', {'timestamp': stamp, 'latency_seconds': time.monotonic() - start, 'status': 'transport_error', 'exception_type': type(e).__name__, 'attempt': attempt})
            raise RuntimeError('Transport error: see run.json') from None
        (target / 'raw-response.json').write_bytes(r.content)
        meta = {'timestamp': stamp, 'latency_seconds': round(time.monotonic() - start, 3), 'status': r.status_code, 'attempt': attempt, 'model': model, 'bug_id': record['bug-id'], 'class': record['class']}
        save(target / 'run.json', meta)
        if not r.ok:
            if attempt < 4:
                time.sleep(10)
                continue
            raise RuntimeError(f'Probe HTTP error {r.status_code}; retry limit reached')
        result = r.json()
        if 'error' in result or not result.get('choices'):
            raise RuntimeError('Well-formed response has no completion; no retry')
        choice = result['choices'][0]
        content = choice['message'].get('content') or ''
        (target / 'response.md').write_bytes(content.encode('utf-8'))
        save(target / 'usage.json', result.get('usage', {}))
        meta.update({'finish_reason': choice.get('finish_reason'), 'provider': result.get('provider'), 'response_id': result.get('id'), 'start_marker': '###Test START##' in content, 'end_marker': '###Test END##' in content})
        save(target / 'run.json', meta)
        save(Path('results/model-selection.json'), {'model': model, 'reason': reason, 'matching_ids': sorted(ids), 'probe_directory': str(target)})
        lines = ['# Model choice and probe', '', reason, '', 'Matching model IDs: ' + ', '.join(sorted(ids)) + '.', '', f'Record: Lang-{record["bug-id"]} {record["class"]}; authors ZSL tokens: {record["token_number_zeroshot"]}.', '', f'HTTP status: {r.status_code}; finish_reason: {meta["finish_reason"]}; completion tokens: {result.get("usage", {}).get("completion_tokens")}; provider: {meta["provider"]}.', f'Start marker: {meta["start_marker"]}; end marker: {meta["end_marker"]}.', f'Latency: {meta["latency_seconds"]} seconds; attempt: {attempt}.', '', 'First 10 lines:', '', '```text', *content.splitlines()[:10], '```']
        Path('results/model-probe.md').write_text('\n'.join(lines) + '\n')
        print('\n'.join(lines), flush=True)
        return

if __name__ == '__main__':
    main()
