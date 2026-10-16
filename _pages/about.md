---
permalink: /
title: "About Me"
excerpt: "About me"
author_profile: true
mathjax: true
redirect_from: 
  - /about/
  - /about.html
---

{% include base_path %}

<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>
<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']]
    }
  };
</script>

I am a **Ph.D. researcher** at Northeastern University developing foundational methods for trustworthy and scalable artificial intelligence in dynamical systems. My work lies at the intersection of **data-driven learning, optimization, and control theory**, with a focus on formal verification, robustness, and safety guarantees for neural-network-based decision-making systems.

I develop theory, algorithms, and software for certifying learning-enabled systems operating in complex, safety-critical environments, with applications spanning autonomous systems and robotics.

<center>
  <img src="/images/frankasiami1.gif" alt="Franka Emika Robot Demo" style="width: 100%; max-width: 500px; border: 1px solid #ddd; padding: 5px; border-radius: 5px;">
</center>
<br>

### Research Highlights
* **Scalable Verification:** Developed a scalable stability and robustness verification pipeline for learning-enabled autonomous systems, achieving up to ~\\(10^4 \times\\) speedup over state-of-the-art methods.
* **Neural Network Bounding:** Introduced novel global and local sector-bounds for Feedforward Neural Networks (FFNNs), enabling depth-agnostic and input-aware bounds with tighter certification than methods like CROWN.
* **Open-Source Library:** Released [nnsector](https://github.com/hmon91/nnsector), a Python and MATLAB library that computes these local and global sector bounds for FFNNs, ready for stability tests of neural feedback loops. See the [Software]({{ base_path }}/software/) page.
* **Tool Integration:** Integrated verification tools (AutoLIRPA, JAX-Verify) with classical control analysis (Lyapunov methods, MPC) to build reproducible verification workflows.

I am currently working on my thesis: *"Scalable Method for Stability and Robustness Verification of Systems with NN Feedback using Positivity Constraints"*.
