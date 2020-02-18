
#### Summary: I show how to calculate a multivariate effective sample size after [Vats et al. (2019)](https://academic.oup.com/biomet/article/106/2/321/5426969)

In applied statistics, Markov chain Monte Carlo (MCMC) is now widely used to fit statistical models. Suppose we have a statistical model $p_\theta$ of some dataset $\mathcal{D}$ which has a parameter $\theta$. The basic idea behind MCMC is to estimate $\theta$ by generating $N$ random variates $\theta_i,\theta_2,...$ from the posterior distribution $p(\theta\vert\mathcal{D}$ which are (hopefully) distributed around $\theta$ in a predictable way. The Bayesian central limit theorem states that under the right conditions, $\theta_i$ is normally distributed about the true parameter value $\theta$ with some sample variance $\sigma^2$. We might then want to use the mean of these samples $\hat{\theta}=\sum_i^N \theta_i$ as an estimator of $\theta$ since this *posterior mean* is an optimal estimator in the context of Bayes risk and mean square loss. 

This task has a few challenges lurking within. The accuracy of our estimate of $\theta$ is going to be low when we have only a few samples, i.e. $N$ is quite small. We can increase our accuracy by taking more samples. Ideally, our samples $\theta_i$ are all going to be *independent* so that we can make use of the theory of Monte Carlo estimators to assert that the error in our estimation of $\theta$ decreases at a rate of $1/N$. Thus, to get more accuracy, we draw more samples! 


## Autocorrelated MCMC draws

Unfortunately, MCMC won't provide uncorrelated values of $\theta_i$ because of its inherently sequential nature. These samples are going to have some autocorrelation $\rho$ and it's helpful to think of this autocorrelation as reduced the number of samples from a nominal $N$ to an effective number $N$. Here's a helpful analogy - suppose that you want to determine the average income within a city. You could pursue two sampling strategies; the first leads you to travel to 10 spots randomly selected on the map and then query a single person. The second approach is that you travel to two neighborhoods and query five people each. The latter method has the downside that you may get grossly misrepresentative numbers if you happen to land in a neighborhood where everyone has similar incomes which are not close to the city-wide average. This is an example of *spatial* autocorrelation leading to poor estimation. The same underlying mechanism is at play with our MCMC estimator having reduced precision.

The literature on sequential data makes frequent use to autocorrelations $\rho_p$ of lag $p$ meant to capture associations between data points with varying amounts of time or distance between them. We can provide a formula for the effective sample size in terms of these autocorrelations [(see here for more)](https://mc-stan.org/docs/2_22/reference-manual/effective-sample-size-section.html) via the following formula:
$$N_{eff} = \frac{N}{\sum_{t=-\infty}^{\infty}\rho_t}$$

We truncate the sum in practice since the autocorrelations typically vanish after a large number of lags. Interestingly, the effective sample size also has another form which also implicitly involves autocorrelations. Suppose that we have a chain of samples $\theta_1,...,\theta_N$ and partition this chain into two *batches* comprising the samples from $1 to N/2$ and from $N/2$ to $N$. If the samples are close to independent, then the per-batch means $T_{(k)}$ should be relatively close to each other. If they aren't, then the batches contain distinct subpopulations of samples. The key insight here is that if the subpopulations are distinct, then they exhibit high within-batch autocorrelation. Thus, we can attempt to back out the autocorrelations by looking at the differences between batch means! For $a$ batch means, each of size $N/a$, this produces the following quantity:

$$\lambda^2=\frac{N}{a(a-1)}\sum_k (T_{(k)}-\hat{\theta})^2$$

Then, if we take the ratio of this quantity with the overall sample variance $\sigma^2$, we get another formula for the effective sample size:

$$N_{eff} = \frac{n\lambda^2}{\sigma^2}$$


## Effective sample size for multivariate draws

The aforementioned equations for the effective sample size are fine for draws of univariate quantities. We also want to know how to obtain an analogous number for vector-valued random processes. Researchers often attempt to do so by simply evaluating the scalar $N_{eff}$ for each individual dimension of a chain of vector samples, but this isn't very satisying. Fortunately, recent work by [Dats et al. (2019)](https://academic.oup.com/biomet/article/106/2/321/5426969) has shown that a the straightforward multivariate generalization of the above formula works perfectly well! We simply have to generalize the quantities $\lambda^2$ and $\sigma^2$ to their matrix counterparts:
$$\Lambda=\frac{N}{a(a-1)}\sum_k ({\vec{T}}_{(k)}-{\hat{\theta}})^T({\vec{T}}_{(k)}-\hat{{\theta}})$$
$$\Sigma=\frac{1}{N-1}\sum_i ({\vec{\theta_i}}-{\hat{\theta}})^T({\vec{\theta_i}}^{(k)}-\hat{{\theta}})$$
With these quantities, we write out the effective number of samples as before just with the matrix generalizations of all quantities involved. Note that here, $p$ represents the dimension of $\theta_i$.
$$N_{eff}^{multi} = N\left(\frac{\vert\Lambda\vert}{\vert\Sigma\vert}\right)^{1/p}$$
Note that you still need to choose how many batches are used - a rule-of-thumb (there are more technical conditions that are worth reading about, though) is to use a batch size of $\sqrt{N}$, so if you have 256 samples then there would be 16 batches of 16 samples each.

In the code below, I'll show how to calculate this for a toy example.


```python
import numpy as np

n    = 256 # Number of draws
p    = 10   # Dimension of each draw
cov  = np.eye(p) # True covariance matrix
mean = np.zeros(p) # true mean vector

samples = np.random.multivariate_normal(mean,cov,size=n)

n_batches         = int(n**0.5)
samples_per_batch = int(n / n_batches)

# Split up data into batches and take averages over
# individual batches as well as the whole dataset
batches     = samples.reshape(n_batches,samples_per_batch,p)
batch_means = batches.mean(axis=1)
full_mean   = samples.mean(axis=0)

# Calculate the matrix lam as a sum of vector
# outer products
prefactor       = samples_per_batch / (n_batches-1)
batch_residuals = (batch_means - full_mean)
lam = 0 
for i in range(n_batches):
    lam += prefactor * (batch_residuals[i:i+1,:] * batch_residuals[i:i+1,:].T)

sigma =  np.cov(samples.T)
n_eff = n* (np.linalg.det(lam) / np.linalg.det(sigma))**(1/p)

```

Let's see what $N_{eff}$ is for this case:


```python
print('There are {0} effective samples'.format(int(n_eff)))
```

    There are 166 effective samples


Since I used 256 truly independent samples in total, it appears that this statistic is somewhat conservative in reporting the effective sample size. I hope this was useful! Again, you can read more about this method at [this Biometrika article](https://academic.oup.com/biomet/article/106/2/321/5426969) by Dootika Vats et al.
