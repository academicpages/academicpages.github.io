---
hide:
  - navigation
  - toc
---

# Code

Github profile: <https://github.com/SkafteNicki>

My github profile contains the a near exhaustive list of code that I have developed throughout my years. The following
list the most completed code projects that you may find interesting.

## libcpab

Link: <https://github.com/SkafteNicki/libcpab>

*libcpab* provide an library for working with diffiomorphic transformations in both numpy, tensorflow and pytorch. The
library is written to be user friendly, such that you do not have to know the slightest thing about diffiomorphic
transformations to actually get started with using them. The code is designed to work with both 1D data (time series),
2D data (images) and 3D data (volumetric images).

## ddtn

Link: <https://github.com/SkafteNicki/ddtn>

Code related to the experiments of our 2018 paper on *Deep Diffiomorphic Transformers Networks* (see publications).
The code is written in a combination of `c++` and `Tensorflow` and enables the user to easily use the diffiomorphic
transformer layer that we develop in their own code.

## torchplot

Link: <https://github.com/MachineLearningLifeScience/torchplot>

Have you ever encountered the problem of forgetting to call `.cpu().detach().numpy()` when you are trying to plot
something from `pytorch` in `matplotlib.pyplot`? Then `torchplot` is something for you. It is a simple plug-in
replacement for your standard `matplotlib.pyplot` replacement that makes sure to transfer, detach and convert any
`torch.tensor` before calling the actual plot function.
