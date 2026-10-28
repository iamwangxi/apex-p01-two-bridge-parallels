# Framed recursive parallels and balanced doubles of fibred knots

[Contents](../README.md) · [Main theorem](main-theorem.md) · [Scope](scope.md) · [Sources](../sources/bibliography.md)

## 1. Results and exact scope

The recursive class defined below admits **every integer framing**, with no restriction on the number or orientations of the actual components. For an **arbitrary fibred knot**, the balanced case is proved here for **two oppositely oriented parallels**, again at every integer framing. Arbitrary balanced clusters of four or more parallels of arbitrary fibred knots remain outside the unconditional conclusion, except in the subclasses specified below. For those clusters we give an exact reduction to their separating-companion subcomplex.

Let $`\mathcal C`$ be the smallest class containing the nontrivial two-bridge knots and the nontrivial torus knots, including mirrors, and closed under finite connected sums and cables

```math
C_{p,q}(J),\qquad p\geq 2,\quad q\neq 0,\quad \gcd(p,q)=1.
```

The winding number is $`p`$; the cable on the child boundary is $`p\lambda_J+q\mu_J`$. Only finite constructions are allowed.

For a nontrivial knot $`K`$, write

```math
L=L_f(K;\epsilon_1,\ldots,\epsilon_n),\qquad
f\in\mathbb Z,\quad \epsilon_i\in\{+1,-1\},\quad
d=\sum_i\epsilon_i.
```

These are labelled winding-one parallels of slope $`\lambda+f\mu`$ in the actual tubular neighbourhood of $`K`$. Coherently referenced components have pairwise linking number $`f`$. The framing of the parallel pattern is distinct from any cabling operation used to construct $`K`$.

Throughout, vertices are ordinary ambient-isotopy classes of oriented, componentwise incompressible spanning systems, with one prescribed oriented boundary on every actual torus and no closed components. Disconnected surfaces and all genera are included. Boundaries may move on their labelled tori; isotopies start at the identity.

Let $`X(L)`$ be the flag complex of class-minimum whole-open-complement cyclic width one for the single total linking homomorphism $`\Phi`$. Let $`Y(L)`$ be the complex of simultaneous geometric disjointness on exactly the same vertex set. Let $`MS(L)\subseteq X(L)`$ be the **taut cyclic** complex, with the Przytycki–Schultens convention. All realizations have the weak/CW topology. The notation $`\searrow`$ below means a strong deformation retraction.

**Theorem A (all framed recursive parallels).** If $`K\in\mathcal C`$, then, for every $`n,\epsilon,f`$,

```math
|Y(L)|\searrow |X(L)|\searrow |MS(L)|.
```

In particular both complexes are contractible. More precisely:

**(1)** If $`fd\neq0`$, every vertex is connected and taut, and

```math
X(L)=Y(L)=MS(L),\qquad
\chi(S)=|d|(1-2g(K))-|fd|(n-1).
```

**(2)** If $`d=0`$, except for the annular root modes in item 3, the endpoint is the pure pattern-annular cyclic subcomplex $`\mathcal A_X`$, and $`\mathcal A_X=MS(L)`$.

**(3)** If $`d=0`$ and the top construction block is a torus exterior $`E(T(a,b))`$ with $`f=ab`$, or a cable space of $`C_{p,q}(J)`$ with $`f=pq`$, every vertex is annular. Here $`X(L)=MS(L)`$; the taut subcomplex is not artificially restricted to annuli missing the companion.

The $`f=0`$ part is proved in [the recursive proof](recursive-and-fibred.md). Theorem A extends it to all $`f\neq0`$, including arbitrary alternations of sum and cable operations and nonparallel HT pieces inside horizontal cable systems.

**Theorem B (balanced doubles of arbitrary fibred knots).** For every nontrivial fibred knot $`K`$ and every integer $`f`$,

```math
|Y(L_f(K;+1,-1))|\searrow
|X(L_f(K;+1,-1))|\searrow
|MS(L_f(K;+1,-1))|.
```

For $`f=0`$, $`MS(L)`$ is the single standard annulus vertex. The proof uses a connected-surface exchange argument with a compression barrier; it does not classify the separating longitudinal surfaces of $`K`$, assume they are parallel, or assume that their complementary chambers form a path.

For $`f\neq0`$, the link is linking-indecomposable, and the already proved linking-indecomposable theorem [C, Theorem D] applies. Section 9 proves the zero-framed double using the barrier exchange lemma.

**Theorem C (exact reduction for arbitrary balanced fibred clusters).** Let $`K`$ be any nontrivial fibred knot, $`f=0`$, and $`d=0`$. Let $`X_{\mathrm{sep}}`$ be the induced cyclic subcomplex on the vertices whose efficient companion cut is empty or has only separating components. Let $`Y_{\mathrm{sep}}`$ have the same vertices with geometric simplices. Then

```math
MS(L)=\mathcal A_X,\qquad
|X(L)|\searrow |X_{\mathrm{sep}}|,\qquad
|Y_{\mathrm{sep}}|\searrow |X_{\mathrm{sep}}|.
```

The first retraction fixes $`X_{\mathrm{sep}}`$ pointwise. Thus the full balanced problem is equivalent to contractibility of $`X_{\mathrm{sep}}`$, or of $`Y_{\mathrm{sep}}`$. This is a reduction retaining all separating vertices, not an assertion that they disappear because $`K`$ is fibred.

The nonbalanced fibred theorem also extends to every framing:

**Corollary D.** For any nontrivial fibred $`K`$, all $`n`$, all $`d\neq0`$, and all integer $`f`$, both strong retractions onto $`MS(L)`$ hold. When $`f\neq0`$, the stronger equality and Euler formula in Theorem A(1) hold. This corollary does not settle balanced clusters with $`n\geq4`$.

## 2. Geometric and analytic inputs

The following results are used at their stated geometric scope.

- [the recursive proof](recursive-and-fibred.md), §§2–6, proves recursively efficient cutting, the classification of **whole systems at every finite slope**, ordinary internal-slope invariance, and natural roots. Its final stated theorem specializes to slope zero. Section 4 below recalls the finite-slope proof and isolates the annular exceptions.
- [the framed proof](framed-clusters.md), §§2–3 and 6–8, proves the actual framed peripheral calculation, the horizontal pattern calculation, and the framing-sensitive transverse-return coordinate. Its topology of the pattern and its positive-genus return lemma do not require a two-bridge companion.
- [the zero-framed proof](zero-framed-clusters.md), §§5–6 and 8–10, provides the one-boundary circular envelope and the rooted path-chamber closure and prisms. The conditions needed to apply these arguments are checked again below.
- [CW, Part 7, Theorem D] gives $`X\subseteq Y`$ and a strong deformation $`H_D`$ of $`Y`$ onto $`X`$, for every non-split link. Write $`R_D`$ for its endpoint. It recombines **whole original actual-bearing components**, and exactly recovers every point of a cyclic simplex. It does not assert contractibility.
- [PS, Theorem 1.1] gives contractibility of the taut cyclic complex after the taut endpoint has been identified.
- For Theorem B we additionally use the geometric input and exchange theorem of the **official 11 September 2026 competition version** [C], together with geometric connectedness [K92, Theorem A]. Specifically, the relative-area existence, disjointness, finite-area compactness, boundary regularity and local rounding arguments are used for connected surfaces meeting both actual tori once. Section 8 verifies the replacement for the two global uses of linking indecomposability: connected raw actual-bearing frontiers and compression without separation of their actual boundaries. The general-link conclusion that [C] leaves open is not an input.

