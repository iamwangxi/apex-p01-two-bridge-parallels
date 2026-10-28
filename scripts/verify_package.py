#!/usr/bin/env python3
"""Verify the existing manifest before running diagnostics; never rewrites it."""
from hashlib import sha256
from pathlib import Path
import re
import sys
from run_all import run_all

ROOT = Path(__file__).resolve().parents[1]


def verify_manifest():
    entries = {}
    for line in (ROOT/'MANIFEST.sha256').read_text(encoding='utf-8').splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        if not match:
            raise SystemExit('invalid manifest line')
        digest, name = match.groups()
        path = ROOT/name
        if name in entries or path.is_symlink() or ROOT not in path.resolve().parents:
            raise SystemExit('unsafe or duplicate manifest entry: ' + name)
        if name == 'MANIFEST.sha256' or path.name == '.DS_Store':
            raise SystemExit('excluded manifest entry: ' + name)
        if not path.is_file() or sha256(path.read_bytes()).hexdigest() != digest:
            raise SystemExit('manifest mismatch: ' + name)
        entries[name] = digest
    files = {str(p.relative_to(ROOT)) for p in ROOT.rglob('*')
             if p.is_file() and p.name not in {'MANIFEST.sha256', '.DS_Store'}
             and '.git' not in p.relative_to(ROOT).parts}
    if set(entries) != files:
        raise SystemExit('manifest coverage mismatch')
    print('PASS existing manifest: ' + str(len(entries)) + ' files', flush=True)


if __name__ == '__main__':
    if sys.argv[1:]:
        raise SystemExit('usage: python3 -B scripts/verify_package.py')
    verify_manifest()
    run_all()
    verify_manifest()
