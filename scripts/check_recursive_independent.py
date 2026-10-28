#!/usr/bin/env python3
"""Exact offline finite diagnostics; standard library only.
No topology certification. No file access by the mathematical implementation.
"""

from collections import Counter, defaultdict
from itertools import product
from math import gcd
from random import Random
from fractions import Fraction
import json


class Graph:
    def __init__(self):
        self.adj = []
        self.cost = []

    def vertex(self, cost=0):
        i = len(self.adj)
        self.adj.append([])
        self.cost.append(cost)
        return i

    def edge(self, u, v, flip=0):
        self.adj[u].append((v, flip))
        self.adj[v].append((u, flip))

    def solve(self):
        labels = [-1] * len(self.adj)
        signs = [-1] * len(self.adj)
        costs = []
        coherent = True
        for u in range(len(labels)):
            if labels[u] != -1:
                continue
            c = len(costs)
            costs.append(0)
            labels[u], signs[u] = c, 0
            todo = [u]
            while todo:
                v = todo.pop()
                costs[c] += self.cost[v]
                for w, flip in self.adj[v]:
                    if labels[w] == -1:
                        labels[w], signs[w] = c, signs[v] ^ flip
                        todo.append(w)
                    else:
                        assert labels[w] == c
                        coherent &= signs[w] == (signs[v] ^ flip)
        return labels, signs, costs, coherent


def square(n, t):
    # Exact signed-piece or peripheral arithmetic check.
    return list(reversed(range(t))) + list(reversed(range(t, n)))


def inverse(p):
    ans = [0] * len(p)
    for i, j in enumerate(p):
        ans[j] = i
    return ans


def ht(graph, n, beta, weights, slope):
    length = len(beta)
    root = next((i for i, b in enumerate(beta) if b % 2), 0)
    bands = [[graph.vertex(length - 1 if j == root else 0)
              for i in range(n)] for j in range(length)]
    matches = [square(n, t) for t in weights]
    for j, b in enumerate(beta):
        if b % 2:
            for i in range(n):
                graph.edge(bands[j][i], bands[j][n - 1 - i], 1)
    for j, match in enumerate(matches):
        for i, k in enumerate(match):
            graph.edge(bands[j][i], bands[j + 1][k])

    # Exact signed-piece or peripheral arithmetic check.
    transports = {root: list(range(n))}
    for j in range(root, length - 1):
        transports[j + 1] = [matches[j][i] for i in transports[j]]
    for j in range(root - 1, -1, -1):
        inv = inverse(matches[j])
        transports[j] = [inv[i] for i in transports[j + 1]]
    constants = []
    for j, b in enumerate(beta):
        if not b % 2:
            continue
        p = transports[j]
        inv = inverse(p)
        folded = [inv[n - 1 - p[i]] for i in range(n)]
        c = folded[0]
        assert all(folded[i] == (c - i) % n for i in range(n))
        constants.append(c)
    return dict(port=bands[root], slope=slope, density=length - 1,
                constants=constants, root=0 if constants else None,
                children=[], kind="ht", band_vertices=bands,
                matches=matches, weights=weights)


def annuli(graph, n, slope):
    port = [graph.vertex() for _ in range(n)]
    for i in range(n):
        graph.edge(port[i], port[n - 1 - i], 1)
    return dict(port=port, slope=slope, density=0,
                constants=[n - 1], root=0, children=[], kind="annuli")


