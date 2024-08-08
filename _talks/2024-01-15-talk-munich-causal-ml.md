---
title: "Bounds on Representation-Induced Confounding Bias for Treatment Effect Estimation, ICLR 2024 paper"
collection: talks
type: "Presentation"
venue: "2nd Munich Causal ML Workshop"
date: 2024-01-15
location: "LMU Munich, Munich, Germany"
slides: 'https://docs.google.com/presentation/d/1TYfvgoJm2XLGq97-O_Xrh7Gd5p0kKIOB/edit?usp=sharing&ouid=109713321342366246841&rtpof=true&sd=true'
---

**Title**: Bounds on Representation-Induced Confounding Bias for Treatment Effect Estimation

**Abstract**: State-of-the-art methods for conditional average treatment effect (CATE) estimation make widespread use of representation learning. Here, the idea is to reduce the variance of the low-sample CATE estimation by a (potentially constrained) low-dimensional representation. However, low-dimensional representations can lose information about the observed confounders and thus lead to bias, because of which the validity of representation learning for CATE estimation is typically violated. In this paper, we propose a new, representation-agnostic refutation framework for estimating bounds on the representation-induced confounding bias that comes from dimensionality reduction (or other constraints on the representations) in CATE estimation. First, we establish theoretically under which conditions CATE is non-identifiable given low-dimensional (constrained) representations. Second, as our remedy, we propose a neural refutation framework which performs partial identification of CATE or, equivalently, aims at estimating lower and upper bounds of the representation-induced confounding bias. We demonstrate the effectiveness of our bounds in a series of experiments. In sum, our refutation framework is of direct relevance in practice where the validity of CATE estimation is of importance.

**Paper Link**: [https://openreview.net/forum?id=d3xKPQVjSc](https://openreview.net/forum?id=d3xKPQVjSc)