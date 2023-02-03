---
title: '一图理解CMake工作流程'
date: 2023-01-31
permalink: /posts/2023/01/cmake-1-zkm/
tags:
  - cmake
  - vs
  - c++
---

### CMake工作流程图  

![png](/images/posts/map-cmake.png)

官方在线文档：<https://cmake.org/documentation/>


### CMake跨平台工作
![png](/images/posts/map-cmake2.png)

[CMake软件构建实战](https://youtu.be/dIs7TFBDbIw?list=PLyzWS70eCgMGAqbbeSAu4UfXZFJ532QHa)


### 最小案例

1. CMakeLists.txt  
```  
CMAKE_MINIMUM_REQUIRED(VERSION 1.18.0)
PROJECT(hellocmake)
AUX_SOURCE_DIRECTORY(. SRC_LIST)
ADD_EXECUTABLE(hellocmake ${SRC_LIST})
```


2. hellocmake.cpp  
```  
#include <iostream>
using namespace std;

int main()
{
cout<<"hellocmake!<<endl;
return 0;
}
```  