def combine(graph, children, shifts, kind, p=None, q=None):
    if kind == "sum":
        n = len(children[0]["port"])
        assert all(len(c["port"]) == n for c in children)
        density_local = len(children) - 1
        slope = sum(c["slope"] for c in children)
    else:
        assert len(children) == 1 and gcd(p, q) == 1 and p >= 2
        n = len(children[0]["port"]) // p
        assert p * n == len(children[0]["port"])
        s = children[0]["slope"]
        slope = p * p * s
        density_local = (p - 1) * abs(q - p * s)
        assert density_local > 0
    port = [graph.vertex(density_local) for _ in range(n)]
    constants = []
    selected = None
    for child, shift in zip(children, shifts):
        for inner, v in enumerate(child["port"]):
            graph.edge(port[(inner - shift) % n], v)
        constants.extend((c - 2 * shift) % n for c in child["constants"])
        if selected is None and child["root"] is not None:
            selected = (child, shift)
    root = None if selected is None else (selected[0]["root"] - selected[1]) % n
    density = density_local + sum(c["density"] for c in children) * (
        p if kind == "cable" else 1)
    return dict(port=port, slope=slope, density=density,
                constants=constants, root=root, children=children,
                shifts=shifts, kind=kind, selected=selected)


def partition(labels):
    parts = defaultdict(list)
    for i, c in enumerate(labels):
        parts[c].append(i)
    return sorted(tuple(p) for p in parts.values())


def reflection_partition(n, constants):
    remaining = set(range(n))
    parts = []
    while remaining:
        start = min(remaining)
        orbit = {start}
        todo = [start]
        while todo:
            i = todo.pop()
            for c in constants:
                j = (c - i) % n
                if j not in orbit:
                    orbit.add(j)
                    todo.append(j)
        remaining -= orbit
        parts.append(tuple(sorted(orbit)))
    return sorted(parts)


def check_tree_word(word, number):
    current = 0
    endpoints = {}
    degree = Counter()
    next_vertex = 1
    for e in word:
        if e not in endpoints:
            endpoints[e] = (current, next_vertex)
            degree[current] += 1
            degree[next_vertex] += 1
            current = next_vertex
            next_vertex += 1
        else:
            a, b = endpoints[e]
            assert current == a or current == b
            current = b if current == a else a
    assert current == 0 and len(endpoints) == number
    assert max(degree.values()) <= 2


COUNTS = Counter()


def check_restricted_squares(system, labels, keep_components):
    if system["kind"] == "ht":
        bands = system["band_vertices"]
        for j, match in enumerate(system["matches"]):
            left = [i for i, v in enumerate(bands[j]) if labels[v] in keep_components]
            right = [i for i, v in enumerate(bands[j + 1]) if labels[v] in keep_components]
            assert len(left) == len(right)
            ranks = {i: k for k, i in enumerate(right)}
            actual = [ranks[match[i]] for i in left]
            inner_count = sum(i < system["weights"][j] for i in left)
            assert actual == square(len(left), inner_count)
            COUNTS["restricted_actual_squares"] += 1
    for child in system["children"]:
        check_restricted_squares(child, labels, keep_components)


