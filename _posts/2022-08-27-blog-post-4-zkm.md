---
title: 'Markdown代码语法'
date: 2022-08-27
permalink: /posts/2022/08/markdown-6-zkm/
tags:
  - cool posts
  - markdown
  - 代码
---
要将单词或短语表示为代码，请将其包裹在反引号（`` ` ``）中。  

# 单词或短语  
```
pyhon包有：`numpy`、`matplotlib`等等。
```
渲染效果如下：  
pyhon包有：`numpy`、`matplotlib`等等。

# 转义-双反引号  
```
反引号本身要显示出来，例如通过反引号包裹单词表示为代码：`` `matplotlib`、`numpy` ``等
```  
渲染效果如下：  
反引号本身要显示出来，例如通过反引号包裹单词表示为代码：`` `matplotlib`、`numpy` ``等
# 代码块  
要创建代码块，请将代码块的每一行缩进至少4个空格或1个制表符。  
```
    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure()
    sub = fig.add_subplot(111)
```  
渲染效果如下：  

    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure()
    sub = fig.add_subplot(111)
