# 2. HT carriers, purity and relative classes

[Contents](../README.md) · [Conventions](objects.md) · [Sources](../sources/bibliography.md)

We use [HT, Theorem 1(b)–(e), p.228; Propositions 1–2, p.230]. Their construction allows disconnected systems (p.227). The proof of classification uses the entire level system, with its total sheet number and one level path (pp.233–239). Thus its input here is a whole essential disjoint union, rather than independently selected normal forms of its components.

**Lemma 2.1 (exhaustive enumeration).** All admissible expansions of $`0\lt p/q\lt1`$ are obtained by taking $`r=0,1`$ and recursively, for the current tail $`x`$, choosing

```math
\lvert b\rvert\ge2,\qquad \lvert b-1/x\rvert\lt1,\qquad
y=b-1/x,
```

and terminating at $`y=0`$. Filtering by $`\sigma(b)=\sigma(E)`$ gives exactly $`\mathcal Z(C)`$.

**Proof.** Every nonempty admissible tail satisfies $`0\lt\lvert x\rvert\lt1`$, by induction backwards from $`\lvert b\rvert\ge2`$. Hence the initial integer is zero or one. The displayed inequalities are necessary and sufficient for the next coefficient and remaining tail. If $`x=A/D`$ is reduced, the reduced denominator of nonzero $`y`$ is $`\lvert A\rvert\lt D`$. Denominators strictly decrease, so the recursion terminates, has finitely many branches, and loses no expansion. Finally [HT, Proposition 2] gives slope $`2(\sigma(b)-\sigma(E))`$. ∎

**Proposition 2.2 (carrier purity).** A nonempty essential bounded system in $`Q`$, without closed components, lies as a whole on one HT carrier. Every component has that same carrier. Surfaces with distinct carrier labels cannot be disjoint. This statement also applies to one-sided surfaces after orientations are forgotten.

**Proof.** Apply HT Theorem 1(b) to the whole system. Componentwise essentiality suffices: a compression or boundary compression would be one for its affected component. Restrict the resulting sheets and plumbing squares to a connected component. The restricted branch equations give a common sheet number along all vertical bands. Equivalently, each of its boundary circles runs once around the whole knot and therefore meets each vertical band in the same sheet number. The restriction is another nonempty $`S_n(m_i)`$ on this carrier. There is no closed component with zero boundary count. If that component was specified on a different carrier, HT Theorem 1(d) contradicts the two labels. Apply this to every component. For disjoint separately specified systems apply the argument to their union. ∎

**Lemma 2.3 (component data).** On a length-$`s`$ carrier, an $`n`$-sheet surface has $`n`$ boundary circles and Euler characteristic $`n(1-s)`$. On the all-even carrier its components are orientable, each with one boundary, genus $`s_E/2`$ and relative class $`\pm\eta`$, where $`\partial\eta=[\lambda]`$. On an odd zero carrier every oriented connected component has an even number of boundaries, equally many of either sign, has relative class zero, and separates $`Q`$.

**Proof.** Boundary and Euler counts are [HT, pp.243–244]. For a connected oriented component this yields $`g=1+n(s-2)/2`$. The boundary homomorphism from $`H_2(Q,T;\mathbb Z)`$ to $`H_1(T;\mathbb Z)`$ is injective, with image $`\mathbb Z[\lambda]`$, since $`H_2(Q)=0`$ and $`H_1(Q)=\mathbb Z[\mu]`$. A connected proper oriented surface has either zero class or primitive nonzero class. Indeed, a separating surface has class zero; otherwise a crossing arc closes in its complement to a loop pairing with it by one.

The proof of [HT, Proposition 1, p.245] gives exactly $`n`$ components on an all-even carrier, each of one sheet. Each is orientable by the one-sheet orientability statement on p.230. This proves the all-even assertions; it does not imply that these components are all isotopic or parallel.

On an odd carrier the one-sheet plumbing is nonorientable. An $`S_n`$ is abstractly an $`n`$-fold covering of that plumbing [HT, p.244]. An orientable connected covering has even degree, since its subgroup lies in the index-two orientation subgroup. Thus its number of longitude boundaries is even and its oriented sum is even. Primitivity excludes any nonzero relative class, so the sum is zero and the component separates. Its own boundary signs alternate around $`T`$ after other components are omitted, because a meridian alternates between its two sides. ∎

This paragraph proves the necessary parity statement. [Lemma 13.1 and §13.2](assembly-obstruction.md) give the converse for each connected component and compute the full component partition; [Theorem 13.2](assembly-obstruction.md) excludes larger-boundary components from global vertices. The pure-stack specialization under (P) remains [§6](odd-normal-forms.md).

The all-even expansion has even length: the continuant recursion modulo two gives odd reduced denominator at even length and even denominator at odd length. Every zero-slope carrier also has even length because its signed count equals $`\sigma(E)`$, and signed count and length have the same parity. These facts will ensure positive genus for the two-boundary frontiers used below.
