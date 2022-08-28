---
title: 'Markdown链接语法'
date: 2022-08-27
permalink: /posts/2022/08/markdown-8-zkm/
tags:
  - cool posts
  - markdown
  - 链接
---
链接文本放在中括号内，链接地址放在后面的括号中，链接title可选。  
超链接Markdown语法代码：`[超链接显示名](超链接地址 “超链接title”)`  
```
这是[个人学术主页](zhangkmsjtu.githu.io)。
```  
渲染效果如下：  
这是[个人学术主页](zhangkmsjtu.githu.io)。

# 添加title  
```
这是[个人学术主页](zhangkmsjtu.githu.io "zhangkm")。
```  
渲染效果如下：  
这是[个人学术主页](zhangkmsjtu.githu.io "zhangkm")。

# 网址和Email  
使用尖括号可以很方便地把URL或者Email地址变成可点击的链接。  
```
个人学术网页：<https://zhangkmsjtu.github.io/>
工作邮箱：<zhangkeming@usst.edu.cn>
```
渲染效果如下：  
个人学术网页：<https://zhangkmsjtu.github.io/>
工作邮箱：<zhangkeming@usst.edu.cn>

# 格式化链接  
```
这是 **[个人学术主页](zhangkmsjtu.githu.io "zhangkm")**。
这是 *[个人学术主页](zhangkmsjtu.githu.io "zhangkm")*。
这是 [`个人学术主页`](zhangkmsjtu.githu.io "zhangkm")。
```  
渲染效果如下：  

这是 **[个人学术主页](zhangkmsjtu.githu.io "zhangkm")**。
这是 *[个人学术主页](zhangkmsjtu.githu.io "zhangkm")*。
这是 [`个人学术主页`](zhangkmsjtu.githu.io "zhangkm")。

# 引用-参考文献  
引用样式链接是一种特殊的链接，它使URL在Markdown中更易于显示和阅读。参考样式链接分为两部分：与文本保持内联的部分以及存储在文件中其他位置的部分，以使文本易于阅读。  
## 第一部分  
引用类型的链接的第一部分使用两组括号进行格式设置。第一组方括号包围链接的文本。第二组括号显示了一个标签，该标签用于指向您存储在文档其他位置的链接。  
尽管不是必须的，可以在第一组和第二组括号之间包含一个空格。第二组括号中的标签不区分大小写，可以包含字母、数字、空格和标点符号。  
以下示例格式对于链接的第一部分效果相同：  
-  [usst][1]
-  [usst] [1]

## 第二部分  
引用类型链接的第二部分使用以下属性设置格式：  
1. 放在括号中的标签，其后紧跟一个冒号和至少一个空格（例如：`[usst][1]: `） 
2. 链接的URL，可以选择将其括在尖括号中。  
3. 链接的可选标题，可以将其括在双引号，单引号或括号中。

以下示例格式对于链接的第二部分效果相同：  
- `[1]: https:\\usst.edu.cn`
- `[1]: https:\\usst.edu.cn 'usst'`
- `[1]: https:\\usst.edu.cn "usst"`
- `[1]: https:\\usst.edu.cn (usst)`
- `[1]: <https:\\usst.edu.cn> 'usst'`
- `[1]: <https:\\usst.edu.cn> "usst"`
- `[1]: <https:\\usst.edu.cn> (usst)`

可以将链接的第二部分放在Markdown文档中的任何位置。有些人将它们放在出现的段落之后，有些人则将它们放在文档的末尾。  
这是学校 [官网][1]。
这是个人 [学术主页][2]。

[1]: <https:\\usst.edu.cn>
[2]: zhangkmsjtu.github.in