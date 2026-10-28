#!/usr/bin/env python3
"""Independent finite diagnostics for framed recursive parallels and fibred examples.

The HT calculation builds actual band/core/plumbing edges before components.
Standard library only; no author mathematical module is imported. Finite arithmetic does not certify topology, isotopy,
compression barriers, the analytic exchange package or continuity.
Run with --check for a deterministic read-only snapshot comparison.
"""
from exact_replay import replay
from fractions import Fraction
from itertools import product, combinations
from math import gcd
import json


def cf(coeffs):
    # Continuants of the reciprocal minus continued fraction, not nested division.
    pm2, pm1, qm2, qm1 = -1, 0, 0, 1
    for b in coeffs:
        pm2, pm1 = pm1, b * pm1 - pm2
        qm2, qm1 = qm1, b * qm1 - qm2
    return Fraction(pm1, qm1)


def enumerate_carriers(value):
    cap = value.denominator
    answer, nodes = [], 0

    def visit(pm2, pm1, qm2, qm1, seq):
        nonlocal nodes
        v, t = (qm1, qm2) if qm1 > 0 else (-qm1, -qm2)
        lo, hi = -((cap - t) // v), (cap + t) // v
        for b in range(lo, hi + 1):
            if abs(b) < 2:
                continue
            p, q = b * pm1 - pm2, b * qm1 - qm2
            assert abs(q) > abs(qm1)
            if abs(q) > cap:
                continue
            nodes += 1
            new = seq + (b,)
            for integer in (0, 1):
                if integer + Fraction(p, q) == value:
                    answer.append((integer, new))
            if abs(q) < cap:
                visit(pm1, p, qm1, q, new)

    visit(-1, 0, 0, 1, ())
    return sorted(answer), nodes


def signed_count(coeffs):
    return sum(1 if b > 0 else -1 for b in coeffs)


def square_matching(n, size):
    # Independently use the two finite reversed intervals, not a modular formula.
    return list(reversed(range(n))) + list(reversed(range(n, size)))


def graph_components(vertex_count, edges):
    adj = [[] for _ in range(vertex_count)]
    for u, v, sign in edges:
        adj[u].append((v, sign))
        adj[v].append((u, sign))
    components, signs, oriented = [], {}, True
    for start in range(vertex_count):
        if start in signs:
            continue
        queue, comp = [start], set()
        signs[start] = 1
        while queue:
            u = queue.pop()
            comp.add(u)
            for v, sign in adj[u]:
                wanted = signs[u] * sign
                if v in signs:
                    oriented = oriented and signs[v] == wanted
                else:
                    signs[v] = wanted
                    queue.append(v)
        components.append(comp)
    return components, signs, oriented


def ht_system(coeffs, size, parameters, root=None):
    bands = len(coeffs)
    assert len(parameters) == bands - 1
    odd = [v for v, b in enumerate(coeffs) if b % 2]
    root = odd[0] if root is None and odd else (0 if root is None else root)
    edges = []
    for v, b in enumerate(coeffs):
        for i in range(size):
            j = size - 1 - i if b % 2 else i
            edges.append((v * size + i, v * size + j, -1 if b % 2 else 1))
    for v, n in enumerate(parameters):
        for i, j in enumerate(square_matching(n, size)):
            edges.append((v * size + i, (v + 1) * size + j, 1))
    comps, signs, oriented = graph_components(bands * size, edges)
    parts = [sorted(i for i in range(size) if root * size + i in c) for c in comps]
    order = sorted(range(len(parts)), key=lambda j: parts[j][0])
    comps, parts = [comps[j] for j in order], [parts[j] for j in order]
    rows = []
    for comp, orbit in zip(comps, parts):
        edge_count = sum(u in comp for u, _, _ in edges)
        chi = len(comp) - edge_count
        assert all(sum(v * size + i in comp for i in range(size)) == len(orbit)
                   for v in range(bands))
        restricted = [sum(v * size + i in comp for i in range(n))
                      for v, n in enumerate(parameters)]
        h = [None] * bands
        h[root] = 0
        for v in range(root, bands - 1):
            h[v + 1] = restricted[v] - h[v]
        for v in range(root - 1, -1, -1):
            h[v] = restricted[v] - h[v + 1]
        rows.append({
            "orbit": orbit, "chi": chi, "boundary_count": len(orbit),
            "restricted_plumbing": restricted,
            "large_heights_in_band_order": [h[v] for v, b in enumerate(coeffs) if abs(b) > 2],
        })
        assert chi == -(bands - 1) * len(orbit)
        if oriented:
            numerator = 2 - len(orbit) - chi
            assert numerator >= 0 and numerator % 2 == 0
            rows[-1]["genus"] = numerator // 2
            if odd:
                assert sum(signs[root * size + i] for i in orbit) == 0
    return rows, oriented


def quotient(size, partitions, cable_winding=1):
    # Edges first join whole child components, then actual cable sheets.
    total = size * cable_winding
    edges = []
    for parts in partitions:
        for part in parts:
            for i in part[1:]:
                edges.append((part[0], i, 1))
    if cable_winding > 1:
        for outer in range(size):
            for layer in range(1, cable_winding):
                edges.append((outer, outer + layer * size, 1))
    comps, _, _ = graph_components(total, edges)
    return [sorted(c) for c in comps]


def exact_examples():
    beta = (3, 4, 2)
    even = (-2, -2, 2, -2)
    assert cf(beta) == 1 + cf(even) == Fraction(7, 19)
    slope = 2 * (signed_count(beta) - signed_count(even))
    child, ok = ht_system(beta, 8, (3, 0))
    assert ok and slope == 10
    assert [r["restricted_plumbing"] for r in child] == [[1, 0]] * 3 + [[0, 0]]
    assert [r["large_heights_in_band_order"] for r in child] == [[0, 1]] * 3 + [[0, 0]]
    merged = quotient(4, [[r["orbit"] for r in child]], cable_winding=2)
    cable_rows = []
    for orbit in merged:
        children = [i for i, r in enumerate(child) if set(r["orbit"]) <= set(orbit)]
        outer = sorted({i % 4 for i in orbit})
        chi = len(outer) * (-(2 - 1) * abs(3 - 2 * slope))
        chi += sum(child[i]["chi"] for i in children)
        genus = (2 - len(outer) - chi) // 2
        assert chi == -42 and genus == 21
        cable_rows.append({"outer_labels": outer, "child_components": children,
                           "chi": chi, "genus": genus})
    assert [r["child_components"] for r in cable_rows] == [[0, 3], [1, 2]]

    ht4, ok = ht_system(beta, 4, (1, 0))
    assert ok
    torus4 = [[0, 1], [2, 3]]
    sums = quotient(4, [[r["orbit"] for r in ht4], torus4])
    assert sums == [[0, 1, 2, 3]]
    sum_chi = -4 + sum(r["chi"] for r in ht4)
    assert sum_chi == -12 and (2 - 4 - sum_chi) // 2 == 5

    fibre_even = (-2, -2, -2, -2, 2, -2, -2, 2)
    fibre_odd = (4, -2, -2, -3, -3, -2)
    assert cf(fibre_odd) == 1 + cf(fibre_even) == Fraction(29, 137)
    assert signed_count(fibre_even) == signed_count(fibre_odd) == -4
    r2, ok = ht_system(fibre_odd, 2, (0, 0, 0, 0, 0), root=3)
    assert ok and len(r2) == 1 and r2[0]["genus"] == 5
    r8, ok = ht_system(fibre_odd, 8, (1, 0, 0, 2, 0), root=3)
    assert ok
    assert [r["orbit"] for r in r8] == [[0, 3, 4, 7], [1, 2, 5, 6]]
    assert [r["large_heights_in_band_order"] for r in r8] == [[1, 0, 1], [0, 0, 1]]
    assert all(r["genus"] == 9 for r in r8)

    # Extra nested example: C_{3,2}(K_{7/19} # T(2,-3)), f=36.
    h12, ok = ht_system(beta, 12, (1, 0))
    assert ok
    torus12 = [sorted({i, (1 - i) % 12}) for i in range(12)]
    torus12 = [list(t) for t in sorted({tuple(t) for t in torus12})]
    sum12 = quotient(12, [[r["orbit"] for r in h12], torus12])
    assert sum12 == [list(range(12))]
    nested = quotient(4, [sum12], cable_winding=3)
    assert nested == [list(range(12))]
    nested_chi = -12 + sum(r["chi"] for r in h12) - 4 * (3 - 1) * abs(2 - 3 * 4)
    assert nested_chi == -116 and (2 - 4 - nested_chi) // 2 == 57
    return {
        "cable_C23_K7_19_f40": {"child_HT_rows": child, "outer_rows": cable_rows},
        "sum_K7_19_T2minus3_f4": {"outer_partition": sums, "chi": sum_chi, "genus": 5},
        "fibred_K29_137": {"orientation_double": r2, "accepted_eight_sheet_system": r8,
                            "shared_component_pair_chi": [-20, -10]},
        "extra_C32_sum_f36": {"outer_boundary_count": 4, "chi": nested_chi, "genus": 57},
    }


def raw_ht_box():
    cases = orientable = restrictions = 0
    specs = [((3, 4, 2), range(1, 15), 0),
             ((4, -2, -2, -3, -3, -2), (2, 4, 6), 3)]
    for coeffs, sizes, root in specs:
        for size in sizes:
            for pars in product(range(size + 1), repeat=len(coeffs) - 1):
                rows, ok = ht_system(coeffs, size, pars, root=root)
                cases += 1
                if not ok:
                    continue
                orientable += 1
                assert len({r["boundary_count"] for r in rows}) == 1
                # Independently obtain the meridian word from actual components.
                lookup = {i: j for j, r in enumerate(rows) for i in r["orbit"]}
                word = [lookup[i] for i in range(size)]
                k, arity = len(rows), rows[0]["boundary_count"]
                assert word == (list(range(k)) + list(reversed(range(k)))) * (arity // 2)
                # Restrict the actual plumbing rectangles, then rebuild that surface.
                for j in range(len(rows)):
                    restricted, good = ht_system(coeffs, arity,
                                                rows[j]["restricted_plumbing"], root=root)
                    assert good and len(restricted) == 1
                    assert restricted[0]["chi"] == rows[j]["chi"]
                    restrictions += 1
    return {"raw_band_square_systems": cases, "orientable_systems": orientable,
            "actual_component_reconstructions": restrictions}


def integer_lattice_checks():
    all_cable = integer_child = resonances = 0
    for p in range(2, 8):
        for q in range(-11, 12):
            if not q or gcd(p, q) != 1:
                continue
            for s in range(-20, 21):
                assert p * q != p * p * s
                resonances += 1
            for a in range(1, 25):
                for b in range(-64, 65):
                    if gcd(a, b) != 1 or b + q * a == 0:
                        continue
                    child_slope = Fraction(-b, p * a)
                    outer_slope = Fraction(-p * b, a)
                    assert outer_slope == p * p * child_slope
                    outer_boundary = gcd(a, p * b)
                    inner_boundary = gcd(p * a, b)
                    orbifold_degree = p * abs(b + q * a)
                    chi = Fraction(-(p - 1), p) * orbifold_degree
                    genus_twice = 2 - outer_boundary - inner_boundary - chi
                    assert genus_twice >= 0 and genus_twice % 2 == 0
                    all_cable += 1
                    if child_slope.denominator == 1:
                        assert a == 1 and outer_boundary == 1 and inner_boundary == p
                        assert chi == -(p - 1) * abs(q - p * child_slope)
                        integer_child += 1
    patterns = genera = 0
    for n in range(2, 8):
        for signs in product((-1, 1), repeat=n):
            d = sum(signs)
            for f in range(-6, 7):
                if not f * d:
                    continue
                degree = abs(f * d)
                actual_boundaries = [gcd(degree, e) for e in signs]
                companion_boundaries = gcd(degree, d)
                assert actual_boundaries == [1] * n and companion_boundaries == abs(d)
                chi_h = degree * (1 - n)
                g2_h = 2 - n - companion_boundaries - chi_h
                assert g2_h >= 0 and g2_h % 2 == 0
                for g in range(1, 5):
                    chi_s = chi_h + companion_boundaries * (1 - 2 * g)
                    genus_from_pieces = g2_h // 2 + companion_boundaries * g
                    assert 2 - 2 * genus_from_pieces - n == chi_s
                    assert chi_s == abs(d) * (1 - 2 * g) - abs(f * d) * (n - 1)
                    genera += 1
                patterns += 1
    return {"primitive_cable_lattice_classes": all_cable,
            "integer_child_classes": integer_child,
            "annular_resonance_exclusions": resonances,
            "horizontal_pattern_classes": patterns, "glued_genus_checks": genera}


def main():
    carrier_reports = {}
    for value in (Fraction(7, 19), Fraction(29, 137)):
        carriers, visited = enumerate_carriers(value)
        evens = [c for _, c in carriers if all(b % 2 == 0 for b in c)]
        assert len(evens) == 1
        base = signed_count(evens[0])
        carrier_reports[str(value)] = {
            "prefix_nodes": visited,
            "carriers": [{"integer_part": r, "coefficients": list(c),
                          "slope": 2 * (signed_count(c) - base)} for r, c in carriers],
        }
    assert len(carrier_reports["7/19"]["carriers"]) == 6
    assert len(carrier_reports["29/137"]["carriers"]) == 14
    result = {"result": "PASS", "exact_examples": exact_examples(),
              "carrier_enumeration": carrier_reports,
              "raw_HT_diagnostics": raw_ht_box(),
              "lattice_diagnostics": integer_lattice_checks(),
              "limits": "Finite arithmetic and actual prescribed gluing graphs only; no topology, isotopy, analysis, barrier, or continuity certification."}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    replay(main, 'recursive_framed_independent.txt')
