#!/usr/bin/env python3
"""Exact finite arithmetic diagnostics; Python standard library only.

Run from the repository root: python3 -B scripts/check.py
Use --check to compare the adjacent checks.json without writing.
These checks do not certify three-dimensional isotopy or contractibility.
The universal mathematical arguments are in proof/.
"""
import argparse
from collections import deque
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json


@lru_cache(None)
def tails(x):
    if x == 0:
        return ((),)
    z = 1 / x
    floor = z.numerator // z.denominator
    out = []
    for b in range(floor - 1, floor + 3):
        if abs(b) < 2 or abs(b - z) >= 1:
            continue
        y = b - z
        assert y == 0 or y.denominator < x.denominator
        out.extend((b,) + t for t in tails(y))
    return tuple(out)


def expansions(x):
    return tuple((r, b) for r in (0, 1) for b in tails(x - r))


def value(b):
    x = Fraction(0)
    for c in reversed(b):
        x = 1 / (c - x)
    return x


def signed_count(b):
    return sum(1 if c > 0 else -1 for c in b)


def table(x):
    rows = expansions(x)
    assert all(r + value(b) == x for r, b in rows)
    even = [(r, b) for r, b in rows if all(c % 2 == 0 for c in b)]
    assert len(even) == 1
    s0 = signed_count(even[0][1])
    return [dict(r=r, b=b, slope=2 * (signed_count(b) - s0),
                 odd_count=sum(c % 2 != 0 for c in b),
                 large_count=sum(abs(c) > 2 for c in b))
            for r, b in rows]


def family_rows(m):
    twos = (2,) * (2 * m - 1)
    return {
        (0, (2, -2, -2, -(2 * m + 1))),
        (0, (3, 3, -2 * m)),
        (0, (3, 4) + twos),
        (1, (-2, -3, -2, -(2 * m + 1))),
        (1, (-2, -2, 2, -2 * m)),
        (1, (-2, -2, 3) + twos),
    }


def check_parameter_box(length, exceptional, n):
    """All HT moves except at one coefficient; exceptional is zero based."""
    dimension = length - 1
    moves = []
    for i in range(length):
        if i == exceptional:
            continue
        v = [0] * dimension
        if i > 0:
            v[i - 1] = 1
        if i < dimension:
            v[i] = 1
        moves.append(v)
    start = (0,) * dimension
    seen = {start}
    queue = deque([start])
    while queue:
        x = queue.popleft()
        for v in moves:
            for sign in (-1, 1):
                y = tuple(a + sign * b for a, b in zip(x, v))
                if all(0 <= a <= n for a in y) and y not in seen:
                    seen.add(y)
                    queue.append(y)
    assert len(seen) == (n + 1) ** dimension
    return len(seen)


