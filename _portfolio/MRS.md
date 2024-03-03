---
title: "Swimming of a thin filament immersed in a viscous fluid using the Method of Regularized Stokeslet"
excerpt: "Final project for a special topics course titled _Boundary integral method_ of 22  <br/><img src='/images/RS1.gif'>"
collection: portfolio
---

# Method of Regularized Stokeslet
## Introduction
**This work was done as a part of the final project for a special topics course titled _Boundary integral method_ in the fall of 22 by [Professor Cortez](https://sse.tulane.edu/math/faculty/cortez)**

**Note:** Source codes are available in [RegularizedStokeslet](https://github.com/muddin21/RegularizedStokeslet).

The fluid flow problems in tiny scales are usually modeled  by the Stokes equations for incompressible flows 
  $$\mu \Delta \textbf{u}=\nabla p-\textbf{F}$$
  $$ \nabla \cdot \textbf{u}=0$$
where $\mu$ is the fluid viscosity, $p$ is the pressure, $\textbf{u}$ is the velocity, and $\textbf{F}$ is force. A fundamental solution of these equations is called a $Stokeslet$. The particular case of a single force $\mathbf{f}_0$ exerted at $\mathbf{x}_0$ results in a velocity  field given by
$$\mathbf{u}=\frac{\mathbf{f}_0}{8\pi\mu r}+\frac{(\mathbf{f_0\cdot(x-x_0)})(\mathbf{x-x_0})}{8
\pi\mu r}$$
where $r=||\mathbf{x-x_0}||$.

Note this solution is undefined at $r=0$ or $\mathbf{x=x}_0$.

However, the singularities can be eliminated through the function(usually known as blob function) $\phi_{\delta}(\mathbf{x})$ which is radially symmetric and satisfies that the integral over the space is one. So, considering $\mathbf{F}=\mathbf{f}_0\phi_{\delta}$ the singularity can be removed. The idea is due to [Professor Cortez](https://epubs.siam.org/doi/10.1137/S106482750038146X).

With the following choice of blob function:
$$\phi_\delta(r)=\dfrac{15\delta^4}{8\pi(r^2+\delta^2)^{\frac{7}{2}}}$$
the regularized stokeslet is 
$$\vec{u}(x)=\boldsymbol f_0 \dfrac{r^2+2\delta^2}{8\pi\mu(r^2+\delta^2)^{\frac{3}{2}}}+\dfrac{(\boldsymbol f_{0} .\boldsymbol x)\boldsymbol x}{8\pi\mu(r^2+\delta^2)^{\frac{3}{2}}}$$



## Swimming of filament immersed in a viscous fluid

We suppose the slender body is a sine wave,
$$y(s)=A\cos(\lambda s-2\pi t),z(s)=0$$
and $x(s)$ such that $\sqrt{(x')^2+(y')^2}=1$,
and the curvature 
$$\kappa=\frac{x''y'-y''x'}{(\sqrt{(x')^2+(y')^2})^{3}}=x''y'-y''x'=\frac{-y''}{\sqrt{1-(y')^2}}$$
To compute the forces, we've utilized the approach discussed in the article [A computational model of aquatic animal locomotion
](https://www.sciencedirect.com/science/article/abs/pii/0021999188901581).

Once we've computed forces at each point, we can calculate velocity. Then, the locomotion of filament can be found by solving $\dfrac{d\boldsymbol X}{dt}=\boldsymbol u$. To solve this we have used the forward Euler method(other methods like RK can also be used).

It's worth mentioning that this model has been utilized for various problems; especially those related to the [motility of hyper-activated mammalian sperm](https://www.sciencedirect.com/science/article/abs/pii/S0022519314001635). 
