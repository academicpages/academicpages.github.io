---
The definition of differential privacy, explicitly
---

This is the first part of a series of articles where I attempt to clarify some mathematical notions of differential privacy. 

It serves mainly as a study note for myself. And regarding to learning the math behind differential privacy, I have benefited greatly from reading this [post](https://ypei.me/posts/2019-03-13-a-tail-of-two-densities.html). 

I will try to explain the notions used as detailed as possible, but
do not expect this article to be self-contained. 
Please refer to the original [post](https://ypei.me/posts/2019-03-13-a-tail-of-two-densities.html) for a
more complete description of the topic.

TLDR
-------------
This article is a short one just to clarify the very definition of differential privacy.

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

I think that the above interpretation is wrong, and I think it is implicitly assumed that two probabilities are compared on the same support (maybe this is a trivial assumption for a mathematician or computer scientist). 

The following, which is a more explicit way of rewriting Equation (1) is more comfortable to me:
$$\mathbb P(M(x) = r ) \le e^\epsilon P(M(x') = r ), \qquad (2)$$
where $r \in S$.

Many references prove that the Laplace mechanism is a differentially private mechanism using Equation (2) implicitly.

**Definition**. The *Laplace distribution* over $\mathbb R$
with parameter $b > 0$ has probability density function

$$f_{\text{Lap}(b)}(x) = {1 \over 2 b} e^{- {|x| \over b}}.$$

**Definition**. Let $d = 1$. The *Laplace mechanism* is
defined by

$$M(x) = f(x) + \text{Lap}(b).$$

**Claim**. The Laplace mechanism with

$$b \ge \epsilon^{-1} S_f \qquad (1.5)$$

is $\epsilon$-dp.

**Proof**. Let $p$ and $q$ be the laws
of $M(x)$ and $M(x')$ respectively.

$${p (y) \over q (y)} = {f_{\text{Lap}(b)} (y - f(x)) \over f_{\text{Lap}(b)} (y - f(x'))} = \exp(b^{-1} (|y - f(x')| - |y - f(x)|))$$

Using triangular inequality $|A| - |B| \le |A - B|$ on the right hand
side, we have

$${p (y) \over q (y)} \le \exp(b^{-1} (|f(x) - f(x')|)) \le \exp(\epsilon)$$

where in the last step we use the condition (1.5). $\square$

I therefore suspect that Equation (2) is correct, and is an explicit way of writing Equation (1).