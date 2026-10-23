# 6. Odd carriers under (P): pure stacks and complete coverage

[Contents](../README.md) · [Carrier input](carriers.md) · [Next: return winding](odd-returns.md)

Fix an odd zero-slope carrier $`\beta`$ satisfying (P), of length $`s`$, and let $`\ell`$ be the position of its unique exceptional coefficient. Write its sheet parameters as $`x_1,\ldots,x_{s-1}\in[0,N]`$.

**Lemma 6.1 (bounded normalization).** All parameter vectors are connected to zero by HT moves, staying within the parameter box.

**Proof.** At each coefficient except $`\ell`$ the value is $`\pm2`$. HT Theorem 1(e) permits adding or subtracting one from both adjacent parameters, with the same sign, omitting the absent parameter at an endpoint. Deleting the $`\ell`$-th move splits the variable chain into two independent blocks, each controlled from its outside endpoint.

A block of $`m`$ variables with an endpoint single-coordinate move and consecutive same-sign pair moves is connected in $`[0,N]^m`$. Induct on $`m`$. For one variable this is immediate. To lower a positive last coordinate, use induction to put the last coordinate of the prefix at one, without changing the block's last coordinate, then lower that final pair by one. Repeat until the last coordinate is zero and normalize the prefix. The temporary value one is allowed even for $`N=1`$. Reversibility gives all prefix changes used in the induction. Apply this independently to both blocks; an endpoint exceptional coefficient leaves just one nonempty block. ∎

Let $`B_\beta`$ be the zero-parameter one-sheet plumbing and $`S_\beta`$ its horizontal regular-neighbourhood frontier, omitting the vertical annulus on $`T`$ and rounding corners.

**Lemma 6.2 (simultaneous stack).** The entire zero-parameter system is

```math
S_{2k}(0)=kS_\beta,\qquad
S_{2k+1}(0)=B_\beta\cup kS_\beta,
```

as actual simultaneous nested parallel systems. Thus every oriented system on $`\beta`$ is a stack of $`S_\beta`$ pieces, with independent orientations. Each piece is connected, separating, essential, has two opposite longitude boundaries, class zero, and genus $`s-1>0`$.

**Proof.** At zero parameters all sheets choose the same plumbing squares, so they are the ordered normal-level neighbourhood model of the one-sheet plumbing. It is one-sided because the carrier is not all even [HT, p.230]. Its normal holonomy reverses the normal coordinate. Nonzero levels therefore pair as $`\{t,-t\}`$; an odd number also retains the middle level zero. Each pair is the connected orientation double, namely the horizontal frontier. The explicit doubling rule is [HT, p.240]. Varying the positive radius gives genuine simultaneous parallel copies, not separately normalized components.

Odd total sheet number retains the nonorientable core and is excluded for an oriented system. Lemma 6.1 brings every parameter choice to this model. The frontier is essential by HT Theorem 1(c), has $`\chi=2(1-s)`$ and two boundaries, hence genus $`s-1`$. Its relative class is zero as a neighbourhood frontier, and it separates. The length is even by §2 and positive; the nontrivial knot case here has $`s\ge2`$. ∎

For a fixed reference stack of $`k`$ pieces its cyclic boundary order and pairing are

```math
S_1^+,\ldots,S_k^+,S_k^-,\ldots,S_1^-;
\qquad q(i)=-1-i\pmod{2k}.
```

Independent orientations replace this sign word by $`(\epsilon_1,\ldots,\epsilon_k,-\epsilon_k,\ldots,-\epsilon_1)`$, without changing the pairing.

**Lemma 6.3 (no boundary permutation).** A returning identity isotopy of the underlying stack fixes every boundary circle individually and does not exchange its end chambers. Its endpoint also preserves every chosen orientation sign.

**Proof.** On the torus the permutation preserves cyclic meridian order, so is a rotation $`i\mapsto i+r`$. Preserving $`q`$ gives $`2r=0\pmod{2k}`$, hence $`r=0`$ or $`k`$. The latter interchanges the end chamber containing $`B_\beta`$ and the other end chamber. The endpoint homeomorphism would send that one-sided essential core into the opposite chamber, disjoint from the original core. Both have carrier $`\beta`$ under identity isotopy. Their union, by carrier purity, is a two-sheet system there; but every two-sheet surface on an odd carrier is connected [HT, Proposition 1(2)]. This contradicts the two disjoint components. Thus $`r=0`$. The torus isotopy preserves longitude orientation, so signs at individually fixed circles are preserved as well. ∎

