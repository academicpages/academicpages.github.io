---
title: "Efficient and Sharp Off-Policy Learning under Unobserved Confounding"
collection: publications
authors: 'K. Hess, D. Frauen, <b>V. Melnychuk</b>, S. Feuerriegel'
date: 2025-02-18
excerpt: "![eff-pol](/images/eff-pol.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2502.13022'
preprint: true
---

We develop a novel method for personalized off-policy learning in scenarios with unobserved confounding. Thereby, we address a key limitation of standard policy learning: standard policy learning assumes unconfoundedness, meaning that no unobserved factors influence both treatment assignment and outcomes. However, this assumption is often violated, because of which standard policy learning produces biased estimates and thus leads to policies that can be harmful. To address this limitation, we employ causal sensitivity analysis and derive a statistically efficient estimator for a sharp bound on the value function under unobserved confounding. Our estimator has three advantages: (1) Unlike existing works, our estimator avoids unstable minimax optimization based on inverse propensity weighted outcomes. (2) Our estimator is statistically efficient. (3) We prove that our estimator leads to the optimal confounding-robust policy. Finally, we extend our theory to the related task of policy improvement under unobserved confounding, i.e., when a baseline policy such as the standard of care is available. We show in experiments with synthetic and real-world data that our method outperforms simple plug-in approaches and existing baselines. Our method is highly relevant for decision-making where unobserved confounding can be problematic, such as in healthcare and public policy.

Recommended citation: 
```bibtex
@article{hess2025efficient,
  title={Efficient and Sharp Off-Policy Learning under Unobserved Confounding},
  author={Hess, Konstantin and Frauen, Dennis and Melnychuk, Valentyn and Feuerriegel, Stefan},
  journal={arXiv preprint arXiv:2502.13022},
  year={2025}
}
```
