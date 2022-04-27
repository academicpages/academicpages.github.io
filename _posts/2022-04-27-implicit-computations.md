---
title: 'How to formalize the notion that a computation implicitly contains another one?'
date: 2022-04-25
permalink: /posts/2022/04/implicit-computations/
tags:
  - quant-ph
  - cs.cc
---

Suppose you want to play the original version of Tetris, written for a Soviet Elektronika 60 computer - but you only have a binary version of that program. To solve the problem, you write an _emulator_ that runs on your modern MacBook, and simulates the Elektronika 60's behaviour. The straightforward way to write such an emulator is to simulate the Elektronika 60's memory states and CPU step-by-step - but is there another way?


For particular problems, the answer may clearly be "yes" - for example, a program that adds all integers from 1 to n is equivalent to one that returns n*(n+1)/2. But for a generic emulator, one can form a suspicion that this is impossible: That for some inputs, the emulator's _execution trace_ - the history of instructions and memory states it went through before termination, and the causal implications that gave rise to them - must "implicitly contain" contain the execution trace of the original computer's calculation.[^1][^2] In the case of classical Turing machines, I currently don't understand how to formalize this intuition that yields neither false positives nor false negatives - I may write another post going into more detail.[^3] But considering quantum circuits rather than classical Turing machines, I think that formalizing it is possible - largely because the no-cloning principle precludes some strategies how a quantum emulator may fool a definition. What's more, it seems possible to me that one can prove such a notion using ideas from the recent paper ["Linear growth of quantum circuit complexity"](https://doi.org/10.1038/s41567-022-01539-6) by Haferkamp et al.


The quantum case
----------------
Namely, consider a Hilbert space of $S$ qubits, and some subset $\mathcal{A}\subseteq \mathcal{SU}(2^S)$ defined to be "computationally simple" (e.g. all unitaries acting on only 2 qubits - for a ideas are fleshed out e.g. in the [Haferkamp et al. paper](https://doi.org/10.1038/s41567-022-01539-6), together with a probability measure on that subset. Furthermore, consider some notion of unitaries being similar, $U \approx V$, e.g. by the condition that $U=V$ or that $\lVert U V^\dagger-I \rVert\leq \epsilon$ according to some matrix norm. Based on that, define the _conditional computational complexity_ of a unitary $U$ given a unitary $V$, $\mathcal{C}(U\mid V)$, as the minimal number of computationally simple unitaries necessary to append to $V$ to approximate $U$:

$\mathcal{C}(U\mid V):=\min \\{t\mid U \approx A_t \ldots A_2 A_1 V, \\{A_1,\ldots, A_t\\}\subseteq \mathcal{A}\\}$.

Now consider an equivalence between sequences of computation steps, $A_n \ldots A_2 A_1 \approx A'\_m \ldots A'\_2 A'\_1$ - with the left-hand side considered the original computation and the right-hand side an alternative computation. Then we say that this equivalence is _k-unsurprising_ (with $k\ll n$ in the cases we are interested in) if for all $i\in \{1,\ldots, n\}$, there exists $j\in \\{1,\ldots, m\\}$ such that $\mathcal{C}(A_i \ldots A_1\mid A'\_j \ldots A'\_1)\leq k$ - in other words, during its proceeding, the alternative computation comes very close to calculating all intermediate results of the original one while it runs. Then the hypothesis of this post can then be made more rigorous in the folllowing style:

(\*) **Choose S and a subset of S' qubits, let $m=poly(n)$, $n=poly(S')$ and $k$ such that $poly(k)=n$. Randomly chose unitaries $A_n \ldots A_1$ under the condition that they act trivially on all qubits except those in the subset.[^4] Then the probability that every equivalence $A_n \ldots A_2 A_1 \approx A'_m \ldots A'_2 A'_1$ is k-unsurprising is 1.**

Of course, one can consider various variants of this hypothesis. However, some bounds on $m$ in $n$ and $n$ in $S'$ seems necessary to me: For a reasonable probability distribution on $\mathcal{A}$, computations of unbounded length will come arbitrarily close to implementing any unitary by ergodicity, so we shouldn't be too surprised by a "surprising algorithm" in that case.

An analogous claim isn't true in a merely reversible (or classical) model of computation. A strategy to construct a sequence of $V$ contradicting it would be to first copy the input and compute a high-complexity unrelated function, then copy the input again and perform the original computation $U_1,\ldots$, and finally uncompute the unrelated function. In the general quantum case, the no-cloning principle forbids this.[^5]

A recent paper by Haferkamp et al. shows that, for reasonable models of random circuits, the circuit complexity of a random unitary grows linearly with the number of steps. To my understanding, this is not exactly enough to show a hypothesis of the form in (\*). Nevertheless, it seems to me that the methods used in that paper may be helpful for a rigorous proof.


Applications
------------
Finally, I'll talk about possible applications of such a notion and result - one connecting to mathematical open problems, one more philosophical.

 - A similar notion and related theorem may play a part in proving lower bounds on the computational complexity. Consider a deterministic algorithm A that solves an NP-complete problem, i.e. calculates whether a nondeterministic Turing machine NT will accept some input. If it calculates that NT won't accept, it makes a statement about the behaviour of NT for all the (exponentially many) nondeterministic choices. If one now proves a theorem that any such computation implicitly contains many of the possible intermediate computations of NT, and a theorem that a single computational step can't implicitly perform calculations for multiple unrelated branches at once, one has shown a lower bound on the number of steps.
 
To me, this approach seems to evade the [natural proofs barrier](https://theory.stanford.edu/~liyang/teaching/projects/natural-proofs-barrier-and-P-NP.pdf), as the property "any algorithm computing a function must implicitly contain a computation of intermediate steps" doesn't seem to be efficiently computable.

- In a quantum analogue, one may try to lower-bound the number of copies of e.g. magic states needed to perform certain computations in a measurement-based way.

- For a more philosophical application, consider the perennial debate of whether free will "exists". A reductionist approach to this problem - laid out e.g. [here](https://wiki.lesswrong.com/wiki/Free_will_%28solution%29) - claims to dissolve the problem by  _identifying_ the consciousness subjectively experiencing free will with the algorithm executed by the associated brain. Then even though the algorithm is deterministic and a computer simulating it could predict a person's choices, that computer would have to rerun the algorithm to actually do so. If the algorithm _is_ the consciousness itself, that would mean that, subjectively, the actor themselves makes the decision in the computer or in real physics. An associated catchphrase is that "free will is how an algorithm feels from the inside".

However, this works much better if one believes in a notion as discussed in this post - namely, that every emulation of someone's brain performs structurally similar computations as the original brain, including calculations of intermediate results. The linked discussion explicitly claims so, stating e.g. that ["it is not possible to compute the Future without computing the Present as an intermediate"](https://www.lesswrong.com/posts/EsMhFZuycZorZNRF5/the-ultimate-source), without an attempt at formalization or proof.

- Relatedly, consider what Scott Aaronson calls the ["pretty-hard problem of consciousness"](https://scottaaronson.blog/?p=1799): Given a description of a physical system (for example, a brain or a computer simulating one), predict whether and what subjective experiences (i.e. actual thoughts and feelings) are implied by a physical realization of that system. One guesses that this mapping is local in both time and (at least to some degree) in space: If someone wakes up on a sunny Monday morning and looks out of the window, their subjective experience of seeing a blue sky is a result of physical processes happening at that time, in the part of the universe currently containing their brain.[^6] An unsurprising computer simulation of the person and their environment preserves this notion: One can pinpoint the time when the simulated person looks out of the window, and (if the computer has multiple processors) the processors that simulate their brain. But this generally won't work anymore with a surprising algorithm. In conclusion, a result that surprising simulation algorithms generally don't exist would be helpful for one's peace of mind (and body) regarding this philosophical question.

Conclusion and outlook
----------------------
Formalizing a notion of unsurprising simulation algorithms seems simpler to me in the quantum case. We may compare this to the [adversary bound-quantum query algorithm duality](https://arxiv.org/abs/1504.06943), which has no known full equivalent in the classical case either.

Though my current understanding is sketchy, the Haferkamp et al. paper contains interesting ideas from algebraic geometry to prove that, with probability 1, the complexity of a random circuit grows linearly for subexponential circuit sizes. To me, it seems worth investigating whether one can apply these to prove the hypothesis (*).

Acknowledgement
---------------
Thanks to XY for a helpful discussion a long time ago.

[^1]: Or, more generally: Any program that makes a nontrivial statement about a collection of generic computations, e.g. an algorithm for an NP-complete problem.

[^2]: The classical time hierarchy theorem in computational complexity tells us that the _amount_ of steps and memory cells can't be much lower than that used by the original of the original program. But it doesn't tell us anything about the _structure_ of possible solvers.

[^3]: One can think of various caveats to attempts formalizing this notion. For example, one can convert the computational problem into that of solving a 3SAT instance using an NP-completeness reduction, and then find the result using brute force or Schöning's algorithm. One can randomize the exact point where intermediate steps are performed, encrypt and decrypt intermediate results, or do the calculation using [homomorphic encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption). Considering these examples in more detail, it seemed to me that they don't break the general _intuition_ that an analogue should be true, with the caveat that they may invert the _causal order_ in which the program implicitly makes logical deductions. But they did break my attempts at formalizing them.

[^4]: In other words, we allow the equivalent algorithms to use more quantum memory than the original one.

[^5]: An idea to go around this would be to allow non-reversibility in the sense that one is allowed to delete data when deriving the intermediate results. Fooling such a definition is left as an exercise to the reader.

[^6]: Presumably, even more specifically, their visual processing systems.
