---
permalink: /codes/
title: "Codes"
author_profile: true
redirect_from: 
  - /md/
---
<!-- the styles -->
<style>

div.noshow { display: none; }
div.bibtex {
  margin-right: 0%;
  margin-top: 1.2em;
  margin-bottom: 1.3em;
  border: 1px solid silver;
  padding: 0.3em 0.5em;
  background: #eeeeee;
}
div.bibtex pre { font-size: 75%; overflow: auto;  width: 100%; }
</style>


<!-- the scripts -->
<script>
function toggleBibtex(articleid) {
  var bib = document.getElementById(articleid);
  if (bib) {
    if(bib.className.indexOf('bibtex') != -1) {
    bib.className.indexOf('noshow') == -1?bib.className = 'bibtex noshow':bib.className = 'bibtex';
    }
  } else {
    return;
  }
}
</script>

[📧](wengzf20@mails.tsinghua.edu.cn) **Source codes and demos are available upon reasonable request.**

> "Code is poetry." ---<cite>Automattic</cite>

## <img src="https://wengzf20.github.io/images/Cantera.png" style="height: 2em;vertical-align: middle;"> Cantera Real Gas Model
The real gas model, which is based on RK EoS, and is available since Cantera v2.0. In 2022, Cantera v2.6 was released and include the real gas model based on PR EoS $^{[1]}$. In addition, Bai et al. included in Cantera the virial EoS, which takes into account the molecular polarization of species, like $\rm H_{2}O$ $^{[2]}$. Based on the structure of the thermo and kinetics classes in Cantera, Weng and Mevel $^{[3]}$ implemented several cubic EoS, including PR, van der Waals (vdW), Noble-Abel (NA), SRK, as well as different reaction rate laws and equilibrium constants in Cantera v2.4. <br>
<a href="javascript:toggleBibtex('canteraRG')" class="textlink">[ref.]</a>
<div id="canteraRG" class="bibtex noshow">
<pre>
[1] 🔗 https://cantera.org
[2] J. Bai, P. Zhang, C.-W. Zhou, and H. Zhao, “Theoretical studies of real-fluid oxidation of hydrogen under supercritical conditions by using the virial equation of state,” Combustion and Flame, 111945 (2021).
[3] Z. Weng, and R. Mével, “Real gas effect on steady planar detonation and uncertainty quantification,” Combustion and Flame 245, 112318 (2022).
</pre></div>


## <img src="https://wengzf20.github.io/images/CFDfoundationLogoDark-600x600.png" style="height: 2em;vertical-align: middle;"> RSDFoam (Real gas shock and detonation solver in OpenFOAM)
The high pressure condition widely used in industry makes it necessary to evaluate the impact of real gas behaviour in numerical simulation, especially for shock and detonation problems. The solver considers the nonidealities in the equation of state, thermodynamic functions and mass action law brought about by the interaction between the fluid particles and by their finite volume. Connection between blastFoam and Cantera was built to utilize the CFD capabilities from the former and the efficient chemistry solver and real gas models in Cantera. The new solver has been thoroughly validated against analytical solutions, previous numerical simulation results and experimental data. For non-reactive flow, shock tube and oblique shock problems were solved. For reactive cases, constant volume reactor, steady detonation speed, reaction zone structure, and cellular structure were numerically studied. The satisfactory agreement demonstrates the accuracy and robustness of the solver
for real gas based shock and detonation simulation.
<br>
<a href="javascript:toggleBibtex('RSDFoam')" class="textlink">[ref.]</a>
<div id="RSDFoam" class="bibtex noshow">
<pre>
[1] Z. Weng, and R. Mével, “Implementation of an OpenFOAM solver for shock and detonation simulation at high pressure,” Computers & Fluid, in press (2023).
</pre></div>

## <img src="https://wengzf20.github.io/images/edl-logo.gif" style="height: 2em;vertical-align: middle;"> RSDToolbox (Real gas shock and detonation toolbox)
Some in-house codes developed based on the SDToolbox of Prof. Joseph E. Shepherd $^{[1]}$ for shock and detonation in real gas   <br>
<a href="javascript:toggleBibtex('RSDToolbox')" class="textlink">[ref.]</a>
<div id="RSDToolbox" class="bibtex noshow">
<pre>
[1] 🔗 https://shepherd.caltech.edu/EDL/PublicResources/sdt/.
</pre></div>
