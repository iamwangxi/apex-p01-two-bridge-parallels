#!/usr/bin/env python3
"""Independent, offline checks; no import or execution of the author's program.

Writes only single_odd_checks.json in this directory.  Graph edges are generated from
the two labelled involutions, and HT restrictions from the individual inner
rectangle counts, before comparison with the stated formulas.  These checks
do not certify the three-dimensional interpretation of those involutions.
"""
from diagnostic_io import save_json
from collections import defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import gcd
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def components(adj):
    unseen = set(adj)
    out = []
    while unseen:
        todo = [min(unseen)]
        part = set()
        while todo:
            x = todo.pop()
            if x in part:
                continue
            part.add(x)
            todo.extend(adj[x] - part)
        unseen -= part
        out.append(frozenset(part))
    return out


def ht_orbits():
    result = []
    for N in range(1, 13):
        unseen = set(product(range(N + 1), repeat=3))
        buckets = {}
        while unseen:
            start = min(unseen)
            todo, part = [start], set()
            while todo:
                x = todo.pop()
                if x in part:
                    continue
                part.add(x)
                for delta in (-1, 1):
                    for move in ((delta, delta, 0), (0, 0, delta)):
                        y = tuple(a + b for a, b in zip(x, move))
                        if all(0 <= v <= N for v in y):
                            todo.append(y)
            unseen -= part
            ds = {x[0] - x[1] for x in part}
            assert len(ds) == 1
            d = ds.pop()
            assert d not in buckets
            buckets[d] = len(part)
        assert set(buckets) == set(range(-N, N + 1))
        result.append(dict(N=N, states=(N + 1)**3,
                           orbit_count=len(buckets),
                           orbit_sizes=buckets,
                           printed_p230_count=N + 1))
    return result


def transport(N, parameters, root=0):
    """Build the matching by reversing the two actual rectangle stacks."""
    frames = {root: tuple(range(N))}
    for direction in (-1, 1):
        v = root
        while 0 <= v + direction <= len(parameters):
            w = v + direction
            n = parameters[min(v, w)]
            rev = tuple(reversed(range(n))) + tuple(reversed(range(n, N)))
            frames[w] = tuple(rev[i] for i in frames[v])
            v = w
    return frames


def restricted_rectangle_counts(N, parameters, orbit, root=0):
    frames = transport(N, parameters, root)
    return tuple(sum(frames[e][i] < n for i in orbit)
                 for e, n in enumerate(parameters))


