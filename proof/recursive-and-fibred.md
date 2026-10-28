# Zero-framed parallel clusters beyond two-bridge knots

The construction class and the nonzero-orientation-sum fibred case are stated separately. General Montesinos knots are outside the proved range.

## 1. Statements and conventions

Let $`\mathcal C`$ be the smallest class of nontrivial knots with the following properties:

1. Every nontrivial two-bridge knot and every nontrivial torus knot belongs to $`\mathcal C`$, including mirrors.
2. A connected sum of finitely many members belongs to $`\mathcal C`$.
3. If $`J\in\mathcal C`$, its $`(p,q)`$ cable belongs to $`\mathcal C`$ whenever $`p\ge2`$, $`q\ne0`$, and $`\gcd(p,q)=1`$. The winding number is $`p`$, and the cable curve on the companion torus is $`p\lambda_J+q\mu_J`$.

Only finite constructions are allowed. Adjacent connected-sum operations may be flattened into one composing block. Fix one such construction, with an ordering of the children of each composing block. It is used for the proof, not added to the equivalence relation on surfaces.

For a nontrivial knot $`K`$, let $`L=L(K;n,\epsilon)`$ consist of $`n\ge1`$ labelled, **zero-framed** parallels, with orientations $`\epsilon_i\in\{1,-1\}`$, and put $`d=\sum_i\epsilon_i`$. All statements use the full reduced ordinary conventions: surfaces are oriented and componentwise incompressible; disconnected surfaces are allowed; every actual boundary torus is used once; closed components are forbidden; boundaries may move on their labelled tori; ambient isotopies start at the identity. There is no genus bound or norm restriction.

The cyclic complex $`X(L)`$ is the flag complex of class-minimum whole-complement width one for the **single** total oriented linking class $`\Phi`$. The geometric complex $`Y(L)`$ uses simultaneous disjoint representatives. Write $`MS(L)`$ for the taut cyclic subcomplex, with the Przytycki–Schultens edge convention.

**Theorem A (two-bridge and torus construction class).** If $`K\in\mathcal C`$, then for every $`n`$ and every orientation pattern,

```math
|X(L)|\searrow |MS(L)|,
\qquad
|Y(L)|\searrow |MS(L)|.
```

In particular both complexes are contractible. In the balanced case $`d=0`$, $`MS(L)`$ is precisely the full cyclic subcomplex of pure pattern-annular vertices.

This includes arbitrary connected sums of two-bridge knots and arbitrary finite nesting of connected sums and cables with two-bridge or torus terminal knots. Cables of hyperbolic two-bridge knots supply prime satellite companions outside both the two-bridge and graph-manifold ranges. The connected-sum subfamily gives a composite arborescent extension; no statement about all prime arborescent knots is intended.

**Theorem B (arbitrary fibred companions, nonzero total orientation).** If $`K`$ is any nontrivial fibred knot and $`d\ne0`$, the two strong deformation retractions in Theorem A hold. Thus they hold for every fibred Montesinos knot when $`d\ne0`$; in particular they hold for every odd number of parallels with every orientation pattern. Fibredness does not remove the balanced multi-boundary problem.

**Theorem C (single-boundary criterion).** Suppose every connected oriented essential surface in $`E(K)`$ with nonempty purely longitudinal boundary has one boundary. For $`d=0`$, the two complexes strongly deformation retract onto the pure pattern-annular taut subcomplex. If, in addition, every incompressible Seifert surface of $`K`$ has genus $`g(K)`$, the same conclusion onto $`MS(L)`$ holds for all $`d`$.

The new work in Theorem A is the closure of the **rooted whole-system reflection structure** under the two construction operations. Boundary slopes and Euler characteristics alone would not prove it. Sections 3–7 establish that closure; Sections 8–9 give the contraction. Section 10 proves Theorem B independently of that reflection closure. Theorem C is the single-boundary part of the same argument.

## 2. Accepted inputs and efficient normal forms

For $`n\ge2`$, write

```math
E(L)=P\cup_T Q,
\qquad
P=S^1_\lambda\times B_n,
\qquad Q=E(K),
\qquad \Phi|_Q=d\psi,
```

where $`B_n`$ is a disk with $`n`$ actual holes and one companion boundary, $`\lambda`$ is the preferred longitude, and $`\psi(\mu_K)=1`$. The actual spanning slopes are $`\epsilon_i\lambda`$. There is no choice of an independent cover or additive constant on a companion component.

We use the following established inputs in their stated ranges.

- [The zero-framed cluster theorem](zero-framed-clusters.md): essential cutting, ordinary efficient comparison, the one-boundary circular envelope, and the rooted path-chamber closure. We reproduce the interfaces and the contraction below so that its new hypotheses can be checked.
- Part 7 §9, Theorem D: for every non-split link, $`X\subseteq Y`$ and there is a strong deformation retraction $`R_D:|Y|\to|X|`$. Its output on a geometric simplex recombines whole actual-bearing components. It exactly recovers every point of a cyclic simplex.
- Hatcher–Thurston, Theorem 1(b)–(e), Proposition 1, Proposition 2, and the sheet/fold proof, printed pp.227–230 and 242–245. These apply to the whole disconnected bounded essential system, not just to one Seifert surface.
- Hatcher, *Notes on Basic 3-Manifold Topology*, Lemma 1.11 and Proposition 1.12, printed pp.20–23: boundary incompressibility and the vertical/horizontal classification in a Seifert piece, including the horizontal product and Euler formula.
- Przytycki–Schultens, *Trans. AMS* 364 (2012), Theorem 1.1, printed p.1490, applied only to the endpoint after it has been identified as the taut cyclic complex.

No independently assumed Oertel 1984 theorem or Hatcher–Oertel completeness statement is an input to Theorems A–C. HT and PS retain their own published dependencies, including branched-surface results; this is not an assertion that their entire reference chains avoid Oertel.

### 2.1. Essential cutting and reconstruction

The structural tori of a construction of $`K`$ separate composing spaces, cable spaces, terminal torus exteriors, and terminal two-bridge exteriors. They are incompressible. All summands are nontrivial; a cable has winding at least two; adjacent composing blocks are merged. The usual amalgam normal form preserves the piece and boundary groups. Sphere cutting gives irreducibility. The same assertions hold after attaching $`P`$, so $`L`$ is non-split and there are no actual disk components.

Use a recursively efficient position, for an actual surface or a finite disjoint coloured family. First minimise intersection with the outer companion torus $`T`$. In each resulting companion subexterior minimise intersection with its immediate child tori, then continue inside those children, keeping the already fixed parent boundary. This is a finite parent-before-child sequence of integer minima. It ensures essentiality of the system in **every whole child exterior**, not just of the final terminal cut pieces.

