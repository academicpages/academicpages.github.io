---
title: 'MATLAB Codegen for fminsearch without anonymous functions'
date: 2020-09-18
permalink: /posts/2012/08/2021-09-18-matlab-codegen1/
tags:
  - MATLAB
  - Codegen
---

Code Generation from MATLAB Code is a common way to generate performant C Code for hardware applications. 
Only certain functions are supported for automatic code generation.  

Why is this even a problem? 
===========================

Luckily the optimization toolbox contains the function fminsearch which minimizes the target function fun which may either be passed as an argument as an anonymous function or a function handle. 

Before

```matlab
targetFun = @(x, constantPar1, constantPar2)();
functionToMinimize = @(x)(targetFun(x,constantPar1, constantPar2));
x0 = []; % Starting values
minimizedX = fminsearch(functionToMinimize,x0);
```

```matlab
function out = functionToMinimize(x, constantPar1, constantPar2)
  persistent ConstantPar1, ConstantPar2
  if nargin > 1
    ConstantPar1 = constantPar1
    ConstantPar2 = constantPar2
  end
  out = %Calculation of the output 
end
```




Resources
---------


