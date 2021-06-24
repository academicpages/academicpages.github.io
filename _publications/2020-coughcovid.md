---
title: "Detecting COVID-19 from Breathing and Coughing Sounds using Deep Neural Networks"
collection: publications
permalink: /publication/2020-coughcovid
excerpt: ''
date: 2020/12/29
venue: 'IEEE CBMS'
paperurl: 'https://arxiv.org/pdf/2012.14553.pdf'
biburl: /files/schuller2020detecting.bib
award: 'Best Student Paper Award at The 34th IEEE International Symposium on Computer-Based Medical Systems (CBMS 2021)'
citation: Mina A. Nessiem, Mostafa M. Mohamed, <b>Harry Coppock</b>, Alexander Gaskell, Björn W. Schuller (2020) Detecting COVID-19 from Breathing and Coughing Sounds using Deep Neural Networks <i>IEEE CBMS</i>'
author_profile: false
---
The COVID-19 pandemic has affected the world unevenly; while industrial economies have been able to produce the tests necessary to track the spread of the virus and mostly avoided complete lockdowns, developing countries have faced issues with testing capacity. In this paper, we explore the usage of deep learning models as a ubiquitous, low-cost, pre-testing method for detecting COVID-19 from audio recordings of breathing or coughing taken with mobile devices or via the web. We adapt an ensemble of Convolutional Neural Networks that utilise raw breathing and coughing audio and spectrograms to classify if a speaker is infected with COVID-19 or not. The different models are obtained via automatic hyperparameter tuning using Bayesian Optimisation combined with HyperBand. The proposed method outperforms a traditional baseline approach by a large margin. Ultimately, it achieves an Unweighted Average Recall (UAR) of 74.9%, or an Area Under ROC Curve (AUC) of 80.7% by ensembling neural networks, considering the best test set result across breathing and coughing in a strictly subject independent manner. In isolation, breathing sounds thereby appear slightly better suited than coughing ones (76.1% vs 73.7% UAR).

**Best Student Paper Award**, 34th IEEE International Symposium on Computer-Based Medical Systems (CBMS 2021), Mina A. Nessiem, Mostafa M. Mohamed, Harry Coppock, Alexander Gaskell, Björn W. Schuller, “Detecting COVID-19 from Breathing and Coughing Sounds using Deep Neural Networks,” IEEE Technical Committee on Computational Life Science (TCCLS), online, 07.-09.06.2021.

[Download paper here](https://arxiv.org/pdf/2012.14553.pdf)

<details closed>
<summary>Bibtex Entry</summary>
<code>
<pre>
@misc{nessiem2020detecting,
      title={Detecting COVID-19 from Breathing and Coughing Sounds using Deep Neural Networks}, 
      author={Mina A. Nessiem and Mostafa M. Mohamed and Harry Coppock and Alexander Gaskell and Björn W. Schuller},
      year={2020},
      journal={IEEE CBMS}
}
</pre>
</code>
</details>