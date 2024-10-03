---
title: "Symbolic Computational Dynamics"
excerpt: "An introduction to multibody dynamics and the use of symbolic computation in modelling them."
---

## [Weblink](https://www.angadhn.com/ComputationalDynamics/kinematics/introduction.html)

## Who might find the above link useful?
{% newthought "The above text is most useful for" %} QMUL's first year undergraduate students taking
[EMS418U: Computational and Mathematical Modelling 2](https://www.qmul.ac.uk/modules/items/ems418u-computational-and-mathematical-modelling-2.html).
It could also be a useful resource for educators interested in classical mechanics wishing to teach computational
modeling to students using computer symbolic algebra. The content makes have use of `sympy`; specifically, its 
`physics.mechanics` module which has some utilities for quickly diving into vector operations.

## Our purpose
The idea is to encourage intuition-driven modelling and computational thinking in three-dimensions. Where most
introductory textbooks on classical mechanics emphasise hand-derived models to study motions of
simple systems (particles or a simple pendulum), our approach focuses on enabling deeper capabilities with
computing. We teach the fundamentals of modeling motion in three dimensions of particles and rigid bodies. We
then introduce planar kinematics of rigid multibody systems. Why? Multibody systems are everywhere; humans are
one example and robot arms are another. Waiting to introduce students to these concepts in an advanced
postgraduate course does little to stimulate imagination, in my humble opinion, or challenge the student.
Empowering students with the tools to build models seems like a better way to go about things from both
a perspective of upskilling but also for students to find and refine their personal interests in pursuing
their educational path into engineering. The use of computational tools early in their career
likely {% sidenote '' 'I believe this will hold even in the age of AI.'%} also prepares them 
for their future roles in research, industry, and entrepreneurship.

Later courses can build on the modeling capabilities towards analysing systems through numerical simulation
in a more discipline specific sense. For example, we analyse spacecraft motion in
[Computational Spacecraft Dynamics](https://www.angadhn.com/online_textbooks/spacecraft_dynamics/).
