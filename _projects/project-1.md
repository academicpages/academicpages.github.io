---
title: "Survey of Deep Exploration"
excerpt: ""
collection: project
---

Introduction
===

![Summary of approaches in RL based on whether we want to model the value, policy, or the environment.(Image source: reproduced from David Silver's RL course lecture 1.)](http://remyjkim.github.io/images/RL_algorithm_categorization.png)


[the survey paper in pdf](http://remyjkim.github.io/files/Survey_Exploration_RL.pdf)
 
Exploration versus exploitation is a critical topic in reinforcement learning.
Although the ultimate goal of RL problems is to maximize the expected reward of the policy, committing to solutions too early on without enough exploration has significant opportunity costs.
Modern RL algorithms such as Lillicrap et al.(2016), Schulman et al.(2015), Schulman et al.(2017) that optimize for the best returns can achieve good exploitation quite efficiently, while exploration remains more like an open topic.
Such RL algorithms that proved successful in dense reward environments utilized $\epsilon$-greedy exploration which leaves space only to how much randomness will be allowed, but not to how the randomness will be directed. 

Haarnoja et al.(2018) was among the first algorithms to apply entropy of the policy as part of the loss function, thus encouraging diverse actions to be considered within a single policy. Furthermore, Lee et al.(2019) incorporated Tsallis entropy, a generalized entropy term into the actor-critic framework, thereby allowing the degree of exploration to be manipulated. However, this still could not shed light on how the stochasticity of the policy will unfold as exploration in a directed fashion.

The biggest problem can be elucidated on their performance on hard-exploration problems with sparse reward environments. 
A concrete example of this would be **montezuma's revenge**, where the player needs to take hundreds of actions(i.e. moving to the next room, going down the ladder and jumping over the monsters) to get the first reward signal. 
These environments require much "wandering around" to find which line of actions has the highest possibility of a reward before concluding that all actions seem pretty much equal reward-wise. 
Another problem was evident in the "Noisy-TV" problem first presented in Burda et al.(2019).
Imagine that an RL agent is rewarded with seeking novel experience, however a TV with uncontrollable and unpredictable random noise outputs would be able to attract the agent’s attention forever. 
The agent obtains new rewards from noisy TV consistently, but it fails to make any meaningful progress and becomes a “couch potato”.

As we will explore throughout this report, intrinsic motivation was one of the biggest clues in the area. Agents formulated their own rewards based on counts over observations, past memories, predictions over the future states, etc. Variational inference (information gain) was also utilized in computing the intrinsic rewards. Moreover, exploration was also studied on meta-reinforcement learning and multi-agent environments.
