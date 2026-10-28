# Arbitrarily framed parallel clusters of two-bridge knots

The framing is any integer. The proof retains the ordinary boundary-motion data and uses no sheet-number cutoff.

## 1. Statement

Let K be a nontrivial two-bridge knot. Fix its meridian–preferred-longitude basis (μ,λ), and put

```math
L=L_f(K;\varepsilon_1,\ldots,\varepsilon_n),\qquad
n\ge1,\quad f\in\mathbb Z,\quad
\varepsilon_i\in\{1,-1\},\quad d=\sum_i\varepsilon_i .
```

Here the components are winding-one parallels of slope δ_f=λ+fμ in the actual tubular neighbourhood of K. Coherently referenced components have pairwise linking f; the oriented linking of components i,j is ε_iε_j f.

Use the full ordinary reduced conventions of [the zero-framed cluster theorem](zero-framed-clusters.md) and Part 7: oriented, componentwise incompressible spanning systems, one oriented boundary on each labelled actual torus, no whole closed components, boundary free on its labelled torus, and ambient isotopies starting at the identity. Disconnected systems and arbitrary genus are allowed. X is the whole-open-complement cyclic-width-one flag complex; Y is the simultaneous geometric-disjointness complex. MS(L) denotes the **taut cyclic** complex of Przytycki–Schultens, as a subcomplex of X. All cyclic constructions use the one total linking class Φ.

**Theorem A (all integer framings).** For every K,n,ε,f above,

```math
|Y(L)|\ \searrow\ |X(L)|\ \searrow\ |MS(L)|,
```

where both arrows are strong deformation retractions. In particular X and Y are contractible.

The following sharper statements hold.

1. If fd≠0, then **X=Y=MS(L)**. Every vertex is connected, and, writing g=g(K),
```math
\chi(S)=|d|(1-2g)-|fd|(n-1),\qquad
g(S)=\frac{2-n+|d|(2g-1)+|fd|(n-1)}2 .
\qquad\text{(1.1)}
```
2. If d=0 and K is not a torus knot, the strong retraction ends in the pure pattern-annular cyclic subcomplex A_X, and **A_X=MS(L)**. For f≠0, a nonempty companion cut can occur only on a non-all-even HT carrier of boundary slope f. If no such carrier exists, X=A_X already.
3. If d=0, f≠0 and K=T(2,q), or its mirror, every vertex is annular, so **X=MS(L)**. At the regular-fibre framing τ_K=2q, including its sign, companion annuli are allowed. At other nonzero framings the companion is unused and X=A_X.

The f=0 assertions, including the torus-knot case, are exactly the [zero-framed cluster theorem](zero-framed-clusters.md). In item 2 they include that theorem when f=0.

**Theorem B (ordinary vertices and the point criterion).** Suppose fd≠0, and put r=|d|. The ordinary vertices of X are in bijection with the ordinary essential systems in E(K) consisting of r coherently oriented one-boundary Seifert surfaces. Equivalently, they are the all-even HT systems

```math
S_r(t_1,\ldots,t_{s-1}),\qquad 0\le t_i\le r,
\qquad\text{(1.2)}
```

modulo precisely HT Theorem 1(e)'s moves at coefficients ±2. This is a vertex description, not an assertion identifying all simplices with an unspecified subdivision.

Consequently X and Y are a point **if and only if** K has a unique ordinary incompressible Seifert surface. In terms of the unique all-even admissible expansion, this means that at most one coefficient has absolute value greater than two. Fibred two-bridge knots satisfy the criterion, but fibredness is not necessary.

In particular “fd≠0 always gives a point” is false. For K=K_{4/15}, n=2, ε=(+,+), f=1, there are at least two vertices, all of genus two. This does not obstruct contractibility.

## 2. Inputs and the framed peripheral calculation

The mathematical inputs are:

