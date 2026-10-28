# Main theorem: spanning surface complexes of parallel clusters

[Contents](../README.md) · [Scope](scope.md) · [Sources](../sources/bibliography.md)

## General objects

Fix a nontrivial knot $`K`$, a meridian–preferred-longitude basis $`(\mu,\lambda)`$, an integer framing $`f`$, and $`n\ge1`$ labelled winding-one parallels of slope $`\lambda+f\mu`$. Give them signs $`\epsilon_i\in\{1,-1\}`$ and write $`d=\sum_i\epsilon_i`$. Denote the oriented link by $`L_f(K;\epsilon)`$.

A vertex is an ordinary ambient-isotopy class of compact properly embedded oriented, componentwise incompressible spanning systems: one prescribed oriented curve on each actual labelled boundary torus and no closed components. Disconnected surfaces and arbitrary genus are permitted. Boundary curves move on their labelled tori; isotopies start at the identity. There is no extra quotient by torus twists.

The total oriented linking class is the single class $`\Phi`$. In coherently referenced actual meridian–preferred-longitude coordinates,

```math
\Phi(\mu_i)=\epsilon_i,\qquad
\Phi(\lambda_i^0)=f(d-\epsilon_i),\qquad
\alpha_i=\epsilon_i\lambda_i^0-f(d-\epsilon_i)\mu_i.
```

Thus the prescribed spanning slope includes the linking correction. Equivalently, if $`h_i=\lambda_i^0+f\mu_i`$, then $`\alpha_i=\epsilon_i h_i-fd\mu_i`$. For $`f=0`$ these are the signed longitudes.

$`X(L)`$ is the flag complex with edges given by class-minimum cyclic-cover width one of **whole open complements**, using this one $`\Phi`$-cover. The complements are connected and lift homeomorphically, by the actual-meridian argument of [Lemma 4.1](comparison.md), which uses every actual torus once and applies for any $`n`$. A finite set of vertices is a simplex of $`Y(L)=IS(L)`$ precisely when it has simultaneously disjoint whole representatives. $`MS(L)`$ is the taut cyclic subcomplex with the Przytycki–Schultens convention, not a second geometric flag completion. All realizations have the weak simplicial/CW topology.

Let $`\mathcal C`$ be the smallest class containing nontrivial two-bridge and torus knots, including mirrors, and closed under finite connected sums and $`(p,q)`$ cabling with $`p\ge2`$, $`q\ne0`$, $`\gcd(p,q)=1`$. Only finite constructions are allowed; the cable curve is $`p\lambda+q\mu`$.

## Main theorem

For each of the following ranges, the full cyclic complex and the original geometric complex strongly deformation retract onto the same taut cyclic complex:

1. $`K`$ is any nontrivial two-bridge knot, with **any integer framing, any positive number of parallels and any orientations**.
2. $`K\in\mathcal C`$, with **zero framing**, any positive number and any orientations.
3. $`K`$ is any nontrivial **fibred knot**, with **zero framing** and **nonzero orientation sum $`d`$**.

```math
X(L)\subseteq Y(L),\qquad
|Y(L)|\searrow |X(L)|\searrow |MS(L)|,\qquad
|X(L)|\simeq |Y(L)|\simeq *.
```

Both arrows are strong deformation retractions, and their concatenation fixes $`MS(L)`$ pointwise. In range 1, if $`fd\ne0`$, the stronger equality $`X(L)=Y(L)=MS(L)`$ holds. It need not be a point: the precise point criterion is [the framed theorem, Theorem B](framed-clusters.md). In the balanced zero-framed range, $`MS(L)`$ is the pure pattern-annular cyclic subcomplex. At balanced nonzero framing for a two-bridge torus companion, annuli at the regular-fibre framing can also use the companion.

