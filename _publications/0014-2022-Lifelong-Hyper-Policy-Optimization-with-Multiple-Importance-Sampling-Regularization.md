---
title: "Lifelong Hyper-Policy Optimization with Multiple Importance Sampling Regularization"
collection: publ_conferences
permalink: /publication/0014-2022-Lifelong-Hyper-Policy-Optimization-with-Multiple-Importance-Sampling-Regularization
note: 'To appear'
acceptance: 'Acceptance rate: 1349/9020 (15.0%)'
rankCORE: 'CORE 2021: A*'
rankGGS: 'GGS 2021: A++'
date: 2022-01-01
venue: 'The Thirty-Sixth AAAI Conference on Artificial Intelligence (AAAI)'
paperurl: 'https://arxiv.org/abs/2112.06625'
pubtype: 'conferences'
authors: ' Pierre  Liotet,  Francesco  Vidaich,  Alberto Maria Metelli, and  Marcello  Restelli'
citation: ' Pierre  Liotet,  Francesco  Vidaich,  Alberto Maria Metelli, and  Marcello  Restelli&quot;Lifelong Hyper-Policy Optimization with Multiple Importance Sampling Regularization.&quot; The Thirty-Sixth AAAI Conference on Artificial Intelligence (AAAI), 2022'
---
Abstract
 <br> Learning in a lifelong setting, where the dynamics continually evolve, is a hard challenge for current reinforcement learning algorithms. Yet this would be a much needed feature for practical applications. In this paper, we propose an approach which learns a hyper-policy, whose input is time, that outputs the parameters of the policy to be queried at that time. This hyper-policy is trained to maximize the estimated future performance, efficiently reusing past data by means of importance sampling, at the cost of introducing a controlled bias. We combine the future performance estimate with the past performance to mitigate catastrophic forgetting. To avoid overfitting the collected data, we derive a differentiable variance bound that we embed as a penalization term. Finally, we empirically validate our approach, in comparison with state-of-the-art algorithms, on realistic environments, including water resource management and trading. <br> 

 [[Link](https://arxiv.org/abs/2112.06625){:target="_blank"}] 