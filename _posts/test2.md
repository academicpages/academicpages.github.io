---
Some notes on basic mathematical notions of differential privacy, Part 1 Equivalent notions of differential privacy
---

I have benefited greatly from this article. 
In fact, the purpose of this post is to add some explanations on parts of the article which are not clear to me.

This is Part 1 of a two-part post where I give an introduction to
the mathematics of differential privacy.

Practically speaking, [differential privacy](https://en.wikipedia.org/wiki/Differential_privacy) 
is a technique of perturbing database queries so that query results do not 
leak too much information while still being relatively accurate.

This post however focuses on the mathematical aspects of differential privacy, which is
a study of [tail bounds](https://en.wikipedia.org/wiki/Concentration_inequality)
of the divergence between
two probability measures, with the end goal of applying it to [stochastic
gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent).
This post should be suitable for anyone familiar with probability theory.

I start with the definition of $\epsilon$-differential privacy
(corresponding to max divergence), followed by
$(\epsilon, \delta)$-differential privacy (a.k.a. approximate
differential privacy, corresponding to the $\delta$-approximate max
divergence). I show a characterisation of the $(\epsilon, \delta)$-differential privacy
as conditioned $\epsilon$-differential privacy.
Also, as examples, I illustrate the $\epsilon$-dp with Laplace mechanism and, using
some common tail bounds, the approximate dp with the Gaussian mechanism.

Then I continue to show the effect of combinatorial
and sequential compositions of randomised queries (called mechanisms)
on privacy by stating and proving the composition theorems for differential privacy, 
as well as the effect of mixing mechanisms, by presenting the subsampling theorem
(a.k.a. amplification theorem).

In [Part 2](/posts/2019-03-14-great-but-manageable-expectations.html), I discuss the Rényi differential privacy, corresponding to
the Rényi divergence, a study of the [moment generating functions](https://en.wikipedia.org/wiki/Moment-generating_function) of the 
divergence between probability measures to derive the tail bounds. 

Like in Part 1, I prove a composition theorem and a subsampling theorem.

I also attempt to reproduce a seemingly better moment bound for the
Gaussian mechanism with subsampling, with one intermediate step which I
am not able to prove.

After that I explain the Tensorflow implementation of differential privacy
in its [Privacy](https://github.com/tensorflow/privacy/tree/master/privacy) module,
which focuses on the differentially private stochastic gradient descent 
algorithm (DP-SGD).

Finally I use the results from both Part 1 and Part 2 to obtain some privacy
guarantees for composed subsampling queries in general, and for DP-SGD in particular. 
I also compare these privacy guarantees.


The gist of differential privacy 
--------------------------------

If you only have one minute, here is what differential privacy is about:

Let $p$ and $q$ be two probability densities, we define the *divergence
variable*[^dv] of $(p, q)$ to be

$$L(p || q) := \log {p(\xi) \over q(\xi)}$$

where $\xi$ is a random variable distributed according to $p$.

Roughly speaking, differential privacy is the study of the tail bound of
$L(p || q)$: for certain $p$s and $q$s, and for
$\epsilon > 0$, find $\delta(\epsilon)$ such that

$$\mathbb P(L(p || q) > \epsilon) < \delta(\epsilon),$$

where $p$ and $q$ are the laws of the outputs of a randomised functions
on two very similar inputs.
Moreover, to make matters even simpler, only three situations need to be considered:

1.  (General case) $q$ is in the form of $q(y) = p(y + \Delta)$ for some bounded constant $\Delta$.
2.  (Compositions) $p$ and $q$ are combinatorial or sequential compositions of some simpler $p_i$'s and $q_i$'s respectively
3.  (Subsampling) $p$ and $q$ are mixtures / averages of some simpler $p_i$'s and $q_i$'s respectively

In applications, the inputs are databases and the randomised functions
are queries with an added noise, and the tail bounds give privacy
guarantees. When it comes to gradient descent, the input is the training
dataset, and the query updates the parameters, and privacy is achieved
by adding noise to the gradients.

Now if you have an hour\...

[^dv]: For those who have read about differential privacy and never heard 
of the term \"divergence variable\", it is closely related to the notion of \"privacy loss\",
see the paragraph under Claim 6 in [Back to approximate differential privacy](#back-to-approximate-differential-privacy).
I defined the term this way so that we can focus on the more general stuff: 
compared to the privacy loss $L(M(x) || M(x'))$, the term $L(p || q)$ removes 
the \"distracting information\" that $p$ and $q$ are related to databases, 
queries, mechanisms etc., but merely probability laws. By removing the distraction, 
we simplify the analysis. And once we are done with the analysis of $L(p || q)$, 
we can apply the results obtained in the general setting to the special case 
where $p$ is the law of $M(x)$ and $q$ is the law of $M(x')$.

$\epsilon$-dp 
-------------

**Definition (Mechanisms)**. Let $X$ be a
space with a metric $d: X \times X \to \mathbb N$. A *mechanism* $M$ is
a function that takes $x \in X$ as input and outputs a random variable
on $Y$.

In this post, $X = Z^m$ is the space of datasets of $m$ rows for some
integer $m$, where each item resides in some space $Z$. In this case the distance
$d(x, x') := \#\{i: x_i \neq x'_i\}$ is the number of rows that differ
between $x$ and $x'$.

Normally we have a query $f: X \to Y$, and construct the mechanism $M$
from $f$ by adding a noise:

$$M(x) := f(x) + \text{noise}.$$

Later, we will also consider mechanisms constructed from composition or mixture of
other mechanisms.

In this post $Y = \mathbb R^d$ for some $d$.

**Definition (Sensitivity)**. Let
$f: X \to \mathbb R^d$ be a function. The *sensitivity* $S_f$ of $f$ is
defined as

$$S_f := \sup_{x, x' \in X: d(x, x') = 1} \|f(x) - f(x')\|_2,$$

where $\|y\|_2 = \sqrt{y_1^2 + ... + y_d^2}$ is the $\ell^2$-norm.

**Definition (Differential
Privacy)**. A mechanism $M$ is called $\epsilon$*-differential privacy*
($\epsilon$-dp) if it satisfies the following condition: for all
$x, x' \in X$ with $d(x, x') = 1$, and for all measureable set
$S \subset \mathbb R^n$,

$$\mathbb P(M(x) \in S) \le e^\epsilon P(M(x') \in S). \qquad (1)$$

Practically speaking, this means given the results from perturbed query on
two known databases that differs by one row, it is hard to determine
which result is from which database.

An example of $\epsilon$-dp mechanism is the Laplace mechanism.

**Definition**. The *Laplace distribution* over $\mathbb R$
with parameter $b > 0$ has probability density function

$$f_{\text{Lap}(b)}(x) = {1 \over 2 b} e^{- {|x| \over b}}.$$

**Definition**. Let $d = 1$. The *Laplace mechanism* is
defined by

$$M(x) = f(x) + \text{Lap}(b).$$

**Claim**. The Laplace mechanism with

$$b \ge \epsilon^{-1} S_f \qquad (1.5)$$

is $\epsilon$-dp.

**Proof**. Quite straightforward. Let $p$ and $q$ be the laws
of $M(x)$ and $M(x')$ respectively.

$${p (y) \over q (y)} = {f_{\text{Lap}(b)} (y - f(x)) \over f_{\text{Lap}(b)} (y - f(x'))} = \exp(b^{-1} (|y - f(x')| - |y - f(x)|))$$

Using triangular inequality $|A| - |B| \le |A - B|$ on the right hand
side, we have

$${p (y) \over q (y)} \le \exp(b^{-1} (|f(x) - f(x')|)) \le \exp(\epsilon)$$

where in the last step we use the condition (1.5). $\square$

Approximate differential privacy 
--------------------------------

Unfortunately, $\epsilon$-dp does not apply to the most commonly used
noise, the Gaussian noise. To fix this, we need to relax the definition
a bit.

**Definition**. A mechanism $M$ is said to be
$(\epsilon, \delta)$*-differentially private* if for all $x, x' \in X$
with $d(x, x') = 1$ and for all measureable $S \subset \mathbb R^d$

$$\mathbb P(M(x) \in S) \le e^\epsilon P(M(x') \in S) + \delta. \qquad (2)$$

Immediately we see that the $(\epsilon, \delta)$-dp is meaningful only
if $\delta < 1$.

### Indistinguishability 

To understand $(\epsilon, \delta)$-dp, it is helpful to study
$(\epsilon, \delta)$-indistinguishability.

**Definition**. Two probability measures $p$ and $q$ on
the same space are called $(\epsilon, \delta)$*-ind(istinguishable)* if
for all measureable sets $S$:

$$\begin{aligned}
p(S) \le e^\epsilon q(S) + \delta, \qquad (3) \\
q(S) \le e^\epsilon p(S) + \delta. \qquad (4)
\end{aligned}$$

As before, we also call random variables $\xi$ and $\eta$ to be
$(\epsilon, \delta)$-ind if their laws are $(\epsilon, \delta)$-ind.
When $\delta = 0$, we call it $\epsilon$-ind.

Immediately we have

**Claim 0**. $M$ is $(\epsilon, \delta)$-dp (resp.
$\epsilon$-dp) iff $M(x)$ and $M(x')$ are $(\epsilon, \delta)$-ind
(resp. $\epsilon$-ind) for all $x$ and $x'$ with distance $1$.

**Definition (Divergence
Variable)**. Let $p$ and $q$ be two probability measures. Let $\xi$ be a
random variable distributed according to $p$, we define a random
variable $L(p || q)$ by

$$L(p || q) := \log {p(\xi) \over q(\xi)},$$

and call it the *divergence variable* of $(p, q)$.

One interesting and readily verifiable fact is

$$\mathbb E L(p || q) = D(p || q)$$

where $D$ is the [KL-divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence).

**Claim 1**. If

$$\begin{aligned}
\mathbb P(L(p || q) \le \epsilon) &\ge 1 - \delta, \qquad(5) \\
\mathbb P(L(q || p) \le \epsilon) &\ge 1 - \delta
\end{aligned}$$

then $p$ and $q$ are $(\epsilon, \delta)$-ind.

**Proof**. We verify (3), and (4) can be shown in the same
way. Let $A := \{y \in Y: \log {p(y) \over q(y)} > \epsilon\}$, then by
(5) we have

$$p(A) < \delta.$$

So

$$p(S) = p(S \cap A) + p(S \setminus A) \le \delta + e^\epsilon q(S \setminus A) \le \delta + e^\epsilon q(S).$$

$\square$

This Claim translates differential privacy to the tail bound of
divergence variables, and for the rest of this post all dp results are
obtained by estimating this tail bound.

In the following we discuss the converse of Claim 1. The discussions are
rather technical, and readers can skip to the [next subsection](#back-to-approximate-differential-privacy) on first
reading.

The converse of Claim 1 is not true.

**Claim 2**. There exists $\epsilon, \delta > 0$, and $p$
and $q$ that are $(\epsilon, \delta)$-ind, such that

$$\begin{aligned}
\mathbb P(L(p || q) \le \epsilon) &< 1 - \delta, \\
\mathbb P(L(q || p) \le \epsilon) &< 1 - \delta
\end{aligned}$$

**Proof**. Here\'s a example. Let $Y = \{0, 1\}$, and
$p(0) = q(1) = 2 / 5$ and $p(1) = q(0) = 3 / 5$. Then it is not hard to
verify that $p$ and $q$ are $(\log {4 \over 3}, {1 \over 3})$-ind: just
check (3) for all four possible $S \subset Y$ and (4) holds by symmetry.
On the other hand,

$$\mathbb P(L(p || q) \le \log {4 \over 3}) = \mathbb P(L(q || p) \le \log {4 \over 3}) = {2 \over 5} < {2 \over 3}.$$

$\square$

A weaker version of the converse of Claim 1 is true
(Kasiviswanathan-Smith 2015), though:

**Claim 3**. Let $\alpha > 1$. If $p$ and $q$ are
$(\epsilon, \delta)$-ind, then

$$\mathbb P(L(p || q) > \alpha \epsilon) < {1 \over 1 - \exp((1 - \alpha) \epsilon)} \delta.$$

**Proof**. Define

$$S = \{y: p(y) > e^{\alpha \epsilon} q(y)\}.$$

Then we have

$$e^{\alpha \epsilon} q(S) < p(S) \le e^\epsilon q(S) + \delta,$$

where the first inequality is due to the definition of $S$, and the
second due to the $(\epsilon, \delta)$-ind. Therefore

$$q(S) \le {\delta \over e^{\alpha \epsilon} - e^\epsilon}.$$

Using the $(\epsilon, \delta)$-ind again we have

$$p(S) \le e^\epsilon q(S) + \delta = {1 \over 1 - e^{(1 - \alpha) \epsilon}} \delta.$$

$\square$

This can be quite bad if $\epsilon$ is small.

To prove the composition theorems in the next section, we need a
condition better than that in Claim 1 so that we can go back and forth
between indistinguishability and such condition. In other words, we need
a *characterisation* of indistinguishability.

Let us take a careful look at the condition in Claim 1 and call it
**C1**:

**C1**. $\mathbb P(L(p || q) \le \epsilon) \ge 1 - \delta$ and
$\mathbb P(L(q || p) \le \epsilon) \ge 1 - \delta$

It is equivalent to

**C2**. there exist events $A, B \subset Y$ with probabilities
$p(A)$ and $q(B)$ at least $1 - \delta$ such that
$\log p(y) - \log q(y) \le \epsilon$ for all $y \in A$ and
$\log q(y) - \log p(y) \le \epsilon$ for all $y \in B$.

A similar-looking condition to **C2** is the following:

**C3**. Let $\Omega$ be the [underlying probability
space](https://en.wikipedia.org/wiki/Probability_space#Definition).
There exist two events $E, F \subset \Omega$ with
$\mathbb P(E), \mathbb P(F) \ge 1 - \delta$, such that
$|\log p_{|E}(y) - \log q_{|F}(y)| \le \epsilon$ for all $y \in Y$.

Here $p_{|E}$ (resp. $q_{|F}$) is $p$ (resp. $q$) conditioned on event
$E$ (resp. $F$).

**Remark**. Note that the events in **C2** and
**C3** are in different spaces, and therefore we can not write
$p_{|E}(S)$ as $p(S | E)$ or $q_{|F}(S)$ as $q(S | F)$. In fact, if we
let $E$ and $F$ in **C3** be subsets of $Y$ with
$p(E), q(F) \ge 1 - \delta$ and assume $p$ and $q$ have the same
supports, then **C3** degenerates to a stronger condition than
**C2**. Indeed, in this case $p_E(y) = p(y) 1_{y \in E}$ and
$q_F(y) = q(y) 1_{y \in F}$, and so $p_E(y) \le e^\epsilon q_F(y)$
forces $E \subset F$. We also obtain $F \subset E$ in the same way. This
gives us $E = F$, and **C3** becomes **C2** with
$A = B = E = F$.

As it turns out, **C3** is the condition we need.

**Claim 4**. Two probability measures $p$ and $q$ are
$(\epsilon, \delta)$-ind if and only if **C3** holds.

**Proof**(Murtagh-Vadhan 2018). The \"if\" direction is proved
in the same way as Claim 1. Without loss of generality we may assume
$\mathbb P(E) = \mathbb P(F) \ge 1 - \delta$. To see this, suppose $F$
has higher probability than $E$, then we can substitute $F$ with a
subset of $F$ that has the same probability as $E$ (with possible
enlargement of the probability space).

Let $\xi \sim p$ and $\eta \sim q$ be two independent random variables,
then

$$\begin{aligned}
p(S) &= \mathbb P(\xi \in S | E) \mathbb P(E) + \mathbb P(\xi \in S; E^c) \\
&\le e^\epsilon \mathbb P(\eta \in S | F) \mathbb P(E) + \delta \\
&= e^\epsilon \mathbb P(\eta \in S | F) \mathbb P(F) + \delta\\
&\le e^\epsilon q(S) + \delta.
\end{aligned}$$

The \"only-if\" direction is more involved.

We construct events $E$ and $F$ by constructing functions
$e, f: Y \to [0, \infty)$ satisfying the following conditions:

1.  $0 \le e(y) \le p(y)$ and $0 \le f(y) \le q(y)$ for all $y \in Y$.
2.  $|\log e(y) - \log f(y)| \le \epsilon$ for all $y \in Y$.
3.  $e(Y), f(Y) \ge 1 - \delta$.
4.  $e(Y) = f(Y)$.

Here for a set $S \subset Y$, $e(S) := \int_S e(y) dy$, and the same
goes for $f(S)$.

Let $\xi \sim p$ and $\eta \sim q$. Then we define $E$ and $F$ by

$$\mathbb P(E | \xi = y) = e(y) / p(y) \\
\mathbb P(F | \eta = y) = f(y) / q(y).$$

**Remark inside proof**. This can seem a bit
confusing. Intuitively, we can think of it this way when $Y$ is finite:
Recall a random variable on $Y$ is a function from the probability space
$\Omega$ to $Y$. Let event $G_y \subset \Omega$ be defined as
$G_y = \xi^{-1} (y)$. We cut $G_y$ into the disjoint union of $E_y$ and
$G_y \setminus E_y$ such that $\mathbb P(E_y) = e(y)$. Then
$E = \bigcup_{y \in Y} E_y$. So $e(y)$ can be seen as the \"density\" of
$E$.

Indeed, given $E$ and $F$ defined this way, we have

$$p_E(y) = {e(y) \over e(Y)} \le {\exp(\epsilon) f(y) \over e(Y)} = {\exp(\epsilon) f(y) \over f(Y)} = \exp(\epsilon) q_F(y).$$

and

$$\mathbb P(E) = \int \mathbb P(E | \xi = y) p(y) dy = e(Y) \ge 1 - \delta,$$

and the same goes for $\mathbb P(F)$.

What remains is to construct $e(y)$ and $f(y)$ satisfying the four
conditions.

Like in the proof of Claim 1, let $S, T \subset Y$ be defined as

$$\begin{aligned}
S := \{y: p(y) > \exp(\epsilon) q(y)\},\\
T := \{y: q(y) > \exp(\epsilon) p(y)\}.
\end{aligned}$$

Let

$$\begin{aligned}
e(y) &:= \exp(\epsilon) q(y) 1_{y \in S} + p(y) 1_{y \notin S}\\
f(y) &:= \exp(\epsilon) p(y) 1_{y \in T} + q(y) 1_{y \notin T}. \qquad (6)
\end{aligned}$$

By checking them on the three disjoint subsets $S$, $T$, $(S \cup T)^c$,
it is not hard to verify that the $e(y)$ and $f(y)$ constructed this way
satisfy the first two conditions. They also satisfy the third condition:

$$\begin{aligned}
e(Y) &= 1 - (p(S) - \exp(\epsilon) q(S)) \ge 1 - \delta, \\
f(Y) &= 1 - (q(T) - \exp(\epsilon) p(T)) \ge 1 - \delta.
\end{aligned}$$

If $e(Y) = f(Y)$ then we are done. Otherwise, without loss of
generality, assume $e(Y) < f(Y)$, then all it remains to do is to reduce
the value of $f(y)$ while preserving Condition 1, 2 and 3, until
$f(Y) = e(Y)$.

As it turns out, this can be achieved by reducing $f(y)$ on the set
$\{y \in Y: q(y) > p(y)\}$. To see this, let us rename the $f(y)$
defined in (6) $f_+(y)$, and construct $f_-(y)$ by

$$f_-(y) := p(y) 1_{y \in T} + (q(y) \wedge p(y)) 1_{y \notin T}.$$

It is not hard to show that not only $e(y)$ and $f_-(y)$ also satisfy
conditions 1-3, but

$$e(y) \ge f_-(y), \forall y \in Y,$$

and thus $e(Y) \ge f_-(Y)$. Therefore there exists an $f$ that
interpolates between $f_-$ and $f_+$ with $f(Y) = e(Y)$. $\square$

To prove the adaptive composition theorem for approximate differential
privacy, we need a similar claim (We use index shorthand
$\xi_{< i} = \xi_{1 : i - 1}$ and similarly for other notations):

**Claim 5**. Let $\xi_{1 : i}$ and $\eta_{1 : i}$ be random
variables. Let

$$\begin{aligned}
p_i(S | y_{1 : i - 1}) := \mathbb P(\xi_i \in S | \xi_{1 : i - 1} = y_{1 : i - 1})\\
q_i(S | y_{1 : i - 1}) := \mathbb P(\eta_i \in S | \eta_{1 : i - 1} = y_{1 : i - 1})
\end{aligned}$$

be the conditional laws of $\xi_i | \xi_{< i}$ and $\eta_i | \eta_{< i}$
respectively. Then the following are equivalent:

1.  For any $y_{< i} \in Y^{i - 1}$, $p_i(\cdot | y_{< i})$ and
    $q_i(\cdot | y_{< i})$ are $(\epsilon, \delta)$-ind
2.  There exists events $E_i, F_i \subset \Omega$ with
    $\mathbb P(E_i | \xi_{<i} = y_{<i}) = \mathbb P(F_i | \eta_{<i} = y_{< i}) \ge 1 - \delta$
    for any $y_{< i}$, such that $p_{i | E_i}(\cdot | y_{< i})$ and
    $q_{i | E_i} (\cdot | y_{< i})$ are $\epsilon$-ind for any
    $y_{< i}$, where
    $$\begin{aligned}
    p_{i | E_i}(S | y_{1 : i - 1}) := \mathbb P(\xi_i \in S | E_i, \xi_{1 : i - 1} = y_{1 : i - 1})\\
        q_{i | F_i}(S | y_{1 : i - 1}) := \mathbb P(\eta_i \in S | F_i, \eta_{1 : i - 1} = y_{1 : i - 1})
    \end{aligned}$$

    are $p_i$ and $q_i$ conditioned on $E_i$ and $F_i$ respectively.

**Proof**. Item 2 =\> Item 1: as in the Proof of Claim 4,

$$\begin{aligned}
p_i(S | y_{< i}) &= p_{i | E_i} (S | y_{< i}) \mathbb P(E_i | \xi_{< i} = y_{< i}) + p_{i | E_i^c}(S | y_{< i}) \mathbb P(E_i^c | \xi_{< i} = y_{< i}) \\
&\le p_{i | E_i} (S | y_{< i}) \mathbb P(E_i | \xi_{< i} = y_{< i}) + \delta \\
&= p_{i | E_i} (S | y_{< i}) \mathbb P(F_i | \xi_{< i} = y_{< i}) + \delta \\
&\le e^\epsilon q_{i | F_i} (S | y_{< i}) \mathbb P(F_i | \xi_{< i} = y_{< i}) + \delta \\
&= e^\epsilon q_i (S | y_{< i}) + \delta.
\end{aligned}$$

The direction from
$q_i(S | y_{< i}) \le e^\epsilon p_i(S | y_{< i}) + \delta$ can be shown
in the same way.

Item 1 =\> Item 2: as in the Proof of Claim 4 we construct
$e(y_{1 : i})$ and $f(y_{1 : i})$ as \"densities\" of events $E_i$ and
$F_i$.

Let

$$\begin{aligned}
e(y_{1 : i}) &:= e^\epsilon q_i(y_i | y_{< i}) 1_{y_i \in S_i(y_{< i})} + p_i(y_i | y_{< i}) 1_{y_i \notin S_i(y_{< i})}\\
f(y_{1 : i}) &:= e^\epsilon p_i(y_i | y_{< i}) 1_{y_i \in T_i(y_{< i})} + q_i(y_i | y_{< i}) 1_{y_i \notin T_i(y_{< i})}\\
\end{aligned}$$

where

$$\begin{aligned}
S_i(y_{< i}) = \{y_i \in Y: p_i(y_i | y_{< i}) > e^\epsilon q_i(y_i | y_{< i})\}\\
T_i(y_{< i}) = \{y_i \in Y: q_i(y_i | y_{< i}) > e^\epsilon p_i(y_i | y_{< i})\}.
\end{aligned}$$

Then $E_i$ and $F_i$ are defined as

$$\begin{aligned}
\mathbb P(E_i | \xi_{\le i} = y_{\le i}) &= {e(y_{\le i}) \over p_i(y_{\le i})},\\
\mathbb P(F_i | \xi_{\le i} = y_{\le i}) &= {f(y_{\le i}) \over q_i(y_{\le i})}.
\end{aligned}$$

The rest of the proof is almost the same as the proof of Claim 4.
$\square$

### Back to approximate differential privacy 

By Claim 0 and 1 we have

**Claim 6**. If for all $x, x' \in X$ with distance $1$

$$\mathbb P(L(M(x) || M(x')) \le \epsilon) \ge 1 - \delta,$$

then $M$ is $(\epsilon, \delta)$-dp.

Note that in the literature the divergence variable $L(M(x) || M(x'))$
is also called the *privacy loss*.

By Claim 0 and Claim 4 we have

**Claim 7**. $M$ is $(\epsilon, \delta)$-dp if and only if
for every $x, x' \in X$ with distance $1$, there exist events
$E, F \subset \Omega$ with $\mathbb P(E) = \mathbb P(F) \ge 1 - \delta$,
$M(x) | E$ and $M(x') | F$ are $\epsilon$-ind.

We can further simplify the privacy loss $L(M(x) || M(x'))$, by
observing the translational and scaling invariance of $L(\cdot||\cdot)$:

$$\begin{aligned}
L(\xi || \eta) &\overset{d}{=} L(\alpha \xi + \beta || \alpha \eta + \beta), \qquad \alpha \neq 0. \qquad (6.1)
\end{aligned}$$

With this and the definition

$$M(x) = f(x) + \zeta$$

for some random variable $\zeta$, we have

$$L(M(x) || M(x')) \overset{d}{=} L(\zeta || \zeta + f(x') - f(x)).$$

Without loss of generality, we can consider $f$ with sensitivity $1$,
for

$$L(f(x) + S_f \zeta || f(x') + S_f \zeta) \overset{d}{=} L(S_f^{-1} f(x) + \zeta || S_f^{-1} f(x') + \zeta)$$

so for any noise $\zeta$ that achieves $(\epsilon, \delta)$-dp for a
function with sensitivity $1$, we have the same privacy guarantee by for
an arbitrary function with sensitivity $S_f$ by adding a noise
$S_f \zeta$.

With Claim 6 we can show that the Gaussian mechanism is approximately
differentially private. But first we need to define it.

**Definition (Gaussian mechanism)**.
Given a query $f: X \to Y$, the *Gaussian mechanism* $M$ adds a Gaussian
noise to the query:

$$M(x) = f(x) + N(0, \sigma^2 I).$$

Some tail bounds for the Gaussian distribution will be useful.

**Claim 8 (Gaussian tail bounds)**.
Let $\xi \sim N(0, 1)$ be a standard normal distribution. Then for
$t > 0$

$$\mathbb P(\xi > t) < {1 \over \sqrt{2 \pi} t} e^{- {t^2 \over 2}}, \qquad (6.3)$$

and

$$\mathbb P(\xi > t) < e^{- {t^2 \over 2}}. \qquad (6.5)$$

**Proof**. Both bounds are well known. The first can be proved
using

$$\int_t^\infty e^{- {y^2 \over 2}} dy < \int_t^\infty {y \over t} e^{- {y^2 \over 2}} dy.$$

The second is shown using [Chernoff bound](https://en.wikipedia.org/wiki/Chernoff_bound). For any random variable $\xi$,

$$\mathbb P(\xi > t) < {\mathbb E \exp(\lambda \xi) \over \exp(\lambda t)} = \exp(\kappa_\xi(\lambda) - \lambda t), \qquad (6.7)$$

where $\kappa_\xi(\lambda) = \log \mathbb E \exp(\lambda \xi)$ is the
cumulant of $\xi$. Since (6.7) holds for any $\lambda$, we can get the
best bound by minimising $\kappa_\xi(\lambda) - \lambda t$ (a.k.a. the
[Legendre transformation](https://en.wikipedia.org/wiki/Legendre_transformation)). When $\xi$ is standard normal, we get (6.5).
$\square$

**Remark**. We will use the Chernoff bound extensively in the
second part of this post when considering Rényi differential privacy.

**Claim 9**. The Gaussian mechanism on a query $f$ is
$(\epsilon, \delta)$-dp, where

$$\delta = \exp(- (\epsilon \sigma / S_f - (2 \sigma / S_f)^{-1})^2 / 2). \qquad (6.8)$$

Conversely, to achieve give $(\epsilon, \delta)$-dp, we may set

$$\sigma > \left(\epsilon^{-1} \sqrt{2 \log \delta^{-1}} + (2 \epsilon)^{- {1 \over 2}}\right) S_f \qquad (6.81)$$

or

$$\sigma > (\epsilon^{-1} (1 \vee \sqrt{(\log (2 \pi)^{-1} \delta^{-2})_+}) + (2 \epsilon)^{- {1 \over 2}}) S_f \qquad (6.82)$$

or

$$\sigma > \epsilon^{-1} \sqrt{\log e^\epsilon \delta^{-2}} S_f \qquad (6.83)$$

or

$$\sigma > \epsilon^{-1} (\sqrt{1 + \epsilon} \vee \sqrt{(\log e^\epsilon (2 \pi)^{-1} \delta^{-2})_+}) S_f. \qquad (6.84)$$

**Proof**. As discussed before we only need to consider the
case where $S_f = 1$. Fix arbitrary $x, x' \in X$ with $d(x, x') = 1$.
Let $\zeta = (\zeta_1, ..., \zeta_d) \sim N(0, I_d)$.

By Claim 6 it suffices to bound

$$\mathbb P(L(M(x) || M(x')) > \epsilon)$$

We have by the linear invariance of $L$,

$$L(M(x) || M(x')) = L(f(x) + \sigma \zeta || f(x') + \sigma \zeta) \overset{d}{=} L(\zeta|| \zeta + \Delta / \sigma),$$

where $\Delta := f(x') - f(x)$.

Plugging in the Gaussian density, we have

$$L(M(x) || M(x')) \overset{d}{=} \sum_i {\Delta_i \over \sigma} \zeta_i + \sum_i {\Delta_i^2 \over 2 \sigma^2} \overset{d}{=} {\|\Delta\|_2 \over \sigma} \xi + {\|\Delta\|_2^2 \over 2 \sigma^2}.$$

where $\xi \sim N(0, 1)$.

Hence

$$\mathbb P(L(M(x) || M(x')) > \epsilon) = \mathbb P(\zeta > {\sigma \over \|\Delta\|_2} \epsilon - {\|\Delta\|_2 \over 2 \sigma}).$$

Since $\|\Delta\|_2 \le S_f = 1$, we have

$$\mathbb P(L(M(x) || M(x')) > \epsilon) \le \mathbb P(\xi > \sigma \epsilon - (2 \sigma)^{-1}).$$

Thus the problem is reduced to the tail bound of a standard normal
distribution, so we can use Claim 8. Note that we implicitly require
$\sigma > (2 \epsilon)^{- 1 / 2}$ here so that
$\sigma \epsilon - (2 \sigma)^{-1} > 0$ and we can use the tail bounds.

Using (6.3) we have

$$\mathbb P(L(M(x) || M(x')) > \epsilon) < \exp(- (\epsilon \sigma - (2 \sigma)^{-1})^2 / 2).$$

This gives us (6.8).

To bound the right hand by $\delta$, we require

$$\epsilon \sigma - {1 \over 2 \sigma} > \sqrt{2 \log \delta^{-1}}. \qquad (6.91)$$

Solving this inequality we have

$$\sigma > {\sqrt{2 \log \delta^{-1}} + \sqrt{2 \log \delta^{-1} + 2 \epsilon} \over 2 \epsilon}.$$

Using
$\sqrt{2 \log \delta^{-1} + 2 \epsilon} \le \sqrt{2 \log \delta^{-1}} + \sqrt{2 \epsilon}$,
we can achieve the above inequality by having

$$\sigma > \epsilon^{-1} \sqrt{2 \log \delta^{-1}} + (2 \epsilon)^{-{1 \over 2}}.$$

This gives us (6.81).

Alternatively, we can use the concavity of $\sqrt{\cdot}$:

$$(2 \epsilon)^{-1} (\sqrt{2 \log \delta^{-1}} + \sqrt{2 \log \delta^{-1} + 2 \epsilon}) \le \epsilon^{-1} \sqrt{\log e^\epsilon \delta^{-2}},$$

which gives us (6.83)

Back to (6.9), if we use (6.5) instead, we need

$$\log t + {t^2 \over 2} > \log {(2 \pi)^{- 1 / 2} \delta^{-1}}$$

where $t = \epsilon \sigma - (2 \sigma)^{-1}$. This can be satisfied if

$$\begin{aligned}
t &> 1 \qquad (6.93)\\
t &> \sqrt{\log (2 \pi)^{-1} \delta^{-2}}. \qquad (6.95)
\end{aligned}$$

We can solve both inequalities as before and obtain

$$\sigma > \epsilon^{-1} (1 \vee \sqrt{(\log (2 \pi)^{-1} \delta^{-2})_+}) + (2 \epsilon)^{- {1 \over 2}},$$

or

$$\sigma > \epsilon^{-1}(\sqrt{1 + \epsilon} \vee \sqrt{(\log e^\epsilon (2 \pi)^{-1} \delta^{-2})_+}).$$

This gives us (6.82)(6.84). $\square$

When $\epsilon \le \alpha$ is bounded, by (6.83) (6.84) we can require
either

$$\sigma > \epsilon^{-1} (\sqrt{\log e^\alpha \delta^{-2}}) S_f$$

or

$$\sigma > \epsilon^{-1} (\sqrt{1 + \alpha} \vee \sqrt{(\log (2 \pi)^{-1} e^\alpha \delta^{-2})_+}) S_f.$$

The second bound is similar to and slightly better than the one in
Theorem A.1 of Dwork-Roth 2013, where $\alpha = 1$:

$$\sigma > \epsilon^{-1} \left({3 \over 2} \vee \sqrt{(2 \log {5 \over 4} \delta^{-1})_+}\right) S_f.$$

Note that the lower bound of ${3 \over 2}$ is implicitly required in the
proof of Theorem A.1.

Composition theorems 
--------------------

So far we have seen how a mechanism made of a single query plus a noise
can be proved to be differentially private. But we need to understand
the privacy when composing several mechanisms, combinatorially or
sequentially. Let us first define the combinatorial case:

**Definition (Independent
composition)**. Let $M_1, ..., M_k$ be $k$ mechanisms with independent
noises. The mechanism $M = (M_1, ..., M_k)$ is called the *independent
composition* of $M_{1 : k}$.

To define the adaptive composition, let us motivate it with an example
of gradient descent. Consider the loss function $\ell(x; \theta)$ of a neural network,
where $\theta$ is the parameter and $x$ the input, gradient descent updates
its parameter $\theta$ at each time $t$:

$$\theta_{t} = \theta_{t - 1} - \alpha m^{-1} \sum_{i = 1 : m} \nabla_\theta \ell(x_i; \theta) |_{\theta = \theta_{t - 1}}.$$

We may add privacy by adding noise $\zeta_t$ at each step:

$$\theta_{t} = \theta_{t - 1} - \alpha m^{-1} \sum_{i = 1 : m} \nabla_\theta \ell(x_i; \theta) |_{\theta = \theta_{t - 1}} + \zeta_t. \qquad (6.97)$$

Viewed as a sequence of mechanism, we have that at each time $t$, the
mechanism $M_t$ takes input $x$, and outputs $\theta_t$. But $M_t$ also
depends on the output of the previous mechanism $M_{t - 1}$. To this
end, we define the adaptive composition.

**Definition (Adaptive
composition)**. Let $({M_i(y_{1 : i - 1})})_{i = 1 : k}$ be $k$
mechanisms with independent noises, where $M_1$ has no parameter, $M_2$
has one parameter in $Y$, $M_3$ has two parameters in $Y$ and so on. For
$x \in X$, define $\xi_i$ recursively by

$$\begin{aligned}
\xi_1 &:= M_1(x)\\
\xi_i &:= M_i(\xi_1, \xi_2, ..., \xi_{i - 1}) (x).
\end{aligned}$$

The *adaptive composition* of $M_{1 : k}$ is defined by
$M(x) := (\xi_1, \xi_2, ..., \xi_k)$.

The definition of adaptive composition may look a bit complicated, but
the point is to describe $k$ mechanisms such that for each $i$, the
output of the first, second, \..., $i - 1$th mechanisms determine the
$i$th mechanism, like in the case of gradient descent.

It is not hard to write down the differentially private gradient descent
as a sequential composition:

$$M_t(\theta_{1 : t - 1})(x) = \theta_{t - 1} - \alpha m^{-1} \sum_{i = 1 : m} \nabla_\theta \ell(x_i; \theta) |_{\theta = \theta_{t - 1}} + \zeta_t.$$

In Dwork-Rothblum-Vadhan 2010 (see also Dwork-Roth 2013) the adaptive
composition is defined in a more general way, but the definition is
based on the same principle, and proofs in this post on adaptive
compositions carry over.

It is not hard to see that the adaptive composition degenerates to
independent composition when each $M_i(y_{1 : i})$ evaluates to the same
mechanism regardless of $y_{1 : i}$, in which case the $\xi_i$s are
independent.

In the following when discussing adaptive compositions we sometimes omit
the parameters for convenience without risk of ambiguity, and write
$M_i(y_{1 : i})$ as $M_i$, but keep in mind of the dependence on the
parameters.

It is time to state and prove the composition theorems. In this section
we consider $2 \times 2 \times 2 = 8$ cases, i.e. situations of three
dimensions, where there are two choices in each dimension:

1.  Composition of $\epsilon$-dp or more generally
    $(\epsilon, \delta)$-dp mechanisms
2.  Composition of independent or more generally adaptive mechanisms
3.  Basic or advanced compositions

Note that in the first two dimensions the second choice is more general
than the first.

The proofs of these composition theorems will be laid out as follows:

1.  Claim 10 - Basic composition theorem for $(\epsilon, \delta)$-dp
    with adaptive mechanisms: by a direct proof with an induction
    argument
2.  Claim 14 - Advanced composition theorem for $\epsilon$-dp with
    independent mechanisms: by factorising privacy loss and using
    [Hoeffding\'s Inequality](https://en.wikipedia.org/wiki/Hoeffding%27s_inequality)
3.  Claim 16 - Advanced composition theorem for $\epsilon$-dp with
    adaptive mechanisms: by factorising privacy loss and using 
    [Azuma\'s Inequality](https://en.wikipedia.org/wiki/Azuma%27s_inequality)
4.  Claims 17 and 18 - Advanced composition theorem for
    $(\epsilon, \delta)$-dp with independent / adaptive mechanisms: by
    using characterisations of $(\epsilon, \delta)$-dp in Claims 4 and 5
    as an approximation of $\epsilon$-dp and then using Proofs in Item 2
    or 3.

**Claim 10 (Basic composition
theorem).** Let $M_{1 : k}$ be $k$ mechanisms with independent noises
such that for each $i$ and $y_{1 : i - 1}$, $M_i(y_{1 : i - 1})$ is
$(\epsilon_i, \delta_i)$-dp. Then the adpative composition of
$M_{1 : k}$ is $(\sum_i \epsilon_i, \sum_i \delta_i)$-dp.

**Proof
(Dwork-Lei 2009, see also Dwork-Roth 2013 Appendix B.1)**. Let $x$ and
$x'$ be neighbouring points in $X$. Let $M$ be the adaptive composition
of $M_{1 : k}$. Define

$$\xi_{1 : k} := M(x), \qquad \eta_{1 : k} := M(x').$$

Let $p^i$ and $q^i$ be the laws of $(\xi_{1 : i})$ and $(\eta_{1 : i})$
respectively.

Let $S_1, ..., S_k \subset Y$ and $T_i := \prod_{j = 1 : i} S_j$. We use
two tricks.

1.  Since $\xi_i | \xi_{< i} = y_{< i}$ and
    $\eta_i | \eta_{< i} = y_{< i}$ are $(\epsilon_i, \delta_i)$-ind,
    and a probability is no greater than $1$,
    $$\begin{aligned}
    \mathbb P(\xi_i \in S_i | \xi_{< i} = y_{< i}) &\le (e^{\epsilon_i} \mathbb P(\eta_i \in S_i | \eta_{< i} = y_{< i}) + \delta_i) \wedge 1 \\
        &\le (e^{\epsilon_i} \mathbb P(\eta_i \in S_i | \eta_{< i} = y_{< i}) + \delta_i) \wedge (1 + \delta_i) \\
        &= (e^{\epsilon_i} \mathbb P(\eta_i \in S_i | \eta_{< i} = y_{< i})  \wedge 1) + \delta_i
    \end{aligned}$$

2.  Given $p$ and $q$ that are $(\epsilon, \delta)$-ind, define
    $$\mu(x) = (p(x) - e^\epsilon q(x))_+.$$

    We have
    $$\mu(S) \le \delta, \forall S$$

    In the following we define
    $\mu^{i - 1} = (p^{i - 1} - e^\epsilon q^{i - 1})_+$ for the same
    purpose.

We use an inductive argument to prove the theorem:

$$\begin{aligned}
\mathbb P(\xi_{\le i} \in T_i) &= \int_{T_{i - 1}} \mathbb P(\xi_i \in S_i | \xi_{< i} = y_{< i}) p^{i - 1} (y_{< i}) dy_{< i} \\
&\le \int_{T_{i - 1}} (e^{\epsilon_i} \mathbb P(\eta_i \in S_i | \eta_{< i} = y_{< i}) \wedge 1) p^{i - 1}(y_{< i}) dy_{< i} + \delta_i\\
&\le \int_{T_{i - 1}} (e^{\epsilon_i} \mathbb P(\eta_i \in S_i | \eta_{< i} = y_{< i}) \wedge 1) (e^{\epsilon_1 + ... + \epsilon_{i - 1}} q^{i - 1}(y_{< i}) + \mu^{i - 1} (y_{< i})) dy_{< i} + \delta_i\\
&\le \int_{T_{i - 1}} e^{\epsilon_i} \mathbb P(\eta_i \in S_i | \eta_{< i} = y_{< i}) e^{\epsilon_1 + ... + \epsilon_{i - 1}} q^{i - 1}(y_{< i}) dy_{< i} + \mu_{i - 1}(T_{i - 1}) + \delta_i\\
&\le e^{\epsilon_1 + ... + \epsilon_i} \mathbb P(\eta_{\le i} \in T_i) + \delta_1 + ... + \delta_{i - 1} + \delta_i.\\
\end{aligned}$$

In the second line we use Trick 1; in the third line we use the
induction assumption; in the fourth line we multiply the first term in
the first braket with first term in the second braket, and the second
term (i.e. $1$) in the first braket with the second term in the second
braket (i.e. the $\mu$ term); in the last line we use Trick 2.

The base case $i = 1$ is true since $M_1$ is
$(\epsilon_1, \delta_1)$-dp. $\square$

To prove the advanced composition theorem, we start with some lemmas.

**Claim 11**. If $p$ and $q$ are $\epsilon$-ind, then

$$D(p || q) + D(q || p) \le \epsilon(e^\epsilon - 1).$$

**Proof**. Since $p$ and $q$ are $\epsilon$-ind, we have
$|\log p(x) - \log q(x)| \le \epsilon$ for all $x$. Let
$S := \{x: p(x) > q(x)\}$. Then we have on

$$\begin{aligned}
D(p || q) + D(q || p) &= \int (p(x) - q(x)) (\log p(x) - \log q(x)) dx\\ 
&= \int_S (p(x) - q(x)) (\log p(x) - \log q(x)) dx + \int_{S^c} (q(x) - p(x)) (\log q(x) - \log p(x)) dx\\
&\le \epsilon(\int_S p(x) - q(x) dx + \int_{S^c} q(x) - p(x) dx)
\end{aligned}$$

Since on $S$ we have $q(x) \le p(x) \le e^\epsilon q(x)$, and on $S^c$
we have $p(x) \le q(x) \le e^\epsilon p(x)$, we obtain

$$D(p || q) + D(q || p) \le \epsilon \int_S (1 - e^{-\epsilon}) p(x) dx + \epsilon \int_{S^c} (e^{\epsilon} - 1) p(x) dx \le \epsilon (e^{\epsilon} - 1),$$

where in the last step we use $e^\epsilon - 1 \ge 1 - e^{- \epsilon}$
and $p(S) + p(S^c) = 1$. $\square$

**Claim 12**. If $p$ and $q$ are $\epsilon$-ind, then

$$D(p || q) \le a(\epsilon) \ge D(q || p),$$

where

$$a(\epsilon) = \epsilon (e^\epsilon - 1) 1_{\epsilon \le \log 2} + \epsilon 1_{\epsilon > \log 2} \le (\log 2)^{-1} \epsilon^2 1_{\epsilon \le \log 2} + \epsilon 1_{\epsilon > \log 2}. \qquad (6.98)$$

**Proof**. Since $p$ and $q$ are $\epsilon$-ind, we have

$$D(p || q) = \mathbb E_{\xi \sim p} \log {p(\xi) \over q(\xi)} \le \max_y {\log p(y) \over \log q(y)} \le \epsilon.$$

Comparing the quantity in Claim 11 ($\epsilon(e^\epsilon - 1)$) with the
quantity above ($\epsilon$), we arrive at the conclusion. $\square$

**Claim 13 ([Hoeffding\'s Inequality](https://en.wikipedia.org/wiki/Hoeffding%27s_inequality))**. 
Let $L_i$ be independent random variables with
$|L_i| \le b$, and let $L = L_1 + ... + L_k$, then for $t > 0$,

$$\mathbb P(L - \mathbb E L \ge t) \le \exp(- {t^2 \over 2 k b^2}).$$

**Claim 14
(Advanced Independent Composition Theorem)** ($\delta = 0$). Fix
$0 < \beta < 1$. Let $M_1, ..., M_k$ be $\epsilon$-dp, then the
independent composition $M$ of $M_{1 : k}$ is
$(k a(\epsilon) + \sqrt{2 k \log \beta^{-1}} \epsilon, \beta)$-dp.

**Remark**. By (6.98) we know that
$k a(\epsilon) + \sqrt{2 k \log \beta^{-1}} \epsilon = \sqrt{2 k \log \beta^{-1}} \epsilon + k O(\epsilon^2)$
when $\epsilon$ is sufficiently small, in which case the leading term is of order
$O(\sqrt k \epsilon)$ and we save a $\sqrt k$ in the $\epsilon$-part
compared to the Basic Composition Theorem (Claim 10).

**Remark**. In practice one can try different choices of $\beta$ and settle
with the one that gives the best privacy guarantee.
See the discussions at the end of [Part 2 of this post](/posts/2019-03-14-great-but-manageable-expectations.html).

**Proof**. Let $p_i$, $q_i$, $p$ and $q$ be the laws of
$M_i(x)$, $M_i(x')$, $M(x)$ and $M(x')$ respectively.

$$\mathbb E L_i = D(p_i || q_i) \le a(\epsilon),$$

where $L_i := L(p_i || q_i)$. Due to $\epsilon$-ind also have

$$|L_i| \le \epsilon.$$

Therefore, by Hoeffding\'s Inequality,

$$\mathbb P(L - k a(\epsilon) \ge t) \le \mathbb P(L - \mathbb E L \ge t) \le \exp(- t^2 / 2 k \epsilon^2),$$

where $L := \sum_i L_i = L(p || q)$.

Plugging in $t = \sqrt{2 k \epsilon^2 \log \beta^{-1}}$, we have

$$\mathbb P(L(p || q) \le k a(\epsilon) + \sqrt{2 k \epsilon^2 \log \beta^{-1}}) \ge 1 - \beta.$$

Similarly we also have

$$\mathbb P(L(q || p) \le k a(\epsilon) + \sqrt{2 k \epsilon^2 \log \beta^{-1}}) \ge 1 - \beta.$$

By Claim 1 we arrive at the conclusion. $\square$

**Claim 15 ([Azuma\'s Inequality](https://en.wikipedia.org/wiki/Azuma%27s_inequality))**.
Let $X_{0 : k}$ be a [supermartingale](https://en.wikipedia.org/wiki/Martingale_(probability_theory)).
If $|X_i - X_{i - 1}| \le b$, then

$$\mathbb P(X_k - X_0 \ge t) \le \exp(- {t^2 \over 2 k b^2}).$$

Azuma\'s Inequality implies a slightly weaker version of Hoeffding\'s
Inequality. To see this, let $L_{1 : k}$ be independent variables with
$|L_i| \le b$. Let $X_i = \sum_{j = 1 : i} L_j - \mathbb E L_j$. Then
$X_{0 : k}$ is a martingale, and

$$| X_i - X_{i - 1} | = | L_i - \mathbb E L_i | \le 2 b,$$

since $\|L_i\|_1 \le \|L_i\|_\infty$. Hence by Azuma\'s Inequality,

$$\mathbb P(L - \mathbb E L \ge t) \le \exp(- {t^2 \over 8 k b^2}).$$

Of course here we have made no assumption on $\mathbb E L_i$. If instead
we have some bound for the expectation, say $|\mathbb E L_i| \le a$,
then by the same derivation we have

$$\mathbb P(L - \mathbb E L \ge t) \le \exp(- {t^2 \over 2 k (a + b)^2}).$$

It is not hard to see what Azuma is to Hoeffding is like adaptive
composition to independent composition. Indeed, we can use Azuma\'s
Inequality to prove the Advanced Adaptive Composition Theorem for
$\delta = 0$.

**Claim 16
(Advanced Adaptive Composition Theorem)** ($\delta = 0$). Let
$\beta > 0$. Let $M_{1 : k}$ be $k$ mechanisms with independent noises
such that for each $i$ and $y_{1 : i}$, $M_i(y_{1 : i})$ is
$(\epsilon, 0)$-dp. Then the adpative composition of $M_{1 : k}$ is
$(k a(\epsilon) + \sqrt{2 k \log \beta^{-1}} (\epsilon + a(\epsilon)), \beta)$-dp.

**Proof**. As before, let $\xi_{1 : k} \overset{d}{=} M(x)$
and $\eta_{1 : k} \overset{d}{=} M(x')$, where $M$ is the adaptive
composition of $M_{1 : k}$. Let $p_i$ (resp. $q_i$) be the law of
$\xi_i | \xi_{< i}$ (resp. $\eta_i | \eta_{< i}$). Let $p^i$ (resp.
$q^i$) be the law of $\xi_{\le i}$ (resp. $\eta_{\le i}$). We want to
construct supermartingale $X$. To this end, let

$$X_i = \log {p^i(\xi_{\le i}) \over q^i(\xi_{\le i})} - i a(\epsilon) $$

We show that $(X_i)$ is a supermartingale:

$$\begin{aligned}
\mathbb E(X_i - X_{i - 1} | X_{i - 1}) &= \mathbb E \left(\log {p_i (\xi_i | \xi_{< i}) \over q_i (\xi_i | \xi_{< i})} - a(\epsilon) | \log {p^{i - 1} (\xi_{< i}) \over q^{i - 1} (\xi_{< i})}\right) \\
&= \mathbb E \left( \mathbb E \left(\log {p_i (\xi_i | \xi_{< i}) \over q_i (\xi_i | \xi_{< i})} | \xi_{< i}\right) | \log {p^{i - 1} (\xi_{< i}) \over q^{i - 1} (\xi_{< i})}\right) - a(\epsilon) \\
&= \mathbb E \left( D(p_i (\cdot | \xi_{< i}) || q_i (\cdot | \xi_{< i})) | \log {p^{i - 1} (\xi_{< i}) \over q^{i - 1} (\xi_{< i})}\right) - a(\epsilon) \\
&\le 0,
\end{aligned}$$

since by Claim 12
$D(p_i(\cdot | y_{< i}) || q_i(\cdot | y_{< i})) \le a(\epsilon)$ for
all $y_{< i}$.

Since

$$| X_i - X_{i - 1} | = | \log {p_i(\xi_i | \xi_{< i}) \over q_i(\xi_i | \xi_{< i})} - a(\epsilon) | \le \epsilon + a(\epsilon),$$

by Azuma\'s Inequality,

$$\mathbb P(\log {p^k(\xi_{1 : k}) \over q^k(\xi_{1 : k})} \ge k a(\epsilon) + t) \le \exp(- {t^2 \over 2 k (\epsilon + a(\epsilon))^2}). \qquad(6.99)$$

Let $t = \sqrt{2 k \log \beta^{-1}} (\epsilon + a(\epsilon))$ we are
done. $\square$

**Claim 17
(Advanced Independent Composition Theorem)**. Fix $0 < \beta < 1$. Let
$M_1, ..., M_k$ be $(\epsilon, \delta)$-dp, then the independent
composition $M$ of $M_{1 : k}$ is
$(k a(\epsilon) + \sqrt{2 k \log \beta^{-1}} \epsilon, k \delta + \beta)$-dp.

**Proof**. By Claim 4, there exist events $E_{1 : k}$ and
$F_{1 : k}$ such that

1.  The laws $p_{i | E_i}$ and $q_{i | F_i}$ are $\epsilon$-ind.
2.  $\mathbb P(E_i), \mathbb P(F_i) \ge 1 - \delta$.

Let $E := \bigcap E_i$ and $F := \bigcap F_i$, then they both have
probability at least $1 - k \delta$, and $p_{i | E}$ and $q_{i | F}$ are
$\epsilon$-ind.

By Claim 14, $p_{|E}$ and $q_{|F}$ are
$(\epsilon' := k a(\epsilon) + \sqrt{2 k \epsilon^2 \log \beta^{-1}}, \beta)$-ind.
Let us shrink the bigger event between $E$ and $F$ so that they have
equal probabilities. Then

$$\begin{aligned}
p (S) &\le p_{|E}(S) \mathbb P(E) + \mathbb P(E^c) \\
&\le (e^{\epsilon'} q_{|F}(S) + \beta) \mathbb P(F) + k \delta\\
&\le e^{\epsilon'} q(S) + \beta + k \delta.
\end{aligned}$$

$\square$

**Claim 18
(Advanced Adaptive Composition Theorem)**. Fix $0 < \beta < 1$. Let
$M_{1 : k}$ be $k$ mechanisms with independent noises such that for each
$i$ and $y_{1 : i}$, $M_i(y_{1 : i})$ is $(\epsilon, \delta)$-dp. Then
the adpative composition of $M_{1 : k}$ is
$(k a(\epsilon) + \sqrt{2 k \log \beta^{-1}} (\epsilon + a(\epsilon)), \beta + k \delta)$-dp.

**Remark**. 
This theorem appeared in Dwork-Rothblum-Vadhan 2010, but I could not find a proof there.
A proof can be found in Dwork-Roth 2013 (See Theorem 3.20 there).
Here I prove it in a similar way, except that instead of the use of an intermediate random variable there,
I use the conditional probability results from Claim 5, the approach mentioned in Vadhan 2017.

**Proof**. By Claim 5, there exist events $E_{1 : k}$ and
$F_{1 : k}$ such that

1.  The laws $p_{i | E_i}(\cdot | y_{< i})$ and
    $q_{i | F_i}(\cdot | y_{< i})$ are $\epsilon$-ind for all $y_{< i}$.
2.  $\mathbb P(E_i | y_{< i}), \mathbb P(F_i | y_{< i}) \ge 1 - \delta$
    for all $y_{< i}$.

Let $E := \bigcap E_i$ and $F := \bigcap F_i$, then they both have
probability at least $1 - k \delta$, and $p_{i | E}(\cdot | y_{< i}$ and
$q_{i | F}(\cdot | y_{< i})$ are $\epsilon$-ind.

By Advanced Adaptive Composition Theorem ($\delta = 0$), $p_{|E}$ and
$q_{|F}$ are
$(\epsilon' := k a(\epsilon) + \sqrt{2 k \log \beta^{-1}} (\epsilon + a(\epsilon)), \beta)$-ind.

The rest is the same as in the proof of Claim 17. $\square$

Subsampling 
-----------

Stochastic gradient descent is like gradient descent, but with random
subsampling.

Recall we have been considering databases in the space $Z^m$. Let
$n < m$ be a positive integer,
$\mathcal I := \{I \subset [m]: |I| = n\}$ be the set of subsets of
$[m]$ of size $n$, and $\gamma$ a random subset sampled uniformly from
$\mathcal I$. Let $r = {n \over m}$ which we call the subsampling rate.
Then we may add a subsampling module to the noisy gradient descent
algorithm (6.97) considered before

$$\theta_{t} = \theta_{t - 1} - \alpha n^{-1} \sum_{i \in \gamma} \nabla_\theta h_\theta(x_i) |_{\theta = \theta_{t - 1}} + \zeta_t. \qquad (7)$$

It turns out subsampling has an amplification effect on privacy.

**Claim 19 (Ullman 2017)**. Fix
$r \in [0, 1]$. Let $n \le m$ be two nonnegative integers with
$n = r m$. Let $N$ be an $(\epsilon, \delta)$-dp machanism on $Z^n$.
Define mechanism $M$ on $Z^m$ by

$$M(x) = N(x_\gamma)$$

Then $M$ is $(\log (1 + r(e^\epsilon - 1)), r \delta)$-dp.

**Remark**. Some seem to cite
Kasiviswanathan-Lee-Nissim-Raskhodnikova-Smith 2005 for this result, but
it is not clear to me how it appears there.

**Proof**. Let $x, x' \in Z^n$ such that they differ by one
row $x_i \neq x_i'$. Naturally we would like to consider the cases where
the index $i$ is picked and the ones where it is not separately. Let
$\mathcal I_\in$ and $\mathcal I_\notin$ be these two cases:

$$\begin{aligned}
\mathcal I_\in = \{J \subset \mathcal I: i \in J\}\\
\mathcal I_\notin = \{J \subset \mathcal I: i \notin J\}\\
\end{aligned}$$

We will use these notations later. Let $A$ be the event
$\{\gamma \ni i\}$.

Let $p$ and $q$ be the laws of $M(x)$ and $M(x')$ respectively. We
collect some useful facts about them. First due to $N$ being
$(\epsilon, \delta)$-dp,

$$p_{|A}(S) \le e^\epsilon q_{|A}(S) + \delta.$$

Also,

$$p_{|A}(S) \le e^\epsilon p_{|A^c}(S) + \delta.$$

To see this, note that being conditional laws, $p_A$ and $p_{A^c}$ are
averages of laws over $\mathcal I_\in$ and $\mathcal I_\notin$
respectively:

$$\begin{aligned}
p_{|A}(S) = |\mathcal I_\in|^{-1} \sum_{I \in \mathcal I_\in} \mathbb P(N(x_I) \in S)\\
p_{|A^c}(S) = |\mathcal I_\notin|^{-1} \sum_{J \in \mathcal I_\notin} \mathbb P(N(x_J) \in S).
\end{aligned}$$

Now we want to pair the $I$\'s in $\mathcal I_\in$ and $J$\'s in
$\mathcal I_\notin$ so that they differ by one index only, which means
$d(x_I, x_J) = 1$. Formally, this means we want to consider the set:

$$\mathcal D := \{(I, J) \in \mathcal I_\in \times \mathcal I_\notin: |I \cap J| = n - 1\}.$$

We may observe by trying out some simple cases that every
$I \in \mathcal I_\in$ is paired with $n$ elements in
$\mathcal I_\notin$, and every $J \in \mathcal I_\notin$ is paired with
$m - n$ elements in $\mathcal I_\in$. Therefore

$$p_{|A}(S) = |\mathcal D|^{-1} \sum_{(I, J) \in \mathcal D} \mathbb P(N(x_I \in S)) \le |\mathcal D|^{-1} \sum_{(I, J) \in \mathcal D} (e^\epsilon \mathbb P(N(x_J \in S)) + \delta) = e^\epsilon p_{|A^c} (S) + \delta.$$

Since each of the $m$ indices is picked independently with probability
$r$, we have

$$\mathbb P(A) = r.$$

Let $t \in [0, 1]$ to be determined. We may write

$$\begin{aligned}
p(S) &= r p_{|A} (S) + (1 - r) p_{|A^c} (S)\\
&\le r(t e^\epsilon q_{|A}(S) + (1 - t) e^\epsilon q_{|A^c}(S) + \delta) + (1 - r) q_{|A^c} (S)\\
&= rte^\epsilon q_{|A}(S) + (r(1 - t) e^\epsilon + (1 - r)) q_{|A^c} (S) + r \delta\\
&= te^\epsilon r q_{|A}(S) + \left({r \over 1 - r}(1 - t) e^\epsilon + 1\right) (1 - r) q_{|A^c} (S) + r \delta \\
&\le \left(t e^\epsilon \wedge \left({r \over 1 - r} (1 - t) e^\epsilon + 1\right)\right) q(S) + r \delta. \qquad (7.5)
\end{aligned}$$

We can see from the last line that the best bound we can get is when

$$t e^\epsilon = {r \over 1 - r} (1 - t) e^\epsilon + 1.$$

Solving this equation we obtain

$$t = r + e^{- \epsilon} - r e^{- \epsilon}$$

and plugging this in (7.5) we have

$$p(S) \le (1 + r(e^\epsilon - 1)) q(S) + r \delta.$$

$\square$

Since $\log (1 + x) < x$ for $x > 0$, we can rewrite the conclusion of
the Claim to $(r(e^\epsilon - 1), r \delta)$-dp. Further more, if
$\epsilon < \alpha$ for some $\alpha$, we can rewrite it as
$(r \alpha^{-1} (e^\alpha - 1) \epsilon, r \delta)$-dp or
$(O(r \epsilon), r \delta)$-dp.

Let $\epsilon < 1$. We see that if the mechanism $N$ is
$(\epsilon, \delta)$-dp on $Z^n$, then $M$ is
$(2 r \epsilon, r \delta)$-dp, and if we run it over $k / r$
minibatches, by Advanced Adaptive Composition theorem, we have
$(\sqrt{2 k r \log \beta^{-1}} \epsilon + 2 k r \epsilon^2, k \delta + \beta)$-dp.

This is better than the privacy guarantee without subsampling, where we
run over $k$ iterations and obtain
$(\sqrt{2 k \log \beta^{-1}} \epsilon + 2 k \epsilon^2, k \delta + \beta)$-dp.
So with subsampling we gain an extra $\sqrt r$ in the $\epsilon$-part of
the privacy guarantee. But, smaller subsampling rate means smaller
minibatch size, which would result in bigger variance, so there is a
trade-off here.

Finally we define the differentially private stochastic gradient descent
(DP-SGD) with the Gaussian mechanism
(Abadi-Chu-Goodfellow-McMahan-Mironov-Talwar-Zhang 2016), which is (7)
with the noise specialised to Gaussian and an added clipping operation
to bound to sensitivity of the query to a chosen $C$:

$$\theta_{t} = \theta_{t - 1} - \alpha \left(n^{-1} \sum_{i \in \gamma} \nabla_\theta \ell(x_i; \theta) |_{\theta = \theta_{t - 1}}\right)_{\text{Clipped at }C / 2} + N(0, \sigma^2 C^2 I),$$

where

$$y_{\text{Clipped at } \alpha} := y / (1 \vee {\|y\|_2 \over \alpha})$$

is $y$ clipped to have norm at most $\alpha$.

Note that the clipping in DP-SGD is much stronger than making the query
have sensitivity $C$. It makes the difference between the query results
of two *arbitrary* inputs bounded by $C$, rather than *neighbouring*
inputs.

In [Part 2 of this post](/posts/2019-03-14-great-but-manageable-expectations.html) we will use the tools developed above to discuss the privacy
guarantee for DP-SGD, among other things.

References 
----------

-   Abadi, Martín, Andy Chu, Ian Goodfellow, H. Brendan McMahan, Ilya
    Mironov, Kunal Talwar, and Li Zhang. "Deep Learning with
    Differential Privacy." Proceedings of the 2016 ACM SIGSAC Conference
    on Computer and Communications Security - CCS'16, 2016, 308--18.
    <https://doi.org/10.1145/2976749.2978318>.
-   Dwork, Cynthia, and Aaron Roth. "The Algorithmic Foundations of
    Differential Privacy." Foundations and Trends® in Theoretical
    Computer Science 9, no. 3--4 (2013): 211--407.
    <https://doi.org/10.1561/0400000042>.
-   Dwork, Cynthia, Guy N. Rothblum, and Salil Vadhan. "Boosting and
    Differential Privacy." In 2010 IEEE 51st Annual Symposium on
    Foundations of Computer Science, 51--60. Las Vegas, NV, USA:
    IEEE, 2010. <https://doi.org/10.1109/FOCS.2010.12>.
-   Shiva Prasad Kasiviswanathan, Homin K. Lee, Kobbi Nissim, Sofya
    Raskhodnikova, and Adam Smith. "What Can We Learn Privately?" In
    46th Annual IEEE Symposium on Foundations of Computer Science
    (FOCS'05). Pittsburgh, PA, USA: IEEE, 2005.
    <https://doi.org/10.1109/SFCS.2005.1>.
-   Murtagh, Jack, and Salil Vadhan. "The Complexity of Computing the
    Optimal Composition of Differential Privacy." In Theory of
    Cryptography, edited by Eyal Kushilevitz and Tal Malkin,
    9562:157--75. Berlin, Heidelberg: Springer Berlin Heidelberg, 2016.
    <https://doi.org/10.1007/978-3-662-49096-9_7>.
-   Ullman, Jonathan. "Solution to CS7880 Homework 1.", 2017.
    <http://www.ccs.neu.edu/home/jullman/cs7880s17/HW1sol.pdf>
-   Vadhan, Salil. "The Complexity of Differential Privacy." In
    Tutorials on the Foundations of Cryptography, edited by Yehuda
    Lindell, 347--450. Cham: Springer International Publishing, 2017.
    <https://doi.org/10.1007/978-3-319-57048-8_7>.