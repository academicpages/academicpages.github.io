---
title: 'Light Induced Degradation (LID): A quick overview on the performance impact'
date: 2023-08-28
permalink: /posts/2023/08/lid/
tags:
  - Light Induced Degradation
  - LID
  - failure
  - photovoltaic
---

**Light Induced Degradation (LID)**, or Light soaking effect, refers to changes in module power performance due to light exposure and could potentially entail losses up to 30%. 
This article provides an overview on the impact, the loss mechanisms and how to detect LID.  

<figure>
    <img src="https://alexandrehugomathieu.github.io/alexandremathieu.github.io//images/lid_images/lid_main_pictures.png"
    width="100px">
    <figcaption> PV cell with LID degradation (Kwapil et al., 2020) </figcaption>
</figure>

Technology dependency
======

The phenomenon is different for each technology.  

This appears as a degradation of few percentages within the first exposure hours in the crystallin technologies before regenerating over several years. In this case, the **“Light Induced Degradation (LID)”** term is often used and is defined as **“a power degradation effect which occurs during the initial stabilization of a PV module when exposed to light”** from (Aghaei et al., 2022) . 
On the other hand, the amorphous silicon (a-Si) can be impacted up to 10-30 % (Gostein and Dun, 2011) within the first months of outdoor exposure due to the **“Staebler–Wronski Effect” (SWE)** discovered, as you can assume, from D.L Staebler and C.R  Wronski in 1977.  In the a-Si modules, the effect constantly switches between thermal-induced regeneration, generally in summer, and degradation, in winter, can lead to a seasonal variation in performance of 0-15 % (Herz et al., 2022). 
Some other technologies like CIS/CIGS actually benefit from this effect with a gain of 7-15% for CIS (Gostein and Dun, 2011).

<figure>
    <img src="https://alexandrehugomathieu.github.io/alexandremathieu.github.io//images/lid_images/lid_figures.PNG">
    <figcaption> LID performance loss figures from literature </figcaption>
</figure>

Degradation Mechanisms
======

The “Boron -oxygen LID” (BO-LID) is among the most common study cases to illustrate
LID mechanisms. It occurs in Boron-doped monocrystalline Silicium (m-Si) made from
Czochralski method (Woodhouse et al., 2020). The degradations result from unfortunate traces of oxygen left during the cell fabrication process and light exposure. The few percentages of power losses is usually accounted in the power tolerance from the module label and typically appears during the 5 required hours of exposure according to EN 61215 (Gostein and Dun, 2011; Herz et al., 2022).

The BO LID mechanism can be broken down into three states. Initially in the state A,
light or current encourages the formations of BO complexes which shifts the cell into
a degraded state B. This state B continuously traps electrons and holes which won’t 
participate in the expected “photovoltaic effect” and then, reduces the electrical
characteristics of the PV cell. However, after some time, the cell naturally transits
to a third, regenerated, state C thanks to the inclusion of hydrogen which cancels 
the electron-hole trap effect from state B.

<figure>
    <img src="https://alexandrehugomathieu.github.io/alexandremathieu.github.io//images/lid_images/lid_state.png">
    <figcaption> Performance as function of exposure time (Woodhouse et al., 2020) </figcaption>
</figure>

More precisely, the state B uninterruptedly switches through different atomic structures
which captures electrons and holes. As mentioned in (Du et al., 2005), 4 different 
reactions sequentially take place, and the degradation speed is linearly and 
quadratically dependant from the Boron and Oxygen concentrations respectively 
(Rabelo et al., 2021). 

<figure>
    <img src="https://alexandrehugomathieu.github.io/alexandremathieu.github.io//images/lid_images/lid_mechanisms.png">
    <figcaption> Boron-Oxygen chemical mechanisms according to Du et al. (Du et al., 2005) </figcaption>
</figure>

The Light and elevated Temperature Induced Degradation (LeTID) is a variant of LID in
the multicrystalline PV cells and occurs with active temperature over 65° C. The LeTID 
mechanisms are still not fully understood (Gostein and Dun, 2011) (RECgroup, 2019) but
it empirically spikes after hundreds of hours of illumination (Woodhouse et al., 2020).
The performance impact can be worse than LID and in specific conditions reach up to 10 % 
of power losses.


Detection and electrical Signature
======

The LID can be identified with an IV tracer (Bansal et al., 2021; Herz et al., 2022) and 
detected with electroluminescence (Herz et al., 2022) and infrared thermography 
(Herz et al., 2022).

According to (da Silva et al., 2021), the LID affects all I-V curve attributes with
the decrease of the short-circuit current (Isc), Fill Factor (FF) and open-circuit
Voltage (Voc). Naturally, the maximum power point (Pmpp) also decreases. Some
detrimental consequences might be the apparition of mismatches which trigger hot 
spots and accelerate ageing.

<figure>
    <img src="https://alexandrehugomathieu.github.io/alexandremathieu.github.io//images/lid_images/iv_tracer.png">
    <figcaption> LID IV signature (da Silva et al., 2021) </figcaption>
</figure>

References
------

Aghaei, M., Fairbrother, A., Gok, A., Ahmad, S., Kazim, S., Lobato, K., Oreski, G., Reinders, A., Schmitz, J., Theelen, M., Yilmaz, P., Kettle, J., 2022. Review of degradation and failure phenomena in photovoltaic modules. Renew. Sustain. Energy Rev. 159, 112160. https://doi.org/10.1016/j.rser.2022.112160

Bansal, N., Jaiswal, S.P., Singh, G., 2021. Comparative investigation of performance evaluation, degradation causes, impact and corrective measures for ground mount and rooftop solar PV plants – A review. Sustain. Energy Technol. Assess. 47, 101526. https://doi.org/10.1016/j.seta.2021.101526

Da Silva, M.K., Gul, M.S., Chaudhry, H., 2021. Review on the Sources of Power Loss in Monofacial and Bifacial Photovoltaic Technologies. Energies 14. https://doi.org/10.3390/en14237935

Du, M.H., Branz, H.M., Crandall, R.S., Zhang, S.B., 2005. New Mechanism for Non-Radiative Recombination at Light-Induced Boron-Oxygen Complexes in Silicon.

Gostein, M., Dun, L., 2011. Light Soaking Effects on PV Modules: Overview and Literature Review. Presented at the IEEE Photovoltaic Specialists Conference, Seattle, WA, USA. https://doi.org/10.1109/PVSC.2011.6186605

Herz, M., Friesen, G., Jahn, U., Köntges, M., Lindig, S., Moser, D., 2022. Quantification of Technical Risks in PV power Systems (No. IEA-PVPS T13-23:2021). IEA PVPS.

Kwapil, W., Schön, J., Niewelt, T., Schubert, M., 2020. Temporary Recovery of the Defect Responsible for Light- and Elevated Temperature-Induced Degradation: Insights Into the Physical Mechanisms Behind LeTID. IEEE J. Photovolt. 10, 1591–1603. https://doi.org/10.1109/JPHOTOV.2020.3025240

Rabelo, M., Park, H., Kim, Y., Cho, E.-C., Yi, J., 2021. Corrosion, LID and LeTID in Silicon PV Modules and Solution Methods to Improve Reliability. Trans. Electr. Electron. Mater. 22, 575–583. https://doi.org/10.1007/s42341-021-00359-4

RECgroup, 2019. Combatting LeTID in multi and monocrystalline solar panels: How testing has demonstrated the high resistance of REC solar panels to LeTID degradation , ensuring long term power for lasting performance.

Woodhouse, M., Repins, I., Miller, D., 2020. LID and LeTID Impacts to PV Module Performance and System Economics DRAFT Analysis.

