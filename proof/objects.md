# 1. Objects, conventions and the theorem

[Contents](../README.md) · [Sources](../sources/bibliography.md)

This page fixes the **two oppositely oriented, zero-framed parallels** used in the detailed carrier classification. The general objects, framed spanning slopes and main theorem for arbitrary clusters are on [the main theorem page](main-theorem.md). The two-terminal obstruction below is used only in this specialization.

Let $`C=K_{p/q}`$ be a nontrivial two-bridge knot, with $`0\lt p/q\lt1`$, $`q`$ odd and $`\gcd(p,q)=1`$. Let $`L`$ be its two oppositely oriented zero-framed parallels. Write

```math
M=E(L)=Q\cup_T P,\qquad Q=E(C),\qquad P=S^1_\lambda\times B.
```

Here $`B`$ is a pair of pants with outer boundary $`b_0`$ and labelled inner boundaries $`b_+,b_-`$. On $`T=\partial Q=S^1_\lambda\times b_0`$ use the preferred longitude $`\lambda`$ and meridian $`\mu`$. The actual boundary tori have prescribed spanning curves with signs $`+\lambda,-\lambda`$. Boundary curves may move on their labelled tori; all ambient isotopies begin at the identity.

**Definition 1.1 (the two complexes).** A vertex of $`X(L)`$ is an ambient-isotopy class of compact, properly embedded, oriented spanning surfaces, componentwise incompressible and without closed components. Disconnected surfaces are allowed. There is no genus or norm restriction. These are the reduced spanning systems used throughout this note; no extra minimal-genus condition is implicit in “reduced.”

Let $`\phi:\pi_1(M)\to\mathbb Z`$ be total oriented linking number and let $`\widetilde M`$ be its infinite cyclic cover, with positive deck transformation $`\tau`$. For representatives $`F,H`$, take one lift $`W`$ of the **whole open complement** $`M\setminus H`$ and write $`U_i=\tau^iU_0`$ for the lifts of the whole open $`F`$ complement. Define

```math
D(F,H)=\max\{i:W\cap U_i\ne\varnothing\}
-\min\{i:W\cap U_i\ne\varnothing\},\qquad
\delta([F],[H])=\min_{F,H}D(F,H).
```

The complements are connected and the lifts map homeomorphically to them, as proved in Lemma 4.1. Distinct vertices form an edge exactly when $`\delta=1`$; $`X(L)`$ is the flag completion of this edge graph. Thus a finite clique is a simplex by definition. The whole-complement convention matters for disconnected surfaces.

This is Banks's all-incompressible cyclic-cover convention [B, Definition 10.1, p.22], with the class minimum computed using [B, Proposition 4.10 and §10]. On the same full vertex set define $`Y(L)=IS(L)`$ by requiring a finite set of distinct classes to have simultaneously disjoint whole representatives. This is the original geometric disjointness complex [S, pp.863, 871–872], not a flag completion in its definition. The symbols $`Y_E`$ below denote the all-even base of $`X(L)`$, not the whole complex $`Y(L)`$.

The restriction of $`\phi`$ to $`\pi_1(Q)`$ is zero: the companion meridian links the oppositely oriented parallels with cancelling signs, and $`H_1(Q)`$ is meridionally generated. Let $`A`$ be the vertical annulus over an inner-to-inner seam in $`B`$ and put $`a=[A]`$. Such seams have one class with endpoints free on the two labelled inner boundaries.

Use the Hatcher–Thurston minus convention

```math
[b_1,\ldots,b_s]=\frac{1}{b_1-\dfrac{1}{b_2-\cdots-\dfrac1{b_s}}},
\qquad p/q=r+[b_1,\ldots,b_s],\qquad \lvert b_i\rvert\ge2.
```

The **carrier** is labelled by the full admissible expansion $`(r,b)`$, rather than by its slope or length. Let $`E`$ denote the unique all-even expansion, put $`\sigma(b)=\sum_i\mathrm{sgn}(b_i)`$, and define

