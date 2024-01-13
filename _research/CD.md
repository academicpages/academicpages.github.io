---
title: "Steady convection-diffusion equation in the convection dominated regime"
collection: research
permalink: /research/CD
# type: 
# venue: 
# date: 
# location: 
---
Given a convex polygonal domain ($\Omega$) in $\mathbb{R}^2$, the convection-diffusion (CD) equation is:

$$
    \begin{array}{rrccccc}
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

<div style="text-align: center;">
    <figure>
        <img src="/research/figures/Diffusion.gif"
            style="width:100%"
            alt="Animated image showing a diffusion process">
        <figcaption>An illustration of the diffusion process</figcaption>
    </figure>
</div>
<div style="text-align: center;">
    <figure>
        <img src="/research/figures/Convection.png"
            style="width:100%"
            alt="Image showing a convection process">
        <figcaption>A Figure showing the convection process</figcaption>
    </figure>
</div>
<div style="text-align: center;">
    <figure>
        <img src="/research/figures/CD.png"
            style="width:100%"
            alt="Image showing a convection and diffusion process">
        <figcaption>
            A depiction of the convection and the diffusion processes
            <a href="https://en.wikipedia.org/wiki/P%C3%A9clet_number">Source: Wikipedia</a>
        </figcaption>
    </figure>
</div>
    
<!-- ![Diffusion](/research/figures/Diffusion.gif)
![CD](/research/figures/CD.png)
![Convection](/research/figures/Convection.png) -->

In this project, we propose and analyze a numerically stable and convergent scheme for Convection-Diffusion (CD) equation in the convection-dominated regime ($\epsilon \approx 0$). Since the standard CG-FEM for the CD equation causes spurious oscillations, the DG schemes are extremely appropriate for the CD equation. We choose to follow a novel discontinuous Galerkin finite element differential calculus framework and approximate the infinite-dimensional operators in the CD equation by the finite-dimensional operators. Specifically, we construct the numerical method by using the DWDG formulation for the diffusive term and the formulation that uses the average discrete gradient operator for the convective term along with upwinding. We establish the order of convergence of the error assuming the $H^2$ regularity on the exact solution, and provide several numerical tests to demonstrate the theoretical order of convergence of the proposed formulation.

<h4>Numerical Experiment - 1: Continuous Solution</h4>
$$
\Omega = (1,3)^2,\quad \boldsymbol{\rho} = \langle x_1,x_2 \rangle, \quad \epsilon = 10^{-9} \quad u(x_1,x_2) = \dfrac{x_2}{x_1}
$$

<div style="text-align: center;">
    <figure>
        <img src="/research/figures/u_ex1.png"
            style="width:50%"
            alt="exact solution for numerical experiment 1">
        <figcaption>Exact Solution</figcaption>
    </figure>
</div>
<div style="text-align: center;">
    <figure>
        <img src="/research/figures/u_h_ex1.png"
            style="width:50%"
            alt="numerical solution for numerical experiment 1">
        <figcaption>Numerical Solution</figcaption>
    </figure>
</div>

{% include CD_NumEx1.html %}
<table>
  <tr>
    <th>h</th>
    <th>DOF</th>
    <th>$L_2$ Error</th>
    <th>Rate</th>
    <th>$||| \cdot |||$ Error</th>
    <th>Rate</th>
  </tr>
  <tr>
    <td>1/2</td>
    <td>12</td>
    <td>1.20e-01</td>
    <td>--</td>
    <td>2.84e-01</td>
    <td>--</td>
  </tr>
  <tr>
    <td>1/4</td>
    <td>48</td>
    <td>4.20e-02</td>
    <td>1.52</td>
    <td>9.86e-02 </td>
    <td>1.53-</td>
  </tr>
  <tr>
    <td>1/8</td>
    <td>192</td>
    <td>9.95e-03</td>
    <td>2.08</td>
    <td>3.35e-02 </td>
    <td>1.53-</td>
  </tr>
  <tr>
    <td>1/16</td>
    <td>768</td>
    <td>2.41e-03</td>
    <td>2.04</td>
    <td>1.15e-02 </td>
    <td>1.53-</td>
  </tr>
  <tr>
    <td>1/32</td>
    <td>3072</td>
    <td>6.01e-04</td>
    <td>2.01</td>
    <td>3.97e-03 </td>
    <td>1.53-</td>
  </tr>
  <tr>
    <td>1/64</td>
    <td>12288</td>
    <td>1.50e-04</td>
    <td>2.00</td>
    <td>1.38e-03 </td>
    <td>1.53-</td>
  </tr>
   <tr>
    <td>1/128</td>
    <td>49152</td>
    <td>3.73e-05 </td>
    <td>2.01</td>
    <td>4.86e-04 </td>
    <td>1.53-</td>
  </tr>
</table>