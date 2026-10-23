# Scope, attribution and limits of the evidence

[Contents](../README.md) · [Bibliography and checked editions](../sources/bibliography.md)

The contribution is the entire cyclic-distance flag complex of oppositely oriented zero-framed two-parallel links for every nontrivial two-bridge companion: the all-even cone, the two-terminal obstruction, coupled rooted band heights, intrinsic odd-band signatures, complete integer vertex and edge criteria on odd carriers, and their finite-neighbourhood contraction. Under (P) the sharper cone-plus-Farey-trees description remains a corollary. The one-block one-odd case has a two-dimensional tree of disks, and the one-block two-odd case has finitely many Farey trees. Three symbolic infinite families and several mixed examples are supplied.

The all-even base is unrestricted and need not be a point. The result concerns every genus and allows disconnected spanning systems, while retaining its specified cyclic-distance object. It does not claim a theorem for arbitrary links or for the entire original geometric disjointness complex.

## Established inputs and comparison with the literature

Hatcher–Thurston [HT] already classify incompressible surfaces in a two-bridge **companion knot exterior**. That classification, its all-even Seifert-surface consequences and its pillowcase coordinates are inputs, not new companion-knot theorems here. The new statement concerns the two-parallel link exterior and all of its cyclic-width edges and simplices.

Sakuma [S] proves the minimal-genus geometric $`MS`$ complex for special arborescent links is a finite-dimensional ball [Theorem 3.3; Propositions 3.9 and 3.11, pp.873, 876–877]. The full incompressible $`IS`$ contractibility appears in Conjecture 0.2, p.862, and is not that proved theorem. Also his semi-oriented link class does not contain the present oriented parallel links. Indeed his defining tree plumbs unknotted-core annuli with nonzero integer weights [pp.866–867]. The target link has a spanning annulus with $`\chi=0`$, which is minimal because its components are nontrivial knots and no spanning disk component exists. If it were one of his links, Theorem 2.3 [pp.869–870] would make that annulus isotopic to a canonical tree surface. For $`v`$ annuli and $`v-1`$ plumbings its Euler characteristic is $`1-v`$, forcing $`v=1`$. Its nonzero-twist annulus then has nonzero linking number, contrary to zero framing. Thus neither the link class nor the full vertex and edge range matches. Contractibility of the companion's geometric $`MS(C)`$ is already known and is not counted as a contribution.

Roberts [R, Theorem 1, p.1; Theorem 17 and Corollary 18, p.13] counts many inequivalent minimal-genus spanning surfaces for certain arborescent **knots**. His equivalence permits the boundary knot to move in the three-sphere [Definition 3, p.2]. It supplies neither the target two-component parallel-link classification nor its whole cyclic complex. Surface counts alone do not determine its edges or contractibility.

Kakimizu [K05] allows disconnected componentwise incompressible spanning surfaces, so it would be inaccurate to describe that paper as minimal-genus-only. Its main Theorems A and C [pp.48–49] classify prime **knots** of ten or fewer crossings and their geometric $`IS`$ complexes. The general plumbing tools in §§3 and 5 have additional hypotheses, including specified minimal-genus initial plumbings; they do not give the present zero-framed parallel-link theorem. Its two-component annulus example [Lemma 6.4, p.84] has unknotted core and nonzero twist, hence nonzero linking number, and is a different link. The connectivity theorem recalled on p.48 is not a contractibility theorem for arbitrary links. The three read comparison papers therefore do not contain or directly imply the stated result.

This comparison is limited to the specified read works. Kakimizu's 1991 BLMS paper, *Doubled knots with infinitely many incompressible spanning surfaces*, has not been read and is not ruled out by its title. No exhaustive priority certification is claimed.

## Dependence on the target and other theorems

The target is the official 11 September 2026 competition paper [C], not a later author revision. Its Introduction, printed p.2, supplies the general-link question and identifies the failed hypothesis of Lemma 4.9. Its connected-surface geometric conclusion is not transferred to the present disconnected cyclic object by an unstated equivalence.

The proof uses [B] for marked product regions, minimal representative width and the explicit all-incompressible extension in §10. From the journal version [PS] it uses only §§2–3, for complete open blocks and simplified intersection, including coincident components. No projection, order, dismantling or contraction statement from §§4–7 is used. The essential-cut and verticalisation inputs are [H3, Lemma 1.11 and Proposition 1.12], together with the elementary arguments supplied in §3.

## Computations and proof status

The standard-library scripts check exact-rational expansion lists, bounded move orbits, raw rectangle restrictions, coupled rooted heights, folding/sign obstructions, full finite flag complexes and explicit domination deletions. Independent implementations and saved deletion certificates are included. All three infinite families have separate symbolic exhaustion proofs in [§10](infinite-family.md). The script does not certify marked three-dimensional product recognition, ambient isotopies or the contraction. No proof-assistant formalization or implementation of the geometric all-even equality test is claimed.

The mathematical argument received separate adversarial reviews in fresh GPT-6.1 Sol contexts, including the one-odd and multiple-odd general branches, and a novelty check against the cited literature. The present organization includes the prior essential-assembly, winding and edge arguments as numbered proofs, without requiring access to unpublished companion documents. No human expert has certified the result.
