---
title: 'Bayesian [1/2] - A primer on Bayes'
date: 2019-11-01
permalink: /posts/2019/11/a-primer-on-bayes/
tags:
  - Bayesian
  - Inference
  - Hypothesis testing 
---

# A Quick Intro 
-------

This article is the first of the Bayesian series. Next episode [here](https://vincent-maladiere.github.io/posts/2019/11/empirical-bayes-and-shrinkage/). 

You probably already know the Bayes theorem or stumble upon Naive Bayes when comparing machine learning models. Maybe, like me, you feel that you barely saw the shores of the continent that is the Bayesian land and want to set foot in it.  

I wrote this article from a Stanford course with the intent for you to understand the relationships between all Bayesian concepts without having to go through an entire classroom (like I did).
As a matter of readability, most of the maths are hidden in dropdowns. This way, you can follow the logic easily and come back to deep dive into formulas later.

We start with comparing frequentist and bayesian methods, before focusing on different distributions and conjugate families.

<br>

# 1-1 Frequentist analysis
------

Suppose we want to estimate the probability of head of a (possibly biased) given coin. We flip the coin $$N$$ times, generating a sequence of observations $$(x_1, ..., x_N)$$ of an iid random variable $$(X_1, ..., X_N)$$, each of which has the Bernoulli distribution with unknown head probability $$\theta$$.
<details>
<summary> We compute the likelihood and pmf here </summary>
<br>
X has the probability mass function (pmf):

$$f_{\theta}(x)=\theta^x(1-\theta)^{1-x}1\{x\in\{0, 1\}\}$$

so by independence, the likelihood can be written as:

$$\prod_{i=1}^{N}f_{\theta}(x_i)=\theta^{S_N}(1-\theta)^{N-S_N}$$

where 

$$S_N=\sum^N_{i=1}x_i$$
__________________________________________________________________________________
</details>
<br>

The fundamental notion here is that randomness comes from sampling/replicates of the experiment, and all probability statements made in frequentist inference are statements with respect to the probability distribution induced by hypothetical repetitions of the experiment.

This leads us to the basic program of frequentist inference: point estimation, interval estimation, and testing.

## 1-1-1 Point estimation

The ***laws of large numbers*** imply that the sample mean is in some sense a “good” frequentist estimator for the expectation of a random variable.

We toss a coin $$N$$ times and use the sample mean of the random variable $$X = 𝟙_{heads}$$ as an estimator of the probability of heads $$\theta$$. Is it a good estimator? 
<details>
<summary>As a frequentist, we might answer that question by computing its mean squared error (MSE)</summary>
<br>
See a future article for the theorem of large numbers, convergence in probability (i.p.) and almost sure convergence (a. s.).

Mean Square Error (MSE) is var + bias:

$$\mathbb{E}[(\bar{X}_N-\theta)^2]=\mathbb{E}[(\bar{X}_N-\mathbb{E}\bar{X}_N)^2]+(\mathbb{E}X_N-\theta)^2\\=var(\bar{X}_N)+bias^2({\bar{X}_N})$$

Always keep in mind that for frequentists, it is the statistic or estimator – in this case, $$X_N$$ – that is random, and the parameter $$\theta$$ is some fixed, unknown number.

$$if\;\bar{X}_N=\frac{1}{N}S_N=\frac{1}{N}\sum_{i=1}^N{x_i},\;then\\var(S_N)=N\theta(1-\theta),\;\mathbb{E}(S_N)=N\theta,\;so\\var(\bar{X}_N)=N^{-1}\theta(1-\theta),\;\mathbb{E}(\bar{X}_N)=\theta \;$$

Thus, $$X_N$$ is unbiased.
__________________________________________________________________________________
</details>
<br>

The sample mean is the optimal *unbiased* estimator in the sense that among all unbiased estimators, it has minimum variance —thus minimum MSE, see Rao-Blackwell theorem. The point is that the sample mean is a “good” estimator of $$\theta$$ because in a hypothetical infinite sequence of experiments just like the one we performed, it will typically give us a number that is close to $$\theta$$.

## 1-1-2 Interval estimation

Point estimation is an exercise in producing a single number that is in some sense a “best guess” at the value of a parameter $$\theta$$. Interval estimation aims to produce a range of values that are “plausible”.

What would an exact $$1 - 𝛼$$ confidence interval look like for $$\theta$$ for $$N$$ coin tosses? 
<details>
<summary>We use the CDF of the binomial distribution to build a *Clopper-Pearson* interval</summary>. 
See a future article for the central limit theorem and weak convergence.

Well, we know that $$S_N$$ has the binomial distribution with parameters $$N$$, $$\theta$$. Its CDF can be expressed as:

$$F_{\theta}(k)=P(S\leq k)=\sum_{j=1}^k\binom{N}{j}\theta^j(1-\theta)^{N-j}$$

We construct a *Clopper-Pearson* interval $$[a(S), b(S)]$$ with at least $$(1 - \alpha)$$ coverage by solving:

$$\sum_{j=S}^N\binom{N}{j}a^j(1-a)^{N-j}=\alpha/2\\\sum_{j=0}^S\binom{N}{j}b^j(1-b)^{N-j}=\alpha/2$$

It leads to heavy computations. Instead, we prefer an asymptotical approach using the *central limit theorem*. The interval takes the general form:

$$\hat{\theta} \pm \Phi^{-1}(1-\alpha/2)\hat{SE}(\hat{\theta})$$

with (for the coin flipping example):

$$var(\hat{\theta})=N^{-2}var(S_N)=N^{-1}\theta(1-\theta)=\hat{SE(\hat{\theta})}^2$$

therefore

$$a=\bar{X}_N-\Phi^{-1}(\alpha/2)N^{-1/2}\sqrt{\bar{X}_N(1-\bar{X}_N)}\\b=\bar{X}_N+\Phi^{-1}(\alpha/2)N^{-1/2}\sqrt{\bar{X}_N(1-\bar{X}_N)}$$

so that

$$p(\hat{\theta}\in[a, b])=1-\alpha$$
__________________________________________________________________________________
</details>
<br>

However this approach is too heavy in computation.
Instead, we consider intervals that have *asymptotic* $$1 - \alpha$$ coverage, using the ***central limit theorem*** of the general form:

$$\hat{\theta} \pm \Phi^{-1}(1-\alpha/2)\hat{SE}(\hat{\theta})$$

Where $$\Phi$$ is the standard Gaussian CDF and $$\hat{SE}$$ the standard error of $$\hat{\theta}$$.

## 1-1-3 Testing

We want to test whether the coin is fair through hypothesis $$H_0 : \theta = 1/2$$ and $$H_1 : \theta ≠ 1/2$$. The classical way is to use ***Neyman's fixed type I error rate testing***. We reject $$H_0$$ when our estimate $$\hat{\theta}$$ is far from $$1/2$$. We use the Binomial distribution of $$\hat{\theta}$$ to find $$c$$ (according to our chosen type I error rate) such as:

$$|\hat{\theta}-1/2|>c$$

<details>
<br>
Our test is 

$$|\hat{\theta}-1/2|>c$$

Under the null, the sampling distribution of $$\theta_{hat}$$ is given by

$$N\hat{\theta}\; \sim\;Binomial(N, 1/2)$$

So to figure out $$c$$ we compute the probability of rejection (which is no bigger than $$\alpha$$)

$$\sum_{j=0}^{N(1/2-c)}\binom{N}{j}2^{-N}+\sum^{N}_{j=N(1/2+c)}\binom{N}{j}2^{-N}$$

solving for $$c < 1/2$$ to make the quantity as large as possible while still being less than $$\alpha$$ will give a test with at most $$\alpha$$ type I error rate.
__________________________________________________________________________________
</details>
<br>

# 1-2 Bayesian analysis of coin tossing
------

There are two components here. 

- Likelihood (also appearing in frequentist inference). It suggests that we are going to consider the success probability $$\theta$$ itself to be a random variable.

$$p(x_1,..., x_N|\theta)=\prod^N_{i=1}f_{\theta}(x_i)=\theta^{S_N}(1-\theta)^{N-S_N}$$

- Prior distribution. It encapsulates our prior beliefs about $$\theta$$ before observing data $$(x_1, ..., x_N)$$. There are a number of possibilities of how we can proceed.

*i) Informative* prior choice.  
An informative prior choice would likely put a lot of prior mass near $$1/2$$. However, exactly how much mass to place is tricky. We could try to elicit a prior from “experts” (I guess gamblers?).