- [The zero-framed cluster theorem](zero-framed-clusters.md), Theorem A and §§3–4,8–10: the linear-chamber replacement for nonparallel multi-boundary HT pieces, including stationary-event ordering.
- HT, Theorem 1(b)–(e), Propositions 1–2 and the sheet/fold construction, printed pp.227–230,241–245. These statements classify a **whole disconnected essential union**, distinguish carriers, give the complete ordinary move relation, and give boundary slope and Euler characteristic for every sheet number.
- Essential cutting, reverse essential assembly and efficient torus/product comparison from [the geometric foundations](assemblies.md), in the form proved for arbitrary clusters in [the zero-framed cluster theorem](zero-framed-clusters.md) §2. The annulus/product proofs depend on essential parallel trace curves, not on their being preferred longitudes. Their use under the framing change is justified below.
- Part 7, Theorem D: for every non-split oriented S³ link on this full vertex set, X⊆Y and |Y| strongly deformation retracts onto |X|. Write R_D for its retraction. Its component-wall construction, ordinary whole-component packets and exact recovery on cyclic simplices are used in §7.
- PS, *Trans. AMS* 364 (2012), Theorem 1.1, printed p.1490: the taut cyclic complex MS(E,γ,α) is contractible. It is applied only after tautness is proved.

For n≥2 the actual exterior has the decomposition

```math
M=E(L)=Q\cup_T P,\qquad Q=E(K),\qquad
P=S^1_h\times B_n,\qquad h=\delta_f=\lambda+f\mu .
\qquad\text{(2.1)}
```

B_n is a disk with n actual holes and companion boundary b_0; χ(B_n)=1−n. Let μ_i be coherently referenced actual meridians, and let μ_0=μ on the companion side. In H_1(P), μ_0=Σ_i μ_i. If λ_i^0 is the individual preferred longitude of actual component i, its pattern fibre is h_i=λ_i^0+fμ_i. The total class and the oriented spanning boundary α_i are

```math
\begin{aligned}
\Phi(\mu_i)&=\varepsilon_i,&
\Phi(\lambda_i^0)&=f(d-\varepsilon_i),&
\Phi(h)&=fd,\\ 
\alpha_i&=\varepsilon_i\lambda_i^0-f(d-\varepsilon_i)\mu_i
          =\varepsilon_i h-fd\,\mu_i,&
\Phi|_Q&=d\psi ,
\end{aligned}
\qquad\text{(2.2)}
```

where ψ(μ)=1, ψ(λ)=0. The longitude coefficient of α_i is ε_i and Φ(α_i)=0. It is primitive because its coefficients in (h,μ_i) are (ε_i,−fd). Thus (2.2) is the actual spanning slope, including the linking correction; it is not ε_i times the individual preferred longitude when d≠0.

At T, Φ(h)=fd and Φ(μ)=d. Hence, when d≠0, the primitive kernel slope is **λ=h−fμ**, not h. When d=0, the class on all of Q vanishes; the actual curves are ε_i h and the essential pattern annuli force the companion slope **h=δ_f**.

This is the two-bridge version of the framed mode calculation. In the balanced case its modes are the HT expansions β satisfying

```math
m(\beta)=2\bigl(\sigma(\beta)-\sigma(E)\bigr)=f ,
\qquad \sigma(\beta)=\#\{b_i>0\}-\#\{b_i<0\},
\qquad\text{(2.3)}
```

where E is the unique all-even expansion.

All pieces in (2.1) are irreducible and boundary-incompressible. The usual innermost-circle argument for a sphere cut by T proves M irreducible; the amalgam normal form retains the actual boundary-group injections. Thus L is non-split. Alternatively, for f≠0 this follows directly from the nonzero pairwise linking across every partition. Actual spanning disks are excluded by the boundary-group injection. For n=1 the link is isotopic to K, independently of f, and HT already gives X=Y=MS(K); its framing is not a new knot type.

Minimising the number of T circles makes all circles and cut pieces essential, including boundary-incompressibility and exclusion of boundary-parallel cut annuli. The proof uses primitive-annulus straightening and an innermost empty product, by the essential-cut argument in [the geometric foundations](assemblies.md). It applies equally to the basis (h,μ), which is unimodular, or to the horizontal traces λ. Conversely, compatible essential cut pieces assemble incompressibly: an outermost arc of a hypothetical compression disk across T would boundary-compress a cut piece. Whole closed components must be excluded after assembly. No acyclicity assumption is imposed on the surface assembly graph.

For later ordinary comparisons, an empty product meets T in annuli. A whole T in the product would inject Z² into a free group, which is impossible. An innermost returning annulus would make a whole cut annulus boundary-parallel. The remaining spanning annuli straighten simultaneously to product annuli, so the product pushes preserve T. These are the product-annulus arguments of [the geometric foundations](assemblies.md), with no longitude-specific step.

