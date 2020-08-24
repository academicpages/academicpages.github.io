---
title: "Expressive Body Capture: 3D Hands, Face, and Body from a Single Image"
authors: 'Georgios Pavlakos*, Vasileios Choutas*, Nima Ghorbani, Timo Bolkart, Ahmed A. A. Osman, Dimitrios Tzionas, Michael J. Black'
venue: 'Proceedings IEEE Conference on Computer Vision and Pattern Recognition (CVPR)'
date: 2019-06-16
category: 'accepted'
pdf: 'https://ps.is.tuebingen.mpg.de/uploads_file/attachment/attachment/497/SMPL-X.pdf'
teaser: '2019-Expressive-Capture.png'
bibtex: '2019-Expressive-Capture.bib'
permalink: /publication/2019-Expressive-Capture
collection: publications
projectpage: 'https://smpl-x.is.tue.mpg.de/'
youtube: 'https://www.youtube.com/watch?time_continue=1&v=XyXIEmapWkw'
codepage: 'https://github.com/nghorbani/human_body_prior'
---

Abstract
-------
To facilitate the analysis of human actions, interactions and emotions, we compute a 3D model of human body pose, hand pose, and facial expression
from a single monocular image. To achieve this, we use thousands of 3D scans to train a new, unified, 3D model of the human body, SMPL-X, that
extends SMPL with fully articulated hands and an expressive face. Learning to regress the parameters of SMPL-X directly from images is 
challenging without paired images and 3D ground truth. Consequently, we follow the approach of SMPLify, which estimates 2D features and then 
optimizes model parameters to fit the features. We improve on SMPLify in several significant ways: (1) we detect 2D features corresponding
to the face, hands, and feet and fit the full SMPL-X model to these; (2) we train a new neural network pose prior using a large MoCap dataset;
(3) we define a new interpenetration penalty that is both fast and accurate; (4) we automatically detect gender and the appropriate body models (male, female, or neutral);
(5) our PyTorch implementation achieves a speedup of more than 8x over Chumpy. We use the new method, SMPLify-X, to fit SMPL-X to both controlled images and 
images in the wild. We evaluate 3D accuracy on a new curated dataset comprising 100 images with pseudo ground-truth. This is a step towards automatic expressive 
human capture from monocular RGB data. The models, code, and data are available for research purposes at https://smpl-x.is.tue.mpg.de.
