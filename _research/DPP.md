---
title: "Chronic Disease Prevention Intervention"
layout: single-portfolio
excerpt: "<img src='/images/research/DPP-new.png' alt=''>"
collection: research
order_number: 3
header: 
  og_image: "/images/research/DPP-new.png"

gallery:
  - url: "research/DPP-new.png"
    image_path: "research/DPP-new.png"
    alt: "Results of a 5 year DPP LCP study"
    title: "Results of a 5 year DPP LCP study"

  - url: "research/dpp-results.png"
    image_path: "research/dpp-results.png"
    alt: "Results of a 5 year DPP LCP study"
    title: "Results of a 5 year DPP LCP study"
---

The National Diabetes Prevention Program (DPP) established by the Centers for Disease Control and Prevention (CDC) promotes the implementation of an evidence-based lifestyle change program (LCP) to prevent or delay the onset of diabetes. The LCP is a 12-month program with 26 lessons covering topics on healthy diets, increasing physical activity, managing stress, and coping with triggers, among others. It includes weekly goal-setting, food and physical activity tracking, and group support. Little is known about the real-world effectiveness of the LCP in different age groups, particularly in older adults. The aim of this study was to evaluate the effects of age on LCP outcomes (weight loss, average physical activity, program attendance) conducted by Virginia Cooperative Extension from 2018 - 2022. 


## Data Analysis

The collected data is anonymously stored in the __Data Analysis of Participants System__ (DAPS) [databse](https://nationaldppcsc.cdc.gov/s/article/ format and the DPRP-Data-Submission-Conversion-from-the-2018-Format-to-the-2021-Format). For statistical analysis involving the outcomes of the LCP program, only the participants that completed at least eight sessions in the first 6 months of the program were considered. 

From the long-form data a summary of each participants average physical activity and weight loss normalized by the initial weight  and the number of sessions attended is created. Each participant appears once in this summary table; therefore, the study is a between-subject design. Regression is performed when a linear correlation is hypothesized between an outcome and an independent factor. Unless the hypothesized relationship explicitly warrants a zero-intercept, all linear models are constructed with intercepts and regressed using ordinary least squares with t-tests for the significance of coefficients.  

To assess the differences in LCP outcomes between different groups, we perform t-tests followed up by post-hoc tests to assess various hypotheses about the means of outcomes among different groups. The underlying assumption is that the means of any outcome variable is a normally distributed random variable. The conventional ANOVA analysis requires the extra assumption that the variance of the random variable considered is the same across the groups. Our analysis uses the more robust Welch-ANOVA tests that work better with unequal variances across groups. If the main effect is observed, pairwise  Games-Howell[^1]  test is administered to establish the effect in different groups. 

[^1]: Games, Paul A., and John F. Howell. “Pairwise multiple comparison procedures with unequal n’s and/or variances: a Monte Carlo study,” Journal of Educational Statistics 1.2 (1976): 113-125

[^2]: Vallat, R. (2018). Pingouin: statistics in Python. Journal of Open Source Software, 3(31), 1026, https://doi.org/10.21105/joss.01026 
[^3]: Seabold, Skipper, and Josef Perktold. “statsmodels: Econometric and statistical modeling with python.” Proceedings of the 9th Python in Science Conference. 2010. 



All data manipulation is performed using Python with data aggregation and cleanup using the [Pandas](https://doi.org/10.5281/zenodo.3509134) package, statistical tests using [Pingouin](https://pingouin-stats.org/) package[^2] and regressions done using the [statsmodels](https://www.statsmodels.org/stable/index.html) package[^3]. 




{% include gallery caption="" %}

## Results

Among 189 participants enrolled in the LCP, 139 (73%) completed eight or more sessions, and 56% were above 60 years of age. Results show there was a significant direct relationship (coefficient=0.05, p=0.001) between age and weight loss percentage. Participants older than 60 had significantly (p=0.03) higher average physical activity (215 min per week) compared to those under 60 years old (161 min per week). In addition, participants above 60 had significantly (p=0.03) higher attendance (22 sessions) compared to those under 60 years of age (19 sessions). These findings suggest that targeting different age groups and intervention delivery methods can improve program outcomes. 

