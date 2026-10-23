# 18. All actual edges: a finite integer criterion

[Contents](../README.md) · [Proof map](main-theorem.md) · [Sources](../sources/bibliography.md)

Take two distinct non-root vertices of this carrier, with denominators k,k'. They are connected surfaces, so by the [geometric foundations](assemblies.md), [whole-block comparison](comparison.md) and [all-even cone](even-cone.md) they are adjacent exactly when they have disjoint representatives. Jointly essentialise their disjoint union at T and normalize the entire companion union on this carrier. Put K=k+k'. Its state is

```math
U_{\rm total}=U+U'.
```

This additivity holds also for complemented variables: (N-x) is the sum of the two subsystem values (N_1-x_1)+(N_2-x_2).

There are two positive reaching endpoints, two negative reaching endpoints and K-2 waves. The two positive endpoints are consecutive in the cyclic endpoint list, as are the two negative endpoints: each pair lies in the same end annulus of the wave system. If the positive block starts at u in Z/(2K), its endpoints are u,u+1, the negative block is u+K,u+K+1, and the waves pair by

```math
p_u(i)=2u+1-i\pmod{2K}
```

away from these four terminals. The companion pairing is q(i)=-1-i.

**Lemma 18.1.** This joint diagram has two legal terminal paths, each joining a positive to a negative endpoint, and no other component if and only if gcd(u+1,K)=1.

**Proof.** Completing p at the two deleted edges gives two fixed-point-free reflections. Their product is translation by 2(u+1). The full alternating graph has gcd(u+1,K) cycles. The deleted positive edge and negative edge must be in the same cycle; otherwise each open path has two terminals on the same actual hole. If they are in the same cycle, every other cycle is a forbidden closed component. Thus exactly one full cycle is required, and deleting the two edges then gives the two required paths. ∎

For a legal diagram let V be the boundary-vertex set of one path, z its positive endpoint, and I(V)=V∩{0,...,K-1} its companion-pair indices. The individual data are

```math
k_V=|V|/2,\qquad
a_V=\mathrm{rank}_{\mathrm{sorted}(V)}(z),
\qquad
U_V=\sum_{i\in I(V)} f_{K,U_{\rm total}}(i).
```

Each q pair is wholly in a path, so |I(V)|=k_V. The second path gives the complementary data. The common outer winding is retained. For the zero-winding joint reference choose the pair with both individual canonical windings zero. This is possible: the two cap arcs are disjoint or parallel, and the canonical determinant calculation below forces their winding integers to agree. An outer turn changes them together.

**Theorem 18.2 (integer edge test).** Two distinct non-root vertices are adjacent if and only if their winding integers agree and, for some u in {0,...,2K-1} with gcd(u+1,K)=1, the two path restrictions above give their respective k,a,U, in either assignment. The root is adjacent exactly to the k=1 vertices.

**Necessity.** Joint essentialisation and the companion formula have already given q, p_u, the two paths and additive state. Their cap replacement is a disjoint pair. Distinct projected arcs have determinant one; coincident projected arcs have identical k,a,t. For different projected arcs, write p=2a+1+4kt and p'=2a'+1+4k't'. The base numerators have ranges 1,...,4k-1 and 1,...,4k'-1. Consequently a nonzero t-t' makes the determinant have absolute value at least k+k'≥2. Thus an actual edge has t=t'. Subsystem naturality identifies the computed restrictions with the original vertices, rather than just with surfaces of the same genus.

**Sufficiency.** Start from the actual joint HT system of state U+U'. Assign its components to the two paths, with the signs required along those paths. Put the two pattern arc systems in their joint reference diagram and apply the common outer turn. Both whole surfaces are legal essential connected assemblies, are disjoint, and have the specified individual states and marked coordinates. Hence they realize the two vertices and have cyclic width one. The actual companion pieces, including nonparallel adjacent S types, were retained throughout.

For the root use no cap waves. After joint essentialisation A cannot have any companion piece, since its Euler characteristic is zero while every longitudinal essential companion piece has negative Euler characteristic. Its pattern seam can miss a chain's waves exactly when there is no wave, that is k=1. Conversely the two reaching arcs of every k=1 form admit a disjoint inner-to-inner seam. ∎

This is a finite arithmetic criterion: there are 2K possible joint anchors, the two paths are finite graphs, and all state restrictions are sums of the explicit indicator formula. It supplies every edge, not only a selected descending edge.
