---
title: 'Reachable Gram matrices in quantum phase estimation'
date: 2022-05-13
permalink: /posts/2022/05/reachable-phaseest/
tags:
  - quant-ph
  - cs.cc
---

A famous, basic algorithm in quantum computing is the [_quantum phase estimation_](https://en.wikipedia.org/wiki/Quantum_phase_estimation_algorithm) algorithm. We can see the algorithm as a quantum query algorithm [^2] for oracles $O_d=\ket{\mathrm{idle}}\bra{\mathrm{idle}} + d\ket{\mathrm{\psi}}\bra{\mathrm{\psi}}$, where $d\in\mathbb{C}, \lVert d \rVert = 1$ is the eigenvalue to be estimated. A natural way to discretize the problem is to choose a natural number $\|D\|>0$, and require that d is a $\|D\|$th root of unity, i.e. choose a set of possible inputs ${d\middle d\in\mathbb{C}, d^{\|D\|}=1}$. As in [^2], we can track the evolutions of all states at once, subsuming all the oracles in a single block-diagonal "super-oracle" $O=\sum_{d\in D}\ket{d}\bra{d}\otimes O_d$, and the states at a certain step in time in a single "super-state" $\ket{\Psi^j}=\sum_{d\in D}\ket{d}\otimes \ket{\psi^j_d}$. What's more, the quantum computer can transform two super-states $\ket{\Psi}$, $\ket{\Psi'}$ into each other without applying the super-oracle iff they have the same reduced density operator on the input register $\mathcal{D}$. The $d,d'$ entry of this RDO $\rho[d,d']$ is given by the inner product $\bra{\psi_{d'}}\ket{\psi_d}$, i.e. up to a transpose, it is the complex analogue of the _Gram matrix_ of this collection of density operators. Similarly, whether it is possible to obtain certain Bayesian evidence about the oracle by a measurement is entirely determined by the Gram matrix at a certain time. Therefore, it is relevant to characterize the Gram matrices reachable after $T$ steps, starting from initial states independent of $d$. We will now do this for up to the $\|D\|-1$st query - and after that query, the identity matrix is reachable, in which case all $\ket{\psi^j_d}$ are orthogonal and one can determine the phase without error.

Fourier transforming the input register
---------------------------------------
The basic idea is to Fourier transform the input register $\mathcal{D}$. Introduce the orthonormal Fourier basis $K={\ket{k}=\|D\|^{-1/2} \sum_{d\in D} d^k\ket{d}\middle k\in \mathbb{Z}\_{\|D\|}}$. In that basis, one can check that the initial Gram matrix - the all-1 matrix - is $\rho^0= \|D\| \ket{0}\bra{0}$, and the oracle $O$ becomes a combination of identity and shift operators: $O=\sum_{k\in \mathbb{Z}\_{\|D\|}}(\ket{k,\mathrm{idle}}\bra{k,\mathrm{idle}}+\ket{k+1,\psi}\bra{k,\psi})=I_{\mathcal{D}} P_{\mathrm{idle}}+X_{\mathcal{D}} P_{\psi}$ (note that the addition in $\mathbb{Z}\_{\|D\|}$ is modulo $\|D\|$). Now this is a simple permutation matrix of the new basis vectors, and it seems much easier to understand which states are reachable after some number of steps.

Condition 1: $P_k\ket{\Psi^j}=0$ for $k>j$.
-----------------------------------------
This condition is simple - by induction and the form of the oracle, the super-state $\ket{\Psi}$ must lie entirely in the subspace spanned by the Fourier modes $0,\ldots,j$ after $j$ queries.

Modified shift operators
------------------------
Now define the "modified shift operator" $X':=X_{\mathcal{D}}(1-P_{\|D\|-1})=(1-P_0)X_{\mathcal{D}}$. Then for $\Delta k \in {0,\ldots,\|D\|-1}$, $X'^{\Delta k}_{\mathcal{D}}=\sum_{k=0}^{\|D\|-1-\Delta k}\ket{k+\Delta k}\bra{k}$, and the expectation values $\expval{X'^{\Delta k}\_{\mathcal{D}}}{\Psi^j}$ are given by sums of Gram matrix elements along the diagonal or an off-diagonal.

Condition 2: $\expval{X'^\Delta k}{\ket{\Psi^j}}=\|D\| \delta_{k,0}$ whenever $j<\|D\|$
-----------------------------------------------------------------------------------
For $j=0$, the claim in the section title [^1] is clearly true with $\delta_{k,0}$ being the Kronecker delta ($1$ for $k=0$, $0$ otherwise). The quantum computer's unitaries don't change the Gram matrix, so what's left to show is that they are conserved after an oracle call in the first $\|D\|-1$ queries. With $\ket{\Psi^j} the super-state directly before the $j$th query (i.e. after at most $\|D\|-2$ queries), we write

$\expval{O^\dagger X'^{\Delta k} O}{\Psi^j}=\\
\bra{\Psi^j}P_{\mathrm{idle}} X'^{\Delta k}\ket{\Psi^j}+\bra{\Psi^j}{P_{\psi}}X^\dagger X'^{\Delta k} X \ket{\Psi^j}$.

By Condition 1, for $j<\|D\|-1$, $X' \ket{\Psi^j}=X\ket{\Psi^j}$ and $\bra{\Psi^j}X^\dagger X'=\bra{\Psi^j}(I-P_{\|D\|-1})=\bra{\Psi^j}$. So the quantity above equals
$\bra{\Psi^j}P_{\mathrm{idle}} X'^{\Delta k}\ket{\Psi^j}+\bra{\Psi^j}{P_{\psi}} X'^{\Delta k} \ket{\Psi^j}=\expval{X'^{\Delta k}}{\Psi^j}$.

Sufficiency of these conditions
-------------------------------
We now show that the conditions above are actually sufficient for reachability in $j< \|D\|$ queries. This works by induction again - here formulated as an infinite descent.

Clearly, the conditions are sufficient for $j=0$. Now consider the smallest $j$ such that a state $\ket{\Phi^j}=\sum^j_{k=0} \ket{k}\otimes\ket{\phi^j_k}$ exists that can't be reached in $j$ queries despite fulfilling conditions 1-2. Condition 2 for $\Delta k=j$ states that $\bra{\phi^0_k}\ket{\phi^j_k}=0$. So up to a unitary acting on query and ancilla space, we can assume that $\ket{\phi^j_0}=\alpha \ket{\mathcal{idle}}\otimes\ket{w}$ and $\ket{\phi^j_j}=\beta \ket{\mathcal{\psi}}\otimes\ket{w}$, where $\ket{w}$ is an arbitrary member of the ancilla space and $\alpha,\beta$ are norms. But then, applying $O^{-1}$ will turn this state into $\ket{\Psi^{j-1}}=\sum^{j-1}\_{k=0}\ket{k}\otimes\ket{\psi^{j-1}\_k}$, i.e. one that fulfills condition 1 for $j-1$ steps. $\ket{\Psi^{j-1}}$ fulfills condition 2 iff $\ket{\Psi^j}$ did, by the inductive step in the proof of condition 2. This state is not allowed to be reachable in $j-1$ steps by assumption, completing the infinite descent.

As promised, after $\|D\|-1$ queries, it is possible to obtain the identity Gram matrix - in the computational basis, this means that the states for all different inputs are orthogonal and can be distinguished without error.

Measurements
------------
Once again, the conditions fit into a semidefinite program/convex optimization problem: In principle, the set of PSD matrices equals the set of Gram matrices for some non-normalized collection of states, condition 1 determines the dimension of the positive semidefinite matrices to consider, and condition 2 is a set of simple linear constraints on these matrices. As in [^2], understanding the set of possible measurement probabilities fits into a semidefinite programming framework as well.

[^1]: If I am not mistaken, the expectation values $X^\Delta k$ being conserved is equivalent to the fact that the diagonal elements of the Gram matrix in the computational basis - i.e. the norms of the basis vectors - stay the same. One can check that $X^\Delta k = X'^\Delta k + (X'^\dagger)^{\|D\|-\Delta k}$, so what we prove for the first $\|D\|-1$ steps is stronger.

References
----------
[^2]: https://github.com/qudent/RhoPaths
