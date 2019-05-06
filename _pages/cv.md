---
title: "CV"
layout: archive
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<div class="{{ include.type | default: "list" }}__item">
<iframe
    src="{{ site.baseurl }}/assets/pdfviewer/web/viewer.html?file={{ site.url | cgi_escape }}/files/cv/cv.pdf#pagemode=none"
    width="100%"
    height="700vh"
    style="border: none;" />
</div>
