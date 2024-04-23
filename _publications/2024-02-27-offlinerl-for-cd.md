---
title: "Learning Conditional Policies for Crystal Design Using Offline Reinforcement Learning"
collection: publications
permalink: /publication/2024-02-27-offlinerl-for-cd
# excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
# date: 2023-10-01
venue: 'Digital Discovery'
paperurl: 'https://openreview.net/forum?id=VbjD8w2ctG'
# citation: 'Prashant Govindarajan, You. (2009). &quot;Paper Title Number 1.&quot; <i>Journal 1</i>. 1(1).'
---
Navigating through the exponentially large chemical space to search for desirable materials is an extremely challenging task in material discovery. Recent developments in generative and geometric deep learning have shown promising results in molecule and material discovery but often lack evaluation with high-accuracy computational methods. This work aims to design novel and stable crystalline materials conditioned on a desired band gap. To achieve conditional generation, we: 1. Formulate crystal design as a sequential decision-making problem, create relevant trajectories based on high-quality materials data, and use conservative Q-learning to learn a conditional policy from these trajectories. To do so, we formulate a reward function that incorporates constraints for energetic and electronic properties obtained directly from density functional theory (DFT) calculations; 2. Evaluate the generated materials from the policy using DFT calculations for both energy and band gap; 3. Compare our results to relevant baselines, including a random policy, behavioral cloning, and unconditioned policy learning. Our experiments show that conditioned policies achieve targeted crystal design and demonstrate the capability to perform crystal discovery evaluated with accurate and computationally expensive DFT calculations.
