---
layout: archive
title: "Research Overview"
permalink: /research/
author_profile: true
---

My ultimate research goal is to develop **trustworthy autonomous agents interacting with humans**. My current research mainly focus on designing <em> explainable autonomous driving systems</em>, where the decision-making process of autonomous vehicles is <em>tractable</em> and <em>transparent</em> for humans. Such a transparent system is a prerequisite for building trust between humans and autonomous vehicles. My research efforts towards this goal mainly lie in the following aspects:

## Diagnosing Black-box Deep-Learning Functional Modules
<img src="/images/nips.png" width="300" style="float: left; margin-right: 1em; margin-top: 0.5em; margin-bottom: 0.8em">
Deep neural networks achieve state-of-the-art performance in multiple core autonomous driving tasks (e.g., behavior prediction and policy learning). However, their black-box nature is a crucial barrier to genuine trustworthiness. It is, therefore, essential to gain a deeper understanding of their behavior. In my research, **I utilize explainable AI techniques to develop analysis toolkits customized for deep-learning functional modules**. They serve as simple plug-ins to diagnose the models without interfering with the performance. With the help of these toolkits, we identified principled design flaws in popular trajectory prediction models that were previously ignored in the literature, motivating new designs with improved robustness and performance. For instance, we found that Variational-Autoencoder-based trajectory prediction models suffer from an issue we named <em>social posterior collapse</em>, i.e., the model is prone to ignoring all the surrounding agents when predicting the future trajectory of a target agent. Our work is the first in the literature that discovered such systematic defects in interaction modeling. Prior works only focused on the overall performance without studying whether their models encode social context as claimed. <br/>

<p><b>Related Publications:</b><br>
<font size=3> 1. <b>C. Tang</b>, W. Zhan and M. Tomizuka, "Exploring Social Posterior Collapse in Variational Autoencoder for Interaction Modeling," <em>Conference on Neural Information Processing Systems (NeurIPS)</em>, 2021</font><br>
<font size=3> 2. <b>C. Tang</b>, W. Zhan, and M. Tomizuka, “Interventional behavior prediction: Avoiding overly confident anticipation in interactive prediction,” <em>IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)</em>, 2022</font></p>

## Designing Domain-Knowledge-Driven Interpretable Prediction Models
<p style="text-align:center;"><img src="/images/interpretable-prediction.png" width="750" style="margin-top: 0.5em"></p>
Interpretable models ensure that the systems are intelligible for humans at the design stage, which is crucial for <em>high-stakes</em> and <em>safe-critical</em> applications. Therefore, finding interpretable substitutes is a more fundamental solution to ensure transparency, in contrast to explaining black-box deep neural networks. To design interpretable trajectory prediction models, **I investigate principled methods to incorporate domain knowledge of social interaction into prediction models, inducing models reasoning interactive behavior consistently with humans.** Specifically, the proposed methods aim to introduce an interpretable latent space encoding semantically meaningful interactions among the agents. <br/>

<p><b>Related Publications:</b><br>
<font size=3> 1. <b>C. Tang</b>, N. Srishankar, S. Martin and M. Tomizuka, "Grounded Relational Inference: Domain Knowledge-driven Explainable Autonomous Driving," under review for <em>IEEE Transactions on Intelligent Transportation System (T-ITS)</em>, 2022</font><br>
<font size=3> 2. L. Sun<sup>*</sup>, <b>C. Tang</b><sup>*</sup>, Y. Niu, E. Sachdeva, C. Choi, T. Misu, M. Tomizuka, and W. Zhan, “Domain knowledge driven pseudo labels for interpretable goal-conditioned interactive trajectory prediction,” <em>IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)</em>, 2022</font><br></p>
  
