#!/usr/bin/env python3
"""Rooted band-height finite diagnostics, never a substitute for the geometric lemmas.

Run python3 -B on this file. Writes only sibling JSON files; --check is a read-only replay.
"""
from diagnostic_io import save_json
from collections import deque, defaultdict
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json


@lru_cache(None)
def tails(x):
    if not x:
        return ((),)
    z = 1 / x
    f = z.numerator // z.denominator
    return tuple((b,) + t for b in range(f - 1, f + 3)
                 if abs(b) >= 2 and abs(b - z) < 1
                 for t in tails(b - z))


def expansions(x):
    return {(r, b) for r in (0, 1) for b in tails(x - r)}


def family_d(m):
    neg = (-2,) * (2 * m - 2)
    return {(0, (2, -3) + neg + (-3,)),
            (0, (2, -2, 2 * m - 1, -2)),
            (0, (2, -2, 2 * m, 2)),
            (0, (3, 2, 2 * m, -2)),
            (0, (3, 2, 2 * m + 1, 2)),
            (1, (-2, -4) + neg + (-3,)),
            (1, (-2, -3, 2 * m - 1, -2)),
            (1, (-2, -3, 2 * m, 2))}


def family_b(m):
    neg = (-2,) * (2 * m - 1)
    pos = (2,) * (2 * m - 1)
    return {(0, (2, -(2 * m + 1)) + neg + (-3,)),
            (0, (2, -2 * m, 2 * m, -2)),
            (0, (2, -2 * m, 2 * m + 1, 2)),
            (0, (3,) + pos + (2 * m + 1, -2)),
            (0, (3,) + pos + (2 * m + 2, 2)),
            (1, (-2, -(2 * m + 2)) + neg + (-3,)),
            (1, (-2, -(2 * m + 1), 2 * m, -2)),
            (1, (-2, -(2 * m + 1), 2 * m + 1, 2))}


def zero_rows(rows):
    e = [b for r, b in rows if all(x % 2 == 0 for x in b)]
    assert len(e) == 1
    sig = lambda b: sum(1 if x > 0 else -1 for x in b)
    return {(r, b) for r, b in rows if sig(b) == sig(e[0])}


@lru_cache(None)
def profile(k, u):
    """Ordered-sheet lemma: block sum in [0, 2*k*L]."""
    c, r = divmod(u, 2 * k)
    ans = tuple(2 * c + (i < r) + (2 * k - 1 - i < r)
                for i in range(k))
    assert sum(ans) == u
    return ans


def face_of(u, v):
    """Cell at u is a face of cell at v in the subdivided cubical box."""
    for a, b in zip(u, v):
        if b % 2 == 0:
            if a != b:
                return False
        elif a not in (b - 1, b, b + 1):
            return False
    return True


@lru_cache(None)
def joint_paths(K, u):
    n = 2 * K
    positive = {u, (u + 1) % n}
    negative = {(u + K) % n, (u + K + 1) % n}
    terminals = positive | negative
    adj = [set() for _ in range(n)]
    for i in range(n):
        j = (-1 - i) % n
        adj[i].add(j)
        adj[j].add(i)
        if i not in terminals:
            j = (2 * u + 1 - i) % n
            adj[i].add(j)
            adj[j].add(i)
    parts = []
    seen = set()
    for root in range(n):
        if root in seen:
            continue
        todo = [root]
        part = set()
        while todo:
            v = todo.pop()
            if v in part:
                continue
            part.add(v)
            todo.extend(adj[v] - part)
        seen.update(part)
        parts.append(part)
    legal = (len(parts) == 2 and
             all(len(p & positive) == len(p & negative) == 1
                 for p in parts))
    assert legal == (gcd(u + 1, K) == 1)
    if not legal:
        return ()
    ans = []
    for part in parts:
        pos = next(iter(part & positive))
        a = sorted(part).index(pos)
        k = len(part) // 2
        neg = next(iter(part & negative))
        assert sorted(part).index(neg) == (a + k) % (2 * k)
        assert gcd(2 * a + 1, 2 * k) == 1
        indices = tuple(i for i in range(K) if i in part)
        assert len(indices) == k
        first = K > 2 and (u + 2) % n in part
        ans.append((k, a, indices, first))
    return tuple(ans)


