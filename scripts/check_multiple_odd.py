#!/usr/bin/env python3
"""Independent, offline finite audit. Imports no author code; writes here only.

The local plumbing permutation is a hypothesis of the model, checked against
the source drawings separately. Edges are built by restricting raw rectangles,
not by calling the manuscript's summed-height edge routine.
"""
from diagnostic_io import save_json
from collections import defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product, combinations
from math import gcd, floor, ceil
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ROOT = (0, 0, ())


def heights(rectangles, root):
    out = [0] * (len(rectangles) + 1)
    for j in range(root + 1, len(out)):
        out[j] = rectangles[j - 1] - out[j - 1]
    for j in range(root - 1, -1, -1):
        out[j] = rectangles[j] - out[j + 1]
    return tuple(out)


def components(n, permutations):
    parent = list(range(n))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for perm in permutations:
        for i, j in enumerate(perm):
            parent[find(i)] = find(j)
    groups = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)
    return tuple(sorted(tuple(g) for g in groups.values()))


class Plumbing:
    def __init__(self, name, coefficients, root):
        self.name = name
        self.b = tuple(coefficients)
        self.root = root
        self.large = tuple(i for i, b in enumerate(self.b) if abs(b) > 2)
        self.odd = tuple(i for i, b in enumerate(self.b) if b % 2)
        assert root in self.odd

    def key(self, rectangles):
        h = heights(rectangles, self.root)
        return tuple(h[v] for v in self.large)

    def raw(self, n, rectangles):
        """Trace actual finite permutations and selected inner rectangles."""
        maps = [None] * len(self.b)
        maps[self.root] = tuple(range(n))
        order = list(range(self.root + 1, len(self.b)))
        order += list(range(self.root - 1, -1, -1))
        for v in order:
            p = v - 1 if v > self.root else v + 1
            cut = rectangles[min(v, p)]
            maps[v] = tuple((cut - 1 - i) % n for i in maps[p])
        folds = []
        hs = heights(rectangles, self.root)
        for v in self.odd:
            inverse = {j: i for i, j in enumerate(maps[v])}
            f = tuple(inverse[n - 1 - j] for j in maps[v])
            assert f == tuple((-1-i-2*((-1)**abs(v-self.root))*hs[v]) % n
                              for i in range(n))
            folds.append(f)
        orbits = components(n, folds)
        selected = []
        for orbit in orbits:
            counts = tuple(sum(maps[v][i] < cut for i in orbit)
                           for v, cut in enumerate(rectangles))
            ch = heights(counts, self.root)
            # The signed interval formula is checked against raw rectangles.
            for v, h in enumerate(hs):
                q, r = divmod(h, n)
                assert ch[v] == len(orbit)*q + sum(i < r for i in orbit)
            selected.append(counts)
        d = n
        for v in self.odd:
            d = gcd(d, 2*hs[v])
        predicted = components(n, [tuple((i+d) % n for i in range(n)),
                                   tuple(n-1-i for i in range(n))])
        assert predicted == orbits
        return orbits, tuple(selected)

    @lru_cache(None)
    def systems(self, n):
        """Every raw parameter tuple, then quotient by the proposed invariant."""
        representatives = {}
        for rectangles in product(range(n + 1), repeat=len(self.b) - 1):
            key = self.key(rectangles)
            orbit, selected = self.raw(n, rectangles)
            component_keys = tuple(self.key(c) for c in selected)
            record = (rectangles, orbit, selected, component_keys)
            if key in representatives:
                old = representatives[key]
                assert (old[1], old[3]) == (orbit, component_keys)
            else:
                representatives[key] = record
        # Independent strip-inequality enumeration; compare every state.
        bounds = []
        for v in self.large:
            dist = abs(v - self.root)
            bounds.append(range(-n*(dist//2), n*((dist+1)//2)+1))
        predicted = set()
        for key in product(*bounds):
            hs = dict(zip(self.large, key))
            if hs[self.root]:
                continue
            if all(-n*((w-v)//2) <= hs[w]-((-1)**(w-v))*hs[v]
                   <= n*((w-v+1)//2)
                   for v, w in zip(self.large, self.large[1:])):
                predicted.add(key)
        assert predicted == set(representatives)
        return representatives

    def move_quotient(self, n):
        unseen = set(product(range(n+1), repeat=len(self.b)-1))
        keys = set()
        while unseen:
            start = next(iter(unseen))
            found = {start}
            todo = [start]
            while todo:
                x = todo.pop()
                for i, b in enumerate(self.b):
                    if abs(b) != 2:
                        continue
                    for sgn in (-1, 1):
                        y = list(x)
                        for j in (i-1, i):
                            if 0 <= j < len(y):
                                y[j] += sgn
                        y = tuple(y)
                        if min(y) >= 0 and max(y) <= n and y not in found:
                            found.add(y)
                            todo.append(y)
            key = self.key(start)
            assert {self.key(x) for x in found} == {key}
            assert key not in keys
            keys.add(key)
            unseen -= found
        assert keys == set(self.systems(n))
        return len(keys)


def graph_parts(n, edges):
    adj = [set() for _ in range(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    out, seen = [], set()
    for i in range(n):
        if i in seen:
            continue
        part, todo = set(), [i]
        while todo:
            j = todo.pop()
            if j not in part:
                part.add(j)
                todo.extend(adj[j]-part)
        seen |= part
        out.append(part)
    return out


@lru_cache(None)
def joint(k, anchor):
    n = 2*k
    plus = {anchor, (anchor+1) % n}
    minus = {(anchor+k) % n, (anchor+k+1) % n}
    ports = plus | minus
    edges = [(i, n-1-i) for i in range(n)]
    edges += [(i, (2*anchor+1-i) % n) for i in range(n) if i not in ports]
    parts = graph_parts(n, edges)
    legal = len(parts) == 2 and all(len(p & plus) == len(p & minus) == 1
                                  for p in parts)
    assert legal == (gcd(anchor+1, k) == 1)
    if not legal:
        return ()
    return tuple((tuple(sorted(p)), sorted(p).index(next(iter(p & plus))))
                 for p in parts)


def sign_assembly(n, orbits, anchor):
    """Uses only alternating oriented boundary signs, not fold-edge signs."""
    end = (anchor+n//2) % n
    constraints = []
    for orbit in orbits:
        if len(orbit) % 2:
            return False
        constraints += list(zip(orbit, orbit[1:]+orbit[:1]))
    constraints += [(i, (2*anchor-i) % n) for i in range(n)
                    if i not in (anchor, end)]
    adj = [[] for _ in range(n)]
    for i, j in constraints:
        adj[i].append(j)
        adj[j].append(i)
    colours = {}
    for start, value, forced in ([(anchor, 1, True), (end, -1, True)]
                                 +[(i, 1, False) for i in range(n)]):
        if start in colours:
            if forced and colours[start] != value:
                return False
            continue
        colours[start] = value
        todo = [start]
        while todo:
            i = todo.pop()
            for j in adj[i]:
                if j in colours:
                    if colours[j] == colours[i]:
                        return False
                else:
                    colours[j] = -colours[i]
                    todo.append(j)
    return True


@lru_cache(None)
def cut_data(k, anchor):
    n = 2*k
    wave = {(anchor+1) % n, (anchor-1) % n}
    edges = [(i, n-1-i) for i in range(n)]
    edges += [(i, (2*anchor-i) % n) for i in range(n)
              if i not in (anchor, (anchor+k) % n)
              and {i, (2*anchor-i) % n} != wave]
    part = next(p for p in graph_parts(n, edges) if (anchor+k) % n in p)
    pos = next(iter(part & wave))
    return tuple(sorted(part)), sorted(part).index(pos)


def restriction(model, record, part):
    _, orbits, counts, _ = record
    chosen = [c for o, c in zip(orbits, counts) if set(o) <= set(part)]
    assert sum(len(o) for o in orbits if set(o) <= set(part)) == len(part)
    return tuple(sum(c[j] for c in chosen) for j in range(len(model.b)-1))


def scalar_value(k, h, i):
    # Count the infinite periodic pair directly in a signed integer interval.
    lo, hi, sign = (0, h, 1) if h >= 0 else (h, 0, -1)
    return sign*sum(j % (2*k) in (i, 2*k-1-i) for j in range(lo, hi))


@lru_cache(None)
def scalar_ranks(k, anchor, distance):
    low, high = -2*k*(distance//2), 2*k*((distance+1)//2)
    paths = joint(2*k, 2*anchor)
    wave_point = (2*anchor+2) % (4*k)
    owner = next(i for i, (p, _) in enumerate(paths) if wave_point in p)
    outgoing = {h: [] for h in range(low, high+1)}
    for h in range(low, high):
        profile = [scalar_value(2*k, 2*h+1, i) for i in range(2*k)]
        vals = [sum(profile[i] for i in p if i < 2*k) for p, _ in paths]
        assert sorted(vals) == [h, h+1]
        outgoing[vals[owner]].append(vals[1-owner])
    @lru_cache(None)
    def rank(h, visited=()):
        assert h not in visited
        return max([0]+[1+rank(j, visited+(h,)) for j in outgoing[h]])
    return {h: rank(h) for h in outgoing}


def check_complex(model, cap=4):
    vertices = {ROOT}
    records = {}
    sign_checks, rejected_larger = 0, 0
    for k in range(1, cap+1):
        for key, record in model.systems(2*k).items():
            good = all(len(o) == 2 for o in record[1])
            for a in range(2*k):
                compatible = sign_assembly(2*k, record[1], a)
                sign_checks += 1
                if not good:
                    assert not compatible
                    rejected_larger += 1
                if good and gcd(2*a+1, 2*k) == 1:
                    assert compatible
                    v = (k, a, key)
                    vertices.add(v)
                    records[v] = record
    adj = {v: set() for v in vertices}
    def add(v, w):
        assert v in adj and w in adj
        if v != w:
            adj[v].add(w)
            adj[w].add(v)
    for v in vertices:
        if v[0] == 1:
            add(v, ROOT)
    edge_owners = {}
    witnesses = 0
    for total in range(2, 2*cap+1):
        for u in range(2*total):
            paths = joint(total, u)
            if not paths or any(len(p) > 2*cap for p, a in paths):
                continue
            for key, record in model.systems(2*total).items():
                if any(len(o) != 2 for o in record[1]):
                    continue
                pair = []
                for part, a in paths:
                    raw = restriction(model, record, part)
                    pair.append((len(part)//2, a, model.key(raw)))
                v, w = pair
                if v == w:
                    continue
                add(v, w)
                witnesses += 1
                if total > 2:
                    owner = next(vv for vv, (part, a) in zip(pair, paths)
                                 if (u+2) % (2*total) in part)
                    edge = frozenset(pair)
                    assert edge not in edge_owners or edge_owners[edge] == owner
                    edge_owners[edge] = owner
    def signature(v):
        return tuple(v[2][model.large.index(i)]//v[0]
                     for i in model.odd if i != model.root)
    def rank(v):
        if v[0] < 2:
            return 0
        return sum(scalar_ranks(v[0], v[1], abs(i-model.root))[h]
                   for i, h in zip(model.large, v[2]) if i not in model.odd)
    down = {}
    for v in vertices-{ROOT}:
        k, a, key = v
        if k == 1:
            down[v] = ROOT
        else:
            part, ap = cut_data(k, a)
            raw = restriction(model, records[v], part)
            down[v] = (len(part)//2, ap, model.key(raw))
            assert down[v] in adj[v]
            assert 0 < down[v][0] < k
            assert abs((2*a+1)*down[v][0]-(2*ap+1)*k) == 1
    domination = 0
    for edge, owner in edge_owners.items():
        v, w = tuple(edge)
        assert signature(v) == signature(w)
        determinant = abs((2*v[1]+1)*w[0]-(2*w[1]+1)*v[0])
        assert determinant in (0, 1)
        if v[0] != w[0]:
            assert owner == max((v, w), key=lambda vv: vv[0])
        else:
            assert v[:2] == w[:2]
            if v[0] > 1:
                assert rank(v) != rank(w)
                assert owner == max((v, w), key=rank)
        if owner[0] > 1:
            other = next(x for x in edge if x != owner)
            assert down[owner] == other or down[owner] in adj[other]
            domination += 1
    # Full finite induced graph, then the manuscript's actual deletion order.
    remaining = set(vertices)
    deletion = []
    while len(remaining) > 1:
        v = max(remaining-{ROOT}, key=lambda x: (x[0], rank(x), x[1], x[2]))
        d = down[v]
        assert d in remaining
        neighbours = adj[v] & remaining
        assert neighbours <= (adj[d] | {d})
        assert v in adj[d]
        remaining.remove(v)
        deletion.append((v, d, len(neighbours)))
    # Count cliques independently, as a secondary Euler-characteristic check.
    ordered = sorted(vertices)
    ids = {v: i for i, v in enumerate(ordered)}
    f = defaultdict(int)
    def cliques(candidates, size):
        while candidates:
            v = min(candidates, key=ids.get)
            candidates.remove(v)
            f[size+1] += 1
            cliques(candidates & adj[v], size+1)
    cliques(set(vertices), 0)
    euler = sum((1 if i % 2 else -1)*count for i, count in f.items())
    assert euler == 1
    graph_file = HERE/(model.name+'-finite-flag.json')
    data = {'vertices': ordered,
            'edges': sorted((ids[v], ids[w]) for v in adj for w in adj[v]
                            if ids[v] < ids[w]),
            'deletions': [(ids[v], ids[d], degree) for v, d, degree in deletion],
            'root_id': ids[ROOT]}
    save_json(graph_file, data)
    return dict(name=model.name, coefficients=model.b, root=model.root,
                maximum_k=cap, winding_chart=0, vertices=len(vertices),
                edges=sum(map(len, adj.values()))//2,
                edge_witnesses=witnesses, sign_checks=sign_checks,
                rejected_larger_assemblies=rejected_larger,
                signatures=len({signature(v) for v in vertices-{ROOT}}),
                domination_checks=domination, deleted_vertices=len(deletion),
                f_vector=[f[i] for i in range(1, max(f)+1)], euler=euler,
                strong_collapse='verified to the common root', graph=graph_file.name)


def fraction_rows(x):
    result = set()
    for r in (0, 1):
        todo = [(x-r, ())]
        while todo:
            tail, word = todo.pop()
            if not tail:
                result.add((r, word))
                continue
            z = 1/tail
            for b in range(floor(z), ceil(z)+1):
                if abs(b) >= 2 and abs(Fraction(b)-z) < 1:
                    new = b-z
                    assert not new or new.denominator < tail.denominator
                    todo.append((new, word+(b,)))
    return result


def check_b_family():
    examples = {}
    for m in range(1, 257):
        x = Fraction(8*m*m+2*m+2, 16*m*m+8*m+5)
        actual = fraction_rows(x)
        expected = {(0, (2, -(2*m+1))+(-2,)*(2*m-1)+(-3,)),
                    (0, (2, -2*m, 2*m, -2)),
                    (0, (2, -2*m, 2*m+1, 2)),
                    (0, (3,)+(2,)*(2*m-1)+(2*m+1, -2)),
                    (0, (3,)+(2,)*(2*m-1)+(2*m+2, 2)),
                    (1, (-2, -(2*m+2))+(-2,)*(2*m-1)+(-3,)),
                    (1, (-2, -(2*m+1), 2*m, -2)),
                    (1, (-2, -(2*m+1), 2*m+1, 2))}
        assert actual == expected and len(actual) == 8
        for r, b in actual:
            y = Fraction(0)
            for c in reversed(b):
                y = 1/(c-y)
            assert r+y == x
        zero = {(r, b) for r, b in actual if sum(1 if c > 0 else -1 for c in b) == 0}
        assert zero == {(0, (2, -2*m, 2*m, -2)),
                        (1, (-2, -(2*m+1), 2*m+1, 2))}
        if m <= 3:
            examples[str(m)] = {'fraction': str(x), 'rows': sorted(actual)}
    return {'m_checked': [1, 256], 'rows_per_m': 8, 'examples': examples}


def original_table_and_carriers():
    original = []
    rows = fraction_rows(Fraction(5, 13))
    for n in range(1, 9):
        count = 0
        for r, b in rows:
            odd = [i for i, c in enumerate(b) if c % 2]
            if not odd:
                count += int(n == 1)
            else:
                model = Plumbing('HT_table', b, odd[0])
                count += sum(len(record[1]) == 1 for record in model.systems(n).values())
        original.append(count)
    assert original == [7, 8, 4, 4, 8, 8, 12, 8]
    actual = []
    for x, wanted in [(Fraction(12, 29), (-2, -3, 3, 2)),
                       (Fraction(74, 103), (-4, -2, 4, -3)),
                       (Fraction(76, 119), (-3, -4, 3, -3))]:
        rows = fraction_rows(x)
        even = [(r, b) for r, b in rows if all(c % 2 == 0 for c in b)]
        assert len(even) == 1
        signed = lambda b: sum(1 if c > 0 else -1 for c in b)
        zero = sorted((r, b) for r, b in rows if signed(b) == signed(even[0][1]))
        assert (1, wanted) in zero
        assert all(len(b) % 2 == 0 for r, b in zero)
        actual.append({'fraction': str(x), 'all_even': even[0], 'zero_carriers': zero})
    return {'HT_5_13_printed_page_231': original, 'actual_examples': actual}


def larger_examples():
    m = Plumbing('12_29', (-2, -3, 3, 2), 1)
    out = []
    cases = [(4, 1), (4, 3), (6, 2), (8, 2), (12, 2), (12, 3)]
    for n, inner in cases:
        orbits, counts = m.raw(n, (0, inner, 0))
        valid = [a for a in range(n) if sign_assembly(n, orbits, a)]
        assert not valid
        out.append({'N': n, 'n2': inner, 'boundary_orbits': orbits,
                    'orientable_genera': [1+len(o) for o in orbits],
                    'compatible_anchors': valid})
    # Exhaust all two-fold divisors/anchors, beyond the concrete examples.
    tests = 0
    for n in range(2, 65, 2):
        for d in range(2, n+1, 2):
            if n % d:
                continue
            orbits = components(n, [tuple((i+d) % n for i in range(n)),
                                    tuple(n-1-i for i in range(n))])
            for a in range(n):
                colourable = sign_assembly(n, orbits, a)
                if d < n:
                    assert not colourable
                tests += 1
    return {'examples': out, 'divisor_sign_tests': tests, 'maximum_N': 64}


def main():
    watched = ['proof/band-heights.md', 'proof/assembly-obstruction.md',
               'proof/finite-contraction.md', 'proof/main-theorem.md']
    before = {name: sha256((BASE/name).read_bytes()).hexdigest() for name in watched}
    models = [Plumbing('12_29', (-2, -3, 3, 2), 1),
              Plumbing('74_103', (-4, -2, 4, -3), 3),
              Plumbing('76_119', (-3, -4, 3, -3), 0)]
    result = {'assumptions': ['HT local square permutation P_n (source-figure audit separate)',
                              'the inherited geometric width-one and efficient-cut interfaces'],
              'independence': 'No author code imported. Raw rectangles, DSU folds, boundary-sign constraints, raw restrictions and full induced graph collapses.',
              'source_sha256': before,
              'bounded_move_orbits': {m.name: {str(n): m.move_quotient(n)
                                               for n in range(1, 7)} for m in models},
              'B_family': check_b_family(), 'larger_pieces': larger_examples(),
              'original_table_and_carriers': original_table_and_carriers()}
    result['finite_complexes'] = []
    for model in models:
        checked = check_complex(model, 4)
        result['finite_complexes'].append(checked)
        print(json.dumps(checked, ensure_ascii=False), flush=True)
    after = {name: sha256((BASE/name).read_bytes()).hexdigest() for name in watched}
    assert before == after
    result['source_files_unchanged'] = True
    result['script_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    result['status'] = 'all independent finite checks passed'
    save_json(HERE/'multiple_odd_checks.json', result)
    print(result['status'], flush=True)


if __name__ == '__main__':
    main()
