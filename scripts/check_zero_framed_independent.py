#!/usr/bin/env python3
"""Exact offline finite diagnostics; standard library only.
No topology certification. No file access by the mathematical implementation.
"""

from collections import Counter, defaultdict, deque
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, product
from math import gcd
import json
import sys


def minus_cf(coefficients):
    # Continuants, rather than the author's reversed Fraction recursion.
    p2, p1, q2, q1 = -1, 0, 0, 1
    for b in coefficients:
        p2, p1 = p1, b * p1 - p2
        q2, q1 = q1, b * q1 - q2
    return Q(p1, q1)


def expansions(x):
    @lru_cache(None)
    def tails(y):
        z = 1 / y
        lo = z.numerator // z.denominator
        result = []
        for b in (lo, lo + 1):
            if abs(b) < 2 or abs(b - z) >= 1:
                continue
            remainder = b - z
            if not remainder:
                result.append((b,))
            else:
                result.extend((b,) + tail for tail in tails(remainder))
        return tuple(result)
    return [(r, b) for r in (0, 1) for b in tails(x - r)]


def perm_inverse(p):
    inverse = [0] * len(p)
    for i, j in enumerate(p):
        inverse[j] = i
    return inverse


def compose(p, r):
    return [p[r[i]] for i in range(len(p))]


def local_square(n, inner):
    # Two actual reversed intervals, without a modular affine formula.
    return list(reversed(range(inner))) + list(reversed(range(inner, n)))


def orbit_partition(generators, n):
    unseen = set(range(n))
    result = []
    while unseen:
        seed = min(unseen)
        orbit, queue = set(), [seed]
        while queue:
            i = queue.pop()
            if i in orbit:
                continue
            orbit.add(i)
            queue.extend(p[i] for p in generators)
        unseen.difference_update(orbit)
        result.append(frozenset(orbit))
    return result


def orientable(orbit, generators):
    signs = {min(orbit): 1}
    queue = deque(signs)
    while queue:
        i = queue.popleft()
        for p in generators:
            j, target = p[i], -signs[i]
            if j in signs:
                if signs[j] != target:
                    return False
            else:
                signs[j] = target
                queue.append(j)
    return True


def chamber_data(orbits, n):
    labels = [next(j for j, orbit in enumerate(orbits) if i in orbit)
              for i in range(n)]
    state = 0
    gap_states = [state]
    edges = defaultdict(set)
    for j in labels:
        old = state
        state ^= 1 << j
        edges[j].add(frozenset((old, state)))
        gap_states.append(state)
    assert state == 0
    assert all(len(e) == 1 for e in edges.values())
    graph = defaultdict(set)
    for edge in edges.values():
        a, b = next(iter(edge))
        graph[a].add(b)
        graph[b].add(a)
    assert len(graph) == len(orbits) + 1
    assert max(map(len, graph.values())) <= 2
    assert sum(len(v) == 1 for v in graph.values()) == 2
    return labels, gap_states


def plumbing(n, parameters, beta, root):
    frames = {root: list(range(n))}
    heights = {root: 0}
    todo = [root]
    while todo:
        v = todo.pop()
        for w in (v - 1, v + 1):
            if w < 0 or w >= len(beta) or w in frames:
                continue
            inner = parameters[min(v, w)]
            frames[w] = compose(local_square(n, inner), frames[v])
            heights[w] = inner - heights[v]
            todo.append(w)
    reversal = list(reversed(range(n)))
    folds = []
    for v, b in enumerate(beta):
        if b % 2:
            inverse = perm_inverse(frames[v])
            folds.append(compose(inverse, compose(reversal, frames[v])))
    orbits = orbit_partition(folds, n)
    # Restrict by counting actual inner rectangles in every square.
    restricted = []
    for orbit in orbits:
        counts = []
        for e, inner in enumerate(parameters):
            near = e if abs(e - root) < abs(e + 1 - root) else e + 1
            counts.append(sum(frames[near][i] < inner for i in orbit))
        child = {root: 0}
        todo = [root]
        while todo:
            v = todo.pop()
            for w in (v - 1, v + 1):
                if w < 0 or w >= len(beta) or w in child:
                    continue
                child[w] = counts[min(v, w)] - child[v]
                todo.append(w)
        for v, h in heights.items():
            turn, rem = divmod(h, n)
            expected = len(orbit) * turn + sum(i < rem for i in orbit)
            assert child[v] == expected
        restricted.append((tuple(counts), tuple(child[v] for v in range(len(beta)))))
    return frames, heights, folds, orbits, restricted


