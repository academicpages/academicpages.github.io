---
(Almost) Equivalent notions of differential privacy
---


This is part of a series of articles where I attempt to clarify some mathematical notions of differential privacy. 

It serves mainly as a study note for myself, and therefore contains potentially a lot of mistakes and biases ;)

Regarding to learning the math behind differential privacy, I have benefited greatly from reading this [post](https://ypei.me/posts/2019-03-13-a-tail-of-two-densities.html). 

I will try to explain the notions used as detailed as possible, but
do not expect this article to be self-contained. 
Please refer to the original [post](https://ypei.me/posts/2019-03-13-a-tail-of-two-densities.html) for a
more complete description of the topic.

Other useful study materials include:

-   Dwork, Cynthia, and Aaron Roth. "The Algorithmic Foundations of
    Differential Privacy." Foundations and Trends® in Theoretical
    Computer Science 9, no. 3--4 (2013): 211--407.
    <https://doi.org/10.1561/0400000042>.
-   Murtagh, Jack, and Salil Vadhan. "The Complexity of Computing the
    Optimal Composition of Differential Privacy." In Theory of
    Cryptography, edited by Eyal Kushilevitz and Tal Malkin,
    9562:157--75. Berlin, Heidelberg: Springer Berlin Heidelberg, 2016.
    <https://doi.org/10.1007/978-3-662-49096-9_7>.

TLDR
-------------
Clarify some (almost) equivalent notions of differential privacy.
"Almost" means sufficient or necessary conditions for differential privcay.

Approximate differential privacy 
--------------------------------

Unfortunately, $\epsilon$-dp does not apply to the most commonly used
noise, the Gaussian noise. To fix this, we need to relax the definition
a bit.

**Definition**. A mechanism $M$ is said to be
$(\epsilon, \delta)$*-differentially private* if for all $x, x' \in X$
with $d(x, x') = 1$ and for all measureable $S \subset \mathbb R^d$

$$\mathbb P(M(x) \in S) \le e^\epsilon P(M(x') \in S) + \delta. \qquad (2)$$