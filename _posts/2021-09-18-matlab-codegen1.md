---
title: 'MATLAB Codegen for fminsearch without anonymous functions'
date: 2020-09-18
permalink: /posts/2021/09/2021-09-18-matlab-codegen1/
tags:
  - MATLAB
  - Codegen
---

Code Generation from MATLAB Code is a common way to generate performant C Code for hardware applications. 
Only certain MATLAB functions are supported for automatic code generation.  

Running fminsearch on a function with multiple input arguments
==============================================================

Luckily the optimization toolbox contains the function fminsearch which minimizes the target function `functionToMinimize` which may either be passed as an anonymous function or a function handle. 

```matlab
targetFun = @(x, constantPar1, constantPar2)();
functionToMinimize = @(x)(targetFun(x,constantPar1, constantPar2));
x0 = []; % Starting values
minimizedX = fminsearch(functionToMinimize,x0);
```

Unfortunately [Anonymous Functions] (https://de.mathworks.com/help/matlab/matlab_prog/anonymous-functions.html) have only been enabled for code generation in Update R2017b. For all updates before R2017b you need to use function handles instead of anonymous functions.

First you need to write the `functionToMinimize`. This may look something like this:

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

Then you can call fminsearch after initializing the functionToMinize.

```matlab
x0 = []; % Starting values
functionToMinimize(x0,constantPar1, constantPar2);
minimizedX = fminsearch(functionToMinimize,x0);
```

Resources
---------
* [Matlab documentation]()
* [Question on Stackoverflow] ()