The analytic input in the last item is explicit. The balanced-double proof depends on these geometric existence and exchange results in addition to HT. No unverified Hatcher–Oertel or Oertel classification is used.

## 3. Actual framing, efficient cuts, and the ordinary quotient

For $`n\geq2`$, put

```math
M=E(L)=P\cup_T Q,\qquad
Q=E(K),\qquad P=S^1_h\times B_n,\qquad
h=\lambda+f\mu,
```

where $`B_n`$ is a disk with $`n`$ actual holes. Let $`\mu_i`$ be coherently referenced actual meridians and $`\lambda_i^0`$ their individual preferred longitudes. Then

```math
\mu=\sum_i\mu_i,\qquad h_i=\lambda_i^0+f\mu_i,
```

and the total linking class and actual spanning boundary curves are

```math
\begin{aligned}
\Phi(\mu_i)&=\epsilon_i,&
\Phi(\lambda_i^0)&=f(d-\epsilon_i),&
\Phi(h)&=fd,\\ 
\alpha_i&=\epsilon_i\lambda_i^0-f(d-\epsilon_i)\mu_i
         =\epsilon_i h-fd\,\mu_i,&
\Phi|_Q&=d\psi,
\end{aligned}
```

where $`\psi(\mu)=1,\ \psi(\lambda)=0`$. In particular $`\Phi(\alpha_i)=0`$, and each $`\alpha_i`$ is primitive.

When $`d=0`$, the actual slope is the signed pattern fibre, and a nonempty companion cut has slope $`h=\lambda+f\mu`$. When $`d\neq0`$, a companion trace in the kernel of $`\Phi|_T`$ has slope $`\lambda=h-f\mu`$. Confusing these two slopes would invalidate both parts of the argument.

All the tori used in the construction are incompressible, and $`M`$ is irreducible and boundary-irreducible: use amalgam normal form for the peripheral group injections and the innermost-circle sphere argument. Thus $`L`$ is non-split and there are no actual disk components. For arbitrary nontrivial $`K`$, the single outer torus $`T`$ has these same properties. When $`f\neq0`$, non-splitness also follows directly from pairwise linking.

Minimizing intersection with $`T`$ makes all cut curves and cut pieces essential. A boundary-parallel cut annulus has both ends on $`T`$; an innermost empty annular parallelism removes two intersections. Hatcher's boundary-compression lemma then gives boundary incompressibility. Apply this to the entire finite coloured union when simultaneous representatives are involved. For a recursive companion, proceed parent before child, minimizing in each whole child exterior relative to its already fixed parent boundary. This gives essentiality in every whole child exterior, not only in terminal pieces.

Conversely, compatible essential pieces glue incompressibly. An outermost intersection arc of a compression disk with the cutting tori would boundary-compress a piece; after eliminating all such arcs the disk lies in one incompressible piece. The argument allows cycles and branching in the assembly graph of the surface. Only **whole closed components** are discarded.

In the balanced case, an actual-bearing pattern piece is vertical. If the companion is used, at least one reaching annulus forces its trace slope to be $`h`$, and all the traces on $`T`$ have that slope. The whole pattern union then verticalizes simultaneously. If nothing reaches $`T`$, any remaining companion assembly would be a prohibited closed whole component.

The ordinary comparison is not a quotient by marked-torus twists. Once the trace slope on a torus agrees, an empty surface product meets that torus in annuli. A whole incompressible torus cannot inject into the free group of a product with a bounded surface. An innermost returning annulus would make a cut annulus boundary-parallel. All remaining annuli span the product and straighten to product annuli. Thus product simplification preserves the torus and the common boundary motion. This is the slope-independent product-annulus argument of [the framed proof](framed-clusters.md), §2.

For balanced patterns, the possible spanning-bundle exception is excluded because $`\Phi`$ kills the injected $`\mathbb Z^2=\pi_1(T)`$, whereas a compact spanning fibre has free fundamental group. Internal slope agreement in a recursive companion is proved independently by the minimal-subtree argument in §4.4, before applying internal product comparison.

## 4. The recursive finite-slope structure

The finite-slope structure underlying [the recursive proof](recursive-and-fibred.md) is as follows.

### 4.1. Terminal blocks and the two modes

A profile records active block modes, finite slopes, and active HT carriers. It does not identify different plumbing parameters, ordinary gluing twists or ordinary connected surface types.

For an essential oriented system with $`N`$ outer boundary circles of one finite slope, there are two alternatives:

**Regular mode.** every component has one boundary and the slope is zero.
**Reflecting mode.** $`N`$ is even and the actual component partition of the cyclic boundary labels is generated by reflections

```math
i\longmapsto c_\nu-i\pmod N,\qquad c_\nu\ \text{odd}.
```

Each generating identification reverses the boundary orientation sign. This describes existing embedded systems, not arbitrary lists of formally realizable permutations.

An HT carrier includes its integer part and its entire admissible coefficient string: $`\beta=(r;b_1,\ldots,b_s)`$ with $`|b_i|\geq2`$. We use the minus convention $`[b_1,\ldots,b_s]=1/(b_1-1/(b_2-\cdots-1/b_s))`$ and $`p/q=r+[b_1,\ldots,b_s]`$. With $`E`$ the all-even carrier and $`\sigma(\beta)=\sum_i\mathrm{sgn}(b_i)`$, its slope is $`m(\beta)=2(\sigma(\beta)-\sigma(E))`$. Carriers are never identified merely because their slopes or lengths agree.

For a two-bridge terminal on a length-$`s`$ HT carrier, all slopes are integral and

```math
\chi=-N(s-1).
```

The all-even carrier has slope zero and has exactly $`N`$ one-boundary components, each of genus $`g(K)`$. Otherwise the ordered plumbing squares and odd bands give the displayed reflections. An odd number of labels would give an orientation-reversing fixed label, so is impossible. These facts apply to the whole disconnected HT union, and the complete moves at coefficients $`\pm2`$ retain an odd root section.

For $`T(a,b)`$, the regular fibre is $`\lambda+ab\mu`$. A horizontal connected piece has coherent boundary. The longitude kernel and primitivity of its relative class force slope zero and one boundary; it is a knot fibre. A vertical piece is the essential two-boundary annulus separating the exceptional fibres, of slope $`ab`$. A finite vertical system is a parallel annulus stack, with reversal matching and a distinguished side.

For a component with $`A`$ outer boundaries, write $`-\chi=A t`$. The density $`t`$ is fixed by the profile. At an HT terminal $`t=s-1`$; at a horizontal torus terminal $`t=2g(T(a,b))-1`$; at a vertical annular terminal $`t=0`$.

### 4.2. Connected sums

The composing block for $`K=K_1\#\cdots\#K_m`$ has regular fibre the common meridian, and

```math
\lambda_0=\sum_i\lambda_i.
```

A finite outer slope forces a horizontal system meeting every child. Child slopes are finite and, by induction, integral, say $`s_i`$. If the primitive dual class of a connected horizontal piece has value $`k>0`$ on the meridian, its value on $`\lambda_i`$ is $`-ks_i`$. These classes generate first homology, so primitivity forces $`k=1`$. Thus each piece is a section with one boundary at each port, and

```math
r=\sum_i s_i,\qquad t_K=(m-1)+\sum_i t_{K_i}.
```

