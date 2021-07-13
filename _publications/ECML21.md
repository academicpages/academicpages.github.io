---
title: "Multi-Agent Imitation Learning with Copulas"
collection: publications
permalink: /publications/ECML21
venue: "ECML-PKDD 2021"
date: 2021-6-19
citation: 'Hongwei	Wang*, <b>Lantao Yu</b>* (equal contribution), Zhangjie Cao, Stefano Ermon. <i>European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases</i>. <b>ECML-PKDD 2021</b>.'
---

[[PDF]](https://arxiv.org/pdf/2107.04750.pdf)

## Abstract
Multi-agent imitation learning aims to train multiple agents to perform tasks from demonstrations by learning a mapping between observations and actions, which is essential for understanding physical, social, and team-play systems. However, most existing works on modeling multi-agent interactions typically assume that agents make independent decisions based on their observations, ignoring the complex dependence among agents. In this paper, we propose to use copula, a powerful statistical tool for capturing dependence among random variables, to explicitly model the correlation and coordination in multi-agent systems. Our proposed model is able to separately learn marginals that capture the local behavioral patterns of each individual agent, as well as a copula function that solely and fully captures the dependence structure among agents. Extensive experiments on synthetic and real-world datasets show that our model outperforms state-of-the-art baselines across various scenarios in the action prediction task, and is able to generate new trajectories close to expert demonstrations.