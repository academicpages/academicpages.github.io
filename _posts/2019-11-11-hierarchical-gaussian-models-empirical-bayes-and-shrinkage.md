---
title: 'Bayesian [2/2] - Hierarchical Gaussian Models, Empirical Bayes and Shrinkage'
date: 2019-11-10
permalink: /posts/2019/11/empirical-bayes-and-shrinkage/
tags:
  - Bayesian
  - James Stein Estimator
  - Markov Chain Monte Carlo (MCMC)
  - Gibbs sampling
  - Metropolis-Hastings 
---

[Work In Progress]

# Quick Intro
------

This article is the second of the Bayesian series. Previous episode [here](https://vincent-maladiere.github.io/posts/2019/11/a-primer-on-bayes/). 

You probably already know the Bayes theorem or stumble upon Naive Bayes when comparing machine learning models. Maybe, like me, you feel that you barely saw the shores of the continent that is the Bayesian land and want to set foot in it.  

I wrote this article from a Stanford course with the intent for you to understand the relationships between all Bayesian concepts without having to go through an entire classroom (like I did).
As a matter of readability, I hide most of the maths in dropdowns. This way, you can follow the logic easily and come back to deep dive into formulas later.

So far we have dealt with Bayesian analysis of very simple models, mainly using conjugate priors, with few parameters to estimate. In the coin tossing example, we had just one parameter, the probability of heads. In the Gaussian model, we had two parameters, the mean $$\mu$$ and variance $$\sigma^2$$. However, in modern applications one typically must estimate many parameters, using more complicated hierarchical models.


<br>
# 2-1 Empirical Bayes
-----

## 2-1-1 Estimation of the normal mean

Suppose that we have $$N$$ observations each from independent Gaussians all with same variance $$1$$ but with *different* means 

$$y_i \;\sim^{ind}N(\mu_i,1)$$

This is a high-dimensional model: there are as many parameters as there are data. Another way to write it with $$N$$-vectors:

$$y\;\sim\;N(I\mu,I)$$

- Suppose we want to estimate the vector $$\mu$$. The natural "frequentist" thing to do is just to use the MLE, which in this case is simply

    $$\hat{\mu}=y$$

- On the other hand, if we performed a Bayesian analysis, it would be natural to choose the prior

$$\mu_i\;\sim^{iid}\;N(m,\tau^2)$$

<details>
<summary>We compute the difference of risk between the frequentist MLE and the Bayes estimator</summary>
<br>
- Frequentist

The risk of the MLE ($y_i$) is the expectation of its squared error loss

$$E[||\mu-\hat{\mu}||^2_2]=\sum^N_{i=1}E[(\mu_i-\hat{\mu}_i)^2]=\sum^N_{i=1}E[(\mu_i-y_i)^2]=N$$

since the $y_i$ are all independent normals with mean $\mu_i$ and variance $1$
 

- Bayesian

The Bayes estimator of each $\mu_i$ is

$$E[\mu_i|y,m,\tau^2]=\frac{y_i}{1+\tau^{-2}}$$

Proof in the original paper. So the posterior means shrinks the MLE. Let's compute the frequentist risk of this estimator, which is needed to computing the Bayes risk.

$$E(\frac{y_i}{1+\tau^2}-\mu_i)^2=var(\frac{y_i\tau^2}{1+\tau^2})+bias^2(\frac{y_i\tau^2}{1+\tau^2})=\frac{\tau^4}{(1+\tau^2)^2}+\frac{\mu_i^2}{(1+\tau^2)^2}$$

So the Bayes risk of this estimator is 

$$\sum_i E_{m,\tau^2}[\frac{\tau^4}{(1+\tau^2)^2}+\frac{\mu_i^2}{(1+\tau^2)^2}]=NE_{m,\tau^2}[\frac{\tau^4}{(1+\tau^2)^2}+\frac{\mu_i^2}{(1+\tau^2)^2}]=N\frac{\tau^2}{\tau^2+1}$$

So the difference between the risk of the MLE and the Bayes estimator is 

$$N-N\frac{\tau^2}{\tau^2+1}=\frac{N}{\tau^2+1}$$
________________________________________________________________________________
</details>
<br>


$$R_{frequentist}-R_{Bayesian}=\frac{N}{\tau^2+1}$$

which can be very large if $$\tau$$ is small.

## 2-1-2 Admissibility and Empirical Bayes

Obviously we want estimators that have low risk. For any loss function $$L$$ we know that:

- Frequentist deal with the fact that $$\theta$$ is unknown, the risk still depends on $$\theta$$

$$R(\theta,\delta)=\int L(\theta,\delta(y))p(y|\theta))dy$$