All ports see the same cyclic ordering of the $`N`$ sections, up to a shift. Shift-conjugating a reflection changes its constant by an even integer. The outer component partition is exactly the union of the child reflection relations. If all children are regular, so is the output; otherwise it is reflecting. This proves connectivity, not merely the slope formula.

### 4.3. Cables, including the annular root

For $`W=E(C_{p,q}(J))\setminus\mathrm{int}E(J)`$,

```math
\mu_J=p\mu_K,\qquad \lambda_K=p\lambda_J,\qquad
h_0=\lambda_K+pq\mu_K,\qquad
h_1=p\lambda_J+q\mu_J.
```

For a horizontal component, the oriented boundary equation first forces finite child slope $`s`$ and outer slope $`r=p^2s`$. Induction makes $`s`$ integral. A connected component with $`k`$ outer boundaries has primitive dual values

```math
\eta(\mu_K)=k,\qquad \eta(\lambda_J)=-kps.
```

Hence $`k=1`$, its inner boundary count is $`p`$, and

```math
\chi(H)=-(p-1)|q-ps|,\qquad
t_K=(p-1)|q-ps|+p\,t_J.
```

The inner labels are $`\mathbb Z/(pN)`$; a horizontal cable piece identifies exactly labels with the same residue modulo $`N`$. Consequently one first adds the relations $`i\sim i+N`$, and then descends the child's reflections to

```math
j\longmapsto c_\nu-j\pmod N.
```

The first relations preserve signs and the second reverse them. A descended reflection on odd $`N`$ would fix an oriented outer sheet and reverse its sign. Thus the reflecting outer system again has even $`N`$. This argument includes the merger of several different child components into one outer component.

A vertical root instead has outer slope $`pq`$. Any inner trace would have finite slope $`q/p`$, which is nonintegral and excluded by induction. The entire child is therefore unused, and only same-outer-port essential cabling annuli remain. No hidden horizontal mode at $`pq`$ exists, since it would require $`s=q/p`$.

The same induction gives a finite necessary slope envelope

```math
\begin{aligned}
\mathcal S(T(a,b))&=\{0,ab\},\\ 
\mathcal S(K_{\text{two-bridge}})&=\{m(\beta):\beta\text{ admissible HT carrier}\},\\ 
\mathcal S(K_1\#\cdots\#K_m)&=\mathcal S(K_1)+\cdots+\mathcal S(K_m),\\ 
\mathcal S(C_{p,q}(J))&=\{pq\}\cup p^2\mathcal S(J).
\end{aligned}
```

Only necessity is needed. This is not an assertion excluding meridional surfaces in composite knot exteriors; the induction is specifically for finite outer slope.

### 4.4. Chambers, ordinary profiles, and natural roots

Root a reflecting system so that $`c_1=-1`$, and set

```math
e=\gcd(N,c_2-c_1,\ldots,c_h-c_1),\qquad
q_0=e/2,\qquad A=2N/e.
```

For one reflection set $`e=N`$. Products of reflections generate the translation subgroup specified by this gcd. The orbits are residues modulo $`e`$ paired by $`j\leftrightarrow e-1-j`$. Thus there are $`q_0`$ components, each with $`A`$ boundaries, and the actual meridian word is

```math
(0,1,\ldots,q_0-1,q_0-1,\ldots,1,0)^{A/2}.
```

Every orbit has equal positive and negative boundary counts. Its relative class in the knot exterior is zero, so its connected component separates. The complement dual graph is therefore a tree. The first monotone segment of this boundary word traverses every edge once; hence the entire tree is that path. This is not a claim that its interior chambers are products.

Internal traces and their slopes are ordinary invariants. Here is why the argument does not assume that conclusion in order to use torus-preserving comparison. No cut curve on a connected companion surface can be boundary-parallel in that surface: its first outer cut piece would have to be an annulus, whereas a composing section and a horizontal cable piece have negative Euler characteristic; the vertical cable case avoids its child entirely. The dual tree of lifted cut curves therefore maps without folds into the ambient structural Bass–Serre tree. A fold would give an arc of an essential cut piece homotopic into a boundary torus but not into its boundary, contradicting relative boundary incompressibility. After suppressing annular subdivisions, the surface splitting is reduced; each edge lies on an axis. Its embedded tree is the unique minimal invariant tree of the injected surface subgroup. Conjugating that subgroup under an ordinary isotopy therefore preserves the quotient edge labels and their cyclic stabilizers. A primitive trace stabilizer determines its slope. Only now is torus-preserving product comparison applied. This is [the recursive proof](recursive-and-fibred.md), §6.0, whose proof applies at every finite slope.

At an odd HT root, the complete $`\pm2`$ moves avoid the root section. At a vertical torus root, the two exceptional-fibre orders distinguish the sides. At a vertical cable root, one side is a solid torus and the other contains the nonabelian child group. A rooted child gap propagates uniquely through a composing section or a horizontal cable gap to the outer boundary. Although a cable gap can have several inner occurrences, they all give the same outer end: reducing the reflection divisor sends the rooted gap residue $`-1`$ to the same residue for the outer path.

The transverse coordinate at outer slope $`f`$ is

```math
\nu_f(a\lambda+b\mu)=b-fa.
```

In particular longitude motion contributes $`-f`$, and is not discarded. The positive-genus no-return lemma ([the framed proof](framed-clusters.md), Lemma 6.1, and [the recursive proof](recursive-and-fibred.md), §6.1) says that an ordinary return of an essential separating positive-genus integral-slope system has zero transverse configuration winding and no nontrivial cyclic permutation of boundary occurrences. Its auxiliary construction attaches a reaching annulus to each boundary; the auxiliary actual signs balance, so its actual spanning slopes are indeed the signed $`\lambda+f\mu`$. In the product comparison two parallel copies of the connected surface have just one chamber incident to both complete faces, their middle collar. Confining product pushes there gives zero transverse winding; the residual pattern twist is detected by $`m[b_0]`$ in $`H_1(B_A,b_j)`$, nonzero for $`m\neq0`$ since $`A\geq2`$. This argument uses the basis $`(\lambda+f\mu,\mu)`$, not an assumed extension of that basis change across $`Q`$.

Consequently the propagated root is ordinary at nonzero integral slopes as well. Restricting whole outer components retains whole child components and their real sheets at every active child. Ordered compression of this reflection-invariant sheet set preserves the outside root gap. Rooting therefore commutes with deleting components and colours. Distinct ordinary gluing data are retained, not identified.

Finally, except at a top-level vertical torus or cable root, every reflecting profile has $`t\geq1`$. This follows from the terminal value $`s-1\geq1`$ for a non-torus HT carrier, the composing contribution $`m-1`$, and the horizontal cable contribution $`(p-1)|q-ps|\geq1`$. Hence

```math
\chi(F)=-At<0,\qquad g(F)=1+\frac A2(t-1)\geq1.
```

This checks precisely the genus hypothesis just used. At a vertical root we use the annular argument of §5.3 instead; no positive-genus return lemma is applied to annuli.

## 5. Proof of Theorem A

### 5.1. Nonzero pattern-fibre evaluation

Assume $`fd\neq0`$, with $`n\geq2`$. An actual-bearing pattern piece has boundary transverse to $`h`$ and is horizontal. It meets every actual torus, so unit actual usage permits just one such piece $`H`$. It rules out any additional horizontal piece or essential vertical annulus. There are no closed pieces.

Choose $`u:B_n\to\mathbb R/\mathbb Z`$ with degrees $`\epsilon_i`$ on the actual meridians. The model

