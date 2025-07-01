---
title: "Signal Recovery Using a Spiked Mixture Model"
collection: publications
permalink: /publication/2024-11-signal-recovery
excerpt: 'We introduce the spiked mixture model (SMM) to address the problem of estimating a set of signals from many randomly scaled and noisy observations'
date: 2025-01-03
venue: 'preprint'
paperurl: 'https://arxiv.org/abs/2501.01840'
#citation: 'Delacour, Paul. (2025). &quot;Signal Recovery Using a Spiked Mixture Model.&quot; <i>Journal 1</i>. 1(1).'
---

We introduce the spiked mixture model (SMM) to address the problem of estimating a set of signals from many randomly scaled and noisy observations. Subsequently, we design a novel expectation-maximization (EM) algorithm to recover all parameters of the SMM. Numerical experiments show that in low signal-to-noise ratio regimes, and for data types where the SMM is relevant, SMM surpasses the more traditional Gaussian mixture model (GMM) in terms of signal recovery performance.

[Download paper here](https://arxiv.org/abs/2501.01840)


<video width="640" height="360" autoplay loop muted>
  <source src="https://pauldelacour.github.io/images/SMM/synthetic_data_SMM.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>

<style>
  .center {
    text-align: center; /* Centers the video horizontally */
    max-width: 100%; /* Ensures the container doesn’t exceed the page width */
  }

  video {
    width: 100%; /* Makes the video responsive */
    height: auto; /* Maintains the aspect ratio */
  }
</style>

<h3>Low noise \(\sigma^2 = 0.01\)</h3>
<img src="https://pauldelacour.github.io/images/SMM/model_comparison_low_noise_0.01.png" alt="low_noise_case">
<h3>High noise \(\sigma^2 = 0.5\)</h3>
<img src="https://pauldelacour.github.io/images/SMM/model_comparison_high_noise_0.5.png" alt="high_noise_case">

Our Poster presentation for ASMS 2025 : 
[Poster](https://pauldelacour.github.io/images/SMM/2025_05_30_asms2025_smm_clustering_delacour.pdf)
<a href="https://pauldelacour.github.io/images/SMM/2025_05_30_asms2025_smm_clustering_delacour.pdf", rel="permalink">Poster</a>