- Bayesians deal with this issue by integrating a second time over $$\theta$$ with respect to the prior distribution.

$$\bar{R}=\int \int L(\theta,\delta(y))p(y|\theta)p(\theta|\xi)dyd\theta=E_{\xi}[E_{\theta}[L(\theta,\delta(y))]]$$

Where $$\xi$$ are prior hyperparameters. However frequentists don't use prior, so instead we can use admissibility and minimax.

An estimator $$\delta$$ is inadmissible if there exists another estimator $$\delta$$ for which:

$$R(\theta,\delta)\leq R(\theta,\delta^*)$$

So an estimator is admissible if it is not inadmissible. $$\delta$$ dominate $$\delta$$ if $$R(\theta,\delta)≤R(\theta,\delta)$$ for every $$\theta$$.

## 2-1-3 The James-Stein estimator

If we don't know how to choose the parameter $$\tau$$ of $$\mu$$, we try to estimate $$\mu$$ using empirical Bayes via the James-Stein estimator.

$$\hat{\mu}^{(JS)}=(1-\frac{N-2}{||y||^2})\;y$$



<details>
<summary>We prove that the JS estimator has a larger risk than the Bayes estimator (indeed it must be), but it dominates the MLE everywhere if the dimension is large enough $(N≥2)$.</summary>
<br>

So we have

$$y|\mu\;\sim\;N(\mu,I),\;\mu|\tau^2\;\sim \; N(0,\tau^2I)$$

and

$$y\;\sim\;N(0,(1+\tau^2)I).$$

Thus

$$S=||y||^2 \implies S\;\sim\;N(\tau^2+1)\chi^2_N $$

where $\chi^2_N$ has N degrees of freedom and

$$E[\frac{N-2}{S}]=\frac{1}{\tau^2+1}.$$

With our JS estimator defined as

$$\hat{\mu}^{(JS)}=(1-\frac{N-2}{S})\;y$$

the integrated risk of our JS estimator is

$$R(\mu,\hat{\mu}^{(JS)})=E_{\mu}[||\mu-\hat{\mu}^{(JS)}||^2]=E_{\mu}[||\mu-y-\frac{N-2}{S}y||^2]\\=...\\=N\frac{\tau^2}{\tau^2+1}+\frac{2}{\tau^2+1}$$

