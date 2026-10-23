# 9. The tree of disks

[Contents](../README.md) · [Proof map](main-theorem.md) · [Sources](../sources/bibliography.md)

### 9.1. A projected vertex has a path as its fibre

Fix a non-root marked vertex $`v=(p/k)`$, with its $`a,t`$. Its actual vertices have $`U=0,\ldots,2kL`$.

**Lemma 9.1.** The full fibre $`\pi^{-1}(v)`$ is the path

```math
0\ --\ 1\ --\ \cdots\ --\ 2kL.
```

**Proof.** In a joint diagram of two parallel cap arcs $`K=2k`$ and $`u=2a`$. Collapse each adjacent pair of boundary indices $`(2j,2j+1)`$. Both $`q`$ and $`p_u`$ preserve that pairing, and the quotient is the one cap arc. Its two lifted paths take one member of each adjacent pair; equivalently one component of each adjacent pair of companion indices belongs to each surface.

For total state $`2h`$, the ordered profile is the doubled profile of the $`k`$-piece state $`h`$:

```math
f_{2k,2h}(2i)=f_{2k,2h}(2i+1)=f_{k,h}(i).
```

Both surfaces then have the same state and represent the same vertex. For total state $`2h+1`$, precisely one member of one such pair is incremented by one. The two restrictions are $`h`$ and $`h+1`$. Conversely each $`h,h+1`$ is obtained from that joint state, with its two path assignments. These and only these are the distinct fibre edges. Flag completion of a path adds nothing. ∎

At $`k=1`$ this is the coexistence path of the $`S`$ types. The root fibre is the single vertex $`a`$.

### 9.2. A projected edge has one triangulated disk above it

Fix a non-root edge $`vv'`$ of the marked tree, with denominators $`k,k'`$, and $`K=k+k'`$. There is one joint anchor $`u`$, up to the common winding and exchange of the two assignments. One way to see uniqueness is to take the canonical geodesic representatives of the two distinct proper arc classes on the four-holed sphere. They determine their joint marked isotopy class, hence the cyclic cap list and the first positive port. Conversely the $`p_u`$ diagram constructs that pair. The labels of the auxiliary holes fix the end gap. This is an elementary simultaneous arc comparison, not a three-dimensional isotopy claim.

As total state $`T`$ runs from 0 to $`2KL`$ define

```math
x(T)=\sum_{i\in I(V)} f_{K,T}(i),\qquad
y(T)=\sum_{i\in I(V')} f_{K,T}(i).
```

The cross edges above $`vv'`$ are exactly $`(x(T),y(T))`$. At $`T=0`$ the pair is $`(0,0)`$, and at $`T=2KL`$ it is $`(2kL,2k'L)`$. Increasing $`T`$ by one increments exactly one component value in the profile: the active component indices run

```math
0,1,\ldots,K-1,K-1,\ldots,1,0
```

for each full block capacity. That component is in exactly one of the two paths. Thus $`x+y=T`$ and the pairs form a monotone unit-step lattice path from one corner of the rectangle of state indices to the opposite corner.

Include the two fibre paths. Consecutive cross edges share one endpoint and their other endpoints are consecutive in a fibre; flag completion fills the corresponding triangle. Starting with the first cross edge, each step adds one new vertex and one triangle along the preceding cross edge. This builds a triangulated disk whose boundary consists of the two fibre paths and its first and last cross edges. It has exactly $`2KL`$ triangles.

There are no extra triangles or higher simplices: a triangle must use a fibre edge and the two cross edges at one unit step; four vertices in a clique would require all four corners of a unit rectangle in a monotone path, which is impossible. The full inverse image of $`vv'`$ is exactly this disk. For $`L=0`$ it is an edge.

Above an edge from $`a`$ to a $`k=1`$ marked vertex, the inverse image is the cone on its fibre path. It is a finite triangular fan, with $`2L`$ triangles, or an edge when $`L=0`$.

### 9.3. Contraction and all simplices

**Theorem 9.2.** A one-odd carrier with at most two large coefficients has contractible rooted subcomplex. For $`L\ge1`$ it is exactly a two-dimensional tree of finite triangulated disks over the marked Farey tree. The intersection of two panels meeting over a marked vertex is that vertex's entire fibre path.

**Proof.** Projection sends every edge to a vertex or edge of the marked tree. A simplex, by flag completion, therefore projects into one marked edge or vertex. Lemma 9.1 and §9.2 identify all the inverse images, including their higher simplices. Distinct panels meet exactly as specified by the base tree; there is no unexamined compatibility of independently chosen representatives.

For a finite subcomplex $`K_0`$, take the finite subtree spanned by its projected vertices and $`a`$. The **full** inverse image is finite: each marked fibre and each panel is finite. At a leaf of this subtree, its panel meets the rest precisely in the parent fibre path, a boundary arc of the panel disk. A disk strongly deformation retracts onto that boundary arc while fixing it, as is seen by a rectangle parametrization. A root fan similarly retracts to its root when it is the last panel. Remove leaves successively. The full finite inverse image contracts to $`a`$.

Thus every finite input is contained in a finite contractible carrier. Compact images in the weak CW realization lie in finite subcomplexes. All homotopy groups vanish, and the complex is connected; Whitehead's theorem gives contractibility. For $`L=0`$ the same proof is the ordinary tree contraction. No PS projection or dismantling theorem is invoked. ∎

For $`16/39`$, $`L=2`$. Above every marked denominator $`k`$ there is a path of $`4k+1`$ actual vertices. The marked root edges have four-triangle fans. Above a non-root marked edge of denominators $`k,k'`$ there is a disk with $`4(k+k')`$ triangles. In particular this carrier sector is not a tree: it contains filled triangles.
