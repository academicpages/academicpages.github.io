---
title: "<img src='/images/sootfoil.png' style='width: 60%; display: block; margin: 0 auto;'><center>Detonation at elevated pressure</center>"
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
<!-- <img src="https://wengzf20.github.io/images/Cantera.png" style="height: 2em;vertical-align: middle;"> -->

<br>
<div style="text-align: justify;">
The research on detonation can be seperated into several regimes using the pressure and density diagram of Schmitt and Bulter $^{[1]}$. Gas phase detonation focus mainly on low pressure regime with perfect gas assumption while solid explosive or energetic materials lie on high pressure regime. Recently, the research on two-phase RDE partly falls in the regime of liquid phase detonation. However, the regime of gas with elevated pressure seems rarely explored in detonation research. It has been proved that the perfect gas based model fails to capture the detonation speed and cellular structure regularity at elevated pressure $^{[1-2]}$. 
</div>

<center>
  <figure>
    <img src="images/detonationregime.png" style="width: 60%; object-fit: contain;">
    <figcaption style="color: gray; font-size: smaller; text-align: center;">Pressure and density diagram for different detonation research regime $^{[1]}$.</figcaption>
  </figure>
</center>

## 1. Detonation initiation
<div style="text-align: justify;">
A critical decay rate model was derived to study the direct detonation initiation at elevated initial pressure. Compared to the perfect gas based model of Eckett et al. $^{[3]}$, the finite molecular volume results in easier initiation while the inter-molecular interaction results in more difficult initiation.
<center>
  <figure>
    <img src="images/RGeffect_Planar.pdf" style="width: 60%; object-fit: contain;">
    <figcaption style="color: gray; font-size: smaller; text-align: center;">Comparison of the real gas effects on the critical decay time calculated with the quasi-unsteady model (symbol) and asymptotic solutions (line).</figcaption>
  </figure>
</center>

</div>
<a href="javascript:toggleBibtex('RGDDI')" class="textlink"> relevant papers </a>
<div id="RGDDI" class="bibtex">
<pre>
[1] Z. Weng, R. Mével, and C.K. Law, “On the critical initiation of planar detonation in Noble-Abel and van der Waals gas,” Combustion and Flame 255, 112890 (2023).
[2] Z. Weng, R. Mével, Z. Huang, F. Cai, and J. Xu, “Direct detonation initiation: A comparison between the critical curvature and critical decay rate models,” Physics of Fluids 33(9), 096110 (2021).
</pre>
</div>

## 2. Detonation structure
<div style="text-align: justify;">
The detonation speed, reaction zone structure and cellular structure were studied for both perfect gas and real gas models.
</div>

## 3. Detonation stability
<div style="text-align: justify;">
Linear and non-linear stability analysis was performed for 1D detonation for Noble-Abel gas. The finite molecular volume effect stabilizes detonation except for newtonian and weak heat release regimes. Linear stability solutions agree well with numerical simulations.
</div>


## Reference
</div>
<a href="javascript:toggleBibtex('RGDet')" class="textlink">[References]</a>
<div id="RGDet" class="bibtex noshow">
<pre>
1 R.G. Schmitt, and P.B. Butler, “Detonation Properties of Gases at Elevated Initial Pressures,” Combustion Science and Technology 106(1–3), 167–191 (1995).
2 S. Taileb, J. Melguizo-Gavilanes, and A. Chinnayya, “Influence of the equation of state on the cellular structure of gaseous detonationsat elevated pressures.pdf,” (2020).
3 C.A. Eckett, J.J. Quirk, and J.E. Shepherd, “The role of unsteadiness in direct initiation of gaseous detonations,” Journal of Fluid Mechanics 421, 147–183 (2000).
</pre>
</div>