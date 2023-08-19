+++
title = "Selected Projects"

description = ""
sort_by = "none"
weight = 0
render = true
redirect_to = ""
transparent = false

[extra]
+++
### DECaPS2: The Dark Energy Camera Plane Survey DR2
<div id="aladin-lite-div" style="width:800px;height:200px;"></div>
<script type="text/javascript" src="https://aladin.cds.unistra.fr/AladinLite/api/v3/latest/aladin.js" charset="utf-8"></script>
<script type="text/javascript">
let aladin;
A.init.then(() => {
    aladin = A.aladin('#aladin-lite-div', {survey: "P/DECaPS/DR2/color", fov:132, cooFrame:"galactic",target: "303 +0", projection: "AIT"});
});
aladin.setBackgroundColor("rgb(0, 0, 0)")
</script>
<br>
<div style="font-size: 18px;">
I led the data reduction for the second and final release of the Dark Energy Camera Plane Survey (DECaPS2). We provide a catalog of 3.32 billion sources in our survey footprint that covers 6.5% of the sky. We developed new methods well-suited to photometry in the Galactic plane, developed improved measures of photometric depth adapted to crowded-fields, and validate our pipeline extensively with synthetic star tests. For more, see our project <a href="http://decaps.skymaps.info/" target="_blank">website</a>. Tip: See how far you can zoom in (be patient).
</div>

### Diffuse Interstellar Band in Gaia DR3 RVS Spectra
<video width="600" height="600" controls>
    <source src="img/localBubble.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

<br>
<div style="font-size: 18px;">
   I developed and applied a new pipeline to the Gaia (DR3) RVS spectra to measure the diffuse interstellar band (DIB) near 862.1 nm. This method marginalized over stellar types, avoiding false detections of stellar residuals as DIB detections, as in the public Gaia catalog. This analysis allowed us to show that there were no statistically significant detections of DIBs in the Local Bubble. For more, see our project <a href="https://faun.rc.fas.harvard.edu/saydjari/GaiaDIB/" target="_blank">website</a>.
</div>


    






