---
title: "Steady convection-diffusion equation in the convection dominated regime"
collection: research
permalink: /research/CD
# type: 
# venue: 
# date: 
# location: 
---
Given a convex polygonal domain $\Omega$ in $\mathbb{R}^2$ with Lipschitz boundary $\partial \Omega$, the convection-diffusion (CD) equation is:

$$
    \begin{array}{rrcccccccc}
        & - \epsilon \Delta u + \boldsymbol{\rho} \cdot \nabla u
        & =
        & f
        & \text{in}
        & \Omega \\
        & u
        & =
        & g
        & \text{on}
        & \partial \Omega
    \end{array}
$$

where  $\epsilon > 0$ is a constant, $\boldsymbol{\rho}$ is a vector field in $[W^{1,\infty}(\Omega)]^2$, $f \in L_2(\Omega)$ is a given source function and the function $g \in L^{1}(\partial \Omega)$. The unknown scalar function $u$ is some physical quantity that is being transported in the direction $\boldsymbol{\rho}$ along with diffusive effects determined by $\epsilon$. Roughly speaking, $-\epsilon \Delta$ models the diffusion of $u$ while $\boldsymbol{\rho} \cdot \nabla$ models the convection of $u$ in the domain $\Omega$.

{% include /include_research/CD/CD_pic.html %}    

In this project, we propose and analyze a numerically stable and convergent scheme for Convection-Diffusion (CD) equation in the convection-dominated regime ($\epsilon \approx 0$). Since the standard CG-FEM for the CD equation causes spurious oscillations, the DG schemes are extremely appropriate for the CD equation. We choose to follow a novel discontinuous Galerkin finite element differential calculus framework and approximate the infinite-dimensional operators in the CD equation by the finite-dimensional operators. Specifically, we construct the numerical method by using the dual-wind DG (DWDG) formulation for the diffusive term and the formulation that uses the average discrete gradient operator for the convective term along with upwinding. We establish the order of convergence of the error assuming the $H^2$ regularity on the exact solution, and provide several numerical tests to demonstrate the theoretical order of convergence of the proposed formulation.

<h3>Numerical Experiment - 1: Continuous Solution</h3>
$$
\Omega = (1,3)^2,\quad \boldsymbol{\rho} = \langle x_1,x_2 \rangle, \quad \epsilon = 10^{-9} \quad u(x_1,x_2) = \dfrac{x_2}{x_1}
$$

{% include /include_research/CD/CD_NumEx1_pics.html %}
{% include /include_research/CD/CD_NumEx1_table.html %}

<h3>Numerical Experiment - 2: Boundary Layer</h3>
<h4><a href="https://www.jstor.org/stable/25663174">[B Ayuso, LD Marini (2009)]</a></h4>
$$
\Omega = (0,1)^2,\quad \boldsymbol{\rho} = \langle 1,1 \rangle, \quad \epsilon = 10^{-9} 
$$
$$
u(x_1,x_2) = x_1 + x_2(1-x_1) + \dfrac{\exp \left(\dfrac{-1}{\epsilon} \right)-\exp \left(\dfrac{(x_1-1)(1-x_2)}{\epsilon} \right)}{1-\exp \left(\dfrac{-1}{\epsilon} \right)}
$$
{% include /include_research/CD/CD_NumEx2_pics.html %}
{% include /include_research/CD/CD_NumEx2_table.html %}