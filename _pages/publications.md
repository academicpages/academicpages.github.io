---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

Cui, Y., Yang, J. and Zhou, Z. (2023) State-domain change point detection for nonlinear time series regression. Journal of Econometrics, 234, 3-27.
Cui, Y., Levine, M. and Zhou, Z. (2021) Estimation and inference of time-varying auto-covariance under complex trend: A difference-based approach. Electronic Journal of Statistics, 15, 4264-4294.
Cui, Y., Li, Q. and Zhu, F. (2021). Modeling Z-valued time series based on new versions of the Skellam INGARCH model. Brazilian Journal of Probability and Statistics, 35, 292-314.
Mao, H., Zhu, F. and Cui, Y. (2020). A generalized mixture integer-valued GARCH model. Statistical Methods & Applications, 29, 527-552.
Cui, Y., Zhu, F. and Li, W.K. (2020) Modeling RCOV matrices with a generalized threshold conditional autoregressive Wishart model. Statistics and Its Interface, 13, 77-89.
Cui, Y., Li, Q. and Zhu, F. (2020) Flexible bivariate Poisson integer-valued GARCH model, An nals of the Institute of Statistical Mathematics. 72, 1449-1477.
Cui Y. and Zhu, F. (2018) A new bivariate integer-valued GARCH model allowing for negative cross-correlation. TEST, 2, 428-452.


{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