```math
F_P(\theta,b)=fd\,\theta+u(b)\pmod1
```

has fibres that are connected $`|fd|`$-sheeted covers of $`B_n`$: an actual monodromy step is $`\pm1`$, generating the sheet group. There is one boundary on each actual torus and $`|d|`$ coherent longitude boundaries on $`T`$. Thus

```math
\chi(H)=|fd|(1-n).
```

The ordered circular-configuration description of horizontal pieces in a product gives this same topology for every actual pattern piece in the prescribed class. The companion system has $`|d|`$ coherent longitude boundaries. Its class is nonzero, so §4 forces the regular mode. Its $`|d|`$ pieces are one-boundary Seifert surfaces, all of genus $`g(K)`$. The genus statement follows at the terminals from HT or the torus fibre, and propagates by the section and cable Euler formulas; in particular every incompressible Seifert surface of a member of $`\mathcal C`$ is taut, as proved in [the recursive proof](recursive-and-fibred.md), §5.1.

Every piece attaches to the single $`H`$, so the whole surface is connected, with

```math
g(S)=\frac{2-n+|d|(2g(K)-1)+|fd|(n-1)}2.
```

Such vertices exist by attaching coherent minimal Seifert copies to $`H`$. A norm-minimizing spanning representative can be compressed and stripped of whole closed components to give an incompressible spanning vertex. All vertices just classified have the same Euler characteristic, so all are taut.

For a finite geometric family of connected spanning surfaces, its complement dual graph has every edge dual to the same primitive class $`\Phi`$. The collapse onto this graph is onto on first homology. Consequently its cycle space has dimension one: the signed crossing counts of all edges are equal on every cycle. No edge is a bridge, since each whole spanning surface is nonseparating. The graph is a coherently oriented circle. Reading it in the one $`\Phi`$-cover shows that distinct members have cyclic width one. Thus every geometric simplex is cyclic, and

```math
X=Y=MS.
```

No single-vertex assertion is made; different companion Seifert systems can give different ordinary vertices.

### 5.2. Balanced, nonannular root modes

Now $`d=0`$, $`f\neq0`$, and exclude the top annular modes of §5.3. A nonempty companion system has slope $`f`$. It is reflecting, because the regular mode is possible only at zero slope. Section 4 gives positive genus, negative Euler characteristic, uniform even arity $`A`$, the repeated path word, and a natural ordinary root.

A simultaneous finite family has one profile and one arity. At a composing or horizontal cable block, horizontal/vertical or active/empty disagreement is impossible on a common nonempty system. At each active HT terminal the whole union has one carrier. Restricting whole components preserves this profile. Thus no geometric edge joins different nonempty profiles or arities. Since $`X\subseteq Y`$, there are no such cyclic edges either.

Let $`X_{\mathfrak p,A}`$ be a sector, including the common annular subcomplex $`\mathcal A_X`$. We spell out the replacement interface rather than infer a contraction from the reflection arithmetic alone.

For an efficient vertex order its companion pieces from the root end, and choose the side containing that end. The original chambers all of whose incident surface faces lie on that side have pairwise disjoint incident-piece sets. Resolve the root end chamber by replacing its whole incident companion piece with the annuli in its $`T`$-boundary, pushed into the pattern; retain the other pieces as small copies of themselves. A nonproduct chamber can be resolved by this boundary replacement without identifying its two faces by an isotopy.

The raw composition of pattern paths can create a boundary-parallel outer return. Its empty disk contains no old essential pattern arc and no old trace point. Its new endpoints therefore lie in one old boundary gap. The repeated path word identifies exactly one still unselected original chamber on the chosen side, whose entire incident pieces remain. Resolve it too.

The enabling test is monotone: a witness is a complete pattern path between surviving endpoints, and operations with disjoint incident-piece sets cannot change that witness. There is a unique least closed set of original chambers containing the seed. Do not discard a closed component containing companion pieces before this closure terminates. At termination all retained cut pieces are essential. Essential assembly and only then whole-closed-component deletion give an incompressible spanning parent $`p(S)`$, retaining a definite ordinary subcollection and strictly decreasing the number of companion pieces. The number is an ordinary integer; here it also equals $`-\chi(S)/(At)`$.

There is a full-family version. When the seed is first in the common coloured root order, its end chamber is empty of every other colour. A repair disk excludes all the other colours' pattern arcs and traces. Uniform arity and the repeated word make every companion piece in the proposed chamber visible in that same gap. Therefore the entire repair chamber is empty of the family, not merely its one local annulus. Every retained piece keeps its relative position.

Iterate the parent to obtain finite trajectories. Restore shared **whole actual-bearing component** occurrences using the component-wall exact-recovery family in the one original $`\Phi`$-cover. Merge genuine events in their natural coloured root order; each is then first in the current whole family. Put stationary annular events after genuine events, using one fixed total order on annular vertices. This fixed convention is needed for faces.

For a trajectory of length $`\ell`$, give its states heights $`j/\ell`$ above its vertex; give a stationary annular event heights 0 and 1 with equal images. Consecutive affine height graphs form the usual prism slabs. Every slab maps to a genuine geometric simplex by the relative-family assertion. Deleting a vertex deletes its zero-thickness slabs and retains all other heights and orders. The maps therefore agree on faces. Every closed simplex cylinder has a finite event list and finite image, so the weak/CW cylinder criterion gives a continuous homotopy.

Compose with $`R_D`$. Whole-component recombination stays within the same sector. Exact recovery gives the identity initially and fixes $`\mathcal A_X`$ throughout. This is the strong sector retraction

```math
|X_{\mathfrak p,A}|\searrow|\mathcal A_X|.
```

No generic multi-boundary level is assumed incompressible, and no claim that closed-component deletion alone preserves cyclic adjacency is used.

Distinct sectors meet exactly in $`\mathcal A_X`$ and have no simplex mixing their other vertices. Their relative homotopies consequently glue. A balanced pattern has a pure annular representative, obtained by matching opposite actual signs with disjoint planar arcs. Its norm is zero. Every nonempty companion cut in the present modes has negative Euler characteristic, while pattern annuli contribute zero. Hence the taut vertices are exactly the pure pattern-annular ones, and the glued endpoint is $`MS(L)=\mathcal A_X`$.

### 5.3. Annular roots and the remaining cases

If the root is $`E(T(a,b))`$ and $`f=ab`$, the only companion pieces are vertical annuli. If the root is the cable $`C_{p,q}(J)`$ and $`f=pq`$, §4.3 excludes its child and again leaves just returning annuli. Pattern pieces are annuli as well. Each oriented actual-bearing assembly of annuli has Euler characteristic zero and nonempty boundary, and is therefore an annulus. All vertices are taut; use the identity on $`X=MS(L)`$. The pure-pattern restriction would be wrong at these resonances.

If $`f\notin\mathcal S(K)`$, the balanced companion is empty and $`X=\mathcal A_X=MS(L)`$ directly. For $`f=0`$ use [the recursive theorem](recursive-and-fibred.md), which includes its one-boundary circular envelope and all reflecting sectors. For $`n=1`$, $`L`$ is isotopic to $`K`$ independently of $`f`$; the one-boundary genus result gives $`X=Y=MS(K)`$.

The hypotheses of [PS] hold: $`M`$ is irreducible and boundary-irreducible, each prescribed boundary curve is primitive and nonseparating on its torus, and $`H_2(M)\to H_2(M,\partial M)`$ is zero for a link exterior in $`S^3`$. The identified taut endpoint is therefore contractible, including the norm-zero cases.