*ii) Objective* prior choice.
Prior that will have the smallest possible impact on the outcome of our analysis. Properties close to frequentist, but a poor choice in high-dimensional and non-parametric models.

*iii) Empirical* prior choice.
Estimate the prior from the data, then plug the prior and perform a Bayesian Analysis. Advantage: No somewhat arbitrary prior choice. Shortcoming: Lies in the grey area between the "safety" of frequentist guarantees and that of Bayesian analysis using informative priors based on real prior info. 
Nice use-case:

[http://varianceexplained.org/r/empirical_bayes_baseball/](http://varianceexplained.org/r/empirical_bayes_baseball/)

These two components allow us to define the posterior:

$$p(\theta|{x})=\frac{p({x}|\theta)p(\theta)}{\int p({x}|\theta)p(\theta)d\theta}=\frac{p({x}|\theta)p(\theta)}{p({x})}$$

Bayes’ theorem tells us how we should update our prior beliefs about parameters after observing data distributed according to the likelihood.

## 1-2-1 Prior choice

A very common choice is to pick a ***conjugate prior***: posterior and prior belong to the same family of probability distributions, so that the marginal likelihood $$p(x)$$ is often available analytically. 
For our coin-tossing example, with the $$N$$ Bernoulli likelihood, our prior is in the Beta family.

<details>
<br>

We have: 

$$p({x}|\theta)=\theta^{S_N}(1-\theta)^{N-S_N}$$

so the posterior can be expressed as:

$$p(\theta|{x})=C({x})p({x}|\theta)p(\theta)$$

We suppose our prior has the same form that our likelihood, with parameters a and b. The posterior becomes:

$$p(\theta|{x})=C({x})\theta^{S_N+a}(1-\theta)^{N-S_N+b}$$

for $$a > -1, b > -1$$ this function is integrable on the unit interval, and the result is the beta function:

$$C({x})\int^1_0\theta^{S_N+a}(1-\theta)^{N-S_N+b}d\theta=C({x})B(S_N+a+1,N-S_N+b+1)=1$$

so 

$$C({x})=B(S_N+a,N-S_N+b)^{-1}$$

and then

$$p(\theta|{x})=\frac{\theta^{S_N+a}(1-\theta)^{N-S_N+b}}{B(S_N+a+1,N-S_N+b+1)}$$

__________________________________________________________________________________
</details>
<br>

## 1-2-2 Point estimation

If the posterior contains everything we want to know about parameters, then we must be able to use it to construct point estimates of the parameters. The posterior is a distribution, and parameters are numbers, so point estimates must be maps from the space of distributions to real numbers (=expectations).

We find the minimum of the *integrated mean squared error (IMSE)* and even MSE by using the posterior expectation (called the Bayes estimator) as our point estimate. 

$$\hat{\theta}_B=\mathbb{E}[p(\theta|{x})]=\int\theta p(\theta|{x})d\theta$$

## 1-2-3 Interval estimation

One obvious way to construct an interval is to use **quantiles of the posterior**. An equal tailed interval leaves equal posterior probability to the left and to the right of the endpoints of the interval.

Our interval satisfies 

$${P}[\theta\in[a,b]]=1-\alpha$$

where the probability here is the *posterior probability* not the *probability with respect to hypothetical repeated sampling*.

<details>
<summary>For our example, we use the CDF of the Beta distribution to compute the equal-tailed interval</summary>
<br>
If we want a $$(1 - \alpha)$$ equal tailed interval, it would be the interval $$[a, b]$$:

$$a=sup_{a'}\{a':\int^{a'}_{-\inf}p(\theta|{x})d\theta<\ \alpha/2 \}\\b=inf_{b'}\{b':\int^{\inf}_{b'}p(\theta|{x})d\theta<\ \alpha/2 \}$$

The posterior is 

$$Beta(S_N+a,N-S_N+b)$$

so an equal tailed credible interval can be computed from the quantiles of the Beta distribution. If $$I(x; a, b)$$ is the CDF of the Beta distribution, then we have:

$$[I^{-1}(\alpha/2;S_N+a,N-S_N+b),I^{-1}(1-\alpha/2;S_N+a,N-S_N+b)]$$
__________________________________________________________________________________
</details>
<br>

## 1-2-4 Hypothesis testing

We again need to be able to compute everything using $$p(\theta\|{x})$$. Hypotheses are subsets of the parameter space – in this case, the subset is just $$\{\theta = 1/2\}$$. 

If the posterior distribution is continuous, then the posterior probability of the null hypothesis is

$${P}[\theta=1/2]=0$$

So we need to give nonzero positive probability to the null hypothesis by choosing a mixture prior.

$$p(\theta)=q\delta(\theta-1/2)+(1-q)f(\theta)$$

where $$f(\theta)$$ is the density of a $$Beta(a, b)$$ distribution and $$q$$ is in $$[0, 1]$$. The left part is associated with $$H_0$$ and the right with $$H_1$$. 

This is the first thing that might seem odd: in order to carry out the standard Bayes hypothesis test, I have to change my prior.

<details>
<summary>We compute our new posterior, and we compare it with frequentist p-values in the figure below.</summary>
<br>
Our prior is

$$p(\theta)=q\delta(\theta-1/2)+(1-q)f(\theta)$$

The posterior is now

$$p(\theta|{x})=C({x})\binom{N}{S_N}\theta^{S_N}(1-\theta)^{N-S_N}\{q\delta(\theta-1/2)+(1-q)f(\theta)\}$$

with 

$$f(\theta)=\frac{1}{B(a,b)}\theta^{a-1}(1-\theta)^{b-1}$$

Integrating only the part involving $$\theta$$ we find $$C(x)$$ and thus the posterior. See original paper for details.

So we can compute the posterior probability of the null hypothesis

$${P}[\theta=1/2]=\int_{1/2}^{1/2}p(\theta|{x})d\theta=\frac{1}{1+\frac{1-q}{q}\frac{B(a+S_N, N-S_N+b)}{B(a,b)}2^N}$$

**More generally**, if our null hypothesis is $$H_0 : \theta = c$$, our prior become

$$p(\theta)=q\delta(\theta-c)+(1-q)f(\theta)$$

so our posterior density is

$$p(\theta|{x})=C({x})p({x}|\theta)\{q\delta(\theta-c)+(1-q)f(\theta)\}$$

integrating the part involving $$\theta$$ we find $$C(x)$$

$$C({x})^{-1}=qp({x}|\theta=c)+(1-q)\int p({x}|\theta)f(\theta)d\theta=qp({x}|\gamma=0)+(1-q)p({x}|\gamma=1)$$

$$p(x\|\gamma=0)$$ and $$p(x\|\gamma=1)$$ are called *marginal likelihoods*, because they are obtained by integrating the likelihood function over the components of the prior associated with *H0* and *H1.*

So

$${P}[\theta=c]=\int ^c_cp(\theta|{x})d\theta=\int^c_c\frac{p({x}|\theta)\{q\delta(\theta-c)+(1-q)f(\theta)\}}{qp({x}|\gamma=0)+(1-q)p({x}|\gamma=1)}=\frac{qp({x}|\gamma=0)}{qp({x}|\gamma=0)+(1-q)p({x}|\gamma=1)}=\frac{1}{1+\frac{1-q}{q}\frac{p({x}|\gamma=1)}{p({x}|\gamma=0)}}$$

The Bayes Factor is

$$BF(x)=\frac{p({x}|\gamma=1)}{p({x}|\gamma=0)}$$
__________________________________________________________________________________
</details>
<br>

![frequentist vs bayesian](https://vincent-maladiere.github.io/images/freq_vs_bayes.png)

Thus, unlike point estimation, where Bayesians and frequentists mostly agree, and interval estimation, where typically the Bayesian credible intervals are fairly similar to frequentist confidence intervals unless a strong prior is chosen, Bayesian hypothesis tests can reach very different conclusions from frequentist ones. In this case, the Bayesian finds less evidence against the null than the frequentist does.

## 1-2-5 Objective priors

One of the most commonly used in applications is ***Jeffreys prior***. It is defined as 

$$p(\theta) \propto |I(\theta)|^{-1/2}$$

where $$I(\theta)$$ is the Fisher information matrix. 
We show that this prior is actually the $$Beta(1/2, 1/2)$$ prior.

<details>
<br>
Fisher information is defined as

$$I(\theta)=E[(\frac{\partial}{\partial\theta}logf({x};\theta))^2|\theta]$$

so for Bernoulli sampling, we have

$$-\frac{\partial^2}{\partial\theta}\{x\,log(\theta)+(1-x)log(1-\theta)\}=\frac{x}{\theta^2}+\frac{1-x}{(1-\theta)^2}$$

and so 

$$I(\theta)={E}_{x|\theta}[\frac{x}{\theta^2}+\frac{1-x}{(1-\theta)^2}]= \frac{1}{\theta}+\frac{1}{1-\theta}=\frac{1}{\theta(1-\theta)}$$

So Jeffrey prior is 

$$p(\theta)\propto\theta^{-1/2}(1-\theta)^{-1/2}=Beta(1/2, 1/2)$$

and with a transformation

$$\mu=g(\theta)$$

we will have

$$I(\theta)=J'I(\mu)J$$

where J is the Jacobian. Therefore

$$|I(\theta)|^{1/2}=|J||I(\mu)|^{1/2}$$

So this prior is invariant under one-to-one reparametrizations.
</details>

Jeffrey prior is invariant under *one-to-one reparametrizations* which means that is we choose to parametrize the model in terms of 

$$\mu=g(\theta)$$

then the prior will still take the form

$$|I(\mu)|^{1/2}$$
__________________________________________________________________________________
</details>
<br>

# 1-3 Conjugate families
-------

## 1-3-1 The Poisson likelihood

Suppose we observe $$N$$ iid data points $$x_1, ..., x_N$$ from a $$Poisson(\theta)$$ distribution. It has the form of a Gamma distribution, so we choose a prior with the same distribution family.

<details>
<summary>We show that the posterior has also the Gamma form.</summary>
<br>
We have

$$p({x}|\theta)=\prod^N_{i=1}e^{-\theta}\frac{\theta^{x_i}}{x_i!}=e^{-N\theta}\frac{\theta^{S_N}}{\prod_ix_i!}$$

This has the form of the kernel of a *Gamma distribution*

$$\theta^ae^{-b\theta }$$

So we choose our prior as a Gamma distribution

$$p(\theta)=\frac{b^a}{\Gamma(a)}\theta^{a-1}e^{-b\theta}$$

Thus

$$p(\theta|{x})=C({x})e^{-(N+b)\theta}\theta^{S_N+a-1}$$

so the posterior is

$$Gamma(S_N+a,N+b)$$

The Bayes Estimator is therefore

$${E}_{\theta|{x}}[\theta]=\frac{S_N+a}{N+b}$$
__________________________________________________________________________________
</details>
<br>

Which is:

$$Gamma(a,b)=\frac{b^a}{\Gamma(a)}\theta^{a-1}e^{-b\theta}$$

## 1-3-2 The Normal Distribution

The likelihood of the normal distribution looks like the kernel of a Gamma distribution, so we define the prior this way. It is, in fact, the *normal-inverse gamma* distribution. 
<details>
<summary>We claim this is conjugate, and we find the parameters of the posterior.</summary>
<br>
The Likelihood is 

$$p({x}|\mu,\sigma^2)=(2\pi\sigma^2)^{-N/2}exp(-\frac{1}{2}\frac{\sum^N_{i=1}(x_i-\mu)^2}{2\sigma^2})$$

if $$\mu$$ is fixed, it has the form of a Gamma distribution for the parameter $$\sigma^{-2}$$

So the prior on $$\sigma^{-2}$$ is an *inverse Gamma distribution*

$$p(\sigma^2)\propto(\sigma^2)^{-a-1}e^{-\frac{b}{\sigma^2}}$$

Also, if $$\sigma^{-2}$$ was a constant, this would look like the kernel of a normal random variable with variance $$\sigma^{-2}$$. The conjugate prior is:

$$p(\mu,\sigma^2)=p(\mu|\sigma^2).p(\sigma^2)\\=\frac{1}{\sqrt{2\pi\sigma^2\tau^2}}exp(-\frac{(\mu-m)^2}{2\sigma^2\tau^2}).\frac{b^a}{\Gamma(a)}(\sigma^2)^{-a-1}exp(-\frac{b}{\sigma^2})\\\propto(\sigma^2)^{-a-1-1/2}exp(-\frac{1}{\sigma^2}(b+\frac{1}{2}\tau^{-2}(\mu-m)^2))\\\propto N\Gamma^{-1}(m, \tau^2, a,b)$$

This is the *normal-inverse gamma distribution.* Finally, our posterior is

$$p(\mu,\sigma^2|{x})=p({x}|\mu,\sigma^2)p(\mu, \sigma^2)\\\;\propto(\sigma^2)^{-N/2-a-1-1/2}exp(-\frac{1}{\sigma^2}(b+\frac{1}{2}\tau^{-2}(\mu-m)^2+\frac{1}{2}\sum^N_{i=1}(x_i-\mu)^2))$$

Which is also a *normal-inverse gamma distribution*. After a few computations on parameters, we find:

$$p(\mu,\sigma^2|{x})\propto N\Gamma^{-1}(\frac{\tau^{-2}m+N\bar{x}}{N+\tau^{-2}},(N+\tau^{-2})^{-1},a+\frac{N}{2},b+\frac{1}{2}SSE({x})+\frac{1}{2}\frac{N\tau^{-2}}{N+\tau^{-2}}(\bar{x}-m)^2)$$

For any $$N\Gamma$$ distribution, 

$$\mu|\sigma^2,{x} \;\sim\; N(m,\tau^2 \sigma^2)\;\sim\;N(\frac{\tau^{-2}m+N\bar{x}}{N+\tau^{-2}},\sigma^2(N+\tau^{-2})^{-1})$$

So the Bayesian posterior and the frequentist sampling distribution approach one another as the sample size grows.
__________________________________________________________________________________
</details>
<br>

## 1-3-3 Multinomial Distribution

The conjugate prior of the multinomial likelihood is a multivariate of the Beta distribution and is called *Dirichlet* distribution. 

<details>
<br>
**The multinomial likelihood** for a $$d$$ category is given by

$$p(x_1,...,x_d|\theta_1,...,\theta_d)=\binom{N}{x_1!...x_d!}\prod^d_{j=1}\theta^{x_j}_j$$

The conjugate prior should be a distribution on d-1 dimensional simplex that takes the form

$$p({\theta})\propto\prod^d_{j=1}\theta^{a_j-1}_j$$

The resulting probability distribution is called the *Dirichlet* distribution and has pdf

$$p(\theta_1,...,\theta_d|x_1,...,x_d)=\frac{1}{B({a})}\prod^d_{j=1}\theta_j^{a_j-1}{1}\{a\in \mathbb{S}^{d-1}\}$$

where $$S^{d-1}$$ is the $$(d-1)$$-dimensional simplex
__________________________________________________________________________________
</details>
<br>


# Next
-----

Thank you for reading, I hope this guide has been helpful for you so far. Now that you took a bit of crunchy Bayesians, we will spice things up in the [next article](https://vincent-maladiere.github.io/posts/2019/11/empirical-bayes-and-shrinkage/) with high-dimension. 
