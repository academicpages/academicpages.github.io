---
title: 'Anderson Acceleration for Fixed-Point Iteration'
date: 2022-4-13
permalink: /posts/anderson-acceleration
toc: true
---

In the first ever post on my website (yay!), I will introduce you to the Anderson acceleration method in fixed-point iteration. It accompanies our paper [_"Accelerating Federated Edge Learning"_](https://joshnguyen.net/publication/2021-08-FedAA). The code can be found [this repository](https://github.com/joshnguyen99/anderson_acceleration).

## Fixed-Point Iteration

Let $g: \mathbb{R}^d \rightarrow \mathbb{R}^d$ be an affine function of the form $g(x) = Ax + b$, where $A \in \mathbb{R}^{d \times d}$ and $b \in \mathbb{R}^d$. We would like to find a _fixed point_ of $g$, which is a vector $x^\ast$ such that $g(x^\ast) = x^\ast$. The reason why $x^\ast$ is called a fixed point is because applying $g$ to $x^\ast$ doesn't change itself.

The analytical solution to this problem is $x^\ast = -(A - I)^{-1} b$, but there may be several issues to this. First, $A - I$ may not be invertible, in which case we need to use least squares to find its pseudoinverse. Second, even if it is invertible, the cost of solving for $x^\ast$ is $O(d^3)$, where $d$ is the dimensionality $d$, which is very costly in high dimensions.

The common numerical method to solve for a fixed point of $g$ is the _fixed-point iteration_. Start with a randomly chosen $x_0$ and iteratively apply $g$ to it:

$$ 
\label{eqn:fixed_point}
x_{t+1} = g(x_t),
$$

until $\lVert g(x_{t+1}) - x_{t+1} \rVert \lt \epsilon$ for some predetermined precision $\epsilon$. In order for this to converge, we want to ensure that $g$ is a contraction mapping, that is, there exists an $L \in [0, 1)$ such that $\forall x, x' \in \mathbb{R}^d, \lVert g(x) - g(x') \rVert \leq L \lVert x - x' \rVert$. This can be achieved when the _spectral radius_ of $A$ is less than $1$.

We can prove that to achieve a precision of $\epsilon$, we need to apply $O\left(\kappa \log \frac{1}{\epsilon} \right)$ iterations, where $\kappa$ is the _condition number_ of $A$, which is the ratio between $A$'s largest and smallest singular values.

## Anderson Acceleration

Fixed-point iteration could converge very slowly. The reason is that the condition number of $A$ could be large. (In real datasets, $\kappa$ could be greater than $10^6$.) Anderson acceleration (AA) can speed up convergence considerably. Here's how it works.

Define $f_t = g(x_t) - x_t$ to be the _residual_ at iteration $t$. To find $x_{t+1}$, consider the space spanned by the previous $m_t+1$ iterates $\\{x_{t - m_t}, x_{t - m_t + 1}, \ldots, x_t \\}$, where $m_t$ is the _window size_ you can choose. To find the next iterate, we consider a linear combination of these previous vectors:

$$
\label{eqn:linear_comb}
\bar{x}_t = \sum_{i=1}^{m_t} \alpha_i^{(t)} x_{t - m_t + i},
$$

and find $\alpha^{(t)} \in \mathbb{R}^{m_t + 1}$ such that $$\| g(\bar{x}_t) - \bar{x}_t \|$$ is minimized. So what are doing here to use the previous iterates to better guide us to the solution. You can check the paper for a full derivation, but the $\alpha^{(t)}$ we should choose is

$$
\label{eqn:alpha}
\alpha^{(t)} = \frac{(F_t^\top F_t)^{-1}\boldsymbol{1}}{\boldsymbol{1}^\top (F_t^\top F_t)^{-1} \boldsymbol{1}},
$$

where $F_t = \left[ f_{t- m_t},\ldots, f_{t} \right] \in \mathbb{R}^{d \times (m_t + 1)}$ is the matrix of all residuals, $\boldsymbol{1}$ is the $(m_t + 1)$-dimensional column vector of all ones.

