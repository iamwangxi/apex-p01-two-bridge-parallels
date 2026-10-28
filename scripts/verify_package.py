#!/usr/bin/env python3
"""Verify the existing manifest before running diagnostics; never rewrites it."""
from hashlib import sha256
from pathlib import Path
import json
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
        if name == 'MANIFEST.sha256' or path.name == '.DS_Store' or '.git' in Path(name).parts:
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


def verify_review_bindings():
    record = json.loads((ROOT/'sources/review-status.json').read_text(encoding='utf-8'))
    seen = set()
    for entry in record['sources']:
        name, expected = entry['integrated_proof'], entry['integrated_proof_sha256']
        path = ROOT/name
        if name in seen or path.is_symlink() or ROOT not in path.resolve().parents:
            raise SystemExit('unsafe or duplicate reviewed proof: ' + name)
        if not re.fullmatch(r'[0-9a-f]{64}', expected):
            raise SystemExit('invalid reviewed proof digest: ' + name)
        if not path.is_file() or sha256(path.read_bytes()).hexdigest() != expected:
            raise SystemExit('reviewed proof mismatch: ' + name)
        for key in ('manuscript_sha256', 'fresh_context_adversarial_review_sha256'):
            if not re.fullmatch(r'[0-9a-f]{64}', entry[key]):
                raise SystemExit('invalid source/review fingerprint: ' + name)
        seen.add(name)
    if not seen:
        raise SystemExit('empty reviewed proof record')
    print('PASS reviewed proof bindings: ' + str(len(seen)) + ' pages', flush=True)


if __name__ == '__main__':
    if sys.argv[1:]:
        raise SystemExit('usage: python3 -B scripts/verify_package.py')
    verify_manifest()
    verify_review_bindings()
    run_all()
    verify_manifest()
