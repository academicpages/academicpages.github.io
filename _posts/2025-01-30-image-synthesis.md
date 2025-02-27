---
title: 'Image Synthesis'
date: 2025-01-30
permalink: /posts/2025/01/image-synthesis/
tags:
  - image synthesis
  - diffusion
  - autoregressive
  - LLM
---
✅ -> finished reading
❌ -> not yet finished reading

# Diffusion 
[Understanding Diffusion Models: A Unified Perspective](https://arxiv.org/abs/2208.11970) from Calvin Luo. ✅

- Detailed formula derivation for Denoising Diffusion Probabilistic Model (DDPM) and Variational Diffusion Model (VDM)

- Connection between VDM and score-based generative models

- Conditional generation (Classifier Guidance and Classifier-free Guidance)

[What are Diffusion Models?](https://lilianweng.github.io/posts/2021-07-11-diffusion-models) from Lilian Weng. 
- DDPM ✅
- DDIM ❌ 
- Diffusion Speed-up: Progressive Distillation ❌ , Consistency Models ❌ , LDM ✅
- Scale-up Generation: Cascaded Diffusion Models ✅, unCLIP ❌ 
- Model Architecture: U-Net ✅, ControlNet ❌ , DiT ✅

[Generative Modeling by Estimating Gradients of the Data Distribution](https://yang-song.net/blog/2021/score/) from Yang Song. 
- Naive score-based generative modeling and its pitfalls ✅
- Score-based generative modeling with multiple noise perturbations ✅
- Score-based generative modeling with stochastic differential equations (SDEs) ❌ 