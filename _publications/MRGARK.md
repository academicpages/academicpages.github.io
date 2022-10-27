---
title: "Design of High-Order Decoupled Multirate GARK Schemes"
collection: publications
permalink: /publication/MRGARK
venue: 'SIAM Journal on Scientific Computing '
paperurl: 'https://arxiv.org/abs/1804.07716'
date: '2019-01-01'
excerpt: 'multirate integration, generalized additive Runge--Kutta schemes'
---

'Multirate time integration methods apply different step sizes to resolve different components of the system based on the local activity levels. This local selection of step sizes allows increased computational efficiency while achieving the desired solution accuracy. While the multirate idea is elegant and has been around for decades, multirate methods are not yet widely used in applications. This is due, in part, to the difficulties raised by the construction of high order multirate schemes.
Seeking to overcome these challenges, this work focuses on the design of practical high-order multirate methods using the theoretical framework of generalized additive Runge-Kutta (MrGARK) methods, which provides the generic order conditions and the linear and nonlinear stability analyses.
A set of design criteria for practical multirate methods is defined herein: method coefficients should be generic in the step size ratio, but should not depend strongly on this ratio; unnecessary coupling between the fast and the slow components should be avoided; and the step size controllers should adjust both the micro- and the macro-steps.
Using these criteria, we develop MrGARK schemes of up to order four that are explicit-explicit (both the fast and slow component are treated explicitly), implicit-explicit (implicit in the fast component and explicit in the slow one), and explicit-implicit (explicit in the fast component and implicit in the slow one). Numerical experiments illustrate the performance of these new schemes.'

[Perprint](https://arxiv.org/abs/1804.07716) / [Paper](https://epubs.siam.org/doi/abs/10.1137/18M1182875) / [Recorded Talk](https://www.pathlms.com/siam/courses/10878/sections/14361/video_presentations/127463) / [Introductory Slide Deck](
https://docs.google.com/presentation/d/1M43xXqBg24S0TZVmhumRr_c_FNAICulXwpaRKIR-eTs/pub?start=false&loop=false&delayms=30000&slide=id.g1a987f6b5d_0_0) / [Program Abstract](https://meetings.siam.org/sess/dsp_talk.cfm?p=95449)

