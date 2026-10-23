# Contractibility of the cyclic complex for zero-framed parallels of two-bridge knots

For every nontrivial two-bridge knot, the entire cyclic-distance flag complex of its oppositely oriented zero-framed two-parallel link is contractible. It is an all-even cone with finitely many rooted odd-carrier, odd-band-signature sectors attached at its apex; every such sector is contractible. All genera and twisting values are included, and disconnected spanning surfaces are allowed.

[中文说明](README.zh-CN.md) · [Object and statement](proof/objects.md) · [Theorem 12.4 and proof map](proof/main-theorem.md) · [Sources](sources/bibliography.md) · [Scope](proof/scope.md)

## Result and object

Vertices are ambient-isotopy classes of oriented, componentwise incompressible spanning surfaces without closed components. Boundaries move on their labelled actual boundary tori. Edges are minimum whole-open-complement cyclic-cover width one, and the complex is their flag completion. No identification with the entire original geometric disjointness complex is claimed.

Let $`E`$ be the unique all-even zero-slope HT carrier and $`O(C)`$ the other zero-slope carriers. Then Theorems 1.2 and 12.4 give

```math
X(L)=\mathcal B_E\cup_{\{a\}}
\bigcup_{\beta\in O(C)}\ \bigcup_{\mathbf z\in Z_\beta}X_{\beta,\mathbf z},
\qquad \mathcal B_E=a*Y_E.
```

Here $`a`$ is the standard annulus. The finite signature set $`Z_\beta`$ is defined by the odd-band heights in [§12.4](proof/band-heights.md). Each rooted sector is contractible by Theorem 12.3; there are no non-root cross edges. The all-even base $`Y_E`$ need not be a point and has the exact finite geometric test of [Proposition 4.2](proof/comparison.md). Its marked three-dimensional product recognition is not implemented as software.

**The explicit (P) corollary.** If every non-all-even zero-slope HT expansion has exactly one coefficient of absolute value greater than two, each odd carrier contributes one marked Farey tree. Its vertices are $`p/k`$ with odd $`p`$, $`k>0`$, $`\gcd(p,k)=1`$, and root $`a=(1,0)`$; edges satisfy $`\lvert pk'-p'k\rvert=1`$. The all-even carrier is unrestricted and odd-carrier uniqueness is not required.

Three symbolically exhausted infinite families illustrate the structures:

```math
C_m=K_{(6m+1)/(16m+3)},\quad m\ge1;
\qquad D_m=K_{8m/(20m-1)},\quad m\ge2;
\qquad B_m=K_{(8m^2+2m+2)/(16m^2+8m+5)},\quad m\ge1.
```

The first satisfies (P) but has vertices not adjacent to the annulus. The odd sector of $`D_2=K_{16/39}`$ is a two-dimensional tree of triangulated disks: a path of $`4k+1`$ vertices over each marked denominator $`k`$, four-triangle root fans, and $`4(k+k')`$ triangles over a non-root marked edge. The odd sector of $`B_1=K_{12/29}`$ is three Farey trees at the root. Larger-boundary essential companion pieces exist, but Theorem 13.2 proves that none can occur in any legal global oriented vertex.

## Target paper

The target is Apex Intelligence, *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*, official competition version, 11 September 2026, 48 pages. [Official PDF](https://math.apexin.net/papers/seifert-surfaces.pdf). SHA-256: `34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f`.

Its Theorems A and D (printed p.2) treat knots and links satisfying linking indecomposability. These two-component links have linking number zero and lie outside Theorem D. Printed p.2 also identifies the general-link obstruction in Lemma 4.9 when distinct vertices share a component class. The present result fixes the cyclic object and allows disconnected spanning systems; it does not assert the corresponding theorem for the entire original geometric disjointness complex.

## Proof guide

Start with [Definition 1.1 and the statements](proof/objects.md), then [Theorem 12.4](proof/main-theorem.md). The complete proof is organized as follows; section numbers follow the logical statements rather than filename order.

- Foundations: [HT carriers, §2](proof/carriers.md), [essential assemblies, §3](proof/assemblies.md), [whole complements, §4](proof/comparison.md), and [all-even cone, §5](proof/even-cone.md).
- Original (P) structure: [pure stacks, §6](proof/odd-normal-forms.md), [return winding, §7](proof/odd-returns.md), and [canonical marked Farey tree, §8](proof/odd-trees.md).
- Extended local geometry: [orientation and two-terminal obstruction, §13](proof/assembly-obstruction.md), [bounded parameter blocks, §14](proof/bounded-parameters.md), [ordered one-block systems, §15](proof/ordered-systems.md), and [general returns, §16](proof/boundary-returns.md).
- Complete one-block models: [vertices, §17](proof/odd-vertices.md), [finite integer edges, §18](proof/odd-edges.md), [one-odd triangulated disks, §9](proof/one-odd-disks.md), and [two-odd trees, §11](proof/two-odd-trees.md).
- Universal proof: [coupled band heights and Lemma 12.1 and Theorem 12.2](proof/band-heights.md), [lower neighbours, rank and Theorem 12.3](proof/finite-contraction.md), and [Theorem 12.4](proof/main-theorem.md).
- Applications and limits: [three infinite families, §10](proof/infinite-family.md), [completed reduction and remaining work](proof/reduction-and-remaining.md), [scope and literature](proof/scope.md), and [checked bibliography](sources/bibliography.md).

The proof uses HT's Theorem 1(e) directly, with a bounded-orbit proof. The differing aggregate count in the parenthetical aside on printed p.230 is explained in the bibliography and is not used.

## Reproduce the finite diagnostics

Python 3.8 or later; standard library only. From the repository root:

```sh
python3 -B scripts/check.py --check
python3 -B scripts/check_general.py --check
python3 -B scripts/check_single_odd.py --check
python3 -B scripts/check_coupled_single.py --check
python3 -B scripts/check_multiple_odd.py --check
shasum -a 256 -c MANIFEST.sha256
```

Every `--check` command recomputes and compares the saved outputs without writing. Omitting it regenerates only sibling JSON files in `scripts/`. The two independent review implementations retain their independence from the author's mathematical code. [The computation guide](scripts/README.md) specifies ranges, certificates and output metadata. Finite computations support the arithmetic; geometric edge lifting, the symbolic infinite-family exhaustions and contraction have separate proofs. No proof-assistant certification is claimed.

## AI disclosure

GPT-6.1 Sol, in OpenAI Codex under human direction, developed the proof, ran the computations where applicable, and drafted this text; separate GPT-6.1 Sol sessions in fresh contexts performed adversarial reviews and a novelty check against the cited literature. Claude planned the work, checked key steps against the sources, and reviewed and edited the final text. GPT-6 Astra, also in OpenAI Codex, advised on research direction and submission scope. No human expert has certified the work.

## License

Original prose and computation data are licensed under CC BY 4.0; executable code in `scripts/` is under the MIT License. See [LICENSE](LICENSE). External publications retain their own rights and are cited rather than bundled.
