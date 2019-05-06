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

<link rel="stylesheet" href="{{ site.baseurl }}/assets/vallenato/vallenato.css">
<script src="{{ site.baseurl }}/assets/js/vendor/jquery/jquery-1.12.4.min.js"></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
<script src="{{ site.baseurl }}/assets/vallenato/vallenato.js"></script>

<div class="vallenato">
	<div class="vallenato-header">
		Synthetic Homotopy Theory and Classifying Principal Bundles in Homotopy Type Theory
	</div><!--/.vallenato-header-->

	<div class="vallenato-content">
		<p>My masters dissertation, written over the course of Hilary Term 2019. It introduces homotopy type theory and looks at doing synthetic_ homotopy theory, focussing particularly on the theory of fibre bundles. The main result is a proof in homotopy type theory of a theorem originally due to Gottlieb about the homotopy groups of the space $Map(X, K(G,1))$ of maps from a base space $X$ into the classifying space of a discrete group $G$.</p>
    <p>Submitted in April 2019 - Copy to be uploaded after assessment</p>
	</div><!--/.vallenato-content-->
  
</div><!--/.vallenato-->

<script>
	$(document).ready(function() {
		vallenato();
	});
</script>