def reflection_components(k, a):
    n = 2 * k
    adj = [set() for _ in range(n)]
    for i in range(n):
        j = (-1 - i) % n
        adj[i].add(j)
        adj[j].add(i)
        if i not in (a, (a + k) % n):
            j = (2 * a - i) % n
            adj[i].add(j)
            adj[j].add(i)
    seen = set()
    parts = []
    for i in range(n):
        if i in seen:
            continue
        stack = [i]
        part = set()
        while stack:
            v = stack.pop()
            if v in part:
                continue
            part.add(v)
            stack.extend(adj[v] - part)
        seen.update(part)
        parts.append(part)
    d = gcd(2 * a + 1, n)
    path = [s for s in parts if a in s]
    assert len(path) == 1 and (a + k) % n in path[0]
    assert len(path[0]) == 2 * k // d
    assert len(parts) == 1 + (d - 1) // 2
    assert all(len(s) == 4 * k // d for s in parts if a not in s)
    if d == 1:
        signs = {a: 1}
        todo = [a]
        while todo:
            v = todo.pop()
            for w in adj[v]:
                if w in signs:
                    assert signs[w] == -signs[v]
                else:
                    signs[w] = -signs[v]
                    todo.append(w)
        assert signs[(a + k) % n] == -1
    return d == 1


def parent(p, k):
    assert k > 0 and p % 2 and gcd(p, k) == 1
    if k == 1:
        return (1, 0)
    r = pow(p, -1, k)
    p1 = (p * r - 1) // k
    options = [(p1, r), (p - p1, k - r)]
    good = [v for v in options if v[0] % 2]
    assert len(good) == 1
    return good[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='recompute and compare saved JSON without writing')
    args = parser.parse_args()
    family_checks = []
    for m in range(1, 201):
        x = Fraction(6 * m + 1, 16 * m + 3)
        assert x.denominator == 16 * m + 3
        assert set(expansions(x)) == family_rows(m)
        rows = table(x)
        zero = [r for r in rows if r['slope'] == 0]
        assert len(zero) == 2
        odd = [r for r in zero if r['odd_count']]
        assert len(odd) == 1 and odd[0]['large_count'] == 1
        assert sorted(r['slope'] for r in rows) == sorted(
            [0, 6, 4 * m + 6, -4, 0, 4 * m])
        if m <= 4:
            family_checks.append(dict(m=m, fraction=str(x), rows=rows))
    box_count = 0
    box_states = 0
    for length in range(2, 8):
        for exceptional in range(length):
            for n in range(1, 4):
                box_states += check_parameter_box(length, exceptional, n)
                box_count += 1
    matchings = 0
    for k in range(1, 101):
        for a in range(2 * k):
            reflection_components(k, a)
            matchings += 1
    parent_count = 0
    for k in range(1, 81):
        for p in range(-8 * k + 1, 8 * k, 2):
            if gcd(p, k) != 1:
                continue
            anchor = ((p - 1) // 2) % (2 * k)
            twist = (p - (2 * anchor + 1)) // (4 * k)
            assert p == 2 * anchor + 1 + 4 * k * twist
            assert gcd(2 * anchor + 1, 2 * k) == 1
            pp, kk = parent(p, k)
            assert 0 <= kk < k and abs(p * kk - pp * k) == 1
            if kk:
                assert pp % 2 and gcd(pp, kk) == 1
                pa = ((pp - 1) // 2) % (2 * kk)
                pt = (pp - (2 * pa + 1)) // (4 * kk)
                assert pt == twist
            candidates = set()
            for d in range(1, k):
                for sign in (-1, 1):
                    top = p * d - sign
                    if top % k == 0 and (top // k) % 2:
                        candidates.add((top // k, d))
            if k == 1:
                assert not candidates
            else:
                assert candidates == {(pp, kk)}
            parent_count += 1
    examples = {str(x): table(x) for x in
                (Fraction(8, 21), Fraction(12, 29), Fraction(16, 39))}
    assert len([r for r in examples['8/21']
                if r['slope'] == 0 and r['odd_count']]) == 2
    assert all(r['large_count'] == 1 for r in examples['8/21']
               if r['slope'] == 0 and r['odd_count'])
    assert any(r['slope'] == 0 and r['odd_count'] >= 2
               for r in examples['12/29'])
    assert any(r['slope'] == 0 and r['odd_count'] == 1 and
               r['large_count'] > 1 for r in examples['16/39'])
    result = dict(
        status='all arithmetic diagnostics passed',
        warning='Finite diagnostics only; no geometric or homotopy certification.',
        family_m_checked=[1, 200], family_first_rows=family_checks,
        parameter_boxes=box_count, parameter_box_states=box_states,
        reflection_matchings=matchings,
        farey_parent_coordinates=parent_count,
        examples=examples,
        six_boundary_witness=dict(
            fraction='12/29', carrier=[-2, -3, 3, 2], integer_part=1,
            construction='frontier of a connected three-sheet surface guaranteed by HT Proposition 1(3)',
            boundary_count=6, euler_characteristic=-18, genus=7,
            caveat='Not asserted to extend to a spanning vertex.'),
        script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    output = Path(__file__).resolve().parent / 'checks.json'
    serialized = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.check:
        assert output.read_text(encoding='utf-8') == serialized, 'saved diagnostics do not match'
    else:
        output.write_text(serialized, encoding='utf-8')
    print(json.dumps({k: result[k] for k in
                     ['status', 'parameter_boxes', 'parameter_box_states',
                      'reflection_matchings', 'farey_parent_coordinates']},
                     ensure_ascii=False))


if __name__ == '__main__':
    main()
