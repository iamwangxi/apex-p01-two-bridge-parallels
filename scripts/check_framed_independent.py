#!/usr/bin/env python3
"""Exact offline finite diagnostics; standard library only.
No topology certification. No file access by the mathematical implementation.
"""

from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import product
from math import gcd
import json


def cf(coefficients):
    p_old, p, q_old, q = -1, 0, 0, 1
    for b in coefficients:
        p_old, p = p, b * p - p_old
        q_old, q = q, b * q - q_old
    return Fraction(p, q)


def all_bounded_continuants(bound):
    """Complete coefficient tree with |final denominator| <= bound.

    |q_new| >= 2|q|-|q_old| > |q|, so pruning cannot lose a word which
    eventually has denominator <= bound. The coefficient bound below follows
    from |b*q-q_old| <= bound. Intermediate determinants are checked directly.
    """
    carriers = defaultdict(list)
    stack = [((), -1, 0, 0, 1)]
    words = 0
    while stack:
        word, p_old, p, q_old, q = stack.pop()
        b_max = (bound + abs(q_old)) // abs(q)
        for magnitude in range(2, b_max + 1):
            for b in (-magnitude, magnitude):
                p_new, q_new = b * p - p_old, b * q - q_old
                if abs(q_new) > bound:
                    continue
                assert abs(q_new) > abs(q)
                assert abs(p_new * q - p * q_new) == 1
                new_word = word + (b,)
                value = Fraction(p_new, q_new)
                assert 0 < abs(value) < 1
                integer = int(value < 0)
                carriers[value + integer].append((integer, new_word))
                stack.append((new_word, p, p_new, q, q_new))
                words += 1
    return carriers, words


def signature(beta):
    return sum(1 if b > 0 else -1 for b in beta)


def check_carriers(carriers, words, bound):
    counts = Counter()
    for x, data in carriers.items():
        if x.denominator % 2 == 0:
            continue
        counts['knot_inputs'] += 1
        even = [b for _, b in data if all(c % 2 == 0 for c in b)]
        assert len(even) == 1 and len(even[0]) % 2 == 0
        baseline = signature(even[0])
        for integer, beta in data:
            assert integer + cf(beta) == x
            slope = 2 * (signature(beta) - baseline)
            counts['knot_carriers'] += 1
            assert slope % 2 == 0
            if all(b % 2 == 0 for b in beta):
                assert slope == 0
            if len(beta) == 1:
                assert x.numerator in (1, x.denominator - 1)
                assert abs(slope) == 2 * x.denominator
            elif slope:
                for a in range(2, 66, 2):
                    chi = a * (1 - len(beta))
                    twice_genus = 2 - a - chi
                    assert twice_genus >= 2 and twice_genus % 2 == 0
                    counts['positive_genus_cases'] += 1
                    if len(beta) % 2:
                        counts['odd_length_genus_cases'] += 1
    table = []
    x = Fraction(7, 19)
    even = next(b for _, b in carriers[x] if all(c % 2 == 0 for c in b))
    for integer, beta in sorted(carriers[x]):
        table.append([integer, list(beta), 2 * (signature(beta) - signature(even))])
    assert table == [
        [0, [2, -2, -2, -3], 0],
        [0, [3, 3, -2], 6],
        [0, [3, 4, 2], 10],
        [1, [-2, -3, -2, -3], -4],
        [1, [-2, -2, 2, -2], 0],
        [1, [-2, -2, 3, 2], 4],
    ]
    torus_rows = 0
    for denominator in range(3, min(bound, 41) + 1, 2):
        for numerator, resonance in ((1, 2 * denominator),
                                    (denominator - 1, -2 * denominator)):
            rows = carriers[Fraction(numerator, denominator)]
            assert len(rows) == 2
            E = next(b for _, b in rows if all(c % 2 == 0 for c in b))
            assert {2 * (signature(b) - signature(E)) for _, b in rows} == {0, resonance}
            torus_rows += 1
    return {'max_denominator': bound, 'all_continuant_words_including_links': words,
            **counts, 'K_7_over_19': table, 'torus_and_mirror_rows': torus_rows}