Finally concatenate $`H_D`$ with the retraction of $`X`$ just proved. At time $`1/2`$ both formulas take the value $`R_D(y)`$, and both stages fix $`MS(L)`$. This proves Theorem A.

## 6. What fibredness proves, including in total class zero

Let $`Q=E(K)`$ fibre over the circle with one-boundary fibre $`F`$, and let $`\psi`$ be its primitive class.

**Lemma 6.1 (compact product lift).** A compact connected incompressible, relatively boundary-incompressible surface in $`F\times\mathbb R`$, with nonempty essential boundary in $`\partial F\times\mathbb R`$, is a horizontal copy of $`F`$.

Enclose the surface in $`F\times[a,b]`$, put its boundary at distinct levels on the vertical annulus, and cut $`F`$ to a disk by proper arcs. Use their product disks. Incompressibility removes closed intersections. A returning intersection arc either gives a boundary compression or is removable by a boundary disk. Surviving arcs join the two vertical sides in their linear order. Cutting leaves disks in balls; relative disk isotopy straightens them. Regluing gives a finite horizontal covering whose sheets are linearly ordered in every interval. Monodromy preserves this finite linear order, so every connected covering has degree one. This proves the lemma. The detailed product-disk argument is also given in [the recursive proof](recursive-and-fibred.md), §10.

**Lemma 6.2 (whole-system fibred dichotomy).** For any finite essential oriented longitudinal system $`\mathcal R\subset Q`$:

**(1)** if one component is nonseparating, every component has one boundary and genus $`g(K)`$;

**(2)** otherwise every component separates, has a positive even number of boundaries with balanced signs, and has negative Euler characteristic;

**(3)** for each component $`R`$ in the second alternative,

```math
\psi(\pi_1R)=e_R\mathbb Z\quad\text{for some }e_R\geq1.
```

**Proof.** A connected nonseparating proper oriented surface has primitive relative class, by closing a once-crossing arc through its connected complement. Since $`H_2(Q,\partial Q)=\mathbb Z`$, such a component $`R_0`$ represents $`\pm[F]`$. Every loop on any disjoint $`R_j`$ has zero intersection with $`R_0`$; use a normal push-off for loops on $`R_0`$ itself. Therefore $`\psi`$ vanishes on every $`\pi_1R_j`$. Each $`R_j`$ has a homeomorphic compact lift to $`F\times\mathbb R`$. Essentiality lifts, including the relative fundamental-group condition for boundary incompressibility. Lemma 6.1 makes every lift, hence every original component, one-boundary and homeomorphic to $`F`$. Only its topology is read from the lift; no upstairs isotopy is silently descended.

The same argument applied to a least-genus Seifert surface shows $`g(F)=g(K)`$.

If all components separate, each has zero relative class, hence balanced longitudinal boundary and even boundary count. If $`\psi|_{\pi_1R}`$ were zero for one such component, the product lemma would give one boundary and nonzero relative class, a contradiction. This proves item 3. There is no disk by boundary injection. There is no annulus, since its fundamental group is generated by a boundary longitude and would have zero $`\psi`$-image. Every remaining connected orientable bounded surface has negative Euler characteristic. ∎

In particular the second alternative can occur even for a fibred two-bridge knot. It is not ruled out by the uniqueness or minimal genus of a Seifert fibre.

There is a useful precise covering interpretation of item 3. A component of the preimage of $`R`$ in the knot's infinite cyclic fibre cover is the infinite cyclic covering of $`R`$ corresponding to $`\ker(\psi|_{\pi_1R})`$. It is noncompact, and every longitude boundary has infinitely many lifts. Thus the failure of the compact-product proof in the separating case is not just lack of a preferred isotopy: **the required compact lift does not exist**. For nonzero integral slope $`f`$, even the boundary has $`\psi`$-value $`f`$, so its image is nonzero without this argument.

## 7. Exact balanced reduction and a general sufficient certificate

Take $`f=d=0`$. Let $`X_{\mathrm{reg}}`$ contain the pure annular vertices and the vertices all of whose nonempty companion pieces have one boundary. Define $`X_{\mathrm{sep}}`$ as in Theorem C, and similarly define the geometric subcomplexes.

Efficient ordinary comparison at $`T`$ makes these ordinary vertex properties. Normalize an entire finite disjoint family. Lemma 6.2 says a one-boundary piece cannot coexist with a separating piece. Thus there are no geometric, or cyclic, edges between the nonannular portions of the two subcomplexes. Consequently

```math
X=X_{\mathrm{reg}}\cup_{\mathcal A_X}X_{\mathrm{sep}}.
```

The analogous geometric union has intersection $`\mathcal A_Y`$, the pure annular geometric subcomplex.

The one-boundary circular envelope [the recursive proof](recursive-and-fibred.md), §8, and [the zero-framed proof](zero-framed-clusters.md), §§5–6 strongly retracts $`X_{\mathrm{reg}}`$ onto $`\mathcal A_X`$. For clarity, a cyclic simplex's one global band map restricts to a circular companion function $`v(u)`$ of degree zero. Replace it by

```math
v_s(u)=(1-s)v(u)+s\max v.
```

Extend the periodic correction through a fixed pattern collar, keeping actual boundaries fixed. Every generic retained companion level is a whole original one-boundary piece. An outer return joins the only boundaries of two such pieces into a whole closed component, which is deleted. Every actual-bearing output is therefore either one original essential piece with a reaching annulus or a pure actual annulus. Phase averaging, followed by $`R_D`$, is safe and exactly recovers the initial cyclic point. Shared whole-component bands, zero coefficients and face restrictions are handled by the same exact-recovery template as [the recursive proof](recursive-and-fibred.md), §8. No separating piece is included in this construction.

Extend this homotopy by the identity on $`X_{\mathrm{sep}}`$. It agrees on $`\mathcal A_X`$ and yields the first retraction in Theorem C. The component-wall deformation restricts to $`Y_{\mathrm{sep}}`$, because recombining whole original actual-bearing components cannot introduce a nonseparating companion piece. This gives the second.

Every nonempty companion piece in either branch has negative Euler characteristic by Lemma 6.2. Pattern annuli have characteristic zero. Since pure annular representatives exist and disks are excluded, norm zero is equivalent to empty efficient companion cut. Hence $`MS(L)=\mathcal A_X`$.

Finally $`\mathcal A_X`$ is nonempty and contractible by [PS]. Its inclusion in $`X_{\mathrm{sep}}`$ is a CW cofibration. We use the standard cofibration lemma: an inclusion that is both a cofibration and a homotopy equivalence admits a strong deformation retraction; the homotopy extension property makes the inverse and homotopy fixed on the subspace. If $`X_{\mathrm{sep}}`$ is contractible, the inclusion of $`\mathcal A_X`$ is such a homotopy equivalence. Conversely, a strong deformation retraction onto $`\mathcal A_X`$ makes $`X_{\mathrm{sep}}`$ contractible. This proves the equivalence asserted in Theorem C.

A reusable sufficient certificate for the remaining subcomplex is now explicit. Suppose its nonempty companion systems admit ordinary hereditary sectors such that:

**(1)** every simultaneous finite union has one sector and one positive even boundary arity;

**(2)** its complement graph and actual boundary word are the path and repeated word of §4.4;

**(3)** it has an ordinary root end, natural under retaining whole components and deleting colours, with the genuine common boundary motion retained.

