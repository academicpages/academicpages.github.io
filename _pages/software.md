---
layout: archive
title: "Software"
permalink: /software/
author_profile: true
---

{% include base_path %}

## nnsector

[![tests](https://github.com/hmon91/nnsector/actions/workflows/tests.yml/badge.svg)](https://github.com/hmon91/nnsector/actions/workflows/tests.yml)

**Sector bounds for feedforward neural networks, in Python and MATLAB.**<br>
[GitHub repository](https://github.com/hmon91/nnsector) · [BSD 3-Clause license](https://github.com/hmon91/nnsector/blob/main/LICENSE)

nnsector is an open-source library for the stability analysis of feedback loops that contain a neural network, for example as the controller, observer or sensor. You give it a trained network, a point $$y^*$$ and a box around that point. It gives back two slopes $$\gamma_1 \le \gamma_2$$ such that, on the box, the network stays between the two lines through $$(y^*, \pi(y^*))$$ with these slopes. For a network with one input, every $$y \ne y^*$$ in the box satisfies

$$
\gamma_1 \;\le\; \frac{\pi(y) - \pi(y^*)}{y - y^*} \;\le\; \gamma_2 .
$$

This is the form that absolute-stability tests need (circle criterion, Lur'e systems, positive Aizerman conditions). For positive systems, the stability check then comes down to simple Metzler and Hurwitz matrix tests instead of a large semidefinite program.

### What it does

* **Local sector bounds** on a box around any point $$y^*$$, for networks with or without biases. This is the method of my [CDC 2025 paper]({{ base_path }}/publication/2025-12-12-cdc-paper).
* **Global sector bounds** that hold for every input: $$\Gamma_2 = c^q \lvert W_{q+1} \rvert \cdots \lvert W_1 \rvert$$ and $$\Gamma_1 = -\Gamma_2$$, the bound of my [L-CSS 2024 paper]({{ base_path }}/publication/2024-01-01-lcss-positivity).
* **Five activations:** tanh, sigmoid, ReLU, leaky ReLU and softplus.
* **PyTorch models:** `Network.from_torch(model)` reads an `nn.Sequential` network.
* **A sampling check:** `check(net, bound)` tests a bound on many random points, so a wrong bound gets caught.
* **Python and MATLAB** with the same functions. The MATLAB version also runs in GNU Octave.

### Install

**Python** (3.10 or newer, needs NumPy):

```bash
pip install git+https://github.com/hmon91/nnsector.git
```

To read PyTorch models, also install PyTorch.

**MATLAB** (R2016b or newer) or **GNU Octave**: download the [repository](https://github.com/hmon91/nnsector) and add its `matlab` folder to the path.

```matlab
addpath('path/to/nnsector/matlab')
```

### Quick start

A small demo network ships with the library. It has one input, two hidden layers of 8 tanh neurons and one output, and it was trained to act like the controller $$u = -\tanh(2y) - 0.5y$$.

```python
import nnsector as ns

net = ns.demo_network()
sb = ns.local_bound(net, -1, 1)    # box [-1, 1] around y* = 0
print(sb.gamma1, sb.gamma2)        # about -2.786 and -1.200
print(ns.check(net, sb))           # test the bound on random samples
```

The true secant slopes of this network on $$[-1, 1]$$ lie in $$[-2.520, -1.463]$$, so the bound is close. The same in MATLAB:

```matlab
net = nnsector.demo_network();
sb  = nnsector.local_bound(net, -1, 1);   % sb.gamma1 = -2.786, sb.gamma2 = -1.200
```

For your own network, pass its weights and biases, or a PyTorch model:

```python
net = ns.Network([W1, W2, W3], [b1, b2, b3], activation="relu")   # from weights and biases
net = ns.Network.from_torch(model)                                # or from a PyTorch model

sb = ns.local_bound(net, y_lo=-1, y_hi=1, ystar=0.5)   # local bound around y* = 0.5
gb = ns.global_bound(net)                              # global bound
```

The [README](https://github.com/hmon91/nnsector#readme) explains networks with several inputs, the options, and how the bound is computed.

### Citing

If you use nnsector, please cite:

H. Montazeri Hedesh, M. K. Wafi, and M. Siami, "Local Stability and Region of Attraction Analysis for Neural Network Feedback Systems under Positivity Constraints," in *2025 IEEE 64th Conference on Decision and Control (CDC)*, Rio de Janeiro, Brazil, 2025. [IEEE Xplore](https://ieeexplore.ieee.org/document/11312171) · [arXiv:2505.22889](https://arxiv.org/abs/2505.22889)

```bibtex
@inproceedings{montazerihedesh2025local,
  author    = {Montazeri Hedesh, Hamidreza and Wafi, Moh Kamalul and Siami, Milad},
  title     = {Local Stability and Region of Attraction Analysis for Neural Network
               Feedback Systems under Positivity Constraints},
  booktitle = {2025 IEEE 64th Conference on Decision and Control (CDC)},
  year      = {2025},
  doi       = {10.1109/CDC57313.2025.11312171}
}
```

---

The code that reproduces each of my papers is linked from the [Publications]({{ base_path }}/publications/) page.
