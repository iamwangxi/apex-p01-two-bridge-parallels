# 12.5–12.8. Lower neighbours and finite contraction

[Contents](../README.md) · [Proof map](main-theorem.md) · [Sources](../sources/bibliography.md)

### 12.5. A natural lower neighbour

Fix a signature $`z`$. Its root is $`a`$ and its other vertices have the heights and marked coordinates of Theorem 12.2. For $`k>1`$ take the pattern wave nearest the positive actual hole. In boundary indices it is the $`p`$ edge joining $`a+1`$ and $`a-1`$. Delete that edge from the single-surface $`q/p`$ path and keep the component containing the negative reaching endpoint $`a+k`$. Let $`I`$ be its companion-pair indices. Set

```math
k_* = |I|,\qquad
H_{v,*}=\sum_{i\in I} C_{k,H_v}(i).
```

Its marked arc is the unique Farey parent of $`p/k`$; use that parent's canonical $`a_*,t_*`$ and call the resulting actual vertex $`D(F)`$. Set $`D(F)=a`$ at $`k=1`$.

This operation has a direct representative description. A seam for $`A`$ can miss both reaching arcs and cross the parallel waves in their order. Its initial portion to the first wave is disjoint from $`F`$. Cut $`F`$ at that annulus, retain its negative terminal subchain and join it to the positive actual boundary along that initial seam portion. Make the usual small annular push. The result is disjoint from $`F`$ and keeps exactly the companion components indexed by $`I`$. All cut pieces remain essential and the whole result is a legal oriented connected assembly. The retained subchain is nonempty and proper, so $`0<k_*<k`$. Its genus is smaller. Disjointness therefore gives a genuine cyclic edge.

The state is feasible by the restricted-weight lemma and has the same signature: on every odd band its retained value is $`k_*z_v`$. Its cap arc is disjoint from the old one with smaller denominator, so it is the unique marked parent. The root section and subsystem naturality identify it with the data above. Thus $`D`$ is defined on actual vertices, not just on separately selected diagrams.

**Compatibility when the first joint wave belongs to F.** If $`F,H`$ are disjoint and their entire joint pattern has its first wave at $`F`$, the same initial seam segment misses $`H`$. The retained part of $`F`$ already misses $`H`$. Its small push and new annulus may therefore be chosen disjoint from $`H`$. Consequently

```math
D(F)=H\quad\text{or}\quad D(F)\sim H.
```

This is the compatibility statement used below. It does not assume an arbitrary lower neighbour is compatible with $`H`$.

### 12.6. Which surface owns the first wave

Two disjoint non-root representatives have the joint diagram of §18. If their projected marked arcs differ, their denominators differ. The determinant is odd, so $`K=k+k'`$ is odd. Write $`s=u+1`$ and let $`r`$ in $`\{1,\ldots,K-1\}`$ be its inverse modulo $`K`$.

Start the first path at $`u`$. After $`2j`$ edges its boundary index is $`u+2js`$ modulo $`2K`$; after $`2j+1`$ it is $`-(2j+1)s`$. Its negative endpoint is $`u+K`$. Thus its companion count $`h`$ satisfies

```math
hs\equiv (K+1)/2\pmod K,
\qquad
h=\begin{cases}r/2,&r\text{ even},\\(K+r)/2,&r\text{ odd}.
\end{cases}
```

The first wave has endpoint $`u+2`$, occurring at the even position $`2r`$ in the full cycle. It belongs to the $`u`$-path exactly when $`r<h`$. If $`r`$ is odd that path has more than $`K/2`$ pieces and owns the wave. If $`r`$ is even the other, larger path owns it. Therefore **the first joint wave always belongs to the larger-denominator surface**.

For two vertices with the same marked projection, $`k=k'`$, $`K=2k`$ and the joint anchor is $`u=2a`$. Call $`P_*`$ the one of its two paths owning the first wave. Here $`k>1`$, so that wave exists. Collapse adjacent boundary pairs $`(2j,2j+1)`$. Both reflections preserve these pairs; the quotient is the one marked arc, and the two paths take one member of each pair. For a scalar joint height $`2h`$, each path restriction is $`h`$. For height $`2h+1`$, the two restrictions are $`h,h+1`$, since exactly one member of one adjacent companion pair is incremented. These statements hold for negative $`h`$ as well, by the full-cycle identity for $`C`$.