def verify(graph, system, deletions=False):
    labels, signs, costs, coherent = graph.solve()
    port = system["port"]
    n = len(port)
    actual = [labels[v] for v in port]
    parts = partition(actual)
    assert len(set(labels)) == len(set(actual)), "component hidden from outer boundary"
    constants = system["constants"]
    if not constants:
        assert coherent and len(parts) == n and system["slope"] == 0
        assert all(costs[actual[i]] == system["density"] for i in range(n))
        assert system["density"] % 2 == 1
        COUNTS["regular_systems"] += 1
        return
    assert coherent == (n % 2 == 0)
    assert parts == reflection_partition(n, constants)
    COUNTS["reflecting_systems"] += 1
    if not coherent:
        COUNTS["odd_outer_sheet_obstructions"] += 1
        return
    assert all(c % 2 for c in constants)
    a = system["root"]
    divisor = n
    for c in constants:
        divisor = gcd(divisor, c - (2 * a - 1))
    assert divisor % 2 == 0
    number, arity = divisor // 2, 2 * n // divisor
    assert len(parts) == number and all(len(o) == arity for o in parts)
    for orbit in parts:
        assert sum((-1) ** signs[port[i]] for i in orbit) == 0
        assert costs[actual[orbit[0]]] == arity * system["density"]
        genus_numerator = 2 - arity + costs[actual[orbit[0]]]
        assert genus_numerator >= 0 and genus_numerator % 2 == 0
        if system["slope"] == 0:
            assert genus_numerator >= 2 and system["density"] >= 1
        COUNTS["oriented_components"] += 1

    root_labels = [actual[(a + i) % n] for i in range(n)]
    renumber = {}
    word = []
    for c in root_labels:
        renumber.setdefault(c, len(renumber))
        word.append(renumber[c])
    expected = (list(range(number)) + list(reversed(range(number)))) * (arity // 2)
    assert word == expected
    check_tree_word(word, number)
    COUNTS["path_chamber_words"] += 1

    if system.get("selected"):
        child, shift = system["selected"]
        child_n, child_a = len(child["port"]), child["root"]
        child_divisor = child_n
        for c in child["constants"]:
            child_divisor = gcd(child_divisor, c - (2 * child_a - 1))
        for gap in range(child_n):
            if (gap - child_a + 1) % child_divisor == 0:
                outer_gap = (gap - shift) % n
                assert (outer_gap - a + 1) % divisor == 0
                COUNTS["selected_child_end_occurrences"] += 1

    if deletions and number <= 6:
        for bits in range(1, 1 << number):
            retained = {i for i in range(number) if bits & (1 << i)}
            compressed = [c for c in word if c in retained]
            remap = {c: i for i, c in enumerate(sorted(retained))}
            compressed = [remap[c] for c in compressed]
            unit = list(range(len(retained))) + list(reversed(range(len(retained))))
            assert compressed == unit * (arity // 2)
            keep_components = {c for c, i in renumber.items() if i in retained}
            # Exact signed-piece or peripheral arithmetic check.
            check_restricted_squares(system, labels, keep_components)
            COUNTS["whole_component_deletions"] += 1


def leaf(graph, n, which, rng):
    if which == 0:
        return ht(graph, n, (4, -2, -2, -3, -3, -2),
                  [rng.randrange(n + 1) for _ in range(5)], 0)
    if which == 1:
        return ht(graph, n, (-3, -2), [rng.randrange(n + 1)], -4)
    if which == 2:
        return ht(graph, n, (3, 2), [rng.randrange(n + 1)], 4)
    if which == 3:
        return ht(graph, n, (2, -2), [rng.randrange(n + 1)], 0)
    if which == 4:
        return annuli(graph, n, 6)
    if which == 5:
        return annuli(graph, n, -6)
    return annuli(graph, n, 10)


def main():
    rng = Random(20261028)
    # Exact signed-piece or peripheral arithmetic check.
    carriers = [((4, -2, -2, -3, -3, -2), 0),
                ((-3, -2), -4), ((3, 2), 4), ((2, -2), 0)]
    for beta, slope in carriers:
        max_n = 6 if len(beta) == 6 else 24
        for n in range(1, max_n + 1):
            for weights in product(range(n + 1), repeat=len(beta) - 1):
                graph = Graph()
                system = ht(graph, n, beta, weights, slope)
                verify(graph, system, deletions=True)
                COUNTS["raw_HT_parameter_tuples"] += 1

    for trial in range(3600):
        n = 1 + trial % 18
        graph = Graph()
        left = leaf(graph, n, trial % 7, rng)
        right = leaf(graph, n, (trial // 7) % 7, rng)
        children = [left, right]
        if trial % 3 == 0:
            children.append(leaf(graph, n, (trial // 49) % 7, rng))
        system = combine(graph, children,
                         [rng.randrange(n) for _ in children], "sum")
        verify(graph, system, deletions=True)
        COUNTS["expanded_sum_systems"] += 1

    for trial in range(1800):
        n = 1 + trial % 18
        p = 2 + (trial // 18) % 4
        q = [q for q in range(-9, 10) if q and gcd(p, q) == 1][trial % 8]
        graph = Graph()
        child = leaf(graph, p * n, trial % 7, rng)
        system = combine(graph, [child], [rng.randrange(p * n)], "cable", p, q)
        verify(graph, system, deletions=True)
        COUNTS["expanded_cable_systems"] += 1

    # Exact signed-piece or peripheral arithmetic check.
    for trial in range(720):
        n = 1 + trial % 12
        p = 2 + trial % 3
        inner_n = p * n
        graph = Graph()
        j1 = leaf(graph, inner_n, trial % 7, rng)
        j2 = leaf(graph, inner_n, (trial // 7) % 7, rng)
        left = combine(graph, [j1, j2], [0, rng.randrange(inner_n)], "sum")
        j3 = leaf(graph, 2 * inner_n, (trial // 49) % 7, rng)
        right = combine(graph, [j3], [rng.randrange(2 * inner_n)], "cable", 2, -3)
        middle = combine(graph, [left, right], [rng.randrange(inner_n), 0], "sum")
        outer = combine(graph, [middle], [rng.randrange(inner_n)], "cable", p, p + 1)
        verify(graph, outer, deletions=True)
        COUNTS["alternating_nested_systems"] += 1

    # Exact signed-piece or peripheral arithmetic check.
    graph = Graph()
    child = ht(graph, 8, (4, -2, -2, -3, -3, -2), (1, 0, 0, 2, 0), 0)
    outer = combine(graph, [child], [0], "cable", 2, 3)
    verify(graph, outer, deletions=True)
    labels, signs, costs, coherent = graph.solve()
    actual = [labels[v] for v in outer["port"]]
    assert partition(actual) == [(0, 3), (1, 2)]
    examples = {"HT_winding_two": {
        "outer_partition": partition(actual),
        "chi_per_component": [-costs[c] for c in sorted(set(actual))],
        "genus_per_component": [13, 13]}}
    assert all(costs[c] == 26 for c in set(actual))

    # Exact signed-piece or peripheral arithmetic check.
    graph = Graph()
    plus, minus = annuli(graph, 8, 6), annuli(graph, 8, -6)
    zero = combine(graph, [plus, minus], [0, 1], "sum")
    verify(graph, zero, deletions=True)
    labels, _, costs, _ = graph.solve()
    actual = [labels[v] for v in zero["port"]]
    examples["opposite_torus_slopes"] = {
        "slope": zero["slope"], "outer_partition": partition(actual),
        "chi_per_component": [-costs[c] for c in sorted(set(actual))],
        "genus_per_component": [1 for c in set(actual)]}
    assert zero["slope"] == 0 and all(costs[c] == 8 for c in set(actual))

    # Exact signed-piece or peripheral arithmetic check.
    for p in range(2, 9):
        for u in range(-12, 13):
            if not u:
                continue
            for v in range(-60, 61):
                if gcd(u, v) != 1:
                    continue
                child_slope = Fraction(-v, p * u)
                outer_slope = Fraction(-p * v, u)
                COUNTS["primitive_cable_classes"] += 1
                if child_slope.denominator == 1:
                    assert abs(u) == 1
                    assert gcd(abs(u), abs(p * v)) == 1
                    assert gcd(abs(p * u), abs(v)) == p
                    assert outer_slope == p * p * child_slope
                    COUNTS["integral_child_cable_classes"] += 1
    for u in range(1, 9):
        for values in product(range(-8, 9), repeat=3):
            if gcd(u, gcd(values[0], gcd(values[1], values[2]))) != 1:
                continue
            COUNTS["primitive_composing_classes"] += 1
            if all(v % u == 0 for v in values):
                assert u == 1
                COUNTS["integral_child_composing_classes"] += 1
    print(json.dumps({"status": "PASS", "counts": dict(sorted(COUNTS.items())),
                      "examples": examples,
                      "limit": "Finite signed-graph, component Euler and root-gap diagnostics; no isotopy, essentiality, completeness or continuity certification."},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    from exact_replay import replay
    replay(main, "recursive_independent.txt")
