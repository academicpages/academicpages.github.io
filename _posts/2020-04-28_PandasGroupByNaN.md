---
title: 'A Pandas suprise: NaNs and with groupby'
date: 2020-04-28
permalink: /posts/2012/08/blog-post-4/
tags:
  - python
  - hacks_and_tricks
  - fun
---

# A Pandas surprise: NaNs and GroupBy


```python
import pandas as pd
import numpy as np
from pandas.errors import UnsupportedFunctionCall
```

I figure out something about pandas today, which I was quite surprised by.
When you use pandas groupby - NaNs are automatically ignored.

Well this is intended, but sometimes you might be in the situation that you want to have NaNs in the summary. For example, for a quick check, whether all the data are correct. 


```python
# Create a sample Array:
DF = pd.DataFrame.from_dict({'g1': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'], 
                             'g2': ['c', 'c', 'd', 'd', 'c', 'c', 'd', 'd'],
                             'd1': [0, 1, np.nan, 3, 4, 5, 6, 7]})
```

For example in this little example DF we would expect a `NaN` in group `a`, `b`, but we get a `0.5`.


```python
DF.groupby(['g1', 'g2']).mean()
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
      <th></th>
      <th>d1</th>
    </tr>
    <tr>
      <th>g1</th>
      <th>g2</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>c</th>
      <td>0.5</td>
    </tr>
    <tr>
      <th>d</th>
      <td>3.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">b</th>
      <th>c</th>
      <td>4.5</td>
    </tr>
    <tr>
      <th>d</th>
      <td>6.5</td>
    </tr>
  </tbody>
</table>
</div>



The thing is, you cannot use `skipna = False` in the mean, and neither in the summing function.


```python
# This creates an error
try:
    DF.groupby(['g1', 'g2']).mean(skipna=False)
except UnsupportedFunctionCall:
    print('UnsupportedFunctionCall')
```

    UnsupportedFunctionCall


One example that has often been given is to use `.apply(np.mean)` instead of directly calling `.mean()`

However:


```python
DF.groupby(['g1', 'g2']).apply(np.mean)
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
      <th></th>
      <th>d1</th>
    </tr>
    <tr>
      <th>g1</th>
      <th>g2</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>c</th>
      <td>0.5</td>
    </tr>
    <tr>
      <th>d</th>
      <td>3.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">b</th>
      <th>c</th>
      <td>4.5</td>
    </tr>
    <tr>
      <th>d</th>
      <td>6.5</td>
    </tr>
  </tbody>
</table>
</div>



Calling `np.mean` causes pands to bypass the function and calls `DF.mean()`, pandas function with `skipna=True`! 
Afaik, you need to create a new function (or a partial, don't know much about that), but still:


```python
def mean_w_nan(x):
    # Don't forget the np.array call!
    return np.mean(np.array(x))

DF.groupby(['g1', 'g2']).apply(mean_w_nan)
```




    g1  g2
    a   c     0.5
        d     NaN
    b   c     4.5
        d     6.5
    dtype: float64



# Information:
* https://stackoverflow.com/questions/26145585/pandas-aggregation-ignoring-nans
* https://github.com/pandas-dev/pandas/issues/15674
* https://stackoverflow.com/questions/54106112/pandas-groupby-mean-not-ignoring-nans
