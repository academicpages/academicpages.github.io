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
  - image_path: ../images/images/highlight-image-01.png
    alt: "OH trend"
    title: "Atmospheric oxidising capability"
    excerpt: 'This is some sample content that goes here with **Markdown** formatting. Left aligned with `type="left"`'
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