The potential spanning-bundle degeneration is handled as follows. If d=0, Φ kills the injected Z² of T and cannot be a compact spanning fibration. In the coherent case of §3, if a whole spanning surface is a fibre, cut the fibration at T. All T traces are coherent, so its annuli in a fibre product span, and straighten to products. Every Q chamber is then a product between successive one-boundary pieces; Q fibres over the circle. HT then makes K fibred and its ordinary coherent Q system unique. Thus the degeneration cannot identify two distinct Q systems in the proof of Theorem B. This also handles finite simultaneous families and shared whole-component packets.

## 3. Nonzero fibre evaluation: all vertices are already taut

Assume fd≠0 and n≥2; the n=1 case was handled in §2 and satisfies (1.1) directly. An essential pattern component carrying an actual curve α_i is horizontal: its boundary has intersection |fd| with h, so it cannot be vertical. A horizontal component covers **all** B_n and meets every actual torus. Since each actual torus is used once, there is exactly one such component H. No other horizontal component is possible. Nor is an additional essential vertical component possible: H meets every boundary torus transversely to the fibre, so a vertical annulus would intersect it there. Whole closed components were excluded. Consequently the entire P cut is this one connected H.

Here is an explicit classification and existence check. Choose u:B_n→R/Z with degrees ε_i on μ_i, and define

```math
F_P(\theta,b)=fd\,\theta+u(b)\pmod1 .
\qquad\text{(3.1)}
```

It is a submersion with cohomology class Φ|_P. A fibre is a cyclic |fd|-sheeted cover of B_n. On an actual boundary its monodromy step is ε_i up to the common sign convention for cyclic sheet labels, hence generates the sheet group. Thus the fibre is connected, has one boundary on each actual torus, and has r=|d| boundaries on T, because gcd(|fd|,|d|)=r. These T curves have primitive slope λ; their orientations as boundaries of the attached Q pieces are coherent with sign d. The induced H-boundary orientations there are opposite. Each covers b_0 with degree |f|. Thus

```math
\chi(H)=|fd|(1-n).
\qquad\text{(3.2)}
```

Every horizontal cut in this class is ordinarily isotopic to such a fibre. To see this without assuming Q fibred, project it to B_n. Its |fd| ordered points in each oriented circle fibre define a map into the unordered circular configuration space. That space has contractible spacing fibres over its rotation circle. Isotoping the spacings to equal ones leaves exactly the cohomology data in (3.1). The unit actual degrees make this class primitive. This is also the usual horizontal classification in the product P.

The Q boundary consists of exactly r coherent longitudes. HT purity applies to the whole essential union. An odd-carrier orientable component has an even number of longitude boundaries and relative class zero: a connected nonseparating oriented surface has primitive relative class, whereas that even signed sum cannot be ±η. It cannot have only coherent boundaries. Hence the Q union is on E, and HT Proposition 1 makes every component a one-boundary Seifert surface R of genus g(K). There are exactly r of them, all with the sign of d.

All these R's attach to the one H. The whole spanning surface is therefore connected, and (3.2) gives (1.1). Such surfaces exist: attach r parallel minimum-genus Seifert surfaces to H; essential assembly proves incompressibility.

Every incompressible spanning vertex has the same negative Euler characteristic. A Thurston-norm minimiser for the prescribed boundary can be reduced to an incompressible spanning system: remove whole closed components and compress if necessary, retaining the prescribed actual boundary. No disk component is possible. It is therefore among the vertices just classified and has the same −χ. All vertices are taut. Thus X=MS(L).

For completeness, geometric and cyclic complexes coincide in this case. For a finite disjoint family of connected spanning surfaces, collapse complementary chambers to its dual graph G. Each edge is nonseparating, and the cohomology class dual to each edge pulls back to the same primitive Φ. The collapse is surjective on H_1, by joining crossing arcs inside chambers. It follows that b_1(G)=1. A connected graph without bridges and with b_1=1 is a circle; its edges are coherently oriented by Φ. Cutting at any one edge shows that all other surfaces lie in cyclic order in the one whole complement block. Distinct disjoint members have cyclic width one. Hence every Y simplex is an X simplex; the converse is Part 7. We have proved X=Y=MS(L), and PS proves it contractible.

## 4. Ordinary gluing and the point criterion

Continue with fd≠0, n≥2. A coherent Q system determines a vertex, not a vertex together with an additional twisting integer.