### 12.7. An explicit finite rank on the fibres

For a large **even** band $`v`$ at distance $`d_v`$ from $`o`$, all height values in a $`k`$-fibre lie in the finite interval

```math
J_{k,v}=[-2k\lfloor d_v/2\rfloor,
             2k\lceil d_v/2\rceil]\cap\mathbb Z.
```

For every unit pair $`h,h+1`$ in this interval use the formal parallel-path diagram $`u=2a`$ and total scalar height $`2h+1`$. Orient that unit pair from the value on $`P_*`$ to the value on the other path. This construction is scalar; it need not be a feasible full carrier state. Its underlying graph is a finite path, so it has no directed cycle. Let $`\rho_{k,a,v}(h)`$ be the maximum number of directed edges in a path beginning at $`h`$. It is a finite, explicitly computable nonnegative integer and strictly decreases on each directed edge.

Define

```math
\rho(F)=\sum_{v\in J,\ b_v\text{ even}}
             \rho_{k,a,v}(H_v).
```

The odd heights are fixed at $`kz_v`$ inside this signature and are omitted. If two distinct adjacent vertices have the same marked projection, their height restrictions differ by at most one on each coordinate. On every changed coordinate the first-wave path is the source of the scalar directed edge just defined. On unchanged coordinates the ranks agree. At least one even large coordinate changes, since all other data are fixed. Hence $`\rho`$ differs strictly on every such actual edge, and the surface owning the first wave is exactly the one with larger $`\rho`$.

This argument includes all constraints coupling the coordinates. It does not assert a raw product structure on feasible states. If there is no even large band, a marked fibre has a single vertex and there is no same-projection edge to order. At $`k=1`$ no fibre rank is needed, since $`a`$ is adjacent to every vertex in that layer.

### 12.8. A finite contraction for every signature

**Theorem 12.3.** For every odd zero-slope HT carrier and every signature $`z`$, its entire rooted signature subcomplex is contractible. Every finite subcomplex is contained in a finite contractible induced flag subcomplex.

**Proof.** Begin with a finite vertex set and add $`a`$ and every iterate of $`D`$. This is finite because $`D`$ strictly decreases $`k`$ until it reaches $`a`$. Take the full induced flag complex $`Z`$ on that finite set.

Among its non-root vertices choose one $`F`$ of largest $`k`$, and among vertices with its marked projection choose one of largest $`\rho`$. A neighbour $`H`$ remaining in $`Z`$ has either smaller denominator or the same marked projection. There is no edge between different marked projections with equal denominator. In the smaller-denominator case the first joint wave belongs to $`F`$ by §12.6. In the same-projection case its rank is strictly lower, so the first wave again belongs to $`F`$ by §12.7. Thus $`D(F)`$ is equal or adjacent to every neighbour of $`F`$, and it is adjacent to $`F`$ itself.

The closed neighbourhood of $`F`$ is consequently contained in the closed neighbourhood of $`D(F)`$. In a flag complex the map sending $`F`$ to $`D(F)`$ and fixing every other vertex is simplicial and contiguous to the identity: any simplex containing $`F`$ may also include $`D(F)`$. The straight-line homotopy in that finite simplex removes $`F`$ while fixing the remaining subcomplex. The retained vertex set remains $`D`$-closed, because a largest-denominator vertex cannot be the $`D`$-image of a remaining vertex of no larger denominator.

Repeat. When only the $`k=1`$ layer and $`a`$ remain, $`a`$ directly dominates every remaining vertex. The finite induced complex contracts to $`a`$. This is a proved neighbourhood argument with the explicitly defined rank and subchain operation; it invokes none of PS's order or dismantling conclusions.

Every finite subcomplex is therefore null-homotopic inside such a finite carrier. The signature sector is connected by $`D`$. Compact images in the weak CW realization lie in finite subcomplexes, so all its homotopy groups vanish. Whitehead gives contractibility. ∎

The proof uses a maximum only in a finite $`D`$-closed set. It does not posit a global well-order with finite lower stars or an infinite sequence of collapses whose continuity would be unverified.
