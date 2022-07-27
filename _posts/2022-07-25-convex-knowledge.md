---
title: 'The \mathbb{R}-algebra of quasiknowledge and convex optimization'
date: 2022-07-25
permalink: /posts/2022/07/convex-knowledge/
tags:
  - cs.ml
  - cs.cc
  - quant-ph
---
Consider a learner in a (for now, classical) environment described by a ground truth $d\in D.$ The learner wants to find out something about the environment (e.g. output some function $f(d)$ with low error probability for any $d$). It can't influence $d$ (therefore I don't call it "agent"), but may have a choice of which "experiment" to perform in any step, each yielding probabilistic information $p(\mathrm{result}|d)$. Our basic question is about finding good strategies to achieve such a goal - or proving lower bounds on the required number of steps for some problems.

As in any optimization problem, it would be nice to have a _convex_ description of the possible strategies and intermediate "states of knowledge", i.e. one such that the acceptable strategies and intermediate states
 1. form a convex subset of a real vector space,
 2. the states are necessary and sufficient to describe the computer's state of knowledge,
 3. if two states of knowledge are attainable by the learner, their convex combinations are attainable as well, and
 4. if two states allow solving some problem, their convex combinations allow solving that problem as well.

This would allow using the powerful methods of [convex optimization and convex
duality](https://web.stanford.edu/~boyd/cvxbook/) (to be more precise, [semidefinite programming](https://en.wikipedia.org/w/index.php?title=Semidefinite_programming&oldid=1092453332)) to obtain lower bounds and algorithms.

But a naive description by conditional probability matrices doesn't fulfill the fourth property. For example, if the learner's internal state was some permutation of the environment's state, each individual state would correspond to complete knowledge, but randomly mixing them yields a state of complete ignorance.

The aim of this note is to find a convex description for classical agents/learners.[^2] In contrast to the quantum case, our development doesn't give great bounds on the dimension of the vector space.

## Motivation from quantum query complexity
(Note: The next paragraph gives motivation from research on quantum query algorithms, but one shouldn't need to know anything about quantum physics or query algorithms to follow the rest of this post.)

A great thing about the quantum analogue of this problem (_quantum query algorithms_) is that such a description exists there, namely the Gram matrix of the states for different inputs at a given time. This means that the Gram matrices. This allowed developments like [Barnum-Saks-Szegedy 2003](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.113.1101&rep=rep1&type=pdf) - and arguably the [adversary bound - query algorithm duality](https://www.cs.umd.edu/~amchilds/qa/qa.pdf), in particular when developed like [here](https://github.com/qudent/RhoPaths).

## Sketch of the construction
The basic plan is as follows:
1. We start with a naive description of states of knowledge [of an agent about its environment] as collections/matrices of conditional probabilities p(internal memory state|environmental ground truth)≥0; for now, we drop the requirement that the conditional probabilities sum to $1$ for any possible ground truth. We call these CPMs (conditional probability matrices); we consider all possible sets of internal memory states at once (i.e. don't fix the number of rows). The set of possible ground truths is fixed; we denote it by $D$.
2. For CPMs $C_1,C_2$, we write that $C_1\leq C_2$ iff the agent/learner can transform $C_2$ into $C_1$ by a probabilistic transformation without any interaction with the environment. Input and output dimensions are not necessarily equal, and transition probabilities must sum to **at most** $1$.[^3] Clearly, this means that $C_1$ corresponds to "at most as much knowledge" as $C_2$.
3. We say $C_1$ and $C_2$ are equivalent iff $C_1\leq C_2$ and $C_2\leq C_1$. We define the set of **states of knowledge** (SOKs), $\mathbb{K}$, by modding out this equivalence relation from the set of CPMs. Mathematically, $\leq$ was a preorder on the CPMs and becomes a partial order on $\mathbb{K}$.
4. On $\mathbb{K}$, we define multiplication with a nonnegative scalar elementwise, and addition by a **direct sum** of the matrices making up the summands (i.e. taking a disjoint union of the internal memory states, and collecting the conditional probabilities). We can check this behaves well with the equivalence relation. We can also check that addition behaves well with our notion of $\leq$, i.e. $K_1\leq K_2$ iff $K_1+K_3\leq K_2+K_3$. Mathematically, we arrive at a structure called an "[ordered semigroup](https://en.wikipedia.org/w/index.php?title=Ordered_semigroup&oldid=978175111)", which we will turn into an ordered group in step 8. With these definitions, $\mathbb{K}$ is a convex set to which the same intuitions as listed for Gram matrices above apply.[^4]
5. We also define multiplication of two collections by considering the learner to have access to uncorrelated information representing the factors: If the factors are represented by CPMs over internal memory states $a \in A$, $b \in B$, the product is represented by a CPM over the Kronecker product $A\times B$, with the joint probabilities products of the factor probabilities $p((a,b)\mid D)=p(a\mid D)p(b\mid D)$ for $(a,b)\in A\times B$. Besides behaving well with the equivalence relation, it's also commutative on the SOKs.[^6]

6. A vector of nonnegative numbers $\vec{p}\in (\mathbb{R}^+\cup\\\{0\\\})^D$ is represented in $\mathbb{K}$ by a CPM with only one internal memory state. $0$, $1$ and $d\in D$, $D'\subseteq D$ are treated as the all-$0$, all-$1$, and indicator function vectors[^5]. Then in the equivalence classes, $\mathbf{0},\mathbf{1}\in\mathbb{K}$ are neutral w.r.t. addition and multiplication; they correspond to a state of $0$ probability and a state of zero knowledge. We also define $\Omega\in\mathbb{K}$ as the state of complete knowledge.
7. (Note: You can skip reading this item at any time and proceed to the next one.)

   For an example, suppose the learner is in a SOK $K\in\mathbb{K}$ and should make a binary decision which of two experiments to perform next. So it will perform some probabilistic procedure and save the result in an additional register $R'$ with possible states $1$, $2$. Then the memory states where $R'=1$, and the memory states where $R'=2$, form (non-normalized) SOKs individually that sum to a state obtainable from $K$:

   $K_1+K_2\leq K.$

   Now suppose the experiments generate additional data that individually correspond to SOKs $E_1,E_2\in \mathbb{K}$. Then the feasible states of knowledge after one more experiment are given by

   $\\\{E_1 K_1 + E_2 K_2 \mid K_1 + K_2 \leq K\\\}$

   with $K_1,K_2\in\mathbb{K}$.

   Now suppose we have given $K\in\mathbb{K}$ and some utility function $f\colon D\times R\to\mathbb{R}^+ \cup \\\{0\\\}$. So the learner outputs some $r\in R$, and depending on the ground truth $d\in D$, it gets some utility $f(r,d)$. A special case is computing single- or multi-valued functions (the utility is $1$ if the chosen $r$ was acceptable for $d$, $0$ otherwise). The vector $\overrightarrow{f(r,\cdot)}$ represents the utilities the learner would obtain if it always chose $r$; we can consider it as a member of $\mathbb{K}$ as above. Then the claim that the learner can obtain a combination of expected utilities $\vec{q}\in(\mathbb{R}^+\cup\\\{0\\\})^D$ for the various ground truths corresponds to the existence of $K_r\in\mathbb{K}$ for $r\in R$ such that

   $\vec{q}\leq \sum_{r\in R} K_r \overrightarrow{f(r,\cdot)},~~\sum_{r\in R} K_r\leq K$.

   In particular, function evaluation that should succeed with probability at least $1-\epsilon$ for all $d\in D$ corresponds to $\vec{q}=(1-\epsilon)\mathbf{1}$.

   We can chain multiple steps of choosing experiments, starting from complete ignorance, and obtain a convex optimization problem: Suppose we have a (finite for now) set $Q$ of possible experiments, each yielding data $E_q$ for $q\in Q$, and an initial SOK $K^0\in\mathbb{K}$. After $T$ steps, a target SOK $\mathbb{K}^T\in\mathbb{K}$ is achievable iff we can find $K^t_q\in\mathbb{K}$ for $0\leq t<T$, $q\in Q$ such that

   $\sum_{q\in Q} K^0_q \leq K_0,$

   $\sum_{q\in Q} K^t_q\leq\sum_{q\in Q} K^{t-1}_q E_q$ for $1\leq t \leq T-1,$

   $K^T \leq \sum_{q\in Q} K^{T-1}_q E_q.$

   In terms of symbols, this looks analogous to the semidefinite program in Barnum-Saks-Szegedy, equations 9-11 [here](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.113.1101&rep=rep1&type=pdf). The output conditions (the condition that a SOK allows computing some function with a given maximal error), relations 12-13 in that paper, are equivalent to our output conditions as well.

   If such an assignment exists, we can also take a time-average of all the $K^t_q$. Calling these $\overline{K}_q$, we find from adding the inequalities above that

   $K^T + \sum\_{q\in Q}\overline{K}\_q\leq K^0 + \sum\_{q\in Q} \overline{K}\_q E\_q.$

   In quantum query complexity, the requirement that such $\overline{K}_q\in\mathbb{K}$ need to exist for SOKs to be transformable in a given number of experiments yields the _adversary bound_. There, one can apply convex duality to the situation: Feasible solutions of the dual problems yield proofs that given SOKs _aren't_ transformable in a certain number of steps, effectively lower bounds for the complexity of solving that problem.

   Assume now that we have found such a collection of $\overline{K}\_q\in\mathbb{K}$ that fulfill the above inequality for some $T$. Furthermore, assume the algorithm has the option to "do no experiment" as well, i.e. let $\mathbf{1}$ be in the choices of experiments. Then we can "almost solve" the problem of converting $K_0$ to $K_T$ by following a "straight-line path" of intermediate states: The inequality for the $\overline{K}_q$ implies the inequality

   $\frac{K^0 (N-(j+1)) + K^T (j+1)}{N}\mathbf{1} + \frac{1}{N}\sum\_{q\in Q}\overline{K}\_q \leq \frac{K^0 (N-j) + K^T j}{N}\mathbf{1} + \frac{1}{N}\sum\_{q\in Q} \overline{K}\_q E\_q$

   for any natural number $N>0$, $j\in \{0,\ldots,N-1\}$. By the discussion above, these are just the inequalities we need to show that we can transform

   $K_0 + \frac{1}{N}\sum\_{q\in Q}\overline{K}\_q\rightarrow K_T + \frac{1}{N}\sum\_{q\in Q}\overline{K}\_q$

   in $N$ experiments, for any $N$, where the intermediate states are convex mixtures of the initial and the final state. As we let $N\to \infty$, this roughly shows that we are "almost" able to transform $K_0$ to $K_T$ with this construction. This is an analogue of the universal algorithm dual of the adversary bound, in the way developed [here](https://github.com/qudent/RhoPaths).

   Things to think about:
   1. In the quantum case, one can show a concrete bound on how wrong this algorithm would be for some $N$ when applied to some initial state (rather than the shifted initial state) - basically, by a triangle inequality. One can also do this in an ad-hoc way in the classical case. But I don't have a good way to formalize/abstract this in this algebra right now.
   2. It is also weird that this construction needs the algorithm's ability to do nothing. In the classical case, if an algorithm decides it needs to do nothing, it can just do the next internal processing step instead. I don't know if this is possible coherently in the quantum case, however. It would be nice to be able to put this construction into the formalism.

8. Our $+$ and $0$ yield a commutative monoid, i.e. we can add and have a neutral element, but can't yet subtract. A [_Grothendieck group construction_](https://en.wikipedia.org/w/index.php?title=Grothendieck_group&oldid=1091622036)[^26] allows us to turn this monoid into a commutative group. We obtain an $\mathbb{R}$-algebra, which is also a vector space.[^27] Our original set of "physical" states of knowledge is still a convex subset of that vector space. So if we find or truncate to a finite basis, we can hopefully do convex optimization and duality over it.
9. Together, addition and multiplication allows us to define formal power series of knowledge. For example, suppose our learner observes the stars with a telescope without making any choices. In an infinitesimal time $\Delta t\to 0$, it observes a supernova with probability $r \Delta t$, generating experimental data $A\in \mathbb{K}$. Otherwise, it observes nothing. If $K(t)$ is the state of knowledge over time, we obtain

   $K(t+\Delta t)\to ((1-r \Delta t)\mathbf{1}+r\Delta t A) K(t).$

   This is solved by

   $K(t)=\exp((A-\mathbf{1})rt) K(0)$,

   which is to be interpreted as the appropriate formal infinite power series. In fact, writing

   $K(t)=\exp(-rt)\exp(Art)K(0)=\sum^\infty_{k=0} \frac{\exp(-rt) (rt)^k}{k!} A^k K(0)$

   shows that the amount of knowledge obtained follows a Poisson distribution. Note that these equations contain minus signs, so our Grothendieck construction was probably helpful.

10. We discussed classical probability theory so far. But I think this works for both pure and mixed quantum theory as well, though I haven't thoroughly worked through the details and don't want to make a definite claim - it would be really nice to get an adversary method for faulty query algorithms though:
	1. For pure quantum theory, the CPMs correspond to collections of wavefunctions for $d\in D$, and the $\leq$ relation corresponds to applying unitaries and projectors. Then the convex space _should_ be equivalent to the space of Gram matrices (of complex vectors), and the Grothendieck construction should yield the space of Hermitian matrices. In this equivalence, addition and multiplication correspond to elementwise addition and multiplication of these Gram matrices. (Note that, when going from collections of states to Gram matrices, direct sums turn into sums and tensor products turn into elementwise products).
	2. We represent mixed quantum theory using purifications: The analogue of the CPMs are pure quantum vectors including a subsystem representing the environment, and the equivalence relation we mod out over includes local operations on the environment.

## More details
### The set-up/CPMs
Suppose the learner has stored its previous (probabilistic) knowledge as a state of its internal memory $x\in X$. Consider the _conditional probability matrix_ (CPM) $C=(p(x\mid d))\_{x\in X,d\in D}\in\mathbb{R}^{X\times D}$. Then $C$ is sufficient (but, as we'll see, not necessary) to describe the "knowledge" the learner gathers about the environment for any $d\in D$. For example, if the learner's ultimate goal is to calculate some function $f\colon D\to R$, it does (and has to do) so by applying some probabilistic process $X\to R$, with some transition matrix $T=(p(r\mid x))\_{r\in R,x\in X}$. The appropriate matrix entries of $TC$ contain the probabilities $p(r=f(d)\mid d)$, the success probabilities of that procedure for given $d\in D$.

We formally _don't_ require that the conditional probabilities sum to $1$, but do require that they're nonnegative. If the conditional probabilities sum to $<1$ for some $d\in D$, we can interpret this as a learner that has given up on a problem by a certain time, with some probability.

### Preorder on transition matrices by transformability
On the set of CPMs, $\leq$ as discussed in the sketch is a _preorder_ - for any $C,C_1,C_2,C_3$, it fulfills
- transitivity: $C_1\leq C_2$ and $C_2\leq C_3$ implies $C_1\leq C_3$, and
- reflexivity: $C\leq C$.

### $\leq$ isn't a partial order yet
But $\leq$ is _not_ a partial order, as it does not fulfill symmetry: $C_1\leq C_2$ and $C_2\leq C_1$ does not necessarily imply $C_1=C_2$. Two counterexamples:
   - Permuting the rows of a conditional probability matrix $M$, corresponding to changing the labeling of $x\in X$,
   - Replacing some $x\in X$ with one of two additional states $x_1$, $x_2$ with probability $1/2$ each.

Intuitively, this means that, to describe the "state of knowledge" of the learner, the CPMs contain superfluous information. We can define an equivalence relation on the CPMS to capture this, with $C_1\sim C_2$ iff $C_1\leq C_2 \wedge C_2\leq C_1$. We **define our set of _states of knowledge (SOKs)_** $\mathbb{K}$ as a mathematical object as the set of equivalence classes under this equivalence relation. We will now argue that $K_1= K_2\in \mathbb{R}$ iff these "states of knowledge" should philosophically be considered equivalent:

It is clear that  $K_1=K_2$ implies they should be considered equivalent. Conversely, suppose that two CPMs $C_1,C_2$ should be considered equivalent. This means that, given $C_2$, the learner can solve all tasks it could solve when given $C_1$ and vice versa. In particular, it can emit a probability distribution corresponding to $C_1$. But this means that $C_1\leq C_2$. Similarly, $C_2\leq C_1$ as well, so $C_1$ and $C_2$ are in the same equivalence class.

By standard math, for $K_1, K_2\in \mathbb{K}$, $K_1\leq K_2$ is independent of the choice of representative, and $\leq$ is a partial order on $\mathbb{K}$.

### Convexity of states of knowledge
We define addition and scalar multiplication operations on states of knowledge as in step 4 of the sketch. We can easily verify they behave well with the equivalence relation.

A convex combination $p K_1+(1-p)K_2$ now corresponds to a SOK in which, before performing the experiments leading up to some state of knowledge, the learner had randomly decided to perform a procedure leading to $K_1$ with probability $p$, and a procedure leading to $K_2$ with probability $1-p$ (and stored the choice it made). So our definition of addition brings us one step closer to being able to use convex optimization to optimize over states of knowledge:
- When $K_1$ and $K_2$ are feasible in some scheme, their convex combinations are feasible as well,
- and when $K_1$ and $K_2$ are both individually acceptable for some task (i.e. yield a low enough achievable failure probability), their convex combinations are jointly acceptable as well (as one can achieve the appropriate convex mixtures of failure probabilities).

As mentioned in the introduction, if we just took convex combinations of our original CPMs, that wouldn't be true.

### The Grothendieck group
$(\mathbb{K},+)$ forms a commutative _monoid_: There is a neutral element $0\in \mathbb{K}$, represented by any all-$0$ matrix, and addition is associative and commutative. We can turn this into a group, i.e. add enough elements for there to be inverses, by a [_Grothendieck group construction_](https://en.wikipedia.org/w/index.php?title=Grothendieck_group&oldid=1091622036).[^26] This works as follows:

1. We are given a commutative monoid $(M,+)$,
2. We define the group by $M_\pm:=M\times M/\sim$, where $(m_1,m_2)\sim(m_3,m_4)$ iff $m_1+m_4=m_2+m_3$. In words, a tuple $(m_1,m_2)$ is to be interpreted as the group element $m_1-m_2$, and we can determine equivalence of two group elements $m_1-m_2, m_3-m_4$ by checking whether $m_1+m_4=m_3+m_2$.
3. We define $(m_1,m_2)+(m_3,m_4):=(m_1+m_3,m_2+m_4)$, and the inverse of an element $M$ represented by $(m_1,m_2)$ is denoted by $-M$ and represented by $(m_2,m_1)$.

For our monoid $(\mathbb{K},+)$, we call elements of the resulting set $\mathbb{K}_\pm$ _quasistates of knowledge_. The point of our exercise is that these form a vector space over $\mathbb{R}$, if we define scalar multiplication in the natural way ($\alpha (K_1,K_2):=(\alpha K_1, \alpha K_2)$ for $\alpha\geq 0$, and $\alpha K:=(-\alpha) (-K)$ for $\alpha<0$).[^27]

We can also define multiplication on $\mathbb{K}\_\pm$. Keeping in mind that $(K_1,K_2)$ is to be interpreted as $K_1-K_2$, our definition is $(K_1,K_2)(K_3,K_4):=(K_1K_3+K_2K_4,K_2K_3+K_1K_4)$. We arrive at a commutative $\mathbb{R}$-algebra $\mathbb{K}\_\pm$, with the "physical" SOKs $\mathbb{K}\subset\mathbb{K}\_\pm$ a convex subset of $\mathbb{K}\_\pm$. Finally, $(K_1,K_2)\leq(K_3,K_4)$ iff $K_1+K_4\leq K_3+K_2$. This turns our thing into an ordered group, which seems to behave well with standard laws of school arithmetic to me.

Any $\mathbb{R}$-algebra is an $\mathbb{R}$-vector space, but the dimension of the space will probably be infinite in general. Textbook convex optimization is done in Euclidean space (i.e. $\mathbb{R}^n$ with $n$ finite);[^17] we can truncate our space to a finite basis, and for a given finite set of possible experiments taking values in a finite set, we should be able to find a basis that covers any given finite number of observations. But I don't fully understand whether/to what extent the nice ideas of duality and similar would still work in our situation.

## Footnotes
[^2]: Point 10.2 of the sketch hints at mixed quantum states, but I don't want to swear that this works because I didn't check the details so far.
[^3]: Allowing transition probabilities that sum to less than 1 - i.e. allowing to lose probability mass - won't change the equivalence relation/classes, but is helpful for describing the output condition of a query algorithm later.
[^4]: We could have exchanged the order of steps $2$ and $3$.
[^5]: I.e. the vectors which are $1$ on $d$ resp. $d'\in D'$, and $0$ everywhere else.
[^6]: In the quantum case, this would correspond to Hadamard products of Gram matrices and tensor products of state collections.
[^17]: Apparently, [this Oberwolfach seminar](https://homepages.cwi.nl/~monique/ow-seminar-sdp/) contains a lecture on infinite-dimensional semidefinite optimization.
[^26]: I looked into Wikipedia to read that this has his name from a specific case "which resulted in the development of [K-theory](https://en.wikipedia.org/w/index.php?title=K-theory&oldid=1072713370)". What's written there looks formally quite similar to what I do here, though I don't understand it in detail. So maybe one can call these thoughts "K-theory on the space of probabilistic transformations?"
[^27]: To fulfill the vector space axiom that $\alpha X + \beta X=(\alpha+\beta)X$, we needed the modding out operation that took us from CPMs to SOKs.