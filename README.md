# Incompressible spanning surface complexes of parallel clusters

For every nontrivial two-bridge knot, **all parallel clusters, with any integer framing, any positive number of components and any orientations**, have both their cyclic complex $`X(L)`$ and the original geometric complex $`Y(L)=IS(L)`$ strongly deformation retract onto $`MS(L)`$, and hence are contractible. The same conclusion holds for **zero-framed** parallels of every knot obtained from nontrivial two-bridge and torus knots by finitely many connected sums and cables, and for **zero-framed** parallels of any nontrivial fibred knot when the orientation sum is nonzero.

[中文说明](README.zh-CN.md) · [Main theorem and general objects](proof/main-theorem.md) · [Scope](proof/scope.md) · [Checked bibliography](sources/bibliography.md) · [Review status and SHA-256](sources/review-status.md)

## Main statement and proof pages

Let $`L_f(K;\epsilon_1,\ldots,\epsilon_n)`$ denote $`n\ge1`$ labelled winding-one parallels of slope $`\lambda+f\mu`$, and put $`d=\sum_i\epsilon_i`$. In the ranges above,

```math
X(L)\subseteq Y(L),\qquad
|Y(L)|\searrow |X(L)|\searrow |MS(L)|.
```

Both arrows are strong deformation retractions. $`MS(L)`$ is the taut **cyclic** subcomplex, contractible by [PS, Theorem 1.1]. For two-bridge companions, $`fd\ne0`$ gives the stronger equality $`X=Y=MS(L)`$; this need not be a single vertex. For example the two coherently oriented framing-one parallels of $`K_{4/15}`$ have distinct genus-two vertices.

- [Zero-framed clusters](proof/zero-framed-clusters.md): one-boundary circular envelopes; nonparallel multi-boundary systems with path-shaped complementary regions; ordinary roots, exhaustive closure and face-compatible prisms.
- [Arbitrary integer framings](proof/framed-clusters.md): the actual linking-corrected spanning slopes, nonzero fibre evaluation, balanced nonzero slopes, ordinary transverse winding and the torus-annulus exception.
- [Recursive and fibred companions](proof/recursive-and-fibred.md): whole-system reflection closure under connected sum and cabling, followed by the path closure; direct compact-lift purity for an entire nonzero-class system in a fibred exterior.

Vertices are ordinary ambient-isotopy classes of compact oriented componentwise incompressible spanning systems with no closed components, using each actual labelled boundary torus once. Disconnected surfaces and arbitrary genus are allowed; boundaries move on their own tori. $`X`$ uses minimum width one of **whole open complements** in the one total-linking cyclic cover, then flag completion. $`Y`$ uses simultaneous geometric disjointness of whole representatives, with no flag completion inserted in its definition. The actual framed spanning curves and all conventions are in [the main theorem](proof/main-theorem.md).

The first arrow is the mathematical comparison [CW, Part 7, Theorem D], fixed at commit `f6f44253f2ed539a74bf4cfdc99fed299e386546` in [the public reference](https://github.com/iamwangxi/apex-p01-seifert-fibred-links/blob/f6f44253f2ed539a74bf4cfdc99fed299e386546/proof/part7.md#1-objects-and-statements). The three proof pages check its non-splitness, vertex and peripheral hypotheses. The comparison alone does not assert contractibility. The concatenated deformation fixes $`MS(L)`$ throughout.

## Relation to the competition paper

The target is Apex Intelligence, *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*, official competition version, 11 September 2026, 48 pages. [Official PDF](https://math.apexin.net/papers/seifert-surfaces.pdf). SHA-256: `34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f`.

Theorems A and D, printed p.2, treat knots and linking-indecomposable links. Zero-framed clusters with at least two components have zero pairwise linking and lie outside that linking condition. The paper identifies the shared-component obstruction to its Lemma 4.9 for general links. The result here permits disconnected spanning systems and proves the stated extension for the original geometric complex as well. Some nonzero-framed or one-component cases overlap the target's range; they are not all represented as new cases. Theorem D of [CW] is distinct from the competition paper's Theorem D.

## Detailed two-parallel structures

The detailed carrier classification concerns **two oppositely oriented zero-framed parallels**. Start with [Definition 1.1](proof/objects.md) and [Theorems 12.4–12.5](proof/main-theorem.md). The cyclic complex is an all-even cone and rooted odd-band signature sectors. Under condition (P), those sectors are marked Farey trees. One-odd one-block sectors can instead be trees of triangulated disks, and two-odd one-block sectors can be several trees at the root. These explicit simplex descriptions concern $`X`$ in that specialization.

The proof guide is [essential assemblies, §3](proof/assemblies.md), [whole complements, §4](proof/comparison.md), [the all-even cone, §5](proof/even-cone.md), [ordinary returns, §7](proof/odd-returns.md), [two-terminal obstruction, §13](proof/assembly-obstruction.md), [rooted band heights, §12](proof/band-heights.md), and [finite contraction](proof/finite-contraction.md). The [three infinite families](proof/infinite-family.md) have separate symbolic exhaustion proofs. Multi-boundary pieces excluded by the **two-terminal** obstruction can occur in larger clusters; the cluster proofs retain them.

## Reproduce the evidence

Python 3.8 or later, standard library only. From the repository root:

```sh
python3 -B scripts/verify_package.py
```

This **read-only** command first checks the existing `MANIFEST.sha256`, actually reruns all eleven diagnostic implementations against their saved deterministic outputs, and checks the manifest again. It never repairs evidence before checking it. To rerun just the computations use `python3 -B scripts/run_all.py`. Individual diagnostic commands take `--check`; omitting it regenerates their sibling output files in `scripts/`. Manifest generation is a separate packaging operation. [The computation guide](scripts/README.md) gives ranges and evidence limits.

General Montesinos/arborescent companions, balanced arbitrary fibred companions outside the recursive class, and nonzero framings outside the two-bridge theorem remain uncovered. See [scope](proof/scope.md).

## AI disclosure and review status

**Status: accepted after one fresh-context AI adversarial review of each source argument.** [The review record](sources/review-status.md) identifies the source manuscripts and reviews by SHA-256 and specifies the incorporated repairs.

GPT-6.1 Sol, in OpenAI Codex under human direction, developed the two-bridge cyclic, zero-framed-cluster and integer-framed arguments, computations and integration. Separate fresh GPT-6.1 Sol contexts performed the recorded adversarial reviews. **GPT-6 Astra wrote the recursive-class and arbitrary-fibred-companion manuscript**, in addition to advising on direction and scope. Claude planned and reviewed parts of the earlier two-parallel work and checked sources. This integration incorporates the supplied whole-system purity repair and stationary-event conventions. It received local consistency and diagnostic checks; no further fresh-context integration review, human expert certification or proof-assistant certification is claimed.

## License

Original prose and computation data are licensed under CC BY 4.0; executable code in `scripts/` is under the MIT License. See [LICENSE](LICENSE). External publications retain their own rights and are cited rather than bundled.
