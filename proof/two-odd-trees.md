# 11. Two odd coefficients and one free block

[Contents](../README.md) · [Proof map](main-theorem.md) · [Sources](../sources/bibliography.md)

Suppose there are exactly two large coefficients, both odd, with $`L`$ parameters between them; all other coefficients are $`\pm2`$. Endpoint moves normalize the outside blocks and Lemma 14.1 gives one invariant $`U`$ in $`[0,NL]`$.

**Lemma 11.1.** The two fold axes differ by $`\pm2U`$ modulo $`N`$. Hence their reflections agree exactly when $`N`$ divides $`2U`$.

**Proof.** Pack the block to full boxes and one partial box by bounded moves. Full inner or outer plumbing transports the ordered sheets wholly in order or in reverse and changes the transported cycle origin by a full cycle; it does not change equality of the two axes. The partial box of $`r`$ sheets changes the origin between the two odd bands by $`r`$ notches, up to sign. Conjugating a reflection by that rotation changes its constant $`c`$ by $`\pm2r`$. This is the same labelled-cycle calculation as HT Figs.26 and 30. Complementing the alternating parameter reverses that sign, and full boxes contribute multiples of $`N`$. With $`U=Nc+r`$ the criterion is exactly $`N`$ divides $`2U`$. This argument has only one partial plumbing, so no multi-block transport is being suppressed. ∎

For a global vertex $`N=2k`$, Theorem 13.2 forces equal axes. Thus

```math
U=kj,\qquad j\in\{0,1,\ldots,2L\}.
```

The two-sheeted surfaces $`S_j`$ are all orientable and pairwise nonisotopic by the complete block invariant. Multiplying their weights by $`k`$ gives $`k`$ parallel normal copies, so the entire allowed companion system is a pure $`S_j`$ stack. No other parameter system can be a global vertex.

Different $`S_j`$ and $`S_h`$ cannot be disjoint. Their union would have $`N=4`$ and $`U=j+h`$. If $`j+h`$ is odd, the two axes differ and the union has a larger component, contradicting a union of two surfaces. If $`j+h=2v`$, the normal system is two parallel copies of $`S_v`$, and cannot contain two distinct types. This is also a direct necessity check on the joint system; deleting an unwanted component is not allowed.

**Theorem 11.2.** This carrier sector is a wedge at $`a`$ of $`2L+1`$ marked Farey trees, one for each $`S_j`$. Its vertices have coordinates $`(j,k,a,t)`$, with the usual gcd condition, and within one $`j`$ its edge rule is $`\mathrm{abs}(pk'-p'k)=1`$. Different $`j`$ sectors have no non-root edge.

**Proof.** On each pure type, nested pairing, legal matching and positive genus are exactly the inputs of the [cap-wave proof](odd-trees.md). Lemma 16.1 excludes both full and half returns even for a non-frontier $`S_j`$. Thus its coordinates are unique. Jointly normalizing a disjoint pair gives one $`S_j`$ stack, while distinct $`j`$ cannot coexist by the preceding argument. Both directions of the marked arc edge correspondence follow by assigning the actual parallel pieces to their cap waves. The root is adjacent exactly to $`k=1`$. Each marked graph is a tree, and the finite wedge contracts to $`a`$. ∎

For $`12/29`$, the carrier is $`1+[-2,-3,3,2]`$, $`L=1`$, and the free parameter is $`n_2`$. The allowed $`N=2k`$ systems are $`n_2=0,k,2k`$. Its sector is three Farey trees at $`a`$. At $`N=4`$ the intermediate values $`n_2=1,3`$ instead give connected four-boundary surfaces; at $`N=6`$ the value $`n_2=2`$ gives the essential six-boundary frontier from the pure-stack analysis. Theorem 13.2 excludes all of these larger pieces from every global assembly, and retains the three two-boundary types.
