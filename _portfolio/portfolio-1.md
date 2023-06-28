---
title: "Turbulent mixing"
excerpt: "The mixing processes are very used in the industry. Typically, the mixing corresponds to the manipulation of a heterogeneous physical system in order to achieve homogeneity. 
In many cases in the industry, the mixing of components is due to turbulent phenomenon. Here Computational Fluid Dynamics is used to improve this process. 
<br/><img src='/images/case_mixing.gif'>"
collection: portfolio
---

## Introduction 

<p style="text-align: justify;">
The mixing processes are very used in the industry. Typically, the mixing corresponds to the manipulation of a heterogeneous physical system in order to achieve homogeneity. In many cases in the industry, the mixing of components is due to turbulent phenomenon.
The turbulent mixing is commonly described by two distinguished mixing scales. First is macro-mixing, which is characterized by the big scales of vortexes that essentially distribute the diverse particles in the domain of the flow. In this scale is the inertial effects that are important. Second is micro-mixing, where rates of molecular diffusivity of mass and momentum correlate with the time needed to diffuse the momentum into the target smallest turbulent flow eddies and, correspondingly, the mass into the target smallest concentration variation. Eventually, the effects can be also targeted at the molecular scale. 
Between both mixing situations, we can also define a meso-mixing, this is achieved by actuating typically on the turbulence. In this case, the turbulent kinetic energy, at the feed point to the mixer, must be enough to blend the added gas with the existing one.
</p>

## Govening Equations

### Continuity equation:

$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{u}) = 0$$

### Momentum equation:

$$\frac{\partial}{\partial t} (\rho \mathbf{u}) + \nabla \cdot (\rho \mathbf{u} \mathbf{u}) = -\nabla P + \mu \nabla^2 \mathbf{u} + \nabla \cdot \boldsymbol{\tau_{\text{turb}}}$$

### Turbulent kinetic energy equation:

$$\frac{\partial}{\partial t} (\rho k) + \nabla \cdot (\rho \mathbf{u} k) =\nabla \cdot \left[ \left( \mu + \frac{\mu_t}{\sigma_k} \right) \nabla k \right] + P_k - \rho \varepsilon$$

### Turbulent dissipation rate equation:

$$\frac{\partial}{\partial t} (\rho \varepsilon) + \nabla \cdot (\rho \mathbf{u} \varepsilon) = \nabla \cdot \left[ \left( \mu + \frac{\mu_t}{\sigma_\varepsilon} \right) \nabla \varepsilon \right] + C_{\varepsilon 1} \frac{\varepsilon}{k} P_k - C_{\varepsilon 2} \rho \frac{\varepsilon^2}{k}$$


<br>
<img src='/images/case_mixing.gif' style='width: 960px; height: auto;'>

<br/>[More information contact]<br/>
email: silvio.candido@ubi.pt