---
permalink: /
title: "Andrew Saydjari"
excerpt: "About"
author_profile: true
redirect_from:
  - /about/
  - /about.html
  - /resume
  - /cv
  - /publications
---

I am a 5th year graduate student at Harvard in the Physics Department working on the intersection of machine learning, astrostatistics, and the interstellar medium. My Ph.D. advisor is [Douglas Finkbeiner](https://faun.rc.fas.harvard.edu/nebel/dfink/){:target="_blank"}.

I am passionate about scientific communication, open source software/data availability, and the replication crisis. I am also a Julia enthusiast. Please reach out to me for any questions related to my research and explore the site!

In previous lives, I have also been a synthetic chemist, chemical spectroscopist, fabrication engineer, and dilution refrigerator operator and have deeply loved each of these roles.

# CV

Here is the most recent version of my [CV](http://andrew-saydjari.github.io/files/CV_saydjari.pdf){:target="_blank"}.

# Publications

You can find a current list of my articles on [NASA/ADS](https://ui.adsabs.harvard.edu/search/filter_doctype_facet_hier_fq_doctype=AND&filter_doctype_facet_hier_fq_doctype=doctype_facet_hier%3A%220%2FArticle%22&fq=%7B!type%3Daqp%20v%3D%24fq_doctype%7D&fq_doctype=(doctype_facet_hier%3A%220%2FArticle%22)&p_=0&q=%20author%3A%22saydjari%2C%20andrew%22&sort=date%20desc%2C%20bibcode%20desc){:target="_blank"}.

<h1 style="text-align: center;">Projects</h1>

## DECaPS2: The Dark Energy Camera Plane Survey DR2

<div id="aladin-lite-div" style="width:800px;height:200px;"></div>
<script type="text/javascript" src="https://aladin.cds.unistra.fr/AladinLite/api/v3/latest/aladin.js" charset="utf-8"></script>
<script type="text/javascript">
let aladin;
A.init.then(() => {
    aladin = A.aladin('#aladin-lite-div', {survey: "P/DECaPS/DR2/color", fov:132, cooFrame:"galactic",target: "303 +0", projection: "AIT"});
});
</script>
<br>
I led the data reduction for the second and final release of the Dark Energy Camera Plane Survey (DECaPS2). We provide a catalog of 3.32 billion sources in our survey footprint that covers 6.5% of the sky. We developed new methods well-suited to photometry in the Galactic plane, developed improved measures of photometric depth adapted to crowded-fields, and validate our pipeline extensively with synthetic star tests. For more, see our project [website](http://decaps.skymaps.info/).

## Diffuse Interstellar Band in Gaia DR3 RVS Spectra
<div style="width:100%; padding-bottom:100%; padding-right:130%; position:relative;">
  <iframe src="https://faun.rc.fas.harvard.edu/saydjari/GaiaDIB/img/DIB_Local_Bubble_SNR_3D.html" style="position:absolute; top:0px; left:0px;
    width:100%; height:100%; border: none; align: center">
  </iframe>
</div>

<br>
I developed and applied a new pipeline to the Gaia (DR3) RVS spectra to measure the diffuse interstellar band (DIB) near 862.1 nm. This method marginalized over stellar types, avoiding false detections of stellar residuals as DIB detections, as in the public Gaia catalog. This analysis allowed us to show that there were no statistically significant detections of DIBs in the Local Bubble. For more, see our project [website](https://faun.rc.fas.harvard.edu/saydjari/GaiaDIB/).
