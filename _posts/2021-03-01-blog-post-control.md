---
title: 'Learning to Control Soft Robots'
date: 2021-03-01
permalink: /posts/2017/11/blog-post-bipedal/
tags:
  - machine learning
  - co-evolution of morphology and control
  - essay
---

Introduction
------
Classically controlled robots have revolutionised assembly lines where the environment is restrictedand predictable. However, this control scheme has proven less effective in uncertain, unstructured environments due to the unmodelled nonlinearities in the morphology and its interaction with the environment [Atkeson et al., 2015]. Embodied intelligence suggests that we are not controlled centrally but
rather that the morphology and environment also contribute to behaviour. Therefore, the passive dynamics of the robot could be exploited to simplify the controller by making the passive dynamics closer to the desired behaviour [Pfeifer and Bongard, 2006]. Consequently, there has been a growing interest in soft robots which have many passive degrees of freedom and are often underactuated. However, classical control necessitates exact kinematic and dynamic models which are hard to derive analytically for soft
robots due to the nonlinear dynamics of the body, external forces, and uncertain, unstructured environment. Model-free approaches are a potential solution to these problems as they can approximate inverse
kinematic and dynamic models that account for the unknown nonlinearities.

Control Learning for Soft Continuum Manipulators
------
The first use of a model-free method for continuum robotic manipulators used the universal approximation properties of a feedforward neural network to compensate for some of these unknown nonlinear
dynamics [Braganza et al., 2007]. The neural network was added to a closed-loop controller to compen-
sate for the difference between the desired and actual actuator lengths by regulating the pressure of the
nine pneumatic actuators. However, the actual position and orientation of the end effector are still uncertain due to the time-dependant nonlinearities of the compliant material, external forces, and uncertain
environment. Accurate tracking of the end effector is also a particular challenge for continuum robots.
Giorelli et al. [2013] were the first to use a feedforward neural network to solve the inverse kinematics
of a non-constant curvature, cable-driven continuum manipulator for which no analytical solution was
possible. The benefit of using a feedforward neural networks to learn inverse kinematics is that
they can generalise between observed data, even when the data is noisy. This method was able to
approximate the cable tensions to move the end effector in simulation. Later work focused on learning
control in real-world robots due to the simulation-reality gap. Despite the generalisability of neural
networks, developing efficient ways to explore the motor space would be advantageous, especially when
using physical robots. To this end, Rolf and Steil [2013] used goal babbling and online learning to learn
the inverse kinematics of a high-dimensional bionic elephant trunk. Actions were explored by making
goal-directed movements and the observed outcomes were used for supervised learning. This method
improved exploration efficiency over the traditional approach of motor babbling which would be very
inefficient for high-dimensional redundant systems. Goal babbling also speeds up the learning process
due to a positive feedback loop when combined with online learning. Ongoing learning also improves
robustness to changes such as noisy and drifting sensor readings and varying actuator ranges.
Previous model-free methods for learning the inverse kinematic and dynamic models were effectively
used for controlling a continuum manipulator in structured environments when external forces were not
applied. As external forces and an uncertain environment are particularly problematic for continuum
manipulators, George Thuruthel et al. [2017] used a neural network to learn the model-free closed loop
inverse kinematics of a 6DOF tendon-driven continuum manipulator and showed that the learned inverse
model could adapt to external forces when the position and orientation of the end effector was tracked
using an electromagnetic probe.

