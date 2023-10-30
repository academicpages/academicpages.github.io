---
title: "Counterfactual Fairness for Predictions using Generative Adversarial Networks"
collection: publications
authors: 'Y. Ma, D. Frauen, <b>V. Melnychuk</b>, S. Feuerriegel'
date: 2023-10-30
excerpt: "![fair-policy](/images/gan-fairness.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2310.17687'
preprint: true
---

Fairness in predictions is of direct importance in practice due to legal, ethical, and societal reasons. It is often achieved through counterfactual fairness, which ensures that the prediction for an individual is the same as that in a counterfactual world under a different sensitive attribute. However, achieving counterfactual fairness is challenging as counterfactuals are unobservable. In this paper, we develop a novel deep neural network called Generative Counterfactual Fairness Network (GCFN) for making predictions under counterfactual fairness. Specifically, we leverage a tailored generative adversarial network to directly learn the counterfactual distribution of the descendants of the sensitive attribute, which we then use to enforce fair predictions through a novel counterfactual mediator regularization. If the counterfactual distribution is learned sufficiently well, our method is mathematically guaranteed to ensure the notion of counterfactual fairness. Thereby, our GCFN addresses key shortcomings of existing baselines that are based on inferring latent variables, yet which (a) are potentially correlated with the sensitive attributes and thus lead to bias, and (b) have weak capability in constructing latent representations and thus low prediction performance. Across various experiments, our method achieves state-of-the-art performance. Using a real-world case study from recidivism prediction, we further demonstrate that our method makes meaningful predictions in practice.

Recommended citation: 
```bibtex
@article{ma2023counterfactual,
  title={Counterfactual Fairness for Predictions using Generative Adversarial Networks},
  author={Ma, Yuchen and Frauen, Dennis and Melnychuk, Valentyn and Feuerriegel, Stefan},
  journal={arXiv preprint arXiv:2310.17687},
  year={2023}
}
```
