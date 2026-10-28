#!/usr/bin/env python3
"""Exact offline finite diagnostics; standard library only.
No topology certification. No file access by the mathematical implementation.
"""

from itertools import combinations, product
from math import gcd
import json


class SignedGraph:
    def __init__(self, size):
        self.adj = [[] for _ in range(size)]

    def edge(self, a, b, flip):
        self.adj[a].append((b, flip))
        self.adj[b].append((a, flip))

    def components(self):
        component = [-1] * len(self.adj)
        sign = [-1] * len(self.adj)
        coherent = True
        number = 0
        for start in range(len(self.adj)):
            if component[start] >= 0:
                continue
            component[start], sign[start] = number, 0
            todo = [start]
            while todo:
                u = todo.pop()
                for v, flip in self.adj[u]:
                    wanted = sign[u] ^ flip
                    if component[v] < 0:
                        component[v], sign[v] = number, wanted
                        todo.append(v)
                    else:
                        assert component[v] == number
                        if sign[v] != wanted:
                            coherent = False
            number += 1
        return component, sign, coherent


def partition(labels):
    buckets = {}
    for i, value in enumerate(labels):
        buckets.setdefault(value, []).append(i)
    return sorted(tuple(v) for v in buckets.values())


def reflect_graph(n, constants):
    graph = SignedGraph(n)
    for c in constants:
        for i in range(n):
            graph.edge(i, (c - i) % n, 1)
    return graph.components()


def predicted(n, constants):
    assert n % 2 == 0 and constants and all(c % 2 for c in constants)
    shift = (constants[0] + 1) // 2
    divisor = n
    for c in constants[1:]:
        divisor = gcd(divisor, c - constants[0])
    assert divisor % 2 == 0
    q = divisor // 2
    arity = 2 * n // divisor
    labels = []
    for i in range(n):
        residue = (i - shift) % divisor
        labels.append(min(residue, divisor - 1 - residue))
    return labels, q, arity, divisor, shift


def verify_formula(n, constants, actual):
    labels, signs, coherent = actual
    assert coherent == (n % 2 == 0)
    if not coherent:
        return
    expected, q, arity, divisor, shift = predicted(n, constants)
    assert partition(labels) == partition(expected)
    assert len(partition(labels)) == q
    for part in partition(labels):
        assert len(part) == arity
        assert sum(1 if signs[i] else -1 for i in part) == 0
    word = [expected[(shift + i) % n] for i in range(n)]
    unit = list(range(q)) + list(reversed(range(q)))
    assert word == unit * (arity // 2)


def expanded_cable(n, p, constants):
    inner = p * n
    graph = SignedGraph(n + inner)
    for i in range(inner):
        graph.edge(i % n, n + i, 0)
    for c in constants:
        for i in range(inner):
            graph.edge(n + i, n + (c - i) % inner, 1)
    labels, signs, coherent = graph.components()
    return labels[:n], signs[:n], coherent


def expanded_sum(n, child_data):
    graph = SignedGraph(n * (1 + len(child_data)))
    transported = []
    for child, (shift, constants) in enumerate(child_data):
        offset = n * (1 + child)
        for i in range(n):
            graph.edge(i, offset + (i + shift) % n, 0)
        for c in constants:
            for i in range(n):
                graph.edge(offset + i, offset + (c - i) % n, 1)
            transported.append(c - 2 * shift)
    labels, signs, coherent = graph.components()
    return (labels[:n], signs[:n], coherent), transported


def deletion_checks(n, constants):
    labels, q, arity, _, shift = predicted(n, constants)
    if q > 6:
        return 0
    rooted = [labels[(shift + i) % n] for i in range(n)]
    checked = 0
    for bits in range(1, 1 << q):
        selected = [i for i in range(q) if bits & (1 << i)]
        renumber = {old: new for new, old in enumerate(selected)}
        retained = [renumber[i] for i in rooted if i in renumber]
        unit = list(range(len(selected))) + list(reversed(range(len(selected))))
        assert retained == unit * (arity // 2)
        checked += 1
    return checked


def run():
    counts = {"reflection_systems": 0, "component_deletions": 0,
              "expanded_cables": 0, "expanded_sums": 0,
              "cable_root_gaps": 0}

    for n in range(2, 25, 2):
        odds = list(range(1, n, 2))
        for size in range(1, min(3, len(odds)) + 1):
            for cs in combinations(odds, size):
                verify_formula(n, cs, reflect_graph(n, cs))
                counts["reflection_systems"] += 1
                counts["component_deletions"] += deletion_checks(n, cs)

    for n in range(1, 25):
        for p in range(2, 8):
            inner = p * n
            if inner % 2:
                continue
            root = inner - 1
            choices = [(root,)]
            for h in range(1, min(inner // 2, 9)):
                choices.append((root, root - 2 * h))
                choices.append((root, root - 2 * h, root - 2))
            for cs in choices:
                result = expanded_cable(n, p, cs)
                verify_formula(n, cs, result)
                direct = reflect_graph(n, cs)
                assert partition(result[0]) == partition(direct[0])
                assert result[2] == direct[2]
                counts["expanded_cables"] += 1
                if n % 2 == 0:
                    _, _, _, child_e, _ = predicted(inner, cs)
                    _, _, _, outer_e, _ = predicted(n, cs)
                    for gap in range(child_e - 1, inner, child_e):
                        assert (gap % n) % outer_e == outer_e - 1
                        counts["cable_root_gaps"] += 1

    for n in range(2, 19):
        choices = [(), (1,), (1, 3), (1, 5)]
        for child_cs in product(choices, repeat=3):
            if not any(child_cs):
                continue
            for shifts in [(0, 0, 0), (1, 2, 3), (n - 1, 0, n // 2)]:
                data = list(zip(shifts, child_cs))
                result, transported = expanded_sum(n, data)
                verify_formula(n, transported, result)
                direct = reflect_graph(n, transported)
                assert partition(result[0]) == partition(direct[0])
                assert result[2] == direct[2]
                counts["expanded_sums"] += 1

    # An actual HT input from the accepted K_{29/137} example:
    # eight child sheets, folds 7 and 3, carrier length six.
    # A winding-two, q=3 cable has four outer sheets.
    labels, signs, coherent = expanded_cable(4, 2, (7, 3))
    assert coherent
    assert partition(labels) == [(0, 3), (1, 2)]
    child_density = 6 - 1
    cable_density = (2 - 1) * 3 + 2 * child_density
    genus = 1 + 2 * (cable_density - 1) // 2
    assert cable_density == 13 and genus == 13

    # A stress case in which three child orbits merge into one outer orbit.
    # This is an arithmetic diagnostic, with no extra realisation claim.
    child = reflect_graph(12, (11, 5))
    outer = expanded_cable(4, 3, (11, 5))
    assert len(partition(child[0])) == 3
    assert len(partition(outer[0])) == 1
    assert outer[2]

    print(json.dumps({"status": "PASS", "counts": counts,
                      "verified_HT_cable_example": {
                          "inner_sheets": 8, "outer_sheets": 4,
                          "outer_partition": partition(labels),
                          "genus_per_outer_component": genus},
                      "scope": "Finite arithmetic diagnostics only; no isotopy, essentiality, completeness or continuity certification."},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    from exact_replay import replay
    replay(run, "recursive_systems.txt")
