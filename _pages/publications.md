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

<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>

# {% for post in site.publications reversed %}
#  {% include archive-single.html %}
# {% endfor %}

<button onclick="myFunction('2019-04-29-masters_dissertation')" class="w3-button w3-block w3-left-align">
Synthetic Homotopy Theory and Classifying Principal Bundles in Homotopy Type Theory
</button>

<div id="2019-04-29-masters_dissertation" class="w3-container w3-hide">
<p>
My masters dissertation, written over the course of Hilary Term 2019. It introduces homotopy type theory and looks at doing _synthetic_ homotopy theory, focussing particularly on the theory of fibre bundles. The main result is a proof in homotopy type theory of a theorem originally due to Gottlieb about the homotopy groups of the space $Map(X, K(G,1))$ of maps from a base space $X$ into the classifying space of a discrete group $G$.

Submitted in April 2019 - Copy to be uploaded after assessment
</p>
</div>

<script>
function myFunction(id) {
  var x = document.getElementById(id);
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}
</script>
