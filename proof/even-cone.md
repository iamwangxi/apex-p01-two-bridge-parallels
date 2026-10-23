# 5. The all-even part is a cone

[Contents](../README.md) · [HT input](carriers.md) · [Equality and edges](comparison.md)

**Lemma 5.1 (all-even vertex coverage).** Every non-annular vertex whose companion carrier is $`E`$ is disconnected with two components, one actual boundary on each. Each has genus $`s_E/2`$. These vertices are covered by the following specified assemblies:

- An actual HT system $`E_2(x_1,\ldots,x_{s_E-1})`$ with every $`x_i\in\{0,1,2\}`$.
- A choice $`j\in\{0,1\}`$ of the boundary reached from the positive actual torus, fixing both component orientations.
- An outer-collar pattern winding $`t\in\mathbb Z`$, relative to one fixed straight-boundary reference for each finite HT diagram and reaching-end choice.

Write these assemblies as $`G(x,j,t)`$. They form a covering list, with duplicates identified exactly by Proposition 4.2.

**Proof.** By Lemma 2.3 each companion component has one boundary. An outer-to-outer pattern annulus would close the sole boundaries of two such pieces to make a forbidden closed whole component. Hence $`u=0`$, $`N=2`$, and there are two reaching annuli and two oppositely oriented companion components. HT classifies the entire two-sheet system using the stated finite parameter box. Normalize that system simultaneously, carrying its boundary motion into the pattern collar. Lemma 3.4 then verticalises the pattern relative to all straight boundaries.

For fixed outer points and labelled reaching ends the pattern has one remaining outer-twist integer by Lemma 6.4 below. This is an elementary pair-of-pants statement independent of (P) and proved there without using this lemma. Thus the list covers every vertex. All listed compatible assemblies are essential by Lemma 3.6. Duplicates and internal edges are determined by the whole-system geometric comparison of §4, which includes companion permutations, HT moves and boundary circuits. ∎

**Proposition 5.2 (the cone).** Let $`Y_E`$ be the full subcomplex on these all-even vertices. Its full subcomplex together with $`a`$ is exactly $`\mathcal B_E=a*Y_E`$.

**Proof.** For one actual simultaneously vertical representative $`G`$, cut $`B`$ along its two reaching seams. In the resulting disk choose an arc joining the two original inner boundary segments and missing both seam faces. It gives an inner-to-inner seam disjoint from the **same complete representative** $`G`$. Its vertical annulus represents $`a`$, since all such seams are isotopic with free endpoints on labelled boundaries. It is connected and distinct from $`G`$, so Lemma 4.3 gives $`\delta(a,[G])=1`$.

Thus $`a`$ is adjacent to every vertex of $`Y_E`$. By flag completion it cones every simplex of $`Y_E`$. No simultaneous geometric representative for an arbitrarily preselected clique is needed. ∎

No fibration or uniqueness of companion Seifert surfaces was assumed. The base $`Y_E`$ need not be a point, and arbitrary disjoint disconnected pairs are not declared edges. If $`O(C)`$ is empty, these are all vertices and $`X(L)`$ is this cone.

For comparison with a common sufficient condition, define (SB) to mean that every connected orientable essential longitudinal surface in $`Q`$ without closed components has one boundary. It holds for a two-bridge knot exactly when $`O(C)`$ is empty. One direction follows from the all-even component count. In the other direction, an odd zero carrier has a one-sided one-sheet plumbing; its connected orientable horizontal neighbourhood frontier is a two-sheet essential surface with two longitudes [HT, p.240 and Theorem 1(c)]. This violates (SB). The infinite family in §10 has such a frontier and lies beyond this annulus-cone sufficient condition.
