---
permalink: /
title: "Who am I"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Greetings!! I'm a research scientist at CEA—French Atomic Energy and Alternative Energies Commission. My expertise includes high performance computing, finite element method, Boltzmann transport, and meshing. I hold a PhD in computational physics, a master's in computational fluid dynamics, and a bachelor's in aerospace engineering. In a nutshell, I'm the wizard of numbers and equations, blending science and technology to unlock the secrets of the universe. 

Areas of Research
======
- Parallel computing
- Finite Element Methods
- Meshing 
- Mesh Adaption
- Radiative transport
- Computational Fluid Dynamics

List of software's/libraries that I am developing
======
- [SALOME](https://www.salome-platform.org/) - Pre/post-processing scientific computing tool for CAD, meshing, visualization 
- [ArcaneFEM](https://github.com/arcaneframework/arcanefem) - Parallel FEM solver based on CPU-GPU parallelism
- [PSD](https://github.com/mohd-afeef-badri/psd) - Massively parallel  Solid/Structural/Seismic Dynamics FEM solver
- [top-ii-vol](https://github.com/mohd-afeef-badri/top-ii-vol) - Massively parallel geophysics mesher-partitioner  tool 
- [PDMT](https://github.com/mohd-afeef-badri/pdmt)  -  Parallel Dual Meshing Tool, is a polyhedral meshing/remsehing too
- [medio](https://github.com/mohd-afeef-badri/medio)  -   library that facilitates input and output of mesh files for FreeFEM in the `med` format

Current areas of research 
======

Polyhedral Meshing
------
![Editing a markdown file for a talk](https://private-user-images.githubusercontent.com/52162083/254928008-50d292d9-9fff-4e63-85f2-e310e01e5c16.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDA0MzUyOTYsIm5iZiI6MTcwMDQzNDk5NiwicGF0aCI6Ii81MjE2MjA4My8yNTQ5MjgwMDgtNTBkMjkyZDktOWZmZi00ZTYzLTg1ZjItZTMxMGUwMWU1YzE2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE5VDIzMDMxNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ3YWI3Y2RlNTU4ZWQyMjNmODkyMWY4MWU0NTk0NjhkNDg5ZWE5NmQxYzY3YWVhZjRkOGZiOTNkZTU0M2Y3ZTUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.cAhxay6_Izh3PgU0HmTJS9iwSva9hsrFSUQA7EfYW6I){: width="40%"}

![Editing a markdown file for a talk](https://private-user-images.githubusercontent.com/52162083/254594617-ad36705c-47d2-4326-9987-4eccc40fb818.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDA0MzUyOTYsIm5iZiI6MTcwMDQzNDk5NiwicGF0aCI6Ii81MjE2MjA4My8yNTQ1OTQ2MTctYWQzNjcwNWMtNDdkMi00MzI2LTk5ODctNGVjY2M0MGZiODE4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE5VDIzMDMxNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTQyYzg2ZTNlNTk5ZDc0YWZiMzNiOWNkMzVhMGUzZDRlMWJjOTc5MDYyZWRmMTg3YzExNjBiNzFmMWUzYjFiOTEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.UJg4EUZpIr0ufrCeUkzXSDtRm6C8eYOLB7Yt4LmhWFs){: width="20%"}
![Editing a markdown file for a talk](https://private-user-images.githubusercontent.com/52162083/254596238-58aeb5e8-c49b-4527-add9-c2afd738877d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDA0MzUyOTYsIm5iZiI6MTcwMDQzNDk5NiwicGF0aCI6Ii81MjE2MjA4My8yNTQ1OTYyMzgtNThhZWI1ZTgtYzQ5Yi00NTI3LWFkZDktYzJhZmQ3Mzg4NzdkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE5VDIzMDMxNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ2Njc0OWVmYzEzZTQxMTRmZWYxNDM4ZjY1ZDI4N2ZkMDlmZGU4ZmNhYmIxMzIzYWNjOWIzMDQyNGU4MzJiOWQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.Zn05eXZpFBXGpd7xSlD1xt2aixF2_spSYXfvJ2ER1_w){: width="20%"}
![Editing a markdown file for a talk](https://private-user-images.githubusercontent.com/52162083/254599588-d8cb4c44-4cd5-4aef-a788-b5ded2fb26f1.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDA0MzUyOTYsIm5iZiI6MTcwMDQzNDk5NiwicGF0aCI6Ii81MjE2MjA4My8yNTQ1OTk1ODgtZDhjYjRjNDQtNGNkNS00YWVmLWE3ODgtYjVkZWQyZmIyNmYxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE5VDIzMDMxNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdkZmNiZWI1NDE5Njg5MzllYzI0ZjllYjc0YzdlY2M4NTJjZmVkNzY1YTQxNmZjZDJjNzY4YjBmZjBiZTNkZTMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.jUn5cTQTEgC_uvNj9QbWPbV3ogaw_7hdlvQ_nnAYFOI){: width="20%"}

Mesh Adaption
------ 

Finite Element Solver (CPU/GPU)
------

![Editing a markdown file for a talk](https://user-images.githubusercontent.com/52162083/237443631-959988a3-1717-4449-b412-14cbd1582367.png){: width="40%"}![Editing a markdown file for a talk](https://user-images.githubusercontent.com/52162083/251469445-9237d686-2791-4852-b929-4d0c7e5f8df7.gif){: width="32%"}
 


Past areas of research
======


Radiative trasport in porous media
------

![Editing a markdown file for a talk](/images/al-full-img.png){: width="20%"}![Editing a markdown file for a talk](https://www.researchgate.net/publication/344284816/figure/fig3/AS:937040451489792@1600419261029/Heat-paths-of-conduction-compared-with-coupled-conduction-radiation_W640.jpg){: width="45%"}

![Editing a markdown file for a talk](https://www.researchgate.net/publication/344284816/figure/fig1/AS:937040006893569@1600419155709/Coupled-conduction-radiation-in-Kelvin-and-cubic-cell_W640.jpg){: width="60%"}



Number 2
------

