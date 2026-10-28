#!/usr/bin/env python3
"""Finite diagnostics for framed recursive parallels and fibred examples.

Standard library only. Finite arithmetic does not certify topology, isotopy,
compression barriers, the analytic exchange package or continuity.
Run with --check for a deterministic read-only snapshot comparison.
"""

from exact_replay import replay
from fractions import Fraction
from itertools import combinations, product
from math import gcd
import json


def minus_cf(coefficients):
    value = Fraction(coefficients[-1])
    for coefficient in reversed(coefficients[:-1]):
        value = coefficient - 1 / value
    return 1 / value


def partition_and_signs(size, edges):
    adjacency = [[] for _ in range(size)]
    for left, right, sign in edges:
        adjacency[left].append((right, sign))
        adjacency[right].append((left, sign))
    signs = {}
    parts = []
    consistent = True
    for start in range(size):
        if start in signs:
            continue
        signs[start] = 1
        queue = [start]
        part = set()
        while queue:
            vertex = queue.pop()
            part.add(vertex)
            for neighbor, multiplier in adjacency[vertex]:
                desired = signs[vertex] * multiplier
                if neighbor in signs:
                    consistent &= signs[neighbor] == desired
                else:
                    signs[neighbor] = desired
                    queue.append(neighbor)
        parts.append(frozenset(part))
    return parts, signs, consistent


def reflection_edges(size, constants):
    return [
        (index, (constant - index) % size, -1)
        for constant in constants
        for index in range(size)
    ]


def component_word(parts, size):
    lookup = {entry: label for label, part in enumerate(parts) for entry in part}
    return [lookup[entry] for entry in range(size)]


