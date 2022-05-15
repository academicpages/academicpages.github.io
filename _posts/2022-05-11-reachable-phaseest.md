---
title: 'Reachable states in quantum phase estimation'
date: 2022-05-13
permalink: /posts/2022/05/reachable-phaseest/
tags:
  - quant-ph
  - cs.cc
---

A famous, basic algorithm in quantum computing is the [_quantum phase estimation_](https://en.wikipedia.org/wiki/Quantum_phase_estimation_algorithm) algorithm. We can see the algorithm as a quantum query algorithm [^2] for oracles $O_d=\ket{\mathrm{idle}}\bra{\mathrm{idle}} + d\ket{\mathrm{\psi}}\bra{\mathrm{\psi}}$, where $d\in\mathbb{C}, \lVert d \rVert = 1$ is the eigenvalue to be estimated - for discretization purposes, wechoose $\|D\|\in\mathbb{N}^{+}$ and assume $d$ is a $\|D\|$th root of unity, $d\in D$ with $D:=\left\\\{d\mid d\in\mathbb{C}, d^{\|D\|}=1\right\\\}$.

We'll characterize which combinations of states (for some $d\in D$) are reachable in $j$-query quantum query algorithms, i.e. algorithms starting from a $d$-independent initial state $\ket{\psi^0}$ and applying $O_d$ $j$ times in between $d$-independent unitaries $O^0,\ldots, O^j$, acting on the query space together with an _ancilla space_ $\mathcal{W}$. As in [^2], we can track the evolutions of all states at once, subsuming all the oracles in a single block-diagonal "super-oracle" $O=\sum_{d\in D}\ket{d}\bra{d}\otimes O_d$, and the states after the $j$th oracle application in a single "super-state" $\ket{\Psi^j}=\sum_{d\in D}\ket{d}\otimes \ket{\psi^j_d}$, where the $\ket{d}$ are computational basis vectors of a new Hilbert space $\mathcal{D}$.

# Fourier transforming the input register
The basic idea is to Fourier transform the input register $\mathcal{D}$. Introduce the orthonormal Fourier basis $K=\left\{\ket{k}=\|D\|^{-1/2} \sum_{d\in D} d^k\ket{d}\mid k\in \mathbb{Z}\_{\|D\|}\right\}$. In that basis, the initial state is $\ket{\Psi^0}=\|D\| \ket{0}\bra{0}\otimes\ket{\psi^0}$, and the oracle $O$ becomes a combination of identity and shift operators: $O=\sum_{k\in \mathbb{Z}\_{\|D\|}}(\ket{k,\mathrm{idle}}\bra{k,\mathrm{idle}}+\ket{k+1,\psi}\bra{k,\psi})=I_{\mathcal{D}} P_{\mathrm{idle}}+X_{\mathcal{D}} P_{\psi}$ (note that the addition in $\mathbb{Z}\_{\|D\|}$ is modulo $\|D\|$). Now this is a simple permutation matrix of the new basis vectors, and it seems much easier to understand which states are reachable after some number of steps. 

## Condition 1: $P_k\ket{\Psi^j}=0$ for $k>j$.
By induction and the form of the oracle, the super-state $\ket{\Psi}$ must lie entirely in the subspace spanned by the Fourier modes $0,\ldots,j$ after $j$ queries.

## Condition 2
### Modified shift operators
Now define the "modified shift operator" $X':=X\_{\mathcal{D}}(1-P_{\|D\|-1})=(1-P_0)X\_{\mathcal{D}}$, with $X_{\mathcal{D}}$ as in the Fourier basis definition of $O$. Then for $\Delta k \in {0,\ldots,\|D\|-1}$, $(X')^{\Delta k}=\sum\_{k=0}^{\|D\|-1-\Delta k}\ket{k+\Delta k}\bra{k}$, and the expectation values $\langle \Psi^j \mid (X')^{\Delta k}\mid \Psi^j \rangle$ are given by sums of diagonal or off-diagonal reduced density operator entries on the $\mathcal{D}$ register.

### The condition: $\langle\Psi^j\mid (X')^{\Delta k}\mid \Psi^j\rangle=\|D\| \delta_{\Delta k,0}$ for $j<\|D\|, \Delta k \in \mathbb{Z}\_{\|D\|}$
For $j=0$, the claim in the section title [^1] is clearly true with $\delta_{k,0}$ being the Kronecker delta ($1$ for $k=0$, $0$ otherwise). The quantum computer's unitaries act trivially on $\mathcal{D}$ and don't change the expectation values, so we are done when we show that they are conserved after an oracle call in the first $\|D\|-1$ queries. With $\ket{\Phi^j}$ the super-state directly before the $j$th query (i.e. after at most $\|D\|-2$ queries), we write

$\langle \Phi^j \mid O^\dagger (X')^{\Delta k} O \mid \Phi^j \rangle=\\
\bra{\Phi^j}P_{\mathrm{idle}} (X')^{\Delta k}\ket{\Phi^j}+\bra{\Phi^j}{P_{\Phi}}X\_{\mathcal{D}}^\dagger (X')^{\Delta k} X\_{\mathcal{D}} \ket{\Phi^j}$.

By Condition 1, for $j<\|D\|-1$, $X' \ket{\Phi^j}=X\ket{\Phi^j}$ and $\bra{\Phi^j}X^\dagger X'=\bra{\Phi^j}(I-P_{\|D\|-1})=\bra{\Phi^j}$. So the quantity above equals
$\bra{\Phi^j}P_{\mathrm{idle}} (X')^{\Delta k}\ket{\Phi^j}+\bra{\Phi^j}{P_{\Phi}} (X')^{\Delta k} \ket{\Phi^j}=\langle \Phi^j \mid (X')^{\Delta k} \mid \Phi^j \rangle$.

### Sufficiency of these conditions
### Reversing condition 2
We can easily reverse the calculation proving condition 2: If $j<\|D\|-1$, $\ket{\Phi^j}=O U $\ket{\Phi^{j-1}}$$, $\ket{\Phi^{j-1}}$ fulfills condition 1 and $\ket{\Phi^j}$ fulfills condition 2, then $\ket{\Phi^{j-1}}$ fulfills condition 2 as well.

### Reversing condition 1
Let $0<j<\|D\|$, and $\ket{\Phi^j}=\sum^j_{k=0} \ket{k} \otimes \ket{\psi^j_k}$ be a super-state fulfilling both conditions. Condition $2$ for $\Delta k = j$ states that $\langle \psi^j_j \mid \psi^j_0 \rangle=0$. So we can find a unitary $U\ket{\psi^j_0}=\ket{0}\otimes{$ mapping these two states to arbitrary ortogonal state 

Sufficiency of these conditions
-------------------------------
We now show that the conditions above are actually sufficient for reachability in $j< \|D\|$ queries. We work backwards: Assuming $\ket{\Psi^j}$ fulfilling conditions 1-2, we show that $\ket{\Psi^j}=O U \ket{\Psi^{j-1}}$ with $\ket{\Psi^{j-1}}$ fulfilling these conditions for step $j$, and the quantum computer's unitary $U$ acts trivially on $\mathcal{D}$. If the $\ket{\Psi^{j-1}}$ fulfills condition 1, the calculation used in the proof of condition 2 proves that it fulfills that condition as well.

Clearly, the conditions are sufficient for $j=0$. Now consider the smallest $j$ such that a state $\ket{\Phi^j}=\sum^j_{k=0} \ket{k}\otimes\ket{\phi^j_k}$ exists that can't be reached in $j$ queries despite fulfilling conditions 1-2. Condition 2 for $\Delta k=j$ states that $\bra{\phi^0_k}\ket{\phi^j_k}=0$. So up to a unitary acting on query and ancilla space, we can assume that $\ket{\phi^j_0}=\alpha \ket{\mathcal{idle}}\otimes\ket{w}$ and $\ket{\phi^j_j}=\beta \ket{\mathcal{\psi}}\otimes\ket{w}$, where $\ket{w}$ is an arbitrary member of the ancilla space and $\alpha,\beta$ are norms. But then, applying $O^{-1}$ will turn this state into $\ket{\Psi^{j-1}}=\sum^{j-1}\_{k=0}\ket{k}\otimes\ket{\psi^{j-1}\_k}$, i.e. one that fulfills condition 1 for $j-1$ steps. $\ket{\Psi^{j-1}}$ fulfills condition 2 iff $\ket{\Psi^j}$ did, by the inductive step in the proof of condition 2. This state is yofTODO...? allowed or not? allowed to be reachable in $j-1$ steps by assumption, completing the infinite descent.

As promised, after $\|D\|-1$ queries, it is possible to obtain the identity Gram matrix - in the computational basis, this means that the states for all different inputs are orthogonal and can be distinguished without error.

# Measurements
Once again, the conditions fit into a semidefinite program/convex optimization problem: In principle, the set of PSD matrices equals the set of Gram matrices for some non-normalized collection of states, condition 1 determines the dimension of the positive semidefinite matrices to consider, and condition 2 is a set of simple linear constraints on these matrices. As in [^2], understanding the set of possible measurement probabilities fits into a semidefinite programming framework as well.

# Footnote
[^1]: If I am not mistaken, the expectation values $X^{\Delta k}$ being conserved is equivalent to the fact that the diagonal elements of the Gram matrix in the computational basis - i.e. the norms of the basis vectors - stay the same. One can check that $X\_{\mathcal{D}}^\Delta k = X'^\Delta k + (X'^\dagger)^{\|D\|-\Delta k}$, so what we prove for the first $\|D\|-1$ steps is stronger.

# References

[^2]: https://github.com/qudent/RhoPaths
