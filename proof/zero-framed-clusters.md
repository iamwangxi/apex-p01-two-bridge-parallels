# Zero-framed parallel clusters of two-bridge knots

All numbers, signs and genera are unrestricted within the zero-framed two-bridge range.

## 1. Statement and the two new interfaces

Let C be a nontrivial two-bridge knot. Let L consist of n≥1 labelled, zero-framed parallels of C, with signs ε_i∈{+1,−1} relative to a fixed orientation of C. Put d=Σ_i ε_i. Use the full reduced ordinary spanning conventions: surfaces are oriented and componentwise incompressible; disconnected surfaces are allowed; every actual boundary torus is used once; closed components are forbidden; boundary curves move on their labelled tori; isotopies start at the identity. There is no genus or norm restriction.

Write X for the flag complex of minimum whole-open-complement cyclic width one, and Y for the original simultaneous geometric disjointness complex. The cyclic cover always uses the one total oriented linking class Φ. No independent deck constants are assigned to companion components.

**Theorem A (parallel clusters).** For every such C,L, the entire complexes X(L) and Y(L) are contractible. More precisely:

1. If d=0, let A_X be the full cyclic subcomplex of pure pattern-annular vertices. Then |X(L)| strongly deformation retracts onto |A_X|, and A_X is contractible.
2. If d≠0, |X(L)| strongly deformation retracts onto its taut cyclic subcomplex MS(L). This subcomplex is contractible by Przytycki–Schultens, Theorem 1.1.
3. The component-wall comparison, Part 7 Theorem D, gives X⊆Y and |Y|↘|X|. It therefore gives the geometric conclusion too.

In the balanced case A_X is exactly MS(L). Thus the two cases together prove the uniform statement |X(L)|↘|MS(L)|. Concatenating with the given comparison also gives |Y(L)|↘|MS(L)|.

The new geometric point in the balanced case is that a whole oriented odd-carrier HT system has **linear complementary-region incidence even when its components are not parallel or isotopic**. The one-sided chamber closure only needs this incidence and its port-interval structure, not a product between consecutive components. The new even-carrier point is a circular-height envelope. It removes cancelled one-boundary pieces using generic levels, where every actual-bearing output is automatically essential. It does not require the companion Seifert surfaces to be fibres.

Neither argument replaces a connected multi-boundary companion by disconnected arcs. The topology of each retained companion piece is preserved. The proof below distinguishes circles of one-boundary pieces from paths of separating multi-boundary pieces.

## 2. Geometric and printed inputs

For n≥2 write

```math
M=E(L)=Q\cup_T P,\qquad Q=E(C),\qquad
P=S^1_\lambda\times B_n,
```

where B_n is a disk with n actual holes and one companion boundary b_0. Thus it has n+1 boundary circles. The fibre is the preferred longitude λ. If ψ is the positive knot class on Q, then Φ|_Q=dψ. Actual preferred spanning slopes are ε_iλ, since all pairwise linking numbers are zero.

We use the following inputs in their precise ranges.

