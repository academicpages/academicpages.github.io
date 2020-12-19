---
title: "A Pandas Surprise: Groupy and NaNs"
author: Simon R. Steinkamp
data: 2020-04-30
tags:
  - Python
  - Snippets
---
## A Pandas suprise: NaNs and with groupby

```python
import pandas as pd
import numpy as np
from pandas.errors import UnsupportedFunctionCall
```

I figured out something about pandas today, which I was very surprised by.
Applying `.groupby` on a `pd.DataFrame` automatically ignores `NaN` values. This is intendet behavior, but sometimes you actually want to have some `NaN` in the data, to check whether your data-frame is correct and to find possible corruptions.

Here is a little example:


```python
# Create a sample Array:
DF = pd.DataFrame.from_dict({'g1': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
                             'g2': ['c', 'c', 'd', 'd', 'c', 'c', 'd', 'd'],
                             'd1': [0, 1, np.nan, 3, 4, 5, 6, 7]})
```

Averaging the entries in `DF`, we would expect a `NaN` in group `a`, `d`, but we get `3.0`!


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



If you apply pandas `.mean()` method on a `DataFrame` you could speciy a `skipna = False` in the function. This, unfortunately doesn't work after using `.groupby`.


```python
# This creates an error
try:
    DF.groupby(['g1', 'g2']).mean(skipna=False)
except UnsupportedFunctionCall:
    print('UnsupportedFunctionCall')
```

    UnsupportedFunctionCall


I think, I have seen one solution to solve this issue statingt that using `.apply(np.mean)` instead of using `.mean()` might solve the problem.

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



Calling `np.mean` causes pandas to bypass the function and calls `DF.mean()` from pandas with `skipna=True`!
As far as I know, you have to create a new function to solve the issue.


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



# References:
* [https://stackoverflow.com/questions/26145585/pandas-aggregation-ignoring-nans](https://stackoverflow.com/questions/26145585/pandas-aggregation-ignoring-nans)
* [https://github.com/pandas-dev/pandas/issues/15674](https://github.com/pandas-dev/pandas/issues/15674)
* [https://stackoverflow.com/questions/54106112/pandas-groupby-mean-not-ignoring-nans](https://stackoverflow.com/questions/54106112/pandas-groupby-mean-not-ignoring-nans)