At each stage, inessential intersection circles disappear by disk/ball moves. Cut-piece groups inject into the original surface group. A boundary-parallel cut annulus has both ends on a new internal torus; an innermost empty annular parallelism removes two intersections in that stage. One uses the finite union when choosing the innermost parallelism, so disjointness is retained. The move is inside the current child exterior and preserves previous boundaries. Hatcher's Lemma 1.11 makes every resulting piece boundary-incompressible. A closed cut piece would already be a closed whole component and is absent. Subsequent relative isotopies do not change these essentiality statements.

Conversely, compatible essential pieces glue incompressibly. An outermost intersection arc of a hypothetical compression disk with the gluing tori would boundary-compress a cut piece. Remove such arcs until the disk lies in one piece, contradicting incompressibility. This argument permits cycles and branching in the **surface assembly graph**.

A pattern piece reaching an actual torus has fibre-slope boundary and hence is vertical. If any piece reaches $`T`$, all traces on $`T`$ are longitudinal and the whole pattern union is verticalisable. If none reaches $`T`$, a nonempty companion assembly would be a forbidden closed whole component. Thus the pattern consists of actual annuli, reaching annuli and outer returns. Simultaneous verticalisation keeps the common boundary motion on both sides of $`T`$.

### 2.2. Ordinary comparison, not a marked-torus quotient

At the outer torus $`T`$ the slopes are already longitudinal, so the efficient comparison of [the zero-framed cluster proof](zero-framed-clusters.md) §2 and [the ordinary product-annulus comparison](assemblies.md) applies directly. **Internal slope agreement is not assumed.** Section 6.0 proves it for ordinarily isotopic companion systems by an invariant-tree argument, using the geometric normal forms of Sections 3–5. Those sections do not use ordinary profile invariance.

Once this agreement is known, disjoint parallel traces can be chosen on every structural torus, and the product-annulus comparison applies to the finite collection. In an empty product $`F\times I`$ between whole actual-bearing components, a whole incompressible torus cannot inject into the free group $`\pi_1(F)`$. Since its two boundary trace systems now have the same slope, its intersection with the product consists of essential annuli. An innermost returning annulus would cut off a boundary-parallel cut annulus; the remaining spanning annuli straighten to products. Taking an innermost return with respect to the whole finite collection gives the same argument at every torus. Product simplifications can consequently preserve the tori and the entire common boundary paths.

The cyclic bundle exception is absent for $`d=0`$, since the injected $`\mathbb Z^2=\pi_1(T)`$ is killed by $`\Phi`$, whereas a compact spanning fibre has free fundamental group. For $`d\ne0`$, Section 7 first proves that every companion piece has one boundary. Every global component then uses either one actual torus or two oppositely oriented actual tori. It cannot be a whole spanning fibre when $`n\ge2`$; in the two-torus annular case $`d`$ would be zero. The case $`n=1`$ is treated separately.

Together with Section 6.0 this makes the profiles, boundary incidences and retained-piece data below data of ordinary classes. We do not quotient by extra torus twists. The same comparison applies to a finite disjoint family; common whole components are handled by the packet convention of Theorem D.

### 2.3. Whole horizontal families in the Seifert blocks

The finite-system version of horizontalisation can be obtained by applying Hatcher's cutting proof to the entire disjoint union. A connected oriented horizontal component has a constant nonzero transverse sign against the regular fibre. Its relative class is nonzero and primitive, and the horizontal-product argument gives its cut complement as a product. A second horizontal component in that product projects as a finite covering of the first. The sheets have a linear order in each interval, preserved by monodromy; each connected covering therefore has degree one. Straightening gives a joint parallel family with all original orientation labels retained.

This also follows from the horizontal-product argument in [H3, p.23]. In the present planar blocks, common boundary slopes determine the primitive horizontal class up to sign, since rational first homology is generated by the regular fibre and boundary loops. A vertical annulus cannot coexist with this family: the horizontal pieces meet every port, where their boundary slopes are transverse. Thus the proof never separately normalises incompatible local representatives and subsequently assumes they are disjoint. The gap products used in Section 6 are gaps of this jointly normalised family.

## 3. Integer slopes and the local reflection data

On a knot boundary use slope $`r`$ for the primitive curve $`\lambda+r\mu`$ when $`r`$ is integral; in general slope $`a/b`$ denotes $`b\lambda+a\mu`$. The meridional slope is $`\infty`$. Only **finite** slopes occur in the following induction. Composite knot exteriors do have meridional decomposing annuli; they are not excluded by a false all-slopes assertion.

A *profile* records the modes at the active structural blocks, the finite slopes, and the HT carrier at each active two-bridge terminal block. A vertical cable mode stops before its child. It does not record plumbing weights, ordinary gluing twists or the isotopy classes of individual components. Those remain actual geometric data; surfaces with one profile need not be parallel or isotopic.

For a finite essential oriented system with $`N`$ boundary circles of one finite slope, list the circles in their cyclic order along a positive meridian. We shall prove the following alternative in each profile.

**Regular mode.** Every component has one boundary; the connectivity relation on the $`N`$ labels is equality. This mode occurs only at slope zero.

**Reflecting mode.** $`N`$ is even. The connectivity relation is generated by finitely many involutions

```math
i\longmapsto c_\nu-i\pmod N,
\qquad c_\nu\text{ odd}.
```

Each such identification reverses the boundary orientation sign. A specified local reflector also has a specified outside gap. Rooting there normalises its reflection to $`i\mapsto-1-i`$. Root choices are fixed by the profile, not chosen independently on different faces of a simplex.

This is a description of the actual boundary partition of an embedded normal system. It is not a claim that every list of abstract reflections is geometrically realisable. The proof needs coverage of existing systems, not a realisation theorem for arbitrary lists.

### 3.1. Two-bridge terminal blocks

HT Proposition 2 makes every boundary slope integral and every boundary circle longitudinally primitive. On a carrier $`\beta=[b_1,\ldots,b_s]`$, the $`N`$-sheeted system has $`N`$ boundary circles and

```math
\chi=-N(s-1).
```

If all coefficients are even, HT's proof of Proposition 1 gives exactly $`N`$ one-boundary components. Their genus is $`g(K)`$ and their slope is zero.

Otherwise use an odd band as root. In an ordered plumbing square the sheet matching is $`P_t(i)=t-1-i\pmod N`$; an even band has identity normal monodromy and an odd band has full reversal. Transporting the latter to the root gives $`i\mapsto c_\nu-i`$, with all constants odd when the system is orientable. These are the actual identifications in HT Figs.26 and 30–31; the rooted derivation is also in [rooted band heights](band-heights.md), §12.1. The derivation uses band parity and the ordered rectangles, not the numerical value of the boundary slope, so it applies to every finite-slope HT carrier.

