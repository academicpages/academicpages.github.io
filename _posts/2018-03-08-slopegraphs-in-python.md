---
title: Slopegraphs in python
permalink: /posts/2018/03/slopegraphs-in-python
date: 2018-03-08
tags:
    - python
    - plotting
    - coding
    - portfolio
---

Slopegraphs are always introduced as being introduced by this Edward Tufte [post](https://www.edwardtufte.com/bboard/q-and-a-fetch-msg?msg_id=0003nk), though [this page](http://charliepark.org/slopegraphs/) is my top Google hit for "slopegraph."
I'm not sure if the kind of plot I'm talking about is technically a slopegraph, but in my academic circles that's usually the term we end up settling on after a conversation that almost always sounds like, "you know, those plots which are kind of like boxplots except the paired points are connected with lines."

A [recent paper](https://www.ncbi.nlm.nih.gov/pubmed/28591632) (closed access, sorry) comparing microbiome and glycemic responses to different types of bread is the first example that comes to mind, but I do think these are fairly ubiquitous in the literature (if difficult to find, because there isn't a good keyword to search for!)
Technically they're not quite slopegraphs, since the points are showing continuous values rather than ordered categorical variables.
But, tomato toh-mah-toe.

![png](/images/2018-03-08-slopegraphs-in-python_files/slopegraph_example_Korem_2017.png)

Plotting paired data as slopegraphs is actually not my favorite way to show paired data, since in almost all cases the lines connecting the points end up very jumbled and difficult to distinguish any patterns from.
For example, in the Korem at al figure above, it's pretty unclear what we're supposed to get out of the figure (even though there aren't that many lines).
The takeaway is actually that there isn't really a trend either way, but even that isn't necessarily immediately obvious.

I think the best option to explore and analyze paired data is to put the points on a scatter plot, where the x- and y-axes show the value for each member of the pair.
For example, if you're plotting the average abundance of different microbes in healthy patients vs. patients with a disease, you'd have `abundance in healthy` on the x-axis and `abundance in diseased patients` on the y-axis, and each point would be a microbe.
Then, you can just look at how many points are above the y=x line vs. below to get a sense of which abundances are higher.
That said, these plots can be more difficult to interpret, especially for people who aren't as familiar with statistics or who are expecting a more "visual" slopegraph.

Another option is just to plot the differences between pairs of points, but then this loses information about the actual values of each point in the pairs.
And finally, regardless of the best way to show the data, many times your advisor wants you to try a slopegraph anyway and so you can choose to argue with her or just produce the plot and then decide together whether it's a good way to show the data.

So let's do that!

(Spoiler: in my particular case that motivated this post, my advisor ended up being right and the slopegraph was totally the best way to show the data. It's also very clinician-friendly, which is good because this was data for a clinical paper!)

# Generate data

First, let's set up some toy data. I'll use essentially the same data as in my [boxplots post](https://cduvallet.github.io/posts/2018/03/boxplots-in-python). We'll be simulating making some measurements on three different body sites for 15 healthy patients and 15 diseased patients. Because we're making slopegraphs, we're assuming that these are paired measurements - say, the abundance of a specific microbe on a tumor sample and the abundance of that same microbe on a nearby non-cancer sample.


```python
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline

# Set up the data
data = np.concatenate(
    [[np.random.normal(loc=1, size=15), 15*['site1'], 15*['healthy']],
     [np.random.normal(loc=3, size=15), 15*['site2'], 15*['healthy']],
     [np.random.normal(loc=0, size=15), 15*['site3'], 15*['healthy']],
     [np.random.normal(loc=1, size=15), 15*['site1'], 15*['disease']],
     [np.random.normal(loc=1, size=15), 15*['site2'], 15*['disease']],
     [np.random.normal(loc=3, size=15), 15*['site3'], 15*['disease']]],
    axis=1)
df = pd.DataFrame(columns=['value', 'site', 'label'], data=data.T)
df['value'] = df['value'].astype(float)

# Show every ninth row
df.iloc[::9]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>value</th>
      <th>site</th>
      <th>label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.462536</td>
      <td>site1</td>
      <td>healthy</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.606038</td>
      <td>site1</td>
      <td>healthy</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2.793179</td>
      <td>site2</td>
      <td>healthy</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2.903060</td>
      <td>site2</td>
      <td>healthy</td>
    </tr>
    <tr>
      <th>36</th>
      <td>-0.166360</td>
      <td>site3</td>
      <td>healthy</td>
    </tr>
    <tr>
      <th>45</th>
      <td>1.827056</td>
      <td>site1</td>
      <td>disease</td>
    </tr>
    <tr>
      <th>54</th>
      <td>1.483208</td>
      <td>site1</td>
      <td>disease</td>
    </tr>
    <tr>
      <th>63</th>
      <td>0.938095</td>
      <td>site2</td>
      <td>disease</td>
    </tr>
    <tr>
      <th>72</th>
      <td>1.203820</td>
      <td>site2</td>
      <td>disease</td>
    </tr>
    <tr>
      <th>81</th>
      <td>3.761979</td>
      <td>site3</td>
      <td>disease</td>
    </tr>
  </tbody>
</table>
</div>



# Make a basic slope graph


```python
fig, ax = plt.subplots(figsize=(4, 3))

# Set up list to track sites
sites = []
i = 1.0
for site, subdf in df.groupby('site'):
    sites.append(site)
    # Get the values for healthy and disease patients
    h = subdf.query('label == "healthy"')['value'].values
    d = subdf.query('label == "disease"')['value'].values

    # Set up the x-axis values
    x1 = i - 0.2
    x2 = i + 0.2

    # Plot the lines connecting the dots
    for hi, di in zip(h, d):
        ax.plot([x1, x2], [hi, di], c='gray')

    # Plot the points
    ax.scatter(len(h)*[x1-0.01], h, c='k',
               s=25, label='healthy')
    ax.scatter(len(d)*[x2+0.01], d, c='k',
               s=25, label='disease')


    # Update x-axis
    i += 1

# Fix the axes and labels
ax.set_xticks([1, 2, 3])
_ = ax.set_xticklabels(sites, fontsize='x-large')

```


![png](/images/2018-03-08-slopegraphs-in-python_files/2018-03-08-slopegraphs-in-python_4_0.png)

# Let's get fancier

That's the most basic skeleton code. Now let's add some bells and whistles:

- Change the color of the points to indicate healthy [blue] or disease [red].    
- Color the lines according to their slopes: blue if higher in healthy, red if higher in disease   
- Add a legend    


```python
red = '#C25539'
blue = '#3F7F93'

fig, ax = plt.subplots(figsize=(4, 3))

# Set up list to track sites
sites = []
i = 1.0
for site, subdf in df.groupby('site'):
    sites.append(site)
    # Get the values for healthy and disease patients
    h = subdf.query('label == "healthy"')['value'].values
    d = subdf.query('label == "disease"')['value'].values

    # Set up the x-axis values
    x1 = i - 0.2
    x2 = i + 0.2

    # Set up line color
    line_colors = (h - d) > 0
    line_colors = [blue if j else red for j in line_colors]

    # Also set up alpha values to make the lines slightly transparent
    alphas = [0.4]*len(line_colors)

    # Plot the lines connecting the dots
    for hi, di, ci, ai in zip(h, d, line_colors, alphas):
        ax.plot([x1, x2], [hi, di], c=ci, alpha=ai)

    # Plot the points
    # Note: s=25 increase the default point size, lw=0.5 decreases the default
    # point line width
    ax.scatter(len(h)*[x1-0.01], h, c=blue,
               s=25, lw=0.5, label='healthy')
    ax.scatter(len(d)*[x2+0.01], d, c=red,
               s=25, lw=0.5, label='disease')

    # Update x-axis
    i += 1

# Fix the axes and labels
ax.set_xticks([1, 2, 3])
_ = ax.set_xticklabels(sites, fontsize='x-large')

# Add legend and fix it to show only the first two elements
handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles[0:2], labels[0:2],   
              fontsize='large',
              loc='upper center',
              bbox_to_anchor=(0.5, 1.25),
              ncol=2,
              scatterpoints=1)
lgd.legendHandles[0]._sizes = [80]
lgd.legendHandles[1]._sizes = [80]

```


![png](/images/2018-03-08-slopegraphs-in-python_files/2018-03-08-slopegraphs-in-python_6_0.png)


Finally, if you want to get *really* fancy, you can overlay this with a boxplot and jitter the points.

Full disclosure: I made this plot just to see what it would look like, and quickly decided this was a terrible way to visualize data. But, since I went through the work of making it, perhaps it will be useful to someone someday!


```python
red = '#C25539'
blue = '#3F7F93'

fig, ax = plt.subplots(figsize=(4, 3))

# Set up list to track sites
sites = []
# Set up lists to track boxplot data
for_boxplot = []
positions = []

i = 1.0
for site, subdf in df.groupby('site'):
    sites.append(site)

    # Get the values for healthy and disease patients
    h = subdf.query('label == "healthy"')['value'].values
    d = subdf.query('label == "disease"')['value'].values

    # Set up the x-axis values
    x1 = i - 0.2
    x2 = i + 0.2

    ## Track values for one call to boxplot after the loop
    # Add the healthy (left) values first
    for_boxplot.append(h)
    # and disease (right) values next
    for_boxplot.append(d)    

    # And track positions
    positions += [x1, x2]

    # Set up line color
    line_colors = (h - d) > 0
    line_colors = [blue if j else red for j in line_colors]

    # Also set up alpha values to make the lines slightly transparent
    alphas = [0.4]*len(line_colors)

    # Plot the lines connecting the dots
    for hi, di, ci, ai in zip(h, d, line_colors, alphas):
        ax.plot([x1, x2], [hi, di], c=ci, alpha=ai)

    # Plot the points

    # Set up some noise for jitter
    noise = np.random.normal(loc=0, scale=0.025, size=len(h))

    ax.scatter(len(h)*[x1-0.01] + noise, h, c=blue,
               s=25, lw=0.5, label='healthy')
    ax.scatter(len(d)*[x2+0.01] + noise, d, c=red,
               s=25, lw=0.5, label='disease')

    # Update x-axis
    i += 1

## Overlay boxplot
# Set up some parameters for the boxplot
boxprops = {'linewidth': 0.75, 'color': 'k'}
lineprops = {'linewidth': 0.75, 'color': 'k', 'linestyle': '-'}

boxplot_kwargs = dict({'boxprops': boxprops, 'medianprops': lineprops,
                       'whiskerprops': lineprops, 'capprops': lineprops})
bp = ax.boxplot(for_boxplot, positions=positions,
                widths=0.3, **boxplot_kwargs)       

# Fix the axes and labels
ax.set_xticks([1, 2, 3])
_ = ax.set_xticklabels(sites, fontsize='x-large')

# Add legend and fix it to show only the first two elements
handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles[0:2], labels[0:2],   
              fontsize='large',
              loc='upper center',
              bbox_to_anchor=(0.5, 1.25),
              ncol=2,
              scatterpoints=1)
# Make the points in the legend larger
lgd.legendHandles[0]._sizes = [80]
lgd.legendHandles[1]._sizes = [80]

```


![png](/images/2018-03-08-slopegraphs-in-python_files/2018-03-08-slopegraphs-in-python_8_0.png)