```math
\mathcal Z(C)=\{(r,b):\sigma(b)=\sigma(E)\},\qquad
O(C)=\mathcal Z(C)\setminus\{E\}.
```

By [HT, Proposition 2, p.230] these are exactly the zero-slope carriers. “Odd carrier” below means a non-all-even member of $`\mathcal Z(C)`$.

**Condition (P).** Every non-all-even zero-slope HT expansion has **exactly one** coefficient of absolute value greater than two. There is no restriction on the all-even expansion and no uniqueness requirement on odd zero-slope carriers. An odd coefficient has absolute value at least three, so on each odd carrier satisfying (P) that exceptional coefficient is odd and every other coefficient is $`\pm2`$. If $`O(C)`$ is empty, (P) holds vacuously.

**Theorem 1.2 (two-parallel structure; Theorem 12.4 and Corollary 12.5).** For every nontrivial two-bridge knot, the entire cyclic complex $`X(L)`$ of Definition 1.1 has the decomposition

```math
X(L)=\mathcal B_E\cup_{\{a\}}
\bigcup_{\beta\in O(C)}\ \bigcup_{\mathbf z\in Z_\beta}X_{\beta,\mathbf z},
\qquad \mathcal B_E=a*Y_E.
```

Here the finite set $`Z_\beta`$ consists of the odd-band signatures defined in [§12.4](band-heights.md). Each rooted signature sector is contractible by Theorem 12.3; distinct sectors and the all-even cone meet only at $`a`$ and have no non-root cross edge. Consequently $`X(L)`$ is contractible. In addition $`X(L)\subseteq Y(L)`$ and $`|X(L)|`$ is a strong deformation retract of $`|Y(L)|`$; hence $`Y(L)=IS(L)`$ is contractible as well. The cyclic assertion is Theorem 12.4. The geometric assertion is Corollary 12.5, using the cited component-wall comparison [CW, Part 7, Theorem D] after the hypothesis checks in [§19](geometric-comparison.md). Complete cyclic vertex and edge criteria are Theorem 12.2, and the finite contraction and global proof are in [the proof map](main-theorem.md).

**Corollary 1.3 (the explicit (P) structure).** Under (P),

```math
X(L)=\mathcal B_E\cup_{\{a\}}\bigcup_{\beta\in O(C)}\mathcal T_\beta,
\qquad \mathcal B_E=a*Y_E.
```

Here $`Y_E`$ is the full subcomplex on the non-annular all-even vertices. Each $`\mathcal T_\beta`$ has root $`a=\infty=(1,0)`$, other vertices $`p/k`$ with $`k>0`$, $`p`$ odd and $`\gcd(p,k)=1`$, and edge rule

```math
\lvert pk'-p'k\rvert=1.
```

Each such graph is a tree. Distinct pieces intersect only at $`a`$ and have no cross edges away from $`a`$. Consequently $`X(L)`$ is contractible.

The **base** $`Y_E`$ need not be a point. Its vertices are covered by explicit finite HT data and one winding integer; equality and adjacency have the finite geometric criterion in [§4](comparison.md). A closed integer-only quotient for this base is not asserted. The universal proof is assembled in [Theorem 12.4](main-theorem.md); [§10](infinite-family.md) proves three explicit infinite families, including the (P) family.

**Relation to the target paper.** The official competition version [C], Introduction, printed p.2, leaves general links untreated because the disjointness hypothesis of Lemma 4.9 can fail when distinct vertices share a component class. Its Theorems A and D (printed p.2) prove the knot and linking-indecomposable link cases; its knot surfaces are connected and Theorem D has an additional linking hypothesis forcing connectedness. The zero linking number here fails that hypothesis. The present result handles this family with disconnected vertices by a carrier decomposition and cyclic-width edge analysis, followed by the explicit comparison [CW]. It proves the original geometric-complex extension for these links. Theorem D of [CW] is distinct from the target paper's Theorem D and requires only non-splitness, not linking indecomposability.
