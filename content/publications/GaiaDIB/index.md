+++

template = "post.html"
title = "Measuring the 8621 Å Diffuse Interstellar Band in Gaia DR3 RVS Spectra: Obtaining a Clean Catalog by Marginalizing over Stellar Types"
date = 2023-08-01

[extra]
abstract = "Diffuse interstellar bands (DIBs) are broad absorption features associated with interstellar dust and can serve as chemical and kinematic tracers. Conventional measurements of DIBs in stellar spectra are complicated by residuals between observations and best-fit stellar models. To overcome this, we simultaneously model the spectrum as a combination of stellar, dust, and residual components, with full posteriors on the joint distribution of the components. This decomposition is obtained by modeling each component as a draw from a high-dimensional Gaussian distribution in the data-space (the observed spectrum) -- a method we call Marginalized Analytic Data-space Gaussian Inference for Component Separation (MADGICS). We use a data-driven prior for the stellar component, which avoids missing stellar features not well-modeled by synthetic spectra. This technique provides statistically rigorous uncertainties and detection thresholds, which are required to work in the low signal-to-noise regime that is commonplace for dusty lines of sight. We reprocess all public Gaia DR3 RVS spectra and present an improved 8621 Å DIB catalog, free of detectable stellar line contamination. We constrain the rest-frame wavelength to  8623.14±0.087 Å (vacuum), find no significant evidence for DIBs in the Local Bubble from the 1/6th of RVS spectra that are public, and show unprecedented correlation with kinematic substructure in Galactic CO maps. We validate the catalog, its reported uncertainties, and biases using synthetic injection tests. We believe MADGICS provides a viable path forward for large-scale spectral line measurements in the presence of complex spectral contamination.."
authors = ["Andrew K Saydjari, Catherine Zucker, JEG Peek, Douglas P Finkbeiner"]
publication = "ApJ"
year = 2023

links = [
    { name = "ADS", link = "https://ui.adsabs.harvard.edu/abs/2022arXiv221203879S/abstract" },
    { name = "Website", link = "https://faun.rc.fas.harvard.edu/saydjari/GaiaDIB/" },
    { name = "Zenodo", link = "https://doi.org/10.5281/zenodo.7388333" },
]

image = { path = "header.png", style="banner", caption="What a beautiful figure" }

+++