def check_plumbing(quick):
    beta = (4, -2, -2, -3, -3, -2)
    count = subsets = 0
    for n in ((2, 4) if quick else (2, 4, 6, 8)):
        for parameters in product(range(n + 1), repeat=5):
            _, _, folds, orbits, restricted = plumbing(n, parameters, beta, 3)
            assert all(orientable(o, folds) for o in orbits)
            labels, _ = chamber_data(orbits, n)
            a = len(orbits[0])
            assert all(len(o) == a for o in orbits)
            q = len(orbits)
            assert labels == (list(range(q)) + list(reversed(range(q)))) * (a // 2)
            # Every actual subsystem, with its restricted square counts.
            for mask in range(1, 1 << q):
                indices = [j for j in range(q) if mask >> j & 1]
                roots = sorted(set().union(*(orbits[j] for j in indices)))
                p2 = tuple(sum(restricted[j][0][e] for j in indices) for e in range(5))
                _, _, _, o2, r2 = plumbing(len(roots), p2, beta, 3)
                rename = {old: new for new, old in enumerate(roots)}
                expected = [frozenset(rename[i] for i in orbits[j]) for j in indices]
                assert o2 == expected
                assert [r[1] for r in r2] == [restricted[j][1] for j in indices]
                subsets += 1
            count += 1
    return {"raw_parameter_tuples": count, "nonempty_subsystems": subsets,
            "sheet_counts": [2, 4] if quick else [2, 4, 6, 8]}


def check_folds(quick):
    count = orientability_tests = 0
    upper = 20 if quick else 64
    for n in range(1, upper + 1):
        root = list(reversed(range(n)))
        # For odd n, all residues can occur as transported fold constants.
        constants = range((n - 1) % 2, n, 2) if n % 2 == 0 else range(n)
        for c, d in product(constants, repeat=2):
            generators = [root, [(c - i) % n for i in range(n)],
                          [(d - i) % n for i in range(n)]]
            orbits = orbit_partition(generators, n)
            e = gcd(n, gcd(c - (n - 1), d - (n - 1)))
            if n % 2 == 0:
                assert len(orbits) == e // 2
                assert all(len(o) == 2 * n // e for o in orbits)
                chamber_data(orbits, n)
                assert all(orientable(o, generators) for o in orbits)
            else:
                nonorientable = [o for o in orbits if not orientable(o, generators)]
                assert len(nonorientable) == 1 and len(nonorientable[0]) == n // e
            orientability_tests += len(orbits)
            count += 1
    return {"max_N": upper, "fold_tuples": count,
            "component_orientability_tests": orientability_tests}


@lru_cache(None)
def perfect_matchings(points):
    if not points:
        return ((),)
    answer = []
    for j in range(1, len(points), 2):
        for left in perfect_matchings(points[1:j]):
            for right in perfect_matchings(points[j + 1:]):
                answer.append(((points[0], points[j]),) + left + right)
    return tuple(answer)


def trace_data(q, a, w):
    word = (list(range(q)) + list(reversed(range(q)))) * (a // 2)
    signs = [w[v] * (1 if i % (2 * q) < q else -1)
             for i, v in enumerate(word)]
    gap_chamber = []
    for i in range(q * a):
        turn = (i + 1) % (2 * q)
        gap_chamber.append(min(turn, 2 * q - turn))
    return word, signs, gap_chamber


def cap_sets(q, a):
    _, _, gaps = trace_data(q, a, (1,) * q)
    result = [[] for _ in range(q + 1)]
    for i, c in enumerate(gaps):
        result[c].append((i, (i + 1) % (q * a)))
    return result


def path_composition(edges, caps):
    graph = defaultdict(list)
    for u, v in edges + caps:
        graph[u].append(v)
        graph[v].append(u)
    assert all(1 <= len(v) <= 2 for v in graph.values())
    unseen, paths, loops = set(graph), [], 0
    while unseen:
        seed = next(iter(unseen))
        seen, todo = set(), [seed]
        while todo:
            x = todo.pop()
            if x in seen:
                continue
            seen.add(x)
            todo.extend(graph[x])
        unseen.difference_update(seen)
        ends = [x for x in seen if len(graph[x]) == 1]
        if ends:
            assert len(ends) == 2
            paths.append(frozenset(ends))
        else:
            loops += 1
    return frozenset(paths), loops


def actual_components(word, matching, retained=None):
    q = max(word) + 1 if word else 0
    if retained is None:
        retained = set(range(q))
    graph = defaultdict(set)
    for pair in matching:
        u, v = tuple(pair)
        u = ("Q", word[u]) if isinstance(u, int) else u
        v = ("Q", word[v]) if isinstance(v, int) else v
        graph[u].add(v)
        graph[v].add(u)
    unseen = set(graph)
    actual_sets, closed_pieces = [], set()
    while unseen:
        seed = next(iter(unseen))
        seen, todo = set(), [seed]
        while todo:
            u = todo.pop()
            if u in seen:
                continue
            seen.add(u)
            todo.extend(graph[u])
        unseen.difference_update(seen)
        actual = {u for u in seen if u[0] == "A"}
        pieces = {u[1] for u in seen if u[0] == "Q"}
        if actual:
            actual_sets.append((pieces, actual))
        else:
            closed_pieces.update(pieces)
    assert retained == {p for pieces, _ in actual_sets for p in pieces} | closed_pieces
    return actual_sets, closed_pieces


def closure(q, a, w, edges, check_all_orders=True, external_order=None):
    # Name the normal side so the root is negative. This does not change
    # which actual endpoints a return joins or what pieces are retained.
    normalized = tuple(sign * w[0] for sign in w)
    word, signs, gap_chamber = trace_data(q, a, normalized)
    caps = cap_sets(q, a)
    incident = [{0}] + [{c - 1, c} for c in range(1, q)] + [{q - 1}]
    one_sided = {0}
    one_sided.update(c for c in range(1, q)
                     if normalized[c - 1:c + 1] == (-1, 1))
    if normalized[-1] == -1:
        one_sided.add(q)
    for u, v in combinations(one_sided, 2):
        assert not incident[u] & incident[v]
    # A negative push-off of a positive trace lies just before that trace.
    # Every actual hole in these tests has an original reaching arc.
    gap_of = [(i - 1) % len(word) if signs[i] == 1 else i for i in range(len(word))]
    pending = [frozenset((0,))]
    visited, terminal = set(), []
    while pending:
        selected = pending.pop()
        if selected in visited:
            continue
        visited.add(selected)
        used = set().union(*(incident[c] for c in selected))
        retained = set(range(q)) - used
        matching, loops = path_composition(edges, [e for c in selected for e in caps[c]])
        enabled = set()
        for pair in matching:
            u, v = tuple(pair)
            if isinstance(u, int) and isinstance(v, int) and gap_of[u] == gap_of[v]:
                gap = gap_of[u]
                chamber = gap_chamber[gap]
                assert chamber in one_sided - selected
                assert incident[chamber] <= retained
                if external_order is not None:
                    # Are the two bordering original traces also adjacent
                    # after the other family's traces are restored?
                    left, right = gap, (gap + 1) % len(word)
                    indices, total = external_order
                    assert (indices[right] - indices[left]) % total == 1
                enabled.add(chamber)
        if not enabled:
            actual, closed = actual_components(word, matching, retained)
            assert 0 not in {p for pieces, _ in actual for p in pieces}
            terminal.append((selected, matching, loops, actual, closed))
        elif check_all_orders:
            pending.extend(selected | {c} for c in enabled)
        else:
            pending.append(selected | enabled)
    assert terminal
    assert len({t[0] for t in terminal}) == 1
    return terminal[0], len(visited)


def essential_matching(waves, tether_ports, n):
    return all(0 < sum(u < t < v for t in tether_ports) < len(tether_ports)
               for u, v in waves)


def check_closures(quick):
    counters = Counter()
    parameters = [(1, 4), (1, 6), (2, 2), (2, 4), (2, 6), (3, 2), (3, 4), (4, 2)]
    if not quick:
        parameters.append((4, 4))
    for q, a in parameters:
        n = q * a
        if n < 4:
            continue
        for tethers in combinations(range(n), 4):
            free = tuple(i for i in range(n) if i not in tethers)
            for waves in perfect_matchings(free):
                counters["partial_noncrossing_patterns"] += 1
                if not essential_matching(waves, tethers, n):
                    continue
                counters["essential_patterns_before_orientation"] += 1
                for w in product((-1, 1), repeat=q):
                    word, signs, _ = trace_data(q, a, w)
                    if any(signs[u] == signs[v] for u, v in waves):
                        continue
                    edges = list(waves) + [(i, ("A", j)) for j, i in enumerate(tethers)]
                    _, closed = actual_components(word, edges)
                    if closed:
                        continue
                    result, states = closure(q, a, w, edges)
                    counters["oriented_legal_assemblies"] += 1
                    counters["closure_states"] += states
                    counters["interior_repairs"] += any(0 < c < q for c in result[0])
                    counters["closed_Q_outputs"] += bool(result[4])
                    # First closure only: later parents can acquire pure
                    # actual annuli. Endpoint gaps alone then no longer
                    # decide whether a disk contains actual holes.
                    _, _, _, actual, _ = result
                    retained = {p for pieces, _ in actual for p in pieces}
                    assert len(retained) < q
                    actual_usage = [v for _, actual_set in actual for v in actual_set]
                    assert len(actual_usage) == len(set(actual_usage)) == 4
                    counters["strict_first_parents"] += 1
    return dict(counters)


def check_two_colours(quick):
    count = Counter()
    # Every noncrossing complete matching is split into same-colour waves
    # and two-colour reaches to the same actual hole, marked on that edge.
    for q, a in ((4, 2), (3, 4), (4, 4)):
        if quick and a * q > 12:
            continue
        n = q * a
        word, base_signs, _ = trace_data(q, a, (1,) * q)
        for colours in product((0, 1), repeat=q):
            if colours[0] != 0 or len(set(colours)) != 2:
                continue
            for pairs in perfect_matchings(tuple(range(n))):
                holes = [(u, v) for u, v in pairs if colours[word[u]] != colours[word[v]]]
                if len(holes) != 4:
                    continue
                waves = [(u, v) for u, v in pairs if colours[word[u]] == colours[word[v]]]
                if any(not 0 < sum(u < x < y < v for x, y in holes) < 4 for u, v in waves):
                    continue
                for w in product((-1, 1), repeat=q):
                    signs = [base_signs[i] * w[p] for i, p in enumerate(word)]
                    if any(signs[u] != signs[v] for u, v in holes):
                        continue
                    if any(signs[u] == signs[v] for u, v in waves):
                        continue
                    family = []
                    legal = True
                    for c in (0, 1):
                        pieces = [p for p in range(q) if colours[p] == c]
                        ports = [i for i, p in enumerate(word) if colours[p] == c]
                        compressed = {p: j for j, p in enumerate(ports)}
                        edges = [(compressed[u], compressed[v]) for u, v in waves
                                 if colours[word[u]] == c]
                        for j, (u, v) in enumerate(holes):
                            port = u if colours[word[u]] == c else v
                            edges.append((compressed[port], ("A", j)))
                        w2 = tuple(w[p] for p in pieces)
                        word2, _, _ = trace_data(len(pieces), a, w2)
                        assert [pieces[p] for p in word2] == [word[i] for i in ports]
                        _, closed = actual_components(word2, edges)
                        if closed:
                            legal = False
                            break
                        family.append((pieces, ports, edges, w2))
                    if not legal:
                        continue
                    # Only colour 0 is at the family's first end.
                    pieces, ports, edges, w2 = family[0]
                    result, states = closure(len(pieces), a, w2, edges,
                                             external_order=(ports, n))
                    count["legal_two_colour_diagrams"] += 1
                    count["relative_closure_states"] += states
                    count["relative_interior_repairs"] += any(0 < c < len(pieces) for c in result[0])
    return dict(count)


def check_envelope(quick):
    counter = Counter()
    alphabet = tuple(map(Q, (-1, Q(-1, 3), 0, Q(1, 3), 1)))
    for n in range(1, 6 if quick else 8):
        for jumps in product(alphabet, repeat=n):
            degree = sum(jumps)
            if degree < 0 or degree.denominator != 1:
                continue
            knots = [Q(0)]
            for jump in jumps:
                knots.append(knots[-1] + jump)

            def f(u):
                k = u.numerator // u.denominator
                t, index = divmod(k, n)
                return knots[index] + t * degree + (u - k) * jumps[index]

            # Direct maxima over THREE periods, sampled also inside bands.
            samples = [Q(k, 3) for k in range(3 * n + 1)]
            values = []
            for u in samples:
                integers = range((u - 3 * n).numerator // (u - 3 * n).denominator,
                                 u.numerator // u.denominator + 1)
                direct = max([f(u)] + [f(Q(k)) for k in integers])
                short = max([f(u)] + [f(Q(k)) for k in range(
                    (u - n).numerator // (u - n).denominator + 1,
                    u.numerator // u.denominator + 1)])
                assert direct == short
                values.append(direct)
            assert all(a <= b for a, b in zip(values, values[1:]))
            assert values[-1] - values[0] == degree
            if degree == 0:
                assert len(set(values)) == 1
            if all(j >= 0 for j in jumps):
                assert values == [f(u) for u in samples]
            records = values[::3]

            def nodal_records(js):
                prefix = [Q(0)]
                for jump in js:
                    prefix.append(prefix[-1] + jump)
                length, degree2 = len(js), prefix[-1]
                def at(k):
                    turn, index = divmod(k, length)
                    return prefix[index] + turn * degree2
                maxima = [max(at(k) for k in range(j - length, j + 1))
                          for j in range(length + 1)]
                return prefix, maxima

            correction = [m - v for m, v in zip(records[:-1], knots[:-1])]
            rotated_f, rotated_m = nodal_records(jumps[1:] + jumps[:1])
            assert [m - v for m, v in zip(rotated_m[:-1], rotated_f[:-1])] == correction[1:] + correction[:1]
            counter["rotation_checks"] += 1
            for j in range(n - 1):
                if jumps[j] * jumps[j + 1] < 0:
                    continue
                merged = jumps[:j] + (jumps[j] + jumps[j + 1],) + jumps[j + 2:]
                mf, mm = nodal_records(merged)
                assert mf == knots[:j + 1] + knots[j + 2:]
                assert mm == records[:j + 1] + records[j + 2:]
                counter["monotone_packet_merges"] += 1
            if any(jumps) and any(j == 0 for j in jumps):
                active = tuple(j for j in jumps if j)
                af, am = nodal_records(active)
                kept = [j for j, value in enumerate(jumps) if value]
                assert [m - v for m, v in zip(am[:-1], af[:-1])] == [correction[j] for j in kept]
                counter["zero_band_face_checks"] += 1
            # At s=1, sum the measure of positive level intervals in one turn.
            assert sum(values[i + 1] - values[i] for i in range(len(values) - 1)) == degree
            counter["profiles"] += 1
            counter["interior_band_samples"] += len(samples)
    return dict(counter)


def check_examples():
    beta = (4, -2, -2, -3, -3, -2)
    even = (-2, -2, -2, -2, 2, -2, -2, 2)
    assert minus_cf(beta) == 1 + minus_cf(even) == Q(29, 137)
    all_expansions = expansions(Q(29, 137))
    assert (0, beta) in all_expansions and (1, even) in all_expansions
    assert [b for _, b in all_expansions if all(v % 2 == 0 for v in b)] == [even]
    score = lambda b: sum(1 if v > 0 else -1 for v in b)
    assert score(beta) == score(even) == -4
    answer = {"continued_fraction": "29/137", "admissible_expansions": len(all_expansions),
              "zero_slope_expansions": sum(score(b) == -4 for _, b in all_expansions),
              "examples": []}
    for n, parameters, w, waves, tethers in [
        (8, (1, 0, 0, 2, 0), (1, 1), [(0, 2), (3, 5)], [1, 4, 6, 7]),
        (16, (3, 0, 0, 4, 0), (1, 1, -1, 1),
         [(1, 15), (3, 14), (4, 13), (5, 12), (7, 11), (8, 10)], [0, 2, 6, 9]),
    ]:
        _, heights, folds, orbits, restricted = plumbing(n, parameters, beta, 3)
        word, signs, _ = trace_data(len(orbits), len(orbits[0]), w)
        assert all(signs[u] == -signs[v] for u, v in waves)
        assert essential_matching(waves, tethers, n)
        edges = list(waves) + [(i, ("A", j)) for j, i in enumerate(tethers)]
        actual, closed = actual_components(word, edges)
        assert not closed and len(actual) == 1
        output, states = closure(len(orbits), 4, w, edges)
        selected, matching, loops, actual2, closed2 = output
        assert not closed2 and len(actual2) == 1 and len(actual2[0][0]) == 1
        large = (0, 3, 4)
        types = [[h[v] for v in large] for _, h in restricted]
        assert types == ([[1, 0, 1], [0, 0, 1]] if n == 8 else
                         [[1, 0, 1]] * 3 + [[0, 0, 1]])
        if n == 16:
            seed, _ = path_composition(edges, cap_sets(4, 4)[0])
            assert frozenset((10, 11)) in seed
            assert selected == frozenset((0, 3)) and loops == 2
            assert types[2] != types[3]
        else:
            assert selected == frozenset((0,)) and loops == 0
        expected_reaches = ([(1, 0), (2, 3), (5, 1), (6, 2)] if n == 8 else
                            [(1, 0), (6, 2), (9, 3), (14, 1)])
        assert matching == frozenset(frozenset((port, ("A", j)))
                                     for port, j in expected_reaches)
        final_caps = [(6, 1), (2, 5)] if n == 8 else [(14, 1), (6, 9)]
        final, final_loops = path_composition([tuple(p) for p in matching], final_caps)
        final_pairs = [(0, 2), (1, 3)] if n == 8 else [(0, 1), (2, 3)]
        assert final == frozenset(frozenset((("A", u), ("A", v))) for u, v in final_pairs)
        assert final_loops == 0
        chi = n * (1 - len(beta))
        genus = (2 - 4 - chi) // 2
        assert genus == (19 if n == 8 else 39)
        answer["examples"].append({
            "N": n, "folds": [p[0] for p in folds],
            "orbits": [sorted(o) for o in orbits], "large_heights": types,
            "piece_genus": 9, "initial_genus": genus,
            "selected_chambers": sorted(selected), "closure_states": states,
            "closed_pattern_circles": loops,
            "retained_pieces": sorted(actual2[0][0]),
            "after_first_genus": 9,
            "assembly_cycle_rank": len(waves) - len(orbits) + 1,
            "final_actual_pairs": final_pairs,
        })
    return answer


def main():
    quick = "--quick" in sys.argv
    result = {"scope": "Finite exact combinatorics; no topological or isotopy certification.",
              "quick": quick}
    for name, run in [
        ("examples", check_examples),
        ("folds", lambda: check_folds(quick)),
        ("plumbing", lambda: check_plumbing(quick)),
        ("closures", lambda: check_closures(quick)),
        ("two_colours", lambda: check_two_colours(quick)),
        ("envelopes", lambda: check_envelope(quick)),
    ]:
        result[name] = run()
        print(json.dumps({name: result[name]}, ensure_ascii=False), flush=True)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    from exact_replay import replay
    replay(main, "zero_framed_independent.txt")