Odd $`N`$ cannot give an oriented whole system: an odd-cardinality reflection has a fixed sheet, which would reverse its orientation. For even $`N`$, each transported odd-band loop reverses the orientation sign, as does the orientation double of the one-sheeted nonorientable plumbing. Restricting to whole components retains the actual sheets and rectangles on the same carrier.

HT Theorem 1(d)–(e) supplies whole-union purity and the complete bounded moves. All moves occur at coefficients $`\pm2`$ and can avoid the chosen odd root section. Root naturality under ordinary comparisons is checked in Section 6, including the nonzero-slope case. A carrier of length one is a torus-knot annular case and can alternatively be treated by the next subsection.

### 3.2. Torus terminal blocks

For $`T(a,b)`$, with $`a,|b|\ge2`$ coprime, the regular fibre is $`h=\lambda+ab\mu`$. An essential bounded system is either vertical or horizontal.

In the horizontal case all boundary circles of a connected component have the same orientation. The longitude kernel in $`H_1(\partial Q)\to H_1(Q)`$ forces slope zero. If there are $`k`$ boundaries, its relative class is $`\pm k`$ times the Seifert generator. A connected nonseparating proper oriented surface has primitive class, so $`k=1`$. The horizontal product gives the usual fibre genus $`(a-1)(|b|-1)/2`$. A disjoint system consists jointly of fibre copies.

A bounded vertical component is the essential annulus separating the two exceptional fibres, with slope $`ab`$. A finite disjoint system is a parallel annulus stack. Its boundary partition is the full reversal of an even stack. Choose the end adjacent to the exceptional fibre of order $`a`$. The orders $`a`$ and $`|b|`$ are distinct; an identity-starting comparison cannot exchange them. In group terms they are the indices of the central regular-fibre subgroup in the corresponding solid-torus core subgroups. Hence this is an ordinary root.

## 4. Closure under connected sum and cabling

We prove simultaneously that all finite boundary slopes are integral and that every finite oriented essential system has one of the two modes above. These assertions are needed for entire systems, not merely for a connected input.

### 4.1. Connected sums

Let $`K=K_1\#\cdots\#K_m`$, $`m\ge2`$. Its composing block is $`S^1_\mu\times B_m`$; the fibre is the common meridian, and the preferred longitudes satisfy $`\lambda_0=\lambda_1+\cdots+\lambda_m`$ in its first homology.

A finite outer slope is transverse to the meridian fibre. Thus the whole composing cut system is horizontal and meets every child port. Its child slopes are finite; a meridian boundary would be vertical and could not coexist with a horizontal piece. By induction the child slopes $`s_i`$ are integers.

For one connected horizontal piece let $`\eta`$ be its primitive dual class and orient it so that $`k=\eta(\mu)>0`$. At the $`i`$th port,

```math
\eta(\lambda_i)=-k s_i.
```

The fibre and child longitude classes generate the homology of the composing block. Therefore every value of $`\eta`$ is divisible by $`k`$, and primitivity forces $`k=1`$. The piece is a section, with one boundary on every port, and its outer slope is

```math
r=s_1+\cdots+s_m.
```

In a joint horizontal family, the $`N`$ sections have the same circular order on each port. Label the outer boundary circles by $`\mathbb Z/N`$. Each child port has these labels up to one cyclic shift. A child in regular mode identifies no different section labels. A reflecting child identifies labels by odd-constant reflections; a shift changes a constant by an even integer. The global connected components are exactly the orbits of the union of these identifications: the composing sections add the identifications between each outer label and its corresponding child labels, and nothing else.

If every child is regular, the output is regular, with slope zero. Otherwise there is at least one reflection and we are in reflecting mode. Orientation is preserved through a section and reversed by a child reflection. Odd $`N`$ is again impossible. Choose the first reflecting child in the fixed ordering and propagate its root through the section gaps. Section 6 proves this is an ordinary natural root.

For later use put $`t=-\chi/N`$ for the complexity per boundary in a profile. The section has Euler characteristic $`1-m`$, so

```math
t_K=(m-1)+\sum_{i=1}^m t_{K_i}.
```

This holds on each whole component as well, because a component with $`A`$ outer boundaries has $`A`$ section sheets at every port and hence $`A`$ child boundary sheets at every child.

### 4.2. Cable spaces: slopes and sheet counts

Let $`K`$ be the $`(p,q)`$ cable of $`J`$, and write $`E(K)=W\cup E(J)`$. In the free basis $`\mu_K,\lambda_J`$ for $`H_1(W)`$,

```math
[\mu_J]=p[\mu_K],\qquad [\lambda_K]=p[\lambda_J],
\qquad h_0=\lambda_K+pq\mu_K,
\qquad h_1=p\lambda_J+q\mu_J.
```

Suppose the outer finite slope is $`r=a/b`$. If the system is horizontal, every component meets both ports. If one has $`k`$ outer circles of slope $`a/b`$ and $`\ell`$ inner circles of slope $`c/e`$, the coherent oriented boundary relation in $`H_1(W)`$ gives

```math
kbp=\ell e,\qquad ka=\ell cp.
```

In particular $`e\ne0`$, and $`r=p^2s`$ with $`s=c/e`$. The child slope is finite, hence integral by induction. Thus $`r`$ is integral too.

The primitive dual of a horizontal component with $`k`$ outer boundaries has values

```math
\eta(\mu_K)=k,\qquad \eta(\lambda_J)=-kp s.
```

Primitivity gives $`k=1`$. The child port has exactly $`p`$ coherent boundary circles. Such a horizontal piece has Euler characteristic

```math
\chi(H)=-(p-1)|q-ps|.
```

Indeed its degree over the annular base orbifold is $`|pq-r|=p|q-ps|`$, and that orbifold has Euler characteristic $`1/p-1`$. The integer $`q-ps`$ is nonzero by coprimality.

### 4.3. Cable spaces: the two modes

In the horizontal case there are $`N`$ outer pieces and $`pN`$ inner trace circles. Number the latter by $`\mathbb Z/(pN)`$. The circles belonging to one horizontal piece have the same residue modulo $`N`$, because the primitive horizontal phase has degree one on an outer meridian and degree $`p`$ on an inner meridian. In cyclic order the inner word is consequently $`p`$ repetitions of the outer word, with a possible common shift.

If the child is regular, each child piece has one boundary and caps one inner circle. Every global component has one outer boundary. The result is regular and $`s=r=0`$.

If the child has reflections $`i\mapsto c_\nu-i`$ on $`\mathbb Z/(pN)`$, the connectivity relation before taking the outer boundary is generated by those reflections and by $`i\sim i+N`$. On the outer labels it is **exactly** the relation generated by

```math
j\longmapsto c_\nu-j\pmod N.
```

