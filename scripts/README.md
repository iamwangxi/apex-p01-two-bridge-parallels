# Exact finite diagnostics and independent implementations

[Contents](../README.md) · [Symbolic family proofs](../proof/infinite-family.md) · [Finite contraction](../proof/finite-contraction.md)

Python 3.8 or later, standard library only. From the repository root run:

```sh
python3 -B scripts/verify_package.py
# Computations alone, without the manifest check:
python3 -B scripts/run_all.py
```

Each individual command with `--check` recomputes and compares its saved JSON or stdout snapshot without writing. The all-in-one verifier validates the **existing** manifest, then the four integrated proof/review bindings, before running the thirteen commands; it checks the manifest again afterwards. It never regenerates evidence during acceptance. Omit `--check` to regenerate the outputs listed below. Every output is a sibling file in `scripts/`, resolved relative to the script rather than the working directory. `diagnostic_io.py` restricts new outputs to that directory and implements replay comparison; all saved values and stdout are deterministic, with no timestamps or elapsed-time fields. No comparison field is ignored. Script hashes and mathematical data are checked. No network or third-party dependencies are used.

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

## Cluster diagnostics

Six additional implementations retain their exact arithmetic routines and finite ranges; source-manuscript hash checks were moved to the public [review fingerprint record](../sources/review-status.json), so no diagnostic reads a private source. The author and independent implementations remain separate. All outputs below are sibling `.txt` snapshots compared byte for byte by `exact_replay.py`; omitting `--check` regenerates only that snapshot.

- `check_zero_framed_clusters.py`: `zero_framed_clusters.txt`; 1,496 even-sheet fold systems, 2,046 signed chamber words, 6,005 rational envelopes, and the genus 19 and 39 nonparallel four-boundary examples.
- `check_zero_framed_independent.py`: `zero_framed_independent.txt`; independently reconstructs HT interval permutations and restricted rectangles, one-sided closures, two-colour barriers, rational envelopes and both examples. The default uses the full finite ranges; `--quick` is not a public replay option.
- `check_framed_clusters.py`: `framed_clusters.txt`; actual peripheral equations and horizontal covering arithmetic for $`1\le n\le9`$, $`-8\le f\le8`$, all signs, knot genera 1–4; framed normal tracks, odd folds through 40 sheets, and reduced rational knots with odd denominator at most 81. It checks the $`7/19`$ slopes and the $`4/15`$ nonpoint arithmetic.
- `check_framed_independent.py`: `framed_independent.txt`; complete bounded continuants through denominator 101, actual horizontal monodromy permutations, ordinary return displacement arithmetic, sloped rectangles, point-criterion move orbits and explicit odd-length/nonproduct repairs. It imports no author's mathematical module.
- `check_recursive_systems.py`: `recursive_systems.txt`; 1,079 reflection systems, 2,886 whole-component deletions, 1,684 expanded cable systems, 3,213 expanded sums, 27,302 cable root gaps, and the actual winding-two HT example with genus 13 per piece.
- `check_recursive_independent.py`: `recursive_independent.txt`; 29,979 raw HT parameter boxes, 3,600 expanded sums, 1,800 cable systems, 720 alternating nested systems, 88,828 component restrictions and 365,532 retained squares, as well as primitive peripheral lattice classes and opposite internal torus slopes. A fixed random seed selects the recorded finite samples; it does not appear as a timestamp. The expanded graph is built before comparison with the reflection quotient.

The exact replay snapshots give all counts and bounds. No new script imports another new script's mathematical routines. Only the shared stdout-comparison helper is imported. Code and result reads/writes remain inside this package; `-B` prevents bytecode-cache creation. There are no network calls or third-party packages.

## Integrity and generation are separate

`verify_package.py` checks manifest syntax, duplicate/unsafe entries, exact file coverage and SHA-256, then validates all integrated-page digests in the review record **before** executing `run_all.py`. On a mismatch it exits without rewriting the manifest or any saved result. `run_all.py` actually executes all thirteen `--check` commands; it does not trust an earlier PASS record. After any intentional generation, rebuild the manifest separately outside the repository, excluding `.DS_Store` and the manifest itself, then copy it into place. Acceptance is read-only.

The fibre-branch repair is a geometric proof in §10 of [the recursive/fibred page](../proof/recursive-and-fibred.md). No finite script claims to repair an isotopy-descent gap or prove its product lemma.


## Framed recursive and balanced-fibred diagnostics

Two further independent implementations are included and executed by both verification entry points:

- `check_recursive_framed.py` writes `recursive_framed.txt`. It checks signed reflection systems and actual component restrictions, expanded cable descent including odd-outer orientation obstructions, framed peripheral classes, horizontal monodromy and genus formulas, and the exact framed recursive/fibred examples in [the proof](../proof/framed-recursive-and-fibred.md).
- `check_recursive_framed_independent.py` writes `recursive_framed_independent.txt`. It builds every actual HT band vertex, core edge and interval plumbing edge before extracting components, restricts actual rectangles before rebuilding them, enumerates continuants by denominator growth without a length cutoff, and tests primitive cable homology classes without presupposing the one-outer/p-inner result. It independently distinguishes restricted plumbing parameters from large-band heights in band order. The examples include nonparallel child mergers, opposite-slope sums, the fibred shared-component obstruction and an alternating sum/cable construction.

The independent implementation checks 21,414 raw band/square systems (20,854 orientable), 40,180 actual component reconstructions, 163,744 primitive cable lattice classes (2,862 integer-child classes), 3,526 annular-resonance exclusions, 2,688 horizontal pattern classes and 10,752 glued genera. Its exact examples give outer genus 21 at framing 40, genus 5 at framing 4, and genus 57 in the nested example at framing 36. The fibred obstruction has genuine two-boundary genus-five and four-boundary genus-nine HT pieces. These finite checks do not certify the compression barrier or exchange analysis; those are the text arguments of §§6–9.

Both scripts retain their separate mathematical implementations and full reviewed finite ranges. They import only the shared deterministic stdout replay helper, read/write only their sibling snapshots, and take `--check` for byte-for-byte read-only acceptance. No time, machine path or random execution state is included in their output.
