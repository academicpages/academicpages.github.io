---
title: "TSPLIB with Profits"
excerpt: "Python library for parsing TSP with Profits datasets."
collection: portfolio
---

[See the code](https://github.com/PatrickOHara/tspwplib) and [read the docs](https://patrickohara.github.io/tspwplib/).

Get an instance of the Orienteering Problem:

```python
import os
from tspwplib import *

oplib_root = os.getenv("OPLIB_ROOT")    # TODO set your path to oplib
filepath = build_path_to_oplib_instance(
    oplib_root, Generation.gen1, GraphName.st70
)
problem = ProfitsProblem.load(filepath)
```


Get a [networkx](https://networkx.org/) graph with attributes for prize on the vertices and cost on the edges:

```python
nx_graph = problem.get_graph()
```

**Acknowledgements**: This library relies heavily upon [tsplib95](https://github.com/rhgrant10/tsplib95.git) and [OPLib](https://github.com/bcamath-ds/OPLib.git).
