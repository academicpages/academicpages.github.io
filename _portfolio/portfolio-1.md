---
# title: "<img src='/images/sootfoil.png' style='height: 10em'><br/> Detonation at elevated pressure"
title: "<div style='display: flex; justify-content: center; text-align: center;'><figure style='width: 80%;'><img src='images/sootfoil.png' style='object-fit: contain;'><figcaption>Detonation at elevated pressure</figcaption></figure></div>"
# excerpt: "Short description of portfolio item number"
collection: portfolio
---

<!-- <div style='display: flex; justify-content: center; text-align: center;'>
<figure style='width: 80%;'>
    <img src='/Users/weng/THU/CV/wengzf20.github.io/images/sootfoil.png' style='object-fit: contain;'>
    <figcaption>Detonation at elevated pressure</figcaption>
</figure>
</div> -->

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

<figure>
  <img src='/images/detonationregime.png' style='height: 10em; object-fit: contain;'>
  <figcaption style='color: gray; font-size: smaller; text-align: center;'>Pressure and density diagram for different detonation research regime $^{[1]}$.</figcaption>
</figure>

## 1. Detonation initiation
<div style="text-align: justify;">
A critical decay rate model was derived to study the direct detonation initiation at elevated initial pressure. Compared to the perfect gas based model of Eckett et al. $^{[3]}$, the finite molecular volume results in easier initiation while the inter-molecular interaction results in more difficult initiation.
</div>

<a href="javascript:toggleBibtex('RGDDI')" class="textlink">Relevant papers:</a>
<div id="RGDDI" class="bibtex">
<pre>
1 R.G. Schmitt, and P.B. Butler, “Detonation Properties of Gases at Elevated Initial Pressures,” Combustion Science and Technology 106(1–3), 167–191 (1995).
2 S. Taileb, J. Melguizo-Gavilanes, and A. Chinnayya, “Influence of the equation of state on the cellular structure of gaseous detonationsat elevated pressures.pdf,” (2020).
3 C.A. Eckett, J.J. Quirk, and J.E. Shepherd, “The role of unsteadiness in direct initiation of gaseous detonations,” Journal of Fluid Mechanics 421, 147–183 (2000).
</pre>
</div>

## 2. Detonation structure
<div style="text-align: justify;">
text
</div>

## 3. Detonation stability
<div style="text-align: justify;">
text
</div>

<a href="javascript:toggleBibtex('NNregression')" class="textlink">[ref.]</a>
<div id="NNregression" class="bibtex noshow">
<pre>
1 R.G. Schmitt, and P.B. Butler, “Detonation Properties of Gases at Elevated Initial Pressures,” Combustion Science and Technology 106(1–3), 167–191 (1995).
2 S. Taileb, J. Melguizo-Gavilanes, and A. Chinnayya, “Influence of the equation of state on the cellular structure of gaseous detonationsat elevated pressures.pdf,” (2020).
3 C.A. Eckett, J.J. Quirk, and J.E. Shepherd, “The role of unsteadiness in direct initiation of gaseous detonations,” Journal of Fluid Mechanics 421, 147–183 (2000).
</pre></div>
