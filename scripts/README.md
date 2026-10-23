# Exact finite diagnostics and independent implementations

[Contents](../README.md) · [Symbolic family proofs](../proof/infinite-family.md) · [Finite contraction](../proof/finite-contraction.md)

Python 3.8 or later, standard library only. From the repository root run:

```sh
python3 -B scripts/check.py --check
python3 -B scripts/check_general.py --check
python3 -B scripts/check_single_odd.py --check
python3 -B scripts/check_coupled_single.py --check
python3 -B scripts/check_multiple_odd.py --check
```

Each command recomputes and compares the saved JSON without writing. Omit `--check` to regenerate the outputs listed below. Every output is a sibling file in `scripts/`, resolved relative to the script rather than the working directory. `diagnostic_io.py` restricts new outputs to that directory and implements replay comparison; only nondeterministic `elapsed_seconds` is excluded from equality. Script hashes and mathematical data are checked. No network or third-party dependencies are used.

## Author's diagnostics

`check.py` writes `checks.json`. It retains the original arithmetic checks: the entire six-expansion family for parameters 1–200; 81 pure-stack bounded boxes with 44,283 states; 10,100 single-chain reflection matchings; 21,032 primitive marked-parent coordinates, including negative numerators; and the exact 8/21, 12/29 and 16/39 expansion tables. Its local higher-boundary witness is a companion surface, not an additional global vertex.

`check_general.py` writes `general_checks.json`. It checks 20 bounded orbit instances and 5,694 states, 6,096 one-block profiles, 2,480 signed folding constraints, and one-block edge/panel/parent diagnostics through total denominator 15. Its rooted transport tests cover 49,714 local cases and 17,794 one-odd middle-sheet augmentations. Seven general height configurations include internal roots, coupled blocks and several odd bands, with total denominator bounds 7–10 as recorded in JSON. It reproduces HT's eight original p.231 counts and checks the complete D-family expansions for parameters 2–100 and B-family expansions for parameters 1–100. The height-domain and signature tests include the actual 74/103 and 76/119 carriers.

## Independent one-odd review implementation

`check_single_odd.py` writes `single_odd_checks.json`. It imports no author's mathematical code. Bounded BFS runs through sheet bound 12; raw rectangle restrictions check 4,355 parameter tuples. Complete finite disk systems use denominator caps 2, 4, 6, 8 and 10, with every edge and triangle and explicit elementary collapses to the root. The largest has 2,579 vertices, 6,362 edges and 3,784 triangles. Subchain descent checks 4,252 vertices and 6,412 different-projection dominations through denominator 12. Exact D-family expansions are checked for parameters 2–200.

`check_coupled_single.py` imports that independent implementation solely for endpoint graphs and raw rectangle matching. It writes `coupled_single_checks.json`, checking 8,127 raw tuples for the coupled 74/103 carrier, then full graph contraction at denominator caps 2, 3, 4 and 5. The largest graph has 3,647 vertices and 18,266 edges; every non-root vertex is removed by verified closed-neighbourhood domination. This implementation does not import the author's height routine.

## Independent multiple-odd review implementation

`check_multiple_odd.py` writes `multiple_odd_checks.json` and three deletion certificates: `12_29-finite-flag.json`, `74_103-finite-flag.json`, and `76_119-finite-flag.json`. It imports no author's mathematical code. Local square permutations are composed explicitly, component folds use a disjoint-set computation, and actual restricted rectangle counts precede height comparisons. Bounded move BFS covers sheet bounds 1–6; 4,406 divisor/sign configurations are checked through sheet count 64. The B family is checked for parameters 1–256 by exact rational arithmetic, without recursive-depth truncation.

The full induced flag complexes at denominator cap 4 and winding chart zero have f-vectors `55,54`, `1799,8674,12284,5408`, and `919,1902,984`. The certificates list every vertex and edge, root identifier, and every removed vertex with its domination vertex. Every complex contracts to the common root. The first has three signatures and the last fifteen; Euler characteristic one is a secondary check, not the contraction certificate.

Output provenance names only public files in this repository. Source-review manuscript hashes have been replaced by the corresponding public proof-file hashes; this packaging change does not change any mathematical computation. Replay checks these hashes too, so regenerate diagnostics after editing watched proof files and regenerate the manifest last.

## Evidence boundary

All recursion uses exact rational arithmetic and strictly decreasing tail denominators. The three infinite families have symbolic all-parameter exhaustion proofs in the text; finite sample counts are not extrapolated. Likewise the local permutation's three-dimensional interpretation, full-system isotopy and return arguments, actual cyclic-edge lifting and universal contraction are mathematical proofs. These scripts do not implement geometric marked-product recognition or proof-assistant certification. Their independence refers to the two mathematical implementations, not to an additional review performed during packaging.
