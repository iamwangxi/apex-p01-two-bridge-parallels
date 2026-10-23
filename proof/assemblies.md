# 3. Essential assemblies and torus-preserving comparison

[Contents](../README.md) · [Objects](objects.md) · [Next: full-complement comparison](comparison.md)

This section holds for every nontrivial companion. Standard inputs are the Loop Theorem, amalgam normal form, isotopy extension, relative disk isotopy in a ball, and [H3, pp.13–15, Lemma 1.11 and Proposition 1.12, pp.20–22]. The product-region input is [B, Definition 4.1, Proposition 4.2, Remark 4.4] and [PS, §3]. No assertion from [PS, §§4–7] is used.

**Lemma 3.1 (ambient hypotheses).** The pieces and their glued exterior are irreducible, their boundary tori inject on fundamental groups, and $`T`$ is incompressible. Every spanning component is boundary-incompressible. There is no spanning-fibre exception to product simplification.

**Proof.** Cutting the product pattern along vertical annuli over a base-cutting arc system gives a solid torus. The usual cutting argument gives irreducibility of the pattern. Its boundary groups are $`\langle\lambda,b_i\rangle\cong\mathbb Z^2`$ inside $`\mathbb Z\times\pi_1(B)`$ and inject. A nontrivial knot exterior is irreducible with incompressible boundary. Sphere cutting and amalgam normal form give the assertions after gluing, including boundary irreducibility and the Haken hypothesis supplied by $`T`$.

There are no disk spanning components, since the prescribed longitudes are nontrivial in the injected actual torus groups. By [H3, Lemma 1.11] the only boundary-compressible incompressible alternative would be a boundary-parallel annulus. That would use two curves on one actual torus; a spanning surface uses each actual torus once. Finally $`\pi_1(T)=\mathbb Z^2`$ injects into $`\ker\phi`$. A spanning fibration would have a compact fibre with boundary and free kernel group, which cannot contain this subgroup. A component meeting only one actual torus cannot be a fibre of the entire exterior either. ∎

**Lemma 3.2 (primitive annuli).** In a solid torus, a finite disjoint incompressible annulus system with longitudinal degree-one boundary can be straightened simultaneously to circle products of disk arcs, relative to its already straightened boundary. Annuli with both ends on a fixed boundary annulus have an innermost empty annular parallelism there.

**Proof.** Make the primitive slope the circle-fibre slope. A meridian disk has two boundary intersections with each annulus. Remove closed disk intersections by innermost disk and ball moves. The remaining intersection on each annulus is one spanning arc. Cutting the solid torus along the disk turns the annuli into disks in a ball. Relative disk isotopy, taking outermost disks successively, straightens the entire system to product rectangles; the isotopies match on the cut faces. In the resulting disk-arc model, an innermost arc with ends on a fixed boundary interval cuts off an empty disk. Its circle product gives the final assertion. ∎

**Lemma 3.3 (essential cuts and their pattern).** A representative minimizing its $`T`$-circle count has essential intersection circles and incompressible, boundary-incompressible cut pieces, none a disk, closed surface or boundary-parallel annulus. It is either the annulus $`A`$, or its entire pattern consists of two reaching annuli and $`u\ge0`$ essential outer-to-outer annuli, with

```math
N=\lvert F\cap T\rvert=2+2u.
```

All common-torus circles are longitudes. A disjoint pair admits the same conclusions simultaneously, preserving its disjointness, by minimizing the total circle count of the union.

**Proof.** An inessential circle on either of the incompressible surfaces $`F,T`$ is inessential on both. An innermost disk on $`T`$ and its disk on $`F`$ bound a ball. No whole spanning component can be trapped inside, since each has actual boundary. The disk push removes a circle. For a finite union the same empty innermost push preserves the other components. Cut subsurfaces inject into $`F`$ and then into $`M`$, so into their own ambient pieces. Essential circles exclude disks; a closed cut component would already be closed globally.

