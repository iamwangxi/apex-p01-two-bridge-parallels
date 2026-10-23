# 14. Complete bounded parameter blocks

[Contents](../README.md) · [Proof map](main-theorem.md) · [Sources](../sources/bibliography.md)

Let j_1<...<j_l be the indices of coefficients with |b_i|>2. HT Theorem 1(e) permits simultaneous ±1 changes of adjacent parameters at every other coefficient, with the corresponding single change at an available endpoint.

The two outside blocks are controllable from their endpoints and normalize to zero, exactly by the bounded prefix induction of the pure-stack analysis. Between consecutive large indices j_r,j_(r+1), put L_r=j_(r+1)-j_r and list its L_r parameters x_1,...,x_(L_r) in order. Define

```math
y_i=\begin{cases}x_i,&i\text{ odd},\\ N-x_i,&i\text{ even},\end{cases}
\qquad U_r=\sum_{i=1}^{L_r}y_i,
\qquad 0\leq U_r\leq NL_r.
```

An allowed simultaneous change becomes transfer of one unit between neighboring y boxes, each of capacity N. The sum U_r is invariant.

**Lemma 14.1.** A bounded parameter orbit is determined exactly by (N,U_1,...,U_(l-1)). Every integer vector in the displayed product of intervals occurs.

**Proof.** Transfers cannot change these sums. Conversely neighboring unit transfers connect every bounded composition of a fixed sum. For an explicit normalization, fill the first box to min(N,U), moving units left through the first vacancy; then treat the remaining boxes. At every transfer the donor is nonempty and the receiver has capacity. The final form is

```math
(y_1,\ldots,y_L)=(\underbrace{N,\ldots,N}_{c},r,0,\ldots,0),
\qquad U=Nc+r,\quad0\leq r\lt N.
```

This is a finite algorithm in the original box. Blocks are independent and outside blocks have endpoint moves. HT's complete isotopy statement then proves the classification. ∎

In particular every oriented S_2 class on any odd carrier is indexed, before choosing orientation, by

```math
u_r\in\{0,1,\ldots,2L_r\}.
```

All two-sheeted surfaces are connected by HT Proposition 1(2), and all are orientable by Lemma 13.1. With several blocks this classifies the individual two-boundary types; it does not give their joint order by independently applying the one-block formula below.

For 16/39 on [3,2,4,-2], the only moves are (x_1,x_2)↦(x_1±1,x_2±1) and x_3↦x_3±1. Thus

```math
d=x_1-x_2\in[-N,N],\qquad U=N+d\in[0,2N]
```

is the complete invariant. There are five unoriented two-sheeted types, d=-2,-1,0,1,2; the three even-d types are the doubled-weight frontiers already singled out in the pure-stack analysis. The odd-d types are orientable as well and are retained.
