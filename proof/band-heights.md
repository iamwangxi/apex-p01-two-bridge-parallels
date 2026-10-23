# 12. Rooted band heights and complete general coordinates

[Contents](../README.md) · [Proof map](main-theorem.md) · [Sources](../sources/bibliography.md)

### 12.1. The local sheet matching

Choose an odd band as root o. Regard the plumbed one-sheeted surface as band loops joined by the tree of plumbing squares. Number each normal stack by 0,...,N-1, using the induced plumbing order. At a square with n inner and N-n outer rectangles, the ordered matching is

```math
P_n(i)=\begin{cases}
n-1-i,&0\leq i\lt n,\\ 
N+n-1-i,&n\leq i\lt N.
\end{cases}
\qquad P_n(i)=n-1-i\pmod N.
```

Here each of the two intervals is reversed. This is obtained by listing the parallel rectangle ends on the two sides of the complementary squares of HT Fig.3. A full inner or outer stack is the full reversal. Normal frames at consecutive bands are chosen in that plumbing order. A different root labelling conjugates all based monodromies together; we retain the displayed chart convention. The connecting plumbing tree has no frame-consistency cycle. The band core loop itself has identity normal monodromy for an even coefficient and full reversal q(i)=N-1-i for an odd coefficient. Full twists do not alter these permutations. These are exactly the local normal-stack identifications behind HT Figs.26 and 30.

One may obtain the same rule by taking the N normal lifts of each twisted band and gluing the lifted square disks. The n inner disks are one consecutive stack and the other N-n disks are its complementary stack; opposite rectangle ends match in reverse order in each stack. Collapsing connecting disk corridors gives the plumbing tree, while the band core loops retain their parity monodromy. Thus the graph permutations describe the actual band-and-square surface of HT p.227 and its abstract cover on p.244; they are not an arbitrary free-group representation chosen to fit the desired components.

This is an explicit gluing rule, not an assumption that partial squares preserve level numbers. In particular P_mP_n is translation by m-n. Two partial squares therefore generally couple, which is why independent raw block profiles are insufficient.

Write n_e for the HT parameter at a plumbing edge. Define integer band heights on **all** bands by

```math
H_o=0,\qquad H_w=n_e-H_v
```

when edge e is traversed from a band v nearer the root to its child w. Equivalently n_e=H_v+H_w.

These H_v are finite normal-sheet coordinates of the carried surface, not deck heights in the linking-number cover. The homomorphism φ remains zero on Q. All cyclic-edge claims still use the whole-block arguments of the [geometric foundations](assemblies.md), [whole-block comparison](comparison.md) and [all-even cone](even-cone.md).

Along a path of length d, composition of the P_n has the form

```math
M_v(i)=(-1)^d i+A_v,
\qquad A_v=H_v-\frac{1-(-1)^d}{2}.
```

This follows by induction from A_w=n_e-1-A_v. An odd band's based loop consequently acts at the root by

```math
M_v^{-1}qM_v(i)=-i-1-2(-1)^dH_v\pmod N.
```

Thus the transported fold constants, previously denoted c_ν, are explicit integer functions of the parameters. The component divisor of [§13](assembly-obstruction.md) is

```math
d_N=\gcd\bigl(N,\{2H_v:v\text{ an odd band}\}\bigr).
```

The root contributes zero to this gcd. This reproduces HT's single fold for one odd coefficient and its independent relative folds for several odd coefficients.

### 12.2. Isotopy parameters and their finite domain

Let J be the set of large bands, those with |b_v|>2. It contains every odd band and the root. A move at a non-root band v with b_v=±2 changes H_v by one while fixing every other band height, because it adds one to both incident plumbing parameters (or the single one at an endpoint). The root is odd and has no such move.

It follows from the complete bounded move relation, or from the chip-transfer normalization of [§14](bounded-parameters.md), that a carried system is classified by

```math
N,\qquad \mathbf H=(H_v)_{v\in J},\qquad H_o=0.
```

There are no missing discrete parameters. To give an explicit finite feasibility test, take consecutive large indices v<w in the original band line, let L=w-v, and require

