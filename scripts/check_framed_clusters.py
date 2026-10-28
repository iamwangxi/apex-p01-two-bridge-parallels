#!/usr/bin/env python3
"""Exact offline finite diagnostics; standard library only.
No topology certification. No file access by the mathematical implementation.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import gcd


def minus_cf(coefficients):
    value = Fraction(coefficients[-1])
    for coefficient in reversed(coefficients[:-1]):
        value = coefficient - 1 / value
    return 1 / value


@lru_cache(None)
def admissible_tails(value):
    """All |b_i|>=2 minus tails, using decreasing numerator recursion."""
    assert 0 < abs(value) < 1
    reciprocal = 1 / value
    floor = reciprocal.numerator // reciprocal.denominator
    choices = {floor}
    if reciprocal.denominator != 1:
        choices.add(floor + 1)
    result = []
    for coefficient in sorted(choices):
        if abs(coefficient) < 2:
            continue
        tail = coefficient - reciprocal
        if tail == 0:
            result.append((coefficient,))
        else:
            assert abs(tail.numerator) < abs(value.numerator)
            for suffix in admissible_tails(tail):
                result.append((coefficient,) + suffix)
    return tuple(result)


def expansions(value):
    return tuple(
        (integer, coefficients)
        for integer in (0, 1)
        for coefficients in admissible_tails(value - integer)
    )


def signature(coefficients):
    return sum(1 if coefficient > 0 else -1 for coefficient in coefficients)


def peripheral_and_horizontal_checks():
    modes = horizontal = genus_cases = 0
    for n in range(1, 10):
        for signs in product((-1, 1), repeat=n):
            d = sum(signs)
            for framing in range(-8, 9):
                k = framing * d
                modes += 1
                assert sum(signs) == d
                for epsilon in signs:
                    # Basis (h, mu_i); Phi=(fd, epsilon).
                    actual = (epsilon, -k)
                    assert actual[0] * k + actual[1] * epsilon == 0
                    assert gcd(abs(actual[0]), abs(actual[1])) == 1
                    # In individual preferred (lambda_i^0, mu_i).
                    meridian_coefficient = -framing * (d - epsilon)
                    longitude_value = framing * (d - epsilon)
                    assert epsilon * longitude_value + epsilon * meridian_coefficient == 0
                    assert meridian_coefficient == framing * epsilon - k
                if k == 0:
                    continue
                horizontal += 1
                r = abs(d)
                degree = abs(k)
                assert gcd(degree, r) == r
                assert all(gcd(degree, abs(e)) == 1 for e in signs)
                assert degree // r == abs(framing)
                chi_pattern = degree * (1 - n)
                boundary_pattern = n + r
                genus_pattern_twice = 2 - boundary_pattern - chi_pattern
                assert genus_pattern_twice >= 0 and genus_pattern_twice % 2 == 0
                # A full horizontal return moves the outer trace one step.
                fibre_displacement = Fraction(1, k)
                normal_displacement = framing * fibre_displacement
                assert normal_displacement == Fraction(1, d)
                assert r * normal_displacement in (-1, 1)
                assert k * fibre_displacement == 1
                for genus_knot in range(1, 5):
                    chi_surface = r * (1 - 2 * genus_knot) + chi_pattern
                    twice_genus = 2 - n - chi_surface
                    assert twice_genus >= 2 and twice_genus % 2 == 0
                    assert chi_surface < 0
                    assert twice_genus == (
                        2 - n + r * (2 * genus_knot - 1) + degree * (n - 1)
                    )
                    if n == 1:
                        assert twice_genus == 2 * genus_knot
                    genus_cases += 1
    return modes, horizontal, genus_cases


def normal_coordinate_checks():
    count = 0
    for framing in range(-20, 21):
        normal = lambda a, b: b - framing * a
        assert normal(1, framing) == 0
        assert normal(0, 1) == 1
        assert normal(1, 0) == -framing
        for a in range(-10, 11):
            for b in range(-10, 11):
                for tangent in (-3, 0, 4):
                    assert normal(a + tangent, b + framing * tangent) == normal(a, b)
                count += 1
    return count


def component_orbits(n, constants):
    unseen = set(range(n))
    orbits = []
    while unseen:
        todo = [min(unseen)]
        orbit = set()
        while todo:
            point = todo.pop()
            if point in orbit:
                continue
            orbit.add(point)
            todo.extend((constant - point) % n for constant in constants)
        unseen -= orbit
        orbits.append(orbit)
    return sorted(orbits, key=min)


def fold_checks():
    tuples = subsystem_cases = 0
    for n in range(2, 42, 2):
        odds = tuple(range(1, n, 2))
        systems = [(n - 1,)]
        systems.extend((n - 1, second) for second in odds)
        systems.extend((n - 1, second, third) for second in odds for third in odds)
        for constants in systems:
            e = n
            for constant in constants[1:]:
                e = gcd(e, constant - constants[0])
            assert e % 2 == 0
            q, arity = e // 2, 2 * n // e
            assert arity % 2 == 0
            orbits = component_orbits(n, constants)
            assert len(orbits) == q
            assert all(len(orbit) == arity for orbit in orbits)
            labels = {
                point: index
                for index, orbit in enumerate(orbits)
                for point in orbit
            }
            word = tuple(labels[i] for i in range(n))
            walk = tuple(range(q)) + tuple(reversed(range(q)))
            assert word == walk * (arity // 2)
            assert all(labels[i] == labels[n - 1 - i] for i in range(n))
            if q <= 5:
                subsets = [
                    tuple(i for i in range(q) if mask & (1 << i))
                    for mask in range(1, 1 << q)
                ]
            else:
                subsets = [(i,) for i in range(q)]
                subsets += [tuple(range(i)) for i in range(1, q + 1)]
                subsets += [tuple(range(i, q)) for i in range(q)]
            for subset in subsets:
                relabel = {old: new for new, old in enumerate(subset)}
                retained = tuple(relabel[label] for label in word if label in relabel)
                k = len(subset)
                expected = (tuple(range(k)) + tuple(reversed(range(k)))) * (arity // 2)
                assert retained == expected
                subsystem_cases += 1
            tuples += 1
    return tuples, subsystem_cases


def carrier_checks():
    knots = carriers = genera = 0
    for denominator in range(3, 82, 2):
        for numerator in range(1, denominator):
            if gcd(numerator, denominator) != 1:
                continue
            value = Fraction(numerator, denominator)
            data = expansions(value)
            even = [
                coefficients
                for _, coefficients in data
                if all(coefficient % 2 == 0 for coefficient in coefficients)
            ]
            assert len(even) == 1 and len(even[0]) % 2 == 0
            baseline = signature(even[0])
            torus = numerator in (1, denominator - 1)
            for integer, coefficients in data:
                assert integer + minus_cf(coefficients) == value
                slope = 2 * (signature(coefficients) - baseline)
                assert slope % 2 == 0
                if all(coefficient % 2 == 0 for coefficient in coefficients):
                    assert slope == 0
                if len(coefficients) == 1:
                    assert torus and denominator % 2 == 1
                    assert abs(slope) == 2 * denominator
                if slope != 0 and not torus:
                    assert len(coefficients) >= 2
                    assert any(coefficient % 2 for coefficient in coefficients)
                    for arity in range(2, 42, 2):
                        chi = arity * (1 - len(coefficients))
                        twice_genus = 2 - arity - chi
                        assert twice_genus >= 2 and twice_genus % 2 == 0
                        genera += 1
                carriers += 1
            knots += 1
    return knots, carriers, genera


def examples():
    value = Fraction(7, 19)
    data = expansions(value)
    baseline = -2  # E=(-2,-2,2,-2).
    expected = {
        (0, (2, -2, -2, -3), 0),
        (0, (3, 3, -2), 6),
        (0, (3, 4, 2), 10),
        (1, (-2, -3, -2, -3), -4),
        (1, (-2, -2, 2, -2), 0),
        (1, (-2, -2, 3, 2), 4),
    }
    observed = {
        (integer, coefficients, 2 * (signature(coefficients) - baseline))
        for integer, coefficients in data
    }
    assert observed == expected
    assert minus_cf((4, 4)) == Fraction(4, 15)
    assert all(abs(coefficient) != 2 for coefficient in (4, 4))
    # The topological distinction uses the complete HT move relation in the
    # written proof. The script checks its input coefficients and Euler data.
    n, d, framing, genus_knot = 2, 2, 1, 1
    chi = abs(d) * (1 - 2 * genus_knot) - abs(framing * d) * (n - 1)
    assert chi == -4 and (2 - n - chi) // 2 == 2
    return len(expected)


def main():
    modes, horizontal, genera = peripheral_and_horizontal_checks()
    print(f"PASS peripheral modes: {modes}; horizontal classes: {horizontal}; genus cases: {genera}")
    print(f"PASS framed normal-coordinate tracks: {normal_coordinate_checks()}")
    folds, subsystems = fold_checks()
    print(f"PASS odd-fold systems: {folds}; inherited subsystem words: {subsystems}")
    knots, carriers, sloped_genera = carrier_checks()
    print(f"PASS HT rational inputs: {knots}; carriers: {carriers}; sloped genus cases: {sloped_genera}")
    print(f"PASS K_7/19: {examples()} carriers; K_4/15 nonpoint example arithmetic")
    print("Scope: finite exact algebra only; the topology is proved in the proof pages.")


if __name__ == "__main__":
    from exact_replay import replay
    replay(main, "framed_clusters.txt")
