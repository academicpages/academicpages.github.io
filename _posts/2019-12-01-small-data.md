---
title: 'Small Data'
date: 2019-12-01
permalink: /posts/2019/12/small-data/
tags:
  - ?
---

[Work In Progress]

# 1-Small Intro
---

Hello reader, this article is the short version of a [Stanford course](http://web.stanford.edu/~rjohari/teaching/notes/). 
I wrote it after an extensive reading of this course so that you don't have to.

The amount of data we collect is gargantuous (Facebook posts, tweets, medical tests...) and it often arriving faster than we can store and analyze it. 
> "Big" data can't be analyzed on a single machine.
On the contrary, small data can be analyzed and collected on a single machine (even though we now have 64GB of RAM at home).

This article aims at mastering the skills that will help you for "small" data analysis and thus for any data analysis.

# 2-Linear Regression
---

## Summerizing a sample
How can we summerize a sample? We first use simple statistics:
+ Sample mean
+ Sample median (more robust to outliers)
+ Sample standard deviation
All of them can be computed in one shot using pandas:
``python
import pandas as pd

df = pd.read_csv("some_data.csv")
df.describe()
>>>
``
    this is supposed to be code
    code again`

<script src="https://gist.github.com/Vincent-Maladiere/47afb09923df7581a34d5ae9a397339d.js"></script>

## Modeling relationships
We focus on modelizing relationships between observations. 

+ Let $Y=(Y_1, ..., Y_n)$ be the outcome, or target
+ Let $X$ be the features where rows are $X_i=(X_{i1}, ..., X_{ip})$
Our goal is to find a functional relationship such that
$$Y_i \approx f(X_i)$$




```python
%matplotlib inline
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

density_by_hour = {
     0: 0.012888057775425291,
     1: 0.008680583576807108,
     2: 0.006349450092942144,
     3: 0.006540568646330063,
     4: 0.008768223576426983,
     5: 0.01473392812886489,
     6: 0.025094152662242228,
     7: 0.03521227358221182,
     8: 0.05557100024089687,
     9: 0.046950603169852806,
     10: 0.05975931733116441,
     11: 0.061484362142959395,
     12: 0.06498649273017906,
     13: 0.06293924647399846,
     14: 0.07606518424839197,
     15: 0.06870810042488053,
     16: 0.06847142717289502,
     17: 0.07354926763279836,
     18: 0.06447830140708206,
     19: 0.050088447011664566,
     20: 0.04020322825935949,
     21: 0.039900938140188705,
     22: 0.03260026973811931,
     23: 0.015976575834318465}

density_to_df = []
for hour, density in density_by_hour.items():
    density_to_df.append({'hour': hour, 'density': density})
density_df = pd.DataFrame(density_to_df)

fig, ax = plt.subplots()
fig.set_size_inches(10, 5)
sns.barplot(x='hour', y='density', data=density_df)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x126c62a58>




![png](output_0_1.png)


