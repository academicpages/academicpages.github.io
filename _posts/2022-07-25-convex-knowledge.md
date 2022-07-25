---
title: 'A learners possible states of knowledge as a convex subset of an \mathbb{R}-algebra via a Grothendieck construction'
date: 2022-07-25
permalink: /posts/2022/07/convex-knowledge/
tags:
  - cs.cc
  - cs.ml
  - quant-ph
---

A learner's possible states of knowledge as a convex subset of an $\mathbb{R}$-algebra via a Grothendieck construction
----

(Note: The next paragraph gives motivation from research on quantum query algorithms, but one shouldn't need to know anything about quantum physics or query algorithms to follow the rest of this post.)

A great thing about quantum physics and quantum query algorithms that allowed developments like [Barnum-Saks-Szegedy 2003](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.113.1101&rep=rep1&type=pdf) -- and arguably the [adversary bound - query algorithm duality](https://www.cs.umd.edu/~amchilds/qa/qa.pdf), in particular when developed like [here](https://github.com/qudent/RhoPaths) -- is that we have a _convex_ description of the current "state of knowledge" of a quantum query computer, namely the Gram matrix of the states for different inputs at a given time. This means that the Gram matrices
 - form a convex subset of a real vector space (for normed states, the complex positive semidefinite matrices with all-$1$ diagonal as a subset of the space of Hermitian matrices),
 - are necessary and sufficient to describe the quantum computer's state of knowledge,
 - if two Gram matrices are attainable by some procedures, their convex combinations are attainable as well, and
 - if two Gram matrices allow solving some problem (e.g. computing a function with a certain maximal error probability), their convex combinations allow solving that problem as well.

This allows using the powerful methods of [convex optimization and convex
duality](https://web.stanford.edu/~boyd/cvxbook/) (to be more precise, [semidefinite programming](https://en.wikipedia.org/w/index.php?title=Semidefinite_programming&oldid=1092453332)) to obtain lower bounds and query algorithms.

The aim of this note is to find such a description for classical agents/learners.[^2] In contrast to the classical case, our development doesn't give great bounds on the dimension of the vector space. The basic plan is as follows:
1. We start with a naive description of states of knowledge as collections/matrices of conditional probabilities $p(\mathrm{internal~memory~state}\mid\mathrm{environmental~ground~truth})\geq 0$; for now, we drop the requirement that the conditional probabilities sum to $1$ for any possible ground truth. We call these CPMs (conditional probability matrices); we consider all possible sets of internal memory states at once (i.e. don't fix the number of rows). Denote the set of possible ground truths by $D$.
2. For CPMs $C_1,C_2$, we write that $C_1\leq C_2$ iff the agent/learner can transform $C_2$ into $C_1$ by a probabilistic transformation without any interaction with the environment. Input and output dimensions are not necessarily equal, and transition probabilities must sum to **at most** $1$[^3]. Clearly, this means that $C_1$ corresponds to "at most as much knowledge" as $C_2$.
3. We say $C_1$ and $C_2$ are equivalent iff $C_1\leq C_2$ and $C_2\leq C_1$. We define the set of **states of knowledge** (SOK), $\mathbb{K}$, by modding out this equivalence relation from the set of CPMs. Mathematically, $\leq$ was a preorder on the CPMs and becomes a partial order on $\mathbb{K}$.
3. On $\mathbb{K}$, we define multiplication with a nonnegative scalar elementwise, and addition by a **direct sum** of the matrices making up the summands (i.e. taking a disjoint union of the internal memory states, and collecting the conditional probabilities). We check this behaves well with the equivalence relation. With these definitions, $\mathbb{K}$ is a convex set that conforms to the same intuitions as listed for Gram matrices above.[^4]
4. We also define multiplication of two collections by considering the learner to have access to uncorrelated information representing the factors: If the factors are represented by probability collections $p_1(a\mid D)$ and $p_2(b\mid D)$ for members of sets of internal memory states $a \in A$, $b \in B$, respectively, the product is represented by a CPMs with the Kronecker product $A\times B$ as internal memory state, and $p((a,b)\mid D)=p_1(a\in E)p_2(b\in D)$ for $(a,b)\in A\times B$. Besides behaving well with the equivalence relation, it's also commutative on the SOKs.[^6]

5. A vector of nonnegative numbers $\vec{p}\in\{\mathbb{R}^+\cup\{0\}\}^D$ is represented in $\mathbb{K}$ by a CPM with only one internal memory state. $0$, $1$ and $d\in D$, $D'\subseteq D$ are treated as the all-$0$, all-$1$, and indicator function vectors[^5] respectively. Then in the equivalence classes, $\mathbf{0},\mathbf{1}\in\mathbb{K}$ are neutral w.r.t. addition and multiplication, respectively; they correspond to a state of $0$ probability and a state of zero knowledge. We also define $\Omega\in\mathbb{K}$ as the state of complete knowledge.
6. For an example, suppose the learner is in a SOK $K\in\mathbb{K}$ and is to make some binary decision which of two experiments to perform next. When performed from scratch, these would generate results corresponding to states of knowledge $E_1$, $E_2$, respectively. Then the feasible states of knowledge after the next experiments are given by 

$\{E_1 K_1 + E_2 K_2 \mid K_1 + K_2 \leq K\}$

with $K_1,K_2\in\mathbb{K}$. Internal processing of $K$ corresponds to writing the decision into an additional register taking values in $\{1,2\}$ - the first thing is $K_1$, the second $K_2$. After the experiment, we independently get additional data for either decision, which corresponds to multiplying by $E_1$ and $E_2$, respectively.

Now suppose we have given $K\in\mathbb{K}$ and some utility function $f\colon D\times C\to\mathbb{R}^+ \cup \{0\}$. So the learner outputs some $c\in C$, and depending on the ground truth $d\in D$, it gets some utility $f(c,d)$. A special case is computing single- or multi-valued functions (the utility is $1$ if the chosen $c$ was acceptable for $d$, $0$ otherwise). $\vec{f(c,\cdot)}\in\mathbb{K}$ represents the utilities the learner would obtain if it always chooses $c$. Then the claim that the learner can obtain expected utilities $\vec{q}\in(\mathbb{R}^+\cup\{0\})^D$ corresponds to

$\vec{q}\leq \sum_{c\in C} K_c \vec{f(c,\cdot)}, \sum_{c\in C} K_c\leq K$.

In particular, function evaluation that should succeed with probability at least $1-\epsilon$ for all $d\in D$ corresponds to $\vec{q}=(1-\epsilon)\mathbf{1}$.

In terms of symbols, this looks completely analogous to the semidefinite program in Barnum-Saks-Szegedy, equations 9-13 [here](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.113.1101&rep=rep1&type=pdf).

7. Our $+$ and $0$ yield a commutative monoid, i.e. we can add and have a neutral element, but can't yet subtract. A [_Grothendieck group construction_](https://en.wikipedia.org/w/index.php?title=Grothendieck_group&oldid=1091622036)[^26] allows us to turn this monoid into a commutative group. We obtain an $\mathbb{R}$-algebra, which is also a vector space. Our original set of "physical" states of knowledge is still a convex subset of that vector space. So if we find or truncate to a finite basis, we can hopefully do convex optimization and duality over it.
8. $+$ and $*$ allows us to define formal power series of knowledge. For example, suppose our learner observes the stars with a telescope without making any choices. In an infinitesimal time $\Delta t\to 0$, it observes a supernova with probability $r \Delta t$, generating experimental data $A\in \mathbb{K}$. Otherwise, it observes nothing. If $K(t)$ is the state of knowledge over time, we obtain

$K(t+Delta t)\to ((1-r \Delta t)\mathbf{1}+r\Delta t A) K(t)=(\mathbf{1}+r\Delta t (A-\mathbf{1})) K(t)$.

This is solved by

$K(t)=\exp((A-\mathbf{1})rt) K(0)$,

which is to be interpreted as the appropriate formal infinite power series. In fact, writing

$K(t)=\exp(-rt)\exp(Art)K(0)=\sum^\infty_{k=0} \frac{\exp(-rt) r^k}{k!} A^k K(0)$

shows that the amount of knowledge obtained follows a Poisson distribution.

9. We discussed classical probability theory so far. But I think this works for both pure and mixed quantum theory as well, though I haven't thoroughly worked through the details and don't want to make a definite claim -- it would be really nice to get an adversary method for faulty query algorithms though:
	1. For pure quantum theory, the CPMs correspond to collections of wavefunctions for $d\in D$, and the $\subseteq$ operation corresponds to applying unitaries and projectors. Then the convex space _should_ be equivalent to the space of Gram matrices (of complex vectors), and the Grothendieck construction should yield the space of Hermitian matrices. In this equivalence, addition and multiplication correspond to elementwise addition and multiplication of these Gram matrices. (Note that, when going from collections of states to Gram matrices, direct sums turn into sums and tensor products turn into elementwise products).
	2. We represent mixed quantum theory using purifications: The analogue of the CPMs are pure quantum vectors including a subsystem representing the environment, and the equivalence relation includes modding out local operations on the environment.

## The set-up
TODO: I am sure there are more standard terminologies to describe the appropriate notions, what are they?

Consider a (for now, classical) environment described by a state $d\in D$. An agent (call it "learner", as it doesn't influence the environment) has previously performed some sorts of "experiments" on the environment and stored the (probabilistic) results as a state of its internal memory $x\in X$. The learner knows the basic "rules of physics" yielding a (rectangular) matrix of conditional probabilities $M=(p(x\mid d))_{x\in X,d\in D}\in\mathbb{R}^{X\times D}$, but doesn't a priori know $d$. $M$'s columns are probability vectors, i.e. vectors of nonnegative reals summing to $1$. I'll call such a matrix _transition matrix_.[^8]

$M$ is sufficient to describe the "knowledge" the learner gathers about the environment for any $d\in D$. For example, if the learner's ultimate goal is to calculate some function $f\colon D\to C$, it does (and has to do) so by applying some probabilistic process $X\to C$, with some other transition matrix $R=(p(c\mid c))_{c\in C,x\in X}$. Then the appropriate matrix entries of $RM$ contain the probabilities $\sum_{d\in D} p(c=f(d)\mid d)p(d)$ denotes the "success probability" of that procedure for a given $d\in D$.

## Preorder on transition matrices by transformability
We say $M'\leq M$ if $M'=AM$ for a transition matrix $A$ - in words, if the learner could obtain $M'$ from $M$ without any interaction with the environment, just by performing some operation on its internal memory. Of course, this means that the state of knowledge $M$ is "at least as good as" the state of knowledge $M'$.

On the set of CPMs, $\leq$ is a _preorder_ -- it fulfills
- transitivity: $M_1\leq M_2$ and $M_2\leq M_3$ implies $M_1\leq M_3$, and
- reflexivity: $M_1\leq M_1$.

## From transition matrices to states of knowledge by an equivalence relation.
But $\leq$ is _not_ a partial order, as it does not fulfill symmetry: $M_1\leq M_2$ and $M_2\leq M_1$ does not necessarily imply $M_1= M_2$. Two counterexamples:
  - Permuting the rows of a conditional probability matrix $M$, corresponding to changing the labeling of $x\in X$,
   - Reversing the operation of replacing some $x\in X$ with one of two additional states $x_1$, $x_2$ with probability $1/2$ each.

Intuitively, this means that, to describe the "state of knowledge" of the learner, $M$ contains superfluous information. We can confirm that the condition $M_1\leq M_2\wedge M_2\leq M_1$ is necessary and sufficient for the "states of knowledge" associated with two CPMs to be the same.

So we **define our _state of knowledge_** as a mathematical object by modding out this condition as an equivalence relation: We let $M_1\~M_2:\hArr M_1\leq M_2 \wedge M_2\leq M_1$, and define $K:=T/\~$, i.e. $K$ as the set of equivalence classes under this equivalence relation.

By standard math, for $K_1, K_2\in \mathbb{K}$, $K_1\leq K_2$ is independent of the choice of representative, and $\leq$ is a partial order on $\mathbb{K}$.

I claim that this "states of knowledge" definition is better-suited, in particular
## Adding and multiplying states of knowledge
We define addition and scalar multiplication operations on states of knowledge. We can easily verify they behave well with the equivalence relation.
- We define a representative of $K_1+K_2$ by taking a direct sum of the columns of representatives of $K_1$ and $K_2$.
- For $p\in \mathbb{R}^+\cup\{0\}$, we define a representative of $p K_1$ by multiplying the matrix entries by $p$.

A convex combination $p K_1+(1-p)K_2$ now corresponds to a SOK in which, before performing the experiments leading up to some state of knowledge, the learner had randomly decided to perform a procedure leading to $K_1$ with probability $p$, and a procedure leading to $K_2$ with probability $1-p$ (and stored the choice it made). So our definition of addition brings us one step closer to being able to use convex optimization to optimize over states of knowledge:
- When $K_1$ and $K_2$ are feasible in some scheme, their convex combinations are feasible as well,
- and when $K_1$ and $K_2$ are both individually acceptable for some task (i.e. yield a low enough achievable failure probability), their convex combinations are jointly acceptable as well (as one can achieve the appropriate convex mixtures of failure probabilities).

Note that if we just took convex combinations of our original CPMs, that wouldn't be true. For example, for $X=D$, each permutation matrix corresponds to maximal knowledge of the system, but randomly mixing these corresponds to a state of complete ignorance.

Finally, we define a notion of multiplying states of knowledge _with each other_ as well:

- $K_1K_2$ corresponds to the learner having stored the knowledge $K_1$ and $K_2$ in separate registers: We define a representative of $K_1K_2$ from representatives of $K_1, K_2$ by TODO

We can easily verify that this fulfills distributivity.
## The Grothendieck group
$(\mathbb{K},+)$ forms a commutative _monoid_: There is a neutral element $0\in \mathbb{K}$, represented by any all-$0$ matrix, and addition is associative and commutative. We can turn this into a group, i.e. add enough elements for there to be inverses, by a _Grothendieck group construction_(https://en.wikipedia.org/w/index.php?title=Grothendieck_group&oldid=1091622036).[^26]

- We are given a commutative monoid $(M,+)$,
- We define the group by $M_\pm:=M\times M/\langle(m_1,m_2)\~(m_3,m_4):\hArr m_1+m_4=m_2+m_3\rangle$. In words, a tuple $(m_1,m_2)$ is to be interpreted as the group element $m_1-m_2$, and we can determine equivalence of two group elements $m_1-m_2=m_3-m_4$ by checking $m_1+m_4=m_3+m_2$.
- We define $(m_1,m_2)+(m_3,m_4):=(m_1+m_3,m_2+m_4)$, and the inverse of an element $M$ represented by $(m_1,m_2)$ is denoted by $-M$ and represented by $(m_2,m_1)$.

For our monoid $(\mathbb{K},+)$, we call elements of the resulting set $\mathbb{K}_\pm$ _quasistates of knowledge_. The point of our exercise is that these form a real vector space, if we define scalar multiplication in the natural way ($\alpha (K_1,K_2):=(\alpha K_1, \alpha K_2)$ for $\alpha\geq 0$, and $\alpha K:=(-\alpha) (-K)$ for $\alpha<0$).

We can also define multiplication on $\mathbb{K}_\pm$. Keeping in mind that $(K_1,K_2)$ is to be interpreted as $K_1-K_2$, our definition is $(K_1,K_2)(K_3,K_4):=(K_1K_3+K_2K_4,K_2K_3+K_1K_4)$. We arrive at a commutative $\mathbb{R}$-algebra $\mathbb{K}_\pm$, with the "physical" SOKs $\mathbb{K}\subset\mathbb{K}_\pm$ a convex subset of $\mathbb{K}_\pm$.

Any $\mathbb{R}$-algebra is an $\mathbb{R}$-vector space, but the dimension of the space will probably be infinite in general. Textbook convex optimization is done in Euclidean space (i.e. $\mathbb{R}^n$ with $n$ finite);[^17] we can truncate our space to a finite basis, for a given finite set of possible experiments taking values in a finite set, we should be able to find a basis that covers any given finite number of observations. I don't understand whether/how the nice ideas of duality and similar would still work in our situation.

## Footnotes
[^2]: I also think that this would work for quantum agents with mixed states/faulty oracles, as hinted in section TODO, but I don't want to swear on it as I didn't work out the details so far.
[^3]: Allowing transition probabilities that sum to less than 1 - i.e. allowing to lose probability mass - won't change the equivalence relation/classes, but is helpful when denoting the output conditions later.
[^4]: We could have exchanged the order of steps $2$ and $3$.
[^5]: I.e. the vectors which are $1$ on $d$, $d'\in D\$, and $0$ everywhere else.
[^6]: In the quantum case, this would correspond to Hadamard products of Gram matrices and tensor products of state collections.
[^8]: Even though the literature usually requires these matrices to be square.
[^17]: Apparently, [this Oberwolfach seminar](https://homepages.cwi.nl/~monique/ow-seminar-sdp/) contains a lecture on infinite-dimensional semidefinite optimization.
[^26]: I looked into Wikipedia to read that this has his name from a specific case "which resulted in the development of [K theory](https://en.wikipedia.org/w/index.php?title=K-theory&oldid=1072713370)". What's written there looks formally quite similar to what I do here, though I don't understand it in detail. So maybe one can call these thoughts "K-theory on the space of probabilistic transformations?"
