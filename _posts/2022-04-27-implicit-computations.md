---
title: 'How to formalize the notion that a computation implicitly contains another one?'
date: 2022-04-25
permalink: /posts/2022/04/implicit-computations/
tags:
  - quant-ph
  - cs.cc
---

Suppose you want to play the original version of Tetris, written for a Soviet Elektronika 60 computer - but you only have a binary version of that program. So you write an _emulator_ that runs on your modern MacBook and simulates the Elektronika 60's behaviour to solve the problem. Of course, the straightforward way to write such an emulator is to simulate the Elektronika 60's memory states and CPU step-by-step. Then the emulator's _execution trace_ - the history of instructions and memory states it went through before termination, and the causal implications that gave rise to them - "implicitly contains" all the original computer's calculations. The question is: Can we formalize this notion of "implicit containment", and is it possible to write an emulator that doesn't implicitly perform all the original computer's calculations to predict its display outputs?

If the emulator is to simulate a particular program, the answer may be "yes". For example, an Elektronika 60 program that adds all integers from 1 to n is equivalent to an emulation that returns n*(n+1)/2. But in general, one can form a suspicion that it is impossible - call this the hypothesis that "every emulator is unsurprising".[^1][^2] I currently don't understand how to formalize this intuition for classical Turing machines in a way that yields neither false positives nor false negatives.[^3] But I'd like to discuss a formalization of the analogue for quantum circuits, which works because the no-cloning principle precludes some evasive manoeuvres that a classical emulator could perform.

The quantum case
-------------------
Namely, consider a Hilbert space of $S$ qubits, a subset $\mathcal{A}\subseteq \mathcal{SU}(2^S)$ considered "computationally simple" - for example, those local on 2 qubits - together with a probability measure on $\mathcal{A}$. Furthermore, consider some notion of unitaries being similar, $U \approx V$, e.g. by the condition that $U=V$ or that $\lVert U V^\dagger-I \rVert\leq \epsilon$ according to some matrix norm. Based on that, define the _conditional computational complexity_ of a unitary $U$ given a unitary $V$, $\mathcal{C}(U\mid V)$, as the minimal number of computationally simple unitaries necessary to append to $V$ to approximate $U$:

$\mathcal{C}(U\mid V):=\min \\{t\mid U \approx A_t \ldots A_2 A_1 V, \\{A_1,\ldots, A_t\\}\subseteq \mathcal{A}\\}$.

Now consider an equivalence between sequences of computation steps, $A_n \ldots A_2 A_1 \approx A'\_m \ldots A'\_2 A'\_1$ - with the left-hand side considered the original computation and the right-hand side an alternative computation. Then we say that this equivalence is _k-unsurprising_ (with $k\ll n$ in the cases we are interested in) if for all $i\in \{1,\ldots, n\}$, there exists $j\in \\{1,\ldots, m\\}$ such that $\mathcal{C}(A_i \ldots A_1\mid A'\_j \ldots A'\_1)\leq k$. In words, during its proceeding, the alternative computation comes close to calculating all intermediate results of the original one while it runs. Then our hypothesis is in the spirit of:

(\*) **Choose S and a subset of S' qubits, let $m=poly(n)$, $n=poly(S')$ and $k$ such that $poly(k)=n$. Randomly chose unitaries $A_n \ldots A_1$ under the condition that they act trivially on all qubits except those in the subset.[^4] Then the probability that every equivalence $A_n \ldots A_2 A_1 \approx A'_m \ldots A'_2 A'_1$ is k-unsurprising is 1.**

Of course, one can consider various variants of this hypothesis. However, some bounds on $m$ in $n$ and $n$ in $S'$ seem necessary to me: For a reasonable probability distribution on $\mathcal{A}$, computations of unbounded length will come arbitrarily close to implementing any unitary by ergodicity, so we shouldn't be too surprised by a "surprising algorithm" in that case.

An analogous claim isn't valid in a merely reversible (or classical) model of computation. A strategy to construct a sequence of $V$ contradicting it would be to start by copying the input and computing a high-complexity unrelated function, continue by copying the input again and performing the original computation $U_1,\ldots$, and conclude by uncomputing the unrelated function. The reason this doesn't work in the quantum case is the no-cloning principle, as promised.[^5]

Applications
-------------
Finally, some possible applications of such a notion and result - one connecting to complexity lower bounds, one more philosophical.

 - A similar notion and related theorem may play a part in proving lower bounds on the computational complexity. For example, consider a deterministic algorithm A that calculates whether a non-deterministic Turing machine NT will accept some input. If it calculates that NT won't accept, it makes a statement about the behaviour of NT for all the (exponentially many) non-deterministic choices. If one now proves that
   - any such computation implicitly contains many of the possible intermediate computational steps of NT,
    - a single computational step can't implicitly perform calculations for multiple unrelated branches at once,