def permutation_cycles(permutation):
    unseen, answer = set(range(len(permutation))), []
    while unseen:
        start = min(unseen)
        current, orbit = start, []
        while current not in orbit:
            orbit.append(current)
            current = permutation[current]
        assert current == start
        unseen.difference_update(orbit)
        answer.append(frozenset(orbit))
    return answer


def horizontal(signs, framing):
    n, d = len(signs), sum(signs)
    k = framing * d
    assert k
    sheets = abs(k)
    actual_permutations = [[(j + e) % sheets for j in range(sheets)] for e in signs]
    outer = list(range(sheets))
    for perm in actual_permutations:
        outer = [perm[j] for j in outer]
    # Build a connected covering graph of a bouquet with n loops.
    visited, queue = set(), [0]
    while queue:
        j = queue.pop()
        if j in visited:
            continue
        visited.add(j)
        queue.extend(p[j] for p in actual_permutations)
    assert len(visited) == sheets
    actual_cycles = [permutation_cycles(p) for p in actual_permutations]
    outer_cycles = permutation_cycles(outer)
    assert all(len(c) == 1 for c in actual_cycles)
    assert len(outer_cycles) == abs(d)
    assert all(len(c) == abs(framing) for c in outer_cycles)
    # theta += 1/k shifts each actual fibre point j to j+1. Find the
    # induced return on boundary components from the computed orbit sets.
    outer_labels = {j: i for i, orbit in enumerate(outer_cycles) for j in orbit}
    return_permutation = []
    for orbit in outer_cycles:
        image = frozenset((j + 1) % sheets for j in orbit)
        assert image in outer_cycles
        return_permutation.append(outer_labels[next(iter(image))])
    assert len(permutation_cycles(return_permutation)) == 1
    # Number of vertices minus number of lifted bouquet edges, independent
    # of the boundary component formula being tested.
    chi_H = sheets - sum(len(p) for p in actual_permutations)
    b_H = sum(len(c) for c in actual_cycles) + len(outer_cycles)
    assert chi_H == abs(k) * (1 - n)
    twice_genus_H = 2 - b_H - chi_H
    assert twice_genus_H >= 0 and twice_genus_H % 2 == 0
    for i, e in enumerate(signs):
        longitude_value = sum(framing * signs[j] for j in range(n) if j != i)
        meridian_coefficient = -e * longitude_value // e
        assert longitude_value == framing * (d - e)
        assert e * longitude_value + meridian_coefficient * e == 0
        assert meridian_coefficient == framing * e - k
        assert gcd(abs(e), abs(meridian_coefficient)) == 1
    assert Fraction(framing, k) == Fraction(1, d)
    for g_K in (1, 2, 5, 11):
        chi_S = chi_H + len(outer_cycles) * (1 - 2 * g_K)
        genus_numerator = 2 - n - chi_S
        assert genus_numerator >= 2 and genus_numerator % 2 == 0
        assert genus_numerator == 2 - n + abs(d) * (2 * g_K - 1) + abs(k) * (n - 1)
        if n == 1:
            assert genus_numerator == 2 * g_K
    return {'sheets': sheets, 'chi_H': chi_H, 'H_boundary_components': b_H,
            'H_genus': twice_genus_H // 2,
            'outer_boundary_cycles': [sorted(c) for c in outer_cycles],
            'outer_return_permutation': return_permutation}


def check_horizontal():
    modes = nonzero = 0
    for n in range(1, 9):
        for signs in product((-1, 1), repeat=n):
            for framing in range(-9, 10):
                modes += 1
                if framing * sum(signs):
                    horizontal(signs, framing)
                    nonzero += 1
    example = horizontal((1, 1), 1)
    assert example['chi_H'] == -2 and example['H_boundary_components'] == 4
    chi_S = example['chi_H'] + 2 * (-1)
    assert chi_S == -4 and (2 - 2 - chi_S) // 2 == 2
    return {'peripheral_modes': modes, 'cover_classes': nonzero,
            'global_genus_cases': 4 * nonzero, 'K_4_over_15_pattern': example}


