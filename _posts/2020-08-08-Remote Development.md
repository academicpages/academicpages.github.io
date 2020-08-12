---
title: 'Remote Development'
date: 2020-08-01
permalink: /posts/2020/08/remote-dev/
tags:
  - covid
  - programming
  - software
---

A review of tools and workflows for remote working. Code and view outputs from a laptop, run heavy computation from a server.

```
  import numpy as np
  from abc import ABC, abstractmethod
  from tqdm import tqdm

  class ERS(ABC):
      def __init__(self, dimension):
          self.dimension = dimension
```
