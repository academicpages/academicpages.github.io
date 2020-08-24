---
title: "AMASS: Archive of Motion Capture as Surface Shapes"
authors: 'Naureen Mahmood, Nima Ghorbani, Nikolaus F. Troje, Gerard Pons-Moll, Michael J. Black'
venue: 'Proceedings IEEE Conference on Computer Vision (ICCV)'
date: 2019-10-01
category: 'accepted'
pdf: 'http://files.is.tue.mpg.de/black/papers/amass.pdf'
teaser: '2019-AMASS.png'
bibtex: '2019-AMASS.bib'
permalink: /publication/2019-AMASS
collection: publications
projectpage: 'https://amass.is.tue.mpg.de/'
youtube: 'https://www.youtube.com/watch?v=cceRrlnTCEs'
codepage: 'https://github.com/nghorbani/amass'
---

Abstract
-------
Large datasets are the cornerstone of recent advances
in computer vision using deep learning. In contrast, existing human motion capture (mocap) datasets are small
and the motions limited, hampering progress on learning
models of human motion. While there are many different
datasets available, they each use a different parameterization of the body, making it difficult to integrate them into a
single meta dataset. To address this, we introduce AMASS,
a large and varied database of human motion that unifies
15 different optical marker-based mocap datasets by representing them within a common framework and parameterization. We achieve this using a new method, MoSh++, that
converts mocap data into realistic 3D human meshes represented by a rigged body model. Here we use SMPL [26],
which is widely used and provides a standard skeletal representation as well as a fully rigged surface mesh. The
method works for arbitrary marker sets, while recovering
soft-tissue dynamics and realistic hand motion. We evaluate
MoSh++ and tune its hyperparameters using a new dataset
of 4D body scans that are jointly recorded with markerbased mocap. The consistent representation of AMASS
makes it readily useful for animation, visualization, and
generating training data for deep learning. Our dataset is
significantly richer than previous human motion collections,
having more than 40 hours of motion data, spanning over
300 subjects, more than 11000 motions, and is available for
research at https://amass.is.tue.mpg.de/.
