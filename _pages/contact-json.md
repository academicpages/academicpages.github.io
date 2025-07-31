---
layout: archive
title: "Contact Me"
permalink: /contact/
author_profile: false
redirect_from:
  - /resume-json
---

{% include base_path %}

<link rel="stylesheet" href="{{ base_path }}/assets/css/cv-style.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<style>
  .archive {
    width: 80%;
    margin: 0 auto;
    float: none;
    padding-right: 0;
  }
  
  @media (min-width: 80em) {
    .archive {
      width: 70%;
    }
  }

  .cv-section {
    line-height:1.8em;
  }

  .cv-download-links {
    margin-top:-0.6em;
    line-height:1.5em;
  }

  .page__title {
    margin-bottom:0.75em;
  }
</style>

{% include contact-template.html %}

<div class="cv-download-links">
  <a href="{{ base_path }}/files/cv.pdf" class="btn btn--primary">Download CV as PDF</a>
  <a href="{{ base_path }}" class="btn btn--inverse">View Markdown CV</a>
</div>