Then the closure and prisms in §5.2 apply and prove the complete balanced theorem for all $`n`$. Lemma 6.2 supplies the negative Euler characteristics needed to identify the endpoint. This certificate requires facts about entire disjoint systems and their ordinary motions; a list of boundary slopes, or a statement about single Seifert surfaces, is insufficient.

It includes all fibred members of $`\mathcal C`$. If there are no separating essential longitudinal surfaces at all, $`X_{\mathrm{sep}}=\mathcal A_X`$, recovering the single-boundary criterion for all balanced counts. These are sufficient subclasses, not a claimed classification of all fibred knots satisfying the conclusion.

## 8. A connected-sector exchange lemma with a compression barrier

The following exchange lemma applies to balanced doubles. Its analytic dependencies are exactly identified to avoid invoking [C, Theorem D] outside its hypotheses.

Let $`L`$ be a non-split two-component oriented link with incompressible actual boundary tori. Let $`Z\subseteq Y(L)`$ be the full geometric subcomplex on **all connected** incompressible spanning surfaces. Suppose:

- $`Z`$ is nonempty and connected;
- for every distance-two pair $`u,w`$ in $`Z`$, at least one of them has **no disjoint disconnected incompressible spanning system**.

**Lemma 8.1 (barrier exchange).** Under these conditions $`Z`$ is contractible.

### 8.1. Compression cannot split the actual boundaries

Fix a connected incompressible representative $`B`$ of the barrier endpoint. Let $`P`$ be any compact oriented spanning surface disjoint from $`B`$, not necessarily incompressible or connected, with whole closed components removed.

Compress its actual-bearing components until they are incompressible, retaining every actual boundary. Such a finite sequence exists explicitly: after every step discard whole closed components, let $`G`$ be the sum of genera of the actual-bearing components, and let $`c\in\{1,2\}`$ be their count. The lexicographic pair $`(G,2-c)`$ strictly decreases at every essential compression. A nonseparating compression lowers $`G`$; a separating compression either discards a positive-genus closed side or separates the two actual boundaries and increases $`c`$. No essential compression merely cuts off a sphere. Thus termination does not assume that the intermediate surfaces are connected. Its disks can be chosen disjoint from $`B`$, without changing the prescribed successive isotopy classes: clean a disk's intersection circles using incompressibility of $`B`$ and irreducibility of $`M`$. The disk-push balls contain no actual-bearing component of $`P`$, since each has boundary on $`\partial M`$, whereas the balls are interior. This is [C, Lemma 4.5], applied componentwise after discarding whole closed components.

If $`P`$ initially had two actual-bearing components, or if any compression separated its two actual boundaries, the final system would still have two actual-bearing components: compression and deletion of closed components cannot rejoin them. It would be a disconnected incompressible spanning vertex disjoint from $`B`$, forbidden by the barrier hypothesis.

Therefore every such $`P`$ has exactly one actual-bearing component, and every compression retains its two actual boundaries on one component. Every essential compression strictly reduces the genus of that component. This conclusion is proved using only the existence of a complete compression sequence; it does not assume that a raw frontier is already incompressible.

The same cleaning proof gives robustness for an additional incompressible neighbour $`Z'`$: choose the compression sequence first, then clean it against $`Z'`$; the final ordinary classes do not change. They remain connected because that is a property of the classes already constructed with the barrier.

### 8.2. The analytic input applies to the connected sector

Choose a strictly convex relative metric and a longitude foliation on each actual torus, with the actual oriented spanning slopes. The inputs (U), (E), (Fin), (R1), (R2) of [C, §3 and Appendix A] are for a compact irreducible orientable manifold and connected incompressible surfaces meeting each actual boundary torus once. Those hypotheses hold for every vertex of $`Z`$. The multi-torus local formulation is explicitly checked in [C, §6.3, printed pp.20–22]. It does not require linking indecomposability for the individual minimizers.

Let $`A(v)`$ be the least relative area and $`c(v)=(g(v),A(v))`$, lexicographically ordered on the set of attained values. For fixed genus and area bound, (Fin) gives finitely many ordinary classes of connected two-boundary surfaces. The attained complexity set is consequently well-ordered, just as in [C, Lemma 4.8].

Choose minimizers independently for the vertices. By (U), minimizers of adjacent distinct connected classes are disjoint; coincidence would identify the entire connected surfaces and hence the vertices. Thus every clique has simultaneous representatives, $`Z`$ is flag, and for $`x`$ adjacent to both nonadjacent $`u,w`$, its minimizer is disjoint from both other minimizers at once. The shared-component obstruction is absent inside $`Z`$.

### 8.3. Frontiers, connected outputs, and descent

Take $`x,u,w\in Z`$ with $`x`$ adjacent to $`u,w`$ and $`u,w`$ at distance two. All three are connected spanning surfaces dual to the same primitive $`\Phi`$. Cutting along the minimizer for $`x`$ gives one whole fundamental block of the $`\Phi`$-cover, containing lifts of both other minimizers.

Apply the upper/lower frontier construction of [C, Lemma 4.9], with its boundary count performed separately on the two actual tori. The no-disk-patch and corner-rounding arguments are [C, §§5.1–5.3 and §6.3]. They give two raw oriented spanning frontiers, each with one actual boundary on each torus, disjoint from each input, with

```math
\chi(T_\uparrow)+\chi(T_\downarrow)
=\chi(S_u)+\chi(S_w).
```

Discarded closed frontier components have nonpositive Euler characteristic; spheres are excluded by the no-disk-patch argument. The construction is local near the two inputs and has representatives disjoint from every further surface disjoint from both, with the same coarse ordinary classes. The perturbation and push-off scales may depend on that further surface, but all sufficiently small choices are isotopic.

Choose the barrier endpoint among $`u,w`$. Each frontier is disjoint from a representative of it. In a perturbed configuration use the perturbed input as this representative; the barrier is an ordinary-class property. Section 8.1 proves, **before any genus estimate**, that each frontier has one actual-bearing component carrying both actual boundaries, and that all compression descendants can be retained connected. This establishes the connectedness needed by the local exchange argument.

Compress to two fixed vertices $`v_\uparrow,v_\downarrow\in Z`$. The robustness argument shows they are equal or adjacent to $`x,u,w`$, and equal or adjacent to every common neighbour of $`u,w`$ in $`Z`$. The choices are made before that further neighbour is presented. In particular the quantifier order is $`\exists(v_\uparrow,v_\downarrow)\ \forall z`$. Once the successor classes have been fixed, disk cleaning against $`z`$ need not keep the old barrier representative disjoint: connectedness is already a property of those fixed ordinary classes. Pairwise equality or adjacency is sufficient; no simultaneous simplex containing the intersecting inputs $`u,w`$ is asserted.

For a connected two-boundary surface $`\chi=-2g`$. Euler additivity, closed-component removal and the strict genus decrease at each compression yield

```math
g(v_\uparrow)+g(v_\downarrow)\leq g(u)+g(w).
```

If equality holds, no compression occurred. The quantitative rounding gain and smaller push-off cost from [C, §5] then give

```math
A(v_\uparrow)+A(v_\downarrow)\lt A(u)+A(w).
```

The nontransverse and common-boundary-leaf cases use the same local estimates on each torus, as in [C, §6.3]; they use connected inputs and the connected compression conclusion just proved. They do not use linking indecomposability at any further point.