@lru_cache(None)
def scalar_rank(k, a, L):
    if k == 1:
        return (0,) * (2 * k * L + 1)
    paths = joint_paths(2 * k, 2 * a)
    assert len(paths) == 2
    assert all(p[0] == k and p[1] == a for p in paths)
    outgoing = [[] for _ in range(2 * k * L + 1)]
    for h in range(2 * k * L):
        pr = profile(2 * k, 2 * h + 1)
        states = [sum(pr[i] for i in p[2]) for p in paths]
        assert sorted(states) == [h, h + 1]
        owner = next(j for j, p in enumerate(paths) if p[3])
        outgoing[states[owner]].append(states[1 - owner])
    visiting = set()
    cache = {}
    def rank(v):
        if v in cache:
            return cache[v]
        assert v not in visiting, 'directed cycle in a scalar fibre'
        visiting.add(v)
        cache[v] = max((1 + rank(w) for w in outgoing[v]), default=0)
        visiting.remove(v)
        return cache[v]
    return tuple(rank(v) for v in range(len(outgoing)))


def rho(vertex, lengths):
    k, a, us = vertex
    return sum(scalar_rank(k, a, L)[u] for L, u in zip(lengths, us))


@lru_cache(None)
def retained(k, a):
    if k == 1:
        return ()
    n = 2 * k
    cut = {(a + 1) % n, (a - 1) % n}
    adj = [set() for _ in range(n)]
    for i in range(n):
        j = (-1 - i) % n
        adj[i].add(j)
        adj[j].add(i)
        if i not in (a, (a + k) % n):
            j = (2 * a - i) % n
            if {i, j} != cut:
                adj[i].add(j)
                adj[j].add(i)
    root = (a + k) % n
    seen = set()
    todo = [root]
    while todo:
        v = todo.pop()
        if v in seen:
            continue
        seen.add(v)
        todo.extend(adj[v] - seen)
    positive = next(iter(seen & cut))
    kp = len(seen) // 2
    ap = sorted(seen).index(positive)
    assert 0 < kp < k
    p = 2 * a + 1
    pp = 2 * ap + 1
    assert abs(p * kp - pp * k) == 1
    return kp, ap, tuple(i for i in range(k) if i in seen)


def descend(vertex):
    k, a, us = vertex
    if k == 1:
        return None
    kp, ap, indices = retained(k, a)
    return kp, ap, tuple(sum(profile(k, u)[i] for i in indices) for u in us)


def edge_key(v, w):
    return tuple(sorted((v, w)))


def matching_diagnostics(lengths, maximum=12):
    edges = set()
    witnesses = 0
    first_checks = 0
    panels = defaultdict(set)
    anchors = defaultdict(set)
    fibres = defaultdict(set)
    for K in range(2, maximum + 1):
        for u in range(2 * K):
            paths = joint_paths(K, u)
            if not paths:
                continue
            ks = [p[0] for p in paths]
            ps = [2 * p[1] + 1 for p in paths]
            determinant = abs(ps[0] * ks[1] - ps[1] * ks[0])
            assert determinant in (0, 1)
            if ks[0] != ks[1]:
                assert K % 2 and paths[0][3] == (ks[0] > ks[1])
                first_checks += 1
            else:
                assert determinant == 0
            for us in product(*(range(2 * K * L + 1) for L in lengths)):
                vertices = []
                for k, a, indices, first in paths:
                    sub = tuple(sum(profile(K, U)[i] for i in indices)
                                for U in us)
                    vertices.append((k, a, sub))
                v, w = vertices
                if v == w:
                    continue
                assert all(0 <= x <= 2 * v[0] * L for x, L in zip(v[2], lengths))
                assert all(0 <= x <= 2 * w[0] * L for x, L in zip(w[2], lengths))
                if v[:2] == w[:2] and v[0] > 1:
                    rv, rw = rho(v, lengths), rho(w, lengths)
                    assert rv != rw
                    assert paths[0][3] == (rv > rw)
                if len(lengths) == 1:
                    if v[:2] == w[:2]:
                        fibres[v[:2]].add(tuple(sorted((v[2][0], w[2][0]))))
                    else:
                        pair = tuple(sorted((v, w)))
                        marker = (pair[0][:2], pair[1][:2])
                        panels[marker].add((pair[0][2][0], pair[1][2][0]))
                        anchors[marker].add(u)
                edges.add(edge_key(v, w))
                witnesses += 1
    domination = 0
    for v, w in edges:
        for source, target in [(v, w), (w, v)]:
            if source[0] < target[0]:
                continue
            if source[0] == target[0] and source[0] > 1:
                if rho(source, lengths) <= rho(target, lengths):
                    continue
            ds = descend(source)
            if ds is None:
                assert target[0] == 1
            elif ds != target:
                assert edge_key(ds, target) in edges, (lengths, source, target, ds)
            domination += 1
    triangles = 0
    if len(lengths) == 1:
        L = lengths[0]
        for marker, points in panels.items():
            k, kp = marker[0][0], marker[1][0]
            ordered = sorted(points, key=sum)
            assert len(anchors[marker]) == 1
            assert [sum(p) for p in ordered] == list(range(2 * (k + kp) * L + 1))
            assert ordered[0] == (0, 0)
            assert ordered[-1] == (2 * k * L, 2 * kp * L)
            assert all((q[0] - p[0], q[1] - p[1]) in ((1, 0), (0, 1))
                       for p, q in zip(ordered, ordered[1:]))
            triangles += len(ordered) - 1
        for (k, a), pairs in fibres.items():
            assert pairs == {(h, h + 1) for h in range(2 * k * L)}
    return dict(lengths=lengths, max_total_k=maximum,
                distinct_edges=len(edges), witnesses=witnesses,
                first_wave_checks=first_checks, domination_checks=domination,
                zipper_disks=len(panels), zipper_triangles=triangles,
                complete_path_fibres=len(fibres))


