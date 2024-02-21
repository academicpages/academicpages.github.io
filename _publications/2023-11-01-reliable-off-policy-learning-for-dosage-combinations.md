---
title: "Reliable Off-Policy Learning for Dosage Combinations"
collection: publications
authors: 'J. Schweisthal, D. Frauen, <b>V. Melnychuk</b>, S. Feuerriegel'
date: 2023-11-01
venue: NeurIPS
excerpt: "![dose-response](/images/dose-response.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2305.19742'
code: 'https://github.com/JSchweisthal/ReliableDosageCombi'
slides: 'https://neurips.cc/media/neurips-2023/Slides/70533_gMkn2Kt.pdf'
poster: 'https://nips.cc/media/PosterPDFs/NeurIPS%202023/70533.png?t=1701190332.0669198'
paperurl: 'https://proceedings.neurips.cc/paper_files/paper/2023/file/d69103d7895f4e2083f24b664003d386-Paper-Conference.pdf'
---

Decision-making in personalized medicine such as cancer therapy or critical care must often make choices for dosage combinations, i.e., multiple continuous treatments. Existing work for this task has modeled the effect of multiple treatments independently, while estimating the joint effect has received little attention but comes with non-trivial challenges. In this paper, we propose a novel method for reliable off-policy learning for dosage combinations. Our method proceeds along three steps: (1) We develop a tailored neural network that estimates the individualized dose-response function while accounting for the joint effect of multiple dependent dosages. (2) We estimate the generalized propensity score using conditional normalizing flows in order to detect regions with limited overlap in the shared covariate-treatment space. (3) We present a gradient-based learning algorithm to find the optimal, individualized dosage combinations. Here, we ensure reliable estimation of the policy value by avoiding regions with limited overlap. We finally perform an extensive evaluation of our method to show its effectiveness. To the best of our knowledge, ours is the first work to provide a method for reliable off-policy learning for optimal dosage combinations.

Recommended citation: 
```bibtex
@inproceedings{schweisthal2023reliable,
  title={Reliable Off-Policy Learning for Dosage Combinations},
  author={Schweisthal, Jonas and Frauen, Dennis and Melnychuk, Valentyn and Feuerriegel, Stefan},
  booktitle={Advances in Neural Information Processing Systems},
  year={2023}
}
```
