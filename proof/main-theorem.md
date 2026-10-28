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

**(1)** $`K\in\mathcal C`$, with **every integer framing, every positive number of parallels and every orientation assignment**.

**(2)** $`K`$ is any nontrivial **fibred knot**, with **every integer framing** and **nonzero orientation sum $`d`$**.

**(3)** $`K`$ is any nontrivial **fibred knot**, with **two oppositely oriented parallels and every integer framing**.

```math
X(L)\subseteq Y(L),\qquad
|Y(L)|\searrow |X(L)|\searrow |MS(L)|,\qquad
|X(L)|\simeq |Y(L)|\simeq *.
```

Both arrows are strong deformation retractions, and their concatenation fixes $`MS(L)`$ pointwise. For ranges 1–2, when $`fd\ne0`$, every vertex is connected and taut, and

```math
X(L)=Y(L)=MS(L),\qquad
\chi(S)=|d|(1-2g(K))-|fd|(n-1).
```

This equality need not mean a point. In balanced zero-framed ranges the endpoint is the pure pattern-annular cyclic subcomplex $`\mathcal A_X`$. In the recursive balanced branch at a top torus framing $`f=ab`$ or top cable framing $`f=pq`$, all vertices are annular and $`X=MS(L)`$; taut annuli can use the companion. For the zero-framed fibred double the endpoint is the single standard annulus vertex.

**Proof and dependency map.** [Framed recursive parallels and fibred doubles, Theorems A–B and Corollary D](framed-recursive-and-fibred.md) proves all three ranges. Its §§3–5 retain actual slopes, whole-system reflection structure and ordinary hereditary roots at every finite slope, including horizontal cables merging nonparallel child pieces. Its §§6–9 establish the fibred dichotomy and the connected-sector compression barrier. The local multi-torus analytic exchange inputs are taken from the official competition paper [C]; its general-link conjecture is not assumed.

The underlying [zero-framed cluster proof](zero-framed-clusters.md), [integer-framed two-bridge proof](framed-clusters.md) and [zero-framed recursive/nonbalanced fibred proof](recursive-and-fibred.md) supply the stated geometric interfaces. Their stationary-event order/heights and whole-system compact-lift repair are incorporated. Topological type is read from compact lifts; no upstairs isotopy is descended.

For every range, non-splitness and actual boundary injections are checked before applying the fixed public [CW, Part 7, Theorem D](../sources/bibliography.md#cw--component-wall-comparison), commit `f6f44253f2ed539a74bf4cfdc99fed299e386546`. It gives the first arrow on the full, possibly disconnected vertex set, without a tautness or graph-manifold hypothesis. Let $`R_D,H_D`$ be its endpoint and strong deformation and let $`H_X`$ be the second deformation. With $`\iota:|X|\hookrightarrow|Y|`$, set

```math
H_Y(y,t)=\begin{cases}
H_D(y,2t),&0\le t\le\tfrac12,\\ 
\iota H_X(R_D(y),2t-1),&\tfrac12\le t\le1.
\end{cases}
```

The formulas agree at $`\iota R_D(y)`$, are continuous in the weak/CW topology and fix $`MS(L)`$ throughout. The endpoint is identified as taut before [PS, Theorem 1.1] is applied to contract it.

## Exact remaining balanced fibred problem

For any nontrivial fibred $`K`$, with $`f=d=0`$ and arbitrary $`n`$, let $`X_{\mathrm{sep}}`$ be the induced cyclic subcomplex whose efficient companion cut is empty or consists only of separating pieces. Let $`Y_{\mathrm{sep}}`$ have those vertices and geometric simplices. [Theorem C](framed-recursive-and-fibred.md) proves

```math
MS(L)=\mathcal A_X,\qquad
|X(L)|\searrow|X_{\mathrm{sep}}|,\qquad
|Y_{\mathrm{sep}}|\searrow|X_{\mathrm{sep}}|.
```

The first retraction fixes $`X_{\mathrm{sep}}`$ pointwise. Thus the full balanced problem is equivalent to contractibility of that complete separating subcomplex. Theorem C does not assert its contractibility for arbitrary fibred knots with four or more actual components. In that range separating vertices can be disconnected and distinct vertices can share a whole actual-bearing component; the double's automatic barrier fails. [Section 7](framed-recursive-and-fibred.md) gives explicit sufficient hereditary chamber/root conditions, rather than assuming that a chamber tree is a path.

**Scope.** General Montesinos/arborescent companions outside the proved fibred or recursive ranges, and arbitrary balanced fibred clusters with at least four components without the additional stated hypotheses, remain outside the contractibility theorem. Nonzero-framed balanced doubles of any nontrivial companion also follow directly from [C, Theorem D] and the comparison/cofibration argument in §9. No arbitrary-link contractibility theorem is asserted. The explicit Farey, height and disk classifications below concern two oppositely oriented zero-framed parallels, not all larger-cluster simplices.

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