```math
-N\lfloor L/2\rfloor
\ \leq\ H_w-(-1)^L H_v
\ \leq\ N\lceil L/2\rceil.
```

These inequalities and H_o=0 define the integer domain $`\mathcal D_N`$. They are necessary by the alternating sum along the L plumbing edges. They are sufficient because every integer in that alternating-sum range is realized by bounded edge parameters; the independent intervening blocks and outside blocks can then be filled. This is the same bounded-composition proof as Lemma 14.1. Denote the resulting linear bounds also by $`\mathcal D_N`$ when real heights are permitted.

For a band at distance d_v from o, every feasible height has

```math
-N\lfloor d_v/2\rfloor\leq H_v
\leq N\lceil d_v/2\rceil.
```

In particular all the domains used here are finite integer sets. Reading a block from the root, its former alternating block sum is an affine signed difference of its two endpoint heights. Passing from block sums to these heights is an integral triangular change of coordinates, not an extra isotopy identification.

### 12.3. Component types from the same heights

For a root-sheet orbit O define its signed interval count

```math
D_{O,N}(h)=|O|\left\lfloor\frac hN\right\rfloor
+\#\{i\in O:0\leq i\lt h\bmod N\}.
```

The remainder is always in {0,...,N-1}; negative h uses the indicated floor. Every component orbit is invariant under root reversal q, so

```math
D_{O,N}(-h)=-D_{O,N}(h),\qquad
D_{O,N}(h+N)=D_{O,N}(h)+|O|.
```

**Lemma 12.1 (restricted weights).** The component on orbit O has band heights D_(O,N)(H_v). Its plumbing parameter on e=vw is

```math
n_e^O=D_{O,N}(H_v)+D_{O,N}(H_w).
```

**Proof.** The root orbit O is fixed by q. At band v, the image of its levels under M_v is therefore the cyclic translate O+H_v: when the affine sign is negative, the extra -1 is exactly q. The inner rectangles at the next square select the interval [0,n_e). Pulling it back gives the cyclic interval [-H_v,H_w), since n_e=H_v+H_w. Its count is D_(O,N)(H_w)-D_(O,N)(-H_v), which is the formula. These are actual selected rectangles in Fig.3, so the restricted weights specify the component on the same carrier. ∎

The component orbits are explicitly the residue classes modulo d_N paired by t↦-1-t, as in §13. Thus this lemma gives a finite arithmetic component partition, the full restricted HT isotopy type of each component, its genus and its orientability, for **every** parameter tuple. Large component heights classify it by the same bounded move theorem. The signs of orientable components can be carried through this labelled normal form. Return stabilizers for noncontributing larger-boundary systems are not needed for X.

For an admissible global system N=2k, every orbit is a pair O_i={i,2k-1-i}. Set

```math
C_{k,h}(i)=2\left\lfloor\frac h{2k}\right\rfloor
+\mathbf1_{\{i\lt h\bmod 2k\}}
+\mathbf1_{\{2k-1-i\lt h\bmod 2k\}},
\quad0\leq i\lt k.
```

Then its i-th component has large height vector (C_(k,H_v)(i))_(v∈J). The formula is valid for negative heights. It is increasing in h, odd in h, has C_(k,h+2k)=C_(k,h)+2, and its sum over i is h.

These are cumulative-height profiles. They include the coupled transports that a raw product of block profiles misses. For instance, with an odd root and two successive plumbing counts n_1=1,n_2=2 at N=4, the heights are H_1=H_2=1. The two component raw tuples are (1,2) and (0,0); applying two independent raw block profiles would instead give the wrong labels.

**Joint order and coexistence.** The paired indices i=0,...,k-1 are the simultaneous normal order at the root. The vector profile just given is the entire labelled component word. A specified list of two-sheeted types can coexist in that order if and only if its sum of height vectors is a feasible H in D_(2k), has d_(2k)=2k, and its ordered list equals this profile of the sum. This is a finite exact criterion, not a pairwise guess. Unordered coexistence compares multisets and records the order supplied by the profile. Component orientations are independent before pattern matching.

**Naturality under deletion.** Retain any subset I of paired indices. Its total heights are

