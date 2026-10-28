"""Deterministic stdout snapshots, confined to this scripts directory."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent


def replay(function, filename):
    if sys.argv[1:] not in ([], ['--check']):
        raise SystemExit('usage: python3 -B SCRIPT [--check]')
    target = (HERE / filename).resolve()
    if target.parent != HERE or target.suffix != '.txt':
        raise SystemExit('snapshot must be a sibling .txt file')
    buffer = StringIO()
    with redirect_stdout(buffer):
        function()
    output = buffer.getvalue()
    if '--check' in sys.argv:
        if target.read_text(encoding='utf-8') != output:
            raise SystemExit('saved diagnostics do not match: ' + filename)
    else:
        target.write_text(output, encoding='utf-8')
    print(output, end='')
