---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<h2>Journal Articles</h2>
<br><strong>Making the environment like a cool thing: Exploring generation Z and millennials engagement with climate change video on YouTube</strong><br>Seelig, M., Shata, A., **Yang, Z.**, Sd, D., Gao, Y., Hu, H. & Yang, J.<br>
<p style="text-align:justify"><b><i>Abstract: </i></b>Regulation needs effective supervision; but regulated entities may deviate with unobserved actions. For identification, we analyze banks, exploiting ECB’s asset quality review (AQR) and supervisory security and credit registers. After AQR announcement, reviewed banks reduce riskier securities and credit (also overall securities and credit supply), with largest impact on riskiest securities (not on riskiest credit), and immediate negative spillovers on asset prices and firm-level credit supply. Exposed (unregulated) nonbanks buy the shed risk. AQR drives the results, not the end-of-year. After AQR compliance, reviewed banks reload riskier securities, but not riskier credit, with medium-term negative firm-level real effects via credit. Results suggest banks mask risk in supervisory audits, especially using liquid securities that are easier to trade, with not only short-term spillovers on asset prices and credit supply, but also with medium-term implications for the real economy, holding important implications for policy.</p><br>



<h2>Book Chapter</h2>
{% for post in site.publications reversed %}
  {% if post.pubtype == 'chapter' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2>Conference Presentations</h2>
{% for post in site.publications reversed %}
  {% if post.pubtype == 'conference' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}