```math
H_v^I=\sum_{i\in I}C_{k,H_v}(i).
```

It is a genuine carried subsystem by the restricted-weight lemma. More explicitly, an inner interval intersects an ordered retained stack in an initial interval. Restricting the two block reversals therefore gives exactly P_(n_e^I) on the compressed stack. The restricted rectangles and bands are the specified HT subsystem, not just separately isotopic component types.

On each height coordinate the profile has at most two adjacent values, with the odd value at the outer end; a subsequence has exactly the profile of its sum after compressing the ordered indices. Normal straightening of the actual restricted diagram and subsequent bounded moves can fix a section of the odd root band: every movable band has coefficient ±2 and is distinct from that root. The small order-preserving radial compression of the retained root levels preserves both end gaps and has no full meridional circuit. Lemma 16.1 excludes any alternative return permutation or winding. This proves simultaneous subsystem naturality for several blocks, rather than assuming it for the original raw block coordinates. The cap projection is consequently natural on actual disjoint unions, including signature sectors that have no one-sided core.

### 12.4. Exactly which systems assemble

Combining the fold constants with Theorem 13.2 gives a particularly simple test:

```math
N=2k,\qquad \mathbf H\in\mathcal D_{2k},\qquad
H_v\in k\mathbb Z\quad\text{for every odd band }v.
```

These conditions are **necessary and sufficient** for the companion system to be a collection of two-boundary pieces. With any legal single-surface anchor a and winding t it then assembles to a spanning vertex. Necessity is d_N=N; sufficiency is that all fold orbits are pairs, each pair is orientable, and the q/p path orients the pieces and annuli compatibly. No larger-boundary component is deleted.

Define the signature

```math
\mathbf z=(H_v/k)_{v\text{ odd},\ v\ne o}.
```

At an odd band H_v=kz_v, every paired count is C_(k,kz_v)(i)=z_v. Hence all two-boundary components in one global vertex have the same odd-band signature. If two such global vertices are disjoint, their companion union still has only two-boundary components. Its common odd-band signature must restrict to the signature of each side. Thus vertices of different signatures have no non-root edge.

There are finitely many possible signatures: every one is the signature of one two-sheeted component, and $`\mathcal D_2`$ is finite. Conversely a two-sheeted type of signature z has parallel stacks of every size and gives vertices above every marked tree vertex. Each signature sector therefore has the same marked base tree, but generally many height states over a base vertex.

**Theorem 12.2 (complete general vertex and edge criteria).** On any odd zero carrier, all non-root global vertices have unique coordinates

```math
F_\beta(k,\mathbf H,a,t),\qquad
\mathbf H\in\mathcal D_{2k},\quad H_o=0,\quad
H_v\in k\mathbb Z\ (b_v\text{ odd}),
\quad\gcd(2a+1,2k)=1.
```

The ranges of a,t are as in Theorem 17.1. Genus is k(s-1), and minimum T intersection is 2k. Equality is equality of all the data and the carrier label.

The proof of coverage and equality is Theorem 17.1 with the complete height invariant in place of U, using the root-natural subsystem model above. For two vertices on the same carrier, the root edge rule is k=1. For a non-root pair, different signatures or different winding integers exclude an edge. For equal signatures and t, let K=k+k' and total heights H+H'. Enumerate the legal joint anchors u of §18. Restrict each large height by

```math
H_v^V=\sum_{i\in I(V)}C_{K,H_v+H_v'}(i).
```

The pair is adjacent exactly when one of the two path assignments gives the two specified height vectors and marked anchors. This is the same finite integer test as Theorem 18.2, now including the coupled blocks. The sum state is feasible and has the common signature. Necessity uses joint normalization of the whole disjoint union; sufficiency uses that actual joint carried system and the two assigned pattern paths. Both complete surfaces are connected, so the disjoint construction realizes cyclic width one.

The all-even part and cross-carrier exclusions remain those of the [geometric foundations](assemblies.md), [whole-block comparison](comparison.md) and [all-even cone](even-cone.md) and the [global no-cross-edge argument](main-theorem.md). Hence this theorem specifies every actual vertex, edge and, by flag completion, every simplex for arbitrary two-bridge companions.