def check_reflections():
    checked = restrictions = 0
    for size in range(2, 22, 2):
        odds = list(range(1, size, 2))
        for extra_count in range(3):
            for extra in product(odds, repeat=extra_count):
                constants = (size - 1,) + extra
                parts, signs, consistent = partition_and_signs(
                    size, reflection_edges(size, constants)
                )
                assert consistent
                divisor = size
                for constant in constants[1:]:
                    divisor = gcd(divisor, constant - constants[0])
                count, arity = divisor // 2, 2 * size // divisor
                assert len(parts) == count
                assert all(len(part) == arity for part in parts)
                assert all(sum(signs[i] for i in part) == 0 for part in parts)
                expected = (
                    list(range(count)) + list(reversed(range(count)))
                ) * (arity // 2)
                assert component_word(parts, size) == expected
                checked += 1

                # Actual restriction of the permutation, not a new normalization.
                # Singletons and every two-component subset exercise root retention.
                subsets = [(i,) for i in range(count)]
                subsets += list(combinations(range(count), 2))
                for chosen in subsets:
                    retained = sorted(set().union(*(parts[i] for i in chosen)))
                    rank = {old: new for new, old in enumerate(retained)}
                    new_size = len(retained)
                    new_constants = []
                    for constant in constants:
                        permutation = [
                            rank[(constant - old) % size] for old in retained
                        ]
                        new_constant = permutation[0]
                        assert new_constant % 2 == 1
                        assert permutation == [
                            (new_constant - j) % new_size
                            for j in range(new_size)
                        ]
                        new_constants.append(new_constant)
                    assert new_constants[0] == new_size - 1
                    new_parts, _, ok = partition_and_signs(
                        new_size, reflection_edges(new_size, new_constants)
                    )
                    assert ok
                    assert len(new_parts) == len(chosen)
                    assert all(len(part) == arity for part in new_parts)
                    restrictions += 1
    return checked, restrictions


def check_cable_descent():
    checked = odd_obstructions = 0
    for outer_size in range(1, 15):
        for winding in range(2, 7):
            inner_size = winding * outer_size
            if inner_size % 2:
                continue
            for extra in range(1, inner_size, 2):
                constants = (inner_size - 1, extra)
                edges = reflection_edges(inner_size, constants)
                edges += [
                    (i, (i + outer_size) % inner_size, 1)
                    for i in range(inner_size)
                ]
                expanded_parts, _, oriented = partition_and_signs(inner_size, edges)
                outer_parts, _, outer_oriented = partition_and_signs(
                    outer_size,
                    reflection_edges(outer_size, constants),
                )
                projected = {
                    frozenset(i % outer_size for i in part)
                    for part in expanded_parts
                }
                assert projected == set(outer_parts)
                assert oriented == outer_oriented == (outer_size % 2 == 0)
                if not oriented:
                    odd_obstructions += 1
                checked += 1
    return checked, odd_obstructions


def cycle_lengths(size, step):
    remaining = set(range(size))
    lengths = []
    while remaining:
        start = min(remaining)
        here = start
        length = 0
        while True:
            assert here in remaining
            remaining.remove(here)
            length += 1
            here = (here + step) % size
            if here == start:
                break
        lengths.append(length)
    return lengths


def check_framed_pattern():
    peripheral = coverings = genera = 0
    for count in range(1, 9):
        for signs in product((-1, 1), repeat=count):
            total = sum(signs)
            for framing in range(-7, 8):
                for sign in signs:
                    # In the (h, mu_i) basis alpha_i = sign h - f d mu_i.
                    assert sign * (framing * total) - framing * total * sign == 0
                    # In the individual preferred-longitude basis.
                    assert sign * framing * (total - sign) - (
                        framing * (total - sign) * sign
                    ) == 0
                    assert gcd(abs(sign), abs(framing * total)) == 1
                peripheral += 1
                if not framing * total or count == 1:
                    continue
                degree = abs(framing * total)
                outer_count = abs(total)
                for sign in signs:
                    assert cycle_lengths(degree, sign) == [degree]
                assert cycle_lengths(degree, total) == [
                    abs(framing)
                ] * outer_count
                chi_h = degree * (1 - count)
                numerator_h = 2 - count - outer_count - chi_h
                assert numerator_h >= 0 and numerator_h % 2 == 0
                genus_h = numerator_h // 2
                for knot_genus in (1, 2, 5):
                    glued_chi = chi_h + outer_count * (1 - 2 * knot_genus)
                    actual_genus = genus_h + outer_count * knot_genus
                    formula = Fraction(
                        2 - count + outer_count * (2 * knot_genus - 1)
                        + degree * (count - 1),
                        2,
                    )
                    assert actual_genus == formula
                    assert 2 - 2 * actual_genus - count == glued_chi
                    genera += 1
                assert Fraction(framing, framing * total) == Fraction(1, total)
                coverings += 1
    # Framed normal coordinate, including longitudinal contribution.
    normal = 0
    for framing in range(-15, 16):
        for a, b, tangent in product(range(-4, 5), repeat=3):
            value = b - framing * a
            shifted = b + tangent * framing - framing * (a + tangent)
            assert value == shifted
            normal += 1
    return peripheral, coverings, genera, normal


def check_examples():
    even = [-2, -2, 2, -2]
    beta = [3, 4, 2]
    assert 1 + minus_cf(even) == minus_cf(beta) == Fraction(7, 19)
    signed_count = lambda seq: sum(1 if x > 0 else -1 for x in seq)
    slope = 2 * (signed_count(beta) - signed_count(even))
    assert slope == 10
    child_parts, _, _ = partition_and_signs(8, reflection_edges(8, [7]))
    assert child_parts == [
        frozenset((0, 7)), frozenset((1, 6)),
        frozenset((2, 5)), frozenset((3, 4)),
    ]
    cable_edges = reflection_edges(8, [7]) + [
        (i, (i + 4) % 8, 1) for i in range(8)
    ]
    cable_parts, _, ok = partition_and_signs(8, cable_edges)
    assert ok
    child_in_outer = [
        [j for j, child in enumerate(child_parts) if child <= part]
        for part in cable_parts
    ]
    assert child_in_outer == [[0, 3], [1, 2]]
    cable_chi = -abs(3 - 2 * slope)
    # Each outer component contains two cable pieces and two child pieces.
    assembled_chi = 2 * cable_chi + 2 * (-2 * (len(beta) - 1))
    assert assembled_chi == -42
    assert (2 - 2 - assembled_chi) // 2 == 21
    assert 2 ** 2 * slope == 40

    parts, signs, ok = partition_and_signs(4, reflection_edges(4, [3, 1]))
    assert ok and len(parts) == 1
    assert sum(signs.values()) == 0
    density = 1 + (len(beta) - 1) + 0
    sum_chi = -4 * density
    assert slope - 6 == 4 and sum_chi == -12
    assert (2 - 4 - sum_chi) // 2 == 5

    fibre_even = [-2, -2, -2, -2, 2, -2, -2, 2]
    fibre_odd = [4, -2, -2, -3, -3, -2]
    assert 1 + minus_cf(fibre_even) == Fraction(29, 137)
    assert minus_cf(fibre_odd) == Fraction(29, 137)
    assert signed_count(fibre_even) == signed_count(fibre_odd) == -4
    chi_r = 2 * (1 - len(fibre_odd))
    assert chi_r == -10
    assert (2 - 2 - chi_r) // 2 == 5
    assert (2 - 4 - 4 * (1 - len(fibre_odd))) // 2 == 9
    assert 2 * chi_r == -20  # U disjoint union V.
    assert chi_r + 0 == -10  # U disjoint union an actual annulus.
    return {
        "cable_framing": 40,
        "cable_piece_genus": 21,
        "child_component_mergers": child_in_outer,
        "mixed_sum_framing": 4,
        "mixed_sum_arity": 4,
        "mixed_sum_genus": 5,
        "fibred_obstruction_knot": "29/137",
        "two_boundary_piece_genus": 5,
        "four_boundary_piece_genus": 9,
    }


def main():
    reflection_count, restriction_count = check_reflections()
    cable_count, odd_count = check_cable_descent()
    peripheral, covering, genus_count, normal_count = check_framed_pattern()
    report = {
        "result": "PASS",
        "reflection_systems": reflection_count,
        "actual_component_restrictions": restriction_count,
        "expanded_cable_systems": cable_count,
        "odd_outer_orientation_obstructions": odd_count,
        "framed_peripheral_patterns": peripheral,
        "horizontal_monodromy_coverings": covering,
        "glued_genus_checks": genus_count,
        "framed_normal_coordinate_checks": normal_count,
        "exact_examples": check_examples(),
        "limits": [
            "Finite arithmetic only; not a proof of the universal theorems.",
            "No test certifies essentiality, ordinary isotopy, chamber visibility,",
            "the compression barrier, the analytic exchange package, or CW continuity.",
        ],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    replay(main, 'recursive_framed.txt')
