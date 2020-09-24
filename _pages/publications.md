---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

The full list of my publications can be found on [Google Scholar](https://scholar.google.com/citations?user=KQL8tB8AAAAJ&hl=en).

<!-- {% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %} -->

Under construction.

testing latex
$$ {X}_{0} $$ (works)
$$ X_0 $$ (works)

$$\begin{aligned}
D_i &= \mathbb E\mathbb E \left(\exp((\lambda - 1)\log {p_i(\xi_i | \xi_{< i}) \over q_i(\xi_i | \xi_{< i})}) \exp((\lambda - 1)\log {p^{i - 1}(\xi_{< i}) \over q^{i - 1}(\xi_{< i})}) \big| \xi_{< i}\right) \\
&= \mathbb E \mathbb E \left(\exp((\lambda - 1)\log {p_i(\xi_i | \xi_{< i}) \over q_i(\xi_i | \xi_{< i})}) | \xi_{< i}\right) \exp\left((\lambda - 1)\log {p^{i - 1}(\xi_{< i}) \over q^{i - 1}(\xi_{< i})}\right)\\
&\le \mathbb E \exp((\lambda - 1) \rho) \exp\left((\lambda - 1)\log {p^{i - 1}(\xi_{< i}) \over q^{i - 1}(\xi_{< i})}\right)\\
&= \exp((\lambda - 1) \rho) D_{i - 1}.
\end{aligned}$$

<!-- 
{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %} -->
