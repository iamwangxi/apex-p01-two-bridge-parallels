#!/usr/bin/env python3
"""Run all thirteen diagnostics read-only. No generation or outside-package I/O."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
COMMANDS = (
    'check.py', 'check_general.py', 'check_single_odd.py',
    'check_coupled_single.py', 'check_multiple_odd.py',
    'check_zero_framed_clusters.py', 'check_zero_framed_independent.py',
    'check_framed_clusters.py', 'check_framed_independent.py',
    'check_recursive_systems.py', 'check_recursive_independent.py',
    'check_recursive_framed.py', 'check_recursive_framed_independent.py',
)


def run_all():
    for name in COMMANDS:
        result = subprocess.run([sys.executable, '-B', str(ROOT/'scripts'/name), '--check'],
                                cwd=ROOT, capture_output=True, text=True)
        if result.returncode:
            print(result.stdout, end='')
            print(result.stderr, end='', file=sys.stderr)
            raise SystemExit(result.returncode)
        print('PASS ' + name, flush=True)
    print('PASS all 13 deterministic read-only diagnostic replays')


if __name__ == '__main__':
    if sys.argv[1:]:
        raise SystemExit('usage: python3 -B scripts/run_all.py')
    run_all()
