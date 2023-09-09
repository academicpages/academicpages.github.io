---
title: "FIO-AOW"
excerpt: "The full name of FIO-AOW is Atmosphere-Ocean-Wave coupled model which is developed by the First Institute of Oceanography, Ministry of Natural Resources. It consists of atmoshpher component (WRF)，ocean surface wave component (MASNUM) and ocean circulation component (POM&ROMS). All the components are coupled together through C-Coupler. It should be noted that all the components are open source except MASNUM, WRF is avaible at https://github.com/wrf-model/WRF, ROMS is avaible at https://github.com/kshedstrom/roms, C-Coupler could be downloaded at https://github.com/C-Coupler-Group/c-coupler-lib, and POM could be found at its' homepage http://www.ccpo.odu.edu/POMWEB/. In FIO-AOW, the POM and MASNUM were speeded up through MPI technique by Wang et al. (2010).<br/><img src='/images/fio-aow.png'>"
collection: portfolio
---

FIO-AOW has been used to study the impacts of ocean surface waves on tropical cyclone. Currently, the following wave related physical processes have been considered in FIO-AOW, including，
1. Thermal effect of sea spray on air-sea heat and moisture fluxes
2. Sea state dependent air-sea momentum flux
3. Non-breaking wave-induced vertical mixing
4. Relative wind speed
5. Rain-induced surface cooling

For more details about FIO-AOW, people could refer to the papers below

1. Zhao, B., Wang, G., Zhang, J. A., Liu, L., Liu, J., Xu, J., et al. (2022). The effects of ocean surface waves on tropical cyclone intensity: Numerical simulations using a regional atmosphere-ocean-wave coupled model. Journal of Geophysical Research: Oceans, 127, e2022JC019015. https://doi.org/10.1029/2022JC019015

2. Zhao, B., Qiao, F., Cavaleri, L., Wang, G., Bertotti, L., and Liu, L. (2017), Sensitivity of typhoon modeling to surface waves and rainfall, J. Geophys. Res. Oceans, 122, 1702–1723, doi:10.1002/2016JC012262.

3. Wang, G., Zhao, B., Qiao, F. et al. Rapid intensification of Super Typhoon Haiyan: the important role of a warm-core ocean eddy. Ocean Dynamics 68, 1649–1661 (2018). https://doi.org/10.1007/s10236-018-1217-x

3. Sun, C., Liu, L., Li, R., Yu, X., Yu, H., Zhao, B., Wang, G., Liu, J., Qiao, F., and Wang, B., 2021. Developing a common, flexible and efficient framework for weakly coupled ensemble data assimilation based on C-Coupler2.0, Geosci. Model Dev., 14, 2635-2657, https://doi.org/10.5194/gmd-14-2635-2021.

4. Wang, G., Qiao, F. & Xia, C. Parallelization of a coupled wave-circulation model and its application. Ocean Dynamics 60, 331–339 (2010). https://doi.org/10.1007/s10236-010-0274-6