The identifications $`i\sim i+N`$ through a cable piece preserve boundary sign, whereas each child reflection reverses it. If $`N`$ were odd, a descended reflection would fix an outer label and reverse its sign, which is impossible for an oriented surface. Thus $`N`$ is even and the descended constants are odd. This proves reflecting closure, including cases in which several child components merge into one global component. It does not assume one child component per global piece.

The complexity density is

```math
t_K=(p-1)|q-ps|+p\,t_J.
```

This is componentwise, not just an average over the union: a global component with $`A`$ outer boundaries contains $`A`$ cable pieces and $`pA`$ child boundary sheets, and the inductive child density holds on every one of its child components.

Now suppose the cable-space system is vertical. Its outer slope is $`pq`$. A vertical annulus meeting the inner port would require slope $`q/p`$ in $`E(J)`$. This is a finite nonintegral slope, prohibited by the induction hypothesis. Hence every component is the essential returning cabling annulus, entirely in $`W`$. All are jointly parallel, with a reversal boundary partition and density zero. The end on the exceptional-fibre side is distinguished: that side is a solid torus, whereas the other side contains the nonabelian companion group. An ordinary comparison cannot exchange the sides.

There is no hidden horizontal system at slope $`pq`$: that would require $`s=q/p`$. There is also no horizontal/vertical mixture, since a horizontal piece meets every port and has transverse boundary there. This completes the induction for arbitrary finite construction depth.

## 5. What the reflections actually imply

Consider any reflecting profile at the outer boundary of a constructed knot exterior. Root so that $`c_1=-1`$. Put

```math
e=\gcd(N,c_2-c_1,\ldots,c_h-c_1),\qquad
q_0=e/2,\qquad A=2N/e.
```

For one reflection the gcd is $`N`$. Both $`N`$ and $`e`$ are even. Products of reflections generate translations through the differences $`c_\nu-c_1`$. Hence the orbits are the residue classes modulo $`e`$ paired by $`t\leftrightarrow e-1-t`$. There are $`q_0`$ components, each with $`A`$ boundary circles. Reading the meridian from the root gap gives

```math
(0,1,\ldots,q_0-1,q_0-1,\ldots,1,0)^{A/2}.
```

Each orbit contains equally many positively and negatively oriented boundaries: any generating reflection pairs opposite signs without fixed labels. Its relative class in the knot exterior is therefore zero. Each connected component separates.

The complement dual graph is connected and every edge is a bridge, so it is a tree. The first $`q_0`$ crossings of the displayed meridian word traverse every edge once without repetition. A nonrepeating edge walk in a tree is a path. As it already contains every edge, the entire graph is that path. Its two end chambers meet the boundary torus in $`A/2`$ annuli each; an interior chamber meets it in $`A`$ annuli. There are no additional hidden chambers away from the boundary.

This proves a statement about **complementary regions**, not about products. Different components may have different ordinary HT data or different gluing data. Their intervening chamber need not be a product. Their surface assembly graph inside the construction tree can also have cycles; no graph-cycle deletion is used.

In regular mode the components are nonseparating one-boundary surfaces. The dual graph has no bridge. Collapsing onto it gives a surjection on first homology from $`H_1(Q)=\mathbb Z`$, so its Betti number is at most one. It is therefore a circle, oriented consistently by the positive Seifert class. Again its chambers need not be products.

### 5.1. Genus and the zero-slope dichotomy

All profile densities are nonnegative. At a sum node $`t\ge m-1\ge1`$; at a horizontal cable node $`t\ge(p-1)|q-ps|\ge1`$. A reflecting zero-slope terminal HT carrier has even length at least two, so its density is at least one. A terminal torus or vertical cable annulus has nonzero slope and cannot itself be a zero-slope exception.

Consequently every reflecting zero-slope component satisfies

```math
\chi=-A t,\qquad
g=1+\frac A2(t-1)\ge1.
```

All one-boundary components are regular. Their genera obey

```math
g(K_1\#\cdots\#K_m)=\sum_i g(K_i),
\qquad
g(C_{p,q}(J))=p\,g(J)+\frac{(p-1)(|q|-1)}2.
```

Here the formulas can be deduced without assuming a genus theorem: the local Euler computations give the displayed value for **every** incompressible one-boundary surface; a least-genus Seifert surface exists and is incompressible, so that value is $`g(K)`$. At terminal blocks the value is supplied by HT or the torus horizontal computation. Thus every incompressible Seifert surface of every $`K\in\mathcal C`$ is taut.

## 6. Ordinary roots and naturality

This section supplies the information not supplied by orbit counting. It is essential for the deformation, not an optional choice of coordinates.

### 6.0. Internal slopes are ordinary invariants

Here the input is the geometric classification of recursively efficient systems in Sections 3–5, before any ordinary profile assertion. Let $`R`$ be a connected essential component in a constructed knot exterior $`Q`$, with finite outer slope, and let $`\mathcal T`$ be its structural torus collection.

First, no circle of $`R\cap\mathcal T`$ is parallel to $`\partial R`$ on $`R`$. Otherwise choose the first such circle from the outer boundary along the annulus it cuts off. The cut piece adjacent to the outer boundary would be an annulus. At a composing root every outer piece is a section of Euler characteristic $`1-m<0`$. At a horizontal cable root every outer piece has Euler characteristic $`-(p-1)|q-ps|<0`$. At a vertical cable root the whole component is an annulus avoiding its child. A terminal root has no structural torus. These are exhaustive and exclude the proposed first circle. The cut curves are also essential on $`R`$, by essential cutting.

We recall and prove the needed elementary tree fact. Let $`\mathscr B`$ be the tree of lifts of the cut pieces of $`Q`$ in its universal cover, with an edge for every lifted structural torus. This is the Bass–Serre tree of the torus splitting; the amalgam normal form constructs it. Let $`\mathscr D_R`$ be the tree dual to the lifts of the cut curves in the universal cover of $`R`$. The surface injection gives an $`H=\pi_1(R)`$-equivariant map

```math
\mathscr D_R\longrightarrow\mathscr B.
```

This map has no fold. Two distinct edges incident to one lifted surface piece could map to the same lifted boundary torus only if an arc in that surface piece, between their boundary lines, were homotopic relative its endpoints into that torus. Boundary incompressibility, in its relative fundamental-group form, forces such an arc to be homotopic into one boundary component of the surface piece. Lifting that homotopy puts both endpoints on the same boundary line, contrary to the two distinct incident edges. Thus the map is locally injective; a locally injective map between trees is injective.

