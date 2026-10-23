# 8. Canonical pillowcase coordinates and the exact tree edges

[Contents](../README.md) · [Coordinate uniqueness](odd-returns.md) · [Main theorem](main-theorem.md)

Glue a second labelled pair of pants $`B_c`$, with boundaries $`b_0,c_0,c_1`$, to $`B`$ along $`b_0`$. This gives a four-holed sphere $`\Sigma`$. The label $`c_1`$ records the core-containing end chamber of the nested companion stack and $`c_0`$ the other end. Consider essential $`b_+`$-to-$`b_-`$ arcs with endpoints free on their labelled boundaries.

After minimizing intersection with $`b_0`$, an arc either avoids $`B_c`$ or cuts it in $`k`$ nested essential outer-to-outer waves, separating $`c_0,c_1`$. The $`B`$ part consists of two reaching arcs and $`k-1`$ waves. The cap pairing is $`q(i)=-1-i`$ and the pattern pairing is Lemma 3.5. An illegal matching would give a closed component, so is not one arc. Replacing the nested cap waves by actual $`S_\beta`$ pieces, preserving pairings and radial order, constructs a legal oriented essential chain; the zero-wave arc constructs $`A`$. This is a comparison construction, not a claim that the companion exterior is a two-dimensional cap or a Seifert product.

**Lemma 8.1 (canonical coordinates).** The marked arc classes, and hence the reference assemblies, are parametrized by the root $`(1,0)`$ and primitive vectors $`(p,2k)`$ with $`p`$ odd and $`k>0`$, modulo simultaneous sign. Canonical references may be chosen so that

```math
p=2j+1+4kt,\qquad
0\le j\lt2k,\qquad \gcd(2j+1,2k)=1.
```

**Proof.** Fill the four holes temporarily with marked points and use the pillowcase

```math
(\mathbb R^2/\mathbb Z^2)/(x\sim-x),\qquad
P_+=(0,0),\quad P_-=(1/2,0),\quad
C_0=(0,1/2),\quad C_1=(1/2,1/2).
```

A proper arc between the first two marked holes is half of a primitive torus circle. The endpoint condition is exactly odd first coordinate and even second coordinate. The complete classification is the pillowcase arc argument in [HT, p.232]. Choose second coordinate $`2k>0`$; at second coordinate zero, primitivity leaves the root $`(1,0)`$. The two lifts of $`b_0`$ are horizontal circles enclosing the two auxiliary points, and minimum intersection with $`b_0`$ is $`2k`$.

Choose the reference pattern for $`(k,j)`$ from the straight arc with vector $`(2j+1,2k)`$. To read its anchor, put the horizontal lifts at $`y=\pm c`$ and let $`c`$ tend to $`1/2`$ from below. The cap endpoints tend to

```math
x_h=\frac{p(h+1/2)}{2k},\qquad -x_h,
\qquad 0\le h\lt k.
```

Since $`\gcd(p,2k)=1`$, these are the cyclic points $`(2i+1)/(4k)`$. Their reflection is $`i\mapsto-1-i`$, and the positive reaching endpoint tends to $`p/(4k)`$. Hence $`p\equiv2j+1\pmod{4k}`$; the other end is antipodal. Straighten the cap system to fixed nested waves, retaining its order and distinct end labels.

An outer twist lifts to twists about **both** horizontal torus circles, so changes $`p`$ by $`4k`$. Choose its sign accordingly. This proves the formula and covers every primitive odd numerator, including negative ones. It is the same choice of reference in Lemma 6.4; no new vertex identification is imposed. ∎

**Proposition 8.2 (both directions of actual edges).** The cap-wave construction is a graph isomorphism between the odd-carrier sector, including $`a`$, and the marked arc graph. Two distinct vertices are adjacent exactly when

```math
\lvert pk'-p'k\rvert=1.
```

In particular $`a`$ is adjacent to a chain exactly when $`k=1`$.

**Proof.** Coverage is Proposition 6.5 and the reference computation above; injectivity is Corollary 7.4. For an actual edge between chains, Lemma 4.3 supplies disjoint representatives. Apply Lemmas 3.3–3.4 to their whole disjoint union. On this carrier, Lemmas 6.1–6.2 normalize the entire companion union to one parallel stack. Keep the assignment to each complete surface, radial order, orientations and common boundary matching. Replace all companion pieces by corresponding nested cap waves. The two complete surfaces become two disjoint marked arcs. On forgetting one arc, radial normalization of its cap waves is the same actual motion as radial normalization of its assigned companion pieces. Thus its canonical assembly is the original vertex, rather than a genus-based guess.

For a pair involving $`A`$, its efficient companion part stays empty: every nonempty longitudinal HT piece has negative Euler characteristic, whereas $`\chi(A)=0`$, and pattern pieces are annuli. Its zero-cap seam misses chain waves exactly at the root-edge cases of this arc graph.

Conversely start with disjoint marked arcs. Remove empty innermost bigons of their **union** with $`b_0`$, preserving disjointness. Replace the nested cap-wave union by one actual companion stack, retaining assignments, and take simultaneous vertical products of the pattern arcs. Reverse assembly gives the specified disjoint connected complete surfaces. Lemma 4.3 makes their class width one. This proves both directions of cyclic adjacency.

Finally two primitive torus circles lifting the two arcs already meet at the two common branch points. In straight minimal position they have $`\lvert\det\rvert`$ intersections; any additional one descends to an interior crossing. The arcs therefore have disjoint interiors exactly at absolute determinant two. Substituting second coordinates $`2k,2k'`$ gives the displayed determinant-one rule. For $`(1,0)`$ it says $`k=1`$. ∎

**Lemma 8.3 (unique parent).** This marked graph is a tree rooted at $`a`$.

**Proof.** For $`k=1`$ the unique smaller-denominator neighbour is $`(1,0)`$. If $`k>1`$, let $`r`$ be the inverse of odd $`p`$ modulo $`k`$, $`1\le r\lt k`$, and put

```math
(p_1,k_1)=((pr-1)/k,r),\qquad
(p_2,k_2)=(p-p_1,k-r).
```

These are the unique smaller-positive-denominator solutions for the two determinant signs, by reducing the determinant equation modulo $`k`$. Their numerators sum to odd $`p`$, so exactly one is odd. That one is the unique parent in this graph. Equal denominators give even determinant $`k(p-p')`$, so never an edge. Repeated parents strictly lower denominators and reach the root. Any finite cycle would have a maximum-denominator vertex with two distinct lower neighbours, impossible. Thus the graph is connected and acyclic. ∎

This is the odd-numerator subgraph of the Farey graph, rather than the full Farey graph. The scripts verify finite matching and parent identities; the geometric graph isomorphism is proved above.
