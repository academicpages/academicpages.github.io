---
title: "(DRL) MUSIC with Tsallis Entropy"
date: 2022-09-10
# excerpt: "My Final Project for Deep Reinforcement Learning 2021 Spring"
excerpt: http://remyjkim.github.io/images/fetchPush.png
collection: portfolio
---

Abstract
===

[the paper in pdf](http://remyjkim.github.io/files/Mutual_Information_State_Intrinsic_Control_with_Tsallis_Entropy.pdf)
 
RL researches on exploration has been centered around Atari-games and control problems within the Mujoco environment. Mutual Information State Intrinsic Control(MUSIC) is one of the first RL algorithm with intrinsically motivated exploration strategy that proved successful in robotic manipulation tasks. MUSIC utilizes agent-surrounding state separation to compute mutual information between the two and use it as an intrinsic motivation(or a proxy for prioritization coefficient). While Soft-Actor-Critic version of the algorithm is better performing than its Deep Deterministic Policy Gradient version, having a “dense” stochastic policy(as is used in SAC) seems to hinder its performance in certain task. Considering that too much stochasticity in its policy may hinder its applicability in real situation performance of robotic manipulation task, this project utilizes Tsallis Entropy Regularization to the MUSIC algorithm and shows improvements in its performance in FetchPush-v1, FetchSlide-v1, FetchPickandPlace-v1 tasks. 


These are the tasks from openGym Mujoco suite that were used for this experiment.


Task fetchPush
<img src="http://remyjkim.github.io/images/fetchPush.png"  width="30%" height="30%">

Task fetchPushandpick
<img src="http://remyjkim.github.io/images/fetchPushandpick.png"  width="30%" height="30%">

Task fetchSlide
<img src="http://remyjkim.github.io/images/fetchSlide.png"  width="30%" height="30%">

<!-- ![fetchPush task : ](http://remyjkim.github.io/images/fetchPush.png =100x)
![fetchPushandpick task : ](http://remyjkim.github.io/images/fetchPushandpick.png =100x)
![fetchSlide task : ](http://remyjkim.github.io/images/fetchSlide.png =100x) -->