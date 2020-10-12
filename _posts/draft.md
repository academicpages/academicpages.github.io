---
Approximate DP and smoothed-DP
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
-   Vadhan, Salil. "The Complexity of Differential Privacy." In
    Tutorials on the Foundations of Cryptography, edited by Yehuda
    Lindell, 347--450. Cham: Springer International Publishing, 2017.
    <https://doi.org/10.1007/978-3-319-57048-8_7>.

TLDR
-------------
Clarify some (almost) equivalent notions of differential privacy.

Approximate differential privacy 
--------------------------------
We begin with the definition of $(\epsilon,\delta)$-differential privacy,
which has a lot of nice properties, including allowing us to apply the 
Gaussian mechanism.

**Definition**. A mechanism $M: X \to  Y$ is said to be
$(\epsilon, \delta)$*-differentially private* if for all $x, x' \in X$
with $x \sim x' $ and for all measureable 
$S \subset Y$,

$$\mathbb P(M(x) \in S) \le e^\epsilon P(M(x') \in S) + \delta. $$

Note that we make the implicit assumption $M(x) = M(x') $ in the above equation,
as explained in the [previous post](/posts/2020/10/02/).
We make this implicit assumption from now onwards.

### Indistinguishability 

