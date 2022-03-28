---
layout: archive
title: "Gallery"
permalink: /gallery/
author_profile: true
---

This is a gallery of some visualizations/plots/images from my work that I am especially proud of. 

## CED 116

This is an RGB = (zrg - band) image of an HII region in the Dark Energy Camera Plane Survey (DECaPS2) that was used as a test-bed for the development of CloudCovErr.jl, an afterburner pipeline to correct the flux and flux uncertainties for stars in the presence of structured backgrounds.

![CED 116](/images/CED116.png)

## UMAP on WISE 12 $\mu$m Dust Map

Unpublished work showing a UMAP representation of images cut from the WISE 12 $\mu$m dust map based on their wavelet scattering transform (WST) coefficients. Hovering over the scatter points visualizes the image on both sides (the UMAP representation and galactic coordinates) of the coupled plot. The html is large and can take a few seconds to load.

[WISE Link](https://faun.rc.fas.harvard.edu/saydjari/WSSA/DFLabelsSupk10.html){:target="_blank"}

## Wavelet Scattering Coefficient Explorer

While wavelet scattering coefficients are motivated in part by interpretability, it can be informative (and fun!) to visualize their variation across a smoothly varying family of images, specifically those with properties you are interested in capturing. This plot was made while developing a fast equivariant wavelet scattering coefficient package, EqWS.jl which is now available on github.

[EqWS Interactive Plot](https://faun.rc.fas.harvard.edu/saydjari/misc/interactive_curves.html){:target="_blank"}