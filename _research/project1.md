---
title: "Steady convection-diffusion equation in the convection dominated regime"
collection: research
---
In this project, we propose and analyze a numerically stable and convergent scheme for Convection-Diffusion (CD) equation in the convection-dominated regime. Since the
standard CG-FEM for the CD equation causes spurious oscillations, the DG schemes are extremely appropriate for the CD equation. We choose to follow a novel discontinuous Galerkin finite element differential calculus framework and approximate the infinite-dimensional operators in the CD equation by the finite-dimensional operators. Specifically, we construct the numerical method by using the DWDG formulation for the diffusive term and the formulation that uses the average discrete gradient operator for the convective term along with upwinding. We establish the order of convergence of the error assuming the $H^2$ regularity on the exact solution, and provide several numerical tests to demonstrate the theoretical order of convergence of the proposed formulation.

Given a convex polygonal domain ($\Omega$) in $\mathbb{R}^2$, the convection-diffusion (CD) equation is
$$
\begin{equation}
    %\left\{
    \begin{array}{rrccccc}
         & - \epsilon \Delta u + \brho \cdot \nabla u
         & =
         & f
         & \text{in}
         & \Omega                                      \\
         & u
         & =
         & g
         & \text{on}
         & \p \Omega
    \end{array}
    %\right 
\end{equation}
$$
where  $\epsilon > 0$ is a constant, $\brho$ is a vector field in $[W^{1,\infty}(\Omega)]^2$, $f \in L_2(\Ome)$ is a given source function and the function $g \in L^{1}(\p \Omega)$. The unknown scalar function $u$ is some physical quantity that is being transported in the direction $\brho$ along with diffusive effects determined by $\epsilon$. Roughly speaking, $-\epsilon \Delta$ models the diffusion of $u$ while $\brho \cdot \nabla$ models the convection of $u$ in the domain $\Ome$.
