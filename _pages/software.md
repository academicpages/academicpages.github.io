---
layout: archive
title: "Software and data"
permalink: /software/
author_profile: true
---
## Software

### Change point detection in Python: `ruptures`

I maintain a change point detection library in Python called `ruptures` [[homepage]](https://github.com/deepcharles/ruptures) [[documentation]](https://centre-borelli.github.io/ruptures-docs/). This package provides methods for the analysis and segmentation of non-stationary signals. Implemented algorithms include exact and approximate detection for various parametric and non-parametric models. `ruptures` focuses on ease of use by providing a well-documented and consistent interface. In addition, thanks to its modular structure, different algorithms and models can be connected and extended within this package.

If you have any question or if you feel like contributing, do not hesitate to reach me through the [Github repository](https://github.com/deepcharles/ruptures).

If you use this software, please cite the following article:
- Truong, C., Oudre, L., & Vayatis, N. (2020). Selective review of offline change point detection methods. *Signal Processing*, 167. [[abstract]](https://deepcharles.github.io/publication/sp-review-2020) [[doi]](https://doi.org/10.1016/j.sigpro.2019.107299) [[pdf]](http://deepcharles.github.io/files/sp-review-2020.pdf)


## Data

### Study of human locomotion
This data set contains 1020 multivariate gait signals collected with two inertial measurement units (accelerometers and gyroscopes), from 230 subjects undergoing a fixed protocol: standing still, walking 10 m, turning around, walking back and stopping.
In particular, **the start and end timestamps of more than 40,000 footsteps are provided**, as well as a number of contextual information about each trial.
This exact data set was used in [Oudre et al., Template-based step detection with inertial measurement units, Sensors 18, 2018](https://deepcharles.github.io/publication/sensors-gait-2018) to design and evaluate a step detection procedure.

This data set is thoroughly described in the following article:
- Truong, C., Barrois-Müller, R., Moreau, T., Provost, C., Vienne-Jumeau, A., Moreau, A., Vidal, P.-P., Vayatis, N., Buffat, S., Yelnik, A., Ricard, D., & Oudre, L. (2019). A data set for the study of human locomotion with inertial measurements units. Image Processing On Line (IPOL), 9. [[abstract]](https://deepcharles.github.io/publication/ipol-data-2019) [[doi]](https://doi.org/10.5201/ipol.2019.265) [[pdf]](http://deepcharles.github.io/files/ipol-walk-data-2019.pdf) [[online demo]](http://ipolcore.ipol.im/demo/clientApp/demo.html?id=265)

To download the data set, you can either go to the [journal website](https://doi.org/10.5201/ipol.2019.265) or to the [associated Github repository](https://github.com/deepcharles/gait-data).

An [online demo](http://ipolcore.ipol.im/demo/clientApp/demo.html?id=265) is available to skim through the data set without coding or downloading anything.
