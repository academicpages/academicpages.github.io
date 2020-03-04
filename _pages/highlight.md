---
title: "Splash Page"
layout: splash
permalink: /highlight/
author_profile: false
sidebar:
  nav: "sidenav"
toc: true
date: 2020-03-04


feature_row1:
  - image_path: ../images/highlight-image-01.png
    alt: "OH trend"
    title: "Atmospheric oxidising capability"
    excerpt: 'The hydroxyl radical ([OH](https://en.wikipedia.org/wiki/Hydroxyl_radical)) is a highly reactive constituent of the atmosphere. It is thought to be the "detergent" of the troposphere because it reacts with many pollutants and greenhouse gases like methane and ozone. As such, it has a big impact on global climate. Our latest study from the AerChemMIP joint analysis shows that the global OH changed little from 1850 up to around 1980, then increased by around 10 %, with an associated reduction in methane lifetime. However, this seems to be contradicating those derived from inversions of methyl chloroform measurement. '
    url: "https://www.atmos-chem-phys-discuss.net/acp-2019-1219/"
    btn_label: "Read More"
    btn_class: "btn--primary"
feature_row2:
  - image_path: /assets/images/unsplash-gallery-image-2-th.jpg
    alt: "placeholder image 2"
    title: "Placeholder Image Right Aligned"
    excerpt: 'This is some sample content that goes here with **Markdown** formatting. Right aligned with `type="right"`'
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--primary"
feature_row3:
  - image_path: /assets/images/unsplash-gallery-image-2-th.jpg
    alt: "placeholder image 2"
    title: "Placeholder Image Center Aligned"
    excerpt: 'This is some sample content that goes here with **Markdown** formatting. Centered with `type="center"`'
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--primary"
---


{% include feature_row id="feature_row1" type="left" %}

{% include feature_row id="feature_row2" type="right" %}

{% include feature_row id="feature_row3" type="center" %}
