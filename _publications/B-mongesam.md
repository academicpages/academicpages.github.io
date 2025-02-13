---
title: "Preprint: Monge SAM - Robust Reparameterization-Invariant Sharpness-Aware Minimization Based on Loss Geometry"
collection: papers
permalink: /papers/mongesam
excerpt: "Authors: <i><b>Albert Kjøller Jacobsen</b>, Georgios Arvanitidis</i>"
# date: 2025-07-19
# venue: 'Preprint on arXiv'
paperurl: 'https://arxiv.org/abs/2502.08448'

# citation: ' Jacobsen, Albert Kjøller; Højbjerg, Phillip Chavarria; Jacobsen, Aron Djurhuus. (2022). &quot;Visual Question Answering with Knowledge-based Semantics.&quot; <i>DTU Department of Applied Mathematics and Computer Science </i>.'

---
<p style="text-align: justify"> 
Under review. A preprint is available on <a href="https://arxiv.org/abs/2502.08448">arXiv</a>. <br><br>

Working implementation of the optimizer can be found on <a href="https://github.com/albertkjoller/sharpness-aware-minimizers">this GitHub repository</a>.
</p>

Abstract 
======
<p style="text-align: justify"> Recent studies on deep neural networks show that flat minima of the loss landscape correlate with improved generalization. Sharpness-aware minimization (SAM) efficiently finds flat regions by updating the parameters according to the gradient at an adversarial perturbation. The perturbation depends on the Euclidean metric, making SAM non-invariant under reparametrizations, which blurs sharpness and generalization. We propose Monge SAM (M-SAM), a reparametrization invariant version of SAM by considering a Riemannian metric in the parameter space induced naturally by the loss surface. Compared to previous approaches, M-SAM works under any modeling choice, relies only on mild assumptions while being as computationally efficient as SAM. We theoretically argue that M-SAM varies between SAM and gradient descent (GD), which increases robustness to hyperparameter selection and reduces attraction to suboptimal equilibria like saddle points. We demonstrate this behavior both theoretically and empirically on a multi-modal representation alignment task.</p> <br>
<img src='/images/papers/mongesam.png' alt='Intuition of Monge SAM optimizer' style='display: block; margin-left: auto; margin-right: auto; max-width: 70%; height: auto;'>