If a cut annulus were boundary-parallel, both ends would be on $`T`$, since an individual surface uses an actual torus just once. Its parallelism is a solid torus. Other cut pieces inside have groups injecting into that cyclic group, hence are primitive annuli. Lemma 3.2 supplies an innermost empty parallelism. Pushing it across $`T`$ removes two circles, contradicting minimality. This argument applies to the full union. Lemma 1.11 of [H3] now gives boundary-incompressibility of all cut pieces.

A pattern piece meeting an actual boundary has fibre slope there. The vertical-or-horizontal alternative [H3, Proposition 1.12] excludes the horizontal case, and makes it a verticalisable annulus. If it joins the two actual tori, it is already a whole component; everything else would be closed and forbidden. The surface is then just $`A`$. Otherwise there are two inner-to-outer reaching annuli. One gives a longitude on $`T`$; all disjoint essential torus curves share that slope. Every other pattern piece then also has fibre slope and is a verticalisable annulus. Endpoint counting gives the formula. ∎

**Lemma 3.4 (simultaneous verticalisation).** The full pattern annulus system can be verticalised relative to its straight fibre boundary on all three tori.

**Proof.** First straighten all actual and common-torus boundaries in disjoint collars. Extend common-$`T`$ motion to both sides, carrying the whole assembly. Choose disjoint base arcs cutting $`B`$ to a disk and with endpoints avoiding the pattern endpoints. Their circle products meet the annulus system only in circles. Remove inessential circles by empty disk and ball moves decreasing the total count; choose replacement disks close to a cutting annulus, so no other cutting annulus gains intersections. Remaining circles are essential on both annuli. Straighten them to fibres on the cutting faces and extend over collars. After cutting, the ambient manifold is a solid torus and the cut pattern pieces are injective annuli with primitive fibre boundaries. Apply Lemma 3.2 relative to all cut faces, and glue. The matching traces give a simultaneous isotopy. Boundary-parallel base arcs have already been excluded in Lemma 3.3. ∎

**Lemma 3.5 (pattern matching).** Put $`N=2k`$ and index the outer endpoints cyclically. If the positive reaching endpoint is $`j`$, the negative one is $`j+k`$ and the wave pairing is

```math
p_j(i)=2j-i\pmod{2k},\qquad i\ne j,j+k.
```

**Proof.** Every essential outer-to-outer arc separates the inner holes; otherwise it cuts off an empty disk. Cut the pair of pants along the two reaching arcs. In the resulting disk each wave joins the two portions of the outer boundary. Their $`k-1`$ endpoints on each portion match in reverse order, by noncrossing. This gives antipodal reaching endpoints and exactly the displayed reflection. ∎

**Lemma 3.6 (reverse assembly).** Compatible oriented essential cut systems with opposite cut-side signs glue to an incompressible spanning surface if each resulting component reaches an actual boundary.

**Proof.** Minimize a hypothetical compression disk's intersections with $`T`$. Remove closed intersections by incompressibility of $`T`$ and irreducibility. An outermost remaining disk arc is a boundary compression of a cut component. Boundary-incompressibility makes its surface arc boundary-parallel; the resulting surface disk permits a disk replacement removing that arc. Eventually the disk lies in one piece, contradicting its incompressibility. The boundary and no-closed-component assertions are precisely the stated matching conditions. This proof allows companion pieces with more than two boundaries. ∎

**Lemma 3.7 (annuli in a horizontal product).** Let $`W`$ be a compact orientable surface with nonempty boundary. For an incompressible proper annulus system in $`W\times I`$ with boundary in the interiors of the horizontal faces and away from vertical boundary: a returning annulus has an innermost empty parallelism to one horizontal face; if all annuli span, they straighten simultaneously to $`\Gamma\times I`$, keeping horizontal faces setwise.

