---
date: 2022-07-05
tags:
- stream
- python
- tips
title: Beware any vs len
---

I fell into the habit of using `any()` to check if a list is empty. It's nice because it works for any enumerable, including generators, even if `len()` is not defined.
However, it has a pitfall where if the list is nonempty but contains only falsy values, `any()` returns `False`. For this reason, I advise to use `len()` to check if a list is empty.

```python
In [1]: coll = [0]
   ...: if any(coll):
   ...:     print("has some!")
   ...: 

In [2]: coll = [0]
   ...: if len(coll) > 0:
   ...:     print("has some!")
   ...: 
has some!
```