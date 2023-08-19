+++

template = "post.html"
title = "Equivariant Wavelets: Fast Rotation and Translation Invariant Wavelet Scattering Transforms"
date = 2021-07-01

[extra]

abstract = "Wavelet scattering networks, which are convolutional neural networks (CNNs) with fixed filters and weights, are promising tools for image analysis. Imposing symmetry on image statistics can improve human interpretability, aid in generalization, and provide dimension reduction. In this work, we introduce a fast-to-compute, translationally invariant and rotationally equivariant wavelet scattering network (EqWS) and filter bank of wavelets (triglets). We demonstrate the interpretability and quantify the invariance/equivariance of the coefficients, briefly commenting on difficulties with implementing scale equivariance. On MNIST, we show that training on a rotationally invariant reduction of the coefficients maintains rotational invariance when generalized to test data and visualize residual symmetry breaking terms. Rotation equivariance is leveraged to estimate the rotation angle of digits and reconstruct the full rotation dependence of each coefficient from a single angle. We benchmark EqWS with linear classifiers on EMNIST and CIFAR-10/100, introducing a new second-order, cross-color channel coupling for the color images. We conclude by comparing the performance of an isotropic reduction of the scattering coefficients and RWST, a previous coefficient reduction, on an isotropic classification of magnetohydrodynamic simulations with astrophysical relevance."

authors = ["Andrew K Saydjari, Douglas P Finkbeiner"]

links = [
    { name = "ADS", link = "https://ui.adsabs.harvard.edu/abs/2021arXiv210411244S/abstract" },
    { name = "Zenodo", link = "https://zenodo.org/record/4712316" },
    { name = "Code", link = "https://github.com/andrew-saydjari/EqWS.jl" },
]

publication = "TPAMI"
year = 2021

image = { path = "FinkletBank.png", style="banner", caption = "Basis of wavelets carefully constructred for equivariance of the wavelet scattering network." }
+++


