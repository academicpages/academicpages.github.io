---
title: "<img src='/images/rho_field.png' style='width: 60%; display: block; margin: 0 auto;'><center>Supercritical Jet</center>"
# excerpt: "Short description of portfolio item number"
collection: portfolio
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

<br>
## Pressure-based supercritical flow solver

<div style="text-align: justify;">
Injection, mixing and combustion processes in rocket engines typically take place at trans- or super-critical conditions. Liquified fuel and oxidizer were injected at cryogenic and high pressure state. Accurate descriptions of real-fluid properties are essential for numerical simulation. A pressure-based solver was developed on open-source platform, DeepFlame $^{[1]}$, by connecting OpenFOAM and Cantera. The real fluid model in Cantera, including Peng-Robinson equation of state and corresponding thermodynamic functions, transport properties, was used to replace the ideal gas assumption in OpenFOAM. The pressure equation was revised according to Jarczyk and Pfitzner's work $^{[2]}$. The performance of the solver was demonstrated using nitrogen convection and injection cases $^{[2-3]}$.
</div>

<center>
  <figure>
    <img src='/images/N2Convection2.png' style='width: 60%; object-fit: contain;'>
    <figcaption style='color: gray; font-size: smaller; text-align: center;'>Nitrogen convection case proposed by Jarczyk and Pfitzner $^{[2]}$.</figcaption>
  </figure>
</center>

<center>
  <figure>
    <img src='/images/N2Convection1.png' style='width: 60%; object-fit: contain;'>
    <figcaption style='color: gray; font-size: smaller; text-align: center;'>Periodical nitrogen convection case proposed by Ma et al. $^{[3]}$.</figcaption>
  </figure>
</center>

<center>
  <figure>
    <img src='/images/rho_field.png' style='height: 60%; object-fit: contain;'>
    <figcaption style='color: gray; font-size: smaller; text-align: center;'>LES simulation for case 4 in Mayer's experiment $^{[4]}$.</figcaption>
  </figure>
</center>


<a href="javascript:toggleBibtex('NNregression')" class="textlink">[References]</a>
<div id="NNregression" class="bibtex noshow">
<pre>
1 <img src="image/deepflame.jpg" style="height: 2em;vertical-align: middle;"> https://github.com/deepmodeling/deepflame-dev
2 M.-M. Jarczyk, and M. Pfitzner, in 50th AIAA Aerospace Sciences Meeting Including the New Horizons Forum and Aerospace Exposition (American Institute of Aeronautics and Astronautics, 2012).
3 P.C. Ma, Y. Lv, and M. Ihme, “An entropy-stable hybrid scheme for simulations of transcritical real-fluid flows,” Journal of Computational Physics 340, 330–357 (2017).
4 W. Mayer, J. Telaar, R. Branam, G. Schneider, and J. Hussong, “Raman Measurements of Cryogenic Injection at Supercritical Pressure,” Heat and Mass Transfer 39(8), 709–719 (2003).
</pre></div>
