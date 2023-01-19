---
title: "Mitigating stray grains in laser-melting of CMSX-4 single crystal superalloy"
excerpt: "High weld speeds and low powers minimize the amount of stray grains and maximize the epitaxial single crystal growth in traditional laser welding process. We extends the analytical solidification modeling applied in welding to laser melting with conditions representative of laser powder bed fusion (LPBF) additive manufacturing (AM) process. LPBF features higher laser powers and lower scanning speeds compared with welding which shows a potential to further decrease the amount of stray grains and therefore print single crystal components. <br/><img src='/images/cmsx4_ebsd.png'>"
permalink: /research/cmsx4/
date: 2022-12-23
collection: research
---

<div style="text-align: justify">
High weld speeds and low powers minimize the amount of stray grains and maximize the epitaxial single crystal growth in traditional laser welding process. We extends the analytical solidification modeling applied in welding to laser melting with conditions representative of laser powder bed fusion (LPBF) additive manufacturing (AM) process. LPBF features higher laser powers and lower scanning speeds compared with welding which shows a potential to further decrease the amount of stray grains and therefore print single crystal components. 
</div>
<br/>

<figure>
    <img src='/images/new_cmsx4_ebsd.png' class="center"> 
    <figcaption> Crystal orientations in solidified melt pools processed by various laser power and velocity conditions. </figcaption>
</figure>

<div style="text-align: justify"> 
We used Rosenthal-based analytical solidification model and numerical high-fidelity CFD thermal models to predict solidification conditions and stray grain propensity, and verified the simualtion results with single-bead experimental data. The trend and magnitude was consistent in both simulations and experimental data. The keyhole shaped melt pools-especially the two with power 300~W have a significantly larger amount of stray grains than the analytically simulation prediction. This discrepancy is actually expected as the Rosenthal equation usually fails to properly reflect the heat flow in the keyhole regime due to its assumption that heat transfer is governed purely by conduction. Although the CFD model slightly over predicts $\overline{\Phi}$ in all $P-V$ conditions, its prediction under keyhole condition is more accurate than the analytical model. For conduction mode melt pools, the experimental values align more closely with the analytical simulated values.
</div>
<br/>


<div style="text-align: justify">
To understand the microstructure development in AM under highly non-equilibrium cooling conditions, we present microstructure selection maps for CMSX-4 alloy to predict the columnar v.s. epitaxial solification.
</div>
<br/>

<figure>
    <img src='/images/cmsx4-selection-map.png' class="center"> 
    <figcaption> Microstructure selection map for the superalloy CMSX-4 using laser powers 200~W calculated from (a) analytical Rosenthal model and (b) numerical CFD model. The three colored curves trace changes in the local thermal conditions at the solid-liquid interface on the $xy$ horizontal cross section under three different processing parameters. </figcaption>
</figure>

<div style="text-align: justify">
Our current results provide a general guideline for optimal laser parameters to achieve minimal stray grains and maintain single crystal structure. These guidelines provide a suitable process window for minimal stray grains, around power 250 W and scanning velocity ~600 - 800 mm/s). Careful selection of each processing parameter has demonstrated success in printing nearly single crystalline microstructure for stainless steel in the past, which shows promise for CMSX-4 AM builds.
</div>
<br/>


Reference: R Jiang, Z Ren, J Aroh, A Mostafaei, B Gould, T Sun, AD Rollett, 2022, [Quantifying Equiaxed vs Epitaxial Solidification in Laser Melting of CMSX-4 Single Crystal Superalloy](https://link.springer.com/article/10.1007/s11661-022-06929-2), *Metallurgical and Materials Transactions A*.
