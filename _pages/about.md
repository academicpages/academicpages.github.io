---
permalink: /
title: "Home"
excerpt: "Home"
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
Formal Foundations for Programmable Data Planes
</div>
<div class="box-6">
<img src="images/pronto-logo.png" alt="Pronto logo" /><br />
Verifiable Closed-Loop Control for Next-Generation Networks
</div>
</div>
<div class="container">
<div class="box-6">
<img src="images/netkat-logo.png" alt="NetKAT logo" /><br />
(Co)-Algebraic Foundations for Programmable Networks
</div>
<div class="box-6">
<img src="images/neptune-logo.png" alt="Neptune logo" /><br />
Flexibility, Performance, Consistency for Heterogeneous Packet-Processing Architectures
</div>
</div>
<br />

[npi]: https://network-programming.org