- HT, Theorem 1(b)–(e), printed p.228, Propositions 1–2, p.230, and their sheet construction and folding proof, pp.227,242–245. A whole disconnected essential bounded union lies on one carrier; restricting its sheets to a component retains that carrier. All-even components have one boundary and the same genus g(C). Odd-carrier oriented components have even boundary count and zero relative class. Rooted transported fold constants and restricted-sheet counts are spelled out in [rooted band heights](band-heights.md) and [component partitions](assembly-obstruction.md).
- Essential cutting, relative simultaneous verticalisation and efficient torus comparison, as proved in [essential cutting and ordinary comparison](assemblies.md), together with the arguments in this section. Their proofs apply to a disk with any number of actual holes. The spanning-bundle exception is impossible in the balanced auxiliary constructions because the injected group π_1(T)=Z² is killed by Φ, whereas a compact spanning fibre has free fundamental group.
- Banks, arXiv:1109.0965v1, Proposition 4.2, Remark 4.4 and Proposition 4.10 with the explicit all-incompressible extension in §10. These supply product simplification and class-minimum width. No generalisation is inferred merely from a taut PS statement.
- The component-wall comparison, Part 7 [CW, Theorem D and its proof, Part 7, §9](../sources/bibliography.md#cw--component-wall-comparison). Denote its retraction by R_D:|Y|→|X|. It uses Sakuma Proposition 4.9(1)–(2), printed p.883, in the all-incompressible range. Its phase construction and exact recovery on cyclic simplices are used below. It is a comparison, not an assumed contraction.
- PS, *Trans. AMS* 364 (2012), Theorem 1.1, printed p.1490: the taut cyclic complex MS(E,γ,α) is contractible under the link-exterior hypotheses. This input is used only after §6 proves precisely which vertices are taut.

The packet closure and prism arguments are proved below with the weaker, explicitly verified linear-region hypothesis. In particular we do not cite its fixed-parallel-packet theorem as if it covered nonparallel HT components.

At efficient T-intersection every cut piece is essential. A reaching pattern annulus forces all T traces to be longitudinal, and the entire pattern system simultaneously verticalises. If there is no reach, any nonempty companion assembly would be a forbidden closed global component. Conversely compatible essential pieces glue incompressibly: an outermost T arc of a hypothetical compression disk would boundary-compress a cut piece, until the disk lies in one incompressible piece. This argument allows cycles in the **surface assembly graph**.

The geometric torus comparison concerns a different graph. An empty horizontal product meets T in essential annuli. A whole T cannot inject into its free group; a returning annulus would give a boundary-parallel cut annulus; spanning annuli straighten to products. Product simplification may therefore preserve T and its whole common boundary path. The argument also works for a finite coloured disjoint family, retaining common entire components by the component-wall packet convention.

For clarity, the unbalanced case does not use the false assertion Φ|_T=0. Lemma 3.1, which needs only essential cutting and HT, makes every companion piece one-boundary in that case. An outer return would close two such pieces into a forbidden closed component. Thus each actual-bearing global component is either one R with one actual torus or an annulus with two opposite actual signs. For n≥2,d≠0 none meets all actual tori, so none can be a whole spanning fibre of M. This excludes the bundle degeneration in the unbalanced comparison independently of the balanced kernel argument.

These facts imply irreducibility and boundary irreducibility of M: the piece groups and every boundary torus group inject across T. Thus L is non-split. Its actual longitudes are nontrivial, so no actual disk component occurs. The case n=1 is separated at the end: HT already makes every vertex taut.

## 3. HT systems have circular or linear chamber order

Use minus continued fractions and label a carrier by its complete admissible expansion. The zero-slope carriers are precisely those whose signed coefficient count equals that of the unique all-even expansion E. There are finitely many carriers. No finite sheet-number cutoff is used.

**Lemma 3.1 (purity and class dichotomy).** A nonempty efficient companion union lies on one zero-slope HT carrier. If it is all-even, every component R has one boundary, genus g(C), and class +η or −η, where ∂η=λ. If it is odd, every oriented component has even boundary count, class zero, separates Q and has positive genus. Consequently d≠0 forces the all-even carrier.

**Proof.** HT applies to the entire essential union, and its complete isotopy statement excludes mixed carriers after restricting to components. All-even sheet components have degree one by HT Proposition 1. Their one-sheet plumbing is orientable and has genus s_E/2=g(C).

An oriented cover of the nonorientable one-sheet odd plumbing has even degree, equal to its number of longitude boundaries. A connected nonseparating oriented proper surface in a knot exterior represents a primitive class: close a once-crossing arc in its complement. An even signed longitude sum cannot be ±η. Thus the class is zero and the component separates. On a length-s zero-slope carrier its Euler characteristic is a(1−s) and genus 1+a(s−2)/2. The all-even length is even, and equality of signed counts makes every zero-slope length even. Nontriviality gives s≥2, so the genus is positive. The total companion class is dη, proving the last assertion. ∎

The chamber graph of a cut system has a vertex for every Q-complement component and one edge for every connected companion surface. It is not the global surface assembly graph.

**Lemma 3.2 (circular all-even chamber order).** The chamber graph of a nonempty all-even system is a circle, with one edge for each one-boundary component. Orient every such edge using +η. All edges then point consistently around that circle. Components and complementary chambers need not be mutually parallel products.

**Proof.** Each component is nonseparating in Q, so its graph edge is not a bridge. Collapsing the cut surfaces gives a surjection π_1(Q)→π_1(graph). Since H_1(Q)=Z, the graph has first Betti number at most one. A connected finite graph with an edge, no bridges and Betti number at most one is a circle, including the one-loop case. A positive companion meridian crosses every boundary circle once and each +η piece positively, so it traverses that circle once in its consistent orientation. ∎

**Lemma 3.3 (linear odd chamber order).** In every nonempty oriented odd-carrier system there are integers q≥1 and a≥2, with a even, such that:

- there are q connected pieces, each with a boundaries and the same Euler characteristic;
- the chamber graph is a path with q edges and q+1 vertices;
- after choosing one end, the cyclic piece-label word on T is

```math
(0,1,\ldots,q-1,q-1,\ldots,1,0)^{a/2};
```

- an end region meets T in a/2 annuli pairing boundaries of its one incident piece; an interior region meets T in a annuli pairing boundaries of its two incident pieces.

This is a linear **region** assertion; adjacent pieces may have different ordinary HT classes, and the intervening region is not asserted to be a product.

**Proof.** Number the N longitude boundary sheets cyclically by Z/N. Choose an odd root band. HT's transported folds have form i↦c_ν−i, with all c_ν odd. Rotate the origin so the root fold is i↦−1−i. Set

```math
e=\gcd(N,c_2-c_1,\ldots,c_h-c_1),\qquad
q=e/2,\qquad a=2N/e.
```

An odd N gives a nonorientable component, which cannot be a cut of an oriented surface. Hence N and e are even. Products of folds are translations through c_ν−c_1. Their orbits are residues modulo e, paired by t↦e−1−t. Thus there are exactly e/2 components, each of 2N/e sheets. The component label at boundary index i is the smaller of i mod e and e−1−(i mod e). This proves the displayed cyclic word and the common boundary count. Restricted sheet counts, not separate component normalisations, give their possibly different HT types.

Every component separates by Lemma 3.1, so every edge of the connected chamber graph is a bridge; the graph is a tree. Following the meridian first crosses the distinct edge labels 0,1,...,q−1 in succession. A non-repeating edge walk in a tree is a simple path. This walk already contains all q edges, so the entire tree is that path. Its return walk is the reverse list, repeated a/2 times. The stated annular T traces follow from its end turns and consecutive interior crossings. ∎

In particular, if two nonempty odd systems are disjoint, their union has the same carrier and one common value of a. Each subsystem inherits the common path order. Different boundary arities cannot coexist in a disjoint union. None of this asserts that the components have the same isotopy type.

## 4. Ordinary end markings and finite coloured families

The following local observation extends the two-boundary confinement proof; its role is ordinary isotopy, not a cyclic distance calculation.

**Lemma 4.1 (no return at a separating piece).** Let F⊂Q be connected, essential, separating, of positive genus, with a≥2 longitude boundaries. An identity-starting return isotopy that fixes its boundary circles individually has zero meridional winding. An ordinary return of a finite system of such pieces has no nontrivial cyclic boundary permutation and zero common normal configuration winding.

**Proof.** Attach a reaching annulus from every boundary of F to a labelled actual parallel, with the alternating signs supplied by F. This gives a connected efficient spanning assembly of a balanced a-parallel link. A full return of winding m would identify this assembly with its m-fold outer-twisted version.

Put two comparison copies of F at distinct levels of one fixed collar F×[−δ,δ]. Its a boundary annuli lie in disjoint proper meridional strips on T. In empty-product simplification, use the T-preserving product pushes described in §2. Any horizontal product portion in Q has an entire F copy as face: there are no companion intersections and no actual boundary in Q at which a proper face could end. The two parallel separating copies cut Q into three chambers; only their middle collar slab has both copies on its frontier. Thus every Q product in the simplification is this slab. Non-final pushes may end at a nearby distinct collar level, so the same confinement persists throughout the finite reduction. A product avoiding Q fixes T. All boundary tracks remain in their original proper strips.

The resulting confined comparison has winding zero. Remove that boundary transport. A relative pattern tether detects an outer twist: in H_1(B_a,b_j), its difference is m[b_0], and [b_0] is nonzero modulo [b_j] because there is another actual hole. Thus m=0. This uses the full-face and middle-slab arguments of [the return lemma](odd-returns.md); the number of boundary strips is immaterial.

For a system return, boundary motion on T preserves cyclic order. Pass to a finite power fixing every piece, orientation and boundary. Restrict to one piece and apply the first assertion. Its full winding is that power times the original configuration displacement. A nontrivial cyclic permutation has a nonintegral displacement with denominator dividing the number of traces, and cannot become zero after taking a power. Hence the original permutation and winding are both zero. ∎

**Lemma 4.2 (natural rooted order).** On a fixed odd carrier choose one odd root band and its outside normal gap. The end and order of Lemma 3.3 are ordinary invariants, natural under passage to an actual subcollection of components and under deleting colours from a finite disjoint family.

**Proof.** At the root normal stack, its outside gap is the end labelled 0 in Lemma 3.3. HT's complete moves are at coefficients ±2, so none moves the odd root section. They can be supported away from that section, including when they change an adjacent plumbing parameter. The restricted-sheet construction first retains the specified root levels and plumbing rectangles, then compresses their order without crossing the outside gap. The retained level set is invariant under the root reversal i↦N−1−i; compression preserves this reversal and its outside gap. It therefore preserves the end and the induced linear order, including when a component has more than two boundaries. Two normal forms of the same ordinary system are connected by those complete HT moves. Concatenate that root-preserving move path with the two chosen normalising comparisons. A disagreement of their end markings would give an ordinary return permuting the port boundaries, excluded by Lemma 4.1. No classification of isotopy paths beyond this return argument is needed. This proves ordinary invariance and subsystem naturality. It does not use parallelism of adjacent components. ∎

For a cyclic simplex, common whole components are first collapsed as in Part 7 §9. Root its integral difference potentials at the selected Q end chamber. They are a nested zero-one chain. Exact phase recovery restores coloured parallel copies of a common whole component in the phase-interval order, reversed at a negatively oriented companion occurrence. The band endpoints are the fixed partial-sum breakpoints determined by the chamber potentials. Zero coefficients delete their phase intervals. The root order of distinct companion occurrences is already fixed by Lemma 4.2. Hence this supplies one ordinary, realisable coloured linear order, compatible with every face. The product packet used here is a packet of **isotopic whole actual-bearing components**, exactly the general Part 7 packet lemma; no product between distinct HT pieces is inserted.

## 5. A safe phase-average construction for one-boundary cuts

We record why generic-level arguments are safe in the even carrier and are not applied unrepaired to multi-boundary pieces.

Consider a finite cyclic simplex in the even-carrier subcomplex, with its simultaneous efficient representatives. Use the collapsed whole-component Thom bands and the common global Φ-cover of Part 7. Their equivariant real band maps are F_i. For x=Σ_i t_i[v_i] put F_x=Σ_i t_iF_i. On P all maps factor through B_n. Near T choose one product collar where they are independent of the collar coordinate. Restriction to Q factors through the lifted oriented chamber circle of Lemma 3.2. On one component of the restricted global cover, write that real function as f_x(u), with

```math
f_x(u+1)=f_x(u)+d.
```

If d>1 the restriction of the Φ-cover has d components. The others are deck translates of this same construction; their values differ by the one global deck constant. No new local constants are chosen.

Suppose a homotopy changes f_x only by making the old positive bands weakly increasing and the old negative bands weakly decreasing, without reversing any band. Extend its periodic real difference from T across the fixed pattern collar, linearly in the collar coordinate and with zero change at the other collar end. Leave the actual boundaries unchanged. The resulting generic Q levels are entire parallel copies of original R pieces. Generic pattern levels are vertical annuli and closed vertical tori.

**Lemma 5.1 (safe outputs).** Delete every whole closed component of such a generic level. Every remaining component is either an actual-to-actual vertical annulus or one original essential R piece with an actual reaching annulus. In particular the reduced level is an actual incompressible spanning vertex in the even carrier, with no compression choice.

**Proof.** An actual circle is used exactly once because its boundary map is still monotone of unit degree. An outer-to-outer pattern annulus uses two R pieces, each of which has only one boundary; together they form an entire closed component. Thus all such returns, including boundary-parallel ones, disappear under whole-component deletion. A closed base curve also gives a whole closed torus. Remaining reaches and actual-to-actual arcs are essential; capping a reach by an essential R gives an incompressible actual-bearing component by essential assembly. No annulus can use two ends on the same actual torus. ∎

Average the reduced ordinary level classes over generic phase intervals. At fixed parameters these classes have simultaneous disjoint representatives, so the average is a point of Y. Closed-component deletion is used only here, in this one-boundary situation; it is not a purported repair for a multi-boundary actual-bearing surface.

On each closed simplex cylinder there is a finite PL band-and-collar template and bounded finitely many lifted nodal values. Maxima of finitely many chamber values and monotone band restrictions give finitely many critical phase functions and ordinary level patterns. The associated interval lengths vary continuously; at a change of pattern its interval length vanishes. Thus the phase average is continuous with image in a finite subcomplex. Widths of bands and product collars only reparametrise these same monotone rectangles. Ordinary efficient comparisons transport the entire construction; a change of lift adds one common constant and rotates phase. Deleting a zero coefficient removes its unsupported bands and merges equal-value chambers. Consequently the construction is ordinary and face-compatible.

There is also no ambiguity from shared whole-component packets. Each shared one-boundary actual-bearing component has the same Q sign in every occurrence. In the common T-preserving product packet its Q copies are consecutive and have that one sign. Splitting or collapsing the packet therefore only splits or joins consecutive monotone subbands. The record maximum and the collar path composition commute with this operation. Generic levels merely select different isotopic copies in the same phase interval; its ordinary class and interval length are unchanged. Shared pure annular packets miss Q. This checks the unlabelled-union ambiguity using exactly the whole-component packet input of Part 7.

We will compose this Y-valued average with R_D. We do **not** claim that deleting closed components preserves cyclic adjacency between levels. What is preserved is simultaneous geometric disjointness. R_D sends that geometric simplex into X, and recombination of whole actual-bearing components stays in the one-boundary/annular sector. At the initial band map its phase average is exactly x by Part 7 exact recovery on cyclic simplices.

## 6. The circular-envelope deformation

Reverse all orientations if necessary so d≥0. On the oriented lifted chamber circle define

```math
m_x(u)=\sup_{v\le u} f_x(v).
```

For d>0 this equals the maximum over u−1≤v≤u. It is finite, continuous, weakly increasing and satisfies m_x(u+1)=m_x(u)+d. On an old positive band it is the old function clipped from below by the preceding record; on an old negative band it is constant. For d=0 it is simply the constant max f_x over the circle. In both cases use

```math
f_{x,s}(u)=(1-s)f_x(u)+s\,m_x(u),\qquad 0\le s\le1.
```

Positive band slopes remain nonnegative and negative slopes are multiplied by 1−s. Extend the periodic difference by the collar construction of §5 and let Θ_s(x) be the reduced phase average. Set

```math
H_E(x,s)=R_D\bigl(\Theta_s(x)\bigr).
```

Explicitly, Δ_x=m_x−f_x is periodic of degree zero and descends to one real function on Q, even when the restricted Φ-cover has several components: translating a chosen Q lift adds the same constant to m_x and f_x. On the fixed pattern collar with normal coordinate z extend it by χ(z)Δ_x|_T, with χ=1 at T and χ=0 at the far collar end, and set it to zero beyond that collar. The global map is F_x+sΔ_x. It is still equivariant for the original Φ. On a collar gap both old and new functions are constant in the meridian coordinate; on a wall strip they retain its original monotonicity. These monotone rectangles give the canonical annular path composition used in §5 and explain why no arbitrary triangulation or separate companion phase is being chosen.

**Theorem 6.1 (circular-envelope principle).** If d=0, H_E is a strong deformation retraction of the cyclic even-carrier sector onto A_X. If d>0, the entire X equals the even-carrier sector, and H_E strongly deformation retracts it onto its coherent positive-cut subcomplex.

**Proof.** Lemma 5.1 proves all outputs essential. On every original chamber or monotone band, the envelope is determined by finitely many previous chamber maxima and the current band value. It is unchanged by an oriented reparametrisation of the circle, an additive constant, or collapsing a zero-jump band. Thus the ordinary and face-compatibility assertions of §5 apply, even when the all-annular face has no active companion circle. Its function is constant and its correction is zero. Exact recovery gives H_E(x,0)=x.

For d=0, at s=1 the Q function is constant, so a generic phase has no Q piece. All outputs are annular, and R_D stays in their annular subcomplex. For an input in A_X, the correction is zero and exact recovery fixes that input throughout.

For d>0, at s=1 the Q function is weakly increasing of degree d. Every generic phase therefore has exactly d positive R pieces and no negative one. There can be no oriented outer return joining two such positive pieces. R_D recombines whole components with positive Q cuts, so it retains this property. Conversely on a cyclic simplex all of whose Q cuts are positive, f_x was already weakly increasing, hence m_x=f_x. Its phase average is the unchanged x. This proves strong deformation and pointwise fixation of the coherent subcomplex. Lemma 3.1 makes this the entire ambient X when d≠0. ∎

**Lemma 6.2 (the endpoint is precisely taut).** If d>0, the coherent positive-cut subcomplex is MS(L).

**Proof.** Every vertex has r≥d one-boundary Q pieces, with signed sum d and Euler characteristic r(1−2g(C)). All its other pieces are annuli. No actual disk occurs. Thus minimal Thurston norm is attained exactly when r=d, equivalently every Q piece is positive. This bound is realised: use d disjoint positive copies of one Seifert surface, pair each negative actual hole to a positive one by an annulus, and tether the remaining d positive holes to Q. These arcs can be embedded as a planar partial matching. Essential assembly proves incompressibility. Reduced taut spanning surfaces in an irreducible boundary-irreducible link exterior are essential; compressing and deleting closed components gives such representatives of a norm minimum. Thus the lower bound just computed on essential vertices computes that minimum. Closed relative components cannot improve it, and PS excludes torus components in its vertex definition. Hence its taut cyclic complex is exactly the displayed full subcomplex. ∎

PS Theorem 1.1 now proves contractibility for every orientation pattern with d≠0. This includes mixed signs and nonfibred two-bridge companions; no companion bundle was used. The remaining sections treat d=0.

The PS hypotheses here are those for a non-split link exterior: irreducibility and boundary irreducibility were checked in §2; the actual oriented spanning curves are nonseparating on their individual boundary tori; and H_2(M)→H_2(M,∂M) is zero for a link exterior in S³. The oriented actual meridians determine the single class Φ. PS's cyclic width on these taut ordinary classes is the same class minimum δ as ours, so its flag complex is precisely the indicated induced subcomplex, including disconnected surfaces.

## 7. The annular matching subcomplex

Let A_Y be the pure pattern-annular geometric subcomplex, with the companion hole retained as an unused marked boundary. It is nonempty in the balanced case: pair positive and negative actual holes and embed the pairs as disjoint planar arcs. The positions of the labelled holes do not impose an additional order condition; a labelled homeomorphism to a standard paired arrangement gives such arcs.

**Lemma 7.1 (annular contraction).** A_Y and its cyclic subcomplex A_X are contractible.

**Proof.** First, A_X is exactly the taut cyclic complex MS(L) in the balanced case. Annular matchings exist and have norm zero. Every nonempty Q piece on any zero-slope carrier has strictly negative Euler characteristic by Lemma 3.1, whereas all pattern pieces are annuli. There are no actual disks. Thus a reduced essential spanning surface has norm zero exactly when it has empty Q cut. PS Theorem 1.1 proves A_X contractible, and the restricted comparison |A_Y|↘|A_X| proves A_Y contractible. This argument alone is sufficient for the lemma and identifies the uniform taut endpoint in Theorem A.

There is also a direct planar finite phase proof, useful for the matching interface. Fix a base matching a_*. Use one negative-curvature metric with geodesic boundary on B_n and the orthogeodesic cores of the finitely many arc classes in a finite subcomplex J⊂A_Y. Compatible cores are simultaneously disjoint. Choose narrow PL bands and common profiles on shared cores. Their circle-valued Thom maps f_i:B_n→R/Z have actual boundary degrees ε_i and are constant on b_0. They have the same cohomology class. Let u_i be real lifts of f_i−f_* normalized to zero on b_0. For x=Σ_i t_i[a_i] use

```math
g_{x,s}=f_*+(1-s)\sum_i t_i u_i\pmod1.
```

Actual boundary maps remain monotone of the same unit degree. The companion boundary remains constant. A generic level is therefore a union of actual-to-actual arcs and closed curves, with one end on every actual circle and none on b_0. Delete the closed curves; their lifts are whole closed pattern tori. Every remaining arc joins distinct opposite-sign actual holes and gives an essential annulus.

Average these reduced ordinary matching vertices over phase. At fixed parameters they are disjoint levels of one map, hence a geometric simplex. A finite PL template gives finitely many ordinary patterns and critical phase functions, so the average is continuous on each closed simplex cylinder and agrees on faces. At s=1 it is the base vertex. At s=0 on an actual input simplex all levels use whole input annular component classes; these and the input vertices form one geometric carrier after restoring parallel packets. The initial straight carrier homotopy joins x to that phase average. Thus every finite inclusion J→A_Y is nullhomotopic. This proves weak contractibility and hence contractibility by Whitehead in weak/CW topology. The same argument works for any balanced number of actual holes.

The Part 7 retraction stays in A_Y, since recombining whole actual annuli gives only actual annuli. Hence A_X is a strong deformation retract of A_Y and is contractible. ∎

The proof deletes only **whole** closed tori in a purely annular system. It neither changes an actual-bearing component by compression nor asserts that deletion alone preserves cyclic edges. Theorem D handles the latter comparison.

## 8. A linear-port contraction without parallelism

Fix an odd carrier β of length s and an even arity a. Let X_{β,a} consist of A_X and the vertices whose nonempty Q cuts have carrier β and connected boundary count a; define Y_{β,a} similarly. Every disjoint family in this sector has the common linear chamber order of Lemma 3.3. Fix its root end as in Lemma 4.2. Set q(S)=0 on annular vertices and otherwise let q(S) be its number of companion pieces. Each piece has the fixed negative Euler characteristic a(1−s), so q is component-additive.

We prove a linear-port principle. Its hypotheses are precisely the linear chamber incidence, the repeated out-and-back T trace, ordinary natural end order, and essentiality of retained pieces. A product between consecutive, different pieces is **not** one of its hypotheses.

### 8.1. Original one-sided chambers and cap operations

Write the original companion pieces F_0,...,F_{q−1} in root order. Give each a reference coorientation towards the next chamber and write its orientation sign w_i. The negative original chambers are:

- the root end when w_0=+1;
- an interior chamber between F_i,F_{i+1} when (w_i,w_{i+1})=(−1,+1);
- the other end when w_{q−1}=−1.

Their incident-piece sets are pairwise disjoint. Positive chambers have the analogous list with signs exchanged. These assertions use only a path of separating surfaces. An interior chamber may be a nonproduct cobordism between nonisotopic surfaces.

For any subset U of negative chambers, replace every incident whole companion piece by the annuli in the T boundary of that chamber. Push those annuli across T in its empty boundary gaps, and push every retained original piece and pattern piece slightly to the negative side. Call the raw result R_U. The cap operations commute because their incident-piece sets are disjoint. They can be carried out in the chosen chambers and their boundary collars, without crossing the original surface.

**Why a nonproduct chamber is allowed.** A cap is a new surface made from the annular T part of the chamber boundary, replacing its one end face or two interior faces. It is not an isotopy identifying the two faces, and does not move one face through the whole chamber. The annuli are present in the actual boundary of that chamber by Lemma 3.3, and their orientations match because all its surface faces are on the selected side. Their collar push needs no product structure on the chamber interior. Retained pieces remain small copies of the original essential pieces.

Path composition of the vertical annuli in B_n describes the whole new pattern exactly. It can have boundary-parallel outer returns and whole closed components. Delete closed pattern circles, but postpone deletion of closed components containing companion pieces until the closure is finished.

### 8.2. Every bad return identifies one original chamber

**Lemma 8.1 (exhaustive barrier repair).** Every boundary-parallel pattern return of R_U identifies a unique unselected negative original chamber whose incident companion pieces are still present. Resolving that chamber is a further cap operation on the same side. No other cut-piece repair is needed.

**Proof.** Let D be its empty disk in B_n, bounded by the return and a companion-boundary interval. It contains no actual hole. It contains no original S trace point either. An original essential pattern arc starting in that interval cannot cross the new return, since R_U is disjoint from S. It cannot end at an actual hole in D. It would have to be an entire original outer return inside an empty disk, contrary to essentiality.

The new return endpoints therefore lie in one gap between consecutive original trace circles. There are at most two new trace points there, the small selected-side push-offs of its bordering original boundaries. Both can lie in that gap only if the incident chamber has both faces on that side, or is an end chamber with its sole face on that side. By the repeated word in Lemma 3.3, a gap within a monotone block belongs to the chamber between two consecutive pieces; a turning gap belongs to the corresponding end chamber. These are exactly the listed one-sided chambers. The new endpoints certify that all of its one or two incident whole pieces are still present. Hence it is unselected. Resolving it removes the witnessed return, possibly producing others of the same classified form. The remaining companion pieces were already essential, so no additional kind of repair is required. ∎

The proof uses the boundary-interval and chamber **incidences**, not that an interior chamber is a product.

### 8.3. Confluence, an ordinary parent, and relative emptiness

Seed U by the root end, using the normal side containing that end. Add enabled one-sided chambers as in Lemma 8.1 until none remains.

**Lemma 8.2 (ordinary closure).** This finite process has a unique least terminal selected set. Deleting its whole closed components gives an essential spanning parent p(S), with q(p(S))<q(S). Its retained Q pieces form a definite ordinary subcollection of the original pieces. Put p(a)=a on A.

**Proof.** If an unselected chamber G has a witnessing pattern path and another chamber G' is resolved, G's surviving endpoints are not endpoints of G': their incident-piece sets are disjoint. Annular path composition at other endpoints does not change that complete path or its empty-disk class. Thus enabling is monotone. On the finite set of original one-sided chambers this gives the unique least closed superset of the seed. Closed components containing Q pieces were not deleted during this process, so they hide no change of the original chamber set.

At termination there is no boundary-parallel pattern return. Every retained Q piece is an original essential surface; every actual or returning pattern annulus is essential. Reverse assembly therefore proves incompressibility of every actual-bearing component. Delete all whole closed components now. Actual boundary is unchanged and the seed removed at least one Q piece.

The root order, the one-sided original chamber list, their annular T faces and the empty-disk tests are invariant under ordinary efficient comparison. Lemmas 4.1–4.2 exclude a hidden end reversal or boundary circuit and preserve the retained-piece identities. Thus this is an ordinary parent, not a chosen maximal compression. ∎

Only the original global component containing the seed is changed. An enabled return connects the affected incident pieces inside one current component, so a cap never joins two previously separate original components. Unchanged components enable no repair. Consequently p(S) differs from S by replacing one connected component by a system with the same oriented actual boundary set. The shared-component wall argument of [CW, Part 7, §9] gives a cyclic edge if desired. The contraction below only needs the following stronger relative geometric statement.

**Lemma 8.3 (relative empty end).** If S is in a finite disjoint family in the sector and its first Q piece is first in the whole family's root order, then p(S) has representatives disjoint from the whole family, retaining the old relative positions of every surviving piece.

**Proof.** The seed end region is empty of all other companion pieces. At a repair disk D, apply the original-arc argument of Lemma 8.1 to every other family member: no essential original pattern arc can enter D, so its companion interval contains none of the other colours' trace points. The common boundary word is the same repeated path walk. If another Q piece lay between the two repair faces, or on the repair end, it would have a trace in that interval. Hence the identified chamber is empty of other colours. The cap and all small push-offs can be chosen there. Induction proves relative disjointness at every repair and after whole-component deletion. Surviving pieces never cross another retained piece. ∎

Uniform arity of a joint HT family matters here: it makes every intermediate piece visible in every appropriate repeated gap. A mere signed count, or an arbitrary tree with a branching region, would not give this conclusion.

## 9. Face-compatible multistep prisms

Iterate the ordinary parent of a vertex:

```math
v=v^0,\quad v^{j+1}=p(v^j),\quad
v^{\ell(v)}=a(v)\in A,
\qquad \ell(v)\le q(v).
```

Label each event by the first retained Q piece in the original root order. The labels strictly increase, since each step deletes its first piece and retains a subcollection. An annular vertex has a stationary event with the same image at both ends.

For a cyclic simplex σ, merge the genuine events by the ordinary face-compatible coloured companion order from §4. Put all stationary annular events after the genuine events, using the restriction of one fixed total order on the annular vertices. At every genuine event its seed is first among all currently retained pieces. Lemma 8.3 permits that parent step while preserving the geometric compatibility of every current vertex. All intermediate states, and the union of two consecutive states, are therefore genuine geometric simplices. Equal ordinary state vertices are identified only in the simplicial map, after their labelled parallel occurrences have served the geometric argument.

Use explicit prism subdivisions. Above v put its trajectory points at vertical heights j/ℓ(v), or heights 0,1 for a stationary event. The current state defines an affine height graph over |σ|. Each event raises one vertex height. The slab between two consecutive graphs is the simplex spanned by the old state and the new trajectory point. These slabs tile |σ|×I. On a face a deleted vertex's slabs have zero thickness; all other events retain the same order and heights. Thus subdivisions and maps agree on all faces.

Mapping each trajectory point to its ordinary vertex gives

```math
K_{\beta,a}:|X_{\beta,a}|\times I\longrightarrow |Y_{\beta,a}|.
```

It starts at inclusion, ends in A_Y, and fixes A_X pointwise. There are finitely many events and image vertices on each closed simplex cylinder, so the ordinary weak/CW product criterion proves continuity without a uniform bound on q.

The Part 7 retraction restricts to Y_{β,a}. Its output is a recombination of **whole actual-bearing components** of the input geometric simplex. Such a component keeps its original essential Q pieces, their carrier β and their common arity a; a subcollection of the simultaneous union remains an essential system on that carrier. Thus no new component type or arity is introduced. Composing K_{β,a} with R_D proves

```math
|X_{\beta,a}|\ \searrow\ |A_X|.
```

This argument handles both terminal paths of the four-parallel example and arbitrary branching or graph cycles in a global multi-boundary assembly. The ordered events concern the Q **chamber path**, not a supposed single path in the global surface graph.

## 10. Gluing all balanced sectors

**Lemma 10.1 (complete sector decomposition).** For d=0,

```math
X=X_E\ \cup_{A_X}\ \bigcup_{\beta\in\mathcal Z(C)\setminus\{E\}}
\ \bigcup_{a\in2\mathbb Z_{>0}} X_{\beta,a}.
```

The intersections of distinct displayed nonannular sectors are exactly A_X, and no simplex mixes their nonannular vertices.

**Proof.** Essential cutting and Lemma 3.1 cover every vertex. Carrier and trace data are intrinsic by ordinary efficient torus comparison. A cyclic edge has almost-disjoint representatives: a transverse crossing meets three consecutive whole complement blocks, as in the Part 7 comparison. Simultaneous efficient cutting then applies to their whole union. HT purity excludes different carriers, and Lemma 3.3 excludes two different connected arities in one odd union. Thus there are no cross edges. Flag completion gives the simplex assertion. Empty or inadmissible arity sectors simply contribute no extra vertices. ∎

Use H_E on X_E and the prism deformations of §9 on the odd sectors. Every deformation fixes A_X pointwise. They therefore agree on all intersections, and define a strong deformation retraction of all X onto A_X. Every closed simplex belongs to one sector and has a finite image cylinder, which proves continuity even though the arity and genus are unbounded. Lemma 7.1 proves A_X contractible. This proves the balanced assertion of Theorem A.

For d≠0, §§3,6 give |X|↘|MS(L)|, and PS proves the endpoint contractible. For n=1, HT makes every oriented spanning piece a one-sheet all-even Seifert surface of genus g(C), so X=MS(C) and PS applies directly. Reversing all orientations identifies the d<0 case with d>0. The exterior is non-split, as checked in §2, so the stated general comparison gives |Y|↘|X| and completes Theorem A.

Explicitly, let H_X denote the deformation onto MS(L) just constructed, and H_D the given comparison deformation. The concatenation

```math
H_Y(y,t)=\begin{cases}
H_D(y,2t),&0\le t\le1/2,\\ 
H_X(R_D(y),2t-1),&1/2\le t\le1
\end{cases}
```

strongly deformation retracts Y onto the same taut cyclic complex and fixes that complex throughout. Contracting the endpoint gives contractions of X and Y. This final use of PS is entirely within its taut range.

## 11. Boundary checks and nonclaims

The proof makes the following distinctions explicit.

1. **Same carrier does not mean parallel pieces.** Mixed ordinary HT types, including those caused by even coefficients of absolute value greater than two, are allowed. Only the chamber path and its repeated port walk are used in the odd closure.
2. **A chamber path is not the surface assembly graph.** The latter can branch and have genuine cycles with actual boundary. No such cycle is deleted by a graph test. Only whole closed surface components are deleted.
3. **Nonproduct chamber caps are replacements, not isotopies.** Essentiality of the output is proved after the finite barrier closure. There is no claim that two nonisotopic HT pieces cobound a product.
4. **Raw multi-boundary levels are not declared essential.** Only one-boundary levels are used for the circle-envelope proof. Multi-boundary pieces use the original-barrier closure; empty returns in actual-bearing components are repaired before invoking essential assembly.
5. **Geometric disjointness is not cyclic adjacency.** Reduced phase averages and prism states are first geometric. Theorem D returns them to X. A geometric simplex is therefore not, merely by this construction, declared cyclic.
6. **Tautness is an endpoint conclusion in the unbalanced case.** Extra positive-negative one-boundary pieces are permitted during the homotopy. The norm computation in Lemma 6.2, rather than nonzero restriction alone, identifies the endpoint.
7. **Ordinary classes are retained.** The root/no-return argument and the circle's reparametrisation invariance prevent an unannounced torus-twist quotient. No independently rooted companion cover is used.

Theorem A is about nonempty zero-framed parallel clusters of two-bridge knots. It is not a theorem for all satellites, graph links, arbitrary framings or multiple independent companion ports. In particular, an arbitrary essential-system tree need not be a path or have the repeated interval visibility needed in Lemma 8.3.

## 12. A genuine nonparallel multi-boundary check

The linear-region extension is substantive. Take C=K_{29/137}, with the expansions

```math
29/137=1+[-2,-2,-2,-2,2,-2,-2,2]
      =[4,-2,-2,-3,-3,-2].
```

Both signed coefficient counts are −4, so the second is a zero-slope odd carrier β. The first is all ±2, so C is fibred; this does not make its odd pieces parallel. On β use N=8 and plumbing parameters (1,0,0,2,0), rooted at odd band 3, with band indices 0,...,5. The large-band heights are H_0=1,H_3=0,H_4=2. The transported odd folds have constants 7 and 3 modulo 8. Their two component orbits are

```math
U=\{0,3,4,7\},\qquad V=\{1,2,5,6\}.
```

Restricted interval counts give complete large-height data (1,0,1) on U and (0,0,1) on V. HT's complete move relation distinguishes the two connected ordinary classes. Both have four boundaries and genus nine. Their complementary middle chamber is therefore **not** a product. Nevertheless Lemma 3.3 makes their region graph a three-vertex path, with trace word UVVUUVVU.

Orient both reference pieces towards the same path end. Their trace signs are ++--++--. In the four-hole pattern use waves (0,2),(3,5) and reaches 1↔p_1,4↔p_2,6↔n_1,7↔n_2. Each wave cuts off the corresponding positive actual hole and its reaching point, so the two waves and four reaches are disjoint and essential. They give a connected actual-bearing assembly with two Q pieces, a true graph cycle and genus 19.

The root-end caps are (7,0),(3,4). Literal annular path composition leaves the four reaches 1↔p_1,2↔n_2,5↔p_2,6↔n_1, capped by the single retained genus-nine piece V. The next end caps (6,1),(2,5) give the two pure actual annuli. This is a q=2→1→0 trajectory. The middle region was never identified with a product, and no connected multi-boundary piece was replaced by disconnected model arcs.

There is a stronger check in which a **nonproduct interior chamber must actually be resolved**. On the same β take N=16 and parameters (3,0,0,4,0). Its four root-ordered components have large-height data (1,0,1),(1,0,1),(1,0,1),(0,0,1). Thus the chamber between pieces 2 and 3 is nonproduct. Use signs (+,+,−,+), reaches 0↔p_1,2↔n_1,6↔n_2,9↔p_2, and waves

```math
(1,15),\ (3,14),\ (4,13),\ (5,12),\ (7,11),\ (8,10).
```

This is the embedded essential pattern specified here: each wave interval contains one, two or three actual reaches, and its sides both contain actual holes. With the present HT pieces it gives a connected genus-39 four-boundary vertex. Resolve the first end using caps (15,0),(7,8). The composite path 10—8—7—11 becomes the new return (10,11). The old nested waves (8,10) and (7,11) enclose the same single actual hole p_2; the disk between them and the cap contains no actual hole. Thus this really is a boundary-parallel return, not just an assertion about its endpoint labels.

It enables exactly the original negative chamber between pieces 2 and 3, whose types differ. Resolve that chamber with caps (2,3),(4,5),(10,11),(12,13). The result, after discarding two whole closed pattern circles, has only piece 1 and the four reaches 1↔p_1,6↔n_2,9↔p_2,14↔n_1. Its genus is nine. The next end resolution gives the two actual annuli. This q=4→1→0 trajectory exhibits the nonproduct cap repair required by the extension, rather than merely a family in which such a chamber happens to be present but unused.

## 13. Sources and exact diagnostics

The precise editions and page ranges are [HT, B, PS, H3 and CW](../sources/bibliography.md). HT's whole-system moves and folds, not a classification of single surfaces alone, are the classification input. The efficient-cut, reverse-assembly and product-annulus arguments are given in §2 above and [the geometric foundations](assemblies.md). The comparison used throughout is [CW, Part 7, Theorem D]; no general contractibility assertion is imported from it.

The author's `scripts/check_zero_framed_clusters.py` checks 1,496 fold systems, 2,046 one-sided sign words, 6,005 rational envelopes and both nonparallel examples. The independent `scripts/check_zero_framed_independent.py` reconstructs local rectangles, closure paths, coloured barriers and envelopes without importing the author's code. Both are included in [the read-only replay](../scripts/README.md). Finite arithmetic does not certify ordinary isotopy, essentiality or CW continuity.