**Proof and dependency map.** [Zero-framed clusters, Theorem A](zero-framed-clusters.md) proves range 1 with $`f=0`$: a circular envelope for one-boundary pieces and an ordinary rooted path-chamber closure for nonparallel multi-boundary systems. Its §9 specifies both the order and heights of stationary annular events. [Arbitrary framings, Theorem A](framed-clusters.md) proves the rest of range 1, with the corrected peripheral class and transverse return coordinate. [Recursive and fibred companions, Theorems A–B](recursive-and-fibred.md) proves ranges 2–3. Its §§3–7 establish actual whole-system reflection closure under sums and cables; §10 directly compactly lifts every component of a nonzero-class disjoint system and reads only its boundary count and genus, so no isotopy is descended from a cover. Each proof identifies its endpoint exactly as $`MS(L)`$ before applying [PS, Theorem 1.1, p.1490].

For every range, non-splitness follows from sphere cutting across incompressible tori (or the knot case for $`n=1`$). The proofs check the full vertex conventions, linking class and spanning boundary slopes. Hence the fixed public [CW, Part 7, Theorem D](../sources/bibliography.md#cw--component-wall-comparison), commit `f6f44253f2ed539a74bf4cfdc99fed299e386546`, gives the first arrow, without a tautness or graph-manifold hypothesis. Let $`R_D,H_D`$ be its retraction and strong deformation, and $`H_X`$ the second deformation. With $`\iota:|X|\hookrightarrow|Y|`$, set

```math
H_Y(y,t)=\begin{cases}
H_D(y,2t),&0\le t\le\tfrac12,\\ 
\iota H_X(R_D(y),2t-1),&\tfrac12\le t\le1.
\end{cases}
```

Both formulas equal $`\iota R_D(y)`$ at the midpoint. The pasting lemma gives continuity and every point of $`MS(L)`$ is fixed throughout. PS contracts that endpoint. This proves the theorem.

**Scope.** General Montesinos/arborescent companions, the balanced branch for arbitrary fibred companions outside range 2, and nonzero framings of recursive companions outside range 1 are not covered. The same nonzero-framing limitation applies to arbitrary fibred companions outside range 1. No arbitrary-link contractibility result is asserted. The explicit Farey, height and disk classifications below concern the two-opposite-parallel specialization of $`X`$, not the simplices of all these larger complexes.

## Detailed structure for two oppositely oriented zero-framed parallels

[Contents](../README.md) · [Proof map](main-theorem.md) · [Sources](../sources/bibliography.md)

Read the proof in the following order. The general geometric foundations are [essential assemblies](assemblies.md), [whole-complement comparison](comparison.md), [carrier purity](carriers.md), and the [all-even cone](even-cone.md). The [two-terminal obstruction](assembly-obstruction.md), Theorem 13.2, excludes every larger-boundary companion component from a legal oriented odd-carrier assembly. [Bounded parameters](bounded-parameters.md) and [general boundary returns](boundary-returns.md) supply the required isotopy interfaces. [Rooted band heights](band-heights.md), Lemma 12.1 and Theorem 12.2, then classify every actual vertex and edge. Finally [finite contraction](finite-contraction.md), Theorem 12.3, treats each odd-band signature. This proves the cyclic Theorem 12.4. The additional geometric Corollary 12.5 uses [§19](geometric-comparison.md), which checks every hypothesis of the separately cited component-wall comparison [CW, Part 7, Theorem D].

The one-block models are proved separately in [ordered systems](ordered-systems.md), [global vertices](odd-vertices.md), [integer edges](odd-edges.md), [trees of disks](one-odd-disks.md) and [two-odd trees](two-odd-trees.md). They are more explicit structures inside the universal result, not assumptions on its scope. The original [pure stacks](odd-normal-forms.md), [returns](odd-returns.md), and [marked Farey tree](odd-trees.md) prove the (P) specialization without relying on the general contraction.

**No cross-carrier edges.** Every odd-carrier vertex is connected by Theorem 13.2. A hypothetical cross-carrier edge therefore has disjoint representatives by Lemma 4.3. Essentialise their entire union by Lemma 3.3 and verticalise by Lemma 3.4. Proposition 3.8 makes each carrier intrinsic. The mixed essential companion union contradicts Proposition 2.2. This argument applies without (P). Different odd-band signatures on one carrier have no non-root edge by §12.4 of [the height classification](band-heights.md).


### 12.9. The all-two-bridge conclusion

**Theorem 12.4.** For every nontrivial two-bridge companion C, the entire complex X of its two oppositely oriented zero-framed parallels is contractible.

**Proof.** The vertices and edges are completely covered by the [geometric foundations](assemblies.md), [whole-block comparison](comparison.md) and [all-even cone](even-cone.md) and Theorem 12.2. The all-even part is a cone. Distinct carriers have no non-root cross edge by purity, and distinct signatures in one odd carrier have no non-root cross edge by §12.4. There are finitely many carriers and signatures, each signature occurring among finitely many two-sheeted types. Flag completion therefore expresses X as their pointed union at a, together with the all-even cone.

For any finite subcomplex extend each odd-signature portion by Theorem 12.3, and extend its all-even portion by the finite cone with a. The union is a finite contractible carrier, with all contractions fixing a. Thus X is connected and weakly contractible; its weak simplicial realization is a CW complex and is contractible by Whitehead.

This includes the two-large-coefficient disk and tree descriptions in §§9 and 11, all one-odd carriers with arbitrarily many large even coefficients, and carriers with several odd coefficients. No larger-boundary piece is presumed absent without proof: its exclusion was Theorem 13.2, and the full assembly criterion and signatures were derived from the explicit rooted matching. ∎



## 12.10. The original geometric complex

**Corollary 12.5.** For every nontrivial two-bridge companion, on the full vertex set of Definition 1.1,

```math
X(L)\subseteq Y(L)=IS(L),\qquad
|Y(L)|\searrow |X(L)|,\qquad
|Y(L)|\simeq *.
```

The arrow denotes a strong deformation retraction in the weak simplicial (CW) topology.

**Proof.** Lemma 19.1 proves non-splitness and checks the full all-incompressible conventions. Proposition 19.2 applies [CW, Part 7, Theorem D] to obtain a retraction $`R:|Y(L)|\to|X(L)|`$ and a strong deformation $`H_D`$ from the identity to the inclusion followed by $`R`$. Theorem 12.4 gives a contraction $`h_X`$ of $`|X(L)|`$. Concatenate $`H_D`$ with $`h_X\circ(R\times\mathrm{id})`$, as written in §19.4, to contract $`|Y(L)|`$. No equality of the two complexes or extension of the cyclic sector decomposition is used. ∎

## The explicit structure under (P)

**Proof of Corollary 1.3 (the (P) structure).** Sections 5–7 cover and distinguish all vertices. Proposition 5.2 gives $`\mathcal B_E=a*Y_E`$. Proposition 8.2 gives every edge in an odd sector; Lemma 8.3 proves that sector is a rooted tree. The no-cross-carrier argument above excludes all cross edges away from the root. Since the complex is flag, each simplex lies either in the all-even cone or in one of the odd trees. A tree has no three-vertex clique, so its flag completion contributes no higher simplex. This proves equality of the entire simplicial complexes, not merely their vertex sets or finite subgraphs.

Use weak simplicial, equivalently CW, topology on the realizations. Give every tree edge unit length and contract a point toward its root along its unique finite root path, multiplying its distance from the root by $`1-t`$. On each closed edge times the time interval the image lies in a finite rooted subtree, where this is continuous. The weak-topology product criterion with the locally finite CW interval gives continuity on the whole tree times the interval. Perform these contractions on all odd trees while fixing $`\mathcal B_E`$. They agree at their only common point $`a`$ and are continuous by the same cellwise criterion.

Then contract the cone by barycentric interpolation to its apex. For a point in a base simplex $`\sigma`$, the path lies in $`a*\sigma`$ and is $`(1-t)x+ta`$. Extend this stage by keeping the already collapsed tree points at $`a`$. The two stages fix $`a`$ throughout and give a contraction of all of $`X(L)`$. The number of carriers is finite by Lemma 2.1; no finiteness of vertex sets or genus bound was used. ∎

If $`O(C)`$ is empty the entire result is the all-even cone. If its base happens to be a point, the cone is one edge and the entire complex is a tree with that additional leaf. Neither special case is imposed in the general theorem.
