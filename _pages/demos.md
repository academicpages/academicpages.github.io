---
layout: archive
title: "Demos"
permalink: /demos/
author_profile: true
---

## **[VMAgent](https://github.com/mail-ecnu/VMAgent) Simulator**

# ![VMAgent LOGO](../images/logo.svg)

**VMAgent** is a platform for exploiting Reinforcement Learning (RL) on Virtual Machine (VM) scheduling tasks.
It is developed by the Multi-Agent Artificial Intelligence Lab (MAIL) in East China Normal University and [Algorithm Innovation Lab](https://www.huaweicloud.com/lab/algorithm/home.html) in [**HUAWEI Cloud**](https://www.huaweicloud.com).
VMAgent is constructed based on one month real VM scheduling dataset called [*Huawei-East-1*](https://vmagent.readthedocs.io/en/latest/simulator/dataset.html) from HUAWEI Cloud and it contains multiple practicle VM scheduling scenarios (such as Fading, Rcovering, etc).
These scenarios also correspond to the challanges in the RL.
Exploiting the design of RL methods in these secenarios help both the RL and VM scheduling communities.
To emphasis, more details about VMAgent can be found in our paper [*VMAgent: Scheduling Simulator for Reinforcement Learning*](https://arxiv.org/abs/2112.04785).
Our another paper [*Learning to Schedule Multi-NUMA Virtual Machines via Reinforcement Learning*](https://www.sciencedirect.com/science/article/abs/pii/S0031320321004349) has employed this VMAgent simultor to design RL-based VM scheduling algorithms.

**Key Components of VMAgent**:
* SchedGym (Simulator): it provides many practical scenarios and flexible configurations to define custom scenarios.
* SchedAgent (Algorithms): it provides many popular RL methods as the baselines.
* SchedVis (Visulization): it provides the visualization of schedlueing dynamics on many metrics.

**References**
- **Junjie Sheng**, **Shengliang Cai**, **Haochuan Cui**, **Wenhao Li**, **Yun Hua**, **Bo Jin**, W. Zhou, Y. Hu, L. Zhu, Q. Peng, **Hongyuan Zha** and **Xiangfeng Wang**, VMAgent: A Practical Virtual Machine Scheduling Platform. *IJCAI-Demos*, 2022. (**The [VMAgent](https://github.com/mail-ecnu/VMAgent) Simulator**)
- Junjie Sheng, Yiqiu Hu, Wenli Zhou, Lei Zhu, Bo Jin, Jun Wang and Xiangfeng Wang, Learning to Schedule Multi-NUMA Virtual Machines via Reinforcement Learning, Pattern Recognition, 121, 2022, pp.108254.

<iframe
	src="https://mail-cs-ecnu-text-gym-agents.hf.space"
	frameborder="0"
	width="850"
	height="450"
></iframe>