See full proof [here](https://www.dpmms.cam.ac.uk/~qb204/teaching/princip_stat_17.pdf)

This is larger than the Bayesian risk, found in [1.5], and we have

$$\frac{\bar{R}^{(JS)}}{\bar{R}}=1+\frac{2}{N\tau^2}.$$

Thus JS very similar to Bayes estimator when $N$ is large.

The proof also show that

$$R(\mu,\hat{\mu}^{(JS)})=N-E_\mu[\frac{(N-2)^2}{S}]$$

So the JS estimator dominates the MLE if $N≥2$. 

________________________________________________________________________________
</details>
<br>

So why one would use the MLE is high-dimension? Because:

1. The JS estimator is biased, since the MLE is the minimum variance **unbiased** estimator (Rao-Blackwell theorem). So the JS reduces its variance but adds bias: good for point estimation but challenging for frequentist interval estimation. 
2. The MLE is admissible in 1 and 2-dimensions, but even in higher dimensions, if we focus on a single "outlier" entry, the MLE has a better MSE (see why below) 

<details>
<br>
However, high dimension, suppose we generate values from 

$$y_i\;\sim\;N(\mu_i,1)\;for\;i=1,...,11$$

We put

$$\mu_i=(5,-1,-0.75,...,0.75,1)$$

For each simulation replicate, we estimate $\mu$ by the MLE and by JS. We find

![](https://vincent-maladiere.github.io/images/bayes_loss.png)
<br>
________________________________________________________________________________
</details>
<br>


## 2-1-4 Full Bayes inference

We could conclude at this point that one should always use empirical Bayes to choose a prior. However, when it comes to estimating a parameter, the Bayesian approach is to put a prior on it.

Thus if our problem is 

$$y\;\sim\;N(\mu,I)\\\mu\;\sim\;N(0,\tau^2I)\\\tau^2\;\sim\;p(\tau^2)$$

So now our problem is to estimate $$p(\tau^2)$$. Since we want to estimate $$\tau^2$$ from our data, we have to place an objective prior on $$\tau^2$$: $p(\tau^2)=1$

<details>
<summary>So we compute the posterior of $\mu$ to find out that its posterior expectation is challenging to evaluate, although our initial model is simple.</summary>
<br>
We now have

$$y\;\sim\;N(\mu,I)\\\mu\;\sim\;N(0,\tau^2I)\\\tau^2\;\sim\;p(\tau^2)=1$$

Let's compute the posterior

$$p(\mu,\tau^2|y)\propto p(y|\mu)p(\mu|\tau^2)p(\tau^2) = (2\pi)^{-N}e^{-\frac{1}{2}(y-\mu)'I(y-\mu)}(\tau^2)^{-N/2}e^{-\frac{1}{2}\mu'(\tau^2I)^{-1}\mu}\\=(2\pi)^{-N}(\tau^2)^{-N/2}e^{-\frac{1}{2}(\mu-(1+\tau^{-2})^{-1}y)'(1+\tau^{-2})I(\mu-(1+\tau^{-2})^{-1}y)}e^{-\frac{1}{2}y'(1-(1+\tau^2)^{-1}Iy)}$$

I spare you the ugly proof of this result, which would need an article in itself.
________________________________________________________________________________
</details>
<br>

We need some alternative way to do integration that doesn't involve actually computing all of the integrals analytically.

<br>
# 2-2 Markov Chain & Monte Carlo
-----

We still have the same problem. Now we know that getting the posterior is hard if we can't find the normalising constant through some known distribution. 

Another choice is the half Cauchy prior on $$\tau$$

$$p(\tau)\propto\frac{1}{1+\tau^2}$$

We choose to have an *Inverse Gamma* prior on $$\tau^2$$ and a Normal prior on $$m$$. 

<details>
<summary>We show that computing the posterior become very ugly</summary>
<br>
The half Cauchy prior is not a conjugate prior, so now we consider

$$y\;\sim\;N(\mu,\sigma^2I)\\\mu\;\sim\;N(m,\sigma^2\tau^2I)\\p(\tau)\propto\frac{1}{1+\tau^2}$$

The posterior can be written

$$p(m,\tau^2,\sigma^2,\mu|y)\propto p(y|\mu,\sigma^2)p(\mu|\sigma^2,\tau^2,m)p(\sigma^2)p(\tau^2)p(m)$$

We try to find the normalizing constant $p(y)$:

$$\int|2\pi\sigma^2I|^{-1/2}e^{-\frac{1}{2}(y-\mu)^T(\sigma^2I)^{-1}(y-\mu)}|2\pi\sigma^2\tau^2I^{-1/2}|e^{-\frac{1}{2}(\mu-m)^T(\sigma^2\tau^2I)^{-1}(y-m)}d\mu\\=(2\pi\sigma^2)^{-N/2}(\tau^2)^{-N/2}e^{(y-m^*)(\Sigma^*)^{-1}(y-m^*)}$$

So now we have to integrate over $\sigma^2$ and then $\tau^2$, which may not even be doable at all.
________________________________________________________________________________
</details>
<br>

However, in high-dimensions we don't really care about the whole posterior, but more about some functional of it, like the **posterior expectations** of a function $$f$$:

$$\int\frac{f(\theta)p(y|\theta)p(\theta)}{p(y)}d\theta$$

It turns out this integral can be approximated using Markov chain Monte Carlo (MCMC). It consists in sampling the desired distribution by recording states from the Markov chain, which has the desired distribution as its equilibrium distribution.

<details>
<summary>Let's see the difference with ordinary Monte Carlo.</summary>
<br>
Suppose we have $Y \sim G$ and we want to compute the quantity 

$$\mathbb{E}[log(Y)]$$

One idea in to take samples from $g(\theta)$, say

$$\theta_1,..., \theta_N\;\sim^{iid}\;G$$

and then use

$$\widehat{\mathbb{E}[log\,Y]}=\frac{1}{n}\sum^{n-1}_{j=0}log(\theta_j)$$

If we could sample $Y \sim G$, it would be just ordinary Monte Carlo.

________________________________________________________________________________
</details>
<br>

A Markov chain is a sequence of random variable ignoring the whole history (independent) except for the last event:

$$p(X_N|X_0,...,X_{N-1})=p(X_N|X_{N-1})$$

We hop from one state $$n$$ to $$n+1$$ via a transition kernel $$K$$. Some $$K$$ have invariant distribution. 
<details>
<summary>Let's see how it suggests the Gibs sampling model to construct $K$.</summary>
<br>
$$X_n\in\{0,1\}\;and\;\alpha,\beta\in[0,1]\\X_n|(X_{n-1}=0)= \Bigg\{ \begin{array}{ll}0\;with\;proba\;1-\alpha \\ 1\;with\;proba\;\alpha \end{array}\\X_n|(X_{n-1}=1)= \Bigg\{ \begin{array}{ll}0\;with\;proba\;\beta \\ 1\;with\;proba\;1-\beta \end{array}$$

so our transition matrix $K$ is

$$K=\Bigg[ \begin{array}{cc}1-\alpha & \alpha\\ \beta & 1-\beta \end{array} \Bigg]$$

In high dimension, $K$ is no longer a matrix but an operator mapping function. This way, the density

$$X_1|X_0\;\sim\;P$$

can be written

$$\int p(x)k(x,y)dx=\bar{p}(y)$$

How can we use Markov Chain to compute expectations with respect to the posterior?

Some $K$ have an invariant distribution:

$\mu K=\mu$

If $\mu$ has density $p$, this means

$$\int p(x)k(x,y)dx=p(y)$$

If the invariant measure $\mu$ exists and is unique then

$$\lim_{n \rightarrow \infty}\nu K^n=\mu$$

if we start at the state $\nu$, the distribution will look more and more like the invariant distribution. 

Thus if we could make the posterior our invariant distribution, we could sample from it using Markov chains:

$$if\;X_0\;\sim\;\nu\;and\;X_n|X_{n-1}\;\sim\;K(X_{n-1},.),\;then\\\frac{1}{n}\sum^{n-1}_{k=0}\phi(X_k)\rightarrow^{n\rightarrow\infty\;i.p.}\int\phi(x)p(x)dx$$

if $K$ has invariant density $p$. That means the empirical averages converge to expected value we are looking for.
________________________________________________________________________________
</details>
<br>

## 2-2-1 Gibbs sampling

We want to construct $$K$$ for arbitrary distributions. We need to compute the posterior without knowing the normalising constant $$p(y)$$.

In Gibbs sampling the idea is to break the problem of sampling from the high-dimensional joint distribution into a series of samples from low-dimensional conditional distributions. 

<details>
<summary>We illustrate the algorithm here</summary>
<br>
The General MCMC algorithm is:


1. find a $K$ with invariant distribution $p(\theta|y)$
2. start somewhere $X_0 \sim \nu$
3. simulate forward a lot of steps
4. throw out $B$ steps (burn-in, intermediary steps, far from the convergence)
5. average the rest

Here steps 1 to 3 look like this:

$$Initialize\;\theta^{(0)}\in R^{D}\;and\;number\;of\;sample\;N\\for\;i=0\;to\;N-1\\\;\;\;\;•\;\theta^{(i+1)}_0\sim\;p(\theta_1|\theta_2^{(i)},...,\theta^{(i)}_D)\\...\\\;\;\;\;•\;\theta^{(i+1)}_j\sim\;p(\theta_j|\theta_1^{(i+1)},...,\theta^{(i+1)}_{j-1},\theta^{(i)}_{j+1},...,\theta^{(i)}_D)\\...\\\;\;\;\;•\;\theta^{(i+1)}_D\sim\;p(\theta_D|\theta_1^{(i+1)},...,\theta^{(i+1)}_{D-1})\\return \;(\{\theta^{(i)}\}^{N-1}_{i=0})$$

as this has the invariant distribution $p(\theta)$.

Here is an application of Gibbs sampling to a Probit model:

$$y_i\;\sim^{iid}\;Bern(\Phi(\theta))=Bern(p(Z\leq\theta))$$

so

$$y_i=\mathbb{I}_{[z_i>0]}\\z_i\;\sim\;N(\theta,1)$$

thus

$$z_i|y_i\;\sim\;\bigg\{\begin{array}{cc}N_{(0,\infty)}(\theta,1)\;if\;y_i=1\\N_{(-\infty,0]}(\theta,1)\;if\;y_i=0 \end{array}$$

now if $\theta\;\sim\;N(0,\tau^2)$ then $\theta|z\;\sim\;N(\frac{n\bar{z}}{\tau^{-2}+n},\frac{1}{\tau^{-2}+n})$

Thus, we can use Gibbs to do computations with this model. See [Tanner and Wong (87)](https://www.stat.cmu.edu/~brian/905-2009/all-papers/tanner-wong-1987-with-disc.pdf), or [Albert and Chib (1993) data-augmentation](http://www.stat.cmu.edu/~brian/905-2009/all-papers/albert-chib-1993.pdf) for more details.
________________________________________________________________________________
</details>
<br>

A nice implementation can be found here:

[mikhailiuk/medium](https://github.com/mikhailiuk/medium/blob/master/Gibbs-sampling.ipynb)

## 2-2-2 Metropolis-Hastings algorithm

If one of the Gibbs conditionals is not conjugate, a Metropolis-Hasting step is used in the Gibbs iteration. 

Here is an implementation: [MCMC sampling for dummies](https://twiecki.io/blog/2015/11/10/mcmc-sampling/)

This new step ensure the transition kernel is reversible, which guarantee that the Markov chain converges to the correct invariant measure.

The core idea is to compute an acceptance ratio, which is the probability to jump to the next step. 

<details>
<summary>We illustrates the algorithm here with an example and a measure of MSE to assess the quality of convergence.</summary>
<br>
Suppose we want to sample from a density $f(x, a)M(a)$, with $M(a)$ normalising constant.


1. Choose a proposal $Q(x, .)$ with density $q(x, y)$. For exemple $y \sim N(x, s)$
2. At state $n$, propose new state:

$$X_n^*\;\sim\;Q(X_{n-1},.)$$

3.    Compute the acceptance ratio:

$$\alpha(X_{n-1},X_n^*)=min\bigg(1, \frac{f(X_n^*,a)q(X^*_n|X_{n-1})}{f(X_{n-1},a)q(X_{n-1}|X_n^*)}\bigg)$$

4.    With probability $\alpha$, $X_n=X_n^*$, otherwise $X_n=X_{n-1}$ with proba $1-\alpha$

If we take the model 

$$y_i\;\sim\;N(0,\tau^2),\;p(\tau)=\frac{1}{1+\tau^2}$$

the only parameter is $\tau$, so

$$p(\tau|y)\propto p(y|\tau)p(\tau) \propto \bigg(\prod^n_{i=1}\frac{1}{\sqrt{}2\pi\sigma^2}e^{-y_i^2/2\tau^2} \bigg)\frac{1}{1+\tau^2}$$

Let's use MH. For $q(\tau, \tau*)$ take

$$\tau^*\;\sim\;LogNormal(log\;\tau,s)$$

with $s$ extra parameter to make convergence slower or faster (ideal is a ratio of 0.23). The acceptance ratio is

$$\alpha=\frac{p(\tau^*|y)q(\tau^*,\tau)}{p(\tau|y)q(\tau,\tau^*)}=\frac{\tau}{\tau^*}$$

We know that

$$\frac{1}{n}\sum^{n-1}_{j=0}\phi(X_k)\rightarrow^{n\rightarrow\infty}\int\phi(x)p_N(x)dx=\mu\phi$$

We assess the error with MSE (which is frequentist)

$$\mathbb{E}\Big[\Big(\frac{1}{n}\sum(\phi(X_k))-\mu\phi\Big)^2\Big]=\frac{1}{n}\sum^{n-1}_{j=0}\sum^{n-1}_{l=0}Cov(\phi(X_j),\phi(X_l))+\frac{1}{n^2}\sum^{n-1}_{j=0}\sum^{n-1}_{l=0}(\nu K^j-\mu)\phi(\nu K^l-\mu)\phi$$

- If we sample independently it becomes

$$\frac{1}{n^2}\sum^{n-1}_{i=0}\mathbb{V}[\phi(X_j)]=\frac{1}{n} \mathbb{V}[\phi(X)]$$

- If we start at $\nu=\mu$, then the bias would be $0$ but not the covariance

To have convergence of the MSE, we would like an exponential decay of the covariance

$$Cov(\phi(X_j),\phi(X_l))=\bar{\alpha}^{(j-l)}\;with\;\bar{\alpha}\in(0, 1)$$

________________________________________________________________________________
</details>
<br>

We can diagnosis convergence via:

- Asymptotic variance (or effective sample size)
- Trace plotting
- Comparison across multiple chains
- Coupling

### 2-2-2-a Asymptotic variance

<details>
<summary>The Effective sample size (ESS) allows us to estimate $\sigma$, thanks to the Central Limit Theorem.</summary> 
<br>
We have

$$\sqrt{n}\bigg[\frac{1}{n}\sum^{n-1}_{j=0}\phi(X_j)-\mu\phi\bigg]\Rightarrow N(0,\sigma^2)$$

where

$$\sigma^2=\mathbb{V}[X_0]\sum^{\infty}_{j=0}Corr(X_0,X_j)$$

We want to estimate $\sigma^2$. 

For batches $b_n=n^{1/3}$ there are $n-b_n$ such batches and $$\hat{\sigma^2}=\frac{(n-1)b_n}{(n-b_n)(n-b_n-1)}\sum^{n-b_n-1}_{j=0}(\bar{X}_j(b_n)-\bar{X}_n)$$

where 

$$\bar{X}_j(b_n)=\frac{1}{b_n}\sum^{b_n}_{i=1}X_{j+i}, \;\;\bar{X}_n=\sum^{n-1}_{i=1}X_i$$

So the ESS is 

$$ESS=n\frac{\bar{\mathbb{V}}[X_0]}{\hat{\sigma}^2}$$

In the special case of Monte Carlo, note $ESS = n$, but because of correlation in the Markov chain this might be much worse.

________________________________________________________________________________
</details>
<br>

### 2-2-2-b Plotting Autocorrelation

We plot the autocorrelation of the chain, ideally quickly decreasing to zero (the chain itself looks like white noise). 

<details>
<summary>Let's see how to use Gibb sampling to compute conditional mean and variance.</summary>
<br>
Suppose we are interested in sampling 

$$Y\;\sim\;N(\mu,\Sigma)$$

Let's use Gibbs, since sampling from the conditionals is straightforward:

$$\binom{y_A}{y_B}\;\sim\;N\bigg(\binom{\mu_A}{\mu_B}, \Big[\begin{array}{cc}\Sigma_{AA}&\Sigma_{AB}\\\Sigma_{BA}&\Sigma_{BB}\end{array} \Big]\bigg)$$

then the conditionals mean and variance are given by

$$\mu^*=\mu_A+\Sigma_{AB}\Sigma_{BB}^{-1}(y_B-\mu_B)\\\Sigma^*=\Sigma_{AA}-\Sigma_{AB}\Sigma_{BB}^{-1}\Sigma_{BA}$$

________________________________________________________________________________
</details>
<br>


### 2-2-2-c Comparison

<details>
<summary>We run multiple choices and compare them using the *Gelman-Rubin* diagnostic.</summary> 
<br>
The Gelman-Rubin diagnostic is 

1. run $m$ chains of length $2n$, starting over dispersed points, discard first $n$.
2. compute the between variance

$$\frac{B}{n}=\sum^m_{i=1}\frac{(\bar{x}_i-\bar{x})^2}{n-1}$$

and the within variance

$$W=\frac{1}{m}\sum_{i=1}^m \bigg(\frac{1}{n-1}\sum^n_{j=1}x_{ij}-\bar{x}_i\bigg)^2$$

and take the estimated variance to be 

$$\hat{\sigma}^2_+=\frac{n-1}{n}W+\frac{B}{n}$$
________________________________________________________________________________
</details>
<br>

However the shortcomings of this idea is to only consider the effect of auto-correlations for the identity function. 

We need to bound autocorrelations for a huge class of functions if we want to converge in total variation


### 2-2-2-d Coupling

<details>
<summary>We run $m$ pairs of chains to simulate two dependent Markov chains, and run the chains until they meet</summary>
<br>
We have $(X,Y)\sim\Gamma(\nu_0,\nu_1)$

so that marginall

$$X\sim\nu_0\;and\;Y\sim\nu_1 $$

We define the total variation metric between distributions:

$$||\nu_0-\nu_1||_{TV}=sup_A|\nu_0(A)-\nu_1(A)|$$

The coupling inequality states that

$$P[X \neq Y]\geq||\nu_0-\nu_1||_{TV}$$

Thus the idea is to simulate from two dependent Markov chains at different points 

$$X_n\sim\nu_0K^n\;and\;Y\sim\nu_1K^n$$

and run the chain until they meet

For exemple take

$$X\sim f \\W|X\sim U(0,f(X))$$

- If $W < g(X)$ output $(X, X)$
- else sample $Y \sim g$ and take $W|Y \sim U(0, g(Y))$ until $W > f(Y)$ and output $(X, Y)$

________________________________________________________________________________
</details>
<br>
<br>

# 2-3 Nontrivial models
-----

## 2-3-1 Linear regression

<details>
<summary>We see in how Bayesian linear regression</summary>
<br>
The usual least square estimate is 

$$\hat{\beta}_{OLS}=(W^TW)^{-1}W^Tz$$

which is also the MLE for $\beta$. The MLE for $\sigma^2$ is given by

$$\hat{\sigma}^2=\frac{1}{N}(Z-W\hat{\beta})^T(Z-W\hat{\beta})=||z^T(I_d-W(W^TW)^{-1}W^T)z||^2$$

These work fine when $N >> d$, but if $d$ is big, using shrinkage make sens. So we consider the Bayesian hierarchical model

$$z\sim N(W\beta,\sigma^2)\\\beta\sim N(0,\tau^2\sigma^2I)$$

Thus, we have

$$-2log(L(z|\beta,w,\sigma^2)p(\beta))\propto \frac{1}{\sigma^2}(z-W\beta^T)(z-W\beta)+\frac{1}{\sigma^2\tau^2}\beta^T\beta\\\propto\beta^T\Big[\frac{1}{\sigma^2}W^TW+\frac{1}{\sigma^2\tau^2}I\Big]-2\beta^T\Big(\frac{W^Tz}{\sigma^2}\Big)$$

so

$$\beta|W,\sigma^2,\tau^2\sim N(V\mu^*,V)$$

with

$$V = \Big(\frac{1}{\sigma^2}W^TW+\frac{1}{\sigma^2\tau^2I}\Big)^{-1} \\ \mu^*=\frac{1}{\sigma^2}W^Tz$$

Thus the posterior mean is 

$$\hat{\beta}_{ridge}=\mathbb{E}[\beta|W,\sigma^2,z,\tau^2]=V\mu^*=\Big(W^TW+\frac{1}{\tau^2}I\Big)^{-1}W^Tz$$

This is the usual ridge regression estimate, which solves

$$\hat{\beta}_{ridge}=max_{\beta}-||W\beta-z||^2-\tau^{-2}||\beta||^2$$

See original paper for computation optimisation using diagonalisation and Woodbury identity.
</details>

$$z_{N×1}=W_{N×d}\beta_{d×1}+\epsilon_{N×1}\\with\;\epsilon\sim N(0,\sigma^2I)$$

easily leads to ridge estimate

$$\hat{\beta}_{ridge}=\mathbb{E}[\beta|W,\sigma^2,z,\tau^2]=\Big(W^TW+\frac{1}{\tau^2}I\Big)^{-1}W^Tz$$

where $z$ is the response, $W$ is the matrix, $\beta$ is the vector of regression coefficients, and $\epsilon$ is the vector of random error.

## 2-3-2 Tikhonov regularisation

More generally we have *Tikhonov regularization*

$$\hat{\beta}_{ridge}=(W^TW+A^{-1})^{-1}W^Tz$$

where $A$ symmetric, positive definite.

We regularise because:

- Adding a bias may improve our estimation of a vector with more than 2 dimensions (see JS estimator)
- When $$p > N$$, least square can't be done, but regularised solution can

<details>
<summary>We see in that its much harder to get $$A$$ with Empirical Bayes than Full Bayes (in particular when $$\beta$$ doesn't follow a Normal distribution).</summary>
<br>
- Empirical Bayes

    We maximise the marginal likelihood (in term of $\tau^2$)

    $$p(z|W,\tau^2)$$

    Pick a prior structure

    $$\beta|\sigma^2,\tau^2\sim N(0,\sigma^2\tau^2I)\\\sigma^2\sim InvGamma(a,b)$$

    which can be reframed

    $$\beta\sim N(0,\sigma^2\tau^2I)\\Z\sim N(W\beta,\sigma^2I)$$

    so

    $$Z\sim N(0,\sigma^2(\tau^{-2}WW^T+I))$$

    We compute easily the likelihood

    $$p(z|\sigma^2\tau^2,W)$$

    Now we just need to multiply by the prior density for $\sigma^2$ and integrate over $\sigma^2$. This is easy since the function is the kernel of an inverse-gamma distribution. 

    Then we pick $\tau$ according to

    $$max_{\tau^2}\int p(z|W,\sigma^2,\beta,\tau^2)p(\beta,\sigma^2)d\beta d\sigma^2$$

    If $\beta$ were not coming from a Normal distribution, this problem could quickly become intractable (above all because $\beta$ is high-dimensional).

- Full Bayes

    To estimate $A$, we put a prior on $\tau$ . What kind?

    1. Discrete Uniform on a set of grid points
    2. Uniform on an interval
    3. Half-Cauchy
    4. Inverse Gamma

    We use Half-Cauchy: it requires no hyperparameters and it is reasonably uninformative (it let the data speak for itself). The full model is:

    $$\beta|\sigma^2,\tau^2\sim N(0, \sigma^2\tau^2I)\\\sigma^2\sim InvGamma(a,b)\\p(\tau)\sim \frac{1}{2\pi}\frac{1}{1+\tau^2}$$

This can be done using Gibbs sampling

$$\beta|\tau^2,\sigma^2,W,z\\\sigma^2|\tau^2,\beta,W,z\\\tau^2|\sigma^2,\beta^2$$

The first two distribution are easy to sample from. The third distribution is well known and we can directly sample it with Metropolis-Hastings.
</details>

## 2-3-3 Conjugate prior

Another option to solve Bayesian linear regression is using a conjugate prior. 
<details>
<summary>We see how Zellner's $g$ prior gives us a posterior with a mean that is a shrunken factor of the MLE.</summary>
<br>
We have 

$$\beta,\sigma^2\sim N\Gamma^{-1}(\mu,V,a,b)$$

which is equivalent to

$$\sigma^2\sim InvGamma(a,b)\\\beta|\sigma^2\sim N(\mu,\sigma^2 V)$$

so

$$p(\beta,\sigma^2)\propto (\sigma^2)^{-p/2}(\sigma^2)^{-a-1}e^{-\frac{1}{\sigma^2}(b+(\beta-\mu)^TV^{-1}(\beta-\mu))}$$

And if

$$Z\sim N(W\beta,\sigma^2I)$$

then the posterior is

$$\beta,\sigma^2|z, W\sim N\Gamma^{-1}(\mu^*,V^*,a^*,b^*)$$

where

$$\mu^*=(V^{-1}+W^TW)^{-1}(V^{-1}\mu+W^Tz)\\V^*=(V^{-1}+W^TW)^{-1}\\a^*=a+N/2\\b^*=b+1/2\Big[\mu^TV^{-1}\mu+z^Tz-(\mu^*)^T(V^*)^{-1}\mu^*\Big]$$

If we use the Zellner's $g$ prior:

$$p(\beta|\sigma^2,g)\sim N(0,\sigma^2g(W^TW)^{-1})\\p(\sigma^2)\sim \frac{1}{\sigma^2}$$

and we find that the posterior is still Normal InvGamma, but his mean has become

$$\mu^*=\frac{g}{g+1}(W^TW)^{-1}W^Tz=\frac{g}{g+1}\hat{\beta}$$

hence the shrinkage.
</details>

## 2-3-4 Bayesian variable selection

We saw that for *Ridge* or *l1 penalisation* the problem was

$$max_{\beta}||W\beta-z||^2+\lambda||\beta||_1$$

In high-dimension, *Lasso* or *l0 penalisation* allows us to select features automatically. The ideal problem in this case is:

$$max_{\beta}||W\beta-z||^2-\lambda||\beta||_0$$

We still need to select $$\lambda$$ with AIC ($$\lambda = 1$$) or BIC ($$\lambda = 2 log(n)$$). 

<details>
<summary>If we think of variable selection as hypothesis testing, we can compute the Bayes factor for each variable.</summary>
<br>
We can think of variable selection as

$$\gamma_j=\bigg\{\begin{array}{cc} 1\;if\;\beta_j=\not0:H_{1j}\\0\;if\;\beta_j=0:H_{0j}\end{array}$$

Bayesian testing in case of one hypothesis is

$$p[H_0|z]=\frac{1}{1+\frac{1-q}{q}\frac{p(z|H_1)}{p(z|H_0)}}$$

We compute $p(z|H1)$ and $p(z|H0)$ to find the Bayes factor (see original paper)

$$BF_{1:0}=\frac{p(z|H_1)}{p(z|H0)}=\frac{1}{\sqrt{\tau^2+1}}e^{\frac{1}{2}z^2_j(\frac{\tau^2}{\tau^2+1})}$$
</details>


<br>

# The end
------

Thank you for reading, it has been quite a journey and I hope that I successfully put those complex concepts in a short and easy form.
There are some nice state of the art [here]() and [here]() that I leave you to exploring. See you on a next post!

