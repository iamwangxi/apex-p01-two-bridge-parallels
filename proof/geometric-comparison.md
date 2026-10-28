# 19. From the cyclic complex to the original geometric complex

[Contents](../README.md) · [Objects](objects.md) · [Corollary 12.5](main-theorem.md) · [Sources](../sources/bibliography.md)

This page checks the two-opposite-parallel specialization of [Definition 1.1](objects.md). The [main theorem](main-theorem.md) and the three cluster proof pages check the wider ranges, including the corrected framed slopes and the nonzero-orientation branch. The balanced-kernel argument in §19.2 is used only in this specialization.

## 19.1. The fixed comparison theorem

We use **[CW, Part 7, Theorem D]**, the component-wall comparison in the public repository `iamwangxi/apex-p01-seifert-fibred-links`, commit `f6f44253f2ed539a74bf4cfdc99fed299e386546`:

- [Statement: `proof/part7.md`, Part 7, page 1, §1](https://github.com/iamwangxi/apex-p01-seifert-fibred-links/blob/f6f44253f2ed539a74bf4cfdc99fed299e386546/proof/part7.md#1-objects-and-statements).
- [Proof and source ranges: `proof/part7-2.md`, Part 7, page 2, §9](https://github.com/iamwangxi/apex-p01-seifert-fibred-links/blob/f6f44253f2ed539a74bf4cfdc99fed299e386546/proof/part7-2.md#9-a-component-wall-retraction-independent-of-jsj-slices).

**Cited comparison theorem.** For every nonempty oriented non-split link in the three-sphere, on the full reduced all-incompressible spanning vertex set, the identity on vertices gives a simplicial inclusion of the cyclic-distance flag complex into the original geometric disjointness complex. Its realization is a strong deformation retract. Neither graph-manifold structure nor tautness is a hypothesis.

This is a citation of the fixed public theorem, rather than a claimed self-contained proof of it. The cited result compares complexes; its statement alone gives no contraction of either one. It is distinct from the competition paper's Theorem D, whose linking-indecomposability hypothesis fails here.

## 19.2. Verification of every hypothesis and convention

**Lemma 19.1.** For the links of Definition 1.1, all hypotheses of [CW, Part 7, Theorem D] hold, and both of its complexes agree with the objects defined here.

**Proof.** The link is the nonempty oriented two-component link in the three-sphere constructed as two zero-framed parallels of a nontrivial knot. It is **non-split**, even though its linking number is zero. Indeed $`Q=E(C)`$ is irreducible with incompressible torus boundary, and $`P=S^1\times B`$ is irreducible with all three boundary tori incompressible. Gluing along their common incompressible torus gives an irreducible exterior with incompressible actual boundary by the disk/sphere cutting argument of Lemma 3.1. A splitting sphere would be a sphere in that exterior with link components on both sides, and would not bound a ball in the exterior, contradicting irreducibility. This uses nontriviality of the companion, not hyperbolicity; two-bridge torus knots are included.

The full vertex set is identical: compact properly embedded **oriented**, componentwise incompressible spanning systems, no closed components, exactly one prescribed oriented boundary curve on each labelled actual torus, with no connectedness, genus, norm or tautness restriction. Incompressibility is componentwise in all these conventions. Boundaries may slide on their labelled tori during ambient isotopies beginning at the identity; no fixed-boundary marking, peripheral twist quotient, or additional component identification is introduced. The word “reduced” means only this convention and adds no minimality requirement. Sakuma's exterior-isotopy convention [S, p.863] matches it: an identity isotopy cannot permute the discrete boundary tori, and its boundary motion extends through the deleted link collars.

The covering class also agrees. Its value on the positively oriented meridian of each **oriented** actual link component is one. The notation $`+\lambda,-\lambda`$ uses a common companion-longitude coordinate; reversing the second component also reverses its oriented positive meridian. It therefore does not change the agreement with [CW]'s $`\Phi(\mu_i)=1`$. Cancellation gives $`\phi|_{\pi_1(Q)}=0`$, as in §1. It does not give independent deck constants on different companion pieces.

Every spanning component has actual boundary. The actual-meridian argument in Lemma 4.1 shows that the whole open complement is connected and its lifts map homeomorphically onto it. Thus the complete-block minimum-width definition of $`X`$, including distinct pairs of minimum width one and flag completion, agrees with [CW] and [B, Definition 10.1]. A simplex of $`Y=IS(L)`$ means simultaneously disjoint **whole** representatives, as in [S, pp.871–872] and [CW]; no flagness is inserted into its definition. The base symbol $`Y_E`$ in the cyclic decomposition denotes a different, explicitly defined subcomplex of $`X`$.

For the auxiliary essential-surface interface, Lemma 3.1 gives a Haken, boundary-incompressible exterior and boundary-incompressible spanning components. A disk component is excluded by the injected actual longitude. A boundary-parallel annulus would use two boundary curves on one actual torus, which the spanning convention forbids. The global spanning-fibre exception to the product argument cannot occur: $`\pi_1(T)\cong\mathbb Z^2`$ injects into $`\ker\phi`$, whereas the kernel of a spanning fibration would be the free group of a compact surface with boundary. No graph-manifold assumption or coherence of companion traces is needed. ∎

## 19.3. Exact Sakuma and Banks inputs

These are the printed inputs of the cited theorem, not unproved extra hypotheses on the two-bridge family.

| Source | Exact input and range | Application here |
|---|---|---|
| Sakuma 1994, p.863 | Seifert surfaces are oriented and have no closed components; disconnected surfaces are permitted; equivalence is ordinary exterior isotopy | Exactly the full vertex set in Lemma 19.1 |
| Sakuma 1994, pp.871–872 | Geometric simplices have simultaneous whole disjoint representatives | Exactly $`Y(L)=IS(L)`$ |
| Sakuma 1994, Proposition 4.9(1), p.883 | For every non-split link, pairwise geometric edges give a simultaneous simplex, explicitly also for $`IS(L)`$ | Converts a cyclic clique, after the width-one argument, to an actual geometric simplex |
| Sakuma 1994, Proposition 4.9(2), p.883 | The isotopy type of the **unlabelled** disjoint union is determined by its simplex, explicitly also for $`IS(L)`$ | Gives the representative independence used in [CW, §9.1–§9.2], with parallel packets merged before weights are assigned |
| Banks, arXiv:1109.0965v1, Definition 2.1 and Proposition 2.4, p.2; Definition 10.1, p.22 | No closed components; the cyclic convention uses lifts of the whole open complement | Matches $`X`$; componentwise deck indexing is not permitted |
| Banks, Proposition 4.2(1), p.5; Remark 4.4, p.6 | Incompressible, boundary-incompressible product regions, including the stated coincidences | Ambient and surface hypotheses hold by Lemma 3.1; the global fibre exception is excluded above |
| Banks, Proposition 4.10, p.7, **explicitly extended in §10, p.22** | Almost-transverse simplified representatives attain minimum width for all incompressible surfaces; §10 also extends Lemma 4.9 | Permits non-taut vertices throughout the component-wall comparison |

Sakuma's special-arborescent contractibility theorem concerns minimal-genus $`MS`$ and does not apply to this oriented link, as explained in [scope](scope.md). His Proposition 4.9 is separately stated for **every non-split link**, includes $`IS`$ in both clauses, and is applicable here. Unlabelled-union uniqueness is used exactly as stated; no stronger labelled-union theorem is assumed. The packet argument needed for weighted representative independence belongs to the cited proof [CW, §9.1]. Likewise the all-incompressible minimum statement is the explicit Banks §10 input, not an extrapolation from the taut version of [PS, Proposition 3.2].

For orientation on the dependency: [CW, §9.2] averages generic phases of weighted whole-component wall maps; each generic level consists of whole incompressible components and uses every actual torus once. Section 9.3 proves the inclusion and exact recovery on cyclic simplices. Section 9.4 gives a face-compatible strong deformation, with the image of each closed simplex cylinder in a finite subcomplex. Those arguments and their topological continuity assertion are part of the cited theorem, not numerical claims of the scripts here.

## 19.4. Application and contraction

**Proposition 19.2.** For the links of Definition 1.1,

```math
X(L)\subseteq Y(L)=IS(L),\qquad
R:|Y(L)|\longrightarrow |X(L)|,
```

and there is a continuous strong deformation $`H_D:|Y(L)|\times[0,1]\to|Y(L)|`$ such that

```math
H_D(y,0)=y,\qquad H_D(y,1)=\iota R(y),\qquad
R\iota=\mathrm{id}_{|X(L)|},\qquad
H_D(\iota x,t)=\iota x.
```

Here $`\iota`$ is the inclusion. **Proof.** Apply [CW, Part 7, Theorem D] using Lemma 19.1 and the source ranges in §19.3. ∎

Theorem 12.4 gives a contraction $`h_X:|X(L)|\times[0,1]\to|X(L)|`$ to $`a`$. A contraction of the original geometric realization is

```math
K(y,t)=
\begin{cases}
H_D(y,2t),&0\le t\le\tfrac12,\\ 
\iota h_X(R(y),2t-1),&\tfrac12\le t\le1.
\end{cases}
```

The formulas agree at $`t=1/2`$ because both equal $`\iota R(y)`$. The pasting lemma proves continuity in the ordinary product topology, and $`K(y,0)=y`$, $`K(y,1)=a`$. All realizations use the weak simplicial, equivalently CW, topology, the topology of both cited results. Thus Corollary 12.5 proves contractibility of the entire $`IS(L)`$, not just of a vertex subset or finite collection of genera.

The explicit Farey-tree sectors, triangulated disk sectors and absence of cross edges in the cyclic proof describe $`X(L)`$. The comparison is a strong deformation retraction and does not assert that $`X(L)=Y(L)`$ or that the same sector decomposition lists every geometric simplex. No new geometric enumeration or proof-assistant certification is claimed.
