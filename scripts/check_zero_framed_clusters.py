#!/usr/bin/env python3
"""Exact offline finite diagnostics; standard library only.
No topology certification. No file access by the mathematical implementation.
"""

from fractions import Fraction as F
from itertools import product
from math import gcd


def cf(coefficients):
    value = F(0)
    for b in reversed(coefficients):
        value = 1 / (b - value)
    return value


def fold_orbits(n, constants):
    remaining = set(range(n))
    answer = []
    while remaining:
        queue = [min(remaining)]
        orbit = set()
        while queue:
            i = queue.pop()
            if i not in orbit:
                orbit.add(i)
                queue.extend((c - i) % n for c in constants)
        remaining -= orbit
        answer.append(orbit)
    return answer


def check_folds():
    cases = 0
    for n in range(2, 34, 2):
        for c2, c3 in product(range(1, n, 2), repeat=2):
            constants = (n - 1, c2, c3)
            e = gcd(n, gcd(c2 - constants[0], c3 - constants[0]))
            q, a = e // 2, 2 * n // e
            orbits = fold_orbits(n, constants)
            assert len(orbits) == q and all(len(o) == a for o in orbits)
            word = [min(i % e, e - 1 - i % e) for i in range(n)]
            expected = (list(range(q)) + list(reversed(range(q)))) * (a // 2)
            assert word == expected
            for j, orbit in enumerate(orbits):
                assert orbit == {i for i, label in enumerate(word) if label == j}
            # Deleting whole root orbits preserves the outside end and its walk.
            keep = set(range(0, q, 2))
            rename = {v: j for j, v in enumerate(sorted(keep))}
            restricted = [rename[v] for v in word if v in keep]
            k = len(keep)
            assert restricted == (list(range(k)) + list(reversed(range(k)))) * (a // 2)
            cases += 1
    print(f"PASS folds/path walks and subsystem order: {cases} tuples")


def check_one_sided():
    count = 0
    for q in range(1, 11):
        for signs in product((-1, 1), repeat=q):
            regions = []
            if signs[0] == 1:
                regions.append({0})
            regions.extend({j, j + 1} for j in range(q - 1)
                           if signs[j:j + 2] == (-1, 1))
            if signs[-1] == -1:
                regions.append({q - 1})
            for i, a in enumerate(regions):
                assert all(not a & b for b in regions[i + 1:])
            count += 1
    print(f"PASS disjoint incident-piece sets of one-sided chambers: {count} words")


def envelope(jumps):
    n = len(jumps)
    prefix = [F(0)]
    for jump in jumps:
        prefix.append(prefix[-1] + jump)
    degree = prefix[-1]

    def value(k):
        turn, position = divmod(k, n)
        return prefix[position] + turn * degree

    records = [max(value(k) for k in range(j - n, j + 1)) for j in range(n + 1)]
    return prefix, records


def check_envelopes():
    count = 0
    alphabet = tuple(F(i, 2) for i in range(-2, 3))
    for n in range(1, 7):
        for jumps in product(alphabet, repeat=n):
            degree = sum(jumps)
            if degree < 0 or degree.denominator != 1:
                continue
            f, m = envelope(jumps)
            assert m[-1] - m[0] == degree
            assert all(b >= a for a, b in zip(m, m[1:]))
            assert all(a >= b for a, b in zip(m, f))
            for j, jump in enumerate(jumps):
                assert m[j + 1] == max(m[j], f[j + 1])
                assert 0 <= m[j + 1] - m[j] <= max(F(0), jump)
            if degree == 0:
                assert len(set(m)) == 1
            if all(jump >= 0 for jump in jumps):
                assert m == f
            # Rotation changes only the lift constant, not the correction.
            rotated = jumps[1:] + jumps[:1]
            f2, m2 = envelope(rotated)
            correction = [a - b for a, b in zip(m[:-1], f[:-1])]
            assert [a - b for a, b in zip(m2[:-1], f2[:-1])] == correction[1:] + correction[:1]
            # Removing unsupported zero-jump bands is a face restriction.
            active = tuple(jump for jump in jumps if jump)
            if active:
                af, am = envelope(active)
                old_indices = [j for j, jump in enumerate(jumps) if jump]
                assert [am[j] - af[j] for j in range(len(active))] == [m[j] - f[j] for j in old_indices]
            # A generic unit phase has exactly degree many positive end cuts.
            phase = F(1, 7)
            hits = 0
            for lower, upper in zip(m, m[1:]):
                for integer in range(int(lower) - 2, int(upper) + 3):
                    hits += lower < phase + integer < upper
            assert hits == degree
            count += 1
    print(f"PASS circular envelopes, rotation/face invariance, coherent endpoint: {count} words")


def compose_caps(pattern, caps):
    graph = {}
    for a, b in pattern + caps:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    remaining = set(graph)
    result, closed = set(), 0
    while remaining:
        queue = [next(iter(remaining))]
        component = set()
        while queue:
            x = queue.pop()
            if x not in component:
                component.add(x)
                queue.extend(graph[x])
        remaining -= component
        ends = [x for x in component if len(graph[x]) == 1]
        if ends:
            assert len(ends) == 2
            result.add(frozenset(ends))
        else:
            closed += 1
    return result, closed


def check_nonparallel_example():
    beta = (4, -2, -2, -3, -3, -2)
    even = (-2, -2, -2, -2, 2, -2, -2, 2)
    assert cf(beta) == 1 + cf(even) == F(29, 137)
    score = lambda b: sum(1 if x > 0 else -1 for x in b)
    assert score(beta) == score(even)
    # Root band 3; HT parameters (1,0,0,2,0) at N=8.
    n, root = 8, 3
    parameters = (1, 0, 0, 2, 0)
    heights = {root: 0}
    for j in range(root - 1, -1, -1):
        heights[j] = parameters[j] - heights[j + 1]
    for j in range(root + 1, len(beta)):
        heights[j] = parameters[j - 1] - heights[j - 1]
    assert (heights[0], heights[3], heights[4]) == (1, 0, 2)
    constants = tuple((-1 - 2 * (-1) ** abs(j - root) * heights[j]) % n
                      for j, b in enumerate(beta) if b % 2)
    orbits = fold_orbits(n, constants)
    assert orbits == [{0, 3, 4, 7}, {1, 2, 5, 6}]

    def restricted(orbit, h):
        turns, remainder = divmod(h, n)
        return len(orbit) * turns + sum(i < remainder for i in orbit)

    types = [tuple(restricted(o, heights[j]) for j in (0, 3, 4)) for o in orbits]
    assert types == [(1, 0, 1), (0, 0, 1)]  # distinct complete large-height data
    genus = 1 + 4 * (len(beta) - 2) // 2
    assert genus == 9
    pattern = [(0, 2), (3, 5), (1, "p1"), (4, "p2"), (6, "n1"), (7, "n2")]
    after, closed = compose_caps(pattern, [(7, 0), (3, 4)])
    expected = {frozenset(pair) for pair in [(1, "p1"), (2, "n2"), (5, "p2"), (6, "n1")]}
    assert after == expected and closed == 0
    final, closed = compose_caps([tuple(p) for p in after], [(6, 1), (2, 5)])
    assert final == {frozenset(("p1", "n1")), frozenset(("p2", "n2"))} and closed == 0
    assert 2 - 2 * (2 * genus + 1) - 4 == 2 * 4 * (1 - len(beta)) == -40
    print("PASS actual nonparallel four-boundary example: K_29/137, genera 19 -> 9 -> annuli")

    # The mixed-sign Part 9 arc diagram, now with a genuinely nonproduct
    # interior repair chamber between different HT component classes.
    n = 16
    heights = {0: 3, 3: 0, 4: 4}
    orbits = fold_orbits(n, (15, 7))
    expected_orbits = [{j, 7 - j, 8 + j, 15 - j} for j in range(4)]
    assert orbits == expected_orbits
    types = [tuple(restricted(o, heights[j]) for j in (0, 3, 4)) for o in orbits]
    assert types == [(1, 0, 1)] * 3 + [(0, 0, 1)]
    word = tuple(list(range(4)) + list(reversed(range(4)))) * 2
    orientations = (1, 1, -1, 1)
    signs = tuple(orientations[word[i]] * (1 if i % 8 < 4 else -1)
                  for i in range(16))
    tethers = [(0, "p1"), (2, "n1"), (6, "n2"), (9, "p2")]
    waves = [(1, 15), (3, 14), (4, 13), (5, 12), (7, 11), (8, 10)]
    assert all(signs[a] == -signs[b] for a, b in waves)
    for a, b in waves:
        enclosed = sum(a < i < b for i, _ in tethers)
        assert 0 < enclosed < 4
    pattern = waves + tethers
    seed_caps = [(15, 0), (7, 8)]
    raw, _ = compose_caps(pattern, seed_caps)
    assert frozenset((10, 11)) in raw
    # This bad return has endpoints on piece 2 (type 1) and piece 3 (type 0).
    assert word[10] == 2 and word[11] == 3 and types[2] != types[3]
    repair_caps = [(2, 3), (4, 5), (10, 11), (12, 13)]
    repaired, closed = compose_caps(pattern, seed_caps + repair_caps)
    expected = {frozenset(p) for p in [(1, "p1"), (6, "n2"), (9, "p2"), (14, "n1")]}
    assert repaired == expected and closed == 2
    final, closed = compose_caps([tuple(p) for p in repaired], [(14, 1), (6, 9)])
    assert final == {frozenset(("p1", "n1")), frozenset(("p2", "n2"))} and closed == 0
    assert 2 - 2 * 39 - 4 == 4 * 4 * (1 - len(beta)) == -80
    print("PASS nonproduct interior closure: bad return (10,11), genera 39 -> 9 -> annuli")


def main():
    check_folds()
    check_one_sided()
    check_envelopes()
    check_nonparallel_example()
    print("Scope: exact finite arithmetic only; no machine proof of topology.")


if __name__ == "__main__":
    from exact_replay import replay
    replay(main, "zero_framed_clusters.txt")
