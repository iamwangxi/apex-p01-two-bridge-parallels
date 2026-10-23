# 15. One odd coefficient and one free block: the ordered system

[Contents](../README.md) · [Proof map](main-theorem.md) · [Sources](../sources/bibliography.md)

Suppose an odd carrier has exactly one odd coefficient and exactly two large coefficients. There is one free block of length L≥1. Read that block starting at its odd large coefficient; reversing the list gives the corresponding affine change of U, and this convention is fixed throughout. If there is just one large coefficient, use L=0 and U=0 as a convention.

The unique odd band is the root for ordering its normal sheets. HT's one folding pairs

```math
q(i)=N-1-i.
```

For N=2k let i=0,...,k-1 index the pairs from the outer chamber toward the middle gap. Let S_v, 0≤v≤2L, be the two-sheeted type of block invariant v, and B_v, 0≤v≤L, the one-sheeted type. Each S_v has genus s-1, two opposite longitude boundaries and class zero. Each B_v is one-sided of nonorientable genus s.

**Lemma 15.1 (one-block ordered-sheet formula).** Write U=2kc+r, 0≤r<2k. The entire 2k-sheeted system has its components, in the stated order, equal to

```math
S_{f_{k,U}(i)},\qquad
f_{k,U}(i)=2c+\mathbf1_{\{i\lt r\}}+
\mathbf1_{\{2k-1-i\lt r\}},\quad 0\leq i\lt k.
```

At U=2kL the formula is interpreted with c=L,r=0. Equal types in a block are parallel copies. Different types present are adjacent along the path S_0--S_1--...--S_(2L).

**Geometric proof.** Normalize the free block by Lemma 14.1, and outside parameters by endpoint moves. The block now has only one partially used plumbing square; every other plumbing uses one of its complementary squares for the entire stack.

Four elementary rules track the sheets in HT Fig.3. A full stack through one square matches its linear normal levels in their order or in reverse order. A full even band does the same; full twists do not permute these levels. Both changes preserve the pair {i,N-1-i} at the odd root. At the single partial square, the r inner sheets form an initial or final interval of the ordered stack, since disjoint parallel rectangles attach in order. Finally, replacing x by N-x in an alternating coordinate complements that interval. A full y box contributes two to each two-sheeted component. A partial y box contributes the number of members of {i,N-1-i} in its interval.

The counts for an initial and a final interval of length r coincide on this pair. Also complementing an interval of length N-r gives the same count as an interval of length r. Therefore the count is precisely the two indicator functions above, independent of the possible full-stack reversal. All moves were performed on the whole system and away from a fixed transverse section of the odd root band. This proves the common labelled order, rather than separate component isotopies. The argument has one partial square; it does not assume that two separated partial squares have independent level transports. ∎

Equivalently, write U=kj+h, 0≤h<k. If j is even the outer h pieces are S_(j+1) and the other k-h pieces are S_j. If j is odd the outer k-h pieces are S_j and the inner h pieces are S_(j+1). At h=0 all pieces are the same S_j. This also follows by taking parallel normal copies of the orientable S_j and using the complete block invariant.

**Odd N.** For N=2k+1 write U=Nc+r. There is a central one-sheeted component

```math
B_{c+\mathbf1_{\{r>k\}}},
```

and k two-sheeted components of values

```math
2c+\mathbf1_{\{i\lt r\}}+
\mathbf1_{\{N-1-i\lt r\}},\quad0\leq i\lt k.
```

The same interval count proves the formula. The singleton index k is the unique fixed sheet. An entire system is orientable exactly when N is even; its k components can then be oriented independently.

**Coexistence and labels.** Two S types coexist if and only if they are equal or adjacent in the displayed path. Necessity follows by applying the formula to their four-sheeted union; sufficiency is realized at U=u+v. Every longer system is precisely the ordered sequence of Lemma 15.1. For independent orientations ε_i its cyclic boundary order and word are

```math
S_1^+,\ldots,S_k^+,S_k^-,\ldots,S_1^-,
\qquad(\epsilon_1,\ldots,\epsilon_k,-\epsilon_k,\ldots,-\epsilon_1).
```

This is a complete simultaneous classification of the bounded systems for a one-block one-odd carrier.

**Subsystem naturality.** A subcollection inherits its paired order and its block invariant is the sum of the retained component values. Normalize its block by the same bounded transfers, supported away from the odd root section, and make an order-preserving small radial adjustment at that section. This gives its fixed reference system without a boundary permutation or full meridional circuit. This operation retains which component belongs to which spanning surface. It is the compatibility required when a disjoint pair is replaced by cap waves below.

For clarity the end marking can also be detected without the section. Every even system can be augmented by a disjoint B_v at its middle end: for U=2kc+r, add v=c if r≤k and v=c+1 if r≥k, replacing U by U+v and N by N+1. The odd-N formula gives exactly the old components and this one-sided component. Any two possible choices belong to the same end, since one-sided longitudinal surfaces cannot be disjoint in opposite end chambers. Thus the middle end is an intrinsic common end, and is retained on passing to subcollections.

### 15.2. The 16/39 table

Put T_d=S_(d+2), -2≤d≤2. All T_d have genus three and two boundaries. For N=2k:

| Parameter range | Ordered components, outer to inner |
|---|---|
| -2k≤d≤-k | (2k+d) copies of T_-1, then (-d-k) copies of T_-2 |
| -k≤d≤0 | (-d) copies of T_-1, then (k+d) copies of T_0 |
| 0≤d≤k | d copies of T_1, then (k-d) copies of T_0 |
| k≤d≤2k | (2k-d) copies of T_1, then (d-k) copies of T_2 |

Zero multiplicities are omitted and endpoints agree. Thus the two-boundary coexistence graph is the five-vertex path, with repetitions and the stated order; it is not a collection of five arbitrary independent labels. The N-odd formula above supplies its unique one-sided component and all orientable components as well.
