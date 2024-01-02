---
layout: archive
title: "Working Papers"
permalink: /research/
author_profile: true
---
## Corporate Finance
### CEO Overconfidence and Corporate Innovation Under Distress: Evidence from Hurricane Strikes
### Abstract:
Studies have documented a positive relationship between CEO Overconfidence and
corporation innovation, and a negative relationship between natural disasters and corporate innovation outcomes. I study whether overconfidence remains positively related
to innovation following natural disasters. Using a Difference-in-Difference model of
natural disasters occuring between 1998 and 2017, I examine the impact of natural
disasters on corporate innovation between affected firms led by both overconfident and
non-overconfident managers. Firms led with overconfident managers consistently underperform relative to other affected firms, suggesting that overconfident CEOs are
more prone to react negatively under distress, in both cross-sectional and fixed-effect
models. In addition, I find that the negative association between natural disasters and
corporate innovation is mostly driven by firms with Overconfident CEOs. The results
are robust to alternative specifications of both disaster risk and managerial overconfidence. Potential explanatory channels show that overconfident CEOs significantly
reduce R&D expenditure following disasters, which could explain the results of lower
tangibility, higher net working capital, and are more likely to have negative net income.
From an inventors-perspective, I find that innovator productivity remains unchanged
and in some cases increases, however innovators are less willing to work at firms in
affected areas.

### Does Income Inequality Impede Innovation? Evidence from the SEC Mandated Pay Ratio Disclosure
### Abstract:
I examine the importance of an SEC filing rule that enhances pay transparency by
requiring U.S public companies to disclose both employee and CEO compensation. I
test whether this information availability impacts corporate innovation. Firms that
disclose high pay ratios experience lower innovation outcomes three years following
the disclosure. Moreover, innovator output declines following the disclosure of a high
pay ratio. This effect is monotonic decreasing with pay ratio levels. Additionally,
previously available information regarding compensation mitigates the impact of the
disclosure. These effects are robust to various specifications. My results suggest that
innovators are inequality-averse and concerned about high pay dispersion.


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
