---
layout: archive
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

* [3. Potential Outcomes and RCTs](https://github.com/Angela-Coapaza/Causal_Inference_and_Machine_Learning/tree/main/3.%20RCT%20data%20with%20Precision%20Adjustment)

  In this lab, we analyze the Pennsylvania re-employment bonus experiment, which was previously studied in "Sequential testing of duration data: the case of the Pennsylvania ‘reemployment bonus’ experiment" (Bilias, 2000), among others. These experiments were conducted to test the incentive effects of alternative compensation schemes for unemployment insurance (UI). In these experiments, UI claimants were randomly assigned either to a control group or one of five treatment groups and we will focus on treatment group 2. Individuals in the treatment groups were offered a cash bonus if they found a job within some pre-specified period of time (qualification period), provided that the job was retained for a specified duration. The treatments differed in the level of the bonus, the length of the qualification period, and whether the bonus was declining over time in the qualification period. We run classical 2-sample approach, no adjustment (CL), Classical linear regression adjustment (CRA) and Interactive regression adjustment (IRA). IRA regression estimators delivers estimates that are slighly more efficient (lower standard errors) than the simple 2 mean estimator, but essentially all methods have very similar standard errors. From IRA results we also see that there is not any statistically detectable heterogeneity. Also, we explain what is multicollinearity as well as perfect and imperfect multicollinearity. 

* [4.Double Lasso and Testing the Convergence Hypothesis](https://github.com/stephyriega/ML_CI/tree/main/Double%20Lasso%20-%20Testing%20the%20Convergence%20Hypothesis)

  We used a Double Lasso, a method that is used to infer the predictive effect of a specific covariable using Lasso twice in a Partialling-Out process. This is useful when having a high-dimensional regression, that is when p/n is not small where p is the number of regressor or covariates and n the number of observtations. We are interesed in testing the the Convergence Hypothesis, meaning that we are interesed in how the rates at which economies of different countries grow (Y) are related to the initial wealth levels in each country (D) controlling for country's institutional, educational, and other similar characteristics (W). Since the OLS provides a rather noisy estimate (high standard error) of the speed of convergence, and does not allow us to answer the question about the convergence hypothesis since the confidence interval includes zero, we test Double Lassos results. We found that it provides a more precise estimate (lower standard error). The Lasso based point estimate is about 5% and the 95% confidence interval for the (annual) rate of convergence is 7.8% to 2.2%.

* [5.Causal Tree ](https://github.com/stephyriega/ML_CI/tree/main/Causal%20Tree)

  The bootstrap approach can be used to assess the variability of the coefficient estimates and predictions from a statistical learning method. Here we use the bootstrap approach in order evaluate the impact of the treatment four on unemployment duration. If the RCT assumptions hold rigorously, we could estimate the ATE. However, this may obscure important details about how different groups of individuals react to the treatment, as we have seen in the heteregenous model. We can calculate this using the conditional average treatment effect (CATE). Pre-specifying hypotheses prior to looking at the data is in general good practice to avoid "p-hacking" (e.g., slicing the data into different subgroups until a significant result is found). However, valid tests can also be attained if by sample splitting: we can use a subset of the sample to find promising subgroups, then test hypotheses about these subgroups in the remaining sample. This kind of sample splitting for hypothesis testing is called honesty. Using Causal Tree, we found that in general the HTE found in the subgroups are different, that is, the effect of the program in the number of weeks is negative in some groups, and positive in others. We have 16 subgroups, in which the ones related to woman (female==1), have normaly negative or extremely low values of the effect, except for a certain group that has a CATE of 1.1%.

* [6.Causal Forest & Debiased Machine Learning ](https://github.com/stephyriega/ML_CI/tree/main/Causal%20Forest%20%26%20Debiased%20Machine%20Learning)

  We did the replication of Estimating Treatment Effects with Causal Forests: An Application by Athey and Wager (2018). The objetive of this paper is to evaluate the impact of a nudge-like intervention designed to instill students with a growth mindset on student achievement using simulated data from a model fit from the National Study of Learning Mindsets. This paper aims to answer three questions: Was the mindset intervention efective in improving student achievement? Was the efect of the intervention moderated by school level achievement or pre-existing mindset norms? Do other covariates moderate treatment efects?. With the tuned parameters, we estimate the ATE that is 0.248, however we need to prove whether the causal forest would succed in accurately estimating treatment heterogeneity since we don't know if it is better estimate of the real effect than the ATE. It finds that if we insists in cluster-robust inference, there's almost no treatment heterogenity present and thus that the causal forest couldn't identify subgroups with effects at stand. This results remain since they are cluster-robust and do not change if we estimated without fitting the propensity score. We also estimate Debiased Machine Learning to compare Baseline OLS, Least Squares with controls, Lasso, Post-Lasso, CV Lasso, CV Elnet, CV Ridge, Random Forest and Best model. It looks like the best method for predicting D is CV Ridge, and the best method for predicting Y is Post-Lasso because the RMSE of these models are the smallest.


## Overall, here is resume of the methods and models that were developed:


Methods available:
- Data splitting
- Partialling out
- Cross validation
- Boostraping
- Bagging

Models available:
- OLS (with RCT data)
- IRA, CRA
- Lasso
- Dobble lasso
- Tree and Random Forest
- Causal Tree & Random Forest
- Debiased Machine Learning