## Designing Interpretable Hierarchical Driving Policys
<p style="text-align:center;"><img src="/images/interpretable-policy.png" width="720" style="margin-top: 0.5em"></p>
Another line of my research on interpretability studies interpretable driving policies. **I explored hierarchical architectures with interpretable intermediate outputs to reveal the decision-making process**. In particular, I am interested in driving policies with *trajectories* as intermediate outputs. The trajectory indicates a sequence of future states the policy aims to achieve, which implies the intended driving behavior of the policy. It helps the users better understand the decision-making process. Furthermore, such a hierarchical structure decomposes the policy into 1) a *high-level* module that plans the desired behavior represented by a trajectory; 2) a *low-level* module that realizes the desired behavior by controlling the vehicles. It allows flexible composition of different approaches when designing hierarchical policies. In particular, we showed that we could improve robustness or long-term performance by fusing learning-based (e.g., reinforcement learning, imitation learning) and model-based (e.g., robust control, optimal control) approaches in the hierarchy. 

<p><b>Related Publications:</b><br>
<font size=3> 1. Z. Xu<sup>*</sup>, <b>C. Tang</b><sup>*</sup>, and M. Tomizuka, “Zero-shot Deep Reinforcement Learning Driving Policy Transfer for Autonomous Vehicles based on Robust Control,” <em>IEEE International Conference on Intelligent Transportation Systems (ITSC)</em>, 2018 </font><br>
<font size=3> 2. <b>C. Tang</b><sup>*</sup>, Z. Xu<sup>*</sup>, and M. Tomizuka, "Disturbance-Observer-Based Tracking Controller for Neural Network Driving Policy Transfer," <em>IEEE Transactions on Intelligent Transportation Systems</em>, 2020 </font><br>
<font size=3> 3. J. Li, <b>C. Tang</b>, W. Zhan, and M. Tomizuka, “Hierarchical planning through goal-conditioned offline reinforcement learning,” <em>IEEE Robotics and Automation Letters (RA-L)</em> and <em>IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)</em>, 2022 </font><br></p>
 
## Improve Robustness of Learning-based Methods 
In addition to transparency, some of my prior works listed above also improve the robustness of behavior prediction models and policy networks. For behavior prediction, one crucial aspect is designing the model architecture and training scheme to induce a generalizable scene representation (e.g., map, social context). For policy networks, one crucial aspect is dealing with external disturbances and modeling discrepancies. Please find a list of related publications below. 

<p><b>Related Publications:</b><br>
<font size=3> 1. Z. Xu<sup>*</sup>, <b>C. Tang</b><sup>*</sup>, and M. Tomizuka, “Zero-shot Deep Reinforcement Learning Driving Policy Transfer for Autonomous Vehicles based on Robust Control,” <em>IEEE International Conference on Intelligent Transportation Systems (ITSC)</em>, 2018 </font><br>
<font size=3> 2. <b>C. Tang</b><sup>*</sup>, Z. Xu<sup>*</sup>, and M. Tomizuka, "Disturbance-Observer-Based Tracking Controller for Neural Network Driving Policy Transfer," <em>IEEE Transactions on Intelligent Transportation Systems</em>, 2020 </font><br>
<font size=3> 3. <b>C. Tang</b>, W. Zhan and M. Tomizuka, "Exploring Social Posterior Collapse in Variational Autoencoder for Interaction Modeling," <em>Conference on Neural Information Processing Systems (NeurIPS)</em>, 2021</font><br>
<font size=3> 4. J. Li, <b>C. Tang</b>, W. Zhan, and M. Tomizuka, "Dealing with the unkonw: Pessimistic Offline Reinforcement Learning," <em>5th Annual Conference on Robot Learning (CoRL)</em>, 2022 </font><br>
<font size=3> 5. J. Li, <b>C. Tang</b>, W. Zhan, and M. Tomizuka, “Hierarchical planning through goal-conditioned offline reinforcement learning,” <em>IEEE Robotics and Automation Letters (RA-L)</em> and <em>IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)</em>, 2022 </font><br>
<font size=3> 6. C. Xu<sup>*</sup>, T. Li<sup>*</sup>, <b>C. Tang</b><sup>*</sup>, L. Sun, K. Keutzer, M. Tomizuka, A. Fathi, and W. Zhan, "PreTraM: Self-Supervised Pre-training via Connecting Trajectory and Map," <em>European Conference on Computer Vision (ECCV)</em>, 2022 </font><br></p>
 