Fix the ordinary Q system and the unique ordinary H of §3. Restrictions of their identity-starting isotopies to T take values in the configuration space C_r of r unordered parallel longitude curves. Up to contractible straightening data this is a circle; its fundamental generator moves each curve to the next one. Boundary-isotopy extension gives path lifting. Therefore the ordinary gluing states, before quotienting return motions, form a torsor for π_1(C_r)=Z. Loops of the two cut-system spaces act by their boundary restrictions. Equivalently, this is the path-component calculation for their fibre product over C_r. Tangential motion of an unparametrised boundary curve is absorbed in its surface collar and introduces no second annular framing.

The pattern return already surjects onto that Z. In the model (3.1), rotate the fibre coordinate through

```math
\theta\longmapsto\theta+\frac{t}{fd},\qquad 0\le t\le1 .
\qquad\text{(4.1)}
```

This carries H=F_P^{-1}(0) to F_P^{-1}(t) and returns to the same whole unmarked H at t=1. It returns each actual boundary curve to itself. On T, h=fμ modulo λ, so the normal displacement is 1/d: exactly one step in the r-curve configuration, with its sign. Thus the image of the pattern-loop group contains a generator. It kills every gluing state; no property of the Q loop group is required. More explicitly, choose paths from the two reference cut systems to a matched pair. Their boundary paths give a loop in C_r; changing the pattern path by (4.1) changes that loop by one generator without changing its endpoint. This makes its class zero, and boundary-isotopy extension then gives a matched path of whole assemblies. This explains the quotient even when the Q pieces have different ordinary types.

Conversely the ordinary Q system is an invariant of the whole vertex. Efficient ordinary comparison uses the T-preserving product pushes of §2. All comparison traces here are longitude curves, and all Q components are essential one-boundary positive-genus pieces. Product returns cannot delete such pieces. If the bundle exception occurs, the final paragraph of §2 makes Q fibred and gives its unique coherent ordinary system anyway. Thus two assembled surfaces with distinct Q systems cannot be isotopic.

This proves the bijection of Theorem B. HT's complete classification identifies its domain with (1.2). In particular this vertex set is finite, although no finite enumeration is used to prove the bijection or its tautness.

If every one-boundary R is ordinarily isotopic, any finite disjoint collection of them is jointly parallel: the incompressible parallelism/product theorem places consecutive isotopic copies in product regions. There is then one coherent r-system and hence one vertex. If R_0 and R_1 are not isotopic, the two systems of r parallel copies R_0 and r parallel copies R_1 are not isotopic either: an isotopy of the entire union must carry each connected component to an isotopic component. The bijection gives two distinct vertices. The n=1 assertion is the same statement directly for K. HT's Seifert-surface corollary, printed p.230, gives the stated all-even-coefficient criterion.

For an explicit failure of universal single-vertex rigidity,

```math
4/15=[4,4]=\frac1{4-1/4}.
```

There are two one-sheet all-even surfaces R_0=S_1(0), R_1=S_1(1). Neither coefficient is ±2, so HT Theorem 1(e) has no move identifying them. Both have genus one. For n=2, d=2, f=1, take the same connected four-boundary horizontal H with χ(H)=−2 and attach two copies of R_j. The resulting S_j is essential, connected, has χ=−4 and genus two. Its Q cut is S_2(0), respectively S_2(2), again distinguished by the complete HT relation. Theorem B makes S_0 and S_1 distinct ordinary vertices of X=Y=MS(L).

A coherent companion system consisting of unique fibres has just one ordinary class. The two-bridge horizontal pattern is just as anchored, but it does not identify distinct ordinary companion Seifert systems.

## 5. Balanced nonzero framing: HT modes, chambers and the exceptional annulus

Now d=0 and f≠0. Actual boundaries are ε_i h. At efficient intersection every actual-bearing pattern piece is vertical. If the companion is nonempty, some actual component must reach it; otherwise everything outside the actual-to-actual annuli would be a forbidden whole closed component. Such a reach forces slope h on every T curve. The entire pattern system simultaneously verticalises. Thus the Q union is an essential HT union of slope f, as in (2.3).

**Lemma 5.1 (sloped oriented HT dichotomy).** If K is not a torus knot, every connected piece in this union is separating, has an even boundary count a≥2, and has positive genus. On a length-s carrier,

```math
\chi(F)=a(1-s),\qquad
g(F)=1+\frac{a(s-2)}2,\qquad s\ge2.
\qquad\text{(5.1)}
```

**Proof.** The all-even carrier has slope zero and cannot occur. An oriented component on an odd carrier covers the nonorientable one-sheet plumbing with even degree, equal to its boundary count a. Alternatively, its relative class vanishes directly from the nonzero slope: if its signed boundary sum is k(λ+fμ), it must lie in the longitude image of H_2(Q,T). Since f≠0, k=0, and the injectivity of that boundary map gives [F]=0. A connected two-sided proper oriented surface with zero relative class separates.

