# 7. Full return winding and uniqueness of odd coordinates

[Contents](../README.md) · [Stack and pattern data](odd-normal-forms.md) · [Next: tree and edges](odd-trees.md)

Fix one oriented $`S_\beta`$. Let $`H_\beta\subseteq\mathbb Z`$ be the meridional winding numbers of identity-starting ambient isotopies in $`Q`$ returning it with its orientation. Boundary circles return individually by Lemma 6.3; their winding is common because disjoint ordered longitudes cannot pass each other. Concatenation and reversal make this a subgroup. Longitudinal displacement leaves vertical pattern annuli unchanged.

**Lemma 7.1 (one common subgroup).** Every oriented reference stack of $`k`$ copies, with any independent orientation signs, has the same return subgroup $`H_\beta`$.

**Proof.** A return preserves each component and boundary by Lemma 6.3. Restrict to one component and conjugate by a radial identification with the one-piece reference. Its common winding belongs to $`H_\beta`$. Conversely take a one-piece return and carry all nearby parallel levels by that ambient isotopy. The endpoint preserves the surface orientation and hence normal direction. Collar straightening relative to the central piece adjusts the endpoint to preserve the chosen levels. The adjustment is in small normal intervals and adds no full meridional turn. Every level returns with the same winding and retains any assigned sign. Radially conjugate back to the prescribed stack. ∎

**Lemma 7.2 (equality before computing the subgroup).**

```math
[F_\beta(k,j,t)]=[F_\beta(k',j',t')]
\quad\Longleftrightarrow\quad
k=k',\quad j=j',\quad t'-t\in H_\beta.
```

**Proof.** Efficient torus comparison preserves the stack size; Lemma 6.3 fixes its indexed boundary circles, so the positive reaching end has the same $`j`$. Restrict the comparison to $`Q`$ and transport the resulting common boundary path through the pattern collar. Full meridional circuits contribute exactly outer twists, up to the fixed sign convention. After removing this transport, Lemma 6.4 compares fixed-endpoint pattern systems and gives the asserted difference. The sign is immaterial for a subgroup.

Conversely a return realizing any subgroup element carries the entire stack by Lemma 7.1. Extend its common boundary path through the pattern collar; its endpoint changes the outer twist by that integer. Relative isotopy extension gives an ambient isotopy of the compatible assembly. ∎

**Lemma 7.3 (confinement).** Two isotopic $`k=1`$ forms with the same reaching end have the same winding integer. Consequently $`H_\beta=\{0\}`$.

**Proof.** Fix a small two-sided collar $`U=S_\beta\times[-\varepsilon,\varepsilon]`$. Its boundary annuli on $`T`$ lie in two disjoint proper meridional strips $`J_+,J_-`$. Place the two companion pieces at distinct normal levels in $`U`$, extending these small radial movements into the pattern collar with no full circuit. Their common-torus traces and actual boundaries are disjoint. Both full surfaces remain efficient.

Apply the finite empty-product simplification of Proposition 3.8, keeping one surface fixed. Its proof excludes returning $`T`$ traces in any product region and straightens all spanning traces to product annuli. Cutting the region along those annuli gives horizontal products lying in $`Q`$ or $`P`$.

Any nonempty horizontal-face portion in $`Q`$ is an **entire** companion piece. A boundary inside $`Q`$ would have to be a collapsed intersection curve or actual manifold boundary; the companion pieces are disjoint and $`Q`$ has no actual link boundary. Neither is available. Thus a product component in $`Q`$ has the two whole companion pieces as faces, remaining boundary on $`T`$, and empty interior. Its interior is open and closed in a companion complement chamber, hence is that whole chamber.

The connected separating $`S_\beta`$ and two distinct parallel copies cut $`Q`$ into three chambers. Only the middle chamber has both pieces in its frontier. Therefore every such product component is the middle parallel slab inside $`U`$, and its torus annuli remain in $`J_+\cup J_-`$. There is no extra product component in $`Q`$ with empty horizontal face: cutting by spanning product annuli gives products of nonempty cut-face components.

Perform the product push tangent to $`T`$ and supported, on its companion side, in this slab and small collars. For a non-final push passing the moving piece through the fixed piece, take the endpoint at a nearby distinct normal level, still in $`U`$. This is the usual small push beyond a horizontal product face. The collapsed intersection curves being removed are on the pattern side, so this displacement does not spoil the reduction or introduce companion intersections. A region missing $`Q`$ can be pushed away from $`T`$. Thus the same two-piece confinement persists after every move without independently renormalizing the pair. The finite process terminates with the isotopic whole surfaces coincident, reducing the transverse count or finally identifying the whole component exactly as in Proposition 3.8.

All companion boundary motion in this constructed comparison stays in its original proper strips. Close the initial and final small radial paths within those strips. Its meridional winding is zero. Remove that boundary transport and apply the fixed-outer-endpoint test of Lemma 6.4: $`t=t'`$.

This constructs a confined comparison; it does not assume that the originally given isotopy was confined. Any $`m\in H_\beta`$ would identify $`F_\beta(1,0,0)`$ and $`F_\beta(1,0,m)`$ by Lemma 7.2, so confinement forces $`m=0`$. The constant return realizes zero. ∎

**Corollary 7.4 (complete odd equality).**

```math
[F_\beta(k,j,t)]=[F_\gamma(k',j',t')]
\quad\Longleftrightarrow\quad
\beta=\gamma,\qquad (k,j,t)=(k',j',t').
```

**Proof.** Lemmas 7.2–7.3 prove it on a fixed carrier. Efficient comparison and carrier purity preserve the carrier. The other direction uses identical specified assemblies. ∎

All hypotheses used in confinement have been proved: connectedness, separation, two boundaries and positive genus of the piece; simultaneous parallelism; no returning boundary permutation; and efficient torus comparison. No particular genus, such as genus three, is required.