Both outputs are apices of the two-interval. Choose an apex of least complexity. If its complexity were at least both endpoint complexities, repeat the exchange with this apex as the common neighbour. If one output has genus below the least apex genus, its complexity is smaller. Otherwise the total-genus inequality forces both endpoints and both outputs to have that same genus; strict total-area descent then makes one output's area smaller than that of the least apex. Either outcome contradicts its minimality. Hence the two exchange axioms of [C, Definition 2.1] hold. The connected flag complex $`Z`$ is contractible by [C, Theorem B]. ∎

This proof is a verification and use of that paper's analytic exchange package, not an appeal to its unproved general-link extension. The barrier argument replaces [C, Lemmas 6.1–6.2]. No connectedness restriction is imposed on the final full complex: $`Z`$ is only an intermediate subcomplex.

## 9. Applying the barrier to a fibred balanced double

Now let $`L=L_0(K;+1,-1)`$, with $`K`$ arbitrary nontrivial and fibred. The pattern base is a pair of pants.

**Lemma 9.1 (isolation of the two branches).**

**(1)** There is a unique pure pattern-annular vertex $`a`$.

**(2)** Every nonannular connected vertex has only separating companion pieces.

**(3)** Every disconnected vertex has only one-boundary companion pieces, and has two connected actual-bearing components, one at each actual torus.

**(4)** No vertex in item 2 is disjoint from a vertex in item 3.

**Proof.** The actual-to-actual seam in a pair of pants is unique with free endpoints, giving item 1. If all companion pieces have one boundary, any outer-to-outer pattern annulus joins two such pieces into a whole closed component, prohibited here. Therefore a nonempty regular system has just two reaching annuli and two one-boundary pieces. It is disconnected.

Conversely, suppose an actual-bearing component uses only one actual torus. Its oriented pattern boundary equation gives total companion longitude coefficient $`+1`$ or $`-1`$. At least one of its companion pieces has nonzero relative class. By Lemma 6.2 the entire companion union, including the other actual-bearing component, consists of one-boundary pieces. This proves items 2 and 3. If representatives as in item 4 were disjoint, simultaneously normalize their companion union; it would contain both a nonseparating and a separating piece, contrary to Lemma 6.2. ∎

No assertion that all regular vertices are one ordinary vertex is needed. In particular this argument does not descend an isotopy from the fibre cover to claim uniqueness.

Let $`Z`$ be the subcomplex on connected vertices. By Lemma 9.1 it is precisely $`Y_{\mathrm{sep}}`$, and its only intersection with the regular branch is $`a`$. There are no other cross edges. The whole $`Y(L)`$ is connected by [K92, Theorem A], which applies to its componentwise incompressible, possibly disconnected, ordinary vertices. A finite path between vertices of $`Z`$ can leave $`Z`$ only through $`a`$ and can re-enter it only through $`a`$; remove each such excursion. Thus $`Z`$ is connected.

Every distance-two pair in $`Z`$ has at least one endpoint different from $`a`$. This endpoint is a nonannular connected vertex and, by Lemma 9.1(4), is a barrier against all disconnected incompressible spanning systems. Lemma 8.1 therefore applies: $`Z`$ is contractible.

For completeness the geometric and cyclic complexes coincide on this connected vertex set. For a finite simultaneous family the complement dual-graph argument in §5.1 applies: all connected surfaces represent the same primitive $`\Phi`$, giving a coherently oriented cycle and cyclic width one. Flagness then gives

```math
X_{\mathrm{sep}}=Y_{\mathrm{sep}}=Z.
```

Lemma 6.2 also excludes any companion annulus with longitude boundary. Thus every annular whole vertex misses $`Q`$ and equals $`a`$, while any nonempty companion cut has negative Euler characteristic. Hence $`MS(L)=\{a\}`$.

Since $`Z`$ is a contractible CW complex and $`a`$ is a vertex, there is a strong deformation retraction $`Z\searrow\{a\}`$: the inclusion of this point is both a cofibration and a homotopy equivalence. Glue it to the regular circular-envelope retraction $`X_{\mathrm{reg}}\searrow\{a\}`$. Their intersection is exactly $`a`$, which both homotopies fix. This gives $`X(L)\searrow MS(L)`$. Concatenate with $`H_D`$ to obtain the claimed retraction of $`Y(L)`$.

If $`f\neq0`$, the oriented pairwise linking is $`-f\neq0`$. Thus the two-component link is linking-indecomposable. [C, Theorem D] gives contractibility of $`Y`$; [CW] gives contractibility of $`X`$. [PS] gives contractibility of its nonempty taut cyclic subcomplex $`MS`$. The inclusion $`MS\subseteq X`$ is a CW cofibration and a homotopy equivalence between contractible spaces, so is a strong deformation retract. Concatenating with [CW] gives the $`Y`$ statement. This step in fact works for every nontrivial companion at nonzero framing. Theorem B follows.

Corollary D follows as well: for $`fd\neq0`$, the horizontal pattern calculation in §5.1 gives $`|d|`$ coherent longitude boundaries. Lemma 6.2 forces all companion pieces to be one-boundary minimal-genus pieces. The same connectedness, Euler and tautness argument gives $`X=Y=MS`$. For $`f=0,d\neq0`$, use [the nonbalanced fibred theorem](recursive-and-fibred.md), §10, including its whole-system compact-lift proof.

## 10. The remaining balanced obstruction is real, but is not a noncontractibility example

Theorem C is the strongest unconditional reduction here for arbitrary $`n`$. For $`n=2`$, its separating subcomplex has only connected vertices, enabling §8. For $`n\geq4`$, that assertion is false even for explicit fibred two-bridge knots.

Take the example

```math
K=K_{29/137},\qquad
\frac{29}{137}
=1+[-2,-2,-2,-2,2,-2,-2,2]
=[4,-2,-2,-3,-3,-2].
```

The all-$`\pm2`$ expansion makes $`K`$ fibred. Both expansions have signed coefficient count $`-4`$, so the second is a zero-slope odd carrier. Take its oriented two-sheet surface $`R`$, equivalently the horizontal frontier of a regular neighbourhood of the one-sheet nonorientable HT surface. HT gives essentiality; the orientation double is connected and has two boundary circles. It is separating, and

```math
\chi(R)=2(1-6)=-10,\qquad g(R)=5.
```

Take two parallel copies $`R_1,R_2`$ in $`Q`$. Their boundary order is $`R_1,R_2,R_2,R_1`$. In a four-hole pattern choose four disjoint reaches to actual holes, with each copy receiving one positive and one negative actual boundary. Essential assembly gives a disconnected vertex $`U\sqcup V`$, with both $`U`$ and $`V`$ connected and nonannular, each of genus five.

The two actual holes used by $`V`$ can instead be joined by a pattern annulus $`A`$ avoiding the reaches for $`U`$. This gives another vertex $`U\sqcup A`$. They are distinct ordinary vertices and share the entire component class $`U`$. The construction uses genuine essential pieces and labelled actual boundaries, not an abstract incidence graph.

Thus the separating branch for four actual components already contains disconnected vertices and actual shared-component pairs. The connected-minimizer inference in §8.2 is no longer available for that entire branch. The two-boundary compression barrier also fails as an automatic consequence of fibredness: separating pieces can be distributed among balanced proper subsets of the actual components.

