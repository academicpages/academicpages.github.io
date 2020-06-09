---
permalink: /f2mf/
<!-- author_profile: false -->
title: "
	<center>Warp to the Future:</center>
	<center>Joint Forecasting of Features and Feature Motion</center>"
---
<div align="center" markdown="1">
[Josip Šarić](https://scholar.google.com/citations?user=pPaDpsEAAAAJ&hl=hr&oi=ao "Google Scholar"), [Marin Oršić](https://scholar.google.com/citations?user=DWSB7oMAAAAJ&hl=hr "Google Scholar"), [Tonći Antunović](https://scholar.google.com/citations?hl=hr&user=yRIHOmEAAAAJ&view_op=list_works&sortby=pubdate "Google Scholar"), [Sacha Vražić](https://scholar.google.com/citations?user=cG6s5VMAAAAJ&hl=hr&oi=ao "Google Scholar"), [Siniša Šegvić](https://scholar.google.com/citations?user=_nGQT0wAAAAJ&hl=hr&oi=ao "Google Scholar")

*IEEE Conference on Computer Vision and Pattern Recognition 2020*  
\[[paper]()\] \[[video]()\] \[[presentation]()\]
</div>
---
<div align="center">
	<img src="/images/f2mf_model.png" width="600">
	<p style="font-size:16px;text-align:justify;padding-top: 25px">
		We address anticipation of scene development by forecasting semantic segmentation of future frames. 
		Several previous works approach this problem by F2F (feature-to-feature) forecasting where future features are regressed from observed features.
		Different from previous work, we consider a novel F2M (feature-to-motion) formulation, which performs the forecast by warping observed features according to regressed feature flow.
		This formulation models a causal relationship between the past and the future, and regularizes inference by reducing dimensionality of the forecasting target.
		However, emergence of future scenery which was not visible in observed frames can not be explained by warping.
		We propose to address this issue by complementing F2M forecasting with the classic F2F approach.
		We realize this idea as a multi-head F2MF model built a top shared features.
		Experiments show that the F2M head prevails in static parts of the scene while the F2F head kicks-in to fill-in the novel regions.
		The proposed F2MF model operates in synergy with correlation features and outperforms all previous approaches both in short-term and mid-term forecast on the Cityscapes dataset.
	</p>
</div>

