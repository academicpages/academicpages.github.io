---
title: "[Under Review]CRADLE: Constrained Reinforcement for Autonomous Driving Learning in Simulation-to-Real Environment"
collection: publications
permalink: /publication/2309-CRADLE
excerpt:  'Proposed a constraint-RL based formulation for the autonomous driving problem with lane offset and collisions constraints. Developed an autonomous driving algorithm which maximizes the driving distance while adhering to two different constraints. The proposed approach performs better than the previous RL-based approach on the specific autonomous driving task.'
date: 2023-01-01
venue: 'ICRA'
paperurl: # 'http://academicpages.github.io/files/paper3.pdf'
citation: # 'Your Name, You. (2015). &quot;Paper Title Number 3.&quot; <i>Journal 1</i>. 1(3).'
---
Autonomous driving in recent years is becoming an essential component in the domain of modern transportation, ranging from self-driving passenger cars to autonomous robot workers in warehouse management systems. The reinforcement learning(RL) based approach is getting traction as the most suitable learning based method to address the autonomous driving problem due to the sequential decision-making nature of the problem. Learning an ideal policy for the autonomous driving problem requires optimization of different objectives, e.g., maximizing the driving distance while driving in the correct lane and avoiding any collisions. A key challenge in using RL based system is designing the appropriate reward function for the task. Unlike previous approaches of using a fixed-weighted combination of different objectives as a reward, which requires tuning for different driving scenarios. We formulate the problem of autonomous driving as a constrained-RL problem, where we use moving forward as a reward and different costs as constraints. In our proposed approach, the weight coefficients are also learned automatically along with the policy. We evaluate our approach on a popular autonomous driving platform called Duckietown in both simulation and real-world settings. Empirically, we show our approach performs better than the previous RL based approach on the platform.

<!-- [Download paper here](http://academicpages.github.io/files/paper3.pdf) -->

<!-- Recommended citation: Your Name, You. (2015). "Paper Title Number 3." <i>Journal 1</i>. 1(3). -->