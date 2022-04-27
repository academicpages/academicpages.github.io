---
title: "Master's Project: MPM Snow simulation in Unity"
excerpt: "Interactive Snow Simulation using the Unity Game Engine <br/><img src='/images/snowball.gif'>"
collection: portfolio
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/Eonjyxn0tlA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


# Abstract

The MPM method is a hybrid grid and particle technique that can be used to simulate a variety of materials, such as snow, rubber, chocolate, and more. This method combines the advantages of grid based and particle based methods, though it comes at a cost of efficiency and runtime. The method can be changed to simulate different materials by changing the constituent equations that govern the particle and grid interactions. The goal for this project was to get familiar with the method and implement it, following Stomakhin et al, 2013 [\[1\]](https://dl.acm.org/doi/pdf/10.1145/2461912.2461948). 


# Basic MPM Overview

To simulate the material, MPM utilizes a base grid with a mass of particles. The algorithm is as follows:

1. Particle to Grid Transfer
    - Clear the grid from the previous iteration
    - Gather particle quantities (mass, velocity, etc) from nearby particles
    - Interpolate based on distance
2. Compute Grid Solution
    - Depends on the consituent equations of the material
    - Also considers other external forces (gravity and collisions)
3. Grid to Particle Transfer
    - Gather quantities from nearby grid nodes and scatter them back to the particles
    - Interpolate based on distance
4. Update Particle States and Quantities
    - Move the particles to their next timestep positions
    - Update particle states (such as deformation)

# Implementation Details

The simulation was implemented in C# with the Unity Engine. We utilized shaders [\[3\]](https://nialltl.neocities.org/articles/mpm_guide.html) to visualize the actual snow particles and Unity's OpenGL functions for collision object and grid visuals. The algorithm also allows for natural parallelization, so we utilize Unity's job system to multithread the code. The simulation is able to run in real time for a small number of particles, but will slow down significantly when there are many particles. This is mostly due to the expensive math that needs to be compute for every single particle.

# Simulation Parameters

Young's Modulus, controls stiffness of the material.

Hardening Constant, controls plastic hardening.

Critical Compression, controls when plastic deformation occurs.

Critical Stretch, controls when plastic deformation occurs.

Critical Compression and Stretch control when the material fractures, larger numbers mean the snow will end up being more chunky, while smaller numbers will have more powdery snow. The Hardening constant and the Youngs Modulus controls whether the snow is more brittle with higher values or more ductile with lower values [\[1\]](https://dl.acm.org/doi/pdf/10.1145/2461912.2461948).

There some other tunable parameters that we have chosen to have better snow simulation. This includes fixing the grid cell size (too big would cause collisions to work improperly and too small would cause the snow to compact too much), fixing the size of each particle (volume of 25cm^2, kind of arbitrary as we could go with a smaller particle size and a smaller simulation space instead ), and a 24x19m simulation space.


<iframe width="560" height="315" src="https://www.youtube.com/embed/r4KeZ8dU9_I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


# Collision Objects

Collision objects are implemented via signed distance fields, which makes collision checking easy as there is a collision when a point has negative distance. The simulation include 4 collision objects: halfplanes, spheres, rectangles, and arbitrary polygonal colliders. The first three have exact formulas for the distance fields. Polygonal colliders require more work. We create an overlaying grid of samples over the collider and then compute the minimum distance for each sample point. Then for actual collision testing, we query the grid of samples, find the closest 4 points and use bilinear interpolation for the final distance value. To obtain the collision normals, we estimate them using finite differences.

![Example Polygonal Collider with sample grid visualization](/images/examplePolygonalCollider.png)


# Interaction

The final program allows the user to add and remove shapes of snow as well as colliders. For the snow shapes, the users are also able to add an initial velocity in any direction. There are sliders that change simulation parameters that control the material properties. There are also some toggles for visualization. We also include mouse interaction with the snow. There is a repulsive circular "force field" with an adjustable radius that the user can push the snow around with. This allows the user to push around the snow. The user is also able to pan the view of the simulation using the arrow keys.


<iframe width="560" height="315" src="https://www.youtube.com/embed/j4CjyUWuBBo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


# Limitations and Future Extensions

The simulation is in 2D, so the behavior is going to be different from how snow behaves in 3D. Moving the simulation to 3D shouldn't be very difficult, but would explode the runtime by a lot, which would be problematic for user interaction. Even with the current parallelization, we could probably do better using a more high performance language and the GPU, so potentially using C++ or CUDA could provide us with faster simulations. The colliders also can be a bit buggy at times, small amounts of particles get stuck in the colliders, especially if the colliders do not line up with the grid cells. This is more of a result of using a coarse grid, so a finer grid should prevent this from happening.


# References

[Stomakhin, Alexey](https://dl.acm.org/doi/pdf/10.1145/2461912.2461948), et al. "A material point method for snow simulation." ACM Transactions on Graphics (TOG) 32.4 (2013): 1-10.

[Jiang, Chenfanfu](https://dl.acm.org/doi/pdf/10.1145/2897826.2927348), et al. "The material point method for simulating continuum materials." ACM SIGGRAPH 2016 Courses. 2016. 1-52.

[Niall](https://nialltl.neocities.org/articles/mpm_guide.html) for the particle rendering code as well as a helpful guide for parallelization of the code.

[Max Liberman](https://github.com/wyegelwel/snow/blob/master/docs/snow_math.pdf) for helpful math breakdowns of the snow constituent equations.

[Inigo Quilez](https://iquilezles.org/articles/) for 2D signed distance field formulas and estimating distance field normals.

<iframe width="560" height="315" src="https://www.youtube.com/embed/NQkwnMcOjyo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>