If there are cut curves, the $`H`$-action on $`\mathscr D_R`$ is minimal and nonelliptic. To see this without an additional surface classification, suppress annular cut regions between parallel cut curves. Every remaining edge group is a proper cyclic subgroup of its incident surface vertex groups: an annular terminal region would make a cut curve boundary-parallel, already excluded. In this reduced surface splitting one can choose elements on the two sides outside the edge subgroup; their alternating word has an axis through the edge. A nonseparating cut is treated by its crossing stable letter. Restoring annular subdivisions leaves each subdivided edge on that same axis. Consequently every edge is in an axis of an element of $`H`$, and the whole tree is its minimal invariant subtree.

Its embedded image in $`\mathscr B`$ is therefore the unique minimal $`H`$-subtree. If there are no cut curves, $`H`$ fixes a vertex, and no other efficient representative of the same subgroup can instead have a nonelliptic minimal tree. The whole-annulus cases cause no exception: the nonpositive Euler counts above force every efficient annular representative to avoid all structural tori.

Ordinarily isotopic surfaces give conjugate subgroups with the same induced action. Their minimal subtrees are translates. The quotient edge orbits, their structural-torus labels and their cyclic stabilizers are consequently intrinsic. A stabilizer is precisely the subgroup generated by a trace circle, because the surface tree embeds. The trace is primitive in the torus group, so that cyclic subgroup determines its unoriented slope. Deck translation preserves the peripheral coordinates on each named torus. Thus the trace count and slope on every internal torus agree for two ordinary efficient representatives.

For a disconnected system apply this argument to its matched whole components. First use the already justified outer-$`T`$ comparison to match the companion systems of isotopic spanning vertices; then the argument above gives internal slope agreement. Now the finite torus-preserving product comparison of Section 2.2 applies, rather than being used to assume its own slope hypothesis. It carries the entire local systems through isotopies. HT's complete classification and the Seifert mode descriptions then make the profile ordinary. This closes the possible circularity between normalisation, internal slopes and ordinary profiles.

### 6.1. The return obstruction at an HT root

The no-return argument of [the zero-framed cluster proof](zero-framed-clusters.md) Lemma 4.1 has the following coordinate-independent form. Let $`F`$ be a connected essential separating positive-genus surface in a knot exterior, with nonempty boundary of **integral** slope $`\lambda+r\mu`$. An identity-starting return fixing its boundary circles individually has zero winding transverse to that slope. A return of a finite such system has no nontrivial cyclic boundary permutation.

For completeness, use a product pattern whose fibre is $`f=\lambda+r\mu`$, and attach a reaching annulus from each boundary of $`F`$ to a distinct labelled parallel. The signs supplied by separation sum to zero. The attached surface is a connected essential spanning surface. On an actual boundary its fibre is the spanning slope: the other components have total sign $`-\epsilon_i`$, so the linking contribution $`-r\epsilon_i`$ is cancelled by the $`r\mu_i`$ term. This auxiliary construction uses only essential assembly and ordinary product comparison; it invokes no contraction theorem for nonzero framing.

A return of transverse winding $`m`$ would identify this assembly with its $`m`$-fold outer-twisted version. Compare two copies of $`F`$ at distinct levels of a single collar. A horizontal product portion in the companion has an entire $`F`$ as face: it cannot end in the interior of $`F`$, and there is no actual boundary in that companion. The two copies separate the exterior into three chambers; only their middle slab has both copies on its frontier. The single-outer-torus product simplification of Section 2.2 can therefore keep all such pushes in that slab; the two traces already have the same slope, and no internal-torus normalisation is used in this auxiliary argument. Nonfinal pushes end at distinct nearby levels, preserving the confinement. Boundary tracks remain in their original proper transverse strips.

The confined comparison has transverse winding zero. In the pattern base, a reaching tether detects the remaining outer twist: its relative homology change is $`m[b_0]`$, nonzero modulo the chosen actual boundary unless $`m=0`$. There is another actual hole because a separating oriented surface has at least two boundaries. This is precisely the full-face and middle-slab argument of [the zero-framed cluster proof](zero-framed-clusters.md), in the basis $`(f,\mu)`$ instead of $`(\lambda,\mu)`$.

For a system return, take a finite power fixing all pieces, orientations and boundary circles. A nontrivial cyclic permutation of the ordered boundary configuration would then give nonzero integral transverse winding; the preceding argument excludes it. No independent winding is discarded by a quotient.

For an odd HT carrier of length at least two, each oriented connected component has positive genus. All complete HT moves avoid the odd root section. Restricting sheets and plumbing rectangles preserves that outside gap. If two normalisations gave different transported ends, their root-preserving HT comparison, combined with the two normalising paths, would give a prohibited return of the boundary configuration. Hence the root is an ordinary natural end. The length-one annular case is covered by the distinguished torus-knot side in Section 3.2.

### 6.2. Propagating a root through the construction

At a composing node a complementary gap between consecutive sections meets each port in exactly one annulus. Thus a rooted child gap determines an outer gap with no choice. At a horizontal cable node a gap meets the outer port in one annulus and the inner port in $`p`$ annuli; each inner gap annulus still determines a unique outer gap. These are actual complementary-region incidences in the cut Seifert block, not a chosen phase equality.

Choose the first reflecting child at a sum node, and the reflecting child at a horizontal cable node. At a vertical cable or terminal torus node use its distinguished side. This recursively specifies a root from the profile.

Several annuli can represent one child end when its boundary arity exceeds two. They all reach the **same** global end. In root coordinates their gaps have index $`-1`$ modulo the child's divisor. Adding other child reflections, or passing from $`pN`$ labels to $`N`$ labels in a cable, replaces that divisor by a divisor of it. The gaps therefore remain $`-1`$ modulo the global divisor. Section 5 identifies precisely this residue with the same global end. Thus the construction does not choose different ends through different occurrences of one child chamber.

An ordinary efficient comparison preserves the structural blocks, their modes, child slopes and HT carriers. At the selected root node its end is preserved by Section 6.1 or by the distinguished annular side. The unique gap propagation then preserves the outer root. Tangential boundary motion and gluing twists remain part of the comparison; they do not identify distinct ordinary vertices. Any alleged residual transverse boundary circuit at the outer zero-slope separating system is also ruled out by the original [the zero-framed cluster proof](zero-framed-clusters.md) no-return lemma.

### 6.3. Subsystems and colours

Retain a nonempty collection of whole global companion components. At every active child it retains whole child components and their actual sheets: a horizontal section visits every child port, and a horizontal cable piece visits its child $`p`$ times. No active child disappears while an outer component remains. HT restrictions retain the carrier; vertical annulus restrictions retain the distinguished side. Hence the profile is unchanged.

The retained sheet set is invariant under every reflection. At the selected root, its ordered compression preserves the reversal and the outside gap. Gap propagation through a section or a cable commutes with this restriction. The resulting outer path order is exactly the induced order of the retained components; it is not a newly normalised order of individually chosen representatives.

