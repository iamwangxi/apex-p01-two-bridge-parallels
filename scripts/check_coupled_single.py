#!/usr/bin/env python3
"""Raw-rectangle check for 1+[-4,-2,4,-3], companion K_(74/103).

Independent of the author's script.  Uses the preceding independent
implementation only for endpoint graphs and normal-stack matchings.
Writes coupled_single_checks.json in this directory only.
"""
from diagnostic_io import save_json
from collections import defaultdict
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from math import gcd
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('independent_single_odd', HERE/'check_single_odd.py')
base = module_from_spec(spec)
spec.loader.exec_module(base)


@lru_cache(None)
def raw_states(N):
    states = {}
    for x, y, z in product(range(N+1), repeat=3):
        states.setdefault((x-y+z, z), (x,y,z))
    assert len(states) == (N+1)*(2*N+1)
    return states


@lru_cache(None)
def word(N, h0, h2):
    parameters = raw_states(N)[h0,h2]
    result = []
    for i in range(N//2):
        x, y, z = base.restricted_rectangle_counts(
            N, parameters, (i,N-1-i), root=3)
        result.append((x-y+z,z))
    assert tuple(map(sum, zip(*result))) == (h0,h2)
    return tuple(result)


def scalar(k, h, i):
    c, r = divmod(h,2*k)
    return 2*c + int(i < r) + int(2*k-1-i < r)


def transport_check():
    tested = 0
    for N in range(2,15,2):
        k = N//2
        for parameters in product(range(N+1), repeat=3):
            x,y,z = parameters
            h0,h2 = x-y+z,z
            values = []
            for i in range(k):
                xx,yy,zz = base.restricted_rectangle_counts(
                    N,parameters,(i,N-1-i),root=3)
                value = (xx-yy+zz,zz)
                assert value == (scalar(k,h0,i),scalar(k,h2,i))
                values.append(value)
            assert tuple(values) == word(N,h0,h2)
            tested += 1
    return tested


@lru_cache(None)
def scalar_ranks(k,a,lower,upper):
    ps = base.joint(2*k,2*a)
    owner = next(p for p in ps if p[3])
    other = next(p for p in ps if not p[3])
    out = defaultdict(set)
    for h in range(lower,upper):
        H = 2*h+1
        s = sum(scalar(2*k,H,i) for i in owner[2])
        t = sum(scalar(2*k,H,i) for i in other[2])
        assert {s,t} == {h,h+1}
        out[s].add(t)
    ranks, active = {},set()
    def rank(x):
        if x in ranks:
            return ranks[x]
        assert x not in active
        active.add(x)
        ranks[x] = max((1+rank(y) for y in out[x]),default=0)
        active.remove(x)
        return ranks[x]
    return {h:rank(h) for h in range(lower,upper+1)}


def graph_check(kmax):
    vertices = {(k,a,h0,h2) for k in range(1,kmax+1) for a in range(2*k)
                if gcd(2*a+1,2*k) == 1 for h0,h2 in raw_states(2*k)}
    edges = set()
    for K in range(2,2*kmax+1):
        for u in range(2*K):
            paths = base.joint(K,u)
            if not paths or any(k > kmax for k,a,I,owner in paths):
                continue
            for h0,h2 in raw_states(2*K):
                W = word(2*K,h0,h2)
                pair = []
                for k,a,I,owner in paths:
                    vertex = (k,a,sum(W[i][0] for i in I),sum(W[i][1] for i in I))
                    assert vertex in vertices
                    pair.append(vertex)
                if pair[0] != pair[1]:
                    edges.add(tuple(sorted(pair)))
    root = (0,0,0,0)
    vertices.add(root)
    edges.update(tuple(sorted((root,v))) for v in vertices if v[0] == 1)
    adj = {v:set() for v in vertices}
    for v,w in edges:
        adj[v].add(w)
        adj[w].add(v)
    lower = {}
    ranks = {}
    for v in vertices-{root}:
        k,a,h0,h2 = v
        if k == 1:
            lower[v] = root
            ranks[v] = 0
            continue
        kp,ap,I = base.parent_and_subchain(k,a)
        W = word(2*k,h0,h2)
        lower[v] = (kp,ap,sum(W[i][0] for i in I),sum(W[i][1] for i in I))
        assert lower[v] in adj[v]
        # Distances 3 and 1 from odd root band 3.
        ranks[v] = (scalar_ranks(k,a,-2*k,4*k)[h0]
                    + scalar_ranks(k,a,0,2*k)[h2])
    same_projection_rank_checks = 0
    for v,w in edges:
        if v[0] > 1 and v[:2] == w[:2]:
            assert ranks[v] != ranks[w]
            same_projection_rank_checks += 1
    remain = set(vertices)
    domination_checks = 0
    for v in sorted(vertices-{root},key=lambda v:(v[0],ranks[v]),reverse=True):
        d = lower[v]
        assert d in remain
        assert (adj[v] & remain)-{d} <= adj[d]
        remain.remove(v)
        domination_checks += 1
    assert remain == {root}
    return dict(kmax=kmax,vertices=len(vertices),edges=len(edges),
                types_at_N2=len(raw_states(2)),
                same_projection_rank_checks=same_projection_rank_checks,
                dominated_vertices_removed=domination_checks,
                final_vertices=len(remain),
                all_closed_neighbourhood_inclusions_passed=True)


def main():
    result = dict(carrier='1+[-4,-2,4,-3]',knot='74/103',odd_root=3,
                  large_bands=[0,2,3],raw_parameter_tuples=transport_check(),
                  graphs=[graph_check(k) for k in (2,3,4,5)],
                  status='all assertions passed')
    output = HERE/'coupled_single_checks.json'
    save_json(output, result)
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
