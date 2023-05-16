---
layout: archive
title: "Software"
permalink: /software/
author_profile: false
---

{% include base_path %}

# ODE Test Problems

ODE Test Problems (OTP) is an object-oriented MATLAB/GNU Octave package offering
a broad range of ordinary differential equations, partial differential
equations, and differential algebraic equations which can be used to test
numerical methods such as time-steppers and data assimilation methods. It
contains problems that are linear and nonlinear, autonomous and nonautonomous,
scalar and high-dimensional, and stiff and nonstiff. OTP also supports
partitioned systems for testing IMEX methods, multirate methods, and other
partitioned schemes. Many problems come from real-world applications in fields
such as chemistry, astrophysics, meteorology, and electrical engineering. OTP's
interface provides a simple and standardized way to access problem parameters,
the right-hand side function, the Jacobian matrix, and other properties. Each
problem is equipped with functions for computing the solution, plotting the
solution, and creating a movie.


## Installation

OTP can be installed as a local MATLAB toolbox or Octave package by running

```matlab
OTP.install
```

from the root directory of the project. If no longer needed, it can be
uninstalled with `OTP.uninstall`.

## Example

```matlab
% Create a problem
problem = otp.lotkavolterra.presets.Canonical;

% Solve the problem
sol = problem.solve('RelTol', 1e-10);

% Plot the solution
problem.plot(sol);

% Adjust a parameter
problem.Parameters.PreyDeathRate = 2;

% Manually use a MATLAB ODE solver to solve the problem
options = odeset('Jacobian', problem.RHS.Jacobian);
[t, y] = ode15s(problem.RHS.F, problem.TimeSpan, problem.Y0, options);

% Plot the phase space with a custom title
problem.plotPhaseSpace(t, y, 'Title', 'The Circle of Life');

% Create a movie and write to file
mov = problem.movie(t, y, 'Save', 'lotka-volterra.avi');
```