def square_permutation(n, t):
    return [t - 1 - j if j < t else n + t - 1 - j for j in range(n)]


def plumbing(n, beta, parameters):
    root = next(i for i, b in enumerate(beta) if b % 2)
    frames = [None] * len(beta)
    frames[root] = list(range(n))
    for i in range(root, len(beta) - 1):
        p = square_permutation(n, parameters[i])
        frames[i + 1] = [p[j] for j in frames[i]]
    for i in range(root - 1, -1, -1):
        p = square_permutation(n, parameters[i])
        frames[i] = [p[j] for j in frames[i + 1]]
    folds = []
    for i, b in enumerate(beta):
        if not b % 2:
            continue
        inverse = [0] * n
        for j, v in enumerate(frames[i]):
            inverse[v] = j
        folds.append([inverse[n - 1 - frames[i][j]] for j in range(n)])
    unseen, orbits = set(range(n)), []
    while unseen:
        signs = {min(unseen): 1}
        queue = deque(signs)
        while queue:
            j = queue.popleft()
            for fold in folds:
                k = fold[j]
                if k in signs:
                    assert signs[k] == -signs[j]
                else:
                    signs[k] = -signs[j]
                    queue.append(k)
        orbit = frozenset(signs)
        orbits.append(orbit)
        unseen.difference_update(orbit)
    labels = [next(i for i, o in enumerate(orbits) if j in o) for j in range(n)]
    a, q = len(orbits[0]), len(orbits)
    assert a % 2 == 0 and all(len(o) == a for o in orbits)
    assert labels == (list(range(q)) + list(reversed(range(q)))) * (a // 2)
    # Recover complementary sides by crossing the actual boundary word;
    # no path graph is stipulated in the construction.
    state, edges = 0, defaultdict(set)
    for label in labels:
        next_state = state ^ (1 << label)
        edges[label].add(frozenset((state, next_state)))
        state = next_state
    assert state == 0 and all(len(v) == 1 for v in edges.values())
    graph = defaultdict(set)
    for edge in edges.values():
        v, w = next(iter(edge))
        graph[v].add(w)
        graph[w].add(v)
    assert len(graph) == q + 1
    assert max(map(len, graph.values())) <= 2
    assert sum(len(v) == 1 for v in graph.values()) == 2
    return frames, folds, orbits, labels


def check_sloped_plumbing():
    betas = ((3, 3, -2), (3, 4, 2), (-2, -3, -2, -3), (-2, -2, 3, 2))
    tuples = subsets = 0
    observed_arities = set()
    for beta in betas:
        for n in (2, 4, 6, 8, 10, 12):
            for parameters in product(range(n + 1), repeat=len(beta) - 1):
                frames, folds, orbits, _ = plumbing(n, beta, parameters)
                observed_arities.add(len(orbits[0]))
                # Compare the formula AFTER constructing actual fold orbits.
                constants = [fold[0] for fold in folds]
                assert all(fold[j] == (c - j) % n
                           for fold, c in zip(folds, constants) for j in range(n))
                e = n
                for c in constants[1:]:
                    e = gcd(e, c - constants[0])
                assert len(orbits) == e // 2
                assert len(orbits[0]) == 2 * n // e
                for mask in range(1, 1 << len(orbits)):
                    retained = sorted(set().union(*(o for i, o in enumerate(orbits)
                                                   if mask >> i & 1)))
                    counts = tuple(sum(frames[j][i] < t for i in retained)
                                   for j, t in enumerate(parameters))
                    _, _, child_orbits, _ = plumbing(len(retained), beta, counts)
                    compress = {old: new for new, old in enumerate(retained)}
                    expected = [frozenset(compress[j] for j in orbit)
                                for i, orbit in enumerate(orbits) if mask >> i & 1]
                    assert child_orbits == expected
                    subsets += 1
                tuples += 1
    return {'K_7_over_19_nonzero_carriers': len(betas),
            'raw_plumbing_parameter_tuples': tuples,
            'retained_actual_subsystems': subsets,
            'observed_connected_arities': sorted(observed_arities),
            'sheet_counts': [2, 4, 6, 8, 10, 12]}


def ht_move_classes(beta, r):
    vertices = list(product(range(r + 1), repeat=len(beta) - 1))
    parent = {v: v for v in vertices}
    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    for v in vertices:
        for i, b in enumerate(beta):
            if abs(b) != 2:
                continue
            indices = [j for j in (i - 1, i) if 0 <= j < len(v)]
            if all(v[j] < r for j in indices):
                w = tuple(value + int(j in indices) for j, value in enumerate(v))
                parent[find(w)] = find(v)
    return len({find(v) for v in vertices}), len(vertices)


def check_point_criterion():
    boxes = vertices = 0
    for length in (2, 4, 6, 8):
        for big in product((False, True), repeat=length):
            beta = tuple(4 if flag else 2 for flag in big)
            assert cf(beta).denominator % 2 == 1
            for r in ((1, 2, 3) if length <= 6 else (1, 2)):
                classes, total = ht_move_classes(beta, r)
                assert (classes == 1) == (sum(big) <= 1)
                boxes += 1
                vertices += total
    explicit = []
    for r in range(1, 9):
        classes, _ = ht_move_classes((4, 4), r)
        assert classes == r + 1
        explicit.append([r, classes])
    assert cf((4, 4)) == Fraction(4, 15)
    return {'parameter_boxes': boxes, 'parameter_vertices': vertices,
            'K_4_over_15_sheet_count_and_classes': explicit}


def check_normal_coordinate():
    cases = 0
    tether_cases = 0
    for f in range(-25, 26):
        h = (1, f)  # coordinates in (lambda,mu)
        mu = (0, 1)
        determinant = lambda u, v: u[0] * v[1] - u[1] * v[0]
        assert determinant(h, mu) == 1
        assert determinant(h, (1, 0)) == -f
        for a, b in product(range(-12, 13), repeat=2):
            measured = determinant(h, (a, b))
            assert measured == b - f * a
            for t in (-7, -1, 0, 3, 10):
                assert determinant(h, (a + t, b + t * f)) == measured
            cases += 1
    # H_1(B_a)=Z^a, b0=sum b_i. Quotient by one b_j by deleting that
    # coordinate. This is the detector used in the text, not a proof that
    # a proposed three-dimensional isotopy is confined to proper strips.
    for a in range(2, 42):
        for j in range(a):
            for winding in range(-12, 13):
                quotient_vector = [winding for i in range(a) if i != j]
                assert (all(x == 0 for x in quotient_vector)) == (winding == 0)
                tether_cases += 1
    return {'normal_tracks': cases, 'relative_tether_classes': tether_cases}


def splice(pairs, caps, remaining):
    graph = defaultdict(list)
    for a, b in tuple(pairs) + tuple(caps):
        graph[a].append(b)
        graph[b].append(a)
    seen, paths, circles = set(), [], 0
    for start in graph:
        if start in seen:
            continue
        component, todo = set(), [start]
        while todo:
            a = todo.pop()
            if a in component:
                continue
            component.add(a)
            todo.extend(graph[a])
        seen.update(component)
        ends = sorted((v for v in component if v in remaining), key=str)
        if ends:
            assert len(ends) == 2
            paths.append(ends)
        else:
            assert all(len(graph[v]) == 2 for v in component)
            circles += 1
    return sorted(paths, key=str), circles


def assembly_components(orbits, pairs, carrier_length):
    """Compute actual-bearing components from the full attachment graph.

    An annulus contributes chi=0; each Q piece contributes its covering chi.
    Counting actual vertices in each graph component gives its boundary count.
    Parallel graph edges are allowed; genus is then determined by chi and b.
    """
    port_piece = {port: ('Q', j) for j, orbit in enumerate(orbits) for port in orbit}
    usage = Counter(port for pair in pairs for port in pair)
    assert all(count == 1 for count in usage.values())
    assert {port for port in usage if isinstance(port, int)} == set(port_piece)
    graph = defaultdict(set)
    for pair in pairs:
        nodes = [port_piece[x] if isinstance(x, int) else ('A', x) for x in pair]
        graph[nodes[0]].add(nodes[1])
        graph[nodes[1]].add(nodes[0])
    unseen = set(graph)
    data = []
    while unseen:
        component, queue = set(), [min(unseen, key=str)]
        while queue:
            node = queue.pop()
            if node in component:
                continue
            component.add(node)
            queue.extend(graph[node])
        unseen.difference_update(component)
        actual = sorted(x for kind, x in component if kind == 'A')
        q_indices = [j for kind, j in component if kind == 'Q']
        chi = sum(len(orbits[j]) * (1 - carrier_length) for j in q_indices)
        assert actual  # no closed Q component in these test assemblies
        twice_genus = 2 - len(actual) - chi
        assert twice_genus >= 0 and twice_genus % 2 == 0
        data.append({'actual_boundaries': actual, 'Q_pieces': len(q_indices),
                     'chi': chi, 'genus': twice_genus // 2})
    return sorted(data, key=lambda item: item['actual_boundaries'])


def check_new_odd_length_examples():
    # One odd fold, s=3: each Q piece has a=2, genus 2. Two pieces
    # join through an essential wave; p,n lie on opposite sides of it.
    beta = (3, 4, 2)
    frames, _, orbits, labels = plumbing(4, beta, (1, 0))
    assert orbits == [frozenset((0, 3)), frozenset((1, 2))]
    restricted_types = [tuple(sum(frames[j][i] < t for i in orbit)
                              for j, t in enumerate((1, 0))) for orbit in orbits]
    assert restricted_types == [(1, 0), (0, 0)]
    # Only beta[2] is +-2, so the first parameter is an ordinary HT invariant.
    assert abs(beta[0]) > 2 and abs(beta[1]) > 2
    pairs = ((0, 2), (1, 'p'), (3, 'n'))
    first, circles = splice(pairs, ((3, 0),), {1, 2, 'p', 'n'})
    assert first == [[1, 'p'], [2, 'n']] and circles == 0
    last, circles = splice(first, ((2, 1),), {'p', 'n'})
    assert last == [['n', 'p']] and circles == 0
    assert 2 * (2 * (1 - len(beta))) == -8
    components1 = [assembly_components(orbits, pairs, len(beta)),
                   assembly_components(orbits[1:], first, len(beta)),
                   assembly_components([], last, len(beta))]
    assert [[c['genus'] for c in state] for state in components1] == [[4], [2], [0]]
    # Two odd folds, s=3: an explicit four-boundary companion component.
    beta2 = (3, 3, -2)
    _, _, orbits2, labels2 = plumbing(8, beta2, (2, 0))
    assert orbits2 == [frozenset((0, 3, 4, 7)), frozenset((1, 2, 5, 6))]
    pairs2 = ((0, 2), (3, 5), (1, 'p1'), (4, 'p2'), (6, 'n2'), (7, 'n1'))
    first2, circles2 = splice(pairs2, ((7, 0), (3, 4)),
                              {1, 2, 5, 6, 'p1', 'p2', 'n1', 'n2'})
    assert first2 == [[1, 'p1'], [2, 'n1'], [5, 'p2'], [6, 'n2']]
    assert circles2 == 0
    last2, circles2 = splice(first2, ((6, 1), (2, 5)), {'p1', 'p2', 'n1', 'n2'})
    assert last2 == [['n1', 'p2'], ['n2', 'p1']] and circles2 == 0
    chi_piece = 4 * (1 - len(beta2))
    assert chi_piece == -8
    assert (2 - 4 - 2 * chi_piece) // 2 == 7
    assert (2 - 4 - chi_piece) // 2 == 3
    components2 = [assembly_components(orbits2, pairs2, len(beta2)),
                   assembly_components(orbits2[1:], first2, len(beta2)),
                   assembly_components([], last2, len(beta2))]
    assert [[c['genus'] for c in state] for state in components2] == [[7], [3], [0, 0]]
    # A disconnected spanning system where closure MUST repair an interior
    # chamber bounded by two distinct ordinary HT types, on the odd-length
    # slope-10 carrier. Ports 1,2,3,6 are actual reaches. Both original
    # waves have reaches on each side, hence both are essential in B_4.
    parameters3 = (3, 0)
    frames3, _, orbits3, labels3 = plumbing(8, beta, parameters3)
    types3 = [tuple(sum(frames3[j][i] < t for i in orbit)
                    for j, t in enumerate(parameters3)) for orbit in orbits3]
    assert types3 == [(1, 0), (1, 0), (1, 0), (0, 0)]
    assert orbits3 == [frozenset((0, 7)), frozenset((1, 6)),
                       frozenset((2, 5)), frozenset((3, 4))]
    pairs3 = ((0, 4), (5, 7), (1, 'p1'), (2, 'n2'), (3, 'p2'), (6, 'n1'))
    after_seed, cycles_seed = splice(pairs3, ((7, 0),),
                                     {1, 2, 3, 4, 5, 6, 'p1', 'p2', 'n1', 'n2'})
    assert [4, 5] in after_seed and cycles_seed == 0
    # The returning strip next to the empty gap (4,5) contains no original
    # actual reach. It witnesses chamber 3, whose whole faces are F2,F3.
    waves3 = ((0, 4), (5, 7))
    region = lambda x: tuple(a < x < b for a, b in waves3)
    hole_regions = {region(x) for x in (1, 2, 3, 6)}
    assert region(Fraction(15, 2)) == region(Fraction(9, 2))
    assert region(Fraction(9, 2)) not in hole_regions
    assert all(any(a < x < b for x in (1, 2, 3, 6)) and
               any(not a < x < b for x in (1, 2, 3, 6)) for a, b in waves3)
    after_repair, cycles_repair = splice(pairs3, ((7, 0), (2, 3), (4, 5)),
                                         {1, 6, 'p1', 'p2', 'n1', 'n2'})
    assert {frozenset(p) for p in after_repair} == {
        frozenset((1, 'p1')), frozenset((6, 'n1')), frozenset(('n2', 'p2'))}
    assert cycles_repair == 1
    last3, cycles_last = splice(after_repair, ((6, 1),), {'p1', 'p2', 'n1', 'n2'})
    assert last3 == [['n1', 'p1'], ['n2', 'p2']] and cycles_last == 0
    components3 = [assembly_components(orbits3, pairs3, len(beta)),
                   assembly_components([orbits3[1]], after_repair, len(beta)),
                   assembly_components([], last3, len(beta))]
    assert sorted(c['genus'] for c in components3[0]) == [2, 6]
    assert sorted(c['genus'] for c in components3[1]) == [0, 2]
    assert [c['genus'] for c in components3[2]] == [0, 0]
    return {'single_odd_slope_10': {'beta': list(beta), 'labels': labels,
                'companion_orbits': [sorted(o) for o in orbits],
                'restricted_parameters': restricted_types,
                'genus_trajectory': [4, 2, 0], 'last_pairs': last,
                'computed_components': components1},
            'two_odd_slope_6': {'beta': list(beta2), 'labels': labels2,
                'companion_orbits': [sorted(o) for o in orbits2],
                'genus_trajectory': [7, 3, 0], 'last_pairs': last2,
                'computed_components': components2},
            'slope_10_nonproduct_repair': {'labels': labels3,
                'restricted_parameters': types3,
                'nonparallel_faces': [2, 3],
                'Q_piece_counts': [4, 1, 0],
                'initial_component_genera': [6, 2],
                'after_repair_component_genera': [2, 0],
                'closed_pattern_circles_removed': cycles_repair,
                'last_pairs': last3, 'computed_components': components3}}


def main():
    carriers, words = all_bounded_continuants(101)
    result = {
        'status': 'PASS',
        'carriers': check_carriers(carriers, words, 101),
        'horizontal': check_horizontal(),
        'sloped_plumbing': check_sloped_plumbing(),
        'point_criterion': check_point_criterion(),
        'normal_motion_arithmetic': check_normal_coordinate(),
        'new_odd_length_examples': check_new_odd_length_examples(),
        'scope': 'Finite exact arithmetic and explicit permutations only. No certification of isotopy, product confinement, essential assembly, or CW continuity.',
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    from exact_replay import replay
    replay(main, "framed_independent.txt")
