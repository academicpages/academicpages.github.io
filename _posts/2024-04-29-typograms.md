---
layout: post
title: a post with typograms
date: 2024-04-29 23:36:10
description: this is what included typograms code could look like
tags: formatting diagrams
categories: sample-posts
typograms: true
---

This is an example post with some [typograms](https://github.com/google/typograms/) code.

````markdown
```typograms
+----+
|    |---> My first diagram!
+----+
```
````

Which generates:

```typograms
+----+
|    |---> My first diagram!
+----+
```

Another example:

````markdown
```typograms
.------------------------.
|.----------------------.|
||"https://example.com" ||
|'----------------------'|
| ______________________ |
||                      ||
||   Welcome!           ||
||                      ||
||                      ||
||  .----------------.  ||
||  | username       |  ||
||  '----------------'  ||
||  .----------------.  ||
||  |"*******"       |  ||
||  '----------------'  ||
||                      ||
||  .----------------.  ||
||  |   "Sign-up"    |  ||
||  '----------------'  ||
||                      ||
|+----------------------+|
.------------------------.
```
````

which generates:

```typograms
.------------------------.
|.----------------------.|
||"https://example.com" ||
|'----------------------'|
| ______________________ |
||                      ||
||   Welcome!           ||
||                      ||
||                      ||
||  .----------------.  ||
||  | username       |  ||
||  '----------------'  ||
||  .----------------.  ||
||  |"*******"       |  ||
||  '----------------'  ||
||                      ||
||  .----------------.  ||
||  |   "Sign-up"    |  ||
||  '----------------'  ||
||                      ||
|+----------------------+|
.------------------------.
```

For more examples, check out the [typograms documentation](https://google.github.io/typograms/#examples).
