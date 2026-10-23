# 10. Three infinite families and multiple-carrier examples

[Contents](../README.md) · [Main theorem](main-theorem.md) · [Remaining work](reduction-and-remaining.md)

**Theorem 10.1.** For every integer $`m\ge1`$, the knot

```math
C_m=K_{(6m+1)/(16m+3)}
```

satisfies (P), fails the single-boundary condition (SB) of §5, and its oppositely oriented zero-framed two-parallel link has the entire contractible complex of Corollary 1.3. These companions are pairwise distinct. The first is $`K_{7/19}`$.

**Proof.** The numerator and denominator are coprime: subtraction reduces their gcd to $`\gcd(2m,4m+1)=1`$. The denominator is odd. The exhaustive expansion list is the following six possibilities, where $`2^{[h]}`$ denotes a string of $`h`$ coefficients equal to two, not an exponent in the continued fraction:

```math
\begin{aligned}
0+[2,-2,-2,-(2m+1)]&:\quad \sigma=-2,\quad \text{slope }0;\\ 
0+[3,3,-2m]&:\quad \sigma=1,\quad \text{slope }6;\\ 
0+[3,4,2^{[2m-1]}]&:\quad \sigma=2m+1,\quad \text{slope }4m+6;\\ 
1+[-2,-3,-2,-(2m+1)]&:\quad \sigma=-4,\quad \text{slope }-4;\\ 
1+[-2,-2,2,-2m]&:\quad \sigma=-2,\quad \text{slope }0;\\ 
1+[-2,-2,3,2^{[2m-1]}]&:\quad \sigma=2m-2,\quad \text{slope }4m.
\end{aligned}
```

Here is symbolic exhaustion using Lemma 2.1, rather than extrapolation from finitely many computations. In the $`r=0`$ branch the reciprocal is strictly between two and three. Choosing two forces tails

```math
-\frac{4m+1}{6m+1},\qquad
-\frac{2m+1}{4m+1},\qquad
-\frac1{2m+1},
```

so the subsequent coefficients are $`-2,-2,-(2m+1)`$. Choosing three instead leaves $`2m/(6m+1)`$, with reciprocal $`3+1/(2m)`$. The next choices are three, giving terminal $`-2m`$, or four, leaving $`(2m-1)/(2m)`$. A positive tail $`h/(h+1)`$ admits only coefficient two and then tail $`(h-1)/h`$, giving the specified string of twos.

In the $`r=1`$ branch the initial negative reciprocal permits only $`-2`$, leaving $`-(4m+1)/(10m+2)`$. The next choices are $`-3,-2`$. The first leaves $`-(2m+1)/(4m+1)`$, forcing $`-2,-(2m+1)`$. The second leaves $`2m/(4m+1)`$, whose reciprocal is $`2+1/(2m)`$. Choosing two ends with $`-2m`$; choosing three leaves $`(2m-1)/(2m)`$ and the same string of twos. The strict-tail inequalities exclude all other choices, including when $`m=1`$.

The all-even zero carrier is $`1+[-2,-2,2,-2m]`$. The only other zero carrier is $`[2,-2,-2,-(2m+1)]`$, which has exactly one coefficient of absolute value greater than two. Hence (P) holds. Its one-sided four-band plumbing has a connected orientable essential two-boundary frontier of genus three, violating (SB). By §8 there are also legal $`k=2`$ chain vertices not adjacent to $`a`$, so the entire complex is not an annulus cone. Corollary 1.3 nevertheless contracts it as the all-even cone with one rooted tree.

For $`m>1`$ we retain the full geometric criterion for $`Y_E`$; no fibre-based collapse of this base is assumed. Finally the two-fold branched cover is a lens space whose first homology has order $`16m+3`$ [HT, p.225]. These increasing orders distinguish infinitely many companion knots. ∎

Reflection gives the corresponding conclusion for mirrors: it reverses orientations and slopes compatibly, preserves the carrier condition, and preserves whole-complement cyclic widths.

**Example 10.2 (two odd zero carriers).** The exact recursion at $`8/21`$ gives precisely the following zero-slope carriers:

