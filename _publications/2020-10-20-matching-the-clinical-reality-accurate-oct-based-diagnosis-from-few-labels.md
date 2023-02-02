---
title: "Matching the Clinical Reality: Accurate OCT-Based Diagnosis From Few Labels"
collection: publications
authors: '<b>V. Melnychuk</b>, E. Faerman, I. Manakov, T. Seidl'
date: 2020-10-20
excerpt: ""
arxiv: 'https://arxiv.org/abs/2010.12316'
code: 'https://github.com/Valentyn1997/oct-diagn-semi-supervised'
---

![oct-diagn](/images/oct-diagn.png){: style='width: 450px'}

Unlabeled data is often abundant in the clinic, making machine learning methods based on semi-supervised learning a good match for this setting. Despite this, they are currently receiving relatively little attention in medical image analysis literature. Instead, most practitioners and researchers focus on supervised or transfer learning approaches. The recently proposed MixMatch and FixMatch algorithms have demonstrated promising results in extracting useful representations while requiring very few labels. Motivated by these recent successes, we apply MixMatch and FixMatch in an ophthalmological diagnostic setting and investigate how they fare against standard transfer learning. We find that both algorithms outperform the transfer learning baseline on all fractions of labelled data. Furthermore, our experiments show that exponential moving average (EMA) of model parameters, which is a component of both algorithms, is not needed for our classification problem, as disabling it leaves the outcome unchanged. Our code is available online: [URL](https://github.com/Valentyn1997/oct-diagn-semi-supervised).

Recommended citation: 
```bibtex
@article{melnychuk2020matching,
  title={Matching the Clinical Reality: Accurate {OCT-based} Diagnosis From Few Labels},
  author={Melnychuk, Valentyn and Faerman, Evgeniy and Manakov, Ilja and Seidl, Thomas},
  journal={arXiv preprint arXiv:2010.12316},
  year={2020}
}
```