These statements hold for the whole finite coloured union. Deleting a colour simply deletes its sheets and rectangles. Shared whole actual-bearing components are first treated as the parallel packets of Theorem D; exact phase recovery restores their coloured occurrences in the nested potential order, reversing this order at a negatively oriented companion occurrence. This is the same whole-component convention as [the zero-framed cluster proof](zero-framed-clusters.md) §4. It yields a realisable, face-compatible coloured order without inserting a product between distinct companion types.

Sections 6.1–6.3 prove ordinary root invariance, subsystem naturality and coloured naturality separately. Orbit arithmetic alone proves none of these ordinary statements.

## 7. Complete companion sectors for the parallel link

Apply the preceding results to the efficient longitudinal companion system of a spanning surface of $`L`$.

In regular mode all pieces have one boundary and genus $`g(K)`$. In reflecting mode every piece has the same positive even boundary count, separates $`Q`$, and has positive genus. Its entire relative class is zero. Thus $`d\ne0`$ forces regular mode.

If two nonannular vertices are geometrically disjoint, normalise their whole union simultaneously. At each active Seifert block it has one common mode and horizontal class; at each HT terminal it has one carrier. The same profile restricts to both vertices. In reflecting mode Section 5 gives one common boundary arity $`A`$ to all components of the union. There can therefore be no edge between different nonempty profiles, between different arities in one reflecting profile, or between regular and reflecting vertices. Theorem D gives the same exclusion for cyclic edges.

Let $`A_X`$ be the pure pattern-annular cyclic subcomplex. For $`d=0`$, every simplex of $`X`$ lies either in the regular subcomplex or in one reflecting sector $`(\mathfrak p,A)`$, and the intersections of different such subcomplexes are exactly $`A_X`$. A nonexistent profile contributes nothing. Flagness promotes the pairwise exclusion to the entire simplex assertion.

No component-isotopy catalogue is claimed. Two vertices with the same profile, arity and component count can still have different ordinary gluing data and different HT types. They are all retained in their sector.

## 8. The single-boundary deformation

This proves Theorem C and treats the regular part of Theorem A. Reverse orientations if necessary so $`d\ge0`$.

For a cyclic simplex use the collapsed whole-component bands and the one global $`\Phi`$-cover of Theorem D. A barycentric point $`x=\sum_i t_i[v_i]`$ has the equivariant real band map $`F_x=\sum_i t_iF_i`$. On the companion, the ordered one-boundary pieces have a circular chamber graph. On its lifted circle the restriction factors as a function $`f_x(u)`$ satisfying

```math
f_x(u+1)=f_x(u)+d.
```

Define the record envelope

```math
m_x(u)=\sup_{v\le u}f_x(v),
\qquad
f_{x,s}=(1-s)f_x+s m_x.
```

For $`d>0`$, the supremum is the maximum over the last period $`[u-1,u]`$. It is continuous, nondecreasing and has degree $`d`$. For $`d=0`$ it is the constant circular maximum. A positive old band is clipped from below by a preceding record; on a negative band the record is constant. The interpolation never reverses a band.

The difference $`m_x-f_x`$ is periodic and descends to one real function on $`Q`$. Extend it across a fixed pattern collar by a cutoff that is one at $`T`$ and zero at the far edge; leave the actual boundaries fixed. This is a change to the one global equivariant map, also when the restricted cover of $`Q`$ has $`|d|>1`$ components. It chooses no new local deck constants.

A generic companion level is a collection of whole parallel copies of the original one-boundary pieces. A generic pattern level is vertical annuli and closed vertical tori. Delete whole closed components. Any outer return has capped the only boundaries of two companion pieces and is already part of a whole closed component; it cannot remain on an actual-bearing component. What remains is either a single original companion piece with a reaching annulus, or an actual-to-actual annulus. These pieces are essential, and assembly proves the output incompressible. Every actual torus is still used once by the monotone unit boundary map.

Average the ordinary reduced level classes over generic phases. At fixed parameters the levels are simultaneously disjoint, giving a point $`\Theta_s(x)\in|Y|`$. Set $`H_E(x,s)=R_D(\Theta_s(x))`$. No assertion that closed-component deletion preserves cyclic adjacency is needed.

On a fixed closed simplex cylinder there is a finite band-and-collar template and finitely many critical phase functions. Phase-interval lengths vary continuously, and a new ordinary level type appears with zero interval length. Circle reparametrisation, common translation of lifts and deletion of zero-weight bands do not change the construction. A shared whole component has one companion sign, so splitting its packet only subdivides consecutive monotone subbands and leaves the envelope and interval lengths unchanged. Ordinary efficient comparison transports the whole template. These facts give ordinary well-definedness, face agreement and finite-image CW continuity, exactly as in [the zero-framed cluster proof](zero-framed-clusters.md) §§5–6.

Exact recovery on cyclic simplices gives $`H_E(x,0)=x`$. If $`d=0`$, the final companion function is constant and all generic outputs are annular. Annular inputs have zero correction throughout. If $`d>0`$, the endpoint uses precisely $`d`$ positive companion pieces. A simplex whose cuts were already all positive is fixed throughout.

When every one-boundary piece has genus $`g(K)`$, a vertex with $`r`$ pieces has

```math
\chi_-=r(2g(K)-1),\qquad r\ge |d|.
```

Equality in the count occurs exactly for coherent signs. It is realised by $`|d|`$ positive minimal Seifert copies, pairing the remaining positive and negative actual holes by planar annuli. A norm-minimising spanning representative can be made essential by compression and removal of closed components, so the lower bound on essential representatives computes the norm minimum. Thus the coherent endpoint is exactly $`MS(L)`$. For $`d=0`$ under the single-boundary hypothesis, all nonempty companion pieces have negative Euler characteristic, so the annular endpoint is exactly the norm-zero taut subcomplex even without equal genera.

For $`K\in\mathcal C`$, Section 5.1 supplies the required genus statement. For $`d\ne0`$, Section 7 makes this regular subcomplex all of $`X`$.

## 9. The reflecting sectors and the global retraction

We detail the path-chamber transfer to show precisely what has been imported from [the zero-framed cluster proof](zero-framed-clusters.md). Fix a reflecting sector and its ordinary root end. For an efficient vertex $`S`$, order its $`q_0`$ companion pieces from that end. Choose the normal side containing the root end. The original chambers whose every surface face is on that side are the seed end chamber and the appropriate opposite-sign consecutive chambers, possibly also the far end. Their incident-piece sets are pairwise disjoint.

Resolve one such chamber by replacing its incident whole companion pieces with the annuli in its $`T`$-boundary, pushed into the pattern. Retain every other companion piece as a small copy of the original. This is a replacement using boundary collars, not an isotopy through a possibly nonproduct chamber. The annular caps have the correct orientation because all the chamber's faces are on the chosen side.

