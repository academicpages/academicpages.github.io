---
title: "Elliptic optimal control problem with control constraints"
collection: research
permalink: /research/EOCP
# type: 
# venue: 
# date: 
# location: 
---
Caution! This page is under construction. I am adding more zeros and ones to the code and less confusion to the page. Please come back in a while. Thanks for your patience.

Let $\Omega$ contained in \mathbb{R}^2$ be a bounded convex polygonal domain. 

Let $y_d \in L^2(\Omega)$ be the desired state, $u_a, u_b \in \mathbb{R} \cup \{\pm \infty\}$ such that $u_a < u_b$ be given and $\beta > 0$ be a regularization parameter. The elliptic optimal control problem with control constraints in given by

$$
    \begin{array}{rrc}
        & \min \limits_{(y,u) \in H^1_{0}(\Omega) \times U_{ad}} 
        & =
        & f
    \end{array}
$$

where $U_{ad}$ := {$v \in L^2(\Omega): u_a \leq v \leq u_b$} is a closed convex set, $y$ is the "state" variable, and $u$ is the "control" variable. The constraints on the control variable $u$ are called box constraints. When $u_a = -\infty$ and $u_b = \infty$, observe that $U_{ad} = L^2(\Omega)$. Then, we have an optimization problem with no inequality constraints, which is a special case of the optimization problem under consideration.

<!-- {% include CD_pic.html %}     -->

In this project, we aim to obtain an optimization problem with equality and inequality-type constraints in finite dimensions. To do so, we replace the infinite-dimensional admissible set, the infinite-dimensional functional, and the infinite-dimensional Laplacian operator with a finite-dimensional admissible set, a finite-dimensional functional, and a discrete Laplacian operator, respectively. Note that the finite-dimensional admissible set is spanned by the discontinuous piecewise polynomials with respect to the underlying triangulation of the polygonal domain $\Omega \subset \mathbb{R}^2$ while the discrete Laplacian operator is constructed using the DWDG method. The discrete KKT system is derived using this finite-dimensional optimization problem, and the PDAS algorithm is then utilized to find the optimal solution in finite dimensions that satisfies the discrete KKT system. Later, we show that this finite-dimensional optimal solution eventually converges to an infinite-dimensional optimal solution as we refine the triangulation of the polygonal domain $\Omega$. Additionally, we establish the order of convergence in $L^2$ and energy norms.

Here is a lecture on brief introduction to PDE constrained optimization by [Dr. Stegan Volkwein](https://www.math.uni-konstanz.de/numerik/personen/volkwein/)
{% include introPDECO_video.html %}    

<!-- <h4>Numerical Experiment - 1: Continuous Solution</h4>
$$
\Omega = (1,3)^2,\quad \boldsymbol{\rho} = \langle x_1,x_2 \rangle, \quad \epsilon = 10^{-9} \quad u(x_1,x_2) = \dfrac{x_2}{x_1}
$$

{% include CD_NumEx1_pics.html %}
{% include CD_NumEx1_table.html %}

<h4>Numerical Experiment - 2: Boundary Layer <a href="https://www.jstor.org/stable/25663174">[B Ayuso, LD Marini (2009)]</a></h4>
$$
\Omega = (0,1)^2,\quad \boldsymbol{\rho} = \langle 1,1 \rangle, \quad \epsilon = 10^{-9} 
$$
$$
u(x_1,x_2) = x_1 + x_2(1-x_1) + \dfrac{\exp \left(\dfrac{-1}{\epsilon} \right)-\exp \left(\dfrac{(x_1-1)(1-x_2)}{\epsilon} \right)}{1-\exp \left(\dfrac{-1}{\epsilon} \right)}
$$
{% include CD_NumEx2_pics.html %}
{% include CD_NumEx2_table.html %} -->