---
# title: "<img src='/images/ANN.png' style='height: 10em'><br/> AI for Science"
title: "<div style='display: flex; justify-content: center; align-items: center;'> <figcaption>AI for Science    </figcaption> <figure style='text-align: center;'> <img src='images/ANN.png' style='width: 50%; object-fit: contain;'> </figure> </div>"
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
## Neural network (NN) based regression on real fluid properties
<div style="text-align: justify;">
The update of real fluid properties takes about 50% (reactive case) $^{[1]}$ or 75% (non-reactive case) of the computation time in supercritical flow simulation. 

Fully connected (or multi-Layer perceptron) type NN was trained to predict the thermo-physical properties of pure nitrogen. The network was optimized to 69 parameters and with prediction error lower than 1% for most conditions.
</div>
<img src='/images/ANN_pred.png' style='height: 10em'><br/>

<div style="text-align: justify;">
The trained NN was coupled with an AI-empowered platform, DeepFlame, to accelerate CFD simulation. Several tests were done using nitrogen convection and supercritical nitrogen injection as examples. The NN significantly reduced the computation time by several folds.
</div>
<img src='/images/ANN_N2Convection.png' style='height: 10em'><br/>


<a href="javascript:toggleBibtex('NNregression')" class="textlink">[ref.]</a>
<div id="NNregression" class="bibtex noshow">
<pre>
1 P.C. Ma, Y. Lv, and M. Ihme, “An entropy-stable hybrid scheme for simulations of transcritical real-fluid flows,” Journal of Computational Physics 340, 330–357 (2017).
2 W. Mayer, J. Telaar, R. Branam, G. Schneider, and J. Hussong, “Raman Measurements of Cryogenic Injection at Supercritical Pressure,” Heat and Mass Transfer 39(8), 709–719 (2003).
</pre></div>