def block_orbits():
    states = 0
    instances = 0
    for N in range(1, 5):
        for L in range(1, 6):
            unseen = set(product(range(N + 1), repeat=L))
            classes = {}
            while unseen:
                start = next(iter(unseen))
                todo = [start]
                seen = set()
                invariant = sum(x if i % 2 == 0 else N - x
                                for i, x in enumerate(start))
                while todo:
                    x = todo.pop()
                    if x in seen:
                        continue
                    seen.add(x)
                    for i in range(L - 1):
                        for sign in (-1, 1):
                            y = list(x)
                            y[i] += sign
                            y[i + 1] += sign
                            y = tuple(y)
                            if all(0 <= z <= N for z in y):
                                todo.append(y)
                assert invariant not in classes
                assert all(sum(x if i % 2 == 0 else N - x
                               for i, x in enumerate(y)) == invariant for y in seen)
                classes[invariant] = len(seen)
                unseen -= seen
                states += len(seen)
            assert set(classes) == set(range(N * L + 1))
            instances += 1
    return instances, states


def colourable(N, axes, a):
    adj = [set() for _ in range(N)]
    for i in range(N):
        for c in axes:
            j = (c - i) % N
            adj[i].add(j)
            adj[j].add(i)
        if i not in (a, (a + N // 2) % N):
            j = (2 * a - i) % N
            adj[i].add(j)
            adj[j].add(i)
    signs = {}
    for root in range(N):
        if root in signs:
            continue
        signs[root] = 1
        todo = [root]
        while todo:
            i = todo.pop()
            for j in adj[i]:
                if j in signs:
                    if signs[j] == signs[i]:
                        return False
                else:
                    signs[j] = -signs[i]
                    todo.append(j)
    return True


def band_heights(ns, root):
    hs = [None] * (len(ns) + 1)
    hs[root] = 0
    for i in range(root + 1, len(hs)):
        hs[i] = ns[i - 1] - hs[i - 1]
    for i in range(root - 1, -1, -1):
        hs[i] = ns[i] - hs[i + 1]
    return tuple(hs)


def pair_count(N, h, i):
    c, r = divmod(h, N)
    return 2 * c + (i < r) + (N - 1 - i < r)


def transport_checks():
    """Local matching in all charts; augmentation assumes only the root is odd."""
    count = 0
    augmentation = 0
    for N in range(1, 8):
        for s in range(2, 6):
            for root in range(s):
                for ns in product(range(N + 1), repeat=s - 1):
                    hs = band_heights(ns, root)
                    maps = {root: tuple(range(N))}
                    order = list(range(root + 1, s)) + list(range(root - 1, -1, -1))
                    for v in order:
                        parent = v - 1 if v > root else v + 1
                        n = ns[min(v, parent)]
                        maps[v] = tuple((n - 1 - i) % N for i in maps[parent])
                        for i in range(N // 2):
                            selected = sum(maps[parent][q] < n for q in (i, N - 1 - i))
                            assert selected == pair_count(N, hs[v], i) + pair_count(N, hs[parent], i)
                    if N % 2 == 0:
                        bs = []
                        for v, h in enumerate(hs):
                            sign = (-1) ** abs(v - root)
                            z = sign * h
                            bs.append(sign * ((2 * z + N) // (2 * N)))
                        assert bs[root] == 0
                        assert all(bs[i] + bs[i + 1] in (0, 1) for i in range(s - 1))
                        for v, h in enumerate(hs):
                            for i in range(N // 2):
                                assert pair_count(N + 1, h + bs[v], i) == pair_count(N, h, i)
                        augmentation += 1
                    count += 1
    return dict(local_ordered_transport_cases=count,
                one_odd_middle_sheet_augmentations=augmentation)


def configuration(large, odd, root):
    large, odd = tuple(large), tuple(odd)
    assert root in odd and set(odd) <= set(large)
    positions = tuple(v for v in large if v != root)
    edges = []
    ri = large.index(root)
    for i in range(ri + 1, len(large)):
        edges.append((large[i - 1], large[i], large[i] - large[i - 1]))
    for i in range(ri - 1, -1, -1):
        edges.append((large[i + 1], large[i], large[i + 1] - large[i]))
    return (large, odd, root, positions, tuple(edges))


@lru_cache(None)
def height_states(N, config, admissible=True):
    large, odd, root, positions, edges = config
    out = []
    for choices in product(*(range(N * L + 1) for p, c, L in edges)):
        hs = {root: 0}
        for (parent, child, L), u in zip(edges, choices):
            hs[child] = (-1) ** L * hs[parent] + u - N * (L // 2)
        if admissible and N % 2 == 0 and any(2 * hs[v] % N for v in odd):
            continue
        out.append(tuple(hs[v] for v in positions))
    assert len(out) == len(set(out))
    return tuple(out)


def signature(vertex, config):
    k, a, hs = vertex
    large, odd, root, positions, edges = config
    return tuple(hs[positions.index(v)] // k for v in odd if v != root)


def height_rho(vertex, config):
    k, a, hs = vertex
    large, odd, root, positions, edges = config
    ans = 0
    for v, h in zip(positions, hs):
        if v in odd:
            continue
        dist = abs(v - root)
        shifted = h + 2 * k * (dist // 2)
        assert 0 <= shifted <= 2 * k * dist
        ans += scalar_rank(k, a, dist)[shifted]
    return ans


def height_matching(config, maximum=9):
    large, odd, root, positions, reduced = config
    edges = set()
    statesets = {k: set(height_states(2 * k, config)) for k in range(1, maximum + 1)}
    witnesses = 0
    for K in range(2, maximum + 1):
        for u in range(2 * K):
            paths = joint_paths(K, u)
            if not paths:
                continue
            for hs in height_states(2 * K, config):
                vs = []
                for k, a, indices, first in paths:
                    sub = tuple(sum(profile(K, h)[i] for i in indices) for h in hs)
                    assert sub in statesets[k]
                    vs.append((k, a, sub))
                v, w = vs
                if v == w:
                    continue
                assert signature(v, config) == signature(w, config)
                if v[:2] == w[:2] and v[0] > 1:
                    rv, rw = height_rho(v, config), height_rho(w, config)
                    assert rv != rw
                    assert paths[0][3] == (rv > rw)
                edges.add(edge_key(v, w))
                witnesses += 1
    domination = 0
    for v, w in edges:
        for source, target in [(v, w), (w, v)]:
            if source[0] < target[0]:
                continue
            if source[0] == target[0] and source[0] > 1:
                if height_rho(source, config) <= height_rho(target, config):
                    continue
            ds = descend(source)
            if ds is None:
                assert target[0] == 1
            else:
                assert ds[2] in statesets[ds[0]]
                assert signature(ds, config) == signature(source, config)
                if ds != target:
                    assert edge_key(ds, target) in edges, (config, source, target, ds)
            domination += 1
    return dict(large=large, odd=odd, root=root, max_total_k=maximum,
                distinct_edges=len(edges), witnesses=witnesses,
                domination_checks=domination,
                signatures_at_N2=len({tuple(hs[positions.index(v)] for v in odd if v != root)
                                      for hs in height_states(2, config)}))


def ht_table_checks():
    expected = [7, 8, 4, 4, 8, 8, 12, 8]
    rows = expansions(Fraction(5, 13))
    actual = []
    for N in range(1, 9):
        total = 0
        for r, b in rows:
            odd = [i for i, c in enumerate(b) if c % 2]
            large = [i for i, c in enumerate(b) if abs(c) > 2]
            if not odd:
                total += int(N == 1)
                continue
            root = odd[0]
            cfg = configuration(large, odd, root)
            for state in height_states(N, cfg, False):
                hs = {root: 0, **dict(zip(cfg[3], state))}
                d = N
                for v in odd:
                    d = gcd(d, 2 * hs[v])
                components = d // 2 if N % 2 == 0 else (d + 1) // 2
                total += int(components == 1)
        actual.append(total)
    assert actual == expected
    return dict(knot='5/13', physical_pdf_page=7, printed_page=231,
                expected=expected, actual=actual)


def main():
    family_first = {}
    for m in range(2, 101):
        x = Fraction(8 * m, 20 * m - 1)
        rows = expansions(x)
        assert rows == family_d(m)
        assert zero_rows(rows) == {(0, (2, -2, 2 * m, 2)),
                                   (0, (3, 2, 2 * m, -2))}
        if m <= 3:
            family_first['D_' + str(m)] = dict(fraction=str(x), rows=sorted(rows))
    for m in range(1, 101):
        x = Fraction(8 * m * m + 2 * m + 2, 16 * m * m + 8 * m + 5)
        rows = expansions(x)
        assert rows == family_b(m)
        assert zero_rows(rows) == {(0, (2, -2 * m, 2 * m, -2)),
                                   (1, (-2, -(2 * m + 1), 2 * m + 1, 2))}
        if m <= 2:
            family_first['B_' + str(m)] = dict(fraction=str(x), rows=sorted(rows))
    orbit_instances, orbit_states = block_orbits()
    profile_checks = 0
    for k in range(1, 25):
        for lengths in [(1,), (2,), (3,), (4,)]:
            for us in product(*(range(2 * k * L + 1) for L in lengths)):
                words = list(zip(*(profile(k, u) for u in us)))
                assert all(face_of(words[i + 1], words[i]) for i in range(k - 1))
                profile_checks += 1
    folding_checks = 0
    for N in range(2, 31, 2):
        for c in range(1, N, 2):
            for a in range(N):
                result = colourable(N, (1, c), a)
                if c != 1:
                    assert not result
                folding_checks += 1
    matching = [matching_diagnostics((1,), 15),
                matching_diagnostics((2,), 15),
                matching_diagnostics((3,), 15)]
    transports = transport_checks()
    height_models = [
        height_matching(configuration((0, 1, 2), (0,), 0), 10),
        height_matching(configuration((0, 2, 3), (2,), 2), 10),
        height_matching(configuration((0, 1, 2), (0, 2), 0), 10),
        height_matching(configuration((0, 1, 2, 3), (0, 2, 3), 0), 8),
        height_matching(configuration((0, 1, 2, 3), (0,), 0), 8),
        height_matching(configuration((0, 1, 3, 4), (3,), 3), 7),
        height_matching(configuration((0, 1, 2, 4), (0, 2, 4), 2), 8),
    ]
    paper_table = ht_table_checks()
    actual_examples = []
    for x, r, b, cfg, type_count in [
            (Fraction(74, 103), 1, (-4, -2, 4, -3),
             configuration((0, 2, 3), (3,), 3), 15),
            (Fraction(76, 119), 1, (-3, -4, 3, -3),
             configuration((0, 1, 2, 3), (0, 2, 3), 0), 27)]:
        assert (r, b) in zero_rows(expansions(x))
        assert len(height_states(2, cfg)) == type_count
        actual_examples.append(dict(fraction=str(x), carrier=b,
                                    two_sheet_types=type_count))
    result = dict(
        status='all finite diagnostics passed',
        scope='Rooted band heights, including coupled parameter blocks and several odd bands. Geometry is justified separately by the explicit two-block sheet permutation. Independent raw block profiles are NOT asserted.',
        block_orbit_instances=orbit_instances, block_orbit_states=orbit_states,
        profile_checks=profile_checks, signed_folding_checks=folding_checks,
        matching_diagnostics=matching,
        transport_diagnostics=transports,
        height_diagnostics=height_models, HT_original_table=paper_table,
        actual_multiblock_examples=actual_examples,
        D_family_m_checked=[2, 100], B_family_m_checked=[1, 100],
        family_first_rows=family_first,
        script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    output = Path(__file__).resolve().parent / 'general_checks.json'
    save_json(output, result)
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ('family_first_rows', 'script_sha256')},
                     ensure_ascii=False))


if __name__ == '__main__':
    main()
