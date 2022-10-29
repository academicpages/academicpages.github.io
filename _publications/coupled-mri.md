---
title: "Coupled multirate infinitesimal GARK schemes for stiff systems with multiple time scales"
collection: publications
permalink: /publication/coupled-mri
excerpt: 'Initial value problems, Multirate, Implicit time integration'
venue: 'SIAM Journal on Scientific Computing'
date: '2020-01-01'
paperurl: 'https://arxiv.org/abs/1812.00808'
---
Traditional time discretization methods use a single timestep for the entire system of interest and can perform poorly when the dynamics of the system exhibits a wide range of time scales. Multirate infinitesimal step (MIS) methods (Knoth and Wolke, 1998) offer an elegant and flexible approach to efficiently integrate such systems. The slow components are discretized by a Runge-Kutta method, and the fast components are resolved by solving modified fast differential equations. Sandu (2018) developed the Multirate Infinitesimal General-structure Additive Runge-Kutta (MRI-GARK) family of methods that includes traditional MIS schemes as a subset. The MRI-GARK framework allowed the construction of the first fourth order MIS schemes. This framework also enabled the introduction of implicit methods, which are decoupled in the sense that any implicitness lies entirely within the fast or slow integrations. It was shown by Sandu that the stability of decoupled implicit MRI-GARK methods has limitations when both the fast and slow components are stiff and interact strongly. This work extends the MRI-GARK framework by introducing coupled implicit methods to solve stiff multiscale systems. The coupled approach has the potential to considerably improve the overall stability of the scheme, at the price of requiring implicit stage calculations over the entire system. Two coupling strategies are considered. The first computes coupled Runge-Kutta stages before solving a single differential equation to refine the fast solution. The second alternates between computing coupled Runge-Kutta stages and solving fast differential equations. We derive order conditions and perform the stability analysis for both strategies. The new coupled methods offer improved stability compared to the decoupled MRI-GARK schemes. The theoretical properties of the new methods are validated with numerical experiments.

[Preprint](https://arxiv.org/abs/1812.00808) / [Paper](https://epubs.siam.org/doi/abs/10.1137/19M1266952)