The sheet construction gives χ=a(1−s). A length-one admissible expansion would have p/q=r+1/b, so K would be a (2,|b|) torus knot or its mirror; for a knot |b| is odd. Otherwise s≥2, and (5.1) proves positive genus. Unlike the zero-slope proof, this proof does **not** assume s even. ∎

The chamber order is exactly the one needed by the [the zero-framed cluster theorem](zero-framed-clusters.md) replacement and does not require the pieces to be parallel. Choose an odd root band. For the whole N-sheet union its transported folds have form i↦c_ν−i, ν=1,…,ℓ, all c_ν odd; normalise the root to c_1=−1. Put

```math
e=\gcd(N,c_2-c_1,\ldots,c_\ell-c_1),\qquad
q=e/2,\qquad a=2N/e .
\qquad\text{(5.2)}
```

For ℓ=1 the convention is e=N; in particular this includes the two-boundary positive-genus case. Orientation makes N,e even. The component orbits are residues modulo e paired by t↔e−1−t. There are q pieces, all with a boundaries, and their actual cyclic label word on T is

```math
(0,1,\ldots,q-1,q-1,\ldots,1,0)^{a/2}.
\qquad\text{(5.3)}
```

Every piece separates, so its edge in the chamber graph is a bridge. Following the transverse meridian crosses all distinct labels 0,…,q−1 successively. A tree with such a walk containing every edge must be that path. End chambers meet T in a/2 annuli and interior chambers in a annuli. Adjacent pieces may have distinct HT types and the interior chamber need not be a product. Restricted actual sheets, not independently normalised pieces, give their types.

The proof of (5.2)–(5.3) is the point/reflection proof of [the zero-framed cluster theorem](zero-framed-clusters.md) Lemma 3.3. It uses no signed-count equality with E and no assumption that the slope is zero. It works for arbitrary N. A joint family has one carrier and one common a; a subcollection inherits its path order.

Here is the annular exception, with no appeal to a positive-genus normaliser. For K=T(2,q), q≥3 odd, use p/q=1/q. The two admissible expansions are [q] and 1+[−2,…,−2], with q−1 copies of −2. Indeed r=0 forces b=q; r=1 successively forces −2 until the tail terminates. Their slopes are τ_K=2q and zero, respectively; mirroring reverses the signs. At f=τ_K the nonempty Q pieces are precisely the two-sheet annuli on [q]. All pattern pieces are annuli too. Every retained whole actual-bearing component is therefore an annulus. At f≠0,τ_K there is no Q cut and all pieces are pure pattern annuli. In both cases −χ=0 for every vertex, so X=MS(L). PS applies, including norm zero. This proves Theorem A(3). No no-return assertion is made for these genus-zero companion annuli.

## 6. Framed ordinary motion and natural root ends

Assume henceforth K is not a torus knot, d=0, f≠0. We verify the new ordinary-motion input before using the old closure.

The normal coordinate to δ_f is the quotient

```math
H_1(T)/\langle\lambda+f\mu\rangle\cong\mathbb Z,\qquad
\nu_f(a\lambda+b\mu)=b-fa .
\qquad\text{(6.1)}
```

Thus ν_f(μ)=1, ν_f(λ)=−f and ν_f(δ_f)=0. Tangential trace motion contributes zero, while a preferred-longitude track generally contributes **−f**, not zero. We do not claim that the change of basis extends to a homeomorphism of Q.

**Lemma 6.1 (framed no return).** Let F⊂Q be a connected essential separating positive-genus surface with a≥2 boundaries of slope δ_f. An identity-starting return fixing its boundary occurrences individually has zero normal winding ν_f. A return of a finite unmarked oriented system of such pieces has neither nonzero configuration winding nor a nontrivial cyclic boundary permutation.

**Proof.** Attach one reaching annulus to every boundary of F, ending at a different labelled actual f-framed parallel. Since F separates, its oriented boundary sum is zero. The auxiliary a-parallel link is balanced, and (2.2) makes its actual spanning curves exactly the signed pattern fibres h=δ_f. It is an essential spanning assembly.

