---
title: "[Under Review]CRADLE: Constrained Reinforcement for Autonomous Driving Learning in Simulation-to-Real Environment"
collection: publications
permalink: /publication/2309-CRADLE
excerpt:  'Proposed a constraint-RL based formulation for the autonomous driving problem with lane offset and collisions constraints. Developed an autonomous driving algorithm which maximizes the driving distance while adhering to two different constraints. The proposed approach performs better than the previous RL-based approach on the specific autonomous driving task.'
date: 2024-01-01
venue: 'ICRA'
paperurl: # 'http://academicpages.github.io/files/paper3.pdf'
citation: # 'Your Name, You. (2015). &quot;Paper Title Number 3.&quot; <i>Journal 1</i>. 1(3).'
---
Autonomous driving (AD) is becoming an essential component in the domain of modern transportation, ranging from self-driving cars to autonomous warehouse systems. Reinforcement learning (RL) based approaches are getting traction to address the autonomous driving problem due to their aptitude for sequential decision-making. However, a key challenge in using RL for autonomous driving is designing an appropriate reward function that balances different objectives, such as maximizing driving distance while avoiding collisions. Rather than balance different objectives with fixed weights in the reward function, which requires scenario-specific tuning, we formulate AD as a constrained-RL problem, where we use driving distance as the target reward and consider other objectives such as collision avoidance as cost constraints. In our proposed approach, the weight coefficients of these different objectives are learned automatically along with the policy. We evaluate our approach on an autonomous driving platform called Duckietown in both simulation and real-world settings. Empirically, our approach shows superior performance compared with previous RL based methods on the Duckietown platform. Additionally, we successfully transferred our policy from the simulator to the real-world to validate our approach.

<!-- [Download paper here](http://academicpages.github.io/files/paper3.pdf) -->

<!-- Recommended citation: Your Name, You. (2015). "Paper Title Number 3." <i>Journal 1</i>. 1(3). -->