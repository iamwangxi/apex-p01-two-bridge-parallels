# 4. Equality and cyclic edges from whole complements

[Contents](../README.md) · [Assembly hypotheses](assemblies.md) · [Next: even cone](even-cone.md)

This finite geometric criterion applies also to the all-even base, where no closed arithmetic quotient is asserted. Its three-dimensional product recognition is not implemented in the accompanying scripts.

**Lemma 4.1 (one whole block).** For every spanning system $`H`$, the complement $`M\setminus H`$ is connected, and each cyclic-cover lift maps homeomorphically to it.

**Proof.** A small meridian near an actual boundary of each component crosses that component once and misses every other component. Deleting its crossing segment connects the two local sides in the complement. Thus every component-edge of the connected dual graph of complement regions is a loop. The graph has one vertex. Every complement loop has zero intersection with $`H`$, hence $`\phi=0`$. The restriction of the cyclic cover is consequently trivial on that connected complement, as claimed. ∎

For specified embedded assembly diagrams $`F,H`$, retain coincident whole components and make the rest transverse, with disjoint actual boundaries. Remove an empty marked product region [B, Definition 4.1], or identify a pair of whole parallel components, and repeat. The region must miss **both full systems**, including retained components. Collapsed-boundary degeneracies follow [B, Remark 4.4]. Lemma 3.1 verifies the essentiality and ambient hypotheses of [B, Proposition 4.2].

This process terminates: a non-component push decreases the transverse arc/circle count, while a whole-component identification decreases the number of unpaired components. It gives almost-transverse simplified representatives $`F',H'`$ in the sense of [PS, §3, pp.1494–1495]. The test is finite and geometric: the interior of a connected empty product region is a whole complement chamber, since it is open there and its frontier lies in the two systems or the ambient boundary, so is also relatively closed. Inspect the finitely many normalized chamber boundaries, with their marked horizontal faces and collapsed corners, for the required marked product structure. This does not quantify over an unknown global isotopy and does not claim a software product-recognition algorithm.

Construct $`\mathcal W(F',H')`$ with all chambers of $`M\setminus(F'\cup H')`$ as vertices and all connected wall pieces of $`F'\setminus H'`$ as directed edges, oriented from its negative to positive side. Common components are not walls. Starting at one chamber of height zero, increase height by one across every directed wall. The graph is connected because it cuts the connected whole $`H'`$ complement. A closed walk represents a loop in that complement with signed $`F'`$ crossing number $`\phi=0`$, so the heights are consistent. Set

```math
w(F',H')=\max h-\min h.
```

**Proposition 4.2 (exact geometric test).**

```math
\delta([F],[H])=w(F',H'),\qquad
[F]=[H]\ \Longleftrightarrow\ w=0,\qquad
[F]\sim[H]\ \Longleftrightarrow\ w=1.
```

**Proof.** In one lift of the whole $`H'`$ complement, its chamber heights are exactly the indices of the complete open $`F'`$ blocks, up to one common additive constant. Each chamber has nonempty interior and each open block intersection contains an off-wall point. Thus the height range is the representative width. Simplified position realizes the class minimum by [B, Proposition 4.10, p.7], explicitly extended to all incompressible spanning surfaces in [B, §10, p.22]. Jointly varying both representatives changes nothing: an ambient isotopy carrying one to a fixed representative carries the other too and preserves the linking cover.

If $`w=0`$, no noncoincident $`F'`$ wall exists, since its two adjacent heights differ by one. Hence $`F'`$ is a union of whole $`H'`$ components. It already uses both actual boundary labels, so any additional $`H'`$ component would be closed and forbidden. The systems coincide, with orientations fixed by the actual boundary signs. Conversely coincident representatives give minimum zero. The edge assertion is Definition 1.1. ∎

Independent translations of different companion chambers are never allowed in this test. It includes every companion chamber and every pattern attachment.

**Lemma 4.3 (crossings and connected walls).** A transverse interior intersection forces representative width at least two. Distinct disjoint representatives have class width one if at least one whole spanning surface is connected. In simplified position, an edge involving a connected two-actual-boundary surface and another such surface, or an all-even vertex, has genuinely disjoint representatives.

**Proof.** At a crossing of lifted walls $`\widetilde F_i,\widetilde H_j`$, both consecutive whole $`H`$ blocks $`W_{j-1},W_j`$ meet both consecutive $`F`$ blocks $`U_{i-1},U_i`$ in local quadrants. Since $`W_j=\tau W_{j-1}`$, translating back shows $`W_{j-1}`$ also meets $`U_{i-2}`$. Its width is at least two. This is a whole-block argument.

If connected $`F`$ is disjoint from $`H`$, it is one proper wall in the connected cut block of $`H`$. A nonseparating wall would give a loop crossing $`F`$ once and missing $`H`$, although both are dual to $`\phi`$. Therefore it separates into exactly two nonempty chambers. One lift of the whole $`H`$ block contains exactly one whole lift of $`F`$ and meets the two consecutive $`F`$ blocks on its sides. This gives width one; width zero is excluded for distinct classes by Proposition 4.2.

For the last assertion first simplify, so the width is minimal. Width one excludes transverse intersections. Distinct connected complete surfaces have no common whole component; a connected surface with both actual boundaries cannot coincide with an all-even component having just one actual boundary. Hence in these cases “almost disjoint” is genuinely disjoint. ∎

The connected-wall converse is deliberately not applied to arbitrary pairs of disconnected all-even surfaces. Their exact equality and adjacency remain Proposition 4.2.
