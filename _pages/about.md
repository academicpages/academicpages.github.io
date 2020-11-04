---
permalink: /
title: "Overview"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---


My research uses ideas from programming languages to solve problems in
networking, databases, and security. Some specific topics of interest
include language design, semantics, type systems, and mechanized
proof. Recently I've been spending most of my time thinking about how
to design better languages and tools for computer networks.

# News

<ul>
{% for item in site.data.news %}
{% if item.type == "acceptance" %}
<li>[{{item.month}} {{item.year}}] <b>{{ item.name }}</b> accepted to <a href="{{ item.conference_url }}">{{ item.conference }}</a>.</li>
{% endif %}
{% endfor %}
</ul>

# Current Projects

<div class="container">
<div class="box-6">
<img src="images/petr4-logo.png" alt="Petr4 logo" /><br />
<p>Petr4: Formal Foundations for P4 Data Planes</p>
</div>
<div class="box-6">
<img src="images/pronto-logo.png" alt="Pronto logo" /><br />
<p>Pronto: Verifiable Closed-Loop Control for Next-Generation Networks</p>
</div>
</div>
<div class="container">
<div class="box-6">
<img src="images/netkat-logo.png" alt="NetKAT logo" /><br />
<p>NetKAT: Algebraic and Coalgebraic Foudnations for Programmable Networks</p>
</div>
<div class="box-6">
<img src="images/neptune-logo.png" alt="Neptune logo" /><br />
<p>Neptune: Programming System for Heterogeneous Architectures</p>
</div>
</div>
<br />

[npi]: https://network-programming.org
