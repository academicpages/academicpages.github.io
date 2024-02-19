---
layout: archive
title: "Working Papers"
permalink: /research/
author_profile: true
---
## Corporate Finance
### Confident CEOs, Unsteady Times: Corporate Innovation Following Natural Disasters
### Abstract:
Studies have documented a positive relationship between CEO Overconfidence and corporation
innovation, and a negative relationship between natural disasters and corporate innovation outcomes.
I examine the role of overconfidence in mediating the latter effect. Using a Difference-in-Difference
model of natural disasters occurring between 1998 and 2017, I examine the impact of natural
disasters on corporate innovation between affected firms led by both overconfident and non-
overconfident managers. Firms led with overconfident managers consistently underperform relative to
other affected firms, suggesting that overconfident CEOs are more prone to react negatively under
distress, in both cross-sectional and fixed-effect models. In addition, I find that the negative
association between natural disasters and corporate innovation is mostly driven by firms with
Overconfident CEOs. The results are robust to alternative specifications of both disaster risk and managerial overconfidence. 


### Inventor's Inequality Aversion
### Abstract:
I investigate the impact of inequality aversion on corporate innovation
outcomes, specifically examining its variation across racial and ethnic lines among
innovators by using Machine Learning to identify the characteristics of innovators. Using
a quasi-natural experiment that required public U.S. firms to disclose both CEO and
median employee pay, I find that although innovators are generally inequality averse,
variations in aversion exist. Specifically, women, older individuals, and minority
inventors exhibit higher levels of inequality aversion compared to men, younger
individuals, and white inventors. This finding suggests a potential explanation for the
observed disparity in innovation output between these groups. To further validate this
hypothesis, I rely on previously disclosed information related to labor expenses and find
that the effect is mitigated when a firm previously disclosed that information in their
financial statements. Moreover, the drift between the expected pay of a CEO and the
actual pay of CEO is higher, the innovation outcomes are lower. Conversely, the higher
the drift between the expected pay of employees and the actual pay, the higher the
innovation outcome. Altogether, these results show the presence of inequality aversion
among inventors and its consequential effects on innovation when information becomes
more available.


## Risk Management and Insurance
### The National Flood Insurance Program, Racial and Ethnic Disparity, and the Pursuit of Environmental Justice. 
*With Jing Ai*
### Abstract: 
Flood insurance by the NFIP is the most important risk management infrastructure in the 
U.S. to protect vulnerabilities and build resilience to increasing natural disasters. Racial 
and ethnic minorities comprise the most vulnerable populations. We examine disparities 
in insurance outcomes for these groups. Using a combined dataset of nationwide flood 
insurance policies and claims, and census tract level demographics, we find that 
minorities tend to pay higher premium, obtain less coverage per premium dollar, and 
have a lower likelihood of getting claims paid. They also have lower insurance take up 
rates. To aid identification, we utilize an exogenous shock of losing the Minority Tract 
designation. We also find that while social vulnerability leads to less favorable insurance 
outcomes, being racial/ethnic minority exacerbates the effects. More nuanced effects 
across minority groups are also identified. Our results add to the discussions on 
discrimination by institutions and have significant public policy implications.

### The Demographics of Property Insurance: Evidence from the Homeowners Insurance Market. 
*With Jing Ai and Charles Nyce*
### Abstract:
We provide evidence that there is a disparate impact on minorities of the availability of private 
market property insurance in Florida. We show that demographic factors explain reduced private 
market penetration. Results are largely consistent between the two measures of residual market 
(Citizens’) market presence (policy count, total exposure) and across the fixed effects models 
with or without the spatial lag. In general, we find that while risk exposure does seem to be 
contribute significantly to Citizens’ presence, supporting its purpose as a last resort insurer, both 
its market share and property risk exposure are significantly higher in minority concentrated 
census block groups.

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.research reversed %}
  {% include archive-single.html %}
{% endfor %}