```math
[2,-2,-2,2],\qquad [3,2,-2,-2],\qquad
1+[-2,-2,2,3].
```

Their signed counts are all zero. The two odd carriers both satisfy (P), and each contributes a separately labelled rooted Farey tree. They cannot coexist or have a cross edge away from $`a`$.

Here the all-even coefficients are all $`\pm2`$. By [HT, p.230] its unique incompressible Seifert surface is a fibre. The two-sheet all-even system is a parallel pair of these fibres, with opposite orientations. Suspension in the mapping torus rotates the fibre pair and realizes either reaching-end choice. A full suspension circuit returns that oriented stack while each boundary makes one meridional circuit, absorbing one outer pattern twist. Thus all the all-even diagrams give one global vertex $`G`$, and $`\mathcal B_E=[a,G]`$. The entire complex is the two rooted odd trees and this one additional leaf. Uniqueness of the odd zero carrier is therefore unnecessary for the theorem.

## 10.3. One odd coefficient: 16/39 and D_m

**Proposition 10.3 (the D family).** For every integer $`m\ge2`$, the zero-slope carriers of $`D_m=K_{8m/(20m-1)}`$ are exactly the all-even expansion $`[2,-2,2m,2]`$ and the odd carrier $`[3,2,2m,-2]`$. The odd sector is the tree of disks of [§9](one-odd-disks.md) (Theorem 9.2) with block length $`L=2`$.

**Proof.** The exhaustive expansion list is:

| r | Coefficients | Boundary slope |
|---:|---|---:|
| 0 | [2,-3,(-2) repeated 2m-2 times,-3] | -4m-2 |
| 0 | [2,-2,2m-1,-2] | -4 |
| 0 | [2,-2,2m,2] | 0 |
| 0 | [3,2,2m,-2] | 0 |
| 0 | [3,2,2m+1,2] | 4 |
| 1 | [-2,-4,(-2) repeated 2m-2 times,-3] | -4m-6 |
| 1 | [-2,-3,2m-1,-2] | -8 |
| 1 | [-2,-3,2m,2] | -4 |

The all-even signed count is two. Hence the only odd zero carrier is [3,2,2m,-2], with block length L=2 and one odd coefficient. Its entire sector is the tree of disks of [§9](one-odd-disks.md), including m=2, the 16/39 example. The all-even base need not be collapsed to one vertex.

For symbolic exhaustion, the r=0 reciprocal is 2+(4m-1)/(8m). Choosing 2 leaves -(4m-1)/(8m), whose reciprocal allows -3 or -2. The -3 choice leaves -(4m-3)/(4m-1), forcing (-2)^(2m-2),-3. The -2 choice leaves 2/(4m-1), with reciprocal 2m-1/2; it gives 2m-1,-2 or 2m,2. Choosing 3 initially leaves (4m+1)/(8m), forces coefficient 2, then leaves 2/(4m+1), giving 2m,-2 or 2m+1,2.

For r=1 the first negative coefficient is forced to -2, leaving -(4m-1)/(12m-1). Its reciprocal is -3-2/(4m-1); choosing -4 gives the same forced negative string, and choosing -3 gives 2/(4m-1) and the two terminating choices. Every step follows the strict-tail criterion; there is no omitted branch. The identity

```math
[\underbrace{-2,\ldots,-2}_{l},-3]=-(2l+1)/(2l+3)
```

also proves uniqueness of the forced negative strings by induction. The numerator and denominator of D_m are coprime since gcd(8m,20m-1)=gcd(8m,4m-1)=1. ∎

At 16/39 the five companion S_2 types are d=-2,-1,0,1,2. All are orientable of genus three and class zero. Their full un-oriented companion coexistence graph is the five-point path; their labelled longer systems and independent orientations are exactly [§15.2](ordered-systems.md) and the boundary word in §15. The global state d at denominator k ranges from -2k to 2k, with unique a,t and the complete joint-path edge test. This gives the complete component, isotopy, joint-order and subcomplex information for the first example.

## 10.4. Two odd coefficients: 12/29 and B_m

**Proposition 10.4 (the B family).** For every integer $`m\ge1`$, put

