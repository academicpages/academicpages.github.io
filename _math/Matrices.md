---
title: "Matrices"
collection: teaching
type: "Undergraduate course"
permalink: /math/matrices
---
Geometric exposition of matrices...


A linear map $f(x)$ is one that has the property that $f(\alpha_1 x_1 + \alpha_2 x_2) = \alpha_1f(x_1) + \alpha_2 f(x_2)$.   Intuitively, one can think of linear function as one you can apply to each little bit of the argument separately and then add them all up and get the right answer.   If $x \in \mathbb{R}^n$ lives in a vector space with a basis given by the columns of the matrix $V \in \mathbb{R}^{n \times n}$
$$
V =
\begin{bmatrix}
| &  & | \\
v_1 & \dots & v_n \\
| &  & | \\
\end{bmatrix}
$$
then one can represent the linear map $f(x)$ by how it acts on each of the basis vectors.  Indeed if $x = \sum_k \alpha_k v_k$, or in vector notation
$$
x=V\alpha
$$

