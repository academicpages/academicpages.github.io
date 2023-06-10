---
title: "ODE Test Problems"
layout: single-portfolio
excerpt: "<img src='/images/research/lorenz.png' alt=''>"
collection: software
order_number: 1
header: 
  og_image: "/images/research/lorenz.png"
---

`ODE Test Problems` is an object-oriented Octave/Matlab package offering a broad range of initial value problems in the form of ordinary and differential-algebraic equations that can be used to test numerical methods such as time integration or data assimilation methods.  It includes problems that are linear and nonlinear, homogeneous and nonhomogeneous, autonomous and nonautonomous, scalar and high-dimensional, stiff and nonstiff, and chaotic and nonchaotic.  Many are real-world problems from fields such as chemistry, astrophysics, meteorology, and electrical engineering.  OTP also supports partitioned ODEs for testing split, multirate, and other multimethods.  Functions for plotting solutions and creating movies are available for all problems, and exact solutions are included when available. OTP is designed for ease of use---meaning that working with and modifying problems is simple and intuitive.

## Example

```matlab

% Initiate the problem
problem = otp.lorenz63.presets.Canonical;

% Solve the problem
sol = problem.solve();

% Plot the solution trajectory
problem.plot(sol);

% Plot the Phase-Space solution 
problem.plotPhaseSpace(sol);

% Create a movie of the solution 
problem.movie(sol);

```
<img src="/images/lorenz.gif" alt="Markdown Monster icon"   style="float: left; margin-right: 10px" width="300"/> 

## More information
Check out the [Github repository](https://github.com/ComputationalScienceLaboratory/ODE-Test-Problems) for this project for tutorials and installation guide.
<iframe src="https://ghbtns.com/github-btn.html?user=ComputationalScienceLaboratory&repo=ODE-Test-Problems&type=star&size=large&text=true" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe> 
