# 13. Orientability, component partitions, and the obstruction to larger pieces

[Contents](../README.md) · [Proof map](main-theorem.md) · [Sources](../sources/bibliography.md)

### 13.1. Boundary parity determines orientability

**Lemma 13.1.** On an odd zero-slope carrier, a connected carried component is orientable if and only if its number of boundary circles is even. Two one-sided longitudinal components cannot be disjoint.

**Proof.** A connected one-sided proper surface has nonzero relative mod-2 class: its complement is connected and a once-crossing arc closes there to give mod-2 intersection one. For a knot exterior $`H_2(Q;\mathbb F_2)=0`$, so the boundary map $`H_2(Q,T;\mathbb F_2)\to H_1(T;\mathbb F_2)`$ is injective. An even number of longitudinal boundaries has zero mod-2 boundary class. Thus an even-boundary connected surface cannot be one-sided and is orientable.

Conversely a carried component of degree $`n`$ is an abstract $`n`$-fold cover of the nonorientable one-sheeted plumbing, by HT printed p.244. An orientable cover factors through the orientation double and has even degree. Each boundary has degree one and there are $`n`$ boundaries, so odd $`n`$ is nonorientable.

For the final assertion, take two disjoint one-sided components. Each has an odd number of parallel longitude boundaries. Pair all boundaries of their union by disjoint annuli in a collar inside $`N(C)`$. This would produce a closed embedded surface in $`S^3`$ containing a nonorientable subsurface. It is impossible: every closed embedded surface in $`S^3`$ separates and is two-sided and orientable. ∎

Every orientable odd-carrier component has relative class zero and separates $`Q`$. Its even signed longitude sum cannot be a nonzero primitive generator, whereas a connected nonseparating oriented proper surface has primitive class. Its boundary signs therefore alternate around $`T`$, when other components are omitted.

The all-even knot expansion has even length, by reducing its continuant recursion modulo two. Equality of signed counts at zero slope then forces every zero carrier to have even length $`s`$. Nontriviality excludes $`s=0`$, so its two-sheeted oriented pieces have genus $`s-1>0`$, as required in the return argument.

### 13.2. The labelled folding partition

HT printed p.245 identifies the initial four sheet cycles into one $`N`$-cycle. Even coefficients introduce no further identification; each odd coefficient folds this cycle by a reflection. After transport along the labelled cycles of Figs.26--30 write these reflections as

```math
r_\nu(i)=c_\nu-i\pmod N.
```

For even $`N`$ the fold axes lie between adjacent sheets, so every $`c_\nu`$ is odd. A change of cycle origin conjugates all the reflections by the same rotation. The $`c_\nu`$ are read by following the labelled sheets in the finite HT plumbing; they are not independently chosen for a given parameter tuple.

Put

```math
d=\gcd\bigl(N,c_2-c_1,\ldots,c_h-c_1\bigr),
```

with $`d=N`$ for one odd coefficient. Products $`r_\nu r_1`$ are translations by $`c_\nu-c_1`$. Translation orbits are the residue classes modulo $`d`$; reflection pairs a residue $`t`$ with $`c_1-t`$. This gives the **actual boundary partition into components**:

- If $`N`$ is even, $`d`$ is even and the pairing of residues has no fixed class. There are $`d/2`$ components, each with $`2N/d`$ boundaries; all are orientable.
- If $`N`$ is odd, $`d`$ is odd and exactly one residue is fixed. It gives one nonorientable component with $`N/d`$ boundaries. The other $`(d-1)/2`$ components are orientable and each has $`2N/d`$ boundaries.

This is a direct orbit calculation from HT's sheet identifications, not an assertion that all components are parallel or isotopic. A component's restricted plumbing weights further specify its HT isotopy class. On a carrier of length $`s`$, $`\chi=n(1-s)`$ for a component with $`n`$ boundaries. Its orientable genus is $`1+n(s-2)/2`$; its nonorientable genus is $`2+n(s-2)`$.

### 13.3. Larger components cannot enter a global vertex

**Theorem 13.2 (the two-terminal obstruction).** In a legal oriented two-parallel spanning assembly on an odd carrier, $`d=N`$. All companion components have exactly two boundary circles, and the global incidence graph is a chain.

**Proof.** $`N=2k`$. Label the common boundary circles by $`\mathbb Z/N`$. An orientable component is a union of two residue classes modulo $`d`$ as just described. Its boundary signs alternate, so translation by $`d`$ preserves every sign. Hence the total companion boundary-sign function $`e`$ satisfies

```math
e(i+d)=e(i).
```

The pattern reflection for one spanning surface, with positive reaching endpoint $`a`$, is

```math
p(i)=2a-i\pmod N,\qquad i\ne a,a+k.
```

Every wave requires $`e(p(i))=-e(i)`$. If $`d<N`$, then $`d`$ is even and $`p`$ has two fixed residue classes modulo $`d`$, namely $`a`$ and $`a+d/2`$. Their preimages have $`2N/d\ge4`$ points in total. Only two points are actual terminals; choose a nonterminal point in these classes. Periodicity gives $`e(p(i))=e(i)`$, contradicting the required opposite signs. Thus $`d=N`$.

All fold reflections now agree, so their orbits are two-element pairs. Each companion vertex of the assembly incidence graph has degree two. There are two actual degree-one terminals; any cycle would be a whole closed component. The only legal graph is one chain. ∎

For example the six-boundary genus-seven frontier for $`12/29`$ from the pure-stack analysis exists in $`Q`$ but has $`d<N`$ and cannot be part of any legal oriented assembly, even after other companion components are added. This is stronger than the pure-stack sole-component obstruction.

**It does not remove the carrier.** Every odd carrier has an essential oriented two-sheeted frontier, which attaches by two reaching annuli and gives a $`k=1`$ vertex adjacent to $`a`$.

### 13.4. Connectedness for arbitrary odd carriers

The preceding theorem also gives a direct descent without a compatibility claim. For a chain with $`k>1`$, choose a base seam representing $`A`$ that misses its reaching arcs and meets each wave once. Cut at the first wave met from $`b_+`$, retain the terminal subchain containing the negative actual boundary, and attach it to $`b_+`$ along the initial seam segment. The new companion system is a nonempty proper subcollection of the old one; every retained local piece is essential. The new reaching annulus is essential, and the result is a legal oriented connected assembly. It is disjoint from the old complete surface after a small annular push and has strictly fewer companion pieces. The connected-wall criterion gives an edge. At $`k=1`$ there is an edge to $`a`$. Thus every odd-carrier sector is connected, for arbitrary two-bridge $`C`$.

This pointwise descent is not used as an unproved simplex-compatible contraction for several parameter blocks.
