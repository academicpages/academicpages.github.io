---
title: Nonparametric changepoint model in PyMC 
layout: single
mathjax: true
comments: true
---

# Changepoint models

Identifying structural breaks in data is an important problem to folks that frequently work with time series data. Some examples of how people have dealt with the problem of a single changepoint can be found [here](https://cscherrer.github.io/post/bayesian-changepoint/) and [here](https://mc-stan.org/docs/2_23/stan-users-guide/change-point-section.html). 

Generally, the setup looks like this: we have some data $X_t$ indexed by a discrete time coordinate $t \in \{1,...,T\}$ and a parametric submodel linking the distribution of $X$ to another quantity $\mu_t$ which depends on the temporal coordinate. For the simple case of a linear Gaussian model with a single change point, we have


$$a_1, a_2 \sim N(0, \sigma^2_\mu)$$

$$\tau \sim \text{DiscreteUniform}(\{1,...,T\})$$

$$\mu_t = \left\{
    \begin{array}{l}
      a_1 \text{ if } t > \tau \\
      a_2 \text{ if } t \le \tau
    \end{array}
  \right. $$

$$X_t \sim N(\mu_t, \sigma_\epsilon)$$

with your scale priors of choice on the variance parameters $\sigma_\epsilon$ and $\sigma_\mu$. Now, one of the main conceptual problems with this model is that you need to assume it has a single changepoint. You can relax that assumption by extending this model to include more $\tau$ and $a$ parameters, but you'll still need to specify the number of them ahead of time. 

Relaxing the assumption on the number of parameters is, for the most part, a solved problem in the research community (see [here](https://www.sciencedirect.com/science/article/abs/pii/S0167715297000503) and [here](https://repository.upenn.edu/cgi/viewcontent.cgi?article=1376&context=statistics_papers) for a few representative examples). Unfortunately, these require the analyst to implement the inference techniques presented by hand; these are often Gibbs samplers or similar. Wouldn't it be nice to just be able to use a PPL and write down the forward process instead?

That's the point of this notebook - we'll walk through a construction of a changepoint model plus inference in PyMC which is considerably more straightforward than a handwritten sampler. 

We'll start by simulating some data over 50 timesteps; there are 4 changepoints 
and the model's likelihood is Gaussian. We will use a standard set of imports for working with PyMC and set the seed for repeatability.


```python
import pymc as pm
import matplotlib.pyplot as plt
import numpy as np
import aesara.tensor as at
from collections import Counter
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('svg', 'pdf')
np.random.seed(827)
```

# Simulating a dataset

Since the generative process for this data is simple, the code required to simulate data is relatively short. We begin by sampling the changepoints and then adding offsets for each changepoint to the mean value of the data. We then perturb this mean with normal noise variates to create simulated observations.


```python
T = 50
noise_sd = 0.15
n_changepoints = 4
true_cp = np.sort(np.random.choice(T, size=n_changepoints))
offsets_per_period = np.random.randn(n_changepoints)

noiseless = np.zeros(T)
start_time = 0

for changepoint, offset in zip(true_cp, offsets_per_period):
  noiseless[start_time:changepoint] += offset
  start_time = changepoint

xs = noiseless + np.random.randn(T) * noise_sd
```

As we can see below, the green changepoints do clearly correspond to changes in the level of the time series. However, not all of them are obvious - the last one, in particular, is a relatively small jump.


```python
plt.figure(figsize=(9,3))
plt.plot(xs, marker='o', color='k', label='Observed data')
plt.plot(noiseless, color='g', label='Noise-free mean value')

for i, cp in enumerate(true_cp):
  if i == 0:
    label = 'Change point'
  else:
    label=None
  plt.axvline(cp, color='g', linestyle='--',label=label)

plt.legend()

plt.xlabel('Timestep',fontsize=12)
plt.ylabel('$X(t)$',fontsize=18);
```


    
![svg](/images/cp_data.svg)
    


# Creating the model

For inference, we'll assume that we don't know the number of changepoints. The main trick that we'll use is to instantiate way more changepoints than we need, and use latent variables to zero out most of them.

The model that we declare looks like the following:
$$p_{changepoint} \sim \text{Beta}(2,8)$$

$$\tau_1,...,\tau_{M} \sim \text{DiscreteUniform}(\{1,...,T\})$$ 

$$u_1,...,u_M \sim \text{Bernoulli}(p_{changepoint})$$

$$\mu \sim \text{Normal}(0, 1)$$

$$\sigma^2_{\delta} \sim \text{HalfNormal}(2)$$

$$\sigma^2_{\epsilon} \sim \text{HalfNormal}(1)$$

$$\delta_1,...,\delta_M \sim \text{Normal}(0, \sigma^2_{\delta})$$

For convenience in our notation, we assume that $\tau_1,...,\tau_M$ are ordered. We perform an elementwise multiplication of the $\delta$ offsets with 
the latent binary variables $u_m$ as well as indicator variables $I$ $\mu_t$:

$$\mu_t = \left[\left( \begin{array}{ccc}
I(t\ge \tau_1)  \\
\vdots \\
I(t\ge \tau_M)   \end{array}  \right) \odot \left( \begin{array}{ccc}
\delta_1  \\
\vdots \\
\delta_M   \end{array} \right)\right] \left(\begin{array}{ccc} u_1 \cdots u_M \end{array}\right)$$

$$X_t \sim N(\mu_t, \sigma^2_\epsilon)$$

Since $p_{changepoint}$ has a prior encouraging it to be lower, the indicator variables above will be pushed towards zero, thereby deactivating some of the $\delta$ terms' contributions towards $X$.

The code block below implements this model logic, though it uses `uniform_except_ends` to prevent any $\tau$ values from occurring in the first two or last two timesteps.


```python
max_cp_inference = 10

tiled_times = np.arange(T)[:, None].repeat(max_cp_inference, axis=1)

# We do this so that we can allow the Categorical prior over the changepoint
# locations to exclude the timesteps at the very beginning and very end. 
# The reason for this is that these data points always benefit from using an 
# extra changepoint just for the first or last data points. 
uniform_except_ends = np.ones(T)
uniform_except_ends[0:2] = 0
uniform_except_ends[-2:] = 0
uniform_except_ends = uniform_except_ends / uniform_except_ends.sum()

with pm.Model() as model:
  # Probability that any of the <max_cp_inference> change points are active
  p_changepoint  = pm.Beta('p_changepoint', alpha=2, beta=8)

  # Sort the changepoints for faster mixing / convergence
  changepoints = pm.Categorical('changepoints', uniform_except_ends, shape=max_cp_inference)
  is_cp_active = pm.Bernoulli('is_cp_active', p_changepoint, shape=max_cp_inference)

  changepoints_sorted = at.sort(changepoints)

  # This will give us a nice posterior estimate of the number of changepoints
  num_active_cp = pm.Deterministic('num_active_cp', pm.math.sum(is_cp_active))

  global_mean = pm.Normal('global_mean', sigma=1)
  cp_sd = pm.HalfNormal('cp_sd', sigma=2)
  noise_sd = pm.HalfNormal('noise_sd', sigma=1)
  changepoint_deltas = pm.Normal('changepoint_deltas', cp_sd, shape=max_cp_inference)

  # Operation involves operations on arrays with shape (T, max_cp_inference)
  # Elementwise operation zeros-out contributions from changepoints which are
  # not active
  is_timestep_past_cp = (tiled_times > changepoints[None, :].repeat(T, axis=0))
  active_deltas = (changepoint_deltas*is_cp_active)
  cp_contrib = pm.Deterministic('cp_contrib',
                                global_mean + pm.math.sum(is_timestep_past_cp * active_deltas, axis=1)
  )

  _ = pm.Normal('likelihood', mu=cp_contrib, sigma=noise_sd, observed=xs)

  trace = pm.sample(draws=8000, tune=8000, chains=2)

```



<style>
    /* Turns off some styling */
    progress {
        /* gets rid of default border in Firefox and Opera. */
        border: none;
        /* Needs to be in here for Safari polyfill so background images work as expected. */
        background-size: auto;
    }
    progress:not([value]), progress:not([value])::-webkit-progress-bar {
        background: repeating-linear-gradient(45deg, #7e7e7e, #7e7e7e 10px, #5c5c5c 10px, #5c5c5c 20px);
    }
    .progress-bar-interrupted, .progress-bar-interrupted::-webkit-progress-bar {
        background: #F44336;
    }
</style>





<div>
  <progress value='16000' class='' max='16000' style='width:300px; height:20px; vertical-align: middle;'></progress>
  100.00% [16000/16000 02:30&lt;00:00 Sampling chain 0, 6,594 divergences]
</div>





<style>
    /* Turns off some styling */
    progress {
        /* gets rid of default border in Firefox and Opera. */
        border: none;
        /* Needs to be in here for Safari polyfill so background images work as expected. */
        background-size: auto;
    }
    progress:not([value]), progress:not([value])::-webkit-progress-bar {
        background: repeating-linear-gradient(45deg, #7e7e7e, #7e7e7e 10px, #5c5c5c 10px, #5c5c5c 20px);
    }
    .progress-bar-interrupted, .progress-bar-interrupted::-webkit-progress-bar {
        background: #F44336;
    }
</style>





<div>
  <progress value='16000' class='' max='16000' style='width:300px; height:20px; vertical-align: middle;'></progress>
  100.00% [16000/16000 03:03&lt;00:00 Sampling chain 1, 3,278 divergences]
</div>



    ERROR:pymc:There were 6594 divergences after tuning. Increase `target_accept` or reparameterize.
    WARNING:pymc:The acceptance probability does not match the target. It is 0.08247, but should be close to 0.8. Try to increase the number of tuning steps.
    ERROR:pymc:There were 9872 divergences after tuning. Increase `target_accept` or reparameterize.
    WARNING:pymc:The acceptance probability does not match the target. It is 0.5083, but should be close to 0.8. Try to increase the number of tuning steps.


From a sampling perspective, this is a pretty ugly problem. NUTS isn't designed to work well in an alternating NUTS / Gibbs sampling scheme, and we get tons of divergences because NUTS is facing a log-posterior landscape that is shifting dramatically on every iteration because of the discrete latent variables.

That said, the $\hat{R}$ values look good - no warnings are fired off!

# Assessing the results from inference

As a basic statistic for the number of changepoints, we can just take the posterior mean of the indicator variables' sum to see how many parameters were active, on average.


```python
trace.posterior['num_active_cp'].mean()
```




<div><svg style="position: absolute; width: 0; height: 0; overflow: hidden">
<defs>
<symbol id="icon-database" viewBox="0 0 32 32">
<path d="M16 0c-8.837 0-16 2.239-16 5v4c0 2.761 7.163 5 16 5s16-2.239 16-5v-4c0-2.761-7.163-5-16-5z"></path>
<path d="M16 17c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
<path d="M16 26c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
</symbol>
<symbol id="icon-file-text2" viewBox="0 0 32 32">
<path d="M28.681 7.159c-0.694-0.947-1.662-2.053-2.724-3.116s-2.169-2.030-3.116-2.724c-1.612-1.182-2.393-1.319-2.841-1.319h-15.5c-1.378 0-2.5 1.121-2.5 2.5v27c0 1.378 1.122 2.5 2.5 2.5h23c1.378 0 2.5-1.122 2.5-2.5v-19.5c0-0.448-0.137-1.23-1.319-2.841zM24.543 5.457c0.959 0.959 1.712 1.825 2.268 2.543h-4.811v-4.811c0.718 0.556 1.584 1.309 2.543 2.268zM28 29.5c0 0.271-0.229 0.5-0.5 0.5h-23c-0.271 0-0.5-0.229-0.5-0.5v-27c0-0.271 0.229-0.5 0.5-0.5 0 0 15.499-0 15.5 0v7c0 0.552 0.448 1 1 1h7v19.5z"></path>
<path d="M23 26h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 22h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 18h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
</symbol>
</defs>
</svg>
<style>/* CSS stylesheet for displaying xarray objects in jupyterlab.
 *
 */

:root {
  --xr-font-color0: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --xr-font-color2: var(--jp-content-font-color2, rgba(0, 0, 0, 0.54));
  --xr-font-color3: var(--jp-content-font-color3, rgba(0, 0, 0, 0.38));
  --xr-border-color: var(--jp-border-color2, #e0e0e0);
  --xr-disabled-color: var(--jp-layout-color3, #bdbdbd);
  --xr-background-color: var(--jp-layout-color0, white);
  --xr-background-color-row-even: var(--jp-layout-color1, white);
  --xr-background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme=dark],
body.vscode-dark {
  --xr-font-color0: rgba(255, 255, 255, 1);
  --xr-font-color2: rgba(255, 255, 255, 0.54);
  --xr-font-color3: rgba(255, 255, 255, 0.38);
  --xr-border-color: #1F1F1F;
  --xr-disabled-color: #515151;
  --xr-background-color: #111111;
  --xr-background-color-row-even: #111111;
  --xr-background-color-row-odd: #313131;
}

.xr-wrap {
  display: block !important;
  min-width: 300px;
  max-width: 700px;
}

.xr-text-repr-fallback {
  /* fallback to plain text repr when CSS is not injected (untrusted notebook) */
  display: none;
}

.xr-header {
  padding-top: 6px;
  padding-bottom: 6px;
  margin-bottom: 4px;
  border-bottom: solid 1px var(--xr-border-color);
}

.xr-header > div,
.xr-header > ul {
  display: inline;
  margin-top: 0;
  margin-bottom: 0;
}

.xr-obj-type,
.xr-array-name {
  margin-left: 2px;
  margin-right: 10px;
}

.xr-obj-type {
  color: var(--xr-font-color2);
}

.xr-sections {
  padding-left: 0 !important;
  display: grid;
  grid-template-columns: 150px auto auto 1fr 20px 20px;
}

.xr-section-item {
  display: contents;
}

.xr-section-item input {
  display: none;
}

.xr-section-item input + label {
  color: var(--xr-disabled-color);
}

.xr-section-item input:enabled + label {
  cursor: pointer;
  color: var(--xr-font-color2);
}

.xr-section-item input:enabled + label:hover {
  color: var(--xr-font-color0);
}

.xr-section-summary {
  grid-column: 1;
  color: var(--xr-font-color2);
  font-weight: 500;
}

.xr-section-summary > span {
  display: inline-block;
  padding-left: 0.5em;
}

.xr-section-summary-in:disabled + label {
  color: var(--xr-font-color2);
}

.xr-section-summary-in + label:before {
  display: inline-block;
  content: '►';
  font-size: 11px;
  width: 15px;
  text-align: center;
}

.xr-section-summary-in:disabled + label:before {
  color: var(--xr-disabled-color);
}

.xr-section-summary-in:checked + label:before {
  content: '▼';
}

.xr-section-summary-in:checked + label > span {
  display: none;
}

.xr-section-summary,
.xr-section-inline-details {
  padding-top: 4px;
  padding-bottom: 4px;
}

.xr-section-inline-details {
  grid-column: 2 / -1;
}

.xr-section-details {
  display: none;
  grid-column: 1 / -1;
  margin-bottom: 5px;
}

.xr-section-summary-in:checked ~ .xr-section-details {
  display: contents;
}

.xr-array-wrap {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 20px auto;
}

.xr-array-wrap > label {
  grid-column: 1;
  vertical-align: top;
}

.xr-preview {
  color: var(--xr-font-color3);
}

.xr-array-preview,
.xr-array-data {
  padding: 0 5px !important;
  grid-column: 2;
}

.xr-array-data,
.xr-array-in:checked ~ .xr-array-preview {
  display: none;
}

.xr-array-in:checked ~ .xr-array-data,
.xr-array-preview {
  display: inline-block;
}

.xr-dim-list {
  display: inline-block !important;
  list-style: none;
  padding: 0 !important;
  margin: 0;
}

.xr-dim-list li {
  display: inline-block;
  padding: 0;
  margin: 0;
}

.xr-dim-list:before {
  content: '(';
}

.xr-dim-list:after {
  content: ')';
}

.xr-dim-list li:not(:last-child):after {
  content: ',';
  padding-right: 5px;
}

.xr-has-index {
  font-weight: bold;
}

.xr-var-list,
.xr-var-item {
  display: contents;
}

.xr-var-item > div,
.xr-var-item label,
.xr-var-item > .xr-var-name span {
  background-color: var(--xr-background-color-row-even);
  margin-bottom: 0;
}

.xr-var-item > .xr-var-name:hover span {
  padding-right: 5px;
}

.xr-var-list > li:nth-child(odd) > div,
.xr-var-list > li:nth-child(odd) > label,
.xr-var-list > li:nth-child(odd) > .xr-var-name span {
  background-color: var(--xr-background-color-row-odd);
}

.xr-var-name {
  grid-column: 1;
}

.xr-var-dims {
  grid-column: 2;
}

.xr-var-dtype {
  grid-column: 3;
  text-align: right;
  color: var(--xr-font-color2);
}

.xr-var-preview {
  grid-column: 4;
}

.xr-var-name,
.xr-var-dims,
.xr-var-dtype,
.xr-preview,
.xr-attrs dt {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-right: 10px;
}

.xr-var-name:hover,
.xr-var-dims:hover,
.xr-var-dtype:hover,
.xr-attrs dt:hover {
  overflow: visible;
  width: auto;
  z-index: 1;
}

.xr-var-attrs,
.xr-var-data {
  display: none;
  background-color: var(--xr-background-color) !important;
  padding-bottom: 5px !important;
}

.xr-var-attrs-in:checked ~ .xr-var-attrs,
.xr-var-data-in:checked ~ .xr-var-data {
  display: block;
}

.xr-var-data > table {
  float: right;
}

.xr-var-name span,
.xr-var-data,
.xr-attrs {
  padding-left: 25px !important;
}

.xr-attrs,
.xr-var-attrs,
.xr-var-data {
  grid-column: 1 / -1;
}

dl.xr-attrs {
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 125px auto;
}

.xr-attrs dt,
.xr-attrs dd {
  padding: 0;
  margin: 0;
  float: left;
  padding-right: 10px;
  width: auto;
}

.xr-attrs dt {
  font-weight: normal;
  grid-column: 1;
}

.xr-attrs dt:hover span {
  display: inline-block;
  background: var(--xr-background-color);
  padding-right: 10px;
}

.xr-attrs dd {
  grid-column: 2;
  white-space: pre-wrap;
  word-break: break-all;
}

.xr-icon-database,
.xr-icon-file-text2 {
  display: inline-block;
  vertical-align: middle;
  width: 1em;
  height: 1.5em !important;
  stroke-width: 0;
  stroke: currentColor;
  fill: currentColor;
}
</style><pre class='xr-text-repr-fallback'>&lt;xarray.DataArray &#x27;num_active_cp&#x27; ()&gt;
array(3.2660625)</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.DataArray</div><div class='xr-array-name'>'num_active_cp'</div></div><ul class='xr-sections'><li class='xr-section-item'><div class='xr-array-wrap'><input id='section-66376803-d2ba-411c-ba76-1595bd10deff' class='xr-array-in' type='checkbox' checked><label for='section-66376803-d2ba-411c-ba76-1595bd10deff' title='Show/hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-array-preview xr-preview'><span>3.266</span></div><div class='xr-array-data'><pre>array(3.2660625)</pre></div></div></li><li class='xr-section-item'><input id='section-b11f32d2-7f05-4c59-92c9-35b91eea8d9e' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-b11f32d2-7f05-4c59-92c9-35b91eea8d9e' class='xr-section-summary'  title='Expand/collapse section'>Coordinates: <span>(0)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'></ul></div></li><li class='xr-section-item'><input id='section-7ea59420-61bc-4db6-b96c-ab2986f71ecb' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-7ea59420-61bc-4db6-b96c-ab2986f71ecb' class='xr-section-summary'  title='Expand/collapse section'>Attributes: <span>(0)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'></dl></div></li></ul></div></div>



We can also make a plot of the posterior inferences about the location and parameters of each changepoint as compared against the true values:


```python
top_10_cp = Counter(
    trace.posterior['changepoints'].to_numpy().ravel().tolist()
    ).most_common(10)

plt.figure(figsize=(9,4))
plt.plot(noiseless, label='True noiseless values', color='green')

plt.plot(trace.posterior['cp_contrib'].mean(axis=(0,1)), label='Inferred noiseless mean', color='orange')

q10, q90 = np.percentile(trace.posterior['cp_contrib'], [10,90], axis=(0,1))
plt.fill_between(np.arange(T), q10, q90, color='orange', alpha=0.2)
plt.plot(xs, linestyle='', color='k', marker='o', label='Observed data')
for i, cp in enumerate(true_cp):
  if i == 0:
    label = 'True change point'
  else:
    label=None
  plt.axvline(cp, color='g', linestyle='--',label=label)

for i, (t, _) in enumerate(top_10_cp):
  if i == 0:
    label = 'Inferred change point'
  else:
    label=None
  plt.axvline(t, color='orange', linestyle='--', label=label)
plt.xlabel('Timestep',fontsize=12)
plt.ylabel('$X(t)$',fontsize=18)
plt.legend(loc='upper right');
```


    
![svg](/images/cp_inference.svg)
    


Here, the green vertical lines are the true changepoints while the orange vertical lines are one of the top 10 most likely changepoints as gleaned from the posterior samples. We can see that the major jumps around timesteps 10 and 20 are clearly captured, while there is more uncertainty from timesteps 20-40. The smaller jump at timestep 45 is also missed completely; this is not very surprising given how small it was.