```math
B_m=K_{(8m^2+2m+2)/(16m^2+8m+5)}.
```

Its zero-slope carriers are exactly the all-even expansion $`E=[2,-2m,2m,-2]`$ and the two-odd carrier $`1+[-2,-(2m+1),2m+1,2]`$. The odd sector consists of three marked Farey trees at the root $`a`$.

**Proof.** Its exhaustive expansions are:

| r | Coefficients | Boundary slope |
|---:|---|---:|
| 0 | [2,-(2m+1),(-2) repeated 2m-1 times,-3] | -4m |
| 0 | [2,-2m,2m,-2] | 0 |
| 0 | [2,-2m,2m+1,2] | 4 |
| 0 | [3,2 repeated 2m-1 times,2m+1,-2] | 4m |
| 0 | [3,2 repeated 2m-1 times,2m+2,2] | 4m+4 |
| 1 | [-2,-(2m+2),(-2) repeated 2m-1 times,-3] | -4m-4 |
| 1 | [-2,-(2m+1),2m,-2] | -4 |
| 1 | [-2,-(2m+1),2m+1,2] | 0 |

The all-even signed count is zero. Only E=[2,-2m,2m,-2] and the two-odd carrier 1+[-2,-(2m+1),2m+1,2] have zero slope. Its one parameter block has L=1, so its sector is three marked trees at a. The family contains B_1=K_(12/29).

For exhaustion write P=8m²+2m+2 and Q=16m²+8m+5; Q=2P+(4m+1). In the r=0 branch coefficient 2 leaves -(4m+1)/P, whose reciprocal is -2m-2/(4m+1). Its choices are -(2m+1), followed by the forced negative string, and -2m, followed by 2/(4m+1) and the two terminating choices 2m,-2 or 2m+1,2.

Initial coefficient 3 leaves (P-4m-1)/P. Its next 2m-1 coefficients are forced to 2: after any number of them the remaining tail has the form

```math
\frac{j(4m+1)+2}{(j+1)(4m+1)+2},\qquad j\geq1,
```

whose reciprocal lies strictly between one and two. At j=0 it is 2/(4m+3), giving 2m+1,-2 or 2m+2,2. In the r=1 branch coefficient -2 is forced and leaves -(4m+1)/(8m²+6m+3). Its reciprocal is -(2m+1)-2/(4m+1), yielding the three displayed negative-integer-part rows. This exhausts all choices, including m=1.

Here Q-2P=4m+1 and P is congruent to two modulo 4m+1, so gcd(P,Q)=1. Both family denominators strictly increase. HT recalls that the branched double cover has first homology of order q, so both are actual infinite families of companion knots, not just repeated diagrams. ∎

The universal theorem makes these family restrictions unnecessary for contractibility, but they supply small explicit structures outside (P). The earlier C_m=K_((6m+1)/(16m+3)) and its mirrors retain their explicit (P) structure.

## 10.5. Examples beyond the one-block class

For 74/103 the odd zero carrier

```math
1+[-4,-2,4,-3]
```

has three large coefficients and one odd coefficient. Its all-even zero carrier is [2,2,2,-2,-2,-2,-2,-4]. Number bands 0,...,3 and root at band 3. The large coordinates are H_0,H_2,H_3=0, with

```math
0\leq H_2\leq N,\qquad -N\leq H_2-H_0\leq N.
```

There are fifteen unoriented two-sheeted types, and (2k+1)(4k+1) possible height states above a marked denominator k. Their labelled coexistence uses the cumulative profiles, not independent profiles of the two raw block sums. There is one signature, and Theorem 12.3 contracts the entire sector.

For 76/119 the odd zero carrier 1+[-3,-4,3,-3] has four large coefficients and three odd coefficients. Its all-even zero carrier is [2,2,-4,-2,-2,-4]. With root at band 0, its two-sheeted types number twenty-seven and give fifteen odd-height signatures (H_2,H_3). The finite diagnostics include exactly this odd/large configuration. The global sector is the pointed union of the fifteen contractible signature sectors; their internal geometry is not assumed to be a tree or an independent raw-block product.