A return of F with normal winding m would identify this assembly with its m-fold outer-pattern-twisted version. Place the two comparison F copies at different levels in one fixed F collar. Their boundary annuli lie in disjoint proper strips in the transverse μ coordinate of T; δ_f and μ have intersection one. Use the T-preserving empty-product simplification from §2. Every Q horizontal face in such a product is an entire F copy: there is no companion intersection or actual boundary at which a proper face could end. The two parallel separating copies cut Q into three chambers. Only their middle collar slab has both copies on its frontier, so every Q product lies there. Non-final product pushes can stop at a nearby collar level, preserving this confinement. Products missing Q fix T.

Consequently the constructed comparison transports each boundary in its original proper strip, with zero normal winding. After removing this confined transport, a reaching tether in the product base detects the remaining outer twist. In H_1(B_a,b_j) its difference is m[b_0]. The class [b_0] is nonzero modulo [b_j], since there is another actual hole. Thus m=0.

This is the full-face/middle-slab proof of [the zero-framed cluster theorem](zero-framed-clusters.md) Lemma 4.1 applied to (δ_f,μ). Its auxiliary spanning assembly remains valid precisely because the auxiliary signs balance. In particular it measures b−fa in the original (λ,μ) basis; it has not discarded the longitude term.

For a system return, take a finite power fixing every piece, orientation and boundary occurrence. Restrict to one piece and apply the first part. A nontrivial cyclic permutation becomes a nonzero integral transverse winding in that power, so it is excluded too. ∎

**Lemma 6.2 (ordinary rooted order).** A chosen odd root band and its outside normal gap give an ordinary end of the chamber path, natural under retaining actual components and deleting colours from a simultaneous family.

**Proof.** HT's complete moves occur at ±2 coefficients, so they can be supported off the chosen odd root section, even when an adjacent plumbing parameter changes. Retain actual root sheets and plumbing rectangles, then compress their order. The retained set is invariant under root reversal i↔N−1−i; compression preserves that reversal and the outside gap. This is exactly the restricted-sheet argument of [the zero-framed cluster theorem](zero-framed-clusters.md) Lemma 4.2. If two ordinary normalising comparisons gave different transported ends or orders, their concatenation with the root-preserving complete move path would give a forbidden boundary return in Lemma 6.1. No slope-zero assumption occurs. ∎

Efficient torus comparison is valid here without a bundle exception because Φ|_Q=0. Pattern return loops have zero transverse winding by the same anchored tether test: the pure product base and its actual holes are unchanged. Tangential h motion is absorbed in a fibre collar. Thus there is no quotient by a sign-word period, nor by a fictitious independent longitude motion. Ordinary gluing data and the retained root order are genuine, as required for the parent.

## 7. One-sided closure and the cyclic strong retraction

We give the replacement argument, specifying which facts survive the framing change. Fix a slope-f carrier β and a common even arity a. Let X_{β,a} be the induced cyclic sector consisting of vertices with Q cut empty or consisting of pieces on β of arity a, and let Y_{β,a} be the full geometric subcomplex on the same vertices. Write A_Y for the pure pattern-annular geometric subcomplex. Thus every sector contains A_X, respectively A_Y.

For a nonempty Q cut, order its pieces F_0,…,F_{q−1} from the root end, with w_i=+ when its coorientation points along the path. The negative-side original chambers are the first end when w_0=+, an interior chamber when (w_i,w_{i+1})=(−,+), and the last end when w_{q−1}=−. For the positive side reverse the signs. Select the side containing the root end. On either chosen side the eligible chambers' incident sets of **whole original pieces** are disjoint.

Resolving one such chamber replaces every incident F_i by that chamber's annular faces on T, pushed slightly into P, and pushes the rest to the chosen side. Orient the caps using the chamber boundary; its incident faces lie on one chosen side, so the actual oriented boundary is preserved. This is a replacement by a chamber boundary, not an assertion that a nonproduct chamber is a parallelism. Operations at different eligible chambers commute because their endpoint sets are disjoint. The original surface stays as a barrier. Compose the annular pattern paths literally; do not delete a closed component with retained Q pieces yet.

**Closure claim.** Every new boundary-parallel outer return identifies exactly one unselected original one-sided chamber. Indeed, its empty disk D in B_n has no actual hole. An old essential arc cannot enter D: it cannot cross the new system, end at an actual hole there, or be an old essential return entirely inside an empty disk. Thus D contains no old trace point. Its two new endpoints lie in one old gap, which contains at most the two pushed faces adjacent to that gap. By (5.3), this is either an end turn or the gap between two consecutive pieces in a monotone block. It identifies the stated one-sided chamber and certifies that its whole incident pieces remain.