The raw pattern composition can have an outer return cutting off an empty disk. An original essential pattern arc cannot enter that disk: it cannot cross the new return, terminate at an actual hole inside it, or be an original empty return. Thus the boundary interval of the disk contains no original trace point. The new endpoints lie in one original boundary gap. By the repeated path word from Section 5, that gap uniquely identifies either a neighbouring-pair chamber or an end chamber, with all its incident pieces still present on the chosen side. Resolve that original chamber too.

There are no other repairs. Different one-sided original chambers use disjoint whole-piece sets. Resolving one does not change another's already complete witnessing pattern path, so enabling is monotone. Starting with the root end gives a unique least closed selected set in this finite collection. Do not delete a closed component containing companion pieces before the closure terminates; otherwise an original witness could be hidden. At termination there is no boundary-parallel return. All retained pieces are original essential pieces, and reconstruction proves every actual-bearing component incompressible. Delete whole closed components now. The resulting ordinary parent $`p(S)`$ has strictly fewer companion pieces.

The root and the original chamber list are ordinary and natural by Section 6. Hence this is a parent of an ordinary vertex, not a choice of maximal compression. Moreover, if its seed is first in a finite coloured family's root order, the operation is disjoint from that whole family. The same empty-disk argument excludes every other colour's trace; uniform arity and the repeated path word make every intermediate companion piece visible in the relevant interval. Thus the repair chamber is empty of other colours. Surviving pieces retain their relative positions.

Iterate $`p`$ to obtain a finite trajectory from every vertex to an annular vertex. Its event labels, the first retained pieces in the original root order, strictly increase. In a cyclic simplex merge these trajectories in the natural coloured order. At every event the next seed is first in the whole current family, so all current states and each pair of consecutive states have simultaneous disjoint representatives. Put all stationary annular events after the genuine events, in the restriction of one fixed total order on annular vertices. This order restricts to the same order after deleting any vertex.

For a nonstationary trajectory of length $`\ell>0`$, put its states at heights $`j/\ell`$ above that vertex. For an annular input use a stationary event at heights $`0`$ and $`1`$, with the same annular vertex as both images. Each event raises one vertex height; the slab between consecutive affine height graphs is the simplex on the old states and the new state. The slabs tile the simplex cylinder. Deleting a vertex deletes its zero-thickness slabs and preserves the order and heights of the other events. Mapping state points to their ordinary vertices gives a face-compatible homotopy from the cyclic sector into the geometric sector, ending in annuli and fixing annular inputs.

Compose with $`R_D`$. Its whole-component recombination retains the original companion profiles and boundary arities, so it stays in the sector. This gives a strong deformation retraction of that cyclic sector onto $`A_X`$. Each closed simplex cylinder has finite image; the weak/CW cylinder criterion gives continuity with no uniform bound on genus or number of pieces.

For $`d=0`$, these homotopies and the regular envelope agree pointwise on $`A_X`$. Section 7 says every simplex is in one sector, so they glue to a strong deformation retraction of all $`X`$ onto $`A_X`$. Every reflecting companion piece has positive genus and negative Euler characteristic by Section 5.1; therefore a vertex has norm zero exactly when it is pure annular. Hence $`A_X=MS(L)`$.

For $`n=1`$, every spanning surface has one boundary and is regular, so $`X=MS(K)`$. For $`d<0`$, reverse all orientations. The hypotheses of the PS theorem hold for the non-split link exterior; the boundary curves do not separate their individual tori, and $`H_2(E(L))\to H_2(E(L),\partial E(L))`$ is zero. Thus the identified endpoint is contractible.

Finally concatenate the given strong deformation $`H_D`$ from $`Y`$ to $`X`$ with the constructed $`H_X`$:

```math
H_Y(y,t)=
\begin{cases}
H_D(y,2t),&0\le t\le1/2,\\ 
H_X(R_D(y),2t-1),&1/2\le t\le1.
\end{cases}
```

It fixes $`MS(L)`$ throughout. This proves Theorem A and completes Theorem C.

## 10. Arbitrary fibred knots when $`d\ne0`$

The following argument does not use the construction class.

**Product lemma.** Let $`F`$ be a compact connected orientable surface with one boundary, and let $`S\subset F\times\mathbb R`$ be a compact connected incompressible surface whose nonempty boundary consists of essential circles on $`\partial F\times\mathbb R`$. Suppose $`S`$ is boundary-incompressible relative to this vertical boundary. Then $`S`$ is isotopic to a horizontal copy of $`F`$.

**Proof.** Enclose $`S`$ in $`F\times[a,b]`$ and make its boundary horizontal on the vertical annulus. Choose disjoint proper arcs cutting $`F`$ to a disk and use their product disks. Remove intersection circles by incompressibility and the usual innermost disk moves. An outermost intersection arc with both ends on one vertical side would boundary-compress $`S`$, or give a boundary-parallel arc that is removed. Thus the surviving intersections span each product disk from one vertical side to the other. After cutting, the surface in a ball consists of disks, and these span in their linear order. Regluing gives a finite horizontal covering of $`F`$. Its sheets have an order in every interval, preserved by all gluings. A connected ordered finite covering has degree one. Straightening the disks and product rectangles gives the stated isotopy. ∎

Let $`Q=E(K)`$ fibre over the circle with connected one-boundary fibre $`F`$ and knot class $`\psi`$. Let $`\mathcal R=R_0\sqcup\cdots\sqcup R_m`$ be a finite essential oriented longitudinal system with nonzero total relative class. Since $`H_2(Q,\partial Q;\mathbb Z)\cong\mathbb Z`$, some component, relabelled $`R_0`$, has nonzero relative class. It is connected, two-sided and nonseparating. Closing a once-crossing arc in its connected complement proves primitivity, so

```math
[R_0]=\pm[F],\qquad \mathrm{PD}[R_0]=\pm\psi.
```

For $`j\ne0`$, every closed loop $`\gamma\subset R_j`$ is disjoint from $`R_0`$. Its intersection with $`R_0`$ is zero. For a loop on $`R_0`$ itself, a normal push-off gives the same conclusion. Hence

```math
\psi|_{\pi_1(R_j)}=0\quad\text{for every }j.
```

The covering-space lifting criterion therefore gives a homeomorphic compact lift of **every** $`R_j`$ to $`F\times\mathbb R`$. Incompressibility lifts. Boundary incompressibility lifts by the relative fundamental-group injection [H3, p.19]; no projected compression disk is assumed embedded. Apply the product lemma separately to each compact lift. It has one boundary and is homeomorphic to $`F`$, and the lift restricts homeomorphically to $`R_j`$. Thus each original $`R_j`$ has one boundary and genus $`g(F)`$. Only topological type is read from the lift; no covering-space isotopy is descended.

