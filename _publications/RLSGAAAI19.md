---
title: "Deep Reinforcement Learning for Green Security Games with Real-Time Information"
collection: publications
permalink: /publications/RLSGAAAI19
venue: "The Thirty-Third AAAI Conference on Artificial Intelligence (AAAI-19)"
date: 2019-2-1
citation: 'Yufei Wang, Zheyuan Ryan Shi, <b>Lantao Yu</b>, Yi Wu, Rohit Singh, Lucas Joppa, Fei Fang. <i>The Thirty-Third AAAI Conference on Artificial Intelligence</i>. <b>AAAI 2019</b>.'
---  
[[PDF]](https://arxiv.org/pdf/1811.02483.pdf)
## Abstract
Green Security Games (GSGs) have been proposed and applied to optimize patrols conducted by law enforcement agencies in green security domains such as combating poaching, illegal logging and overfishing. However, real-time information such as footprints and agents’ subsequent actions upon receiving the information, e.g., rangers following the footprints to chase the poacher, have been neglected in previous work. To fill the gap, we first propose a new game model GSG-I which augments GSGs with sequential movement and the vital element of real-time information. Second, we design a novel deep reinforcement learning-based algorithm, DeDOL, to compute a patrolling strategy that adapts to the real-time information against a best-responding attacker. DeDOL is built upon the double oracle framework and the policy-space response oracle, solving a restricted game and iteratively adding best response strategies to it through training deep Q-networks. Exploring the game structure, DeDOL uses domain-specific heuristic strategies as initial strategies and constructs several local modes for efficient and parallelized training. To our knowledge, this is the first attempt to use Deep Q-Learning for security games.