After finding $\alpha^{(t)}$, we set the new iterate to

$$
\label{eqn:extrapolate}
x_{t+1} = \beta \sum_{i=0}^{m_t} \alpha_i^{(t)} g(x_{t - m_t + i}) + (1 - \beta) \sum_{i=0}^{m_t} \alpha_i^{(t)} x_{t - m_t + i},
$$

where $\beta \in [0, 1]$ is a predetermined _mixing parameter_.
### "Regularization"

You can see in the paper that in Algorithm 1, we actually set $\alpha^{(t)}$ as

$$
\label{eqn:alpha_reg}
\alpha^{(t)} = \frac{(F_t^\top F_t + \lambda I)^{-1}\boldsymbol{1}}{\boldsymbol{1}^\top (F_t^\top F_t + \lambda I)^{-1} \boldsymbol{1}},
$$ 

which is slightly different from \eqref{eqn:alpha}. The reason is we want to solve the regularized version of the problem

$$
\underset{\alpha^{(t)}: \boldsymbol{1}^\top \alpha^{(t)} = 1}{\min} \| g(\bar{x}_t) - \bar{x}_t \|^2 + \lambda \| \alpha^{(t)} \|^2
$$

for stability (Section II). Without regularization ($\lambda = 0$), we recover \eqref{eqn:alpha}.

### The algorithm

Anderson acceleration is very similar to the vanilla fixed-point iteration: start with some $x_0$. In each iteration, find $\alpha^{(t)}$ like above, and _extrapolate_ from the $m_t + 1$ previous iterates to find the next iterate $x_{t+1}$. In other words, in each iteration $t$:
- Calculate $g(x_t)$.
- Compute the residual: $f_t = g(x_t) - x_t$.
- Form the residual matrix: $F_t = \left[ f_{t- m_t},\ldots, f_{t} \right]$.
- Solve for $\alpha^{(t)}$ according to \eqref{eqn:alpha_reg}.
- Extrapolate from $m_t + 1$ previous iterates according to \eqref{eqn:extrapolate}.

## Python Implementation of AA

You can find the implementation in the [aa.py](https://github.com/joshnguyen99/anderson_acceleration/blob/main/aa.py) file. The `AndersonAcceleration` class should be in instantiated with the `window_size` ($m_t$, defaulted to $5$) and `reg` ($\lambda$, defaulted to 0). Here's an example.

```python
>>> import numpy as np
>>> from aa import AndersonAcceleration
>>> acc = AndersonAcceleration(window_size=2, reg=0)
>>> x = np.random.rand(100)  # some iterate
>>> x_acc = acc.apply(x)     # accelerated from x
```

You will need to apply $g$ to $x_t$ first. The result $g(x_t)$ should be the input to `acc.apply`, which will solve for $\alpha^{(t)}$ and extrapolate to find $x_{t+1}$. See [the repository](https://github.com/joshnguyen99/anderson_acceleration) for more detail.

## Some numerical examples

### Minimizing a convex quadratic objective

We will minimize a strictly convex quadratic objective. Check [`quadratic_example.ipynb`](https://github.com/joshnguyen99/anderson_acceleration/blob/main/quadratic_example.ipynb) for more detail. The below plot shows the _optimality gap_ between $f(x_t)$ and $f(x^\ast)$ over $t$. AA with a window size of 2 converges much faster than the vanilla gradient descent (GD).

<p align="center">
    <img src="https://github.com/joshnguyen99/anderson_acceleration/raw/main/AA_GD_quadratic.png" title="Comparing GD to AA on a quadratic objective with very high condition number">
</p>

### Minimizing a convex non-quadratic objective

We will minimize the $\ell_2$-regularized cross entropy loss function for logistic regression. Check [`logistic_regression_example.ipynb`](logistic_regression_example.ipynb) for more detail. Similarly, AA is much more favorable than the vanilla GD when optimizing this objective.

<p align="center">
    <img src="https://github.com/joshnguyen99/anderson_acceleration/raw/main/AA_GD_logistic_regression.png" title="Comparing GD to AA on a non-quadratic objective with very high condition number">
</p>