For completeness, the product lemma's disk argument can be made explicit. Put its $`k`$ boundary circles at distinct heights on the vertical annulus. Every product cutting disk then has $`k`$ endpoints on each of its vertical sides. After removing circles and returning arcs, disjointness forces the $`i`$th endpoint on one side to join the $`i`$th endpoint on the other. Straighten these arcs. The cut ambient manifold is a ball and the cut surface pieces remain fundamental-group injective, so they are disks. Their boundaries are the cut versions of the $`k`$ horizontal boundary circles. Straighten the disks relative boundary and glue back to obtain $`k`$ horizontal copies. Connectedness forces $`k=1`$. This argument takes place entirely in the cover and requires no deck-equivariant isotopy.

Also $`g(F)=g(K)`$ follows from this lemma: a least-genus Seifert surface $`G`$ is incompressible and boundary-incompressible, has class $`\pm[F]`$, and compactly lifts by the same self-intersection argument. Its lift is homeomorphic to $`F`$, so $`g(G)=g(F)`$.

For the parallel link with $`d\ne0`$, the companion union has total class $`d[F]`$ and therefore consists only of one-boundary minimal-genus pieces, retaining all original signs. The circular-envelope proof in Section 8 applies to the entire complex and proves Theorem B. When $`n=1`$, every vertex is already taut: use the identity homotopy on $`X=MS(K)`$ and the comparison from $`Y`$ to $`X`$. No single-vertex assertion is needed.

For $`d=0`$ this argument gives only the regular-sector retraction. A separating longitudinal component has zero relative class, so the implication $`\psi|_{\pi_1(R)}=0`$ is unavailable. Indeed the fibred two-bridge example $`K_{29/137}`$ in [the zero-framed cluster proof](zero-framed-clusters.md) §12 has essential multi-boundary, nonparallel odd pieces. We do not extrapolate Theorem B to all balanced fibred companions.

## 11. Concrete scope and the Montesinos obstruction

### 11.1. Explicit covered ranges

- $`K=5_2\#5_2`$, or any finite connected sum of nontrivial two-bridge knots, is covered for every number and orientation of zero-framed parallels. For mixed handedness the reflecting cancellation sectors are retained; no common-sign shortcut is needed.
- Every finite iterated cable of $`5_2`$ is covered, and so is a connected sum of such cables with two-bridge or torus knots followed by further cabling. The exterior contains a hyperbolic two-bridge terminal piece, so this is not a pure graph-manifold theorem. For example $`C_{2,3}(5_2)`$ has genus $`3`$; a cluster with $`d=1`$ has taut norm $`5`$, whereas a balanced cluster has taut norm zero.
- The connected-sum genus and the cabling genus in Section 5.1 compute the taut endpoint explicitly. They do not bound the genus of all spanning vertices: reflecting pieces and repeated cancellation can have arbitrarily large complexity.
- Theorem B includes every fibred Montesinos knot with nonzero orientation sum, without requiring a Montesinos surface classification or restricting the number of rational tangles.

The class $`\mathcal C`$ is a construction class, not a claim that every knot with a given JSJ graph belongs to it. The theorem asserts full closure under arbitrary finite sums and cables with two-bridge or torus terminals, together with Theorem B's arbitrary fibred-companion statement. No exhaustive priority claim is made.

### 11.2. Why the full Montesinos claim is still open here

Oertel's 1984 articles *Closed incompressible surfaces in complements of star links* and *Incompressible branched surfaces* are bibliographic context, not independently checked classification inputs here. A closed-surface title does not supply an all-bounded-system classification. Hatcher–Oertel's boundary-slope algorithm is a possible source of Montesinos candidates; no completeness or isotopy theorem from it is invoked. The precise source boundary is recorded in [the bibliography](../sources/bibliography.md).

Even a verified list of all zero-slope candidates would leave the following exact propositions to prove for the desired Montesinos subclass:

1. Every oriented longitudinal nonzero-class component is a one-boundary taut Seifert surface, or there is another safe reduction for such components.
2. An entire disjoint bounded system admits a common normal description, with its actual component partition and oriented boundary signs retained.
3. Every remaining system has a chamber structure supporting exhaustive repair. The proof here needs a path, uniform arity and its repeated boundary word; an arbitrary branching tree is insufficient.
4. A root or a replacement for it is invariant under ordinary isotopy, including all port returns and full gluing twists, and is natural under deletion of colours.
5. The resulting sectors cover the whole complex and glue compatibly. Separate contractibility of selected carriers is not enough.

In a branched chamber, an empty return can see two negative faces while further faces have the other sign. It then does not certify a whole one-sided chamber that can be capped. This is the precise failure of transplanting Section 9 from a path to a general tree. It is an obstruction to this proof, not a noncontractibility example.

For example, the abstract port word $`AABBCC`$ gives a three-edge star: each doubled letter visits one leaf and returns to the central chamber. A gap between the $`A`$ and $`B`$ visits sees the central chamber, but does not see its $`C`$ face. If the first two faces are on the chosen side and the third is not, the gap test does not supply a legal whole-chamber cap. This is a boundary-incidence counterexample to the proposed *inference*; no claim is made here that this exact star has been realised by essential surfaces in a particular Montesinos exterior. A different repair method could still succeed.

The hypothesis “all incompressible Seifert surfaces are taut” concerns only one boundary. [K05]’s classification of prime knots through ten crossings, for example, supplies that information but does not supply items 2–5 for their multi-boundary surfaces. Nor does fibredness do so in the balanced case. Thus neither all three-tangle Montesinos knots nor all prime alternating/arborescent knots are asserted to satisfy Theorem A.

## 12. Sources and exact diagnostics

The editions and ranges are [HT, H3, PS, B and CW](../sources/bibliography.md). HT pp.227–230,241–245 supply whole bounded systems, complete moves, integral slopes and actual folds. H3 p.19 supplies the relative fundamental-group criterion used in §§6.0 and 10; pp.20–23 supply essential Seifert pieces, horizontal products and Euler characteristics. PS Theorem 1.1 is used only on the identified taut cyclic endpoint. The general comparison is [CW, Part 7, Theorem D].

The author's `scripts/check_recursive_systems.py` expands signed socket graphs and checks reflection orbits, whole-component deletion, sums, cables and propagated root gaps. The independent `scripts/check_recursive_independent.py` builds actual HT rectangles and local pieces before the quotient, including alternating sums and cables and opposite internal slopes. These are finite arithmetic diagnostics, not proofs of the product lemma, isotopy, essentiality, classification completeness or CW continuity. See [the computation guide](../scripts/README.md).