one has shown a lower bound on the number of steps.
 
    To me, this approach seems to evade the [natural proofs barrier](https://theory.stanford.edu/~liyang/teaching/projects/natural-proofs-barrier-and-P-NP.pdf), as the property "any algorithm computing a function must implicitly contain a computation of intermediate steps" doesn't seem to be efficiently computable.

- In a quantum analogue, one may try to lower-bound the number of copies of, e.g., magic states needed to perform certain computations in a measurement-based way.

- For a more philosophical application, consider the perennial debate of whether free will "exists". A reductionist approach to this problem - laid out, e.g., [here](https://wiki.lesswrong.com/wiki/Free_will_%28solution%29) - claims to dissolve the problem by  _identifying_ the consciousness subjectively experiencing free will with the algorithm executed by the associated brain. Then even though the algorithm is deterministic and a computer simulating it could predict a person's choices, that computer would have to rerun the algorithm to actually do so. If the algorithm _is_ the consciousness itself, that would mean that, subjectively, the actor themselves makes the decision in the computer or in real physics. An associated catchphrase is that "free will is how an algorithm feels from the inside".

    However, this works much better if one believes in the notion discussed in this post - namely, that every emulation of someone's brain performs structurally similar computations as the original brain, including calculations of intermediate results. The linked discussion explicitly claims so, stating, e.g., that ["it is not possible to compute the Future without computing the Present as an intermediate"](https://www.lesswrong.com/posts/EsMhFZuycZorZNRF5/the-ultimate-source), without an attempt at formalization or proof.

- Relatedly, consider what Scott Aaronson calls the ["pretty-hard problem of consciousness"](https://scottaaronson.blog/?p=1799): Given a description of a physical system (for example, a brain or a computer simulating one), predict whether and what subjective experiences (i.e. actual thoughts and feelings) are implied by a physical realization of that system. One guesses that this mapping is local in time and space: If someone wakes up on a sunny Monday morning and looks out of the window, their subjective experience of seeing a blue sky is a result of physical processes happening at that time, in the part of the universe currently containing their brain.[^6] An unsurprising computer simulation of the person and their environment preserves this notion: One can pinpoint the simulation step in which the simulated person looks out of the window, and (if the computer has multiple processors) the processors that simulate their brain. But with a surprising algorithm, this generally won't work anymore. In conclusion, a result that surprising simulation algorithms don't exist would be helpful for one's peace of mind (and body) regarding this philosophical question.

Conclusion and outlook
----------------------
Formalizing a notion of unsurprising simulation algorithms seems simpler to me in the quantum case. We may compare this to the [adversary bound-quantum query algorithm duality](https://arxiv.org/abs/1504.06943), which has no known full equivalent in the classical case either.

Though my current understanding is sketchy, the recent paper ["Linear growth of quantum circuit complexity"](https://doi.org/10.1038/s41567-022-01539-6) by Haferkamp et al. contains interesting ideas from algebraic geometry to prove that, with probability 1, the complexity of a random circuit grows linearly for subexponential circuit sizes. It seems worth investigating to me whether one can apply these methods to prove the hypothesis (*).

Acknowledgement
---------------
Thanks to XY for a helpful discussion a long time ago.

[^1]: Or, more generally: Any program that makes a nontrivial statement about a collection of generic computations, e.g. an algorithm for an NP-complete problem.

[^2]: The classical time hierarchy theorem in computational complexity tells us that the _amount_ of steps and memory cells can't be much lower than that used by the original of the original program. But it doesn't tell us anything about the _structure_ of possible solvers.

[^3]: One can think of various counterexamples to attempts to formalize this notion. For example, one can convert the computational problem into a 3SAT instance using an NP-completeness reduction and then find the result using brute force or a [derandomized version of Schöning's algorithm](https://dl.acm.org/doi/abs/10.1145/1993636.1993670), randomize the exact point where intermediate steps are performed, encrypt and decrypt intermediate results, or do the calculation using [homomorphic encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption). Considering these examples in more detail, it seems to me that they don't break the general intuition that an analogue should be true, with the caveat that they may invert the _causal order_ in which the program implicitly makes logical deductions. But they did break my attempts at formalizing them.

[^4]: This allows the candidate equivalent algorithms to use more quantum memory than the original one.

[^5]: An idea to go around this would be to allow non-reversibility in the sense that one can delete data when deriving the intermediate results. Fooling such a definition is left as an exercise to the reader.

[^6]: Presumably, even more specifically, their visual processing systems.