**Lemma 6.4 (pattern winding).** With outer points, matching and labelled reaching ends fixed, and inner endpoints free on their labelled circles, an essential pattern system is $`D_0^t\alpha`$ for a unique $`t\in\mathbb Z`$. Here $`D_0`$ is an outer-boundary collar twist and $`\alpha`$ a fixed reference.

**Proof.** Cut along reaching arcs and then waves. Corresponding boundary intervals identify the resulting disks, gluing to a homeomorphism fixing the outer boundary and preserving inner labels. A hexagon seam decomposition shows that a labelled pair of pants with pointwise fixed boundary has only its three boundary-collar twist discrepancies: remove seam bigons, read the collar windings, and apply disk isotopy after removing them. Free rotation of each inner boundary absorbs its collar twist, leaving only the outer integer.

For uniqueness compare positive reaching paths from the same outer point to $`b_+`$. An extra $`m`$ outer twists prefixes the path by $`b_0^m`$; movement of the inner endpoint only adds a power of $`b_+`$. In $`H_1(B;\mathbb Z)`$ the coefficient of $`[b_-]`$ in $`[b_0]`$ is $`\pm1`$, whereas it is zero in $`[b_+]`$. Homotopy of the reaching paths therefore forces $`m=0`$. ∎

**Proposition 6.5 (legal chains and coverage).** Every odd-carrier spanning vertex is a chain of $`k\ge1`$ copies of $`S_\beta`$. With positive reaching endpoint $`j`$ in the indexed $`2k`$-boundary stack, legality is exactly

```math
0\le j\lt2k,\qquad \gcd(2j+1,2k)=1.
```

Its compatible orientations are unique. Together with one winding integer $`t`$, this gives a covering family $`F_\beta(k,j,t)`$ with

```math
g(F_\beta)=k(s_\beta-1),\qquad
\chi(F_\beta)=2k(1-s_\beta),\qquad
\lvert F_\beta\cap T\rvert=2k,\qquad u=k-1.
```

Every $`k`$ occurs, for example with $`j=0`$.

**Proof.** Collapse companion pieces to degree-two vertices, waves to edges, and reaching annuli to two degree-one actual terminals. A legal assembly has one terminal path; any additional cycle would be a forbidden closed component.

Before collapsing companion edges the matching graph has the $`q`$ edges and the reflection $`p_j`$ edges except its two fixed points. Put $`d=\gcd(2j+1,2k)`$. Completing the fixed points gives

```math
(p_j\circ q)(i)=i+2j+1\pmod{2k}.
```

Its translation orbits are the $`d`$ residues modulo $`d`$. The odd integer $`d`$ divides $`k`$. Reflection pairs residues $`r,-1-r`$, with one fixed residue containing both reaching ends. Removing their fixed-point loops leaves one terminal path with $`2k/d`$ boundary vertices and $`(d-1)/2`$ cycles, each with $`4k/d`$ boundary vertices. Thus the path uses $`k/d`$ companion pieces and each cycle $`2k/d`$. Precisely $`d=1`$ is legal.

Put sign plus at $`j`$ and reverse sign across every companion or wave edge. The legal path has $`2k-1`$ edges, so the other reaching sign is minus. This gives the unique component orientations and opposite signs for each annular gluing. Reverse assembly proves incompressibility; annular gluing preserves Euler characteristic and gives the displayed genus. Efficient comparison proves minimal $`T`$ intersection.

For coverage, minimize and essentialise the given whole surface, simultaneously normalize its entire companion system using Lemmas 6.1–6.2, extend the shared boundary path into the pattern collar, and apply Lemma 3.4. The reflection determines $`j`$, the matching graph gives legality and orientations, and Lemma 6.4 records the last integer. Longitudinal boundary motion adds no parameter because fibre rotation leaves vertical annuli invariant. The annulus and the all-even list of §5 cover the other vertices. Carrier purity and Proposition 3.8 distinguish the labels, and connectedness distinguishes the odd vertices from all-even ones. ∎

The references for $`F_\beta(k,j,t)`$ are fixed canonically by the pillowcase construction in §8. That definition only chooses the reference in Lemma 6.4; it does not assume the equality or edge assertions proved next.