There is an actual adjacency obstruction to a blanket barrier assertion as well. Take one of the essential four-boundary genus-nine pieces from the example in the next paragraph and attach all its boundaries to the four actual tori by reaches. This gives a connected spanning vertex. A pure pattern-annular vertex of the same four-component link consists of two annuli and is disconnected. By [K92, Theorem A], a finite geometric edge path connects these vertices, and some edge changes connectedness. Its connected endpoint is necessarily nonannular, since a connected annulus cannot carry four actual boundaries. Hence this specific fibred parallel link has a nonannular connected vertex with a disconnected incompressible neighbour. The assertion that every such connected vertex is a compression barrier, used for doubles, is genuinely false for this four-component link.

There are two additional limits to the fibre-cover shortcut:

- By Lemma 6.2(3), $`R`$ itself has nonzero $`\psi`$-image and has no compact lift to the fibre product. This is an actual obstruction to the proposed proof step, not just an unproved implication.
- The $`N=8`$ system on this same odd carrier has two nonisotopic four-boundary pieces of genus nine and boundary word $`UVVUUVVU`$ [the zero-framed proof](zero-framed-clusters.md), §12. Their middle chamber is not a product. Fibredness therefore does not supply a common parallel packet either.

For companions outside the recursively certified class, no complete proof here gives ordinary hereditary path sectors for all their separating longitudinal systems. Knowing only that a complement graph is a tree is insufficient: a branching chamber can have two faces seen by an empty pattern return and a third face on the wrong side for the proposed replacement. The abstract word $`AABBCC`$ illustrates this failure of the inference from “tree” to the one-sided path closure; we do not claim that this abstract word has been realized by a specified fibred knot.

What remains to prove for the unrestricted $`n\geq4`$ assertion is a contraction of the full $`X_{\mathrm{sep}}`$ of Theorem C. It could come from a complete hereditary chamber/root certificate, or from a new exchange argument handling shared actual-bearing components and possibly disconnected outputs. Neither is supplied by fibredness alone in the arguments above. The actual shared-component example is **not** a counterexample to contractibility: it lies in $`\mathcal C`$, where Theorem A supplies the required different contraction.

The established coverage is as follows; no maximality among all possible subclasses is asserted:

- $`K\in\mathcal C`$, all $`n,\epsilon,f`$: Full strong retractions, Theorem A.
- Arbitrary fibred $`K`$, $`d\neq0`$, all $`n,f`$: Full strong retractions, Corollary D.
- Arbitrary fibred $`K`$, $`n=2,d=0`$, all $`f`$: Full strong retractions, Theorem B.
- Fibred $`K`$, $`d=0,f=0`$, all $`n`$, satisfying the certificate in §7: Full conditional theorem with all hypotheses stated.
- Fibred $`K`$, $`d=0,f=0`$, with no separating essential longitudinal surface: Full single-boundary subclass.
- Arbitrary companion, balanced framing $`f`$ excluded from its essential boundary slopes: Empty companion; $`X=\mathcal A_X=MS`$, and $`Y\searrow X`$.
- Arbitrary fibred $`K`$, $`n\geq4,d=0`$, without those additional inputs: Unclosed; exact remaining subcomplex given in Theorem C when $`f=0`$.

## 11. Concrete recursive checks, separate from the proofs

The framed theorem includes modes with nonparallel hyperbolic terminal pieces. For an explicit example take $`J=K_{7/19}`$. Its all-even expansion is

```math
\frac7{19}=1+[-2,-2,2,-2],
```

with signed count $`-2`$, while $`\beta=[3,4,2]`$ has signed count $`3`$, hence boundary slope $`10`$ and density $`2`$.

Take $`K=C_{2,3}(J)`$ and outer framing $`f=4\cdot10=40`$. The horizontal cable density and the total density are

```math
(2-1)|3-2\cdot10|=17,\qquad t_K=17+2\cdot2=21.
```

Use the eight-sheet system on $`\beta`$ with parameters $`(3,0)`$. Its four two-boundary components have ordinary HT plumbing-parameter types $`(1,0),(1,0),(1,0),(0,0)`$. In the standard [band-height convention](band-heights.md), §§12.1–12.3, the odd root is band 0, $`H_0=0`$, $`H_1=n_1`$ and $`H_2=n_2-H_1`$. The large bands are 0 and 1, so the corresponding large-height vectors in band order are $`(0,1),(0,1),(0,1),(0,0)`$. Projecting the eight inner labels modulo four joins the first and fourth child components into one outer piece, and the second and third into another. Both outer pieces have two boundaries and genus $`21`$. They are not ordinarily parallel: their multisets of child ordinary types differ, and the efficient internal comparison of §4.4 preserves those types. A balanced four-component pattern may attach all four outer boundaries. The theorem handles this whole family without replacing its interior chamber by a product.

A mixed sum mode is just as explicit. Let

```math
K=K_{7/19}\#T(2,-3),\qquad f=10-6=4.
```

Use the slope-10 HT system and the vertical slope-$`-6`$ torus system. For four section labels choose reflection constants $`3`$ and $`1`$, respectively; a relative cyclic shift realizes their difference. Their generated orbit is all four labels and has alternating signs. The density is $`1+2+0=3`$, so the resulting connected companion piece has four boundaries, $`\chi=-12`$, and genus five. This is a cancellation between nonzero child slopes at a nonzero outer framing, with a hyperbolic terminal block.

The standard-library diagnostics [check_recursive_framed.py](../scripts/check_recursive_framed.py) and [check_recursive_framed_independent.py](../scripts/check_recursive_framed_independent.py) check the peripheral identity, horizontal boundary-cycle counts, reflection orbits, cable descent, retained-component order, genus parity, and the exact rational and orbit data in these examples. Its finite checks are diagnostics only. Essentiality, ordinary invariance, the compression barrier, analytic exchange and CW continuity are proved or explicitly sourced above.

## 12. Sources and verification boundary

The [bibliography](../sources/bibliography.md) fixes the editions and printed scopes of [C], [K92], [HT], [H3], [PS] and [CW]. The official competition edition is dated 11 September 2026; its PDF fingerprint is `34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f`.

- [The recursive proof](recursive-and-fibred.md), §§2–6, supplies whole systems at finite slopes and ordinary roots; §§8–9 supply the envelope and closure; §10 contains the corrected whole-system compact-lift proof, with no descent of an upstairs isotopy.
- [The framed proof](framed-clusters.md), §§2–3 and 5–8, supplies peripheral classes, horizontal pattern pieces and the transverse return coordinate.
- [The zero-framed proof](zero-framed-clusters.md), §§3–10 and 12, supplies essential assembly, rooted path closure, face-compatible prisms, stationary-event conventions and explicit nonparallel systems.
- [CW, Part 7, Theorem D](../sources/bibliography.md#cw--component-wall-comparison) supplies the general component-wall comparison, including whole-component recombination and exact recovery. It supplies no contractibility conclusion by itself.
- [C], Definition 2.1 and Theorem B, pp.3–6; §3, pp.6–8; Lemmas 4.3–4.9, pp.9–12; §5, pp.12–20; and §6.3, pp.20–22, supply precisely the analytic and local exchange steps used in §8. The barrier replaces the global connected-output and non-splitting uses of linking indecomposability in Lemmas 6.1–6.2.
- [K92], pp.225–226, supplies geometric connectedness on the full, possibly disconnected, componentwise incompressible vertex set. Its historical disjointness/width equivalence is not used.

All conclusions use the unrestricted ordinary vertex sets of §1. Finite diagnostics do not certify essentiality, ordinary isotopy, the compression barrier, the analytic inputs or CW continuity. The [review record](../sources/review-status.md) distinguishes reviewed source arguments from the integrated proof. No formalization or exhaustive priority certification is claimed.