Control Learning for Locomotion
------
Control for the locomotion of soft robots can also be learned. Vibration-driven tensegrity robots present a
challenge as the motion is unpredictable and therefore have no known analytical solution for generating
gait. Khazanov et al. [2014] used an evolutionary algorithm to optimise the motor frequencies for
the control of a physical vibration-driven tensegrity robot and exploited the inherent resonance of the
tensegrity structures to increase the locomotion speed. Rieffel and Mouret [2018] also aimed to exploit
the resonance of a vibration-driven tensegrity robot to increase locomotion speed. However, they used
Bayesian optimisation to efficiently learn control for a physical robot. The policy is learned by optimising
three pulse width modulation values that control the input voltage of the vibrating motors. Bayesian optimisation models the objective function using regression and uses this to select the next point to
acquire. Comparing the results between random search and Bayesian optimisation with and without
a prior, they found the Bayesian optimisation with a prior produced the fastest speed using the same
number of trials.
Another solution is to exploit the dynamics of the tensegrity robot as a computational recourse using
reservoir computing for morphological computation. Caluwaerts et al. [2013] used this method to simplify
the controller of a tensegrity robot so that the gait could be maintained with a linear feedback control
while integrating external feedback into the control loop. The dynamic system can be viewed as the
computational black-box as the exact dynamics of the system do not need to be explicitly known by the
learning algorithm and the instantaneous state of the system encodes the nonlinear interactions with
the environment. They use an evolutionary algorithm to optimise the control parameters (weights of a
central pattern generator) where fitness is the distance traveled by the tensegrity robot.
Veenstra et al. [2018] used an evolutionary algorithm to optimise the controller of a physical soft fish
robot to increase locomotion speed. The genome representation was 15 bytes separated up into 5 sets of
3 bytes for the frequency, phase and amplitude of a sign wave. These 5 sine waves are summed for the
first five terms of a Fourier series used to control the undulation pattern of the fin. They found that the
optimised controller outperform a hand-programmed controller.

Co-Design of Morphology and Control
------
Embodied intelligence suggests that the design of the morphology is an important factor in the
behaviour. Co-design of the morphology and control may therefore result in a better solution than
optimising the morphology with a fixed controller (e.g. Corucci et al. [2015]) or the controller with a fixed
morphology. The morphology can be adapted either through evolutionary adaption or developmental
adaption. However, the simulation-reality gap is a challenge as it is not possible to exactly model
the behaviour of a real robot in its environment due to simplifications that do not adequately capture
environmental forces interacting with the robot. One solution is to fabricate and test some or all of the
candidate solutions. Such methods are possible with soft robots. For example, soft components could be
rapidly fabricated using hot melt adhesives or a laser cutter. However, fabricating complex morphologies
remains a challenge, as does the time cost for fabrication and testing.
Goal-focused evolutionary algorithms are computationally expensive even in simulation. Joachimczak
et al. [2015] used a combination of novelty search combined with developmental adaptation in simulation to reduce the computational cost of designing the morphologies and controllers of multicellular and
soft-bodied robots. Novelty search rewards a phenotype based on how different it is from other pheno-
types in the population and developmental adaption reduces the computational expense by reducing the
complexity of the fitness landscape.
Vujovic et al. [2017] were the first to combine evolutionary algorithms and developmental adaptation for morphology-control co-evolution using physical robots where the fabrication process of soft-legged robots was automated using a robot arm and hot glue. Evolutionary algorithms are well suited to
morphology-control co-evolution but require all candidate solutions to be evaluated and lack any assumptions about the influence of its parameters. Bayesian optimisation continuously develops a relationship
between the morphology and control parameters and behaviour. Therefore, the behaviour of design parameters that are not yet tested can be inferred from parameters that were already tested. Rosendo et al.
[2017] therefore proposed the use of Bayesian optimisation to infer the best locomotion behaviour using
autonomously assembled physical modular robots. They showed that morphology-control co-optimised
robots outperform robots with an optimised controller for a fixed morphology. However, while Bayesian
optimisation found the best solution after evaluating 25 morphologies, a total of 50 morphologies were
evaluated which took 37.5 hours.
Hardman et al. [2020] used a different technique to reduce the number of evaluated candidate solutions
by using the piecewise morphology controller co-adaption (PMCCA) strategy to adapt the morphological
and control parameters for a rigid 3 degree of freedom walking robot. As continuity in morphology space
means small changes in the morphology cause small changes in behaviour, only small changes in control
parameters are needed to retain the desired behaviour. Therefore, PMCCA was used to perform a refined
search to adapt the morphological parameters. PMCCA was then used to find new control parameters
for these new morphologies using prior knowledge from neighboring morphologies and their controllers.
They found this often increased the fitness and reduced the number of iterations for optimisation com-
pared to using a global optimisation algorithm.

