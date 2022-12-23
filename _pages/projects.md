---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

My research interests are broadly in the stability, robustness, and functional properties of nonlinear networks. My major thrusts can be categorized as: 1) dynamical properties of neural networks, 2) contraction theory and monotone operators for control and learning, and 3) multi-robot coverage control.

***
# Dynamical Properties of Neural Networks

Neural networks are a simple yet powerful class of deep learning architectures whose primary task is to provide a mathematical representation of some complex underlying physical process. I have been interested in studying the properties of various classes of dynamical neural networks, focusing on Hopfield neural networks and other firing-rate models. I have investigated conditions under which these dynamical models are contracting and thus have strong robustness guarantees. I am currently interested in functional properties of neural networks, i.e., given a neural network, what is the optimization problem it is solving? I am also interested in multistability in Hopfield networks and computational properties of modern Hopfield networks. 

In the direction of machine learning, I have studied deep equilibrium networks (DEQs) which are a class of neural networks where layers are replaced by implicit fixed-point equations. In this line of work, I have provided novel sufficient conditions for the well-posedness of DEQs and have provided novel training algorithms for them. I have also studied the robustness of DEQs using contraction theory and mixed monotonicity theory to provide rigorous certificates for the provable robustness of these architectures.

***
# Contraction Theory and Monotone Operators for Control and Learning

Contraction theory is a framework of nonlinear robust stability for dynamical systems. A dynamical system is said to be contracting if any two trajectories come together at an exponential rate in some metric. Contraction is a continuous-time analogy of the classical contraction mapping theorem and implies many strong stability and robustness properties of the underlying system. I am interested in fundamental questions at the heart of non-Euclidean contraction theory, i.e., when a system is contracting with respect to a non-Euclidean norm. Broadly speaking, I am interested in creating non-Euclidean analogs of many of the classical linear-quadratic problems that we are taught in our controls courses and providing computationally scalable strategies to solve them.

Parallel to contraction theory is the theory of monotone operators, which is closely tied to the study of convex optimization. In fact, it is known that the gradient of a strongly convex function is monotone and the negative gradient flow is strongly contracting. Indeed, there are many ties between contraction theory and monotone operator theory, but there are some subtle differences. For instance, many operator splitting schemes in monotone operator theory do not have a natural continuous-time analog that is contracting by design. In a different direction, I have also studied operators that are monotone with respect to a non-Euclidean norm and have demonstrated that many classical results from monotone operator theory carry over essentially for free. 

***
# Multi-Robot Coverage Control

Coverage control aims to address the problem of resource allocation within a domain of interest. For arbitrary domains and regions of interest, finding globally optimal resource allocation configurations is an NP-hard problem. My work has focused on using tools from computational geometry and network systems theory to give sufficient conditions on the optimality of a configuration of agents. Additionally, I am interested in the robustness of different coverage control strategies. One application that I have focused on is the deployment of a team of lower-mobility aerial vehicles to persistently measure wind data in a wind farm for better characterization of wind turbine wakes. 

## Sparsity Structure and Optimality of Multi-Robot Coverage Control
<iframe src="https://www.youtube.com/embed/Zpz-Co44Zyg" width="480" height="270" ></iframe>

<!-- <iframe src="https://www.youtube.com/embed/Hova4bMiVZg" width="480" height="270" ></iframe> -->

## Low-Mobility Atmospheric Sampling

<iframe src="https://www.youtube.com/embed/LY9-zRbFIK0" width="480" height="270" ></iframe>

<!-- <img src= "/images/foo-bar-identity-th.jpg" alt = "sample image"> -->

<!-- {% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %} -->

{% include base_path %}

<!-- {% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %} -->
