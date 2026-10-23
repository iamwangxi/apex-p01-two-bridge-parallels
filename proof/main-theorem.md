# 12.4. Contractibility for every nontrivial two-bridge companion

[Contents](../README.md) · [Proof map](main-theorem.md) · [Sources](../sources/bibliography.md)

Read the proof in the following order. The general geometric foundations are [essential assemblies](assemblies.md), [whole-complement comparison](comparison.md), [carrier purity](carriers.md), and the [all-even cone](even-cone.md). The [two-terminal obstruction](assembly-obstruction.md), Theorem 13.2, excludes every larger-boundary companion component from a legal oriented odd-carrier assembly. [Bounded parameters](bounded-parameters.md) and [general boundary returns](boundary-returns.md) supply the required isotopy interfaces. [Rooted band heights](band-heights.md), Lemma 12.1 and Theorem 12.2, then classify every actual vertex and edge. Finally [finite contraction](finite-contraction.md), Theorem 12.3, treats each odd-band signature.

The one-block models are proved separately in [ordered systems](ordered-systems.md), [global vertices](odd-vertices.md), [integer edges](odd-edges.md), [trees of disks](one-odd-disks.md) and [two-odd trees](two-odd-trees.md). They are more explicit structures inside the universal result, not assumptions on its scope. The original [pure stacks](odd-normal-forms.md), [returns](odd-returns.md), and [marked Farey tree](odd-trees.md) prove the (P) specialization without relying on the new general contraction.

**No cross-carrier edges.** Every odd-carrier vertex is connected by Theorem 13.2. A hypothetical cross-carrier edge therefore has disjoint representatives by Lemma 4.3. Essentialise their entire union by Lemma 3.3 and verticalise by Lemma 3.4. Proposition 3.8 makes each carrier intrinsic. The mixed essential companion union contradicts Proposition 2.2. This argument applies without (P). Different odd-band signatures on one carrier have no non-root edge by §12.4 of [the height classification](band-heights.md).


### 12.9. The all-two-bridge conclusion

**Theorem 12.4.** For every nontrivial two-bridge companion C, the entire complex X of its two oppositely oriented zero-framed parallels is contractible.

**Proof.** The vertices and edges are completely covered by the [geometric foundations](assemblies.md), [whole-block comparison](comparison.md) and [all-even cone](even-cone.md) and Theorem 12.2. The all-even part is a cone. Distinct carriers have no non-root cross edge by purity, and distinct signatures in one odd carrier have no non-root cross edge by §12.4. There are finitely many carriers and signatures, each signature occurring among finitely many two-sheeted types. Flag completion therefore expresses X as their pointed union at a, together with the all-even cone.

For any finite subcomplex extend each odd-signature portion by Theorem 12.3, and extend its all-even portion by the finite cone with a. The union is a finite contractible carrier, with all contractions fixing a. Thus X is connected and weakly contractible; its weak simplicial realization is a CW complex and is contractible by Whitehead.

This includes the two-large-coefficient disk and tree descriptions in §§9 and 11, all one-odd carriers with arbitrarily many large even coefficients, and carriers with several odd coefficients. No larger-boundary piece is presumed absent without proof: its exclusion was Theorem 13.2, and the full assembly criterion and signatures were derived from the explicit rooted matching. ∎



## The explicit structure under (P)

**Proof of Corollary 1.3 (the (P) structure).** Sections 5–7 cover and distinguish all vertices. Proposition 5.2 gives $`\mathcal B_E=a*Y_E`$. Proposition 8.2 gives every edge in an odd sector; Lemma 8.3 proves that sector is a rooted tree. The no-cross-carrier argument above excludes all cross edges away from the root. Since the complex is flag, each simplex lies either in the all-even cone or in one of the odd trees. A tree has no three-vertex clique, so its flag completion contributes no higher simplex. This proves equality of the entire simplicial complexes, not merely their vertex sets or finite subgraphs.

Use weak simplicial, equivalently CW, topology on the realizations. Give every tree edge unit length and contract a point toward its root along its unique finite root path, multiplying its distance from the root by $`1-t`$. On each closed edge times the time interval the image lies in a finite rooted subtree, where this is continuous. The weak-topology product criterion with the locally finite CW interval gives continuity on the whole tree times the interval. Perform these contractions on all odd trees while fixing $`\mathcal B_E`$. They agree at their only common point $`a`$ and are continuous by the same cellwise criterion.

Then contract the cone by barycentric interpolation to its apex. For a point in a base simplex $`\sigma`$, the path lies in $`a*\sigma`$ and is $`(1-t)x+ta`$. Extend this stage by keeping the already collapsed tree points at $`a`$. The two stages fix $`a`$ throughout and give a contraction of all of $`X(L)`$. The number of carriers is finite by Lemma 2.1; no finiteness of vertex sets or genus bound was used. ∎

If $`O(C)`$ is empty the entire result is the all-even cone. If its base happens to be a point, the cone is one edge and the entire complex is a tree with that additional leaf. Neither special case is imposed in the general theorem.