**Proof.** A returning annulus has essential freely homotopic boundary curves, which cobound an annulus in the horizontal surface. Their union, slightly pushed inside, is a torus. The product is an irreducible handlebody with free fundamental group. The torus therefore compresses; the compressible-torus alternative [H3, p.14] makes it bound a solid torus, rather than lie in a ball, since its core is nontrivial. The annular slope has degree one there: higher degree would make its horizontal simple essential curve a proper power in $`\pi_1(W)`$, and degree zero would make it trivial. Essential simple curves in a surface with boundary are not proper powers. For a nonseparating curve use an adapted free basis; for a separating curve use its cyclically reduced boundary word in a basis adapted to the cut surface, with an oriented participating letter occurring once. Thus the solid torus is the annular parallelism. All annuli inside it have ends on its horizontal annulus; Lemma 3.2 supplies an empty innermost one with no extra boundary trace in its face annulus.

For spanning annuli, project to $`W`$ to identify the upper and lower essential curve systems up to isotopy, including multiplicities. Put both at one system $`\Gamma`$ on the horizontal faces without preassigning a permutation of parallel copies. Choose proper arcs cutting $`W`$ into disks and minimize their intersections with $`\Gamma`$. In their product disks remove circle intersections with the annuli. A remaining arc returning to the same horizontal edge is boundary-parallel on its annulus and gives a bigon with the chosen cutting arc in $`W`$, since a horizontal face is a homotopy equivalence. This contradicts minimality. Thus all remaining disk arcs span. They preserve endpoint order and straighten vertically. Cut annuli are now disks in the remaining balls; none can miss all cutting disks, since its core would then be trivial. Relative disk isotopy straightens the disks to product rectangles. Gluing proves the system assertion and determines the compatible parallel-copy matching.

For a collapsed-boundary product region in [B, Definition 4.1], trim a horizontal boundary collar away from the compact annular traces and apply the same argument, extending by the identity. ∎

Call an assembly **efficient** when its cut circles are essential longitudes and all cut pieces satisfy the essentiality conclusions above. Reverse assemblies are efficient: each cut circle is nontrivial in the ambient injected torus, so remains essential after gluing.

**Proposition 3.8 (efficient torus comparison).** Globally isotopic efficient assemblies admit an ambient comparison isotopy preserving $`T`$ setwise. Every efficient assembly already has minimal $`T`$-circle count.

**Proof.** Make the two longitude traces disjoint by $`T`$-preserving collar motions; actual boundaries can also be made disjoint. Keep common whole components and make the others transverse. Take an empty product region of the usual simplification [PS, §3; B, Proposition 4.2]. It meets $`T`$ in proper annuli because $`T`$ is cut by parallel longitude traces. A whole $`T`$ cannot lie inside: the product horizontal face has boundary and free group, into which the injected $`\mathbb Z^2`$ would have to inject. The annulus cores are nontrivial for the same reason; the collapsed locus misses $`T`$ because the traces there are disjoint.

A returning annulus, by Lemma 3.7, would have an innermost empty parallelism to a horizontal subannulus with no other $`T`$ trace inside. That horizontal annulus would be an entire cut piece parallel into $`T`$, contrary to efficiency. Every trace therefore spans. Straighten these annuli to products using Lemma 3.7 and perform the ordinary product push tangent to them. Extend over collars and by isotopy extension. Conjugating back gives a push preserving the original $`T`$, with the usual reduction or whole-component identification.

Repeat on the full systems, retaining identified components and requiring every region to miss them. Non-component pushes reduce the finite transverse intersection count; component identifications reduce the unpaired component count. At simplified intersection isotopic corresponding components coincide, by the parallelism theorem and the coincident-component convention of [PS, §3]. The spanning-bundle exception is excluded in Lemma 3.1. Concatenating gives a $`T`$-preserving comparison without placing a restriction on the originally supplied isotopy. Such moves restrict to isotopies of efficient cut pieces, so efficiency persists.

Compare any efficient assembly to a minimum representative, which is efficient by Lemma 3.3. The comparison preserves the number of $`T`$ circles. Thus the original count was minimal. ∎

In particular the companion carrier, full boundary matching and common boundary-motion orbit are intrinsic. Compatible paths of cut systems extend ambiently by first extending their shared boundary path in collars and then using relative isotopy extension in the two pieces. Separate unmarked component classes do not replace this shared orbit.
