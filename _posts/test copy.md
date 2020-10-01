---
Differential privacy, explicitly
---

This is the first part of a series of articles where I will clarify some mathematical notions of differential privacy. 
Specifically, the relations between $(\epsilon, \delta)$-differential privacy, $(\epsilon, \delta)$-indistinguishability,
 and a claim to be used to prove composition theorems.

I have benefited greatly from reading this post. 

In fact, one personal purpose of this article is to clarify some parts 
of the post which are not trivial to me.

While I will try to explain all notions to be used here,
this article is not meant to be self-contained. 
Please refer to the original post for a
more complete description of the topic.

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

**Definition (Differential
Privacy)**. A mechanism $M$ is called $\epsilon$*-differential privacy*
($\epsilon$-dp) if it satisfies the following condition: for all
$x, x' \in X$ with $d(x, x') = 1$, and for all measureable set
$S \subset \mathbb R^n$,

$$\mathbb P(M(x) \in S) \le e^\epsilon P(M(x') \in S). \qquad (1)$$

This is one part that confuses me. This equation looks to me that for any output of $M(x)$ and $M(x')$, even for the case $M(x) \neq M(x')$, differential privacy is achieved when $\mathbb P(M(x)) \le e^\epsilon P(M(x'))$.

I think that the above interpretation is wrong, and I think it is implicitly assumed that two probabilities are compared on the same support (maybe this is a trivial assumption for mathematicians). 

The following, which is a more explicit way of rewriting Equation (1) is more comfortable to me:
$$\mathbb P(M(x) = r \in S) \le e^\epsilon P(M(x') = r \in S). \qquad (2)$$


Approximate differential privacy 
--------------------------------

Unfortunately, $\epsilon$-dp does not apply to the most commonly used
noise, the Gaussian noise. To fix this, we need to relax the definition
a bit.

**Definition**. A mechanism $M$ is said to be
$(\epsilon, \delta)$*-differentially private* if for all $x, x' \in X$
with $d(x, x') = 1$ and for all measureable $S \subset \mathbb R^d$

$$\mathbb P(M(x) \in S) \le e^\epsilon P(M(x') \in S) + \delta. \qquad (2)$$