---
title: 'Markdown引用语法'
date: 2012-08-27
permalink: /posts/2012/08/markdown-4-zkm/
tags:
  - cool posts
  - markdown
  - 引用
---

要创建应用块，请在段落前添加一个`>`符号。  
```
> If we knew what it was we were doing, it would not be called research, would it?---Albert Einstein
```
渲染效果如下：  
> If we knew what it was we were doing, it would not be called research, would it?---Albert Einstein

块引用-多个段落
======
块引用可以包含多个段落。为段落之间的空白行添加一个`>`符号。  
```
> If we knew what it was we were doing, it would not be called research, would it?---Albert Einstein
> 
> 科学是包罗万象的事业，它需要有各方面的才能。---杨振宁
```
渲染效果如下：  
> If we knew what it was we were doing, it would not be called research, would it?---Albert Einstein
> 
> 科学是包罗万象的事业，它需要有各方面的才能。---杨振宁

嵌套引用
======
块引用可以嵌套。在要嵌套的段落前添加一个`>>`符号。  
```
> 科学研究中任何成就都是经过几次、几十次，甚至成百上千次失败而取得的......因此不要一碰到困难就苦恼、动摇起来。

>> ————《华罗庚传》
```
渲染效果如下：  
> 科学研究中任何成就都是经过几次、几十次，甚至成百上千次失败而取得的......因此不要一碰到困难就苦恼、动摇起来。

>> ————《华罗庚传》


块引用-带有其他元素
======
块引用可以包含其他Markdown格式的元素。并非所有元素都可以使用，你需要进行实验以查看哪些元素有效。  
```
> #### 科研人具有哪些特征？
> 
> - 自制力强：以学术为生
> - 抗压力强：被虐千百遍，依旧视其如初恋
> - 能动性强：不做伸手党，持续更新学术之外的技术
> **总结**：智力在线-死不要脸-一根筋-不休息
```
渲染效果如下：  
> #### 科研人具有哪些特征？
> 
> - 自制力强：以学术为生
> - 抗压力强：被虐千百遍，依旧视其如初恋
> - 能动性强：不做伸手党，持续更新学术之外的技术
> **总结**：智力在线-死不要脸-一根筋-不休息

