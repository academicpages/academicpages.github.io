---
title: "Task Arithmetic with LoRA for Continual Learning"
collection: publications
category: workshops
permalink: /publication/TA_with_LoRA_for_CL
excerpt: 'Developed a computationally efficient method for continual training of ViTs that outperformed SOTA methods, using 5x less computation while maintaining near-perfect accuracy as compared to offline training baselines.'
date: 2023-10-29
venue: 'Workshop on Advancing Neural Network Training NeurIPS & R0-FoMo Workshop NeurIPS'
paperurl: 'https://arxiv.org/abs/2311.02428'
citation: 'Rajas Chitale, Ankit Vaidya, Aditya Kane, and Archana Ghotkar. "Task Arithmetic with LoRA for Continual Learning." (2023).'
---

We propose a computationally efficient approach for continual learning in vision-based transformers. Our method constructs a task-agnostic representation by performing task arithmetic on the weight-space vectors of disjoint tasks, continually trained on a LoRA-augmented Vision Transformer (ViT). To enforce alignment between task-specific and generalized representations, we optimize a weighted combination of cross-entropy loss and KL-divergence loss. Empirical analysis demonstrates that our approach significantly improves performance after few-shot fine-tuning, achieving near-perfect accuracy compared to offline training baselines. Moreover, it outperforms state-of-the-art continual learning methods (A-GEM and Experience Replay) while using 5× less computation.