Resolve every enabled such chamber, starting with the root end. Enabling is monotone: a witness is a complete path between the surviving endpoints of that chamber, while operations elsewhere have disjoint endpoints and cannot change that path or its empty-disk class. On the finite set of original chambers there is a unique least closed selected set. At termination all retained Q pieces are original essential pieces and all remaining pattern annuli are essential. Delete whole closed components now. Essential assembly gives an incompressible spanning parent p(S). It retains a definite ordinary subcollection, and

```math
q(p(S))\lt q(S),\qquad
q(S)=\frac{\chi(S)}{a(1-s_\beta)} .
\qquad\text{(7.1)}
```

The denominator is negative by Lemma 5.1. The genus and number of boundaries need not be bounded. Lemmas 6.1–6.2 make the root, caps, disk tests and retained subcollection ordinary invariants. Put p(v)=v for v∈A_X.

There is a relative version. If the seed piece is first in a simultaneous full family, its end chamber is empty of other colours. A later repair disk excludes the essential old pattern arcs and trace points of **every** colour. Uniform arity and the repeated word (5.3) imply that another Q piece in the proposed chamber would have a trace in that same gap. It cannot be there. Thus every repair can be performed disjointly from the whole family and preserves all surviving relative positions. Pure annular members are also avoided by this disk barrier. This is the all-family assertion; a separate contraction for each of two terminal paths would not suffice.

Iterate p. Each event is labelled by its first retained Q piece in the original root order; the labels strictly increase. For a cyclic simplex restore the coloured occurrences of shared **whole actual-bearing components** using Part 7's component-wall exact-recovery family, rooted at the selected Q end. The integral difference potentials form a nested zero-one chain, so their phase intervals give one realisable coloured order; deleting a coefficient deletes its intervals. Lemma 6.2 supplies the inherited order of distinct companion pieces. This uses one original Φ-cover; Q copies or individual negatively oriented pieces do not receive independent constants.

Merge genuine parent events in this coloured order. **Place every stationary annular event after all genuine events, using the restriction of one fixed total order on the annular vertices.** At each genuine event its seed is first in the current whole family, so the relative barrier applies. Current states and the union of successive states have simultaneous disjoint whole representatives.

For each vertex v place its finite trajectory at heights j/ℓ(v), using heights 0,1 for a stationary event. The affine graphs of the current vertex heights cut |σ|×I into the usual prism slabs, each spanned by the current state and the one new trajectory point. Mapping those points to their ordinary vertices gives a map

```math
K_{\beta,a}:|X_{\beta,a}|\times I\longrightarrow |Y_{\beta,a}|.
\qquad\text{(7.2)}
```

It begins at inclusion, ends in A_Y, and fixes A_X. On a face, deleted-vertex slabs have zero thickness, and the remaining heights and event order are unchanged. Thus the maps agree on all faces. Every closed simplex cylinder has finite event count and finite image, proving continuity in the weak/CW topology.

These are the [the zero-framed cluster theorem](zero-framed-clusters.md) §§8–9 prisms: the complete new inputs needed to reuse them are (5.1)–(5.3), the framed ordinary return calculation (6.1), and Lemmas 6.1–6.2. The closure proof above does not use product interior chambers, preferred-longitude boundary, even carrier length, or a single path in the global surface assembly graph.

Compose (7.2) with R_D. This retraction stays in the sector: it recombines entire original actual-bearing components, retaining only essential Q pieces of the same simultaneous HT carrier and arity. It does not perform arbitrary reconnection of partial Q pieces. Exact recovery fixes every cyclic point initially, and fixes A_X throughout. Therefore

```math
|X_{\beta,a}|\ \searrow\ |A_X|.
\qquad\text{(7.3)}
```

No generic multi-boundary level is declared essential, and no closed-component deletion is presumed to preserve cyclic adjacency; all prism states were first proved geometric before R_D is applied.

## 8. Gluing, tautness and completion

For non-torus K, d=0, f≠0, essential cutting gives the complete sector decomposition

```math
X=A_X\ \cup\ 
   \bigcup_{\substack{\beta:\,m(\beta)=f\\\beta\ {\rm not\ all\ even}}}
       \ \bigcup_{a\in2\mathbb Z_{>0}}X_{\beta,a},
\qquad\text{(8.1)}
```

