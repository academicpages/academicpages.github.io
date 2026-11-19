---
layout: archive
title: "Software"
description: "nnsector and nnstab: open-source Python and MATLAB libraries for sector bounds of neural networks and stability checks of neural feedback loops."
permalink: /software/
author_profile: true
---

{% include base_path %}

Two open-source libraries, in Python and MATLAB, for certifying feedback loops that contain a neural network. **nnsector** bounds the network, and **nnstab** uses those bounds to check that the closed loop is stable.

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
* **Global sector bounds** that need no box, with $$\Gamma_2 = c^q \lvert W_{q+1} \rvert \cdots \lvert W_1 \rvert$$, the bound of my [L-CSS 2024 paper]({{ base_path }}/publication/2024-01-01-lcss-positivity). For a network without biases (with tanh, ReLU or leaky ReLU), $$-\Gamma_2\, y \le \pi(y) \le \Gamma_2\, y$$ for every $$y \ge 0$$. With biases, $$\Gamma_2$$ bounds the change between any two inputs: $$\lvert \pi(y) - \pi(y^*) \rvert \le \Gamma_2 \lvert y - y^* \rvert$$.
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
gb = ns.global_bound(net)                              # global bound on pi(y) - pi(y*)
```

The [README](https://github.com/hmon91/nnsector#readme) explains networks with several inputs, the options, and how the bound is computed.

## nnstab

[![tests](https://github.com/hmon91/nnstab/actions/workflows/tests.yml/badge.svg)](https://github.com/hmon91/nnstab/actions/workflows/tests.yml)

**Stability checks for feedback loops with a neural network controller, in Python and MATLAB.**<br>
[GitHub repository](https://github.com/hmon91/nnstab) · [BSD 3-Clause license](https://github.com/hmon91/nnstab/blob/main/LICENSE)

You give it a plant and the trained network that closes the loop:

$$
\dot{x} = A x + B u, \qquad y = C x, \qquad u = \pi(y).
$$

nnstab checks whether the closed loop is exponentially stable: every solution goes to 0 at least as fast as a decaying exponential. It bounds the network with nnsector and then uses the positive Aizerman conditions, so each test comes down to two matrix checks. With the lower and upper sector slopes $$\gamma_1$$ and $$\gamma_2$$, the matrix $$A + B \gamma_1 C$$ must be Metzler (every entry off the diagonal is $$\ge 0$$) and $$A + B \gamma_2 C$$ must be Hurwitz (every eigenvalue has a negative real part).

### What it does

* **Global test:** is the loop stable for every starting state $$x_0 \ge 0$$? It uses the global sector bound, as in my [L-CSS 2024 paper]({{ base_path }}/publication/2024-01-01-lcss-positivity).
* **Local test:** if the global test fails, nnstab searches for the largest region of starting states around 0 from which every solution goes to 0, as in my [CDC 2025 paper]({{ base_path }}/publication/2025-12-12-cdc-paper).
* **A guaranteed decay rate** in the region, and the option `min_decay` to ask for a faster rate on a smaller region.
* **No solver needed:** the tests use eigenvalues and a few linear solves, with no semidefinite program and no LP solver.
* **A simulator** to test a result from random starting states in the certified region.
* **PyTorch models** or nnsector networks as the controller, and the same functions in Python and MATLAB. The MATLAB version also runs in GNU Octave.

The tests are for positive systems, where the states never become negative. Every entry of $$B$$ and $$C$$ must be $$\ge 0$$, and $$\pi(0) = 0$$, which holds for example for a network without biases with tanh, ReLU or leaky ReLU activations. $$A$$ does not have to be stable on its own, because the controller may be what makes the loop stable. nnstab checks these conditions and tells you if one of them does not hold.

### Install

**Python** (3.10 or newer):

```bash
pip install git+https://github.com/hmon91/nnstab.git
```

This also installs nnsector.

**MATLAB** (R2016b or newer) or **GNU Octave**: download the [repository](https://github.com/hmon91/nnstab) and add its `matlab` folder to the path, together with the one from nnsector.

```matlab
addpath('path/to/nnsector/matlab')
addpath('path/to/nnstab/matlab')
```

### Quick start

The example loop has an unstable plant (one eigenvalue of $$A$$ is 0.95) and a small tanh network without biases, trained to act like the controller $$u = -\tanh(2y) - 0.5y$$. Near 0 the controller makes the loop stable, but far away it is too weak, so no global test can pass. nnstab finds a region of attraction instead:

```python
import nnstab as nst

A, B, C, net = nst.example_system("local")   # or your own plant and network
res = nst.verify(A, B, C, net)
print(res)
```

```
Locally exponentially stable (the global test failed).
  region: {x >= 0 : v^T x <= 3.563},  v = [1.929, 2.089, 1]
  it holds every x0 >= 0 with sum(x0) <= 1.706
  in it: sum(x(t)) <= 2.09 exp(-0.000324 t) sum(x0)
  ...
```

So every solution that starts at an $$x_0 \ge 0$$ with $$x_1 + x_2 + x_3 \le 1.706$$ goes to 0. The same in MATLAB:

```matlab
[A, B, C, net] = nnstab.example_system('local');
res = nnstab.verify(A, B, C, net);
nnstab.report(res)
```

The [README](https://github.com/hmon91/nnstab#readme) explains the options, the results, and how the tests work.

## Citing

If you use nnsector, please cite [1]. If you use nnstab, please cite [1] and [2].

[1] H. Montazeri Hedesh, M. K. Wafi, and M. Siami, "Local Stability and Region of Attraction Analysis for Neural Network Feedback Systems under Positivity Constraints," in *2025 IEEE 64th Conference on Decision and Control (CDC)*, Rio de Janeiro, Brazil, 2025. [IEEE Xplore](https://ieeexplore.ieee.org/document/11312171) · [arXiv:2505.22889](https://arxiv.org/abs/2505.22889)

[2] H. Montazeri Hedesh and M. Siami, "Ensuring Both Positivity and Stability Using Sector-Bounded Nonlinearity for Systems With Neural Network Controllers," *IEEE Control Systems Letters*, vol. 8, pp. 1685-1690, 2024. [IEEE Xplore](https://ieeexplore.ieee.org/document/10561541) · [arXiv:2406.12744](https://arxiv.org/abs/2406.12744)

```bibtex
@inproceedings{montazerihedesh2025local,
  author    = {Montazeri Hedesh, Hamidreza and Wafi, Moh Kamalul and Siami, Milad},
  title     = {Local Stability and Region of Attraction Analysis for Neural Network
               Feedback Systems under Positivity Constraints},
  booktitle = {2025 IEEE 64th Conference on Decision and Control (CDC)},
  year      = {2025},
  doi       = {10.1109/CDC57313.2025.11312171}
}

@article{montazerihedesh2024ensuring,
  author  = {Montazeri Hedesh, Hamidreza and Siami, Milad},
  title   = {Ensuring Both Positivity and Stability Using Sector-Bounded Nonlinearity
             for Systems With Neural Network Controllers},
  journal = {IEEE Control Systems Letters},
  volume  = {8},
  pages   = {1685--1690},
  year    = {2024},
  doi     = {10.1109/LCSYS.2024.3416237}
}
```

---

The code that reproduces each of my papers is linked from the [Publications]({{ base_path }}/publications/) page.
