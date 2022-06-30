---
layout: archive
title: "Codes"
permalink: /code/
title: "Causal Inference and ML Bookdown"
author_profile: true

---

## Applied Statistics: Causal Inference in Economic Analysis and Machine Learning Methods

You will find my repository [here](https://github.com/Angela-Coapaza/Causal_Inference_and_Machine_Learning). In this repo there are replications of the following case studies in R, Python and Julia carried out in the Applied Statistics course at PUCP:

* [1. Introduction to Causal Inference](https://github.com/Angela-Coapaza/Causal_Inference_and_Machine_Learning/tree/main/1.%20Introduction%20to%20Causal%20Inference)

  In this section, we analyze the pay gap between women and men using the March Supplement U.S. Current Population Survey (2015) and job-relevant characteristics, especially in the subset of college-educated workers. Our results indicate that women earn 8.15% less than men, despite the fact that women have an average experience of 12 years.
  We also add the proof of the Frisch-Waugh-Lovell Theorem.

* [2. Partialling-Out using Lasso](https://github.com/Angela-Coapaza/Causal_Inference_and_Machine_Learning/tree/main/2.%20Partialling-Out%20using%20lasso)

  Using the same data base from the March Supplement of the U.S. Current Population Survey and select white non-hispanic individuals, aged 25 to 64 years, and working more than 35 hours per week during at least 50 weeks of the year, we are going  to construct the variable Y which is the hourly wage rate constructed as the ratio of the annual earnings to the total number of hours worked. Next, we use the lasso for partialling-out the basic regressions and we find that this mehod give us a different result compared to a basic OLS regression regarding the gender wage gap (12% versus 7% respectively). We also add the definition and process of Data Splitting. 

* [3. RCT data with Precision Adjusment](https://github.com/Angela-Coapaza/Causal_Inference_and_Machine_Learning/tree/main/3.%20RCT%20data%20with%20Precision%20Adjustment)

  First, we explain multicollinearity in a markdown. Then we analyze the Pennsylvania re-employment bonus experiment, which was previously studied in "Sequential testing of duration data: the case of the Pennsylvania ‘reemployment bonus’ experiment" (Bilias, 2000), among others. In these experiments, unemployment insurance (UI) claimants were randomly assigned either to a control group or one of five treatment groups. Actually, there are six treatment groups in the experiments. Here we focus on treatment group 2. . Individuals in the treatment groups were offered a cash bonus if they found a job within some pre-specified period of time (qualification period), provided that the job was retained for a specified duration. The treatments differed in the level of the bonus, the length of the qualification period, and whether the bonus was declining over time in the qualification period. To analyze this experiment we used a classical 2-sample approach, no adjustment (CL); a classical linear regression adjustment (CRA); an interactive regression adjustment (IRA) and an interactive regression adjustment (IRA) using Lasso.
  
* [4. Orthogonal Learning, Double Lasso and God and Bad Controls](https://github.com/Angela-Coapaza/Causal_Inference_and_Machine_Learning/tree/main/4.%20Orthogonal%20Learning%20and%20Double%20Lasso)

  Here we replicate an experiment on orthogonal learning in Julia. Then, we used the Double Lasso to test the convergence hypthesis,which is that poor countries will grow at higher rates than rich countries. Next, we prove the Neyman Orthogonality Condition and finally we created a tutorial about good and bad controls based on Cinelli et all 2022.
* [5.Causal Tree ](https://github.com/Angela-Coapaza/Causal_Inference_and_Machine_Learning/tree/main/5.%20Bootstraping%20and%20Causal%20Tree)

 First, we go step by step through the construction of a Bootstrapping.Using the U.S. March Supplement of the Current Population Survey (CPS) in 2015 we illustrate how to predict an outcome variable Y in a high-dimensional setting, where the number of covariates is large in relation to the sample size . Aside from linear prediction rules, and Lasso regression, we also consider nonlinear prediction rules including tree-based methods. Finally, we explain how to build a tree regression and to prune a tree.

* [6.Causal Forest & Debiased Machine Learning ](https://github.com/Angela-Coapaza/Causal_Inference_and_Machine_Learning/tree/main/6.%20Causal%20Forest%20and%20Debiased%20Machine%20Learning)

  In this section we replicate the paper of Athey and Wager (2018) in python .

It is important to mention that the replicated codes in R, Python and Julia were were made under a collaborative work with Ana Angulo and Andrea Ulloa.

