---
date: 2022-06-23
tags:
- stream
- python
- tips
title: Print pandas Series as percent
---

Use this snippet to print a `pd.Series` of floats as percentages.
```python
.apply(lambda x: x * 100).apply("{:,.2f}%".format)
```

Example:
```python
In [1]: import pandas as pd

In [2]: s = pd.Series([2.0, 0.5435, 0.999999, 0.04999])

In [3]: print(s)
0    2.000000
1    0.543500
2    0.999999
3    0.049990
dtype: float64

In [4]: print(s.apply(lambda x: x * 100).apply("{:,.2f}%".format))
0    200.00%
1     54.35%
2    100.00%
3      5.00%
dtype: object

In [5]: print(pd
			  .Series([1, 1, 2, 3, 4, 4, 4, 5])
			  .value_counts(normalize=True)
			  .apply(lambda x: x * 100).apply("{:,.2f}%".format)
			  )
4    37.50%
1    25.00%
2    12.50%
3    12.50%
5    12.50%
dtype: object
```