with A_X included also when there are no nonempty sectors. Distinct nonannular sectors intersect exactly in A_X. No simplex mixes them: a cyclic simplex has simultaneous efficient representatives; HT purity forces one carrier for their entire union, and (5.2) forces one common connected arity. These facts are about the chamber path in Q, and do not prohibit branching or cycles of the assembled actual-bearing surface.

All maps (7.3) fix A_X pointwise. They glue to a strong retraction of X onto A_X; every closed simplex is in one sector and has a finite image cylinder. Neither unbounded arity nor unbounded genus causes a continuity exception.

The endpoint is precisely taut. A balanced actual system has a pure pattern-annular representative: match positive and negative holes by disjoint essential arcs in the planar B_n and take their h-products. Hence the minimum norm is zero. Every nonempty Q sector has negative Euler characteristic by (5.1), while its pattern pieces have χ=0; its spanning system therefore has positive norm. Thus

```math
A_X=MS(L).
\qquad\text{(8.2)}
```

This also proves A_X contractible by PS, without assuming that arbitrary geometric annular simplices are cyclic.

In the torus resonance case §5 already gives X=MS(L); away from resonance it gives X=A_X=MS(L). For f=0 use the full [zero-framed retraction](zero-framed-clusters.md), which includes the all-even circular-envelope sector and all zero-slope odd sectors. For n=1 use HT directly. These cases exhaust every f,n,ε,K and prove the second arrow of Theorem A.

To apply PS in every case, M is irreducible and boundary-irreducible as in §2, each actual boundary curve (2.2) is a single primitive nonseparating curve on its torus, and H_2(M)→H_2(M,∂M) vanishes for an S³ link exterior. The class is PD(Φ), with the prescribed oriented boundary. Thus its taut **cyclic** complex is exactly the MS(L) used here. PS supplies its contractibility, including balanced norm-zero cases.

Finally let H_D be the given strong deformation of Y onto X, and H_X the deformation onto MS(L) just proved. The concatenation

```math
H_Y(y,t)=
\begin{cases}
H_D(y,2t),&0\le t\le\tfrac12,\\ 
H_X(R_D(y),2t-1),&\tfrac12\le t\le1
\end{cases}
\qquad\text{(8.3)}
```

fixes MS(L) pointwise and strongly deformation retracts Y onto it. Theorem A and Theorem B follow.

## 9. Explicit slope check and limits of the conclusions

For K_{7/19}, the admissible expansions and slopes in this convention are

| Integer part | Expansion | Slope |
|---|---|---:|
| 0 | [2,−2,−2,−3] | 0 |
| 0 | [3,3,−2] | 6 |
| 0 | [3,4,2] | 10 |
| 1 | [−2,−3,−2,−3] | −4 |
| 1 | [−2,−2,2,−2] (all even) | 0 |
| 1 | [−2,−2,3,2] | 4 |

Each equality is an exact minus continued fraction. Completeness of this short list follows by choosing, at each reciprocal step, the floor or ceiling with absolute value at least two; every admissible remaining tail has absolute value less than one and its numerator decreases. It is a carrier calculation, not a sheet-number enumeration. In particular, for balanced parallels and nonzero f∉{−4,4,6,10}, X=A_X already. At the four listed nonzero slopes, §§5–8 handle **all** even arities and all HT parameters, not just finitely many examples.

There is no unresolved framing, sign, count, slope, or genus case within the stated two-bridge range. The point assertion is conditional exactly as in Theorem B; it is not weakened to fibred companions and is not asserted for all nonfibred companions. No complete combinatorial description of all simplices in (1.2) is claimed. In particular we do not assert an edgewise-subdivision formula without proving it.

The proof does not cover general satellite companions. Their nonzero-slope systems need not have the HT uniform-arity path word, and their coherent essential spanning pieces need not all have genus g(K).

## 10. Sources and exact diagnostics

See [HT, PS, B, H3 and CW](../sources/bibliography.md) for the editions and printed page ranges. The zero-framed case is proved in [its own proof page](zero-framed-clusters.md). The essential-cut and ordinary-comparison arguments are explicit in §2; they are not a claim that a peripheral basis change extends across the companion exterior.

The author's `scripts/check_framed_clusters.py` checks the peripheral class, connected horizontal covering, Euler/genus parity, return displacement, framed normal coordinate and complete rational examples. The independent `scripts/check_framed_independent.py` uses bounded continuants and actual permutations rather than importing that implementation. [Replay instructions](../scripts/README.md) state their finite ranges and limits.
