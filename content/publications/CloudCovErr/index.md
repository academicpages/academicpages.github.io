+++

template = "post.html"
title = "Photometry on Structured Backgrounds: Local Pixel-wise Infilling by Regression"
date = 2022-07-01

[extra]
abstract = "Photometric pipelines struggle to estimate both the flux and flux uncertainty for stars in the presence of structured backgrounds such as filaments or clouds. However, it is exactly stars in these complex regions that are critical to understanding star formation and the structure of the interstellar medium. We develop a method, similar to Gaussian process regression, which we term local pixel-wise infilling (LPI). Using a local covariance estimate, we predict the background behind each star and the uncertainty of that prediction in order to improve estimates of flux and flux uncertainty. We show the validity of our model on synthetic data and real dust fields. We further demonstrate that the method is stable even in the crowded field limit. While we focus on optical-IR photometry, this method is not restricted to those wavelengths. We apply this technique to the 34 billion detections in the second data release of the Dark Energy Camera Plane Survey. In addition to removing many >3σ outliers and improving uncertainty estimates by a factor of ~2-3 on nebulous fields, we also show that our method is well behaved on uncrowded fields. The entirely post-processing nature of our implementation of LPI photometry allows it to easily improve the flux and flux uncertainty estimates of past as well as future surveys."

authors = ["Andrew K Saydjari, Douglas P Finkbeiner"]

links = [
    { name = "ADS", link = "https://ui.adsabs.harvard.edu/abs/2022ApJ...933..155S/abstract" },
    { name = "Zenodo", link = "https://doi.org/10.5281/zenodo.5809521" },
    { name = "Code", link = "https://github.com/andrew-saydjari/CloudCovErr.jl" },
]

publication = "ApJ"
year = 2022

image = { path = "CloudCovErr.gif", style="banner", caption = "HII region CED116 near the Running Chicken nebula. A beautiful and complex field that is a tiny fraction of the survey." }

+++

