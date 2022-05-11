---
title: "Faster Than Real Time Tsunami Warning with Associated Hazard Uncertainties"
collection: publications
permalink: /publications/FTRT
excerpt: ''
date: 2021-01-14
venue: 'Frontiers in Earth Sciences'
paperurl: 'https://doi.org/10.3389/feart.2020.597865'
citation: 'Giles, D., Gopinathan, D., Guillas, S., and Dias, F.: Faster Than Real Time Tsunami Warning with Associated Hazard Uncertainties, Front. Earth Sci., 8, 226, https://doi.org/10.3389/feart.2020.597865, 2021.'
---
<!-- This paper is about the number 1. The number 2 is left for future work. -->

[Download paper here](https://doi.org/10.3389/feart.2020.597865)

## Abstract 
Tsunamis are unpredictable events and catastrophic in their potential for destruction of human lives and economy. The unpredictability of their occurrence poses a challenge to the tsunami community, as it is difficult to obtain from the tsunamigenic records estimates of recurrence rates and severity. Accurate and efficient mathematical/computational modeling is thus called upon to provide tsunami forecasts and hazard assessments. Compounding this challenge for warning centres is the physical nature of tsunamis, which can travel at extremely high speeds in the open ocean or be generated close to the shoreline. Thus, tsunami forecasts must be not only accurate but also delivered under severe time constraints. In the immediate aftermath of a tsunamigenic earthquake event, there are uncertainties in the source such as location, rupture geometry, depth, magnitude. Ideally, these uncertainties should be represented in a tsunami warning. However in practice, quantifying the uncertainties in the hazard intensity (i.e., maximum tsunami amplitude) due to the uncertainties in the source is not feasible, since it requires a large number of high resolution simulations. We approximate the functionally complex and computationally expensive high resolution tsunami simulations with a simple and cheap statistical emulator. A workflow integrating the entire chain of components from the tsunami source to quantification of hazard uncertainties is developed here - quantification of uncertainties in tsunamigenic earthquake sources, high resolution simulation of tsunami scenarios using the GPU version of Volna-OP2 on a non-uniform mesh for an ensemble of sources, construction of an emulator using the simulations as training data, and prediction of hazard intensities with associated uncertainties using the emulator. Thus, using the massively parallelized finite volume tsunami code Volna-OP2 as the heart of the workflow, we use statistical emulation to compute uncertainties in hazard intensity at locations of interest. Such an integration also balances the trade-off between computationally expensive simulations and desired accuracy of uncertainties, within given time constraints. The developed workflow is fully generic and independent of the source (1945 Makran earthquake) studied here.

Recommended citation: Giles, D., Gopinathan, D., Guillas, S., and Dias, F.: Faster Than Real Time Tsunami Warning with Associated Hazard Uncertainties, Front. Earth Sci., 8, 226, https://doi.org/10.3389/feart.2020.597865, 2021.