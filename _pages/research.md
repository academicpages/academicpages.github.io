---
layout: archive
title: "Research Projects"
permalink: /research/
author_profile: true
---

{% include base_path %}

<center>
  <img src="/images/researchschematic.jpg" alt="Research Methodology Schematic" style="width: 100%; max-width: 900px; border: 1px solid #ddd; padding: 5px;">
  <br>
  <em><strong>Figure 1:</strong> Overview of my framework for Scalable Stability & Robustness Verification of Neural Feedback Systems.</em>
</center>
<br>
## 1. Neural Network Bounding
A critical step in verifying neural feedback loops is creating accurate, tractable mathematical models of the neural network's non-linear behavior. My research focuses on deriving linear "Sector Bounds" that enclose the network's output.

> **Software:** Both the global and the local sector bounds below are available in my open-source library [nnsector](https://github.com/hmon91/nnsector), for Python and MATLAB. See the [Software]({{ base_path }}/software/) page.

### Global Sector Bounds
For global stability analysis, I derived a method to calculate **Global Sector Bounds** for fully connected Feedforward Neural Networks (FFNNs). This method assumes the network has **no bias terms** (or biases are handled separately), ensuring the origin is an equilibrium point.

<div style="display: flex; flex-wrap: wrap; align-items: flex-start; gap: 20px;">
  <div style="flex: 1; min-width: 300px;">
    <ul>
      <li><strong>Method:</strong> We propagate the sector properties of individual activation functions (like ReLU or Tanh) layer-by-layer through the weight matrices.</li>
      <li><strong>Result:</strong> This yields a global linear envelope valid for the entire state space:
      $$\Gamma_1 x \le NN(x) \le \Gamma_2 x$$
      where the bounding matrices are defined as:
      $$\Gamma_1 = -c^q \left( \prod_{i=1}^{q+1} |W^i| \right), \quad \Gamma_2 = c^q \left( \prod_{i=1}^{q+1} |W^i| \right)$$
      </li>
    </ul>
  </div>

  <div style="flex: 0 0 45%; min-width: 250px;">
    <img src="{{ base_path }}/images/NN_sector_bounds.png" alt="Global Sector Bounds" style="width: 100%; border: 1px solid #ddd; padding: 5px;">
    <br>
    <em style="font-size: 0.9em;"><strong>Figure 2:</strong> Validation of Global Sector Bounds. The black line represents the neural network output $NN(z)$, which is strictly contained within the linear envelope formed by the lower bound $\Gamma_1 z$ (blue) and upper bound $\Gamma_2 z$ (red) for all 100 random samples.</em>
  </div>
</div>

#### Performance Comparison
As shown in **Table 1**, our method computes bounds orders of magnitude faster than IQC-based methods while providing tighter envelopes than standard norm-based approximations.

<table style="width:100%; border-collapse: collapse; text-align: center;">
  <thead>
    <tr style="border-bottom: 2px solid #333; background-color: #f9f9f9;">
      <th style="padding: 10px; border: 1px solid #ddd;">Method</th>
      <th style="padding: 10px; border: 1px solid #ddd;">Network Architecture</th>
      <th style="padding: 10px; border: 1px solid #ddd;">Computation Time (s)</th>
      <th style="padding: 10px; border: 1px solid #ddd;">Bounds</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Our Method</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd;">10 / 10 / 1</td>
      <td style="padding: 8px; border: 1px solid #ddd;">$2.5 \times 10^{-5}$</td>
      <td style="padding: 8px; border: 1px solid #ddd;">$\pm[2.65, 1.61]$</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Our Method</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd;">10 / 15 / 15 / 1</td>
      <td style="padding: 8px; border: 1px solid #ddd;">$2.6 \times 10^{-5}$</td>
      <td style="padding: 8px; border: 1px solid #ddd;">$\pm[2.75, 1.47]$</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>IQC Method</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd;">10 / 10 / 1</td>
      <td style="padding: 8px; border: 1px solid #ddd;">$0.68$</td>
      <td style="padding: 8px; border: 1px solid #ddd;">—</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Product of Norms</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd;">10 / 10 / 1</td>
      <td style="padding: 8px; border: 1px solid #ddd;">—</td>
      <td style="padding: 8px; border: 1px solid #ddd;">$5.83$</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Product of Norms</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd;">10 / 15 / 15 / 1</td>
      <td style="padding: 8px; border: 1px solid #ddd;">—</td>
      <td style="padding: 8px; border: 1px solid #ddd;">$6.45$</td>
    </tr>
  </tbody>
</table>

<br>
<em><strong>Table 1:</strong> Comparison of computation time and bound tightness. (10/10/1 denotes a 3-layer NN with 10, 10, and 1 neurons). Note that IQC does not explicitly provide bounds for the entire NN, and Product of Norms is used only for bound comparison, not stability verification.</em>

### Local Sector Bounds
Global bounds can be conservative. To address this, I developed a novel **Local Sector Bound** formulation.

The construction contains the iteration of two stages as shown in **Figure 3**. This is the standard procedure used in calculating other NN bounds like CROWN (Wang et al., 2021).

* **S1:** *Propagate sector bounds through the weight matrix and bias.*
* **S2:** *Sector-bounding the activations $\phi$ over their input interval.*

Iterating **S1–S2** from the input to the output yields constant matrices $\gamma_1, \gamma_2$ such that $\gamma_1 y \le \pi(y) \le \gamma_2 y$ for all $y \in \Lambda$.

<center>
  <img src="{{ base_path }}/images/local_schematic.svg" alt="Local Bound Schematic" style="width: 100%; max-width: 600px; border: 1px solid #ddd; padding: 5px;">
  <br>
  <em><strong>Figure 3:</strong> Schematic illustration of the recursive procedure for computing local sector bounds. We propagate interval bounds layer-by-layer to determine the precise slope matrices $\gamma_1$ and $\gamma_2$.</em>
</center>
<br>

* **Innovation:** By restricting the analysis to a specific compact set of inputs, we calculate tighter, input-dependent slope matrices.
* **Advantage:** These bounds are significantly tighter than norm-based approximations and avoid the affine offsets used in methods like CROWN, making them compatible with robust control frameworks.

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; margin-top: 20px;">
  
  <div style="flex: 1; min-width: 300px; max-width: 500px; text-align: center;">
    <img src="{{ base_path }}/images/difbounds.png" alt="Comparison with CROWN" style="width: 100%; border: 1px solid #ddd; padding: 5px;">
    <br>
    <em style="font-size: 0.9em;"><strong>Figure 4a:</strong> Comparison of bound structure. Our "Local Sector Bound" (yellow) is structurally different from the standard interval-based bounds used in CROWN/IBP, making it suitable for integrating with positive Aizerman conjecture.</em>
  </div>

  <div style="flex: 1; min-width: 300px; max-width: 500px; text-align: center;">
    <img src="{{ base_path }}/images/local_plots.png" alt="Local Stability Plots" style="width: 100%; border: 1px solid #ddd; padding: 5px;">
    <br>
    <em style="font-size: 0.9em;"><strong>Figure 4b:</strong> Visualization of Local Sector Bounds for different input intervals. The yellow region indicates the computed sector, which tightly encloses the neural network's nonlinearity (black line).</em>
  </div>

</div>
<br>

---

## 2. Stability Verification & Safety
Once the neural network is bounded, I use **Control Theory** to certify that the closed-loop system (the robot or plant + the neural network) is stable.

### Positive Aizerman Framework
My verification pipeline relies on the **Positive Aizerman Conjecture**. By embedding the bounded neural network into a "Positive Lur'e System" framework, we reduce the complex stability problem to simple linear algebra checks.

<center>
  <img src="{{ base_path }}/images/aizerman_concept.png" alt="Positive Aizerman Concept" style="width: 100%; max-width: 600px; border: 1px solid #ddd; padding: 5px;">
  <br>
  <em><strong>Figure 5:</strong> Conceptual overview of the Aizerman Framework. We replace the nonlinear feedback $\Phi$ with linear surrogates $k x$ bounded within the sector $[k_1, k_2]$. If the system is stable for these linear bounds, it guarantees stability for the nonlinear system.</em>
</center>
<br>

* **Efficiency:** Instead of solving computationally expensive Linear Matrix Inequalities (LMIs), we simply check if the resulting system matrices are **Metzler** and **Hurwitz**.
* **Scalability:** This approach achieves up to $\approx 10^4\times$ speedup over state-of-the-art methods, enabling verification of larger systems.

<center>
  <img src="{{ base_path }}/images/stability_check.png" alt="Stability Check Diagram" style="width: 100%; max-width: 600px; border: 1px solid #ddd; padding: 5px;">
  <br>
  <em><strong>Figure 6:</strong> The simplified verification condition. By constructing lower and upper linear bounds using our novel sector method, stability is certified by checking if the lower bound is Metzler and the upper bound is Hurwitz.</em>
</center>
<br>

### Region of Attraction (ROA) Analysis
For systems that are not globally stable, I use the Local Sector Bounds to estimate the **Region of Attraction** (ROA).

<center>
  <img src="{{ base_path }}/images/roa_plots.png" alt="ROA Analysis Plots" style="width: 30%; max-width: 600px; border: 1px solid #ddd; padding: 5px;">
  <br>
  <em><strong>Figure 7:</strong> Estimation of the Region of Attraction (ROA). The yellow areas represent the certified safe sets of initial conditions from which the system is guaranteed to converge to the origin, calculated using our local sector bounds.</em>
</center>
<br>

* **Guarantee:** We identify a safe set of initial conditions from which the system is guaranteed to converge to equilibrium.
* **Performance:** Our method certifies larger ROAs than standard IQC-based approaches.

<br>
<h4>Computational Complexity Comparison</h4>
<table style="width:100%; border-collapse: collapse; font-size: 0.9em;">
  <thead>
    <tr style="border-bottom: 2px solid #333; background-color: #f9f9f9; text-align: left;">
      <th style="padding: 10px; border: 1px solid #ddd; width: 20%;">Operation</th>
      <th style="padding: 10px; border: 1px solid #ddd; width: 40%;">Proposed Method (Positive Aizerman)</th>
      <th style="padding: 10px; border: 1px solid #ddd; width: 40%;">IQC-based Method (Yin et al., 2021)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>NN bound computation</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd;">$O(l_0 q N^2)$ (Matrix Multiplication)</td>
      <td style="padding: 8px; border: 1px solid #ddd;">Interval-bound propagation $O(\sum n_i n_{i-1})$ + local slope search $O(n_\phi)$</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Stability check</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd;">Metzler/Hurwitz tests, $O(n_x^2)$<br>(One matrix–vector pass)</td>
      <td style="padding: 8px; border: 1px solid #ddd;">SDP feasibility with var $P \in \mathbb{S}^{n_x+n_\phi}$<br>Complexity $O((n_x+n_\phi)^6)$</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>ROA</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd;">Closed-form inequality<br>$Cx_0 \le \frac{\nu_m}{\nu_M} y_{\max}$</td>
      <td style="padding: 8px; border: 1px solid #ddd;">Ellipsoidal ROA via same SDP as stability<br>$O((n_x+n_\phi)^6)$</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Scalability (NN params)</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd;">Quadratic in NN size ($\sim O(N^2)$)</td>
      <td style="padding: 8px; border: 1px solid #ddd;">Cubic in NN size ($\sim O(n_\phi^3)$) via hidden neurons</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Problem class</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd;">LP-like (no SDP), closed-form</td>
      <td style="padding: 8px; border: 1px solid #ddd;">Full SDP with IQCs; requires solver</td>
    </tr>
    <tr style="border-top: 2px solid #333; background-color: #eef;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Overall Dominant Cost</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>$O(n_x^3 + N^2)$</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>$O((n_x+n_\phi)^6)$</strong></td>
    </tr>
  </tbody>
</table>
<br>

---

## 3. Risk-Aware Safety Verification (Delays & Uncertainty)
Autonomous systems in the real world face two critical risks: **Time Delays** (from communication or computation) and **Parametric Uncertainty** (modeling errors). My research addresses these challenges using two distinct frameworks.

### Method A: Positivity-Based Certificates (Scalable)
To address the computational bottlenecks of traditional methods, I developed a delay-independent verification framework based on **Positive Systems Theory**. 

We characterize the uncertain neural feedback system using the following delayed differential inclusion:

$$\dot{x}(t)=\left[\underline{A}_0, \bar{A}_0\right] x(t)+\sum_{i=1}^l\left(\left[\underline{A}_i, \bar{A}_i\right] x\left(t-\tau_i\right)+B_i \,\Phi\!\big(Cx(t-\tau_i)\big)\right)$$

* **Approach:** This model accounts for both parametric uncertainty in the state matrices and the non-linear activation $\Phi$ of the neural network under time-delays $\tau_i$. By enforcing a "Metzler" structure on the interval bounds, we certify stability for all possible delay values.
* **Key Result:** Robust stability is guaranteed if the lower-bound matrix $\underline{A}$ is Metzler and the resulting interval system is Hurwitz.

<center>
  <img src="{{ base_path }}/images/risk_mitigation_results.png" alt="Delay and Uncertainty Robustness" style="width: 100%; max-width: 700px; border: 1px solid #ddd; padding: 5px;">
  <br>
  <em><strong>Figure 8:</strong> Robustness against structured perturbations and delays. The plot shows sampled trajectories $y(t)$ for systems with varying delays (up to 9.18s), all converging to equilibrium as predicted by the positivity-based certificate.</em>
</center>

* **Performance:** Unlike SDP-based methods that scale cubically with the number of neurons, this algebraic approach maintains efficiency even as the system dimension increases.

### Method B: IQC-Based Framework (High-Fidelity)
As a rigorous benchmark, I developed a comprehensive **Integral Quadratic Constraint (IQC)** pipeline tailored for neural networks with delays and uncertainty.

<div style="float: right; margin: 0 0 20px 20px; max-width: 450px; text-align: center;">
  <img src="{{ base_path }}/images/lft_model.png" alt="LFT Model of NN Feedback" style="width: 100%; border: 1px solid #ddd; padding: 5px;">
  <br>
  <em style="font-size: 0.85em;"><strong>Figure 9:</strong> Linear fractional transformation (LFT) model of the NN-feedback-loop with delay and interval uncertainty.</em>
</div>

* **LFT Modeling:** We model the discrete delays and element-wise interval uncertainty as a **Linear Fractional Transformation (LFT)**. This separates the "troublesome" components (uncertainty blocks $\Delta$) from the nominal plant $G$, as shown in the schematic.
* **Composite IQCs:** We construct a composite IQC filter that combines:
    1.  **Delay IQCs:** Using delay-line filters to bound the energy of the delay operator.
    2.  **Uncertainty IQCs:** Using symmetric box multipliers to bound parametric variations.
    3.  **Neural Network IQCs:** Using sector constraints to bound the nonlinearity.
* **Verification:** Stability is certified by solving a large-scale **Semi-Definite Program (SDP)**. While computationally heavier than Method A, this framework provides a high-fidelity robust control baseline for AI-enabled systems, ensuring they can handle worst-case scenarios.

<div style="clear: both;"></div>

---

## 4. Crowd Dynamics & Emergency Evacuation
Beyond neural network verification, my research extends to **multi-agent systems** and public safety. I develop dynamical models to simulate and optimize crowd behavior under high-stress conditions, specifically focusing on active shooter scenarios.

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; margin-bottom: 20px;">
  
  <div style="flex: 1; min-width: 300px; max-width: 450px; text-align: center;">
    <video width="100%" controls autoplay loop muted playsinline style="border: 1px solid #ddd; display: block;">
      <source src="/images/evacuation_baseline.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <br>
    <div style="text-align: left; font-size: 0.9em; line-height: 1.4em; padding: 5px;">
      <em><strong>Simulation A: Uncoordinated Evacuation (Baseline).</strong><br>
      In the absence of an optimized guidance strategy, the crowd (blue agents) relies solely on local repulsive forces. This results in disorganized scattering, increasing vulnerability to the predator (red cross) and yielding higher casualty rates ($K$).</em>
    </div>
  </div>

  <div style="flex: 1; min-width: 300px; max-width: 450px; text-align: center;">
    <video width="100%" controls autoplay loop muted playsinline style="border: 1px solid #ddd; display: block;">
      <source src="/images/evacuation_optimized.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <br>
    <div style="text-align: left; font-size: 0.9em; line-height: 1.4em; padding: 5px;">
      <em><strong>Simulation B: Optimized Guidance Strategy.</strong><br>
      Implementing our tuned parameters ($\alpha=1.625, \lambda=0.71$), the designated guide (green cross) dynamically steers the swarm toward the Safe Zone (green region). This cooperative behavior significantly mitigates casualties by optimizing the trade-off between evasion and evacuation.</em>
    </div>
  </div>

</div>

### The Predator-Swarm-Guide (PSG) Model
We proposed the **Predator-Swarm-Guide (PSG)** model, a hybrid framework designed to capture the complex interplay between three distinct agent types:
1.  **The Predator:** A non-cooperative agent that actively tracks and repels the crowd.
2.  **The Swarm:** A multi-agent system governed by social force interactions (pairwise repulsion/attraction) and environmental constraints.
3.  **The Guide:** A strategic agent tasked with steering the swarm toward a designated "Safe Zone" while minimizing interaction with the predator.

### Key Contributions
* **Dynamic Guidance Formulation:** We modeled the guide's trajectory using a weighted objective function parameterized by $\lambda$, which balances the competing goals of "target acquisition" (moving to safety) and "threat evasion" (avoiding the shooter).
* **Optimization of Casualty Mitigation:** We formulated a nonlinear optimization problem to tune the crowd cohesion parameter ($\alpha_1$) and the guidance weight ($\lambda$). Our results demonstrate that rational cooperation between the guide and the swarm significantly reduces total casualties compared to baseline evacuation methods.
* **Continuum Limit Analysis:** By deriving the mean-field approximation of the particle model, we provided theoretical characterizations of the crowd's steady-state spatial distribution, predicting emergent formations such as annular clustering around the threat.

---

### Related Publications
1. **H. Montazeri Hedesh**, M. Siami. "Delay-Independent Safe Control with Neural Networks: Positive Lur'e Certificates for Risk-Aware Autonomy," *American Control Conference (ACC)*, 2026. [[PDF]](/publication/2026-05-01-acc-delay)
2. **H. Montazeri Hedesh**, M. Wafi, M. Siami. "Local Stability and Region of Attraction Analysis for Neural Network Feedback Systems under Positivity Constraints," *IEEE CDC*, 2025. [[PDF]](/publication/2025-12-12-cdc-paper)
3. **A. Darabi, H. M. Hedesh**, M. Siami, M. Sznaier. "Predator-Swarm-Guide Dynamics: A Hybrid Approach to Crowd Modeling and Guidance in Mass Shooting Scenarios," *American Control Conference (ACC)*, 2024. [[PDF]](/publication/2024-07-01-acc-predator)
4. **H. Montazeri Hedesh**, M. Siami. "Ensuring Both Positivity and Stability Using Sector-Bounded Nonlinearity for Systems With Neural Network Controllers," *IEEE Control Systems Letters*, 2024. [[PDF]](/publication/2024-01-01-lcss-positivity)
