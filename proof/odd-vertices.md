# 17. Global vertices for the one-odd one-block sector

[Contents](../README.md) · [Proof map](main-theorem.md) · [Sources](../sources/bibliography.md)

Fix reference systems of Lemma 15.1, their root sections, and the marked pattern references of [the marked-arc model](odd-trees.md). On N=2k boundary circles the companion pairing is q(i)=-1-i. If the positive reaching endpoint is a, the negative one is a+k and the single-surface pattern reflection is p(i)=2a-i away from the terminals.

The alternating q/p graph has one terminal path and (g-1)/2 cycles, where g=gcd(2a+1,2k). Indeed pq is translation by 2a+1; its g residue classes are paired by q, with one fixed class containing both terminals. The other classes form cycles. Hence a legal assembly has exactly

```math
\gcd(2a+1,2k)=1.
```

Along its path set the companion boundary sign at a to +1 and reverse it across every q or p edge. There are 2k-1 edges, so the other terminal has sign -1. These signs give the unique orientation compatible with the prescribed actual boundaries. No extra orientation choice remains in a connected global vertex.

**Theorem 17.1 (complete coordinates).** Besides a, the sector vertices are exactly

```math
F(k,U,a,t),\qquad k\geq1,\quad0\leq U\leq2kL,
\quad0\leq a<2k,\quad t\in\mathbb Z,
\quad\gcd(2a+1,2k)=1.
```

All data are integers, and equal vertices have equal data. The surfaces are connected, have two actual boundaries, genus k(s-1), minimum T intersection 2k and k-1 pattern waves.

**Proof.** Essential cutting, HT block normalization and the joint ordered-sheet formula give coverage while carrying the common boundary motion into the pattern collar. Relative pattern classification leaves its one outer integer. Conversely every displayed diagram is oriented and essential by reverse assembly, and the gcd test excludes all closed components.

An efficient global comparison preserves T, hence N and the complete HT invariant U. A returning ordered companion system has neither a boundary permutation nor a meridional winding by Lemma 16.1. It therefore preserves a and t. Identical data specify the same reference assembly. This also proves minimum intersection by comparison to a true minimum representative. Genus follows from χ=2k(1-s). ∎

### 17.2. The marked projection

Cap the companion pairing by nested waves in a second pair of pants with two distinctly labelled auxiliary holes, retaining the root end marking. The whole chain becomes a simple arc between the actual holes in the resulting four-holed sphere. This is a labelled comparison, not a homeomorphism of Q with that cap.

[Lemma 8.1](odd-trees.md) gives its primitive vector (p,2k), where

```math
p=2a+1+4kt.
```

p is odd and gcd(p,k)=1. The root a is (1,0)=∞. Disjoint distinct arcs satisfy abs(pk'-p'k)=1. These arcs form the rooted tree T of the pure-stack analysis: every positive denominator has one smaller-denominator odd-numerator neighbour and there are no equal-denominator edges. The explicit parent is obtained from the two solutions of pk'-p'k=±1; exactly one has odd numerator. Parent denominators strictly decrease.

Define π(a)=∞ and π(F(k,U,a,t))=p/k. The state U is **not** discarded from the actual vertex; it is the coordinate in its finite fibre. Subsystem naturality in [§15](ordered-systems.md) and zero boundary returns in [§16](boundary-returns.md) ensure that replacing a whole disjoint union by cap waves gives this same π for each individual surface. Independent normalizations of the two sides would not suffice.