@lru_cache(None)
def raw_type_word(N, total_U):
    # A representative of x1-x2 = total_U-N, with x3=0.
    x1 = min(N, total_U)
    x2 = N - max(0, total_U - N)
    assert 0 <= x1 <= N and 0 <= x2 <= N
    parameters = (x1, x2, 0)
    out = []
    for i in range(N // 2):
        counts = restricted_rectangle_counts(N, parameters, (i, N - 1 - i))
        out.append(2 + counts[0] - counts[1])
    if N % 2:
        counts = restricted_rectangle_counts(N, parameters, (N // 2,))
        out.append(1 + counts[0] - counts[1])
    return tuple(out)


def ordered_systems():
    tested = 0
    odd_tested = 0
    tables = {}
    for N in range(1, 11):
        for parameters in product(range(N + 1), repeat=3):
            x1, x2, _ = parameters
            U = N + x1 - x2
            c, r = divmod(U, N)
            word = []
            for i in range(N // 2):
                counts = restricted_rectangle_counts(N, parameters,
                                                     (i, N - 1 - i))
                value = 2 + counts[0] - counts[1]
                expected = 2*c + int(i < r) + int(N - 1 - i < r)
                assert value == expected
                word.append(value)
            if N % 2:
                counts = restricted_rectangle_counts(N, parameters, (N // 2,))
                core = 1 + counts[0] - counts[1]
                assert core == c + int(r > N // 2)
                word.append(core)
                odd_tested += 1
            assert tuple(word) == raw_type_word(N, U)
            tested += 1
        tables[str(N)] = {str(U): raw_type_word(N, U)
                          for U in range(2*N + 1)}
    coexist = set()
    for U in range(9):
        word = raw_type_word(4, U)
        coexist.add(tuple(sorted(word)))
    assert coexist == {(j, j) for j in range(5)} | {(j, j+1) for j in range(4)}
    return dict(raw_parameter_tuples=tested, odd_N_tuples=odd_tested,
                coexistence_pairs=sorted(coexist), words=tables)


@lru_cache(None)
def joint(K, u):
    N = 2*K
    positive = {u, (u+1) % N}
    negative = {(u+K) % N, (u+K+1) % N}
    adj = {i: {N-1-i} for i in range(N)}
    for i in range(N):
        if i not in positive | negative:
            adj[i].add((2*u+1-i) % N)
    parts = components(adj)
    legal = (len(parts) == 2 and all(len(V & positive) == len(V & negative) == 1
                                    for V in parts))
    assert legal == (gcd(u+1, K) == 1)
    if not legal:
        return ()
    ans = []
    for V in parts:
        ordered = sorted(V)
        z = next(iter(V & positive))
        k, a = len(V)//2, ordered.index(z)
        I = tuple(i for i in range(K) if i in V)
        assert len(I) == k
        assert gcd(2*a+1, 2*k) == 1
        ans.append((k, a, I, (u+2) % N in V))
    return tuple(ans)


def all_model_edges(kmax):
    edges = set()
    witnesses = 0
    anchors = defaultdict(set)
    first_wave_checks = 0
    for K in range(2, 2*kmax+1):
        for u in range(2*K):
            ps = joint(K, u)
            if not ps or any(v[0] > kmax for v in ps):
                continue
            x, y = ps
            projections = tuple(sorted(((x[0], x[1]), (y[0], y[1]))))
            det = (2*x[1]+1)*y[0] - (2*y[1]+1)*x[0]
            if projections[0] == projections[1]:
                assert det == 0
            else:
                assert abs(det) == 1
                assert x[3] == (x[0] > y[0])
                anchors[projections].add(u)
                first_wave_checks += 1
            for T in range(4*K+1):
                types = raw_type_word(2*K, T)
                vs = [(k, a, sum(types[i] for i in I)) for k, a, I, _ in ps]
                if vs[0] == vs[1]:
                    continue
                edges.add(tuple(sorted(vs)))
                witnesses += 1
    assert all(len(us) == 1 for us in anchors.values())
    vertices = {(k, a, U) for k in range(1, kmax+1) for a in range(2*k)
                if gcd(2*a+1, 2*k) == 1 for U in range(4*k+1)}
    assert all(v in vertices and w in vertices for v, w in edges)
    return vertices, edges, dict(witnesses=witnesses,
                                 nonroot_panels=len(anchors),
                                 first_wave_checks=first_wave_checks)


def flag_triangles(vertices, edges):
    adj = {v: set() for v in vertices}
    for v, w in edges:
        adj[v].add(w)
        adj[w].add(v)
    triangles = set()
    for v, w in edges:
        for z in adj[v] & adj[w]:
            tri = tuple(sorted((v, w, z)))
            triangles.add(tri)
            assert not (adj[v] & adj[w] & adj[z]), 'Unexpected 4-clique'
    return triangles


def collapse(vertices, edges, triangles, protected=frozenset()):
    """Elementary simplicial collapses; protected is a full subcomplex."""
    V, E, T = set(vertices), set(edges), set(triangles)
    edge_tri = {e: set() for e in E}
    for t in T:
        for e in combinations(t, 2):
            edge_tri[e].add(t)
    queue = deque(e for e in E if len(edge_tri[e]) == 1
                  and not set(e) <= protected)
    n2 = 0
    while queue:
        e = queue.popleft()
        if e not in E or len(edge_tri[e]) != 1 or set(e) <= protected:
            continue
        t = next(iter(edge_tri[e]))
        E.remove(e)
        T.remove(t)
        n2 += 1
        for f in combinations(t, 2):
            edge_tri[f].remove(t)
            if f in E and len(edge_tri[f]) == 1 and not set(f) <= protected:
                queue.append(f)
    adj = {v: set() for v in V}
    for v, w in E:
        adj[v].add(w)
        adj[w].add(v)
    queue = deque(v for v in V if len(adj[v]) == 1 and v not in protected)
    n1 = 0
    while queue:
        v = queue.popleft()
        if v not in V or v in protected or len(adj[v]) != 1:
            continue
        w = next(iter(adj[v]))
        e = tuple(sorted((v, w)))
        if edge_tri[e]:
            continue
        E.remove(e)
        V.remove(v)
        adj[w].remove(v)
        adj[v].clear()
        n1 += 1
        if w not in protected and len(adj[w]) == 1:
            queue.append(w)
    if protected:
        assert V == set(protected) and not T
        assert E == {e for e in edges if set(e) <= protected}
    else:
        assert len(V) == 1 and not E and not T
    return dict(triangle_edge_collapses=n2, edge_vertex_collapses=n1,
                remaining_vertices=len(V), remaining_edges=len(E),
                remaining_triangles=len(T))


def check_graph(kmax):
    V, E, info = all_model_edges(kmax)
    projected = {(k, a) for k, a, U in V}
    for k, a in projected:
        fibre = {(kk, aa, U) for kk, aa, U in V if (kk, aa) == (k, a)}
        actual = {e for e in E if set(e) <= fibre}
        expected = {((k, a, U), (k, a, U+1)) for U in range(4*k)}
        assert actual == expected
    base_edges = {tuple(sorted(((v[0], v[1]), (w[0], w[1])))) for v, w in E
                  if v[:2] != w[:2]}
    farey_edges = {tuple(sorted((v, w))) for v, w in combinations(projected, 2)
                   if abs((2*v[1]+1)*w[0] - (2*w[1]+1)*v[0]) == 1}
    assert base_edges == farey_edges
    details = []
    for v, w in sorted(base_edges):
        panelV = {x for x in V if x[:2] in (v, w)}
        panelE = {e for e in E if set(e) <= panelV}
        panelT = flag_triangles(panelV, panelE)
        k, kp = v[0], w[0]
        assert len(panelV) == 4*(k+kp)+2
        assert len(panelE) == 8*(k+kp)+1
        assert len(panelT) == 4*(k+kp)
        assert len(panelV)-len(panelE)+len(panelT) == 1
        parent = v if k < kp else w
        protected = frozenset(x for x in panelV if x[:2] == parent)
        collapsed = collapse(panelV, panelE, panelT, protected)
        details.append(dict(base_edge=[v, w], V=len(panelV), E=len(panelE),
                            triangles=len(panelT), euler=1,
                            collapse_to_parent_fibre=collapsed))
    root = (0, 0, 0)
    V.add(root)
    E.update(tuple(sorted((root, v))) for v in V if v[0] == 1)
    for v in projected:
        if v[0] == 1:
            fanV = {root} | {x for x in V if x[:2] == v}
            fanE = {e for e in E if set(e) <= fanV}
            fanT = flag_triangles(fanV, fanE)
            assert (len(fanV), len(fanE), len(fanT)) == (6, 9, 4)
            collapse(fanV, fanE, fanT, frozenset({root}))
    T = flag_triangles(V, E)
    assert len(V)-len(E)+len(T) == 1
    total_collapse = collapse(V, E, T, frozenset({root}))
    return dict(kmax=kmax, vertices=len(V), edges=len(E), triangles=len(T),
                euler=1, base_vertices_with_root=len(projected)+1,
                base_edges_with_root=len(base_edges)+2,
                complete_fibres=len(projected), max_simplex_dimension=2,
                root_fans=2, root_fan_triangles_each=4,
                **info, total_collapse=total_collapse, panels=details)


def expansions(x):
    """Exact Euclidean recursion using integer inequality |b-1/x|<1."""
    @lru_cache(None)
    def rec(a, b):
        if a == 0:
            return ((),)
        z = Fraction(b, a)
        floor = z.numerator // z.denominator
        answer = []
        for n in range(floor-1, floor+3):
            if abs(n) < 2 or abs(n-z) >= 1:
                continue
            y = n-z
            if y:
                assert y.denominator < Fraction(a, b).denominator
            for tail in rec(y.numerator, y.denominator):
                answer.append((n,)+tail)
        return tuple(answer)
    return {(r, tail) for r in (0, 1)
            for tail in rec((x-r).numerator, (x-r).denominator)}


def d_family():
    result = []
    for m in range(2, 201):
        x = Fraction(8*m, 20*m-1)
        rows = expansions(x)
        neg = (-2,)*(2*m-2)
        expected = {(0, (2,-3)+neg+(-3,)), (0, (2,-2,2*m-1,-2)),
                    (0, (2,-2,2*m,2)), (0, (3,2,2*m,-2)),
                    (0, (3,2,2*m+1,2)), (1, (-2,-4)+neg+(-3,)),
                    (1, (-2,-3,2*m-1,-2)), (1, (-2,-3,2*m,2))}
        assert rows == expected
        slopes = {row: 2*(sum(1 if b > 0 else -1 for b in row[1])-2)
                  for row in rows}
        assert sorted((r,b) for (r,b),s in slopes.items() if s == 0) == [
            (0, (2,-2,2*m,2)), (0, (3,2,2*m,-2))]
        result.append(dict(m=m, expansion_count=len(rows), zero_carriers=2,
                           slopes=sorted(slopes.values())))
    return result


def parent_and_subchain(k, a):
    if k == 1:
        return None
    N = 2*k
    terminals = {a, (a+k) % N}
    adj = {i: {N-1-i} for i in range(N)}
    for i in range(N):
        if i not in terminals:
            adj[i].add((2*a-i) % N)
    e = ((a+1) % N, (a-1) % N)
    adj[e[0]].remove(e[1])
    adj[e[1]].remove(e[0])
    V = next(P for P in components(adj) if (a+k) % N in P)
    z = next(i for i in V if len(adj[i]) == 1 and i != (a+k) % N)
    kp, ap = len(V)//2, sorted(V).index(z)
    assert 0 < kp < k
    assert abs((2*a+1)*kp - (2*ap+1)*k) == 1
    I = tuple(i for i in range(k) if i in V)
    return kp, ap, I


def descent_check(kmax):
    V, E, _ = all_model_edges(kmax)
    adj = {v: set() for v in V}
    for v, w in E:
        adj[v].add(w)
        adj[w].add(v)
    D = {}
    for k, a, U in V:
        if k == 1:
            continue
        kp, ap, I = parent_and_subchain(k, a)
        values = raw_type_word(2*k, U)
        D[k,a,U] = (kp,ap,sum(values[i] for i in I))
        assert D[k,a,U] in adj[k,a,U]
    tested = 0
    for v, w in E:
        if v[0] == w[0]:
            continue
        high, low = sorted((v,w), reverse=True)
        assert D[high] == low or D[high] in adj[low]
        tested += 1
    return dict(kmax=kmax, lower_neighbours=len(D),
                different_projection_domination_checks=tested)


def main():
    result = dict(
        methodology='Independent implementation; HT geometry remains a mathematical input.',
        inputs_sha256={str(p.relative_to(BASE)): sha256(p.read_bytes()).hexdigest()
                       for p in (BASE/'proof/ordered-systems.md',
                                 BASE/'proof/odd-edges.md',
                                 BASE/'proof/band-heights.md')},
        ht_move_orbits=ht_orbits(),
        ordered_systems=ordered_systems(),
        finite_complexes=[check_graph(k) for k in (2,4,6,8,10)],
        descent=descent_check(12),
        d_family=d_family(),
    )
    target = HERE/'single_odd_checks.json'
    save_json(target, result)
    print(json.dumps({
        'output':target.name,
        'ht_orbit_N_max':12,
        'ordered_parameter_tuples':result['ordered_systems']['raw_parameter_tuples'],
        'finite_complexes':[{key:c[key] for key in (
            'kmax','vertices','edges','triangles','euler','nonroot_panels',
            'complete_fibres','total_collapse')} for c in result['finite_complexes']],
        'descent':result['descent'],
        'D_m_checked':[2,200],
        'status':'all assertions passed',
    },ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