Conclusion
------
Control learning for soft robots has proven advantageous and readily implementable. Kinematic and
dynamic models that are hard to derive analytically can be approximated using model-free methods.
More efficient methods for exploring the motor space have improved the learning of control strategies
for physical robots. However, the control parameters would need to be updated if the task, morphology
or environment changed. Continuously adapting the control parameters and the morphology to these
changes would be the most promising approach in the future and could better exploit the rich dynamics
of the soft robots. This goes hand in hand with the sensing cost to provide accurate body configuration
feedback which is also a challenge for high-dimensional soft robots.
Co-design of morphology and control is largely performed in the real world due to the simulation-
reality gap. Optimisation techniques have reduced the number of evaluated candidates needed for co-
design of morphology and control and these solutions have been shown to outperform a controller optimised for a fixed morphology. However, the time cost for automating the fabrication and testing of
physical candidates is still substantial. The biggest hurdle is therefore the development of an autonomous
system for the fabrication and testing of candidate robots that reduces the time cost and can fabricate more
complex robots.

Bibliography
------
Christopher G Atkeson, Benzun P Wisely Babu, Nandan Banerjee, Dmitry Berenson, Christoper P Bove,
Xiongyi Cui, Mathew DeDonato, Ruixiang Du, Siyuan Feng, Perry Franklin, et al. No falls, no resets:
Reliable humanoid behavior in the darpa robotics challenge. In 2015 IEEE-RAS 15th International
Conference on Humanoid Robots (Humanoids), pages 623–630. IEEE, 2015.

David Braganza, Darren M Dawson, Ian D Walker, and Nitendra Nath. A neural network controller for
continuum robots. IEEE transactions on robotics, 23(6):1270–1277, 2007.

Ken Caluwaerts, Michiel D’Haene, David Verstraeten, and Benjamin Schrauwen. Locomotion without a
brain: physical reservoir computing in tensegrity structures. Artificial life, 19(1):35–66, 2013.

Francesco Corucci, Marcello Calisti, Helmut Hauser, and Cecilia Laschi. Novelty-based evolutionary
design of morphing underwater robots. In Proceedings of the 2015 annual conference on Genetic and
Evolutionary Computation, pages 145–152, 2015.

Thomas George Thuruthel, Egidio Falotico, Mariangela Manti, Andrea Pratesi, Matteo Cianchetti, and
Cecilia Laschi. Learning closed loop kinematic controllers for continuum manipulators in unstructured
environments. Soft robotics, 4(3):285–296, 2017.

Michele Giorelli, Federico Renda, Gabriele Ferri, and Cecilia Laschi. A feed-forward neural network
learning the inverse kinetics of a soft cable-driven manipulator moving in three-dimensional space. In
2013 IEEE/RSJ International Conference on Intelligent Robots and Systems, pages 5033–5039. IEEE,
2013.

David Hardman, Thomas George Thuruthel, and Fumiya Iida. Towards growing robots: A piecewise
morphology-controller co-adaptation strategy for legged locomotion. In Annual Conference Towards
Autonomous Robotic Systems, pages 357–368. Springer, 2020.

Michal Joachimczak, Reiji Suzuki, and Takaya Arita. Improving evolvability of morphologies and con-
trollers of developmental soft-bodied robots with novelty search. Frontiers in Robotics and AI, 2:33,
2015.

Mark Khazanov, Julian Jocque, and John Rieffel. Evolution of locomotion on a physical tensegrity robot.
In Artificial Life Conference Proceedings 14, pages 232–238. MIT Press, 2014.

Rolf Pfeifer and Josh Bongard. How the body shapes the way we think: a new view of intelligence. MIT
press, 2006.

John Rieffel and Jean-Baptiste Mouret. Adaptive and resilient soft tensegrity robots. Soft robotics, 5(3):
318–329, 2018.

Matthias Rolf and Jochen J Steil. Efficient exploratory learning of inverse kinematics on a bionic elephant
trunk. IEEE transactions on neural networks and learning systems, 25(6):1147–1160, 2013.

Andre Rosendo, Marco Von Atzigen, and Fumiya Iida. The trade-off between morphology and control
in the co-optimized design of robots. PloS one, 12(10):e0186107, 2017.

Frank Veenstra, Jonas Jørgensen, and Sebastian Risi. Evolution of fin undulation on a physical knifefish-
inspired soft robot. In Proceedings of the Genetic and Evolutionary Computation Conference, pages
157–164, 2018.

Vuk Vujovic, Andre Rosendo, Luzius Brodbeck, and Fumiya Iida. Evolutionary developmental robotics:
Improving morphology and control of physical robots. Artificial life, 23(2):169–185, 2017.
