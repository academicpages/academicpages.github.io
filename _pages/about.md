---
permalink: /
title: "Who am I"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
  .column {
    float: left;
    width: 50%;
  }
  
  .full-width {
    text-align: justify;
  }
</style>

<div class="full-width">
Greetings!! I'm a research scientist at CEA—French Atomic Energy and Alternative Energies Commission. My expertise includes high performance computing, finite element method, Boltzmann transport, and meshing. I hold a PhD in computational physics, a master's in computational fluid dynamics, and a bachelor's in aerospace engineering. In a nutshell, I'm the wizard of numbers and equations, blending science and technology to unlock the secrets of the universe.
</div>



## Areas of Research

<div class="column">

- Finite Element Methods  <br>
- Parallel computing <br>
- Meshing
</div>

<div class="column">

- Mesh Adaption  <br>
- Radiative transport  <br>
- Computational Fluid Dynamics
</div>



&nbsp;  <!-- Blank line with non-breaking space -->
&nbsp;  <!-- Another blank line with non-breaking space -->

## Codes that I am developing

- [SALOME](https://www.salome-platform.org/) - Pre/post-processing scientific computing tool for CAD, meshing, visualization 
- [ArcaneFEM](https://github.com/arcaneframework/arcanefem) - Parallel FEM solver based on CPU-GPU parallelism
- [PSD](https://github.com/mohd-afeef-badri/psd) - Massively parallel  Solid/Structural/Seismic Dynamics FEM solver
- [top-ii-vol](https://github.com/mohd-afeef-badri/top-ii-vol) - Massively parallel geophysics mesher-partitioner  tool 
- [PDMT](https://github.com/mohd-afeef-badri/pdmt)  -  Parallel Dual Meshing Tool, is a polyhedral meshing/remsehing too
- [medio](https://github.com/mohd-afeef-badri/medio)  -   library that facilitates input and output of mesh files for FreeFEM in the `med` format

Current areas of research 
======


<style>
  .container {
    display: flex;
    flex-wrap: wrap;
  }

  .column {
    width: 50%;
  }

  .text-column {
    padding: 0 20px;  /* Add some padding for better spacing */
  }

  img {
    max-width: 100%;
    height: auto;
    display: block;  /* Remove default image spacing */
    margin: 0 auto;  /* Center the image */
  }

  @media (max-width: 600px) {
    .container {
      flex-direction: column;
    }

    .column {
      width: 100%;
    }
  }
</style>

## Polyhedral Meshing
<div class="container">
  <div class="column">
    <img src="https://github.com/mohd-afeef-badri/pdmt/assets/52162083/bc7f98a6-7631-439d-934f-7daa49250721" alt="Image 1">
  </div>
  <div class="column text-column">
    Polyhedral meshing is gaining importance in modern computational simulations. It offers advantages in terms of accuracy, adaptability to complex geometries, efficiency in parallel computing, and improved convergence of numerical solvers. These benefits make polyhedral meshing a valuable tool in various scientific and engineering applications.
  </div>
</div>

<details>
  <summary style="cursor: pointer; font-weight: bold;">Load more</summary>

  <div class="container">
    <div class="column">
      <img src="https://github.com/mohd-afeef-badri/pdmt/assets/52162083/8ae5798d-5a4f-474d-ae39-c7207085f7bd" alt="Image 1">
    </div>
    <div class="column text-column">
      Text description for Image 1
    </div>
  </div>

  <div class="container">
    <div class="column">
      <img src="https://github.com/mohd-afeef-badri/pdmt/assets/52162083/03f0e8ae-75dd-4823-870b-4c65fab363fe" alt="Image 2">
    </div>
    <div class="column text-column">
      Text description for Image 2
    </div>
  </div>

  <div class="container">
    <div class="column">
      <img src="https://github.com/mohd-afeef-badri/pdmt/assets/52162083/9052499a-3993-425e-a111-2f94c4ca8798" alt="Image 3">
    </div>
    <div class="column text-column">
      Text description for Image 3
    </div>
  </div>

</details>










<style>
  .container {
    display: flex;
  }
  .column {
    flex: 1;
  }
  .text-column {
    text-align: justify;
  }
</style>

## Mesh Adaption
<div class="container">
  <div class="column text-column">
    Mesh adaptation is crucial in computational simulations as it enables the dynamic adjustment of the mesh based on evolving solution characteristics. By refining or coarsening the mesh in specific regions, mesh adaptation improves accuracy in critical areas, reducing computational costs by avoiding unnecessary refinement elsewhere. This is particularly important for capturing complex geometries, handling singularities, and optimizing element types, ensuring efficient and reliable simulations. Mesh adaptation in a nutshell helps in making simulations more  robust in dynamic environments.
  </div>
  <div class="column">
    <img src="/images/c8d84a25f315d4ff94a409a6ce96ddf80a568f01.png" alt="Image 2" width="80%">
  </div>
</div>

<details>
  <summary style="cursor: pointer; font-weight: bold;">Load more</summary>
  <img src="https://github.com/mohd-afeef-badri/pdmt/assets/52162083/8ae5798d-5a4f-474d-ae39-c7207085f7bd" alt="Image 1" width="25%">
</details>



<style>
  .container {
    display: flex;
  }
  .column {
    flex: 1;
  }
  .text-column {
    text-align: justify;
  }
</style>

## Finite Element Solver (CPU/GPU)
<div class="container">
  <div class="column">
    <img src="https://user-images.githubusercontent.com/52162083/237443631-959988a3-1717-4449-b412-14cbd1582367.png" alt="Image 2" width="100%">
  </div>
  <div class="column text-column">
    A parallel FEM solver is indispensable in many computational simulations as it leverages the power of parallel processing to tackle complex and large problems more efficiently. By dividing the computational workload among multiple processors (CPU/GPU/Threads), parallel FEM solvers dramatically reduce simulation time for large-scale models. This is particularly crucial in fields such as structural mechanics, fluid dynamics, and electromagnetics, where simulations involve intricate geometries and intricate physical interactions.
  </div>
</div>

<details>
  <summary style="cursor: pointer; font-weight: bold;">Load more</summary>
  <img src="https://user-images.githubusercontent.com/52162083/251469445-9237d686-2791-4852-b929-4d0c7e5f8df7.gif" alt="Image 1" width="40%">
</details>

 
HPC for Fracture 
------

![Editing a markdown file for a talk](https://www.researchgate.net/profile/Giuseppe-Rastiello/publication/344688580/figure/fig6/AS:947232815730690@1602849310156/Large-scale-perforated-medium-test-domain-and-partitioned-mesh_W640.jpg){: width="40%"}

FEM-Compliant parallel meshing-partitioning in Geophysics 
------

Past areas of research
======


Radiative transport in porous media
------

![Editing a markdown file for a talk](/images/al-full-img.png){: width="20%"}![Editing a markdown file for a talk](https://www.researchgate.net/publication/344284816/figure/fig3/AS:937040451489792@1600419261029/Heat-paths-of-conduction-compared-with-coupled-conduction-radiation_W640.jpg){: width="45%"}


<details>
  <summary style="cursor: pointer; font-weight: bold;">Load more</summary>

  <img src="https://www.researchgate.net/publication/344284816/figure/fig1/AS:937040006893569@1600419155709/Coupled-conduction-radiation-in-Kelvin-and-cubic-cell_W640.jpg" alt="Image 1" width="60%">
  <img src="https://www.researchgate.net/publication/344284816/figure/fig2/AS:937040245964802@1600419212628/Temperature-fields-for-coupled-condition-radiation-ceramic-samples_W640.jpg" alt="Image 2" width="60%">
  <img src="https://www.researchgate.net/publication/344284816/figure/fig5/AS:937041797861379@1600419582366/Temperature-comparison-for-SiC-ceramics-with-different-cell-structure_W640.jpg" alt="Image 3" width="60%">

</details>




Inverse problem for hypersonic flow
------

