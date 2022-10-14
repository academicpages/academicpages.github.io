---
date: 2022-10-10
tags:
- stream
- nn
title: Siamese network and triplet loss
---

Define distance as the norm between the two encodings: $d(x_i, x_j) = ||f(x_i) - f(x_j)||^2$.

Goal: learn parameters so that
- $x_i, x_j$ are the same person -> $d(x_i, x_j)$ is small
- $x_i, x_j$ are the different people -> $d(x_i, x_j)$ is large

How to train? Triplet loss
- Anchor $A$
- Positive $P$
- Negative $N$
- Want:
	- $d(A, P) \leq d(A, N)$
	- $d(A, P) - d(A, N) \leq 0$
	- This can be satisfied trivially with $d(*) = 0$.
	- To prevent trivial solution, require the difference larger than a margin. $d(A, P) - d(A, N) + \alpha \leq 0$.
	- End up with Triplet loss $\mathcal L(A, P, N) = max(d(A, P) - d(A, N) + \alpha, 0)$