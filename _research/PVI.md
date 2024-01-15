---
title: "Parabolic variational inequality"
collection: research
permalink: /research/PVI
# type: 
# venue: 
# date: 
# location: 
---
Caution! This page is under construction. I am adding more zeros and ones to the code and less confusion to the page. Please come back in a while. Thanks for your patience.

Let $\Omega$ be a bounded convex polygonal domain in $\mathbb{R}^2$, $T_F > 0$, and set $J = [0, T_F]$. 

For a given $f \in C(J; L^\infty(\Omega))$ and $\psi \in H^1(\Omega)$ with $\psi \leq 0$ a.e. on $\partial \Omega$, we consider the parabolic VI:

For all $t \in (0,T_F]$, find $u(t) \in K$ contained in $H^1_{0}(\Omega)$ such that

$
    \begin{array}{rrcrc}
        & ( \partial_t u, v-u ) + a(u, v-u)
        & \geq
        & ( f(t), v-u )
        & \forall
        & v \in K;
        & u(0)
        & =
        & u_0
    \end{array}
$

where $u_0 \in K$ is the given initial condition, $K$ is the constrained set with

$
    \begin{array}{rrc}
        & K
        & :=
        & \{v \in H^1_0(\Omega): v \geq \psi \ \text{a.e. in} \ \Omega\}
    \end{array}
$

and the bilinear forms $(\cdot, \cdot)$ and $a(\cdot, \cdot)$ are defined by

$
    \begin{array}{rrcccc}
        & (v, w)
        & =
        & \displaystyle \int_{\Omega} v \, w \, dx;
        & a(v,w)
        & = 
        & \displaystyle \int_{\Omega} \nabla v \cdot \nabla w \, dx
        & \forall \, v, w \in H^1(\Omega)
    \end{array}
$

By utilizing a symmetric dual-wind DG (DWDG) spatial discretization and a backward Euler temporal discretization, we propose a fully discrete scheme designed to solve the above time-dependent VI. In this [paper](https://doi.org/10.1016/j.jmaa.2020.123840), these methods were used to analyze elliptic VIs and sharp error estimates for linear and quadratic elements were derived. We show that numerical solutions tend to converge in $L^\infty(L^2)$ and $L^2(H^1)$-like energy norms as long as the exact solution meets certain regularity conditions. The analysis of these methods in the case of parabolic VIs is more subtle and delicate due to the use of discrete gradient operators and the low regularity of the time derivative, $\partial_t u$. To make the convergence analysis easier, we introduced a novel interpolation operator that combines the standard interpolation operator with a positive-preserving interpolation operator. We then show that the proposed method converges in space and time by $O(h + \tau^{\frac34}(log(\tau^{-1}))^{\frac14})$ in the suitable norm. Under strong assumptions, we improve the order of convergence to $O(h + \tau(log(\tau^{-1}))^{\frac12})$.

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