---
title: 'VS2019 Qt开发环境搭建'
date: 2023-02-01
permalink: /posts/2023/02/blog-post-1-name/
tags:
  - VS
  - Qt
  - 软件开发环境
---

大概是这么个搭配:

vs2015匹配的大概是 Qt5.7 、5.9、5.6这些

vs2017匹配的大概是 Qt5.9~~~Qt5.14

vs2019/vs2022匹配的大概是 Qt5.14~~~Qt6

一. 安装VS2019
======
VS2019 C++主要安装模块：

> 不用C#, python的，可以只勾选C++模块  
![png](/images/posts/vs2019c++.png)


二. 安装Qt
======
可以选择5.14，低于该版本的可能没有VS2019对应的Qt.
![png](/images/posts/qt5-14.png)

    注意：安装Qt前最好断网(5.14之前的版本断网安装可以，5.15之后必须在线安装了)
![png](/images/posts/qt5-14mscv.png)


三. 安装vsaddin 
------
Qt安装结束后，再安装Qt VS插件，找到vsaddin
![png](/images/posts/vsaddin.png)


四. 设置Qt路径创建Qt项目
------
打开VS，由于VS2019相对于之前的版本启动界面做了一些改动，先任意新建一个C++项目，设置Qt路径，不设置Qt路径的界面可能会这样
![png](/images/posts/QTVersion.png)  
Qt路径设置如下图：
![png](/images/posts/QTVersion1.png)  
![png](/images/posts/QTVersion2.png)  


五. 创建VS2019 QT GUI项目  
------
Qt路径设置后，再新建Qt程序，如下图，可以选择GUI程序和控制台程序，例如我创建的是GUI项目
![png](/images/posts/VS2019QT.png)  
![png](/images/posts/VS2019QT2.png)  


六. 用VS Qt 开发的项目结果
------
![png](/images/posts/VS2019QT3.png)  


> vs2019 qt打开ui文件闪退的解决办法：[vs2019 qt打开ui文件闪退的解决办法_令狐掌门的博客-CSDN博客](https://mingshiqiang.blog.csdn.net/article/details/123615642)