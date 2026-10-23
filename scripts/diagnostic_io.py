"""Local JSON output and read-only replay; standard library only."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent

def save_json(path, result):
    """Write one sibling result, or compare it under --check without writing."""
    path = Path(path).resolve()
    assert path.parent == HERE, 'diagnostics must stay in scripts/'
    assert set(sys.argv[1:]) <= {'--check'}, 'only --check is supported'
    text = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if '--check' in sys.argv[1:]:
        old = json.loads(path.read_text(encoding='utf-8'))
        new = json.loads(text)
        # Timing is reported, but is not a mathematical invariant.
        if isinstance(old, dict):
            old.pop('elapsed_seconds', None)
            new.pop('elapsed_seconds', None)
        assert old == new, 'saved diagnostics do not match: ' + path.name
    else:
        path.write_text(text, encoding='utf-8')
