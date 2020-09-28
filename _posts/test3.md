---
---

This is Part 2 of a two-part blog post on differential privacy.
Continuing from [Part 1](/posts/2019-03-13-a-tail-of-two-densities.html),
I discuss the Rényi differential privacy, corresponding to
the Rényi divergence, a study of the [moment generating functions](https://en.wikipedia.org/wiki/Moment-generating_function)
of the divergence between probability measures in order to derive the tail bounds. 

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

*If you are confused by any notations, ask me or try [this](/notations.html).*

Rényi divergence and differential privacy 
-----------------------------------------

Recall in the proof of Gaussian mechanism privacy guarantee (Claim 8) we
used the Chernoff bound for the Gaussian noise. Why not use the Chernoff
bound for the divergence variable / privacy loss directly, since the
latter is closer to the core subject than the noise? This leads us to
the study of Rényi divergence.

So far we have seen several notions of divergence used in differential
privacy: the max divergence which is $\epsilon$-ind in disguise:

$$D_\infty(p || q) := \max_y \log {p(y) \over q(y)},$$

the $\delta$-approximate max divergence that defines the
$(\epsilon, \delta)$-ind:

$$D_\infty^\delta(p || q) := \max_y \log{p(y) - \delta \over q(y)},$$

and the KL-divergence which is the expectation of the divergence
variable:

$$D(p || q) = \mathbb E L(p || q) = \int \log {p(y) \over q(y)} p(y) dy.$$

The Rényi divergence is an interpolation between the max divergence and
the KL-divergence, defined as the log moment generating function /
cumulants of the divergence variable:

$$D_\lambda(p || q) = (\lambda - 1)^{-1} \log \mathbb E \exp((\lambda - 1) L(p || q)) = (\lambda - 1)^{-1} \log \int {p(y)^\lambda \over q(y)^{\lambda - 1}} dx.$$

Indeed, when $\lambda \to \infty$ we recover the max divergence, and
when $\lambda \to 1$, by recognising $D_\lambda$ as a derivative in
$\lambda$ at $\lambda = 1$, we recover the KL divergence. In this post
we only consider $\lambda > 1$.

Using the Rényi divergence we may define:

**Definition (Rényi
differential privacy)** (Mironov 2017). An mechanism $M$ is
$(\lambda, \rho)$*-Rényi differentially private* ($(\lambda, \rho)$-rdp)
if for all $x$ and $x'$ with distance $1$,

$$D_\lambda(M(x) || M(x')) \le \rho.$$

For convenience we also define two related notions, $G_\lambda (f || g)$
and $\kappa_{f, g} (t)$ for $\lambda > 1$, $t > 0$ and positive
functions $f$ and $g$:

$$G_\lambda(f || g) = \int f(y)^{\lambda} g(y)^{1 - \lambda} dy; \qquad \kappa_{f, g} (t) = \log G_{t + 1}(f || g).$$

For probability densities $p$ and $q$, $G_{t + 1}(p || q)$ and
$\kappa_{p, q}(t)$ are the $t$th moment generating function and [cumulant](https://en.wikipedia.org/wiki/Cumulant)
of the divergence variable $L(p || q)$, and

$$D_\lambda(p || q) = (\lambda - 1)^{-1} \kappa_{p, q}(\lambda - 1).$$

In the following, whenever you see $t$, think of it as $\lambda - 1$.

**Example 1 (RDP for the Gaussian
mechanism)**. Using the scaling and translation invariance of $L$ (6.1),
we have that the divergence variable for two Gaussians with the same
variance is

$$L(N(\mu_1, \sigma^2 I) || N(\mu_2, \sigma^2 I)) \overset{d}{=} L(N(0, I) || N((\mu_2 - \mu_1) / \sigma, I)).$$

With this we get

$$D_\lambda(N(\mu_1, \sigma^2 I) || N(\mu_2, \sigma^2 I)) = {\lambda \|\mu_2 - \mu_1\|_2^2 \over 2 \sigma^2} = D_\lambda(N(\mu_2, \sigma^2 I) || N(\mu_1, \sigma^2 I)).$$

Again due to the scaling invariance of $L$, we only need to consider $f$
with sensitivity $1$, see the discussion under (6.1). The Gaussian
mechanism on query $f$ is thus $(\lambda, \lambda / 2 \sigma^2)$-rdp for
any $\lambda > 1$.

From the example of Gaussian mechanism, we see that the relation between
$\lambda$ and $\rho$ is like that between $\epsilon$ and $\delta$. Given
$\lambda$ (resp. $\rho$) and parameters like variance of the noise and
the sensitivity of the query, we can write $\rho = \rho(\lambda)$ (resp.
$\lambda = \lambda(\rho)$).

Using the Chernoff bound (6.7), we can bound the divergence variable:

$$\mathbb P(L(p || q) \ge \epsilon) \le {\mathbb E \exp(t L(p || q)) \over \exp(t \epsilon))} =  \exp (\kappa_{p, q}(t) - \epsilon t). \qquad (7.7)$$

For a function $f: I \to \mathbb R$, denote its [Legendre transform](https://en.wikipedia.org/wiki/Legendre_transformation) by

$$f^*(\epsilon) := \sup_{t \in I} (\epsilon t - f(t)).$$

By taking infimum on the RHS of (7.7), we obtain

**Claim 20**. Two probability densities $p$ and $q$ are
$(\epsilon, \exp(-\kappa_{p, q}^*(\epsilon)))$-ind.

Given a mechanism $M$, let $\kappa_M(t)$ denote an upper bound for the
cumulant of its privacy loss:

$$\log \mathbb E \exp(t L(M(x) || M(x'))) \le \kappa_M(t), \qquad \forall x, x'\text{ with } d(x, x') = 1.$$

For example, we can set $\kappa_M(t) = t \rho(t + 1)$. Using the same
argument we have the following:

**Claim 21**. If $M$ is $(\lambda, \rho)$-rdp, then

1.  it is also
    $(\epsilon, \exp((\lambda - 1) (\rho - \epsilon)))$-dp for any
    $\epsilon \ge \rho$.
2.  Alternatively, $M$ is $(\epsilon, - \exp(\kappa_M^*(\epsilon)))$-dp
    for any $\epsilon > 0$.
3.  Alternatively, for any $0 < \delta \le 1$, $M$ is
    $(\rho + (\lambda - 1)^{-1} \log \delta^{-1}, \delta)$-dp.

**Example 2 (Gaussian mechanism)**.
We can apply the above argument to the Gaussian mechanism on query $f$
and get:

$$\delta \le \inf_{\lambda > 1} \exp((\lambda - 1) ({\lambda \over 2 \sigma^2} - \epsilon))$$

By assuming $\sigma^2 > (2 \epsilon)^{-1}$ we have that the infimum is
achieved when $\lambda = (1 + 2 \epsilon / \sigma^2) / 2$ and

$$\delta \le \exp(- ((2 \sigma)^{-1} - \epsilon \sigma)^2 / 2)$$

which is the same result as (6.8), obtained using the Chernoff bound of
the noise.

However, as we will see later, compositions will yield different results
from those obtained from methods in [Part 1](/posts/2019-03-13-a-tail-of-two-densities.html) when considering Rényi dp.

### Moment Composition

**Claim 22 (Moment Composition
Theorem)**. Let $M$ be the adaptive composition of $M_{1 : k}$. Suppose
for any $y_{< i}$, $M_i(y_{< i})$ is $(\lambda, \rho)$-rdp. Then $M$ is
$(\lambda, k\rho)$-rdp.

**Proof**. Rather straightforward. As before let $p_i$ and
$q_i$ be the conditional laws of adpative composition of $M_{1 : i}$ at
$x$ and $x'$ respectively, and $p^i$ and $q^i$ be the joint laws of
$M_{1 : i}$ at $x$ and $x'$ respectively. Denote

$$D_i = \mathbb E \exp((\lambda - 1)\log {p^i(\xi_{1 : i}) \over q^i(\xi_{1 : i})})$$

Then

$$\begin{aligned}
D_i &= \mathbb E\mathbb E \left(\exp((\lambda - 1)\log {p_i(\xi_i | \xi_{< i}) \over q_i(\xi_i | \xi_{< i})}) \exp((\lambda - 1)\log {p^{i - 1}(\xi_{< i}) \over q^{i - 1}(\xi_{< i})}) \big| \xi_{< i}\right) \\
&= \mathbb E \mathbb E \left(\exp((\lambda - 1)\log {p_i(\xi_i | \xi_{< i}) \over q_i(\xi_i | \xi_{< i})}) | \xi_{< i}\right) \exp\left((\lambda - 1)\log {p^{i - 1}(\xi_{< i}) \over q^{i - 1}(\xi_{< i})}\right)\\
&\le \mathbb E \exp((\lambda - 1) \rho) \exp\left((\lambda - 1)\log {p^{i - 1}(\xi_{< i}) \over q^{i - 1}(\xi_{< i})}\right)\\
&= \exp((\lambda - 1) \rho) D_{i - 1}.
\end{aligned}$$

Applying this recursively we have

$$D_k \le \exp(k(\lambda - 1) \rho),$$

and so

$$(\lambda - 1)^{-1} \log \mathbb E \exp((\lambda - 1)\log {p^k(\xi_{1 : i}) \over q^k(\xi_{1 : i})}) = (\lambda - 1)^{-1} \log D_k \le k \rho.$$

Since this holds for all $x$ and $x'$, we are done. $\square$

This, together with the scaling property of the legendre transformation:

$$(k f)^*(x) = k f^*(x / k)$$

yields

**Claim 23**. The $k$-fold adaptive composition of
$(\lambda, \rho(\lambda))$-rdp mechanisms is
$(\epsilon, \exp(- k \kappa^*(\epsilon / k)))$-dp, where
$\kappa(t) := t \rho(t + 1)$.

**Example 3 (Gaussian mechanism)**.
We can apply the above claim to Gaussian mechanism. Again, without loss
of generality we assume $S_f = 1$. But let us do it manually to get the
same results. If we apply the Moment Composition Theorem to the an
adaptive composition of Gaussian mechanisms on the same query, then
since each $M_i$ is $(\lambda, (2 \sigma^2)^{-1} \lambda)$-rdp, the
composition $M$ is $(\lambda, (2 \sigma^2)^{-1} k \lambda)$-rdp.
Processing this using the Chernoff bound as in the previous example, we
have

$$\delta = \exp(- ((2 \sigma / \sqrt k)^{-1} - \epsilon \sigma / \sqrt k)^2 / 2),$$

Substituting $\sigma$ with $\sigma / \sqrt k$ in (6.81), we conclude
that if

$$\sigma > \sqrt k \left(\epsilon^{-1} \sqrt{2 \log \delta^{-1}} + (2 \epsilon)^{- {1 \over 2}}\right)$$

then the composition $M$ is $(\epsilon, \delta)$-dp.

As we will see in the discussions at the end of this post, this result
is different from (and probably better than) the one obtained by using
the Advanced Composition Theorem (Claim 18).

### Subsampling

We also have a subsampling theorem for the Rényi dp.

**Claim 24**. Fix $r \in [0, 1]$. Let $m \le n$ be two
nonnegative integers with $m = r n$. Let $N$ be a $(\lambda, \rho)$-rdp
machanism on $X^m$. Let $\mathcal I := \{J \subset [n]: |J| = m\}$ be
the set of subsets of $[n]$ of size $m$. Define mechanism $M$ on $X^n$
by

$$M(x) = N(x_\gamma)$$

where $\gamma$ is sampled uniformly from $\mathcal I$. Then $M$ is
$(\lambda, {1 \over \lambda - 1} \log (1 + r(e^{(\lambda - 1) \rho} - 1)))$-rdp.

To prove Claim 24, we need a useful lemma:

**Claim 25**. Let $p_{1 : n}$ and $q_{1 : n}$ be
nonnegative integers, and $\lambda > 1$. Then

$${(\sum p_i)^\lambda \over (\sum q_i)^{\lambda - 1}} \le \sum_i {p_i^\lambda \over q_i^{\lambda - 1}}. \qquad (8)$$

**Proof**. Let

$$r(i) := p_i / P, \qquad u(i) := q_i / Q$$

where

$$P := \sum p_i, \qquad Q := \sum q_i$$

then $r$ and $u$ are probability mass functions. Plugging in
$p_i = r(i) P$ and $q_i = u(i) Q$ into the objective (8), it suffices to
show

$$1 \le \sum_i {r(i)^\lambda \over u(i)^{\lambda - 1}} = \mathbb E_{\xi \sim u} \left({r(\xi) \over u(\xi)}\right)^\lambda$$

This is true due to Jensen\'s Inequality:

$$\mathbb E_{\xi \sim u} \left({r(\xi) \over u(\xi)}\right)^\lambda \ge \left(\mathbb E_{\xi \sim u} {r(\xi) \over u(\xi)} \right)^\lambda = 1.$$

$\square$

**Proof of Claim 24**. Define $\mathcal I$ as
before.

Let $p$ and $q$ be the laws of $M(x)$ and $M(x')$ respectively. For any
$I \in \mathcal I$, let $p_I$ and $q_I$ be the laws of $N(x_I)$ and
$N(x_I')$ respectively. Then we have

$$\begin{aligned}
p(y) &= n^{-1} \sum_{I \in \mathcal I} p_I(y) \\
q(y) &= n^{-1} \sum_{I \in \mathcal I} q_I(y),
\end{aligned}$$

where $n = |\mathcal I|$.

The MGF of $L(p || q)$ is thus

$$\mathbb E((\lambda - 1) L(p || q)) = n^{-1} \int {(\sum_I p_I(y))^\lambda \over (\sum_I q_I(y))^{\lambda - 1}} dy \le n^{-1} \sum_I \int {p_I(y)^\lambda \over q_I(y)^{\lambda - 1}} dy \qquad (9)$$

where in the last step we used Claim 25. As in the proof of Claim 19, we
divide $\mathcal I$ into disjoint sets $\mathcal I_\in$ and
$\mathcal I_\notin$. Furthermore we denote by $n_\in$ and $n_\notin$
their cardinalities. Then the right hand side of (9) becomes

$$n^{-1} \sum_{I \in \mathcal I_\in} \int {p_I(y)^\lambda \over q_I(y)^{\lambda - 1}} dy + n^{-1} \sum_{I \in \mathcal I_\notin} \int {p_I(y)^\lambda \over q_I(y)^{\lambda - 1}} dy$$

The summands in the first are the MGF of $L(p_I || q_I)$, and the
summands in the second term are $1$, so

$$\begin{aligned}
\mathbb E((\lambda - 1) L(p || q)) &\le n^{-1} \sum_{I \in \mathcal I_\in} \mathbb E \exp((\lambda - 1) L(p_I || q_I)) + (1 - r) \\
&\le n^{-1} \sum_{I \in \mathcal I_\in} \exp((\lambda - 1) D_\lambda(p_I || q_I)) + (1 - r) \\
&\le r \exp((\lambda - 1) \rho) + (1 - r).
\end{aligned}$$

Taking log and dividing by $(\lambda - 1)$ on both sides we have

$$D_\lambda(p || q) \le (\lambda - 1)^{-1} \log (1 + r(\exp((\lambda - 1) \rho) - 1)).$$

$\square$

As before, we can rewrite the conclusion of Lemma 6 using
$1 + z \le e^z$ and obtain
$(\lambda, (\lambda - 1)^{-1} r (e^{(\lambda - 1) \rho} - 1))$-rdp,
which further gives $(\lambda, \alpha^{-1} (e^\alpha - 1) r \rho)$-rdp
(or $(\lambda, O(r \rho))$-rdp) if $(\lambda - 1) \rho < \alpha$ for
some $\alpha$.

It is not hard to see that the subsampling theorem in moment method,
even though similar to the results of that in the usual method, does not
help due to lack of an analogue of advanced composition theorem of the
moments.

**Example 4 (Gaussian mechanism)**.
Applying the moment subsampling theorem to the Gaussian mechanism, we
obtain $(\lambda, O(r \lambda / \sigma^2))$-rdp for a subsampled
Gaussian mechanism with rate $r$.
Abadi-Chu-Goodfellow-McMahan-Mironov-Talwar-Zhang 2016 (ACGMMTZ16 in the
following), however, gains an extra $r$ in the bound given certain
assumptions.

ACGMMTZ16 
---------

What follows is my understanding of this result. I call it a conjecture
because there is a gap which I am not able to reproduce their proof or
prove it myself. This does not mean the result is false. On the
contrary, I am inclined to believe it is true.

**Claim 26**. Assuming Conjecture 1 (see below) is true. 
For a subsampled Gaussian mechanism
with ratio $r$, if $r = O(\sigma^{-1})$ and $\lambda = O(\sigma^2)$,
then we have $(\lambda, O(r^2 \lambda / \sigma^2))$-rdp.

Wait, why is there a conjecture? Well, I have tried but not been able to
prove the following, which is a hidden assumption in the original proof:

**Conjecture 1**.
Let $M$ be the Gaussian mechanism with subsampling rate $r$,
and $p$ and $q$ be the laws of $M(x)$ and $M(x')$ respectively, where $d(x, x') = 1$.
Then

$$D_\lambda (p || q) \le D_\lambda (r \mu_1 + (1 - r) \mu_0 || \mu_0)$$ 

where $\mu_i = N(i, \sigma^2)$.

**Remark**. 
Conjecture 1 is heuristically reasonable.
To see this, let us use the notations $p_I$ and $q_I$ to be $q$ and $p$ conditioned on
the subsampling index $I$, just like in the proof of the subsampling theorems (Claim 19 and 24).
Then for $I \in \mathcal I_\in$,

$$D_\lambda(p_I || q_I) \le D_\lambda(\mu_0 || \mu_1),$$

and for $I \in \mathcal I_\notin$,

$$D_\lambda(p_I || q_I) = 0 = D_\lambda(\mu_0 || \mu_0).$$

Since we are taking an average over $\mathcal I$, of which $r |\mathcal I|$ are
in $\mathcal I_\in$ and $(1 - r) |\mathcal I|$ are in $\mathcal I_\notin$, (9.3) says
"the inequalities carry over averaging".

[A more general version of Conjecture 1 has been proven false](https://math.stackexchange.com/a/3152296/149540).
The counter example for the general version does not apply here, so it is still possible Conjecture 1 is true.

Let $p_\in$ (resp. $q_\in$) be the average of $p_I$ (resp. $q_I$) over $I \in \mathcal I_\in$,
and $p_\notin$ (resp. $q_\notin$) be the average of $p_I$ (resp. $q_I$) over $I \in \mathcal I_\notin$.

Immediately we have $p_\notin = q_\notin$, hence

$$D_\lambda(p_\notin || q_\notin) = 0 = D_\lambda(\mu_0 || \mu_0). \qquad(9.7)$$ 

By Claim 25, we have

$$D_\lambda(p_\in || q_\in) \le D_\lambda (\mu_1 || \mu_0). \qquad(9.9) $$

So one way to prove Conjecture 1 is perhaps prove a more specialised 
comparison theorem than the false conjecture: 

Given (9.7) and (9.9), show that 

$$D_\lambda(r p_\in + (1 - r) p_\notin || r q_\in + (1 - r) q_\notin) \le D_\lambda(r \mu_1 + (1 - r) \mu_0 || \mu_0).$$

\[End of Remark\]

<!---
**Conjecture 1** \[Probably [FALSE](https://math.stackexchange.com/a/3152296/149540), to be removed\]. Let $p_i$, $q_i$, $\mu_i$, $\nu_i$ be
probability densities on the same space for $i = 1 : n$. If
$D_\lambda(p_i || q_i) \le D_\lambda(\mu_i || \nu_i)$ for all $i$, then

$$D_\lambda(n^{-1} \sum_i p_i || n^{-1} \sum_i q_i) \le D_\lambda(n^{-1} \sum_i \mu_i || n^{-1} \sum_i \nu_i).$$

Basically, it is saying \"if for each $i$, $p_i$ and $q_i$ are closer to
each other than $\mu_i$ and $\nu_i$, then so are their averages over
$i$\".
So it is heuristically reasonable.
But it is probably [**FALSE**](https://math.stackexchange.com/a/3152296/149540).
This does not mean Claim 26 is false, as it might still be possible that Conjecture 2 (see below) is true.

This conjecture is equivalent to its special case when $n = 2$ by an induction argument
(replacing one pair of densities at a time).
-->

Recall the definition of $G_\lambda$ under the definition of Rényi
differential privacy. The following Claim will be useful.

**Claim 27**. Let $\lambda$ be a positive integer, then

$$G_\lambda(r p + (1 - r) q || q) = \sum_{k = 1 : \lambda} {\lambda \choose k} r^k (1 - r)^{\lambda - k} G_k(p || q).$$

**Proof**. Quite straightforward, by expanding the numerator
$(r p + (1 - r) q)^\lambda$ using binomial expansion. $\square$

**Proof of Claim 26**. 
By Conjecture 1, it suffices to prove the following:

If $r \le c_1 \sigma^{-1}$ and $\lambda \le c_2 \sigma^2$ for some
positive constant $c_1$ and $c_2$, then
there exists $C = C(c_1, c_2)$ such that
$G_\lambda (r \mu_1 + (1 - r) \mu_0 || \mu_0) \le C$ (since
$O(r^2 \lambda^2 / \sigma^2) = O(1)$).

**Remark in the proof**. Note that the choice of
$c_1$, $c_2$ and the function $C(c_1, c_2)$ are important to the
practicality and usefulness of Claim 26.

<!---
Part 1 can be derived using Conjecture 1, but since Conjecture 1 is probably false,
let us rename Part 1 itself _Conjecture 2_, which needs to be verified by other means.
We use the notations $p_I$ and $q_I$ to be $q$ and $p$ conditioned on
the subsampling index $I$, just like in the proof of the subsampling theorems (Claim 19 and 24).
Then

$$D_\lambda(q_I || p_I) = D_\lambda(p_I || q_I) 
\begin{cases}
\le D_\lambda(\mu_0 || \mu_1) = D_\lambda(\mu_1 || \mu_0), & I \in \mathcal I_\in\\
= D_\lambda(\mu_0 || \mu_0) = D_\lambda(\mu_1 || \mu_1) = 0 & I \in \mathcal I_\notin
\end{cases}$$

Since $p = |\mathcal I|^{-1} \sum_{I \in \mathcal I} p_I$ and
$q = |\mathcal I|^{-1} \sum_{I \in \mathcal I} q_I$ and
$|\mathcal I_\in| = r |\mathcal I|$, by Conjecture 1, we have Part 1.

**Remark in the proof**. As we can see here, instead of trying to prove Conjecture 1,
it suffices to prove a weaker version of it, by specialising on mixture of Gaussians,
in order to have a Claim 26 without any conjectural assumptions.
I have in fact posted the Conjecture on [Stackexchange](https://math.stackexchange.com/questions/3147963/an-inequality-related-to-the-renyi-divergence).

Now let us verify Part 2.
-->

Using Claim 27 and Example 1, we have

$$\begin{aligned}
G_\lambda(r \mu_1 + (1 - r) \mu_0 || \mu_0)) &= \sum_{j = 0 : \lambda} {\lambda \choose j} r^j (1 - r)^{\lambda - j} G_j(\mu_1 || \mu_0)\\
&=\sum_{j = 0 : \lambda} {\lambda \choose j} r^j (1 - r)^{\lambda - j} \exp(j (j - 1) / 2 \sigma^2). \qquad (9.5)
\end{aligned}$$

Denote by $n = \lceil \sigma^2 \rceil$. It suffices to show

$$\sum_{j = 0 : n} {n \choose j} (c_1 n^{- 1 / 2})^j (1 - c_1 n^{- 1 / 2})^{n - j} \exp(c_2 j (j - 1) / 2 n) \le C$$

Note that we can discard the linear term $- c_2 j / \sigma^2$ in the
exponential term since we want to bound the sum from above.

We examine the asymptotics of this sum when $n$ is large, and treat the
sum as an approximation to an integration of a function
$\phi: [0, 1] \to \mathbb R$. For $j = x n$, where $x \in (0, 1)$,
$\phi$ is thus defined as (note we multiply the summand with $n$ to
compensate the uniform measure on $1, ..., n$:

$$\begin{aligned}
\phi_n(x) &:= n {n \choose j} (c_1 n^{- 1 / 2})^j (1 - c_1 n^{- 1 / 2})^{n - j} \exp(c_2 j^2 / 2 n) \\
&= n {n \choose x n} (c_1 n^{- 1 / 2})^{x n} (1 - c_1 n^{- 1 / 2})^{(1 - x) n} \exp(c_2 x^2 n / 2)
\end{aligned}$$

Using Stirling\'s approximation

$$n! \approx \sqrt{2 \pi n} n^n e^{- n},$$

we can approach the binomial coefficient:

$${n \choose x n} \approx (\sqrt{2 \pi x (1 - x)} x^{x n} (1 - x)^{(1 - x) n})^{-1}.$$

We also approximate

$$(1 - c_1 n^{- 1 / 2})^{(1 - x) n} \approx \exp(- c_1 \sqrt{n} (1 - x)).$$

With these we have

$$\phi_n(x) \approx {1 \over \sqrt{2 \pi x (1 - x)}} \exp\left(- {1 \over 2} x n \log n + (x \log c_1 - x \log x - (1 - x) \log (1 - x) + {1 \over 2} c_2 x^2) n + {1 \over 2} \log n\right).$$

This vanishes as $n \to \infty$, and since $\phi_n(x)$ is bounded above
by the integrable function ${1 \over \sqrt{2 \pi x (1 - x)}}$ (c.f. the
arcsine law), and below by $0$, we may invoke the dominant convergence
theorem and exchange the integral with the limit and get

$$\begin{aligned}
\lim_{n \to \infty} &G_n (r \mu_1 + (1 - r) \mu_0 || \mu_0)) \\
&\le \lim_{n \to \infty} \int \phi_n(x) dx = \int \lim_{n \to \infty} \phi_n(x) dx = 0.
\end{aligned}$$

Thus we have that the generating function of the divergence variable
$L(r \mu_1 + (1 - r) \mu_0 || \mu_0)$ is bounded.

Can this be true for better orders

$$r \le c_1 \sigma^{- d_r},\qquad \lambda \le c_2 \sigma^{d_\lambda}$$

for some $d_r \in (0, 1]$ and $d_\lambda \in [2, \infty)$? If we follow
the same approximation using these exponents, then letting
$n = c_2 \sigma^{d_\lambda}$,

$$\begin{aligned}
{n \choose j} &r^j (1 - r)^{n - j} G_j(\mu_0 || \mu_1) \le \phi_n(x) \\
&\approx {1 \over \sqrt{2 \pi x (1 - x)}} \exp\left({1 \over 2} c_2^{2 \over d_\lambda} x^2 n^{2 - {2 \over d_\lambda}} - {d_r \over 2} x n \log n + (x \log c_1 - x \log x - (1 - x) \log (1 - x)) n + {1 \over 2} \log n\right).
\end{aligned}$$

So we see that to keep the divergence moments bounded it is possible to
have any $r = O(\sigma^{- d_r})$ for $d_r \in (0, 1)$, but relaxing
$\lambda$ may not be safe.

If we relax $r$, then we get

$$G_\lambda(r \mu_1 + (1 - r) \mu_0 || \mu_0) = O(r^{2 / d_r} \lambda^2 \sigma^{-2}) = O(1).$$

Note that now the constant $C$ depends on $d_r$ as well. Numerical
experiments seem to suggest that $C$ can increase quite rapidly as $d_r$
decreases from $1$. $\square$

In the following for consistency we retain $k$ as the number of epochs,
and use $T := k / r$ to denote the number of compositions / steps /
minibatches. With Claim 26 we have:

**Claim 28**. Assuming Conjecture 1 is true. Let $\epsilon, c_1, c_2 > 0$,
$r \le c_1 \sigma^{-1}$,
$T = {c_2 \over 2 C(c_1, c_2)} \epsilon \sigma^2$. then the DP-SGD with
subsampling rate $r$, and $T$ steps is $(\epsilon, \delta)$-dp for

$$\delta = \exp(- {1 \over 2} c_2 \sigma^2 \epsilon).$$

In other words, for

$$\sigma \ge \sqrt{2 c_2^{-1}} \epsilon^{- {1 \over 2}} \sqrt{\log \delta^{-1}},$$

we can achieve $(\epsilon, \delta)$-dp.

**Proof**. By Claim 26 and the Moment Composition Theorem
(Claim 22), for $\lambda = c_2 \sigma^2$, substituting
$T = {c_2 \over 2 C(c_1, c_2)} \epsilon \sigma^2$, we have

$$\mathbb P(L(p || q) \ge \epsilon) \le \exp(k C(c_1, c_2) - \lambda \epsilon) = \exp\left(- {1 \over 2} c_2 \sigma^2 \epsilon\right).$$

$\square$

**Remark**. Claim 28 is my understanding / version of
Theorem 1 in \[ACGMMTZ16\], by using the same proof technique. Here I
quote the original version of theorem with notions and notations altered
for consistency with this post:

> There exists constants $c_1', c_2' > 0$ so that for any
> $\epsilon < c_1' r^2 T$, DP-SGD is $(\epsilon, \delta)$-differentially
> private for any $\delta > 0$ if we choose

$$\sigma \ge c_2' {r \sqrt{T \log (1 / \delta)} \over \epsilon}. \qquad (10)$$

I am however unable to reproduce this version, assuming Conjecture 1 is
true, for the following reasons:

1.  In the proof in the paper, we have $\epsilon = c_1' r^2 T$ instead
    of \"less than\" in the statement of the Theorem. If we change it to
    $\epsilon < c_1' r^2 T$ then the direction of the inequality becomes
    opposite to the direction we want to prove:
    $$\exp(k C(c_1, c_2) - \lambda \epsilon) \ge ...$$

2.  The condition $r = O(\sigma^{-1})$ of Claim 26 whose
    result is used in the proof of this theorem is not mentioned in the
    statement of the proof. The implication is that (10) becomes an
    ill-formed condition as the right hand side also depends on
    $\sigma$.

Tensorflow implementation 
-------------------------

The DP-SGD is implemented in [TensorFlow
Privacy](https://github.com/tensorflow/privacy). In the following I
discuss the package in the current state (2019-03-11). It is divided
into two parts: [`optimizers`](https://github.com/tensorflow/privacy/tree/master/privacy/optimizers) which implements the actual differentially
private algorithms, and [`analysis`](https://github.com/tensorflow/privacy/tree/master/privacy/analysis) which computes the privacy guarantee.

The `analysis` part implements a privacy ledger that \"keeps a record
of all queries executed over a given dataset for the purpose of
computing privacy guarantees\". On the other hand, all the computation
is done in [`rdp_accountant.py`](https://github.com/tensorflow/privacy/blob/7e2d796bdee9b60dce21a82a397eefda35b0ac10/privacy/analysis/rdp_accountant.py).
At this moment, `rdp_accountant.py` only implements the computation of
the privacy guarantees for DP-SGD with Gaussian mechanism. In the
following I will briefly explain the code in this file.

Some notational correspondences: their `alpha` is our $\lambda$, their
`q` is our $r$, their `A_alpha` (in the comments) is our
$\kappa_{r N(1, \sigma^2) + (1 - r) N(0, \sigma^2)} (\lambda - 1)$, at
least when $\lambda$ is an integer.

-   The function `_compute_log_a` presumably computes the cumulants
    $\kappa_{r N(1, \sigma^2) + (1 - r) N(0, \sigma^2), N(0, \sigma^2)}(\lambda - 1)$.
    It calls `_compute_log_a_int` or `_compute_log_a_frac` depending on
    whether $\lambda$ is an integer.
-   The function `_compute_log_a_int` computes the cumulant using (9.5).
-   When $\lambda$ is not an integer, we can\'t use (9.5). I have yet to
    decode how `_compute_log_a_frac` computes the cumulant (or an upper
    bound of it) in this case
-   The function `_compute_delta` computes $\delta$s for a list of
    $\lambda$s and $\kappa$s using Item 1 of Claim 25 and return the
    smallest one, and the function `_compute_epsilon` computes epsilon
    uses Item 3 in Claim 25 in the same way.

In `optimizers`, among other things, the DP-SGD with Gaussian mechanism
is implemented in `dp_optimizer.py` and `gaussian_query.py`. See the
definition of `DPGradientDescentGaussianOptimizer` in `dp_optimizer.py`
and trace the calls therein.

At this moment, the privacy guarantee computation part and the optimizer
part are separated, with `rdp_accountant.py` called in
`compute_dp_sgd_privacy.py` with user-supplied parameters. I think this
is due to the lack of implementation in `rdp_accountant.py` of any
non-DPSGD-with-Gaussian privacy guarantee computation. There is already
[an issue on this](https://github.com/tensorflow/privacy/issues/23), so
hopefully it won\'t be long before the privacy guarantees can be
automatically computed given a DP-SGD instance.

Comparison among different methods 
----------------------------------

So far we have seen three routes to compute the privacy guarantees for
DP-SGD with the Gaussian mechanism:

1.  Claim 9 (single Gaussian mechanism privacy guarantee) -\> Claim 19
    (Subsampling theorem) -\> Claim 18 (Advanced Adaptive Composition
    Theorem)
2.  Example 1 (RDP for the Gaussian mechanism) -\> Claim 22 (Moment
    Composition Theorem) -\> Example 3 (Moment composition applied to
    the Gaussian mechanism)
3.  Claim 26 (RDP for Gaussian mechanism with specific magnitudes
    for subsampling rate) -\> Claim 28 (Moment Composition Theorem
    and translation to conventional DP)

Which one is the best?

To make fair comparison, we may use one parameter as the metric and set
all others to be the same. For example, we can

1.  Given the same $\epsilon$, $r$ (in Route 1 and 3), $k$, $\sigma$,
    compare the $\delta$s
2.  Given the same $\epsilon$, $r$ (in Route 1 and 3), $k$, $\delta$,
    compare the $\sigma$s
3.  Given the same $\delta$, $r$ (in Route 1 and 3), $k$, $\sigma$,
    compare the $\epsilon$s.

I find that the first one, where $\delta$ is used as a metric, the best.
This is because we have the tightest bounds and the cleanest formula
when comparing the $\delta$. For example, the Azuma and Chernoff bounds
are both expressed as a bound for $\delta$. On the other hand, the
inversion of these bounds either requires a cost in the tightness (Claim
9, bounds on $\sigma$) or in the complexity of the formula (Claim 16
Advanced Adaptive Composition Theorem, bounds on $\epsilon$).

So if we use $\sigma$ or $\epsilon$ as a metric, either we get a less
fair comparison, or have to use a much more complicated formula as the
bounds.

Let us first compare Route 1 and Route 2 without specialising to the
Gaussian mechanism.

**Warning**. What follows is a bit messy.

Suppose each mechanism $N_i$ satisfies
$(\epsilon', \delta(\epsilon'))$-dp. Let
$\tilde \epsilon := \log (1 + r (e^{\epsilon'} - 1))$, then we have the
subsampled mechanism $M_i(x) = N_i(x_\gamma)$ is
$(\tilde \epsilon, r \tilde \delta(\tilde \epsilon))$-dp, where

$$\tilde \delta(\tilde \epsilon) = \delta(\log (r^{-1} (\exp(\tilde \epsilon) - 1) + 1))$$

Using the Azuma bound in the proof of Advanced Adaptive Composition
Theorem (6.99):

$$\mathbb P(L(p^k || q^k) \ge \epsilon) \le \exp(- {(\epsilon - r^{-1} k a(\tilde\epsilon))^2 \over 2 r^{-1} k (\tilde\epsilon + a(\tilde\epsilon))^2}).$$

So we have the final bound for Route 1:

$$\delta_1(\epsilon) = \min_{\tilde \epsilon: \epsilon > r^{-1} k a(\tilde \epsilon)} \exp(- {(\epsilon - r^{-1} k a(\tilde\epsilon))^2 \over 2 r^{-1} k (\tilde\epsilon + a(\tilde\epsilon))^2}) + k \tilde \delta(\tilde \epsilon).$$

As for Route 2, since we do not gain anything from subsampling in RDP,
we do not subsample at all.

By Claim 23, we have the bound for Route 2:

$$\delta_2(\epsilon) = \exp(- k \kappa^* (\epsilon / k)).$$

On one hand, one can compare $\delta_1$ and $\delta_2$ with numerical
experiments. On the other hand, if we further specify
$\delta(\epsilon')$ in Route 1 as the Chernoff bound for the cumulants
of divergence variable, i.e.

$$\delta(\epsilon') = \exp(- \kappa^* (\epsilon')),$$

we have

$$\delta_1 (\epsilon) = \min_{\tilde \epsilon: a(\tilde \epsilon) < r k^{-1} \epsilon} \exp(- {(\epsilon - r^{-1} k a(\tilde\epsilon))^2 \over 2 r^{-1} k (\tilde\epsilon + a(\tilde\epsilon))^2}) + k \exp(- \kappa^* (b(\tilde\epsilon))),$$

where

$$b(\tilde \epsilon) := \log (r^{-1} (\exp(\tilde \epsilon) - 1) + 1) \le r^{-1} \tilde\epsilon.$$

We note that since
$a(\tilde \epsilon) = \tilde\epsilon(e^{\tilde \epsilon} - 1) 1_{\tilde\epsilon < \log 2} + \tilde\epsilon 1_{\tilde\epsilon \ge \log 2}$,
we may compare the two cases separately.

Note that we have $\kappa^*$ is a monotonously increasing function,
therefore

$$\kappa^* (b(\tilde\epsilon)) \le \kappa^*(r^{-1} \tilde\epsilon).$$

So for $\tilde \epsilon \ge \log 2$, we have

$$k \exp(- \kappa^*(b(\tilde\epsilon))) \ge k \exp(- \kappa^*(r^{-1} \tilde \epsilon)) \ge k \exp(- \kappa^*(k^{-1} \epsilon)) \ge \delta_2(\epsilon).$$

For $\tilde\epsilon < \log 2$, it is harder to compare, as now

$$k \exp(- \kappa^*(b(\tilde\epsilon))) \ge k \exp(- \kappa^*(\epsilon / \sqrt{r k})).$$

It is tempting to believe that this should also be greater than
$\delta_2(\epsilon)$. But I can not say for sure. At least in the
special case of Gaussian, we have

$$k \exp(- \kappa^*(\epsilon / \sqrt{r k})) = k \exp(- (\sigma \sqrt{\epsilon / k r} - (2 \sigma)^{-1})^2) \ge \exp(- k ({\sigma \epsilon \over k} - (2 \sigma)^{-1})^2) = \delta_2(\epsilon)$$

when $\epsilon$ is sufficiently small. However we still need to consider
the case where $\epsilon$ is not too small. But overall it seems most
likely Route 2 is superior than Route 1.

So let us compare Route 2 with Route 3:

Given the condition to obtain the Chernoff bound

$${\sigma \epsilon \over k} > (2 \sigma)^{-1}$$

we have

$$\delta_2(\epsilon) > \exp(- k (\sigma \epsilon / k)^2) = \exp(- \sigma^2 \epsilon^2 / k).$$

For this to achieve the same bound

$$\delta_3(\epsilon) = \exp\left(- {1 \over 2} c_2 \sigma^2 \epsilon\right)$$

we need $k < {2 \epsilon \over c_2}$. This is only possible if $c_2$ is
small or $\epsilon$ is large, since $k$ is a positive integer.

So taking at face value, Route 3 seems to achieve the best results.
However, it also has some similar implicit conditions that need to be
satisfied: First $T$ needs to be at least $1$, meaning

$${c_2 \over C(c_1, c_2)} \epsilon \sigma^2 \ge 1.$$

Second, $k$ needs to be at least $1$ as well, i.e.

$$k = r T \ge {c_1 c_2 \over C(c_1, c_2)} \epsilon \sigma \ge 1.$$

Both conditions rely on the magnitudes of $\epsilon$, $\sigma$, $c_1$,
$c_2$, and the rate of growth of $C(c_1, c_2)$. The biggest problem in
this list is the last, because if we know how fast $C$ grows then we\'ll
have a better idea what are the constraints for the parameters to
achieve the result in Route 3.

Further questions 
-----------------

Here is a list of what I think may be interesting topics or potential
problems to look at, with no guarantee that they are all awesome
untouched research problems:

1.  Prove Conjecture 1
2.  Find a theoretically definitive answer whether the methods in Part 1
    or Part 2 yield better privacy guarantees.
3.  Study the non-Gaussian cases, general or specific. Let $p$ be some
    probability density, what is the tail bound of
    $L(p(y) || p(y + \alpha))$ for $|\alpha| \le 1$? Can you find
    anything better than Gaussian? For a start, perhaps the nice tables
    of Rényi divergence in Gil-Alajaji-Linder 2013 may be useful?
4.  Find out how useful Claim 26 is. Perhaps start with computing
    the constant $C$ nemerically.
5.  Help with [the aforementioned
    issue](https://github.com/tensorflow/privacy/issues/23) in the
    Tensorflow privacy package.

References 
----------

-   Abadi, Martín, Andy Chu, Ian Goodfellow, H. Brendan McMahan, Ilya
    Mironov, Kunal Talwar, and Li Zhang. "Deep Learning with
    Differential Privacy." Proceedings of the 2016 ACM SIGSAC Conference
    on Computer and Communications Security - CCS'16, 2016, 308--18.
    <https://doi.org/10.1145/2976749.2978318>.
-   Erven, Tim van, and Peter Harremoës. "R\\'enyi Divergence and
    Kullback-Leibler Divergence." IEEE Transactions on Information
    Theory 60, no. 7 (July 2014): 3797--3820.
    <https://doi.org/10.1109/TIT.2014.2320500>.
-   Gil, M., F. Alajaji, and T. Linder. "Rényi Divergence Measures for
    Commonly Used Univariate Continuous Distributions." Information
    Sciences 249 (November 2013): 124--31.
    <https://doi.org/10.1016/j.ins.2013.06.018>.
-   Mironov, Ilya. "Renyi Differential Privacy." 2017 IEEE 30th Computer
    Security Foundations Symposium (CSF), August 2017, 263--75.
    <https://doi.org/10.1109/CSF.2017.11>.