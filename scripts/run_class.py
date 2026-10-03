"""Run JUnit methods; resume after timeouts without rerunning measured methods."""
import argparse
from collections import Counter
import json
from pathlib import Path
import subprocess
import time


def invoke(command, timeout):
    start = time.monotonic()
    try:
        result = subprocess.run(command, capture_output=True, text=True, errors='replace', timeout=timeout)
        out, err, code = result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired as exc:
        def decode(value):
            return value.decode('utf-8', errors='replace') if isinstance(value, bytes) else (value or '')
        out, err, code = decode(exc.stdout), decode(exc.stderr) + '\nWrapper process timeout', 124
    return dict(command=command, exit_status=code, stdout=out, stderr=err,
                wall_seconds=round(time.monotonic() - start, 3))


def events(text):
    result = []
    for line in text.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict) and isinstance(event.get('method'), str):
            result.append(event)
    return result


def run_class(fqcn, classpath, output, timeout_ms=30000, java_options=()):
    start = time.monotonic()
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    base = ['java', *java_options, '-cp', classpath, 'JsonRunner', fqcn]
    listing = invoke(base + ['--list'], 60)
    methods = [event['method'] for event in events(listing['stdout'])]
    if len(methods) != len(set(methods)):
        raise RuntimeError('Duplicate JUnit method identities: ' + fqcn)
    completed, launches, list_error = {}, [], ''
    if listing['exit_status'] or not methods:
        list_error = f'Listing failed: exit={listing["exit_status"]}; methods={len(methods)}; ' + listing['stderr'][-4000:]
    else:
        while len(completed) < len(methods):
            launch = len(launches) + 1
            command = base + ['--timeout-ms', str(timeout_ms)]
            if completed:
                command += ['--exclude', ','.join(completed)]
            remaining = len(methods) - len(completed)
            result = invoke(command, remaining * (timeout_ms / 1000 + 5) + 60)
            result['launch'] = launch
            launches.append(result)
            current = []
            for event in events(result['stdout']):
                name = event['method']
                if name not in methods or name in completed:
                    raise RuntimeError(f'Unexpected/repeated method {name} in {fqcn}')
                if event.get('status') not in {'pass', 'fail', 'error', 'ignored', 'timeout'}:
                    raise RuntimeError(f'Invalid method status: {event}')
                current.append(event)
                completed[name] = {**event, 'launch': launch}
            if result['exit_status'] == 3 and any(e['status'] == 'timeout' for e in current):
                continue
            if len(completed) < len(methods):
                tail = result['stderr'][-4000:]
                for name in methods:
                    if name not in completed:
                        completed[name] = dict(method=name, status='not-run', exception=None,
                                               message=f'JVM exited {result["exit_status"]}; stderr tail: {tail}',
                                               milliseconds=None, launch=launch)
            break
    measured = [completed[name] for name in methods if name in completed]
    output.write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in measured))
    summary = dict(fqcn=fqcn, classpath=classpath, timeout_ms=timeout_ms, listed_methods=methods,
                   listing=listing, list_error=list_error, launches=launches,
                   methods=measured, counts=dict(Counter(row['status'] for row in measured)),
                   wall_seconds=round(time.monotonic() - start, 3))
    output.with_suffix('.summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False) + '\n')
    if list_error:
        raise RuntimeError(list_error)
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('fqcn')
    parser.add_argument('--classpath', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--timeout-ms', type=int, default=30000)
    args = parser.parse_args()
    summary = run_class(args.fqcn, args.classpath, args.output, args.timeout_ms)
    print(json.dumps(dict(fqcn=args.fqcn, counts=summary['counts'], launches=len(summary['launches']))))
